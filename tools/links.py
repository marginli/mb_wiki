#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mb_wiki 內部連結檢查。

  python3 tools/links.py          # 完整報告
  python3 tools/links.py --quiet  # 只在有問題時輸出（給收工前用）

檢查四件事：
  1. 壞連結        [[X]] 指向不存在的頁
  2. 反引號待開頁   wiki/ 頁面「待開頁面：」那一行上的 `X`，但 X 其實已經存在
                   （規則要求改成 [[X]]）。**只查那一行**——log.md 是只追加的歷史紀錄，
                   CLAUDE.md 等規則文件在反引號裡提檔名是正常的，都不算違規。
  3. 孤兒頁        沒有任何入連結的頁
  4. 互指          主題↔來源、主題↔概念/實體 的單向連結
  5. 統計          各層頁數與入連結最少的幾頁

互指不是硬規則，是提示：**主題列了某來源，該來源的「相關」通常也該列回那條主題**
（讀者才能從一篇論文找到它在哪幾條線上）。概念/實體同理——列出「它在哪些主題底下
被討論」是查詞頁的核心功能。判斷仍在人，工具只負責把單向的挑出來。

**會跳過程式碼區塊與行內反引號**——規則文件裡的 `[[頁名]]` 是說明，不是連結。
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAYERS = ['sources', 'topics', 'concepts', 'entities', 'synthesis']
EXTRA = ['index.md', 'numbers.md', 'intake.md', 'log.md', 'CLAUDE.md']

FENCE = re.compile(r'```.*?```', re.S)
INLINE = re.compile(r'`[^`\n]*`')

def strip_code(t):
    """移除程式碼區塊與行內反引號，避免把說明文字誤判成連結。"""
    return INLINE.sub(' ', FENCE.sub(' ', t))

def main():
    quiet = '--quiet' in sys.argv
    pages = {os.path.basename(p)[:-3]
             for L in LAYERS for p in glob.glob(os.path.join(ROOT, 'wiki', L, '*.md'))}
    specials = {os.path.splitext(f)[0] for f in EXTRA}
    known = pages | specials

    files = [p for L in LAYERS for p in sorted(glob.glob(os.path.join(ROOT, 'wiki', L, '*.md')))]
    files += [os.path.join(ROOT, f) for f in EXTRA if os.path.isfile(os.path.join(ROOT, f))]

    bad, stale, inbound = [], [], {p: 0 for p in pages}
    inbound_src = {}
    for f in files:
        rel = os.path.relpath(f, ROOT)
        raw = open(f, encoding='utf-8').read()
        t = strip_code(raw)
        src = os.path.basename(f)[:-3]
        tgts = set()
        for m in set(re.findall(r'\[\[([^\]|#\n]+)', t)):
            m = m.strip()
            if not m:
                continue
            if m not in known:
                bad.append((rel, m))
            elif m in inbound and m != src:
                inbound[m] += 1
                tgts.add(m)
        if src in pages:
            inbound_src[src] = tgts
        # 反引號待開頁面：只查 wiki/ 頁面「待開頁面：」那一行
        # log.md 只追加、規則文件在反引號裡提檔名，都不在規則的適用範圍內
        if rel.startswith('wiki' + os.sep):
            for line in raw.splitlines():
                if '待開頁面' not in line:
                    continue
                for m in set(re.findall(r'`((?:s|e|c|t|syn)-[a-z0-9][a-z0-9.\-]*)`', line)):
                    if m in pages:
                        stale.append((rel, m))

    # 互指
    kind = lambda s: s.split('-')[0]
    oneway = []
    for a in sorted(pages):
        for b_ in sorted(inbound_src.get(a, ())):
            ka, kb = kind(a), kind(b_)
            pair = {ka, kb}
            if pair in ({'t', 's'}, {'t', 'c'}, {'t', 'e'}) and a not in inbound_src.get(b_, ()):
                oneway.append((a, b_))

    problems = len(bad) + len(stale)
    orphans = sorted(k for k, v in inbound.items() if v == 0)

    if quiet and not problems and not orphans:
        return 0

    print(f'頁數：' + '　'.join(
        f'{L} {len(glob.glob(os.path.join(ROOT, "wiki", L, "*.md")))}' for L in LAYERS))
    print()
    print(f'== 壞連結（{len(bad)}）==')
    for f, m in sorted(bad):
        print(f'  ⚠ {f} -> [[{m}]]')
    if not bad:
        print('  無')
    print()
    print(f'== 反引號待開頁面，但該頁已存在（{len(stale)}）==')
    for f, m in sorted(stale):
        print(f'  ⚠ {f} -> `{m}`　應改為 [[{m}]]')
    if not stale:
        print('  無')
    print()
    print(f'== 單向連結（{len(oneway)}）——提示，非錯誤 ==')
    for a, b_ in oneway[:20]:
        print(f'  · {a}  →  {b_}　（{b_} 未回指）')
    if len(oneway) > 20:
        print(f'  …另有 {len(oneway)-20} 組')
    if not oneway:
        print('  無')
    print()
    print(f'== 孤兒頁（{len(orphans)}）==')
    print('  ' + ('、'.join(orphans) if orphans else '無'))
    print()
    print('== 入連結最少的五頁 ==')
    for k, v in sorted(inbound.items(), key=lambda x: x[1])[:5]:
        print(f'  {k:36s} {v}')
    return 1 if (problems or orphans) else 0

if __name__ == '__main__':
    sys.exit(main())
