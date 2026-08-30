#!/usr/bin/env python3
"""
v2-lint.py, the gate for the v2 rebuild.

GOAL     Make it impossible to build a v2 page the way v1 pages got built. v1
         accumulated 586 lines of CSS inside one page, two nav variants, eight
         footer variants, and 153 pages the nav rule never even matched. Every
         one of those was allowed because nothing checked. This checks.

AUDIENCE Michelle, and every session building a v2 page. She reads the summary.

PROCESS  Run from the repo root, or let preflight run it.
             python3 tools/v2-lint.py

         Exits non-zero on CRITICAL. Everything here is CRITICAL by design:
         v2 is being built from nothing, so there is no legacy to forgive.

WHY THE RULES ARE STRICTER THAN v1's
  v1 has 300+ pages of history and the linter has to tolerate it. v2 has no
  history, so a rule can simply be absolute. That is the whole advantage of a
  rebuild and it evaporates the moment an exception is allowed "just once".

ON PROMOTION DAY
  When v2 moves to the root, these rules become the site's rules. Delete v1's
  leniency in design-lint.py rather than loosening anything here.
"""
import os, re, sys, glob
from collections import defaultdict

ROOT = os.getcwd()
findings = defaultdict(list)
def add(f, msg): findings['CRITICAL'].append((f, msg))

# The locked v2 chrome. The name is the Home link, so there is no Home nav item.
NAV    = ['Work', 'About']
FOOTER = ['Work', 'About', 'Email', 'Top &uarr;']

def text_of(html):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', html)).strip()

pages = 0
for f in sorted(glob.glob('v2/**/*.html', recursive=True)):
    if os.path.basename(f).startswith('_'):      # _template.html is checked separately
        continue
    raw = open(f, encoding='utf-8', errors='ignore').read()
    if '<body' not in raw:
        continue
    pages += 1
    s = re.sub(r'<!--.*?-->', '', raw, flags=re.S)

    # ---- the stylesheet rule, the one that caused the v1 mess ------------
    # Check the comment-stripped source, not the raw file. A header comment that
    # documents the rule ("never link /assets/site.css") is documentation, not a
    # link, and reading raw made the linter flag its own rule being written down.
    # Fixed 30 Aug 2026, same class of false positive as the <div> count in a comment.
    if '/v2/assets/v2.css' not in s:
        add(f, 'does not link /v2/assets/v2.css')
    if re.search(r'<link[^>]*href="/assets/site\.css"', s):
        add(f, 'links the v1 stylesheet /assets/site.css. v2 pages use v2.css only')
    if re.search(r'<style\b', s, re.I):
        add(f, 'contains a <style> block. Every rule belongs in v2.css')
    inline = re.findall(r'<[^>]*\sstyle="([^"]*)"', s)
    if inline:
        add(f, f'{len(inline)} inline style= attribute(s), first is: {inline[0][:60]}')

    # ---- document skeleton ---------------------------------------------
    if not re.search(r'<html[^>]*\slang=', raw):        add(f, 'no lang on <html>')
    if not re.search(r'<title>\s*\S', raw):             add(f, 'no <title>')
    if not re.search(r'name="description"', raw, re.I): add(f, 'no meta description')
    if 'noindex' not in raw:
        add(f, 'no robots noindex. v2 must stay out of the index until promotion day')
    og = re.search(r'og:image"[^>]*content="([^"]+)"', raw, re.I)
    if not og:                                          add(f, 'no og:image')
    elif not og.group(1).lower().endswith('.png'):      add(f, 'og:image is not a PNG. LinkedIn will not render it')
    elif not og.group(1).startswith('http'):            add(f, 'og:image is not an absolute URL')

    body = s[s.index('<body'):] if '<body' in s else s
    h1 = re.findall(r'<h1[\s>]', body)
    if len(h1) != 1:                                    add(f, f'{len(h1)} <h1> elements, must be exactly one')
    if len(re.findall(r'<main[^>]*\sid="main"', body)) != 1:
        add(f, 'missing a single <main id="main">')
    skip = re.search(r'class="skip-link"[^>]*href="#([^"]+)"', raw)
    if not skip:                                        add(f, 'no skip-to-content link')
    elif f'id="{skip.group(1)}"' not in raw:            add(f, f'skip link points at #{skip.group(1)}, which does not exist')

    # ---- locked nav and footer -----------------------------------------
    nav = re.search(r'<nav[^>]*class="site-nav"[^>]*>(.*?)</nav>', body, re.S)
    if not nav:
        add(f, 'no site-nav')
    else:
        got = [text_of(x) for x in re.findall(r'<a\b[^>]*>.*?</a>', nav.group(1), re.S)]
        if got != NAV:
            add(f, f'site-nav is {got}. Locked: {NAV}. The name is the Home link')
    foot = re.search(r'<div class="foot-links">(.*?)</div>', body, re.S)
    if not foot:
        add(f, 'no footer link set')
    else:
        got = [text_of(x) for x in re.findall(r'<a\b[^>]*>.*?</a>', foot.group(1), re.S)]
        if got != [text_of(x) for x in FOOTER]:
            add(f, f'footer is {got}. Locked: {[text_of(x) for x in FOOTER]}')
    if re.search(r'<footer[^>]*class="sitefoot"', body) and '</main>' in body:
        if body.index('<footer') < body.index('</main>'):
            add(f, '<footer class="sitefoot"> is inside <main>. It must sit outside')

    # ---- the eyebrow sits UNDER the h1, never above ---------------------
    if 'eyebrow' in body:
        if body.index('eyebrow') < body.index('<h1'):
            add(f, 'eyebrow appears above the <h1>. It always sits directly under it')

    # ---- house rules ----------------------------------------------------
    visible = text_of(body)
    if '—' in visible:                             add(f, 'em dash in visible text')
    if re.search(r"\w'\w", visible):                    add(f, 'straight apostrophe in prose, use a curly one')
    if re.search(r'linear-gradient|radial-gradient', raw, re.I):
        add(f, 'CSS gradient. Solid palette colors only')
    for tag in ('div', 'main', 'section'):
        o = len(re.findall(r'<' + tag + r'[\s>]', s)); c = len(re.findall(r'</' + tag + r'>', s))
        if o != c: add(f, f'unbalanced <{tag}>: {o} open, {c} close')

W = 68
print('=' * W); print(f'  V2 LINT, {pages} pages in scope'); print('=' * W)
rows = findings['CRITICAL']
if not rows:
    print('\n  CLEAN. Every v2 page is on the template, the stylesheet, and the locked chrome.\n')
else:
    print(f'\n  CRITICAL  ({len(rows)})\n')
    for fn, msg in rows:
        print(f'    {fn}\n        {msg}')
    print(f'\n  {len(rows)} finding(s). v2 has no legacy, so all of these are blocking.\n')
sys.exit(1 if rows else 0)
