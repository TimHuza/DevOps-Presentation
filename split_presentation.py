"""
split_presentation.py
Splits presentation.html into per-topic section files and generates index.html
that assembles all sections back into a single working presentation.
"""

from pathlib import Path
import re

SRC = Path(__file__).parent / "presentation.html"
OUT = Path(__file__).parent

# ── Read source ────────────────────────────────────────────────────────────────
html = SRC.read_text(encoding="utf-8")

# ── Extract <head> block (styles) ─────────────────────────────────────────────
head_match = re.search(r"(<head>.*?</head>)", html, re.DOTALL)
head_block = head_match.group(1) if head_match else "<head></head>"

# ── Extract nav block ─────────────────────────────────────────────────────────
nav_match = re.search(r"(<!-- ═+\s*NAV\s*═+ -->.*?</nav>)", html, re.DOTALL)
nav_block = nav_match.group(1) if nav_match else ""

# ── Extract JS block ──────────────────────────────────────────────────────────
js_match = re.search(r"(<script>.*?</script>)", html, re.DOTALL)
js_block = js_match.group(1) if js_match else ""

# ── Extract all <section …> blocks ────────────────────────────────────────────
sections = re.findall(r"(<section[^>]*>.*?</section>)", html, re.DOTALL)
print(f"Found {len(sections)} slides")

# ── Define topic groups (slide indices, 0-based) ──────────────────────────────
# slide 0 = title, slides 1-6 = linux, etc.
TOPICS = [
    ("00-title",          "DevOps Presentation — Title",     [0]),
    ("01-linux",          "🐧 Linux",                        list(range(1, 7))),
    ("02-network-basics", "🌐 Network Basics",               list(range(7, 12))),
    ("03-git-github",     "🔧 Git & GitHub",                 list(range(12, 18))),
    ("04-jenkins",        "⚙️ Jenkins",                      list(range(18, 22))),
    ("05-cicd",           "🔄 CI/CD",                        list(range(22, 25))),
    ("06-pipelines",      "🔗 Pipelines",                    list(range(25, 29))),
    ("07-docker",         "🐳 Docker",                       list(range(29, 34))),
    ("08-kubernetes",     "☸️ Kubernetes",                   list(range(34, 40))),
    ("09-ansible",        "🤖 Ansible",                      list(range(40, 44))),
    ("10-terraform",      "🏗️ Terraform",                    list(range(44, 47))),
    ("11-iac",            "📦 IaC",                          list(range(47, 49))),
    ("12-python",         "🐍 Python",                       list(range(49, 53))),
]

# Collect ALL dot titles from the nav in order
dot_titles = re.findall(r'<button class="dot[^"]*" title="([^"]*)"', nav_block)

def make_dots(slide_indices):
    """Return nav-mid dot buttons for the given global slide indices."""
    dots_html = []
    for i, idx in enumerate(slide_indices):
        title = dot_titles[idx] if idx < len(dot_titles) else ""
        cls = 'dot on' if i == 0 else 'dot'
        dots_html.append(f'    <button class="{cls}" title="{title}"></button>')
    return "\n".join(dots_html)

# ── Template for each standalone section file ─────────────────────────────────
def build_section_file(filename, title, slide_indices):
    topic_sections = "\n\n".join(sections[i] for i in slide_indices)
    count = len(slide_indices)
    dots_html = make_dots(slide_indices)

    page = f"""<!DOCTYPE html>
<html lang="en">
{head_block}
<body>
<div class="deck">

{topic_sections}

</div><!-- /deck -->

<!-- ═══════════════ NAV ═══════════════ -->
<nav class="nav">
  <button class="nbtn" id="btn-prev">&#8592; Prev</button>
  <div class="nav-mid">
{dots_html}
    <span class="ctr" id="ctr">1 / {count}</span>
  </div>
  <button class="nbtn" id="btn-next">Next &#8594;</button>
</nav>

<script>
const slides = document.querySelectorAll('.slide');
const dots   = document.querySelectorAll('.dot');
const ctr    = document.getElementById('ctr');
const prev   = document.getElementById('btn-prev');
const next   = document.getElementById('btn-next');
let cur = 0;

function go(n){{
  slides[cur].classList.remove('active');
  dots[cur].classList.remove('on');
  cur = Math.max(0, Math.min(n, slides.length - 1));
  slides[cur].classList.add('active');
  dots[cur].classList.add('on');
  ctr.textContent = (cur + 1) + ' / ' + slides.length;
  prev.disabled = cur === 0;
  next.disabled = cur === slides.length - 1;
  const body = slides[cur].querySelector('.s-body');
  if(body) body.scrollTop = 0;
}}

prev.addEventListener('click', () => go(cur - 1));
next.addEventListener('click', () => go(cur + 1));
dots.forEach((d, i) => d.addEventListener('click', () => go(i)));
document.addEventListener('keydown', e => {{
  if(e.key === 'ArrowRight' || e.key === 'ArrowDown') go(cur + 1);
  if(e.key === 'ArrowLeft'  || e.key === 'ArrowUp')   go(cur - 1);
}});
go(0);
</script>
</body>
</html>"""
    path = OUT / f"{filename}.html"
    path.write_text(page, encoding="utf-8")
    print(f"  Wrote {path.name}  ({count} slides)")

# ── Write all section files ───────────────────────────────────────────────────
print("\nWriting section files …")
for (fname, title, indices) in TOPICS:
    build_section_file(fname, title, indices)

# ── Build index.html — all slides combined, identical to presentation.html ────
print("\nWriting index.html …")

# Rebuild full dot list from original nav
all_sections_html = "\n\n".join(sections)
total = len(sections)

index_page = f"""<!DOCTYPE html>
<html lang="en">
{head_block}
<body>
<div class="deck">

{all_sections_html}

</div><!-- /deck -->

{nav_block}

{js_block}
</body>
</html>"""

(OUT / "index.html").write_text(index_page, encoding="utf-8")
print(f"  Wrote index.html  ({total} slides total)")
print("\nDone! ✅")
