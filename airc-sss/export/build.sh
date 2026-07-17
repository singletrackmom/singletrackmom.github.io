#!/usr/bin/env bash
# ============================================================
# LOCKED, reproducible export for the Student Journey Gap Analysis.
# Source: airc-sss/_paper-source.html
# Outputs: Student_Journey_Gap_Analysis.docx and .pdf
# Usage: bash airc-sss/export/build.sh [OUTPUT_DIR]
# Every future export MUST run this so the format never drifts.
# Locked choices are in README.txt / header.tex / reference.docx / cover.tex.
# ============================================================
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"       # airc-sss/export
AIRC="$(dirname "$HERE")"                    # airc-sss
SRC="$AIRC/_paper-source.html"
GRAPHIC="$AIRC/cover-notitle.png"
OUT="${1:-$AIRC/export/out}"
mkdir -p "$OUT"
BASE="Student_Journey_Gap_Analysis"
TMP="$(mktemp -d)"

# Preprocess: drop the in-body cover paragraphs (title lives on the cover page)
# and the <title> element (so pandoc emits no duplicate \maketitle).
sed -e '/class="doctitle"/d;/class="docsub"/d;/class="docauth"/d' \
    -e 's#<title>[^<]*</title>##' "$SRC" > "$TMP/paper.html"

# Copy local images into the temp dir so the docx pandoc run can embed them.
cp "$AIRC"/*.png "$TMP"/ 2>/dev/null || true

# ---- PDF (xelatex, Carlito, black headings, black TOC, ragged right) ----
export TEXINPUTS="$AIRC:"   # so cover-notitle.png resolves from cover.tex
pandoc "$TMP/paper.html" \
  --pdf-engine=xelatex \
  --toc --toc-depth=2 \
  -V colorlinks=false \
  -V papersize=letter \
  --include-in-header="$HERE/header.tex" \
  --include-before-body="$HERE/cover.tex" \
  -o "$OUT/$BASE.pdf"

# ---- DOCX (Carlito, black headings/links via reference.docx) ----
pandoc "$TMP/paper.html" \
  --toc --toc-depth=2 \
  --reference-doc="$HERE/reference.docx" \
  -o "$TMP/$BASE.docx"
python3 "$HERE/finish_docx.py" "$TMP/$BASE.docx" "$GRAPHIC"
cat "$TMP/$BASE.docx" > "$OUT/$BASE.docx"   # copy (mount blocks delete/mv)

rm -rf "$TMP"
echo "Built: $OUT/$BASE.pdf  and  $OUT/$BASE.docx"
