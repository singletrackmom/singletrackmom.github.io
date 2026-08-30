#!/usr/bin/env python3
"""
a11y-lint.py, the accessibility gate for singletrackmom.github.io / michelleblomberg.com

GOAL     Catch the WCAG 2.1 AA failures a hiring manager or a screen-reader user would hit,
         which design-lint.py does not check. Structure, alt text, link text, labels,
         heading order, duplicate ids, new-tab safety, iframe titles, and focus states.
AUDIENCE Michelle. She never opens this file; it is an assistant tool. Report in plain
         language: what was broken, what was fixed, what is clean.
PROCESS  Run from the repo root. Exits non-zero if anything CRITICAL is found.
             python3 tools/a11y-lint.py           portfolio surface only
             python3 tools/a11y-lint.py --all     every page, family and tool pages included

SCOPE, mirrors website-style-guide:
  Portfolio surface  root index/work/about, render, copamigo, course-dialer, wayfinder,
                     cultivate, airc-sss, style-guide, sss_committee, and every
                     overview.html / prd.html.
  Universal only     family and tool pages (flow, focus, soar, summerwork, jobs, command,
                     lunch, traillog, frisco, devan, roughcut, syllabus-checker).
  Exempt             Canvas page fragments (no <body> by design), .private.html working
                     sheets, node_modules, and command/todo.html (git-ignored, local only).
"""
import os, re, sys, glob
from collections import defaultdict

ALL = '--all' in sys.argv
ROOT = os.getcwd()

PORTFOLIO = ('index.html', 'work.html', 'about.html', 'render/', 'copamigo/',
             'course-dialer/', 'wayfinder/', 'cultivate/', 'airc-sss/',
             'style-guide/', 'sss_committee/')
FAMILY = ('flow/', 'focus/', 'soar/', 'summerwork/', 'jobs/', 'command/', 'lunch/',
          'traillog/', 'frisco/', 'devan/', 'roughcut/', 'syllabus-checker/')
# deliberately standalone, documented in website-style-guide, do not "fix"
EXEMPT = {'copamigo/widget.html', 'render/render-maya.html', 'render/render-riley.html',
          'command/todo.html'}

findings = defaultdict(list)
def add(sev, f, msg):
    findings[sev].append((f, msg))

def in_scope(f):
    if f in EXEMPT or 'node_modules' in f or f.startswith('.git') or '.private.' in f:
        return False
    if f.startswith(PORTFOLIO) or f.endswith(('overview.html', 'prd.html')):
        return True
    return ALL and f.startswith(FAMILY)

def strip_scripts(s):
    s = re.sub(r'<script\b.*?</script>', '', s, flags=re.I | re.S)
    return re.sub(r'<!--.*?-->', '', s, flags=re.S)

pages = 0
for f in sorted(glob.glob('**/*.html', recursive=True)):
    if not in_scope(f):
        continue
    raw = open(f, encoding='utf-8', errors='ignore').read()
    if '<body' not in raw:          # Canvas fragment
        continue
    pages += 1
    s = strip_scripts(raw)
    stub = 'http-equiv="refresh"' in raw

    # ---- document structure -------------------------------------------------
    if not re.search(r'<html[^>]*\slang=', raw):
        add('CRITICAL', f, 'no lang attribute on <html>')
    if not re.search(r'<title>\s*\S', raw):
        add('CRITICAL', f, 'no <title>')
    h1 = re.findall(r'<h1[\s>]', s)
    if len(h1) == 0:
        add('CRITICAL', f, 'no <h1>')
    elif len(h1) > 1:
        add('CRITICAL', f, f'{len(h1)} <h1> elements, must be exactly one')
    if len(re.findall(r'<main[^>]*\sid="main"', s)) != 1:
        add('CRITICAL', f, 'missing a single <main id="main">')
    if 'skip-link' not in raw and 'class="skip"' not in raw:
        add('CRITICAL', f, 'no skip-to-content link')
    else:
        for tgt in re.findall(r'class="skip[^"]*"[^>]*href="#([^"]+)"', raw):
            if f'id="{tgt}"' not in raw:
                add('CRITICAL', f, f'skip link points at #{tgt} which does not exist')

    # ---- heading order ------------------------------------------------------
    levels = [int(m) for m in re.findall(r'<h([1-6])[\s>]', s)]
    prev = 0
    for lv in levels:
        if prev and lv > prev + 1:
            add('MAJOR', f, f'heading level jumps h{prev} to h{lv}')
            break
        prev = lv

    # ---- images -------------------------------------------------------------
    for tag in re.findall(r'<img\b[^>]*>', s, re.I):
        if not re.search(r'\salt\s*=', tag, re.I):
            add('CRITICAL', f, 'image with no alt attribute: ' + tag[:70])
        elif re.search(r'alt\s*=\s*"(image|photo|picture|img|graphic)"', tag, re.I):
            add('MAJOR', f, 'unhelpful alt text: ' + tag[:70])

    # ---- links --------------------------------------------------------------
    for tag, text in re.findall(r'(<a\b[^>]*>)(.*?)</a>', s, re.I | re.S):
        label = re.sub(r'<[^>]+>', '', text).strip()
        # An <img alt="..."> inside the link supplies its accessible name.
        img_alt = re.search(r'<img\b[^>]*\salt="([^"]+)"', text, re.I)
        if img_alt:
            label = label or img_alt.group(1).strip()
        if not label and not re.search(r'aria-label|title\s*=', tag, re.I):
            add('CRITICAL', f, 'link with no accessible text: ' + tag[:70])
        if label.lower() in ('click here', 'here', 'read more', 'more', 'link'):
            add('MAJOR', f, f'non-descriptive link text: "{label}"')
        if 'target="_blank"' in tag and 'rel=' not in tag:
            add('MAJOR', f, 'target="_blank" without rel="noopener": ' + tag[:70])

    # ---- controls -----------------------------------------------------------
    # A control counts as labelled by any of the four legitimate mechanisms:
    #   1. a <label for="id"> elsewhere on the page
    #   2. being nested inside a <label> (the wrapping-label pattern, valid and common)
    #   3. aria-label / aria-labelledby
    #   4. a title attribute
    # Checking only for `for=` produced 500+ false positives on the tool pages,
    # which all use the wrapping pattern. Fix the checker, never the finding.
    inside_label = []
    for m in re.finditer(r'<label\b[^>]*>.*?</label>', s, re.I | re.S):
        inside_label.append((m.start(), m.end()))
    def wrapped(pos):
        return any(a <= pos <= b for a, b in inside_label)

    for m in re.finditer(r'<(?:input|select|textarea)\b[^>]*>', s, re.I):
        tag = m.group(0)
        if re.search(r'type\s*=\s*"(hidden|submit|button|reset|image)"', tag, re.I):
            continue
        has_id = re.search(r'\sid="([^"]+)"', tag)
        labelled = bool(re.search(r'aria-label|aria-labelledby|\stitle\s*=', tag, re.I))
        if has_id and f'for="{has_id.group(1)}"' in s:
            labelled = True
        if wrapped(m.start()):
            labelled = True
        if not labelled:
            add('CRITICAL', f, 'form control with no label: ' + tag[:70])
    for tag in re.findall(r'<iframe\b[^>]*>', s, re.I):
        if not re.search(r'\stitle\s*=', tag, re.I):
            add('CRITICAL', f, 'iframe with no title: ' + tag[:70])

    # ---- clickable divs -----------------------------------------------------
    # A <div onclick> is only a failure when it is not operable by keyboard.
    # A div carrying role + tabindex + a key handler is a correctly built ARIA
    # widget and passes. A backdrop that only dismisses on its own click
    # (event.target===this) is not a control and is not flagged.
    for tag in re.findall(r'<div[^>]*\sonclick=[^>]*>', s, re.I):
        if 'event.target===this' in tag.replace(' ', ''):
            continue                                   # modal backdrop, not a control
        keyboard = 'onkeydown' in tag.lower() or 'onkeyup' in tag.lower() or 'onkeypress' in tag.lower()
        has_role = re.search(r'\srole="(button|tab|link|checkbox|switch|menuitem|option)"', tag, re.I)
        focusable = re.search(r'\stabindex="(0|-1)"', tag)
        if has_role and focusable and (keyboard or has_role.group(1).lower() == 'tab'):
            continue                                   # properly built widget
        add('CRITICAL', f, 'clickable <div> not operable by keyboard: ' + tag[:80])

    # ---- inherited colour on a dark band -------------------------------------
    # THE BUG THIS EXISTS FOR, found 30 Aug 2026 on 42 live pages, several of them
    # sent to family members: a page sets a light colour on .hero and expects the
    # h1 to inherit it. assets/site.css sets h1{color:var(--ink)} EXPLICITLY, and
    # an explicit rule always beats an inherited one, so the h1 rendered in the
    # page's own near-black ink on its own near-black band. Not low contrast.
    # Identical to the background. Invisible, for months, with nothing checking.
    #
    # A linter cannot resolve the cascade, so it checks the shape instead: a dark
    # .hero background with no explicit .hero h1 colour is always this bug.
    css_all = ' '.join(re.findall(r'<style[^>]*>(.*?)</style>', raw, re.S))
    css_all = re.sub(r'/\*.*?\*/', '', css_all, flags=re.S)
    if 'class="hero"' in raw and not re.search(r'\.hero\s+h1\s*\{[^}]*color', css_all):
        v = dict(re.findall(r'--([a-z-]+):\s*(#[0-9a-fA-F]{3,6})', css_all))
        hm = re.search(r'(?:header\.hero|\.hero)\s*\{([^}]*)\}', css_all)
        bgm = re.search(r'background(?:-color)?\s*:\s*([^;]+)', hm.group(1)) if hm else None
        if bgm:
            tok = bgm.group(1).split()[0].strip()
            vm = re.match(r'var\(--([a-z-]+)\)', tok)
            bg = v.get(vm.group(1)) if vm else (tok if tok.startswith('#') else None)
            if bg:
                def _l(h):
                    h = h.lstrip('#')
                    if len(h) == 3: h = ''.join(c * 2 for c in h)
                    q = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
                    q = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in q]
                    return 0.2126 * q[0] + 0.7152 * q[1] + 0.0722 * q[2]
                ink = v.get('ink', '#26221f')
                a, b = _l(ink), _l(bg)
                if (max(a, b) + .05) / (min(a, b) + .05) < 4.5:
                    add('CRITICAL', f, f'.hero h1 has no colour of its own, so it falls back to '
                        f'site.css h1 colour {ink} on the dark band {bg}. State the colour on .hero h1')

    # ---- focus visibility ---------------------------------------------------
    if re.search(r'outline\s*:\s*(none|0)\b', raw, re.I) and 'focus-visible' not in raw:
        add('MAJOR', f, 'outline:none with no :focus-visible replacement')

    # ---- duplicate ids ------------------------------------------------------
    ids = re.findall(r'\sid="([^"]+)"', s)
    dupes = {i for i in ids if ids.count(i) > 1}
    for d in sorted(dupes):
        add('MAJOR', f, f'duplicate id="{d}"')

    # ---- sharing ------------------------------------------------------------
    if f.startswith(PORTFOLIO) and not stub:
        if 'og:image' in raw and re.search(r'og:image"[^>]*content="[^"]*\.svg', raw, re.I):
            add('MAJOR', f, 'og:image is an SVG; LinkedIn will not render it, use a PNG')
        if not re.search(r'name="description"', raw, re.I):
            add('MINOR', f, 'no meta description')

# ---- report -----------------------------------------------------------------
W = 68
print('=' * W)
print(f'  ACCESSIBILITY LINT, {pages} pages in scope' + ('  (--all)' if ALL else ''))
print('=' * W)
total = 0
for sev in ('CRITICAL', 'MAJOR', 'MINOR'):
    rows = findings.get(sev, [])
    if not rows:
        continue
    total += len(rows)
    print(f'\n  {sev}  ({len(rows)})\n')
    for fname, msg in rows:
        print(f'    {fname}\n        {msg}')
if not total:
    print('\n  CLEAN. No accessibility violations found.\n')
else:
    print(f'\n  {total} finding(s). CRITICAL must be fixed before shipping.\n')
sys.exit(1 if findings.get('CRITICAL') else 0)
