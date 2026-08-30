#!/usr/bin/env python3
"""
preflight.py, the one gate. Run this before anything is called done.

GOAL     Make "done" mean something checkable instead of something an assistant asserts.
         A rule that is not checked is a wish. This runs every check in one command so
         no session can drift past them.

AUDIENCE Michelle, and every future Claude session. She does not read the output of the
         individual linters; she reads the one summary line at the bottom of this.

PROCESS  From the repo root:
             python3 tools/preflight.py            portfolio surface
             python3 tools/preflight.py --all      every page

         Exit 0 = safe to commit. Exit 1 = something CRITICAL, do not ship.

WHAT IT RUNS
  1. design-lint.py    the locked design system: widths, nav, palette, quotes, em dashes
  2. a11y-lint.py      WCAG 2.1 AA: structure, alt text, labels, headings, link safety
  3. link check        every internal href and src actually resolves
  4. tidy check        file placement, the rules in CLAUDE.md that used to be prose only

THE ESCAPE HATCH
  If the git hook ever blocks a commit you need to make, create an empty file named
  `.skip-preflight` inside `tools/`. Finder can do this; no Terminal needed. The hook
  will warn instead of blocking. Delete the file to turn the gate back on.
"""
import os, re, sys, glob, subprocess, urllib.parse

ALL = '--all' in sys.argv
ROOT = os.getcwd()
FAIL = []          # blocking
WARN = []          # reported, not blocking

def run(label, cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    out = (p.stdout or '') + (p.stderr or '')
    crit = re.search(r'CRITICAL\s*\((\d+)\)', out)
    n = int(crit.group(1)) if crit else 0
    if p.returncode != 0 or n:
        FAIL.append(f'{label}: {n} CRITICAL' if n else f'{label}: failed to run')
        # surface the critical block so the fix is obvious
        blk = re.search(r'CRITICAL.*?(?=\n\s*(MAJOR|MINOR|\d+ (issue|finding))|\Z)', out, re.S)
        if blk:
            for line in blk.group(0).strip().split('\n')[:14]:
                print('     ' + line.rstrip())
    else:
        m = re.search(r'(MAJOR\s*\((\d+)\))', out)
        extra = f", {m.group(2)} major" if m else ''
        print(f'  ok   {label}{extra}')

# ---------------------------------------------------------------- 1 & 2
print('\npreflight' + (' --all' if ALL else '') + '\n')
args = ['--all'] if ALL else []
run('design system   ', ['python3', 'tools/design-lint.py'] + args)
run('accessibility   ', ['python3', 'tools/a11y-lint.py'] + args)

# Register check. Advisory only: it never blocks, because tone is a judgement call.
_p = subprocess.run(['python3', 'tools/prose-lint.py'] + args, capture_output=True, text=True)
_m = re.search(r'MAJOR\s*\((\d+)\)', _p.stdout or '')
if _m:
    WARN.append(f'register: {_m.group(1)} conversational finding(s), see prose-lint.py')
    print(f'  warn register         {_m.group(1)} findings, run tools/prose-lint.py to read them')
else:
    print('  ok   register         formal throughout')

# ---------------------------------------------------------------- 3 links
sc = re.compile(r'<script\b.*?</script>', re.I | re.S)
lk = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"', re.I)
broken, checked = [], 0
for f in glob.glob('**/*.html', recursive=True):
    if 'node_modules' in f or f.startswith('.git'):
        continue
    d = os.path.dirname(f)
    s = sc.sub('', open(f, encoding='utf-8', errors='ignore').read())
    for u in lk.findall(s):
        u = u.strip()
        if (not u or u.startswith(('http', 'mailto:', 'tel:', 'data:', 'javascript:', '#'))
                or '${' in u or "'+" in u or '+ ' in u):
            continue
        path = urllib.parse.unquote(u.split('#')[0].split('?')[0])
        if not path:
            continue
        t = (os.path.normpath(os.path.join(ROOT, path.lstrip('/'))) if path.startswith('/')
             else os.path.normpath(os.path.join(ROOT, d, path)))
        checked += 1
        if not (os.path.exists(t) or os.path.exists(os.path.join(t, 'index.html'))):
            broken.append(f'{f} -> {u}')
if broken:
    FAIL.append(f'links: {len(broken)} broken')
    for b in broken[:12]:
        print('     ' + b)
else:
    print(f'  ok   links            {checked} resolved')

# ---------------------------------------------------------------- 4 tidy
# The CLAUDE.md file-placement rules, as checks instead of prose.
tidy = []

junk = [f for f in glob.glob('**/*', recursive=True)
        if 'node_modules' not in f and not f.startswith('.git')
        and re.search(r'\.bak$|\.pre-[\w-]+$|(^|/)_tmp|_old(\.|$)', f)]
tidy += [f'temp or backup file, delete it: {f}' for f in junk]

ROOT_MD_OK = {'CLAUDE.md', 'TASKS.md', 'README.md'}
for f in glob.glob('*.md'):
    if f not in ROOT_MD_OK:
        tidy.append(f'markdown at the repo root: {f}. A project gets a directory.')

# one working markdown per project directory (uppercase = the project's own file)
SKIP_DIRS = {'tools', 'canvas', 'notes', 'drafts', 'node_modules', 'assets', 'airc-sss', 'agents'}
for d in sorted(os.listdir('.')):
    if not os.path.isdir(d) or d.startswith('.') or d in SKIP_DIRS:
        continue
    mds = [m for m in glob.glob(f'{d}/*.md') if os.path.basename(m).upper() == os.path.basename(m)]
    if len(mds) > 1:
        tidy.append(f'{d}/ has {len(mds)} project markdowns, expected one: '
                    + ', '.join(os.path.basename(m) for m in mds))

if tidy:
    WARN.append(f'tidy: {len(tidy)} issue(s)')
    for t in tidy[:12]:
        print('  warn tidy             ' + t)
else:
    print('  ok   tidy             file placement clean')

# ---------------------------------------------------------------- verdict
print()
if FAIL:
    print('  BLOCKED. Fix these before committing:')
    for x in FAIL:
        print('    - ' + x)
    print('\n  If you need to commit anyway, create an empty file at tools/.skip-preflight')
    print('  in Finder. Delete it afterwards to turn the gate back on.\n')
    sys.exit(1)
if WARN:
    print('  PASS with warnings: ' + '; '.join(WARN))
    print('  Safe to commit. Worth tidying when there is time.\n')
else:
    print('  PASS. Everything clean, safe to commit.\n')
sys.exit(0)
