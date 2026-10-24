#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 wiki 產成靜態 HTML，供瀏覽器本機閱讀。

  python3 tools/build_site.py           # 產到 site/
  python3 tools/build_site.py --fast    # 跳過縮圖（圖已產過時用）

為什麼要有這個：Obsidian 走 X11 轉發會 lag，因為渲染在 Linux 端做。
產成 HTML 之後渲染在 Windows 的瀏覽器做，只有 HTTP 走 SSH，於是不 lag。

本庫的網站是公開的，但**不含全文 PDF**；serve.sh 在本機預覽時只綁 127.0.0.1。
"""
import os, re, sys, json, glob, shutil, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, 'site')
LAYERS = [('sources','來源'), ('topics','主題'), ('concepts','概念'),
          ('entities','實體'), ('synthesis','綜述')]
ROOTDOCS = [('index','索引'), ('numbers','數字登記簿'),
            ('intake','收錄登記簿'), ('log','日誌')]
MAXW = 1400          # 縮圖最大寬度

import markdown

def read(p):
    return open(p, encoding='utf-8').read()

def strip_fm(t):
    m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
    return (t[m.end():], m.group(1)) if m else (t, '')

def short_of(slug, title):
    """側欄／反向連結用的短標籤。來源頁的完整英文題名太長，改用『姓氏 年份 · 關鍵字』。"""
    m = re.match(r'^s-([a-z]+)-(\d{4})-(.+)$', slug)
    if m:
        return f'{m.group(1).capitalize()} {m.group(2)} · {m.group(3).replace("-", " ")}'
    return title

def title_of(t, fm, slug):
    m = re.search(r'^title:\s*(.+)$', fm, re.M)
    if m:
        return m.group(1).strip().strip('"')
    m = re.search(r'^#\s+(.+)$', t, re.M)
    return re.sub(r'[*`]', '', m.group(1)).strip() if m else slug

# ---------- 蒐集頁面 ----------
pages = {}   # slug -> dict
for d, _ in LAYERS:
    for p in sorted(glob.glob(os.path.join(ROOT, 'wiki', d, '*.md'))):
        slug = os.path.basename(p)[:-3]
        raw = read(p); body, fm = strip_fm(raw)
        ti = title_of(body, fm, slug)
        pages[slug] = dict(slug=slug, layer=d, body=body, fm=fm,
                           title=ti, short=short_of(slug, ti), src=p)
for slug, label in ROOTDOCS:
    p = os.path.join(ROOT, slug + '.md')
    if os.path.isfile(p):
        raw = read(p); body, fm = strip_fm(raw)
        ti = title_of(body, fm, label)
        pages[slug] = dict(slug=slug, layer='root', body=body, fm=fm,
                           title=ti, short=label, src=p)

# ---------- 連結圖（供反向連結）----------
back = {s: set() for s in pages}
for s, pg in pages.items():
    for m in re.findall(r'\[\[([^\]|#\n]+)', pg['body']):
        m = m.strip()
        if m in back and m != s:
            back[m].add(s)

# ---------- 轉換 ----------
FENCE = re.compile(r'```mermaid\n(.*?)```', re.S)

def convert(pg):
    t = pg['body']
    holds = []
    def keep(m):
        holds.append(m.group(1))
        return f'\n@@MERMAID{len(holds)-1}@@\n'
    t = FENCE.sub(keep, t)
    # wikilink
    def wl(m):
        tgt, _, alias = m.group(1).partition('|')
        tgt = tgt.strip(); alias = (alias or tgt).strip()
        if tgt in pages:
            return f'<a class="wl" href="{tgt}.html">{html.escape(alias)}</a>'
        return f'<span class="wl-dead" title="頁面不存在">{html.escape(alias)}</span>'
    t = re.sub(r'\[\[([^\]\n]+)\]\]', wl, t)
    t = t.replace('../../assets/', 'assets/').replace('../../papers/', 'papers/')
    h = markdown.markdown(t, extensions=['tables','fenced_code','attr_list',
                                         'sane_lists','footnotes','nl2br'])
    for i, code in enumerate(holds):
        h = h.replace(f'<p>@@MERMAID{i}@@</p>',
                      f'<pre class="mermaid">{html.escape(code)}</pre>')
        h = h.replace(f'@@MERMAID{i}@@',
                      f'<pre class="mermaid">{html.escape(code)}</pre>')
    return h

# ---------- 側欄 ----------
def sidebar(cur):
    out = ['<nav id="side">',
           '<input id="q" placeholder="搜尋全文…" autocomplete="off">',
           '<div id="results"></div>', '<div id="tree">']
    for slug, label in ROOTDOCS:
        if slug in pages:
            k = ' class="cur"' if slug == cur else ''
            out.append(f'<a{k} href="{slug}.html">{label}</a>')
    for d, label in LAYERS:
        ps = sorted((p for p in pages.values() if p['layer'] == d),
                    key=lambda x: x['slug'])
        if not ps: continue
        out.append(f'<div class="grp">{label}<span class="n">{len(ps)}</span></div>')
        for p in ps:
            k = ' class="cur"' if p['slug'] == cur else ''
            out.append(f'<a{k} href="{p["slug"]}.html">'
                       f'<span class="t">{html.escape(p["short"])}</span>'
                       f'<span class="s">{p["slug"]}</span></a>')
    out.append('</div></nav>')
    return '\n'.join(out)

CSS = """
*{box-sizing:border-box} html{font-size:16px}
body{margin:0;display:flex;font-family:-apple-system,"Segoe UI","Microsoft JhengHei",sans-serif;
 background:#fbfbfa;color:#1f2328;line-height:1.85}
#side{width:310px;min-width:310px;height:100vh;overflow:auto;border-right:1px solid #e3e3e0;
 padding:12px;background:#f6f6f4;position:sticky;top:0}
#side input{width:100%;padding:7px 9px;border:1px solid #d6d6d2;border-radius:6px;
 font-size:.86rem;margin-bottom:8px;background:#fff}
#side a{display:block;padding:4px 8px;border-radius:5px;color:#333;text-decoration:none;font-size:.84rem}
#side a:hover{background:#ececea} #side a.cur{background:#e4ebf5;font-weight:600}
#side a .s{display:block;font-size:.7rem;color:#9a9a95;font-family:ui-monospace,monospace}
.grp{margin:12px 0 4px;font-size:.74rem;font-weight:700;color:#8a8a85;letter-spacing:.06em}
.grp .n{float:right;font-weight:400}
#results a{border-left:3px solid #7aa2d2;margin:2px 0;background:#fff}
#results .ctx{display:block;font-size:.72rem;color:#777;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
main{flex:1;min-width:0;padding:34px 46px 100px;max-width:1000px}
h1{font-size:1.85rem;border-bottom:2px solid #e3e3e0;padding-bottom:.3em;margin-top:0}
h2{font-size:1.32rem;margin-top:2em;border-bottom:1px solid #ececeb;padding-bottom:.25em}
h3{font-size:1.1rem;margin-top:1.6em} h4{font-size:1rem;color:#444}
a.wl{color:#2f6fb0;text-decoration:none;border-bottom:1px solid #cfe0f0}
a.wl:hover{background:#eaf2fb} .wl-dead{color:#b04040;border-bottom:1px dotted #d99}
table{border-collapse:collapse;margin:1.1em 0;font-size:.9rem;display:block;overflow-x:auto;max-width:100%}
th,td{border:1px solid #dcdcd8;padding:6px 11px;vertical-align:top}
th{background:#f0f0ed} tr:nth-child(even) td{background:#fafaf8}
blockquote{border-left:4px solid #cfd6de;background:#f4f6f8;margin:1.1em 0;padding:.7em 1.1em;color:#33383d}
code{background:#f0f0ec;padding:.12em .35em;border-radius:4px;font-size:.87em}
pre{background:#f6f6f3;padding:12px;border-radius:7px;overflow-x:auto}
pre code{background:none;padding:0}
img{max-width:100%;height:auto;border:1px solid #e6e6e2;border-radius:6px;display:block;margin:1em 0;cursor:zoom-in}
img.zoom{position:fixed;inset:0;margin:auto;max-width:96vw;max-height:96vh;z-index:99;
 cursor:zoom-out;box-shadow:0 0 0 100vmax rgba(0,0,0,.82);border:none}
.mermaid{background:#fff;border:1px solid #e6e6e2;border-radius:7px;padding:10px}
.meta{font-size:.78rem;color:#8a8a85;font-family:ui-monospace,monospace;margin-bottom:1.4em}
.bl{margin-top:3.5em;border-top:1px solid #e3e3e0;padding-top:1em;font-size:.86rem}
.bl b{color:#8a8a85;font-weight:600;font-size:.78rem;letter-spacing:.05em}
.bl a{margin-right:.55em}
@media(max-width:900px){body{flex-direction:column}#side{width:100%;height:auto;position:static}main{padding:20px}}
"""

JS = """
document.addEventListener('click',e=>{
  if(e.target.tagName==='IMG') e.target.classList.toggle('zoom');
});
let IDX=null;
const q=document.getElementById('q'), res=document.getElementById('results'), tree=document.getElementById('tree');
async function idx(){ if(!IDX) IDX=await (await fetch('search.json')).json(); return IDX; }
let tmr;
q.addEventListener('input',()=>{clearTimeout(tmr);tmr=setTimeout(run,140)});
async function run(){
  const s=q.value.trim();
  if(s.length<1){res.innerHTML='';tree.style.display='';return}
  tree.style.display='none';
  const data=await idx(); const low=s.toLowerCase(); const out=[];
  for(const p of data){
    let sc=0, ctx='';
    if(p.title.toLowerCase().includes(low)) sc+=100;
    if(p.slug.includes(low)) sc+=60;
    const i=p.text.toLowerCase().indexOf(low);
    if(i>=0){ sc+=10; ctx=p.text.slice(Math.max(0,i-28), i+52); }
    if(sc) out.push({p,sc,ctx});
  }
  out.sort((a,b)=>b.sc-a.sc);
  res.innerHTML = out.length
    ? out.slice(0,40).map(o=>`<a href="${o.p.slug}.html"><span class="t">${o.p.title}</span>`+
        (o.ctx?`<span class="ctx">…${o.ctx.replace(/</g,'&lt;')}…</span>`:'')+`</a>`).join('')
    : '<div class="ctx" style="padding:6px 8px">沒有結果</div>';
}
q.addEventListener('keydown',e=>{if(e.key==='Escape'){q.value='';run()}});
document.addEventListener('keydown',e=>{
  if(e.key==='/'&&document.activeElement!==q){e.preventDefault();q.focus()}
});
"""

def page_html(pg, has_mermaid):
    body = convert(pg)
    bl = sorted(back.get(pg['slug'], ()))
    blhtml = ''
    if bl:
        links = ' '.join(f'<a class="wl" href="{b}.html">{html.escape(pages[b]["short"])}</a>'
                         for b in bl)
        blhtml = f'<div class="bl"><b>被 {len(bl)} 頁連結</b><br>{links}</div>'
    mer = ('<script src="mermaid.min.js"></script>'
           '<script>mermaid.initialize({startOnLoad:true,theme:"neutral"})</script>'
           ) if has_mermaid else ''
    return f"""<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(pg['title'])}</title><link rel="stylesheet" href="style.css"></head><body>
{sidebar(pg['slug'])}
<main><div class="meta">{pg['layer']} / {pg['slug']}.md</div>
{body}{blhtml}</main>
<script src="app.js"></script>{mer}</body></html>"""

# ---------- 產出 ----------
def main():
    fast = '--fast' in sys.argv
    os.makedirs(SITE, exist_ok=True)
    # 圖：縮到 MAXW 以內
    ad = os.path.join(SITE, 'assets'); os.makedirs(ad, exist_ok=True)
    if not fast:
        from PIL import Image
        tot_in = tot_out = 0
        for p in sorted(glob.glob(os.path.join(ROOT, 'assets', '*'))):
            o = os.path.join(ad, os.path.basename(p))
            tot_in += os.path.getsize(p)
            try:
                im = Image.open(p)
                if im.width > MAXW:
                    im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
                if im.mode in ('RGBA','P') and o.lower().endswith(('.jpg','.jpeg')):
                    im = im.convert('RGB')
                im.save(o, quality=86, optimize=True)
            except Exception:
                shutil.copy2(p, o)
            tot_out += os.path.getsize(o)
        print(f'圖：{len(glob.glob(os.path.join(ROOT,"assets","*")))} 張　'
              f'{tot_in/1e6:.1f} MB → {tot_out/1e6:.1f} MB')

    # mb_wiki 是公開網站：**不把 papers/ 放進 site/**，全文由來源頁連到 PMC。
    # 舊版留下的符號連結一併移除，免得部署時把 PDF 帶出去。
    lp = os.path.join(SITE, 'papers')
    if os.path.islink(lp):
        os.unlink(lp)

    ven = os.path.join(ROOT, 'tools', 'vendor', 'mermaid.min.js')
    has_mer = os.path.isfile(ven)
    if has_mer:
        shutil.copy2(ven, os.path.join(SITE, 'mermaid.min.js'))
    open(os.path.join(SITE,'style.css'),'w',encoding='utf-8').write(CSS)
    open(os.path.join(SITE,'app.js'),'w',encoding='utf-8').write(JS)

    search = []
    for slug, pg in pages.items():
        open(os.path.join(SITE, slug + '.html'), 'w', encoding='utf-8').write(
            page_html(pg, has_mer))
        txt = re.sub(r'\s+', ' ', re.sub(r'[#*`>|\-\[\]()]', ' ', pg['body']))
        search.append(dict(slug=slug, title=pg['short'], text=txt[:20000]))
    json.dump(search, open(os.path.join(SITE,'search.json'),'w',encoding='utf-8'),
              ensure_ascii=False)
    print(f'頁面：{len(pages)} 個 → {SITE}/')
    print(f'mermaid：{"已內嵌" if has_mer else "未取得（以程式碼區塊呈現）"}')

if __name__ == '__main__':
    main()
