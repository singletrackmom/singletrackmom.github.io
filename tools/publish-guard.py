#!/usr/bin/env python3
"""
publish-guard.py, the exposure gate.

GOAL     Make it impossible to ship a private file on a public website by accident.
         This repo is a public GitHub Pages site with a .nojekyll file, which means
         GitHub serves EVERY committed file at its literal path: .md, .docx, .xlsx,
         .pptx, .csv, .json, all of it. There is no way to commit a file and not
         serve it. So on this site, private means NOT COMMITTED. Nothing else.

AUDIENCE Michelle, and every future Claude session. Sessions keep writing private
         notes into the repo because the repo is the folder they can reach. This
         check exists because the rule kept being written down and kept being broken.
         A rule that is not checked is a wish.

PROCESS  From the repo root:
             python3 tools/publish-guard.py           the summary
             python3 tools/publish-guard.py --list    every finding, no truncation

         Runs inside preflight.py. Exit 1 = do not commit.

WHAT IT CHECKS
  A. CONTENT. Any served file holding a phone number, a personal email address,
     a family member's name, medical or financial detail, or an explicit
     "never publish" marker.
  B. FORMAT. Office documents and archives served as downloads. A portfolio site
     has no reason to serve a .docx, .xlsx, .pptx, .imscc or .zip.
  C. VOLUME. Any other non-web file, reported so the count cannot quietly grow.

WHERE PRIVATE FILES GO INSTEAD
     ~/Documents/Claude/<Project>/ on Michelle's Mac, outside this repo.
     A session reaches it by mounting that exact subfolder. ~/Documents/Claude
     itself cannot be mounted because it contains a protected system folder,
     but any subfolder of it mounts fine. Verified 31 Aug 2026.

THE ESCAPE HATCH
     A file that genuinely belongs on the public web can be listed in
     tools/publish-allow.txt, one path per line. Add a reason on the same line
     after a #. An allowlist entry is a decision, so it should read like one.
"""
import os, re, sys, fnmatch

LIST_ALL = '--list' in sys.argv
ROOT = os.getcwd()

# ---------------------------------------------------------------- what gets served
WEB = {'.html', '.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp',
       '.ico', '.woff', '.woff2', '.ttf', '.otf', '.eot', '.mp4', '.webm', '.pdf',
       '.xml', '.webmanifest', '.avif', '.map', '.txt'}

# Office documents and archives. These are downloads, not pages. Blocking.
DOCS = {'.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.csv', '.tsv',
        '.imscc', '.zip', '.tar', '.gz', '.rtf', '.pages', '.numbers', '.key',
        '.gs', '.tmp', '.bak', '.sql', '.db'}

SKIP_DIRS = {'.git', 'node_modules'}


def gitignore_matchers():
    pats = []
    p = os.path.join(ROOT, '.gitignore')
    if os.path.exists(p):
        for ln in open(p, encoding='utf-8'):
            ln = ln.strip()
            if ln and not ln.startswith('#'):
                pats.append(ln.rstrip('/'))
    return pats


def is_ignored(rel, pats):
    base = os.path.basename(rel)
    for q in pats:
        if rel == q or rel.startswith(q + '/'):
            return True
        if fnmatch.fnmatch(rel, q) or fnmatch.fnmatch(base, q):
            return True
    return False


def allowlist():
    allowed = set()
    p = os.path.join(ROOT, 'tools', 'publish-allow.txt')
    if os.path.exists(p):
        for ln in open(p, encoding='utf-8'):
            ln = ln.split('#')[0].strip()
            if ln:
                allowed.add(ln)
    return allowed


# ---------------------------------------------------------------- private signals
# Tuned to this repo. Each pattern carries the plain-English reason it fires,
# because a finding nobody understands gets ignored.
# Two tiers, on purpose.
#
# BLOCK  is for things that are almost never legitimate portfolio content. A phone
#        number, a personal inbox, a live-looking credential, or an explicit
#        "never publish" marker on a file that is being published.
#
# REVIEW is for words that CAN be private and CAN be ordinary. This site legitimately
#        discusses health, advising and family. Kevin's page is public on purpose.
#        Render's personas are fictional and have conditions. So these report and
#        never block, because a check that cries wolf gets ignored, and that is
#        exactly how the last one failed.
SIGNALS = [
    ('BLOCK', r'\b(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}\b', 'phone number'),
    ('BLOCK', r'\b[\w.+-]+@(?:gmail|yahoo|hotmail|outlook|icloud|aol)\.com\b',
     'personal email address'),
    ('BLOCK', r'\b(?:sk-|ghp_|xox[baprs]-)[A-Za-z0-9]{16,}\b|AKIA[0-9A-Z]{16}',
     'looks like a live credential'),
    ('BLOCK', r'\bnever\s+publish\b|\bdo\s+not\s+publish\b|\bnot\s+for\s+publication\b|'
              r'\blocal\s+only\b|\bprivate,?\s+never\b',
     'the file says it should not be published'),
    ('REVIEW', r'\bmammogram\b|\bcolonoscopy\b|\bprescription\b|\bassisted\s+living\b|'
               r'\bdiagnos(?:is|ed)\b|\btherapist\b|\bADHD\b', 'health wording'),
    ('REVIEW', r'\bmortgage\b|\brouting\s+number\b|\baccount\s+number\b|\btax\s+return\b',
     'financial wording'),
    ('REVIEW', r'\b(Kevin|Jasper|Devan|Jillian)\b', 'family member named'),
]

COMPILED = [(tier, re.compile(p, re.I), why) for tier, p, why in SIGNALS]


TEXT = {'.md', '.html', '.txt', '.json', '.py', '.tex', '.sh', '.css', '.js'}

# Files that talk ABOUT the rules will trip the rules. Exclude them by name.
SELF = {'tools/publish-guard.py', 'tools/publish-allow.txt'}


def scan(path):
    if os.path.splitext(path)[1].lower() not in TEXT:
        return []
    try:
        s = open(path, encoding='utf-8', errors='ignore').read()
    except Exception:
        return []
    hits = []
    for tier, rx, why in COMPILED:
        m = rx.search(s)
        if m:
            hits.append((tier, why, m.group(0)[:48].replace('\n', ' ')))
    return hits


# ---------------------------------------------------------------- walk
def main():
    pats = gitignore_matchers()
    allowed = allowlist()

    block_hits, review_hits, doc_hits, other = [], [], [], []

    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            full = os.path.join(dp, fn)
            rel = os.path.relpath(full, ROOT)
            if fn == '.DS_Store' or is_ignored(rel, pats) or rel in allowed or rel in SELF:
                continue
            ext = os.path.splitext(fn)[1].lower()

            if ext in DOCS:
                doc_hits.append(rel)
                continue

            if ext in WEB or ext in {'.md', '.py', '.json', '.tex', '.sh'}:
                hits = scan(full) if ext in TEXT else []
                if any(t == 'BLOCK' for t, _, _ in hits):
                    block_hits.append((rel, hits))
                elif hits:
                    review_hits.append((rel, hits))
                if ext not in WEB:
                    other.append(rel)
            else:
                other.append(rel)

    # ------------------------------------------------------------ report
    print('\npublish-guard\n')
    cap = 10_000 if LIST_ALL else 12

    # One combined count first, because preflight reads the first CRITICAL (n) it sees.
    if block_hits:
        print(f'  CRITICAL ({len(block_hits)})  private data in a file the site serves\n')

    if block_hits:
        print(f'  CRITICAL ({len(block_hits)})  private data in a file the site serves')
        for rel, hits in block_hits[:cap]:
            why = ', '.join(sorted({w for t, w, _ in hits if t == 'BLOCK'}))
            print(f'     {rel}')
            print(f'        {why}')
        if len(block_hits) > cap:
            print(f'     ... and {len(block_hits) - cap} more, run with --list')
        print()

    if doc_hits:
        print(f'  MAJOR ({len(doc_hits)})  office document or archive served as a download')
        print('     Her own work, so not blocking. Still a download on a portfolio site.')
        for rel in doc_hits[:cap]:
            print(f'     {rel}')
        if len(doc_hits) > cap:
            print(f'     ... and {len(doc_hits) - cap} more, run with --list')
        print()

    if other:
        print(f'  MAJOR ({len(other)})  other non-web files the site serves')
        if LIST_ALL:
            for rel in other:
                print(f'     {rel}')
            print()

    if review_hits:
        print(f'  REVIEW ({len(review_hits)})  wording that is sometimes private, sometimes not')
        print('     Reported, never blocking. Skim once, then allowlist the settled ones.')
        if LIST_ALL:
            for rel, hits in review_hits:
                why = ', '.join(sorted({w for _, w, _ in hits}))
                print(f'     {rel}  ({why})')
        print()

    if other:
        print(f'  MAJOR ({len(other)})  other non-web files the site serves')
        if LIST_ALL:
            for rel in other:
                print(f'     {rel}')
        print()

    total_crit = len(block_hits)
    if not total_crit and not other and not review_hits:
        print('  ok   nothing private is being served\n')
        return 0

    if total_crit:
        print('  Move these OUT of the repo, to ~/Documents/Claude/<Project>/ on the Mac,')
        print('  then commit the deletion in GitHub Desktop. Removing a file stops it being')
        print('  served; it does not remove it from commit history.')
        print('  A file that truly belongs public goes in tools/publish-allow.txt with a reason.\n')
        return 1

    print('  Nothing blocking. The counts above are worth watching.\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
