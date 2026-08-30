#!/usr/bin/env python3
"""
prose-lint.py, the register check.

GOAL     Catch conversational writing in artifacts that carry Michelle's professional
         name: course pages, portfolio pages, PRDs, and anything a student, colleague,
         or hiring manager reads. Her chat voice and her artifact voice are different,
         and only one of them belongs on a page.

AUDIENCE Michelle, and every future Claude session. She reads the summary, not the code.

PROCESS  Run from the repo root, or let preflight run it.
             python3 tools/prose-lint.py            portfolio and course surface
             python3 tools/prose-lint.py --all      everything

WHAT THIS CAN AND CANNOT DO
  CAN   catch headings written as sentences, a defined list of casual terms,
        exclamation marks, and second-person chat openers. These are mechanical.
  CANNOT judge whether the register is right overall, whether an explanation
        condescends, or whether the framing suits the reader. A human still reads it.

  This check exists because on 29 Aug 2026 a student-facing course page shipped with
  the heading "Start here, and read this part," which is a text message, not a heading.
  The style guide already said headings are short labels and never sentences. Nothing
  enforced it.
"""
import os, re, sys, glob
from collections import defaultdict

ALL = '--all' in sys.argv

# Artifacts that carry her professional name and must read formally.
FORMAL = ('index.html', 'work.html', 'about.html', 'render/', 'copamigo/',
          'course-dialer/', 'wayfinder/', 'cultivate/', 'airc-sss/', 'canvas/',
          'style-guide/', 'sss_committee/', 'learning-design/', 'microcredentials/',
          'authentic-assessment/', 'capabilities/', 'data-science-course/',
          'light-and-lasers/', 'stem-project/', 'campus-cares/', 'roughcut/')
# Personal and family tools. Warm is correct there; not checked unless --all.
INFORMAL = ('flow/', 'focus/', 'soar/', 'summerwork/', 'devan/', 'traillog/',
            'frisco/', 'lunch/', 'jobs/', 'command/')

# Terms that do not belong in an artifact. Word-boundary matched, case-insensitive.
CASUAL = [
    # Unambiguous chat register. These do not belong in an artifact.
    r"\blet\u2019s\b", r"\blet's\b", r"\bgonna\b", r"\bwanna\b", r"\bkinda\b",
    r"\bsorta\b", r"\bstuff\b", r"\ba bunch of\b", r"\btons of\b",
    r"\bgrab\b", r"\bcheck out\b", r"\bdive in(to)?\b", r"\bsuper\b",
    r"\bawesome\b", r"\bno worries\b", r"\beasy peasy\b", r"\bheads up\b",
    r"\byou guys\b", r"\bokay,", r"\bhang tight\b", r"\bnbd\b",
]
# Words Michelle has banned in her own writing. Flagged separately, lower severity,
# because context sometimes earns them (an instruction to "look honestly at" is fine).
BANNED_SOFT = [r"\bgenuinely\b", r"\bstraightforward\b"]

# Conversational openers that signal a heading was written as speech.
CHAT_OPENERS = r"^(start here|okay|ok|alright|so\b|now\b|here'?s|let'?s|read this|the thing is|one more thing|a quick|just )"

findings = defaultdict(list)
def add(sev, f, msg):
    findings[sev].append((f, msg))

def in_scope(f):
    if 'node_modules' in f or f.startswith('.git') or '.private.' in f:
        return False
    if f.startswith(FORMAL):
        return True
    return ALL and f.startswith(INFORMAL)

def strip(s):
    s = re.sub(r'<script\b.*?</script>', '', s, flags=re.I | re.S)
    s = re.sub(r'<style\b.*?</style>', '', s, flags=re.I | re.S)
    return re.sub(r'<!--.*?-->', '', s, flags=re.S)

pages = 0
for f in sorted(glob.glob('**/*.html', recursive=True)):
    if not in_scope(f):
        continue
    raw = open(f, encoding='utf-8', errors='ignore').read()
    if '<body' not in raw:
        continue
    pages += 1
    s = strip(raw)

    # ---- headings must be labels, not sentences -----------------------------
    for lvl, txt in re.findall(r'<h([1-6])[^>]*>(.*?)</h\1>', s, re.S | re.I):
        t = re.sub(r'<[^>]+>', '', txt)
        t = re.sub(r'&[a-z]+;', ' ', t).strip()
        if not t:
            continue
        if t.endswith('.'):
            add('MAJOR', f, f'h{lvl} ends in a period, so it is a sentence: "{t[:64]}"')
        if len(t.split()) > 9:
            add('MINOR', f, f'h{lvl} is {len(t.split())} words, headings are short labels: "{t[:64]}"')
        if re.match(CHAT_OPENERS, t, re.I):
            add('MAJOR', f, f'h{lvl} opens conversationally: "{t[:64]}"')
        if '!' in t:
            add('MAJOR', f, f'h{lvl} contains an exclamation mark: "{t[:64]}"')

    # ---- casual terms in body prose -----------------------------------------
    body = re.sub(r'<[^>]+>', ' ', s)
    body = re.sub(r'&[a-z]+;', ' ', body)
    for pat in CASUAL:
        for m in re.finditer(pat, body, re.I):
            a = max(0, m.start() - 38)
            ctx = ' '.join(body[a:m.end() + 38].split())
            add('MAJOR', f, f'casual term "{m.group(0)}" in: ...{ctx}...')
            break        # one report per term per page, not per instance
    for pat in BANNED_SOFT:
        for m in re.finditer(pat, body, re.I):
            a = max(0, m.start() - 38)
            ctx = ' '.join(body[a:m.end() + 38].split())
            add('MINOR', f, f'"{m.group(0)}" is on your avoid list: ...{ctx}...')
            break

    if '!' in body and re.search(r'\w!', body):
        add('MINOR', f, 'exclamation mark in body prose')

W = 68
print('=' * W)
print(f'  PROSE / REGISTER LINT, {pages} pages in scope' + ('  (--all)' if ALL else ''))
print('=' * W)
total = 0
for sev in ('CRITICAL', 'MAJOR', 'MINOR'):
    rows = findings.get(sev, [])
    if not rows:
        continue
    total += len(rows)
    print(f'\n  {sev}  ({len(rows)})\n')
    for fname, msg in rows[:60]:
        print(f'    {fname}\n        {msg}')
    if len(rows) > 60:
        print(f'    ... and {len(rows) - 60} more')
if not total:
    print('\n  CLEAN. Register is consistent.\n')
else:
    print(f'\n  {total} finding(s). Nothing here blocks a commit; these are judgement calls.\n')
sys.exit(0)
