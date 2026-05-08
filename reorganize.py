"""
reorganize.py
1. Creates templates/ directory
2. Moves all 00-title.html … 12-python.html into templates/
3. Fixes image/src paths inside them (static/ -> ../static/)
4. Rewrites index.html to dynamically fetch() each template and assemble
   the full presentation — no content duplication.
"""

import re
import shutil
from pathlib import Path

ROOT      = Path(__file__).parent
TEMPLATES = ROOT / "templates"
TEMPLATES.mkdir(exist_ok=True)

# ── Section files in order ────────────────────────────────────────────────────
SECTION_FILES = [
    "00-title.html",
    "01-linux.html",
    "02-network-basics.html",
    "03-git-github.html",
    "04-jenkins.html",
    "05-cicd.html",
    "06-pipelines.html",
    "07-docker.html",
    "08-kubernetes.html",
    "09-ansible.html",
    "10-terraform.html",
    "11-iac.html",
    "12-python.html",
]

# ── Move & fix image paths ────────────────────────────────────────────────────
print("Moving section files to templates/ …")
for fname in SECTION_FILES:
    src = ROOT / fname
    if not src.exists():
        print(f"  [SKIP] {fname} not found – run split_presentation.py first")
        continue

    content = src.read_text(encoding="utf-8")
    # Fix relative paths: static/ -> ../static/  (images are one level up)
    content = content.replace('src="static/', 'src="../static/')
    content = content.replace("src='static/", "src='../static/")

    dst = TEMPLATES / fname
    dst.write_text(content, encoding="utf-8")
    src.unlink()           # remove from root
    print(f"  {fname} -> templates/{fname}")

# ── Read head/nav/dots from original presentation.html ───────────────────────
print("\nReading presentation.html for styles & nav …")
pres = (ROOT / "presentation.html").read_text(encoding="utf-8")

head_match = re.search(r"(<head>.*?</head>)", pres, re.DOTALL)
head_block  = head_match.group(1) if head_match else "<head></head>"

dot_buttons = re.findall(
    r'(<button class="dot[^"]*" title="[^"]*"></button>)',
    pres
)
# Build full dot list (53 dots) from original nav
all_dots_html = "\n    ".join(dot_buttons)

# ── Write index.html ──────────────────────────────────────────────────────────
print("Writing index.html …")

templates_js = ",\n  ".join(f"'templates/{f}'" for f in SECTION_FILES)

index_html = f"""<!DOCTYPE html>
<html lang="en">
{head_block}
<body>
<div class="deck" id="deck">
  <!-- slides are injected here by JS -->
  <div id="loading" style="
    display:flex;align-items:center;justify-content:center;
    height:100%;flex-direction:column;gap:1rem;color:var(--muted)">
    <div style="font-size:3rem">⚙️</div>
    <p style="font-size:1.1rem">Loading presentation…</p>
  </div>
</div>

<!-- ═══════════════ NAV ═══════════════ -->
<nav class="nav">
  <button class="nbtn" id="btn-prev">&#8592; Prev</button>
  <div class="nav-mid" id="nav-dots">
    <!-- dots injected after load -->
    <span class="ctr" id="ctr">— / —</span>
  </div>
  <button class="nbtn" id="btn-next">Next &#8594;</button>
</nav>

<script>
// Section template files (in order)
const TEMPLATE_FILES = [
  {templates_js}
];

// Full slide dot titles (in presentation order)
const DOT_TITLES = [
  {', '.join(f'"{re.sub(chr(34), chr(39), btn)}"' for btn in [
    re.search(r'title="([^"]*)"', b).group(1) for b in dot_buttons
  ])}
];

let cur = 0;
let slides = [];
let dots   = [];

async function loadPresentation() {{
  const deck   = document.getElementById('deck');
  const navDots = document.getElementById('nav-dots');
  const ctr    = document.getElementById('ctr');
  const prev   = document.getElementById('btn-prev');
  const next   = document.getElementById('btn-next');

  // -- fetch & inject all section slides --
  for (const url of TEMPLATE_FILES) {{
    try {{
      const res  = await fetch(url);
      const text = await res.text();
      const parser = new DOMParser();
      const doc    = parser.parseFromString(text, 'text/html');
      doc.querySelectorAll('section.slide').forEach(sec => {{
        // remove 'active' class — we control that ourselves
        sec.classList.remove('active');
        deck.appendChild(sec);
      }});
    }} catch(e) {{
      console.error('Failed to load', url, e);
    }}
  }}

  // remove loading placeholder
  const loading = document.getElementById('loading');
  if (loading) loading.remove();

  // -- build slides & dots arrays --
  slides = Array.from(deck.querySelectorAll('section.slide'));
  const total = slides.length;

  DOT_TITLES.forEach((title, i) => {{
    const btn = document.createElement('button');
    btn.className = 'dot';
    btn.title = title;
    navDots.insertBefore(btn, document.getElementById('ctr'));
    btn.addEventListener('click', () => go(i));
  }});
  dots = Array.from(navDots.querySelectorAll('.dot'));

  prev.addEventListener('click', () => go(cur - 1));
  next.addEventListener('click', () => go(cur + 1));
  document.addEventListener('keydown', e => {{
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') go(cur + 1);
    if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')   go(cur - 1);
  }});

  function go(n) {{
    if (slides[cur]) slides[cur].classList.remove('active');
    if (dots[cur])   dots[cur].classList.remove('on');
    cur = Math.max(0, Math.min(n, slides.length - 1));
    if (slides[cur]) slides[cur].classList.add('active');
    if (dots[cur])   dots[cur].classList.add('on');
    ctr.textContent = (cur + 1) + ' / ' + slides.length;
    prev.disabled = cur === 0;
    next.disabled = cur === slides.length - 1;
    const body = slides[cur] && slides[cur].querySelector('.s-body');
    if (body) body.scrollTop = 0;
  }}

  go(0);
}}

loadPresentation();
</script>
</body>
</html>"""

(ROOT / "index.html").write_text(index_html, encoding="utf-8")
print("  index.html written")
print("\nDone! Open index.html via a local server (e.g. python -m http.server 8080)")
