#!/usr/bin/env bash
# 重建網站並在本機起一個唯讀 HTTP 伺服器。
#
#   ./tools/serve.sh          # 重建 ＋ 啟動（預設 port 8788）
#   ./tools/serve.sh 9000     # 指定 port
#   ./tools/serve.sh --fast   # 跳過縮圖（圖沒動過時快很多）
#
# 本機預覽用，只綁 127.0.0.1。公開網站由 GitHub Pages 部署（見 .github/workflows/pages.yml）。
# 遠端主機上執行時，可用 SSH port forwarding 把這個埠轉到本機。
set -euo pipefail
cd "$(dirname "$0")/.."

PORT=8788
ARGS=()
for a in "$@"; do
  if [[ "$a" =~ ^[0-9]+$ ]]; then PORT="$a"; else ARGS+=("$a"); fi
done

python3 tools/build_site.py "${ARGS[@]+"${ARGS[@]}"}"

echo
echo "→ http://127.0.0.1:${PORT}/index.html"
echo "  Ctrl-C 結束"
echo
exec python3 -m http.server "$PORT" --bind 127.0.0.1 --directory site
