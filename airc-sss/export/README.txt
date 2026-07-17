LOCKED EXPORT CONFIG for the Student Journey Gap Analysis paper.
Source: airc-sss/_paper-source.html  ->  Student_Journey_Gap_Analysis.docx / .pdf
Every future export MUST use these files so the format never drifts again.

Locked choices: Carlito throughout (body and headings); ALL headings black
(not blue); TOC entries and page numbers black (colorlinks=false); block
paragraphs with no first-line indent and 6pt between paragraphs; ragged right
(left-aligned, never justified); 1 inch margins; centered footer page numbers;
cover page then Contents (depth 2) then body.

Files:
  header.tex    LaTeX header-includes for the PDF (xelatex).
  cover.tex     Cover page: title once at top, subtitle, title-less journey
                graphic (cover-notitle.png), two-line byline.
  reference.docx  Reference doc for the DOCX (Carlito, black headings/links).
  build.sh      Reproducible build. Run it to regenerate both files.

To rebuild: bash airc-sss/export/build.sh  (writes .docx and .pdf; pass an
output directory as the first argument, otherwise it prints one to set).
Uses: pandoc --toc --toc-depth=2, xelatex, Carlito font.
