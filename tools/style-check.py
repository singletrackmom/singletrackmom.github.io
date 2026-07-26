#!/usr/bin/env python3
"""
Style-guide checker for singletrackmom.github.io.
Scans every page reachable from index.html and flags the recurring violations:
  - pill buttons on portfolio pages (class="links" pill links)
  - anything between the hero image and Goal on overview pages
  - purple headings / purple uppercase labels (purple is links ONLY)
  - faux headings (a <p> standing in for a real <h2>/<h3>)
  - non-green bullet markers
Apps, the design-history tool, family pages, and the private dashboard keep their
own interface and are skipped where noted.
Run:  python3 tools/style-check.py
"""
import re, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

OWN_INTERFACE = ('render/', 'copamigo/', 'wayfinder/', 'syllabus-checker/', 'course-dialer/',
                 'command/', 'flow/', 'focus/', 'soar/', 'summerwork/', 'devan/', 'roughcut/',
                 'scrum/', 'wgu/', 'mines/', 'jobs/', 'canvas/design-history/')

def is_app(f): return any(f.startswith(p) for p in OWN_INTERFACE)

def links_in(f):
    try: s = open(f, encoding='utf-8', errors='ignore').read()
    except: return []
    out = []
    for h in re.findall(r'href="([^"]+)"', s):
        if h.startswith(('http', '#', 'mailto', 'tel')) or h.endswith(
            ('.css', '.png', '.jpg', '.jpeg', '.svg', '.ico', '.xml', '.webmanifest', '.pdf', '.zip')):
            continue
        h = h.split('#')[0].split('?')[0]
        if not h: continue
        p = os.path.normpath(os.path.join(os.path.dirname(f), h)) if not h.startswith('/') else h.lstrip('/')
        if p == '' or p.endswith('/'): p = os.path.join(p, 'index.html')
        if not p.endswith('.html') and os.path.isdir(p): p = os.path.join(p, 'index.html')
        out.append(p)
    return out

def reachable():
    seen = {'index.html'}; frontier = ['index.html']
    for _ in range(3):
        nxt = []
        for f in frontier:
            for p in links_in(f):
                if p not in seen and os.path.exists(p):
                    seen.add(p); nxt.append(p)
        frontier = nxt
    return sorted(seen)

def body_of(s): return s.split('</head>', 1)[-1] if '</head>' in s else s

viol = {}
def add(f, msg): viol.setdefault(f, []).append(msg)

for f in reachable():
    s = open(f, encoding='utf-8', errors='ignore').read()
    style = s.split('</head>', 1)[0]
    b = body_of(s)

    # 1) pill buttons on portfolio pages
    if not is_app(f):
        if re.search(r'<div class="links">\s*<a', b):
            add(f, 'PILL: <div class="links"> pill link (portfolio pages have no pills)')

    # 2) anything between hero image and Goal on overview pages
    if f.endswith('overview.html') and not is_app(f):
        m = re.search(r'(hero-media"[^>]*>.*?</div>|</figure>)(.*?)<h2', b, re.S)
        if m:
            between = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(2))).strip()
            if between and len(between) > 3:
                add(f, f'HERO->GOAL: text between hero and Goal: "{between[:60]}..."')
            if re.search(r'class="(links|note|cap)"', m.group(2)):
                add(f, 'HERO->GOAL: pill/note/caption element between hero and Goal')

    # 3) purple headings / purple uppercase labels
    for m in re.finditer(r'(?:^|[^.\w])(h[123])(?:\.[\w-]+)?\s*\{([^}]*)\}', style, re.I):
        d = m.group(2).replace(' ', '')
        if 'color:var(--plum' in d or 'color:#7a5080' in d:
            add(f, f'PURPLE HEADING: {m.group(1)} rule is purple (headings are green H2 / grey H3)')
    for m in re.finditer(r'\.([\w-]+)\s*\{([^}]*)\}', style):
        cls, d = m.group(1), m.group(2).replace(' ', '')
        if cls == 'eyebrow': continue
        if 'text-transform:uppercase' in d and ('color:var(--plum' in d or 'color:#7a5080' in d):
            if re.search(r'<[a-z0-9]+ class="[^"]*\b' + re.escape(cls) + r'\b', b):
                add(f, f'PURPLE LABEL: .{cls} uppercase label is purple')

    # 4) faux headings (a <p> standing in for a heading)
    for c in ('subsec', 'sec', 'subsection-label', 'doc-label'):
        if re.search(r'<p[^>]*class="[^"]*\b' + c + r'\b', b) and not is_app(f):
            add(f, f'FAUX HEADING: <p class="{c}"> should be a real <h2>/<h3>')

    # 5) non-green bullets
    if ('<li>' in b or '<li ' in b):
        green = (re.search(r'li::before\{[^}]*content:[^}]*(sage|456546)', s)
                 or re.search(r'li::marker\{[^}]*(sage|456546)', s)
                 or re.search(r'li::marker\{[^}]*var\(--sage', s))
        greymarker = re.search(r'li::marker\{color:var\(--muted\)', s)
        if not green:
            add(f, 'BULLETS: no green bullet rule' + (' (grey ::marker found)' if greymarker else ''))

if not viol:
    print("PASS: no style-guide violations on any page reachable from index.")
else:
    print(f"FOUND {sum(len(v) for v in viol.values())} issue(s) on {len(viol)} page(s):\n")
    for f in sorted(viol):
        print(f"  {f}")
        for m in viol[f]:
            print(f"      - {m}")
