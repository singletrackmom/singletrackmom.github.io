#!/usr/bin/env python3
"""
frozen-guard.py  ·  BLOCKING gate in preflight.py

Some documents in this repo were SUBMITTED to a real person and are historical
record. They are frozen. Nobody edits them again, including Claude, including
as collateral damage from a repo-wide find-and-replace.

This exists because on 19 September 2026 a district-wide naming correction
("AI Resource Committee" to "AI Resource Center") was run across every file in
the repo and it silently rewrote five passages of the FEP that had already been
submitted to the VP. Michelle caught it by reading her own GitHub. A rule in a
markdown file would not have caught it. This does.

Frozen paths and their SHA-256 are in tools/FROZEN.txt.
To intentionally re-freeze after a deliberate, Michelle-approved change:
    python3 tools/frozen-guard.py --refreeze
"""
import hashlib, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / 'tools' / 'FROZEN.txt'

FROZEN = [
    'fep/fep-2026.md',
    'fep/index.html',
    'fep/fep-guidance.md',
]

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def refreeze():
    lines = ["# Frozen documents. Submitted, historical, never edited again.",
             "# Regenerate ONLY with Michelle's explicit approval:",
             "#   python3 tools/frozen-guard.py --refreeze", ""]
    for rel in FROZEN:
        p = ROOT / rel
        if p.exists():
            lines.append(f"{sha(p)}  {rel}")
    MANIFEST.write_text("\n".join(lines) + "\n", encoding='utf-8')
    print(f"re-froze {len(FROZEN)} path(s) into tools/FROZEN.txt")

def check():
    if not MANIFEST.exists():
        print("FROZEN.txt missing. Run: python3 tools/frozen-guard.py --refreeze")
        return 1
    want = {}
    for line in MANIFEST.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        h, rel = line.split(None, 1)
        want[rel.strip()] = h
    bad = []
    for rel, h in want.items():
        p = ROOT / rel
        if not p.exists():
            bad.append(f"  MISSING  {rel}  (a frozen document was deleted)")
        elif sha(p) != h:
            bad.append(f"  CHANGED  {rel}")
    if bad:
        print("FROZEN DOCUMENT MODIFIED. This is a submitted historical record.")
        print("\n".join(bad))
        print("\n  Restore it:  git checkout -- " + " ".join(want.keys()))
        print("  Do NOT re-freeze to make this pass unless Michelle said to change it.")
        return 1
    print(f"{len(want)} frozen document(s) intact")
    return 0

if __name__ == '__main__':
    sys.exit(refreeze() or 0 if '--refreeze' in sys.argv else check())
