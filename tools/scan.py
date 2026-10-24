#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mb_wiki 收錄狀態對帳。

用途：找出 papers/ 裡還沒處理的 PDF，並查核 intake.md 有沒有跟現實脫節。

  python3 tools/scan.py          # 完整報告
  python3 tools/scan.py --todo   # 只列出待處理的 PDF（一行一個）

真相來源有三個，本腳本比對它們：
  1. papers/ 底下實際存在的 PDF
  2. wiki/sources/*.md 的 frontmatter citation 欄裡指向的 PDF（URL 編碼）
  3. intake.md 的登記表

三者不一致就是異常，會被列出來。**不自動修正**——修正要人或 Claude 判斷。

另外做一件對帳做不到的事：**重複偵測**。上面三個來源全部以檔名比對，
所以「同一篇論文換個檔名再丟一次」會乾乾淨淨地被列進待處理。
本腳本改以三個不靠檔名的指紋交叉比對 papers/ 內的每一對 PDF：

  1. 檔案 sha256          → 同一個檔案，只是改名
  2. 首兩頁抽出的 DOI     → 同一篇，但換來源重新下載
  3. pdfinfo 的 Title     → 同一篇，但 DOI 沒印在正文上
  4. 逐頁文字雜湊的重疊率 → 同一篇，且 DOI 與標題**兩道都失效**時的最後一道
                            （掃描版、去識別化的檔）。它也直接抓得到「子集」關係：
                            一份是正文、另一份是正文＋附錄

四者任一成立即列為異常。另有一個不算異常的提示：**首頁正文相似度**
（預印本 vs 正式版、v1 vs v2 這種「同一篇但不是同一版」抓得到，DOI 卻不同）。
指紋存在 .cache/fingerprints.json，以檔名＋大小＋mtime＋指紋版本為鍵，檔案沒動就不重算。
"""
import os, re, sys, glob, json, hashlib, subprocess, difflib
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def papers_on_disk():
    d = os.path.join(ROOT, 'papers')
    if not os.path.isdir(d):
        return set()
    return {f for f in os.listdir(d) if f.lower().endswith('.pdf')}

def papers_claimed_by_sources():
    """來源頁 -> 它宣稱對應的 PDF 檔名集合。

    一頁通常只對一份 PDF，但**補充材料另成一檔時，同一頁會對到兩份**
    （2026-09-15 起：Ito 2014 的正文與 85 頁補充材料）。因此回傳集合而非單值；
    找不到任何連結時回傳空集合。

    mb_wiki：本庫是公開網站，citation 連到 PMC 等免費全文，不連本機 PDF。
    本機檔名改寫在 frontmatter 之後的隱藏註解 `<!-- 本機 PDF：papers/<URL 編碼檔名> -->`，
    一份 PDF 一行。GitHub 與網站都不顯示註解，對帳仍能比對三個真相來源。
    citation 裡若仍有 papers/ 連結（母庫格式）也照樣讀。
    """
    out = {}
    for p in sorted(glob.glob(os.path.join(ROOT, 'wiki', 'sources', '*.md'))):
        slug = os.path.basename(p)[:-3]
        t = open(p, encoding='utf-8').read()
        hits = re.findall(r'<!--\s*本機 PDF[:：]\s*papers/(\S+?\.pdf)\s*-->', t, re.I)
        m = re.search(r'^citation:.*$', t, re.M)
        if m:
            hits += re.findall(r'papers/([^)\s]+\.pdf)', m.group(0), re.I)
        out[slug] = {unquote(h) for h in hits}
    return out

def intake_rows():
    """intake.md 的表格列 -> (pdf, 狀態, 來源頁, 領域, 日期)"""
    p = os.path.join(ROOT, 'intake.md')
    rows = []
    if not os.path.isfile(p):
        return rows
    for line in open(p, encoding='utf-8'):
        if not line.lstrip().startswith('| `'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 2:
            continue
        pdf = cells[0].strip('`')
        if not pdf.lower().endswith('.pdf'):
            continue          # 只認 PDF 列，避開文件裡其他有反引號的表格
        status = cells[1]
        src = re.sub(r'^\[\[|\]\]$', '', cells[2]) if len(cells) > 2 else ''
        domain = cells[3] if len(cells) > 3 else ''
        date = cells[4] if len(cells) > 4 else ''
        rows.append((pdf, status, src, domain, date))
    return rows

# ── 重複偵測 ────────────────────────────────────────────────────────────
# 上面的對帳全部以檔名為鍵，抓不到「同一篇論文換個檔名再丟一次」。
# 下面三個指紋都不看檔名。

CACHE = os.path.join(ROOT, '.cache', 'fingerprints.json')
FP_VERSION = 'v3'          # 指紋格式版本。改了要一併改，否則會讀到舊快取
DOI_RE = re.compile(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+')

# 逐頁雜湊的兩個門檻
PAGE_MIN_WORDS = 120       # 少於這麼多詞的頁（純圖、扉頁）不列入比對
SKETCH_K = 96              # 每頁保留的詞組雜湊個數
PAGE_SIM = 0.60            # 兩頁 Jaccard ≥ 此值＝視為同一頁
PAGE_HARD = 0.80           # 重疊率 ≥ 此值＝同一篇，列為異常
PAGE_SOFT = 0.50           # 介於兩者之間＝提示


def _norm(s):
    """壓成只剩小寫英數與單一空白，供比對用。"""
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9]+', ' ', (s or '').lower())).strip()


def _pdf_text(path, last_page):
    """抽出文字。last_page=None 代表整份（頁與頁之間以 \\f 分隔）。"""
    cmd = ['pdftotext', path, '-'] if last_page is None else \
          ['pdftotext', '-f', '1', '-l', str(last_page), path, '-']
    try:
        out = subprocess.run(cmd, capture_output=True, timeout=120)
        return out.stdout.decode('utf-8', 'replace')
    except (OSError, subprocess.SubprocessError):
        return ''


def _pdf_title(path):
    try:
        out = subprocess.run(['pdfinfo', path], capture_output=True, timeout=30)
        for line in out.stdout.decode('utf-8', 'replace').splitlines():
            if line.startswith('Title:'):
                return line.split(':', 1)[1].strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return ''


def _page_sketches(path):
    """每一頁的詞組指紋（bottom-k MinHash）。用來抓「B 的每一頁都在 A 裡」這種子集關係。

    **不用精確雜湊，因為期刊的頁首橫幅會讓它整個失效**——Chiang 2011 的「in press」
    引用行只黏在 41 頁中的 11 頁上（27%），任何「出現在多數頁面才算版面元件」的
    規則都會漏掉它，而它一旦留下，同一篇的兩個版本就沒有任何一頁會相等。

    改為：把每頁切成 8 詞的重疊詞組，取雜湊值最小的 K 個當該頁的指紋。
    二十來個詞的橫幅只佔數百個詞組中的幾個，對 Jaccard 相似度的影響可忽略，
    換行位置不同也不影響。正文太少的頁（純圖頁、扉頁）不列入，它們彼此容易誤撞。
    """
    out = []
    for pg in _pdf_text(path, None).split('\f'):
        words = _norm(pg).split()
        if len(words) < PAGE_MIN_WORDS:
            continue
        shingles = {' '.join(words[k:k + 8]) for k in range(len(words) - 7)}
        hs = sorted(int(hashlib.sha1(s.encode()).hexdigest()[:12], 16) for s in shingles)
        out.append(hs[:SKETCH_K])
    return out


def _sketch_sim(s1, s2):
    """兩頁的 Jaccard 相似度估計（bottom-k 估計量）。"""
    if not s1 or not s2:
        return 0.0
    k = min(len(s1), len(s2), SKETCH_K)
    a, b = set(s1[:k]), set(s2[:k])
    union = sorted(a | b)[:k]
    if not union:
        return 0.0
    return sum(1 for v in union if v in a and v in b) / len(union)


def _page_overlap(fa, fb):
    """(重疊率, 對得上的頁數)。分母取頁數較少的一方，才抓得到子集關係。"""
    pa, pb = fa.get('pages') or [], fb.get('pages') or []
    if not pa or not pb:
        return 0.0, 0
    small, big = (pa, pb) if len(pa) <= len(pb) else (pb, pa)
    hit = sum(1 for s in small if any(_sketch_sim(s, o) >= PAGE_SIM for o in big))
    return hit / len(small), hit


def _fingerprint(path):
    """一份 PDF 的四個指紋。慢的部分（雜湊、pdftotext）由外層快取。"""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)

    dois = sorted({d.rstrip('.,;)').lower() for d in DOI_RE.findall(_pdf_text(path, 2))})

    # 首頁正文：去掉期刊／預印本頁首橫幅那幾行，再壓成 1500 字供相似度比對。
    lines = [l for l in _pdf_text(path, 1).splitlines()
             if not re.search(r'biorxiv|preprint|copyright|creative commons|'
                              r'cc.by|all rights reserved|downloaded from|doi:',
                              l, re.I)]
    head = _norm(' '.join(lines))[:1500]

    return {'sha256': h.hexdigest(), 'dois': dois,
            'title': _norm(_pdf_title(path)), 'head': head,
            'pages': _page_sketches(path)}


def fingerprints(pdfs):
    """{檔名: 指紋}。以檔名＋大小＋mtime 為快取鍵，檔案沒動就不重算。"""
    try:
        cache = json.load(open(CACHE, encoding='utf-8'))
    except (OSError, ValueError):
        cache = {}

    out, dirty = {}, False
    for name in sorted(pdfs):
        path = os.path.join(ROOT, 'papers', name)
        st = os.stat(path)
        key = f'{name}|{st.st_size}|{int(st.st_mtime)}|{FP_VERSION}'
        if key not in cache:
            cache[key] = _fingerprint(path)
            dirty = True
        out[name] = cache[key]

    if dirty:
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        live = {f'{n}|{os.stat(os.path.join(ROOT, "papers", n)).st_size}'
                f'|{int(os.stat(os.path.join(ROOT, "papers", n)).st_mtime)}|{FP_VERSION}'
                for n in pdfs}
        json.dump({k: v for k, v in cache.items() if k in live},
                  open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return out


def duplicates(pdfs, settled=frozenset(), same_source=()):
    """回傳 (未判定的重複, 已判定的重複, 疑似同一篇不同版)，三者皆為 (檔A, 檔B, 理由)。

    `settled` 是登記簿裡已標為「不收錄」的檔名。**一對重複只要有一邊已判定，
    就不再算異常**——`papers/` 是唯讀的，重複檔刪不掉，若不給收斂條件，
    「異常必須為 0」這條收工規則就永遠達不到。判定紀錄留在 intake.md。

    `same_source` 是「由同一個來源頁宣稱」的檔名配對集合。**正文與補充材料的 DOI
    本來就相同**，那不是重複而是同一篇的兩個部分，因此同樣不算異常。
    """
    fp = fingerprints(pdfs)
    names = sorted(fp)
    hard, settled_dups, soft = [], [], []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            fa, fb = fp[a], fp[b]
            why = None
            if fa['sha256'] == fb['sha256']:
                why = '位元組完全相同（只是檔名不同）'
            elif set(fa['dois']) & set(fb['dois']):
                why = f'DOI 相同：{sorted(set(fa["dois"]) & set(fb["dois"]))[0]}'
            elif fa['title'] and fa['title'] == fb['title']:
                why = f'PDF 標題相同：{fa["title"][:60]}'
            # 第四道：逐頁詞組指紋。前三道都失效時（掃描版、去識別化的檔）靠它，
            # 而且**不論是哪一道先命中，它都負責說明兩份的關係是不是「子集」**
            # ——同一篇的兩個檔最常見的差別就是有沒有附錄。
            ov, nshared = _page_overlap(fa, fb)
            if ov >= PAGE_HARD and nshared >= 3:
                na, nb = len(fa['pages']), len(fb['pages'])
                rel = f'逐頁詞組指紋重疊 {ov:.0%}（{nshared} 頁對得上）'
                if na != nb:
                    big, small = (a, b) if na > nb else (b, a)
                    rel += (f'；**{small} 的正文頁全部落在 {big} 裡**，'
                            f'後者另有 {abs(na - nb)} 頁（多半是附錄）')
                why = f'{why}；{rel}' if why else rel
            if why:
                expected = (a in settled or b in settled) or ((a, b) in same_source)
                (settled_dups if expected else hard).append((a, b, why))
                continue

            if ov >= PAGE_SOFT and nshared >= 2:
                soft.append((a, b, f'逐頁詞組指紋重疊 {ov:.0%}（{nshared} 頁對得上）'))
                continue
            if fa['head'] and fb['head']:
                r = difflib.SequenceMatcher(None, fa['head'], fb['head']).ratio()
                if r >= 0.75:
                    soft.append((a, b, f'首頁正文相似度 {r:.2f}（可能是同一篇的不同版本）'))
    return hard, settled_dups, soft


def main():
    todo_only = '--todo' in sys.argv

    disk = papers_on_disk()
    claimed = papers_claimed_by_sources()
    claimed_pdfs = {v for vs in claimed.values() for v in vs}
    # 同一來源頁宣稱的兩份（正文＋補充材料）互為預期，不是重複
    same_source = set()
    for vs in claimed.values():
        for x in sorted(vs):
            for y in sorted(vs):
                if x < y:
                    same_source.add((x, y))
    rows = intake_rows()
    reg = {r[0]: r for r in rows}

    # 待處理＝在 papers/ 裡、沒有來源頁指向它、且登記簿沒把它標為「不收錄」
    excluded = {p for p, st, *_ in rows if st.startswith('不收錄')}
    todo = sorted(disk - claimed_pdfs - excluded)

    hard_dups, settled_dups, soft_dups = duplicates(disk, excluded, same_source)

    if todo_only:
        # --todo 供機器讀，一行一個檔名。重複的警告走 stderr，不污染清單。
        flagged = {a for a, b, _ in hard_dups} | {b for a, b, _ in hard_dups}
        for f in todo:
            print(f)
        for a, b, why in hard_dups:
            print(f'⚠ 疑似重複：{a} ←→ {b}（{why}）', file=sys.stderr)
        if flagged & set(todo):
            print('⚠ 上列待處理檔案中有疑似重複，動手前先跑一次完整 scan.py。', file=sys.stderr)
        return 0

    print(f'庫位置：{ROOT}')
    print(f'papers/ 內 PDF：{len(disk)}　來源頁：{len(claimed)}　登記簿列數：{len(rows)}')
    print()

    print(f'== 待處理（{len(todo)}）==')
    if todo:
        for f in todo:
            note = f'　←登記簿狀態：{reg[f][1]}' if f in reg else '　←登記簿尚未登記'
            print(f'  ! {f}{note}')
    else:
        print('  無。papers/ 裡每一份 PDF 都已收錄或已標為不收錄。')
    print()

    done = sorted((v, k) for k, vs in claimed.items() for v in sorted(vs))
    print(f'== 已收錄（{len(done)}）==')
    for pdf, slug in done:
        mark = '' if pdf in disk else '　⚠ 這份 PDF 在 papers/ 找不到'
        print(f'  - {slug}  ←  {pdf}{mark}')
    print()

    if excluded:
        gone = sorted(f for f in excluded if f not in disk)
        print(f'== 標為不收錄（{len(excluded)}）==')
        for f in sorted(excluded):
            mark = '　（已從 papers/ 移除）' if f in gone else ''
            print(f'  - {f}{mark}')
        if gone:
            print('    ↑ 判定不收錄之後檔案被移除，是預期的收斂結果，不算異常；')
            print('      判定紀錄留在 intake.md，下次同一份再丟進來仍會被攔下。')
        print()

    if hard_dups or settled_dups or soft_dups:
        print(f'== 疑似重複（{len(hard_dups) + len(settled_dups) + len(soft_dups)}）==')
        for a, b, why in hard_dups:
            print(f'  ⚠ {a}')
            print(f'    ←→ {b}')
            print(f'    {why}')
        for a, b, why in settled_dups:
            if (a, b) in same_source:
                tail = '　——同一個來源頁宣稱的正文與補充材料，不是重複'
            else:
                tail = '　——已在登記簿判定為不收錄，不算異常'
            print(f'  ✓ {a}')
            print(f'    ←→ {b}')
            print(f'    {why}{tail}')
        for a, b, why in soft_dups:
            print(f'  ? {a}')
            print(f'    ←→ {b}')
            print(f'    {why}　——提示，非錯誤')
        print()

    # 異常
    problems = []
    for a, b, why in hard_dups:
        problems.append(f'papers/ 內有兩份同一篇：{a} ←→ {b}（{why}）')
    for slug, pdfs in claimed.items():
        if not pdfs:
            problems.append(f'來源頁 {slug} 找不到「本機 PDF」註解（或 citation 裡的 papers/*.pdf 連結）')
        for pdf in sorted(pdfs):
            if pdf not in disk:
                problems.append(f'來源頁 {slug} 指向不存在的 PDF：{pdf}')
    for f in sorted(disk - set(reg)):
        problems.append(f'papers/ 有但登記簿沒登：{f}')
    for pdf, st, src, *_ in rows:
        # 標為「不收錄」的列，檔案從 papers/ 消失是預期的收斂結果，不是脫節：
        # 判定理由留在 intake.md，沒有任何內容跟著檔案一起不見。
        # 其餘狀態（已收錄／待處理／處理中）檔案不見就是真的異常——
        # 「已收錄」尤其嚴重，來源頁的 citation 會指向一個開不起來的 PDF。
        if pdf not in disk and not st.startswith('不收錄'):
            problems.append(f'登記簿有但 papers/ 沒有：{pdf}（狀態：{st}）')
        if st == '已收錄':
            if not src:
                problems.append(f'登記簿標「已收錄」卻沒填來源頁：{pdf}')
            elif pdf not in claimed.get(src, set()):
                problems.append(f'登記簿說 {pdf} → {src}，但該來源頁的 citation 對不上')
    seen = set()
    for pdf, *_ in rows:
        if pdf in seen:
            problems.append(f'登記簿重複列：{pdf}')
        seen.add(pdf)

    print(f'== 異常（{len(problems)}）==')
    if problems:
        for p in problems:
            print(f'  ⚠ {p}')
    else:
        print('  無。papers/、來源頁、登記簿三者一致。')
    return 1 if problems else 0

if __name__ == '__main__':
    sys.exit(main())
