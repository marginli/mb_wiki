#!/usr/bin/env bash
# 從一份論文 PDF 抽出文字與圖，供 ingest-paper 使用。
# 用法：./extract.sh "papers/檔名.pdf" [輸出目錄]
set -euo pipefail

PDF="${1:?用法: ./extract.sh <PDF 路徑> [輸出目錄]}"
[ -f "$PDF" ] || { echo "找不到檔案：$PDF" >&2; exit 1; }

BASE=$(basename "$PDF" .pdf)
SLUG=$(echo "$BASE" | tr 'A-Z ' 'a-z-' | tr -cd 'a-z0-9._-' | cut -c1-60)
OUT="${2:-$(dirname "$PDF")/../.cache/$SLUG}"
mkdir -p "$OUT"

echo "→ $OUT"

pdfinfo "$PDF" | sed -n '1,20p' > "$OUT/info.txt"
PAGES=$(awk '/^Pages:/{print $2}' "$OUT/info.txt")

pdftotext -layout "$PDF" "$OUT/text.txt"
pdfimages -list "$PDF" > "$OUT/images-list.txt" 2>/dev/null || true
pdfimages -all -p "$PDF" "$OUT/img" 2>/dev/null || true

# 丟掉小圖（logo、圖示、色塊）：任一邊 < 400 px 即刪
python3 - "$OUT" <<'PY'
import sys, os, glob, re
out = sys.argv[1]
rows = []
lp = os.path.join(out, "images-list.txt")
if os.path.exists(lp):
    for line in open(lp):
        m = re.match(r'\s*(\d+)\s+(\d+)\s+\S+\s+(\d+)\s+(\d+)', line)
        if m:
            rows.append((int(m.group(2)), int(m.group(3)), int(m.group(4))))  # num, w, h
files = sorted(glob.glob(os.path.join(out, "img-*")))
kept = removed = 0
for f in files:
    m = re.search(r'img-\d+-(\d+)\.', os.path.basename(f)) or re.search(r'img-(\d+)\.', os.path.basename(f))
    idx = int(m.group(1)) if m else None
    dims = next((( w,h) for n,w,h in rows if n == idx), None)
    small = (dims and (dims[0] < 400 or dims[1] < 400)) or (not dims and os.path.getsize(f) < 40000)
    if small:
        os.remove(f); removed += 1
    else:
        kept += 1
print(f"圖：保留 {kept} 張，刪掉 {removed} 張小圖")
PY

# 整頁渲染（150 dpi）：複合圖的分格、色階圖例、箭頭標示常是獨立元件，
# pdfimages 抽不到或會被小圖濾網刪掉。整頁渲染是唯一可靠的來源。
pdftoppm -r 150 -jpeg "$PDF" "$OUT/page" 2>/dev/null || true

echo
echo "頁數：${PAGES:-?}    文字：$(wc -c < "$OUT/text.txt") bytes"
echo "整頁渲染：$(ls "$OUT"/page-*.jpg 2>/dev/null | wc -l) 頁（150 dpi）"
echo
echo "── 檢查清單 ─────────────────────────────"

if grep -qiE 'supplement|supporting information|figure S1|table S1' "$OUT/text.txt"; then
  echo "  ✓ 文字裡有補充資料的痕跡（Supplement / Figure S1 / Table S1）"
  echo "    → 確認方法參數是否在附錄。方法參數多半只在附錄。"
else
  echo "  ⚠ 文字裡找不到補充資料。**這份 PDF 可能不含 SM——跟人類要。**"
  echo "    Chiang 2011 的熱休克時間、物鏡 NA、體素大小、演算法步驟，正文一句都沒有。"
fi

echo "  □ 逐張用 Read 看過 $OUT/img-*    ← pdftotext 抽不出圖，不能只讀文字層"
echo "  □ **複合圖改用整頁渲染**：img-* 若缺分格標籤／色階圖例／箭頭，看 page-N.jpg"
echo "     入庫前以 300 dpi 重繪該頁再裁切，作法見 reference/page-spec.md 第三節"
echo "  □ 挑出的圖複製到 assets/，改名 <姓氏><年份>-figN.jpg"
echo "  □ 讀 reference/page-spec.md 再動筆"
echo "  □ 跟人類討論 3–5 個關鍵發現，停下來等回應"
