#!/usr/bin/env python3
"""
design-lint.py, the portfolio design-system regression check.

Goal:     make design consistency verifiable instead of promised. Run it, get a
          pass/fail list, fix what it names, run it again.
Audience: Michelle, and any assistant working in this repo.
Process:  reads the locked rules from CLAUDE.md, checks every portfolio HTML page
          against them, prints violations grouped by severity, exits non-zero if
          anything CRITICAL is found.

Usage:  python3 tools/design-lint.py
        python3 tools/design-lint.py --all      (include family/tool pages)

Scope note: family agent pages and tool pages (flow, focus, soar, summerwork,
jobs, command, lunch) are deliberately EXEMPT from portfolio chrome rules.
Their overview.html case-study pages are NOT exempt.
"""
import re, sys, glob, os, io
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

FAMILY_DIRS = ("flow/", "focus/", "soar/", "summerwork/", "jobs/", "command/", "lunch/")
SKIP_DIRS   = ("node_modules/", ".git/")

# TIER 1: the portfolio surface a hiring manager actually sees. Full chrome rules.
PORTFOLIO_ROOT  = ("index.html", "work.html", "about.html")
PORTFOLIO_DIRS  = ("render/", "copamigo/", "course-dialer/", "wayfinder/",
                   "cultivate/", "airc-sss/", "style-guide/")
# TIER 2: course content, Canvas exports, drafts. Universal rules only
# (no em dashes, no gradients, curly quotes). Chrome rules do not apply.
def in_portfolio(f):
    if f in PORTFOLIO_ROOT: return True
    if f.endswith("overview.html"): return True
    if f.endswith("prd.html"): return True
    return f.startswith(PORTFOLIO_DIRS)
ALL = "--all" in sys.argv

issues = defaultdict(list)
def add(sev, f, msg): issues[sev].append((f, msg))

def is_family_tool(f):
    """Family/tool page, exempt from portfolio chrome. overview.html is not exempt."""
    return f.startswith(FAMILY_DIRS) and not f.endswith("overview.html")

def strip_code(s):
    """Remove style/script/tags so we only inspect visible prose."""
    s = re.sub(r'<style.*?</style>', '', s, flags=re.S)
    s = re.sub(r'<script.*?</script>', '', s, flags=re.S)
    s = re.sub(r'<[^>]+>', '', s)
    return s

files = [f for f in sorted(glob.glob("**/*.html", recursive=True))
         if not f.startswith(SKIP_DIRS)]

for f in files:
    try:
        s = io.open(f, encoding='utf-8').read()
    except Exception:
        continue
    fam = is_family_tool(f)
    # redirect stubs are exempt: no body content by design
    if re.search(r'<meta http-equiv="refresh"', s, re.I):
        continue
    prose = strip_code(s)

    # ---------- universal rules (every page, no exceptions) ----------
    if '—' in prose:
        add("CRITICAL", f, "em dash in visible text (rule: never use em dashes)")
    if re.search(r"(?<=[A-Za-z])'(?=[A-Za-z])", prose):
        add("MAJOR", f, "straight apostrophe in prose (use curly ’)")
    if re.search(r'gradient\s*\(', s):
        add("CRITICAL", f, "CSS gradient found (rule: solid palette colors only)")
    if 'lang="en"' not in s:
        add("CRITICAL", f, 'missing lang="en" on <html>')
    h1 = len(re.findall(r'<h1[\s>]', s))
    if h1 == 0:
        add("CRITICAL", f, "no <h1>")
    elif h1 > 1:
        add("CRITICAL", f, f"{h1} <h1> elements (must be exactly 1)")
    if '<title>' not in s:
        add("CRITICAL", f, "missing <title>")
    if re.search(r'outline\s*:\s*none', s) and 'focus-visible' not in s:
        add("CRITICAL", f, "outline:none with no :focus-visible replacement")
    for m in re.finditer(r'<img(?![^>]*\balt=)[^>]*>', s):
        add("CRITICAL", f, "img without alt attribute"); break
    for m in re.finditer(r'<iframe(?![^>]*\btitle=)[^>]*>', s):
        add("MAJOR", f, "iframe without title"); break
    # curly quotes used as JavaScript string delimiters break the parser and
    # render raw code on screen. This shipped live on 4 pages before 16 Aug 2026.
    if re.search(r'(?:\$\{\[|[\[\(]\s*|=\s*)[\u2018\u2019][A-Za-z][^\u2018\u2019\n]{0,60}[\u2018\u2019]\s*[,\]\)]', s):
        add("CRITICAL", f, "curly quote used as a JS string delimiter (breaks the script, renders raw code)")
    # leftovers from a find-and-replace that scrubbed the institution name
    for frag in ("the official the college", "the college:", "the college provides",
                 "the college Faculty", "the the "):
        if frag in s:
            add("CRITICAL", f, "find-and-replace leftover in visible text: %r" % frag)
            break
    if re.search(r'<div[^>]*\bonclick=', s):
        add("CRITICAL", f, "clickable <div> (use a real <button> or <a>)")

    # ---------- portfolio-only chrome rules ----------
    if fam or not in_portfolio(f):
        continue

    if 'class="site-head"' not in s:
        add("CRITICAL", f, "missing the site header (.site-head with name + Home/Work/About)")
    if 'class="sitefoot"' not in s and 'class="toolfoot"' not in s:
        add("MAJOR", f, "missing the site footer")
    if 'assets/site.css' not in s:
        add("MAJOR", f, "does not load /assets/site.css, so shared header/footer styles will not apply")
    if '<main' in s and 'id="main"' not in s:
        add("CRITICAL", f, '<main> without id="main"')
    if 'skip-link' not in s and 'class="skip"' not in s:
        add("MAJOR", f, "no skip-to-content link")

    # alignment: header / main / footer must share max-width 1000px
    widths = {}
    for sel, pat in (("site-head", r'\.site-head\{[^}]*max-width:\s*(\d+)px'),
                     ("main",      r'(?<!\.)\bmain\s*\{[^}]*max-width:\s*(\d+)px'),
                     ("sitefoot",  r'\.sitefoot\{[^}]*max-width:\s*(\d+)px')):
        m = re.search(pat, s)
        if m: widths[sel] = int(m.group(1))
    if len(set(widths.values())) > 1:
        add("CRITICAL", f, f"max-width mismatch causes horizontal shift: {widths}")
    for sel, w in widths.items():
        if w != 1000:
            add("CRITICAL", f, f".{sel} max-width {w}px (locked: 1000px)")

    # double padding: an inner wrapper re-padding inside an already padded main
    if re.search(r'main\s+\.wrap\{[^}]*padding:[^}]*\d+(\.\d+)?rem\s+1\.5rem', s):
        add("CRITICAL", f, "main .wrap adds a second 1.5rem padding (content shifts right)")

    # tab bar indent drift
    if re.search(r'\.tabs a\.tab\{[^}]*padding:\s*0\.55rem 0\.85rem', s):
        add("CRITICAL", f, "old .tabs padding 0.55/0.85 indents tabs ~14px right of the h1")

    # footer must be outside main
    if re.search(r'<footer[^>]*class="sitefoot".*?</footer>\s*</main>', s, re.S):
        add("CRITICAL", f, "<footer class=sitefoot> is INSIDE <main> (must sit outside)")

    # nav must be exactly Home / Work / About
    nav = re.search(r'<nav class="site-nav">(.*?)</nav>', s, re.S)
    if nav:
        links = re.findall(r'<a[^>]*>([^<]+)</a>', nav.group(1))
        clean = [re.sub(r'\s+', ' ', x).strip() for x in links]
        if clean != ["Home", "Work", "About"]:
            add("MAJOR", f, f"site-nav links are {clean} (locked: Home, Work, About)")

    # eyebrow must sit UNDER the h1
    if 'class="eyebrow"' in s:
        ih1 = s.find('<h1')
        iey = s.find('class="eyebrow"')
        if iey < ih1:
            add("MAJOR", f, "eyebrow appears ABOVE the h1 (locked: under the title)")

    # palette
    if re.search(r'--ink:\s*#(?!26221f)', s):
        m = re.search(r'--ink:\s*(#[0-9a-fA-F]{6})', s)
        add("CRITICAL", f, f"--ink overridden to {m.group(1)} (locked: #26221f)")
    for bad in ("#ede4f2",):
        if bad in s:
            add("MAJOR", f, f"off-palette box fill {bad} (locked fill: #f7f4f8)")
    # sage/gold/rose used as text colour without the accessible -text variant
    for var, fix in (("--sage", "--sage-text #456546"),
                     ("--gold", "--gold-text #75592c"),
                     ("--rose", "--rose-text #94395a")):
        if re.search(r'color:\s*var\(' + var + r'\)', s):
            add("MAJOR", f, f"color:var({var}) fails 4.5:1 as text (use {fix})")

# ---------- report ----------
order = ["CRITICAL", "MAJOR", "MINOR"]
total = sum(len(issues[k]) for k in order)
print("=" * 68)
nport = len([f for f in files if in_portfolio(f) and not is_family_tool(f)])
print("  DESIGN SYSTEM LINT, %d pages scanned, %d in portfolio scope" % (len(files), nport))
print("=" * 68)
for sev in order:
    if not issues[sev]:
        continue
    print("\n%s  (%d)" % (sev, len(issues[sev])))
    by_file = defaultdict(list)
    for f, m in issues[sev]:
        by_file[f].append(m)
    for f in sorted(by_file):
        print("  %s" % f)
        for m in sorted(set(by_file[f])):
            print("      - %s" % m)
if total == 0:
    print("\n  CLEAN. No violations found.\n")
else:
    print("\n  %d issue(s). CRITICAL must be fixed before shipping.\n" % total)
sys.exit(1 if issues["CRITICAL"] else 0)
