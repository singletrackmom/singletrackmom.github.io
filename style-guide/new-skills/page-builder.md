---
name: page-builder
description: Build or update any page on Michelle Blomberg's portfolio site (singletrackmom.github.io) - an overview/case-study page, a tool page, a PRD, or a project page. Use whenever she asks to create, build, add, or redo a page, card, or section. Applies the website-style-guide skill and the WCAG 2.1 AA accessibility gate from the first draft.
---

# Page builder

**Goal:** every new or edited page is completely consistent with the current design system and fully accessible from the very first draft, so design drift (the #1 recurring problem) never happens.
**Audience:** portfolio visitors, including hiring managers, district leadership, and screen-reader users.
**Process:** read the website-style-guide skill for ALL styling and structure, clone the template, fill the content, pass the accessibility gate before calling it done.

## Start here
- **All type, color, headings, eyebrow, nav, tabs, footer, lists, callouts, layout, page anatomy, categories, and language rules live in the `website-style-guide` skill. Read it first and follow it exactly. Do NOT repeat or invent design values here.** That skill is the single source of truth and supersedes any older design notes in CLAUDE.md.
- Decide the page type FIRST (website content page vs an actual running tool or a presentation), per the website-style-guide skill. Tools and presentations keep their own chrome and take ONLY the standardized return footer, never the heading system.
- For a new overview/case-study page, clone `references/overview-template.html` rather than starting from scratch. Note: that template still reflects the older look, so bring it onto the current website-style-guide system before relying on it.
- Header, footer, and nav are locked and identical on every content page, exactly as the website-style-guide skill specifies (the name is the Home link; header nav is Work and About; the footer is the one fixed row plus copyright, nothing else).

## Accessibility gate (WCAG 2.1 AA, hard, before "done")
Skip-to-content link; one `<main id="main">`; exactly one `<h1>`, no skipped heading levels; `lang="en"`; unique descriptive `<title>`; every `<img>` real alt text (decorative `alt=""`); every interactive thing a real button or link (never a clickable div); visible `:focus-visible` outline (never `outline:none` with no replacement); every form control labelled; every iframe titled; text meets 4.5:1 contrast (use the `-text` variants for sage/gold/rose). Responsive: fluid max-widths, no fixed-px text containers, collapses to one column on phones, tap targets big enough.

## Sharing
- Any shareable page needs Open Graph tags with a raster `og:image` (1200x630 PNG at an absolute URL), plus `og:title`, `og:description`, `twitter:card=summary_large_image`. LinkedIn will not render an SVG preview, so covers used as share images must be exported to PNG.
- Never add a `download` attribute or link a `.docx`/`.xlsx`. Every link opens in the browser as HTML.

## Before calling any page done
Spot-check against the website-style-guide skill and an existing clean page: same nav, header, footer, heading colors and sizes, eyebrow, tabs, margins. If anything differs, fix it. Then run the full accessibility gate above.
