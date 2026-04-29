#!/usr/bin/env python3
"""Generate DevOps Presentation HTML from markdown files."""
import os, re, glob

BASE = os.path.dirname(os.path.abspath(__file__))

SLIDES_CONFIG = [
    ('01-linux.md',         'linux',         '🐧 Linux',          '#f97316'),
    ('02-network-basics.md','network-basics', '🌐 Network Basics',  '#06b6d4'),
    ('03-git-github.md',    'git-github',     '🔧 Git & GitHub',    '#f43f5e'),
]

# ── markdown → HTML ──────────────────────────────────────────────────────────
def escape(s):
    return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def inline(s):
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*(.+?)\*',     r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`',     r'<code>\1</code>', s)
    return s

def parse_table(lines):
    rows = [l.strip().strip('|').split('|') for l in lines if not re.match(r'^\s*\|?[-:| ]+\|?\s*$', l)]
    html = '<div class="table-wrap"><table>'
    for i, row in enumerate(rows):
        tag = 'th' if i == 0 else 'td'
        html += '<tr>' + ''.join(f'<{tag}>{inline(c.strip())}</{tag}>' for c in row) + '</tr>'
    return html + '</table></div>'

def md2html(text, topic):
    lines = text.splitlines()
    out, i = [], 0
    in_ul = in_ol = False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul: out.append('</ul>'); in_ul = False
        if in_ol: out.append('</ol>'); in_ol = False

    while i < len(lines):
        line = lines[i]

        # fenced code block (``` or ````), possibly with lang and id="..."
        if re.match(r'^`{3,}', line):
            lang_match = re.match(r'^`{3,}(\w*)', line)
            lang = lang_match.group(1) if lang_match else ''
            close_lists()
            code_lines = []
            i += 1
            while i < len(lines) and not re.match(r'^`{3,}', lines[i]):
                code_lines.append(escape(lines[i]))
                i += 1
            cls = f'lang-{lang}' if lang else ''
            out.append(f'<pre><code class="{cls}">' + '\n'.join(code_lines) + '</code></pre>')
            i += 1
            continue

        # horizontal rule
        if re.match(r'^-{3,}\s*$', line):
            close_lists()
            out.append('<hr>')
            i += 1
            continue

        # headings
        m = re.match(r'^(#{1,4})\s+(.*)', line)
        if m:
            close_lists()
            level = len(m.group(1))
            text_h = inline(m.group(2))
            out.append(f'<h{level}>{text_h}</h{level}>')
            i += 1
            continue

        # table (line starts with |)
        if line.strip().startswith('|'):
            close_lists()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1
            out.append(parse_table(table_lines))
            continue

        # unordered list
        m = re.match(r'^(\s*)[-*]\s+(.*)', line)
        if m:
            if not in_ul:
                close_lists(); out.append('<ul>'); in_ul = True
            out.append(f'<li>{inline(m.group(2))}</li>')
            i += 1
            continue

        # ordered list
        m = re.match(r'^(\s*)\d+\.\s+(.*)', line)
        if m:
            if not in_ol:
                close_lists(); out.append('<ol>'); in_ol = True
            out.append(f'<li>{inline(m.group(2))}</li>')
            i += 1
            continue

        # tip/note lines (💡 👉 ⚠️ ✅)
        stripped = line.strip()
        if stripped and re.match(r'^(💡|👉|⚠️|✅)', stripped):
            close_lists()
            out.append(f'<div class="tip">{inline(stripped)}</div>')
            i += 1
            continue

        # blank line
        if not stripped:
            close_lists()
            i += 1
            continue

        # paragraph
        close_lists()
        out.append(f'<p>{inline(stripped)}</p>')
        i += 1

    close_lists()
    return '\n'.join(out)

# ── image helpers ─────────────────────────────────────────────────────────────
def topic_images(topic):
    folder = os.path.join(BASE, 'static', 'images', topic)
    if not os.path.isdir(folder):
        return []
    exts = ('*.png','*.jpg','*.jpeg','*.webp','*.gif','*.svg')
    imgs = []
    for ext in exts:
        imgs.extend(glob.glob(os.path.join(folder, ext)))
    return [os.path.basename(p) for p in imgs]

def img_tag(topic, filename, cls='slide-img'):
    path = f'static/images/{topic}/{filename}'
    return f'<img src="{path}" alt="{filename}" class="{cls}" loading="lazy">'

# ── build slides ──────────────────────────────────────────────────────────────
def build_slide(fname, topic, title, color, idx):
    path = os.path.join(BASE, 'content', fname)
    with open(path, encoding='utf-8') as f:
        raw = f.read()

    # Strip preamble text (non-md lines before first heading)
    raw = re.sub(r'^.*?(?=^#)', '', raw, flags=re.DOTALL | re.MULTILINE)

    content_html = md2html(raw, topic)
    imgs = topic_images(topic)

    # Find logo (filename contains 'logo')
    logo = next((x for x in imgs if 'logo' in x.lower()), None)
    other_imgs = [x for x in imgs if x != logo]

    logo_html = img_tag(topic, logo, 'topic-logo') if logo else ''

    # Inject other images as a gallery at bottom of slide
    gallery_html = ''
    if other_imgs:
        gallery_html = '<div class="img-gallery">' + \
            ''.join(img_tag(topic, im) for im in other_imgs) + \
            '</div>'

    return f'''
<section class="slide" id="slide-{idx}" style="--accent:{color}">
  <div class="slide-header">
    <div class="slide-num">0{idx}</div>
    <div class="slide-title-bar">{title}</div>
    {logo_html}
  </div>
  <div class="slide-body">
    {content_html}
    {gallery_html}
  </div>
</section>'''

# ── CSS ───────────────────────────────────────────────────────────────────────
CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0d1117;--surface:#161b22;--border:#30363d;
  --text:#e6edf3;--muted:#8b949e;--accent:#4f46e5;
  --green:#3fb950;--blue:#58a6ff;--yellow:#d29922;--red:#f85149;
}
html,body{height:100%;background:var(--bg);color:var(--text);
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  font-size:16px;overflow:hidden}

/* ── Presentation shell ── */
.presentation{position:relative;width:100vw;height:100vh;overflow:hidden}
.slide{
  position:absolute;inset:0;
  display:none;flex-direction:column;
  overflow:hidden;
  opacity:0;transition:opacity .35s ease;
}
.slide.active{display:flex;opacity:1}
.slide.exit{display:flex;opacity:0}

/* ── Title Slide ── */
.title-slide{
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  height:100%;text-align:center;
  background:linear-gradient(135deg,#0d1117 0%,#161b22 50%,#0d1117 100%);
  padding:2rem;
}
.title-slide h1{
  font-size:clamp(2.5rem,6vw,4.5rem);font-weight:700;
  background:linear-gradient(90deg,#4f46e5,#06b6d4);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  margin-bottom:.5rem;
}
.title-slide .subtitle{font-size:1.25rem;color:var(--muted);margin-bottom:1.5rem}
.title-slide .author{
  font-size:1.1rem;font-weight:600;color:var(--text);
  background:var(--surface);border:1px solid var(--border);
  border-radius:999px;padding:.4rem 1.2rem;margin-bottom:2.5rem;
}
.topics-grid{
  display:grid;grid-template-columns:repeat(3,1fr);gap:.75rem;
  max-width:600px;width:100%;
}
.topic-chip{
  background:var(--surface);border:1px solid var(--border);
  border-radius:8px;padding:.5rem .75rem;font-size:.85rem;
  transition:border-color .2s;cursor:default;
}
.topic-chip:hover{border-color:var(--accent)}
.big-icon{font-size:5rem;margin-bottom:1rem;filter:drop-shadow(0 0 20px rgba(79,70,229,.4))}

/* ── Content Slide ── */
.slide-header{
  display:flex;align-items:center;gap:1rem;
  padding:1rem 2rem;
  background:var(--surface);
  border-bottom:2px solid var(--accent);
  flex-shrink:0;position:relative;
}
.slide-num{
  font-size:1.8rem;font-weight:800;
  background:linear-gradient(90deg,var(--accent),#06b6d4);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  min-width:2.5rem;
}
.slide-title-bar{font-size:1.6rem;font-weight:700;color:var(--text)}
.topic-logo{height:44px;object-fit:contain;margin-left:auto;filter:drop-shadow(0 0 8px rgba(255,255,255,.15))}

.slide-body{
  flex:1;overflow-y:auto;padding:1.5rem 2rem;
  scroll-behavior:smooth;
}
.slide-body::-webkit-scrollbar{width:6px}
.slide-body::-webkit-scrollbar-track{background:transparent}
.slide-body::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}

/* ── Typography ── */
h1{font-size:2rem;font-weight:700;color:var(--text);margin-bottom:1rem;
  background:linear-gradient(90deg,var(--accent),#06b6d4);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;}
h2{font-size:1.4rem;font-weight:600;color:var(--blue);
  margin:1.4rem 0 .6rem;padding-left:.75rem;
  border-left:3px solid var(--accent);}
h3{font-size:1.1rem;font-weight:600;color:var(--text);margin:.9rem 0 .4rem}
h4{font-size:1rem;font-weight:600;color:var(--muted);margin:.6rem 0 .3rem}
p{line-height:1.7;margin-bottom:.6rem;color:#c9d1d9}
strong{color:var(--text);font-weight:600}
em{color:var(--yellow)}
hr{border:none;border-top:1px dashed var(--border);margin:1.2rem 0}
code{
  font-family:'JetBrains Mono',Consolas,'Courier New',monospace;
  font-size:.85em;background:#1f2937;color:#79c0ff;
  padding:.1em .35em;border-radius:4px;
}

/* ── Code blocks ── */
pre{
  background:#161b22;border:1px solid var(--border);border-radius:10px;
  padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;
  position:relative;
}
pre code{
  background:transparent;color:#c9d1d9;padding:0;font-size:.88rem;
  line-height:1.6;
}
.lang-bash pre code,.lang-bash{color:#79c0ff}
.lang-yaml,.lang-yml{color:#7ee787}
.lang-python{color:#ffa657}
.lang-dockerfile{color:#56d364}
.lang-hcl{color:#d29922}

/* ── Lists ── */
ul,ol{margin:.4rem 0 .8rem 1.4rem;color:#c9d1d9}
li{margin:.3rem 0;line-height:1.6}
ul li::marker{color:var(--accent)}
ol li::marker{color:var(--blue);font-weight:600}

/* ── Table ── */
.table-wrap{overflow-x:auto;margin:.8rem 0}
table{border-collapse:collapse;width:100%;font-size:.9rem}
th{background:var(--surface);color:var(--text);font-weight:600;
   padding:.6rem 1rem;border:1px solid var(--border);text-align:left}
td{padding:.55rem 1rem;border:1px solid var(--border);color:#c9d1d9}
tr:nth-child(even) td{background:rgba(255,255,255,.02)}
tr:hover td{background:rgba(79,70,229,.06)}

/* ── Tip / Note ── */
.tip{
  background:rgba(56,189,248,.08);border-left:3px solid #38bdf8;
  border-radius:0 8px 8px 0;padding:.55rem 1rem;margin:.6rem 0;
  color:#7dd3fc;font-size:.95rem;
}

/* ── Images ── */
.slide-img{
  max-width:100%;max-height:280px;border-radius:10px;
  border:1px solid var(--border);object-fit:contain;display:block;
  margin:.75rem auto;
}
.img-gallery{
  display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));
  gap:1rem;margin-top:1.5rem;
}
.img-gallery img{
  width:100%;max-height:220px;object-fit:contain;
  border-radius:10px;border:1px solid var(--border);
  background:var(--surface);padding:.5rem;
}

/* ── Navigation bar ── */
.nav{
  position:fixed;bottom:0;left:0;right:0;
  display:flex;align-items:center;justify-content:space-between;
  padding:.6rem 1.5rem;
  background:rgba(22,27,34,.95);backdrop-filter:blur(10px);
  border-top:1px solid var(--border);
  z-index:100;
}
.nav-btn{
  display:flex;align-items:center;gap:.5rem;
  background:var(--surface);border:1px solid var(--border);
  color:var(--text);padding:.5rem 1.2rem;border-radius:8px;
  font-size:.9rem;font-weight:500;cursor:pointer;
  transition:all .2s;
}
.nav-btn:hover{border-color:var(--accent);color:var(--accent)}
.nav-btn:disabled{opacity:.3;cursor:not-allowed}
.nav-center{display:flex;align-items:center;gap:.6rem;flex-wrap:wrap;justify-content:center}
.slide-counter{font-size:.85rem;color:var(--muted);min-width:60px;text-align:center}
.dot{
  width:8px;height:8px;border-radius:50%;background:var(--border);
  cursor:pointer;transition:all .2s;border:none;
}
.dot.active{background:var(--accent);transform:scale(1.4)}
.dot:hover{background:var(--muted)}
.topic-label{font-size:.75rem;color:var(--muted);font-weight:500}
"""

# ── JavaScript ────────────────────────────────────────────────────────────────
JS = """
const slides = document.querySelectorAll('.slide');
const dots   = document.querySelectorAll('.dot');
const counter= document.getElementById('counter');
const prevBtn= document.getElementById('btn-prev');
const nextBtn= document.getElementById('btn-next');
const topicLbl=document.getElementById('topic-label');
const TOPICS = ['', ...TOPIC_LABELS];
let cur = 0;

function go(n){
  slides[cur].classList.remove('active'); dots[cur].classList.remove('active');
  cur = Math.max(0,Math.min(n,slides.length-1));
  slides[cur].classList.add('active'); dots[cur].classList.add('active');
  counter.textContent = (cur+1)+' / '+slides.length;
  topicLbl.textContent = TOPICS[cur] || '';
  prevBtn.disabled = cur===0;
  nextBtn.disabled = cur===slides.length-1;
}
prevBtn.addEventListener('click',()=>go(cur-1));
nextBtn.addEventListener('click',()=>go(cur+1));
dots.forEach((d,i)=>d.addEventListener('click',()=>go(i)));
document.addEventListener('keydown',e=>{
  if(e.key==='ArrowRight'||e.key==='ArrowDown') go(cur+1);
  if(e.key==='ArrowLeft'||e.key==='ArrowUp')   go(cur-1);
});
go(0);
"""

# ── main ─────────────────────────────────────────────────────────────────────
def main():
    slide_sections = []
    topic_labels   = []

    # Title slide
    topics_chips = ''.join(
        f'<div class="topic-chip">{s[2]}</div>'
        for s in SLIDES_CONFIG
    )
    title_html = f'''
<section class="slide active" id="slide-0">
  <div class="title-slide">
    <div class="big-icon">🚀</div>
    <h1>DevOps Presentation</h1>
    <p class="subtitle">A comprehensive overview of DevOps tools &amp; practices</p>
    <p class="author">👤 Tim Huza</p>
    <div class="topics-grid">
      {''.join(f'<div class="topic-chip">{s[2]}</div>' for s in SLIDES_CONFIG)}
    </div>
  </div>
</section>'''
    slide_sections.append(title_html)
    topic_labels.append('')

    for idx, (fname, topic, title, color) in enumerate(SLIDES_CONFIG, start=1):
        slide_sections.append(build_slide(fname, topic, title, color, idx))
        topic_labels.append(title)

    total = len(slide_sections)
    dots_html = ''.join(f'<button class="dot" title="Slide {i+1}"></button>' for i in range(total))
    topics_js  = '[' + ','.join(f'"{t}"' for t in topic_labels) + ']'

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>DevOps Presentation – Tim Huza</title>
<meta name="description" content="A modern DevOps presentation covering Linux, Networking, Git, Docker, Kubernetes and more.">
<style>{CSS}</style>
</head>
<body>
<div class="presentation">
{''.join(slide_sections)}
</div>
<nav class="nav">
  <button class="nav-btn" id="btn-prev">&#8592; Prev</button>
  <div class="nav-center">
    <span class="topic-label" id="topic-label"></span>
    {dots_html}
    <span class="slide-counter" id="counter">1 / {total}</span>
  </div>
  <button class="nav-btn" id="btn-next">Next &#8594;</button>
</nav>
<script>
const TOPIC_LABELS = {topics_js};
{JS}
</script>
</body>
</html>'''

    out_path = os.path.join(BASE, 'presentation.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'[OK] Generated: {out_path}  ({len(html):,} bytes, {total} slides)')

if __name__ == '__main__':
    main()
