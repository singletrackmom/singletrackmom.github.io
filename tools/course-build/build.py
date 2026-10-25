#!/usr/bin/env python3
"""One build for every course page (canvas/<course>/course.html).

What is shared, written once:
  - the page shell: head, site header, footer, styles (/canvas/course.css, /canvas/course-site.css)
    and script (/canvas/course.js)
  - Module 0 · Getting Started, from canvas/_shared/module0.html

What stays course-specific, kept inside each course.html between markers:
  <!-- build:head --> ... <!-- /build:head -->        title, description, social tags
  <!-- build:main --> ... <!-- /build:main -->        breadcrumbs, tabs, banner, Modules 1 and up
  <!-- slot:name --> ... <!-- /slot:name -->           course pieces inside the shared Module 0

Usage (from the repo root):
  python3 tools/course-build/build.py --all          rebuild every course page
  python3 tools/course-build/build.py avc150         rebuild one
  python3 tools/course-build/build.py --check        fail if any page drifted from the masters
  python3 tools/course-build/build.py --convert avc150   one-time: put an old page under the build

Never hand-edit the shared parts of a course page; edit the master and rebuild.
"""
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CANVAS = os.path.join(ROOT, 'canvas')
MASTER_M0 = os.path.join(CANVAS, '_shared', 'module0.html')

DISCORD_URL = 'https://discord.gg/fyzAXNS4yF'

# Course values. ai: False only for AVC100 (not an AI-focused course).
# setup_comp / ai_comp: the course competency Module 0's two objectives support.
# hours: Module 0 seat time shown on the module bar.
COURSES = {
    'avc100': dict(code='AVC100', ai=False, hours='3', setup_comp='1', ai_comp=''),
    'avc150': dict(code='AVC150', ai=True, hours='6', setup_comp='8', ai_comp='8'),
    'avc183': dict(code='AVC183', ai=True, hours='9.5', setup_comp='3', ai_comp='3'),
    'avc190': dict(code='AVC190', ai=True, hours='7.5', setup_comp='6', ai_comp='6'),
    'avc248': dict(code='AVC248', ai=True, hours='7.5', setup_comp='8', ai_comp='2'),
    'avc283': dict(code='AVC283', ai=True, hours='8', setup_comp='3', ai_comp='3'),
    'avc2xx': dict(code='AVC2xx', ai=True, hours='10', setup_comp='3', ai_comp='3'),
}

SHELL_TOP = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">
<meta name="theme-color" content="#7a5080">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Built by tools/course-build/build.py. Edit only the build:head, build:main and slot regions. -->
<!-- build:head -->
{head}
<!-- /build:head -->
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;1,400&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/canvas/course.css">
<link rel="stylesheet" href="/canvas/course-site.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-head"><div class="site-bar"><a class="site-name" href="/">Michelle Blomberg</a>
<nav class="site-nav" aria-label="Primary"><a href="/#work">Work</a><a href="/about.html">About</a></nav></div></header>
<main id="main">
<!-- build:main -->
'''
SHELL_BOTTOM = '''<!-- /build:main -->
</main>
<footer class="sitefoot">
<div class="foot-links"><a href="/#work">Work</a><a href="/about.html">About</a><a href="/about.html" class="mailme">Email</a><a href="#main">Top <span aria-hidden="true">&uarr;</span></a></div>
<div style="margin-top:.5rem;font-size:.875rem">Course materials shared under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener">CC BY-NC-SA 4.0</a>.</div>
</footer>
<script src="/canvas/course.js"></script>
</body>
</html>
'''

SLOT_RE = re.compile(r'<!-- slot:([a-z_]+) -->(.*?)<!-- /slot:\1 -->', re.S)
M0_RE = re.compile(r'<!-- build:module0 -->.*?<!-- /build:module0 -->', re.S)
BANNED = ['Where You Stand', 'where you stand', 'position statement', '&mdash;', '—']


def page_path(c):
    return os.path.join(CANVAS, c, 'course.html')


def region(s, name):
    m = re.search(r'<!-- build:%s -->\n?(.*?)\n?<!-- /build:%s -->' % (name, name), s, re.S)
    if not m:
        raise SystemExit('%s region missing; run --convert first' % name)
    return m.group(1)


def render_m0(vals, slots):
    t = open(MASTER_M0, encoding='utf-8').read()
    t = re.sub(r'^<!-- MASTER:.*?-->\n', '', t, flags=re.S)
    def sect(m):
        on = vals['ai']
        return m.group(2) if (m.group(1) == '#') == on else ''
    t = re.sub(r'\{\{([#^])ai\}\}(.*?)\{\{/ai\}\}', sect, t, flags=re.S)
    t = re.sub(r'\{\{slot:([a-z_]+)\}\}',
               lambda m: '<!-- slot:%s -->%s<!-- /slot:%s -->' % (m.group(1), slots.get(m.group(1), ''), m.group(1)), t)
    v = dict(vals, discord_url=DISCORD_URL, discord_label=DISCORD_URL.replace('https://', ''))
    t = re.sub(r'\{\{([a-z_]+)\}\}', lambda m: str(v[m.group(1)]), t)
    if '{{' in t:
        raise SystemExit('unfilled placeholder in Module 0 master')
    return '<!-- build:module0 -->\n' + t.rstrip('\n') + '\n<!-- /build:module0 -->'


def render(c, s):
    head = region(s, 'head')
    main = region(s, 'main')
    m0 = M0_RE.search(main)
    if not m0:
        raise SystemExit('%s: build:module0 region missing' % c)
    slots = dict(SLOT_RE.findall(m0.group(0)))
    main = main[:m0.start()] + render_m0(COURSES[c], slots) + main[m0.end():]
    # every module title is a real heading (h2), so the page outline runs h1 > h2 > h3
    main = re.sub(r'<span class="ltitle">(.*?)</span>', r'<h2 class="ltitle">\1</h2>', main)
    return SHELL_TOP.replace('{head}', head.strip('\n')) + main.strip('\n') + '\n' + SHELL_BOTTOM


def check_page(c, s):
    problems = []
    ids = set(re.findall(r'\bid="([^"]+)"', s))
    for a in sorted(set(re.findall(r'href="#([^"]+)"', s))):
        if a not in ids:
            problems.append('broken in-page link #%s' % a)
    text = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    for b in BANNED:
        if b in text:
            problems.append('banned text: %r' % b)
    if 'TBD' in str(COURSES[c].values()):
        problems.append('course values still TBD in build.py')
    return problems


def convert(c):
    p = page_path(c); s = open(p, encoding='utf-8').read()
    if '<!-- build:main -->' in s:
        print(c, 'already converted'); return
    hm = re.search(r'<head>(.*?)</head>', s, re.S).group(1)
    keep = []
    for line in hm.split('\n'):
        l = line.strip()
        if not l: continue
        if re.match(r'<(meta charset|meta name="viewport"|meta name="theme-color"|link rel="icon"|link rel="apple-touch-icon"|link rel="stylesheet"|link href="https://fonts)', l):
            continue
        keep.append(l)
    head = '\n'.join(keep)
    head = re.sub(r'<style.*?</style>\n?', '', head, flags=re.S).strip()
    mm = re.search(r'<main id="main">(.*?)</main>', s, re.S)
    if not mm:
        raise SystemExit('%s: no <main id="main">; wrap the page body in it first' % c)
    main = mm.group(1)
    # Module 0: the balanced <details class="lesson" id="start-here"> element
    i = main.find('<details class="lesson" id="start-here"')
    if i < 0:
        raise SystemExit('%s: no Module 0 (details#start-here)' % c)
    depth = 0; j = i
    for t in re.finditer(r'<details\b|</details>', main[i:]):
        depth += 1 if t.group(0) == '<details' else -1
        if depth == 0:
            j = i + t.end(); break
    old = main[i:j]
    os.makedirs(os.path.join(ROOT, 'drafts'), exist_ok=True)
    open(os.path.join(ROOT, 'drafts', '%s-module0-old.html' % c), 'w', encoding='utf-8').write(old)
    main = main[:i] + '<!-- build:module0 --><!-- /build:module0 -->' + main[j:]
    s2 = '<head>\n<!-- build:head -->\n%s\n<!-- /build:head -->\n</head><main id="main">\n<!-- build:main -->\n%s\n<!-- /build:main -->\n</main>' % (head, main.strip('\n'))
    out = render(c, s2)
    open(p, 'w', encoding='utf-8').write(out)
    print(c, 'converted; old Module 0 saved to drafts/%s-module0-old.html; fill its slots, then rebuild' % c)


def main(argv):
    if not argv:
        print(__doc__); return 0
    if argv[0] == '--convert':
        for c in argv[1:]: convert(c)
        return 0
    check = argv[0] == '--check'
    targets = list(COURSES) if (check or argv[0] == '--all') else argv
    bad = 0
    for c in targets:
        p = page_path(c)
        s = open(p, encoding='utf-8').read()
        if '<!-- build:main -->' not in s:
            print('%s: not on the shared build yet' % c); bad += check; continue
        out = render(c, s)
        if check:
            probs = check_page(c, out)
            if out != s: probs.insert(0, 'page differs from a fresh build (shared text edited by hand, or not rebuilt)')
            print('%s: %s' % (c, 'OK' if not probs else '\n  - ' + '\n  - '.join(probs)))
            bad += bool(probs)
        else:
            open(p, 'w', encoding='utf-8').write(out)
            probs = check_page(c, out)
            print('%s: built%s' % (c, '' if not probs else '\n  - ' + '\n  - '.join(probs)))
    return 1 if (check and bad) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
