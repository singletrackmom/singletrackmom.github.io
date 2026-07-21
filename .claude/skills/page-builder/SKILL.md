---
name: page-builder
description: Build or update any page on Michelle Blomberg's portfolio site (singletrackmom.github.io) - an overview/case-study page, a tool page, or a project page. Use whenever she asks to create, build, add, or redo a page, card, or section on the site. Enforces the one design system and WCAG 2.1 AA accessibility from the first draft.
---

# Page builder

**Goal:** every new page is completely consistent with the existing design system and fully accessible from the very first draft, so design drift (the #1 recurring problem) never happens.
**Audience:** visitors to the portfolio, including hiring managers, district leadership, and screen-reader users.
**Process:** start from the bundled template, keep the locked header/footer/nav, fill Goal/Audience/Process, pass the accessibility gate before calling it done.

## Start here
- Clone `references/overview-template.html` (in this skill folder) for a new overview/case-study page. It is a neutral, blank version of the canonical layout, not tied to any one project. Do NOT start from scratch and do NOT invent per-page styles.
- Header, footer, and nav are LOCKED and identical on every page: `.site-head` with the name link left and exactly three plain-text nav links (Home, Work, About) right; `.sitefoot` outside the content wrapper with Home, Work, About, Email, Top. Never add a page-specific nav link. Never use pill nav.

## The one design system (exact values, no exceptions)
- Fonts: Lora (serif) for headings/titles ONLY; DM Sans for everything else. Body base 15px.
- Colors: `--ink:#26221f` (headings + body), `--muted:#6d635f` (subtitles, nav, captions), `--rule:#e5ddd1`, `--warm:#f4efe8` (thumbnails), `--plum:#7a5080` + `--sage:#6b8f6e` (accents). Background always #fff.
- BOX FILL, ONE COLOR: every filled box (cards, callouts, notes, panels, stat/definition boxes) is `#f7f4f8` (available as both `--lav` and `--plum-pale`). Borders `--lav-line:#d9c9e0`. Never a second tint. Controls sitting on a filled box (pill links) are white #fff. A pill means it is a link; never put a non-clickable pill/chip on a card.
- Type sizes: page-title h1 = 1.9rem Lora; homepage hero = 2rem Lora; subtitle/lead-in = 1.08rem `--muted`; body prose = 1.03rem `--ink`; eyebrow = 0.72rem uppercase, letter-spacing 0.12em, `--sage-text` or `--muted`; card description = 0.82rem `--muted`.
- Layout: `main` and `header` both max-width 1000px, centered, padding 2.4rem 1.5rem. Left edges line up. Never double-wrap content in a second padded container. Title is the first element, same top spot on every page.
- Eyebrow, if used, goes UNDER the title. Consistent category labels: "AI tools & strategy", "In the classroom", "Agentic & personal build", "Experiential learning".
- Solid palette colors ONLY. Never gradients or blended/multi-stop colors anywhere.

## Overview vs tool (the split)
- An overview page is the case study: cover image, Goal / Audience / Process prose, and a primary link to the real tool.
- The tool itself carries NO Goal / Audience / Process description; it just does its job. Never duplicate the description on both.
- Goal, Audience, and Process must all appear, clearly labeled, on every overview/project page.
- The **Technology** (or "Built with") section is ALWAYS a bulleted list (`ul.stack`), never a paragraph, and should be comprehensive, matching the depth of the other overviews: the build method, the design logic and standards, the assessment approach, the OER/tools (license-noted), the instructor materials, and how it is delivered.

## Accessibility gate (WCAG 2.1 AA, hard, before "done")
Skip-to-content link; one `<main id="main">`; exactly one `<h1>`, no skipped heading levels; `lang="en"`; unique descriptive `<title>`; every `<img>` real alt text (decorative `alt=""`); every interactive thing a real button or link (never a clickable div); visible `:focus-visible` outline (never `outline:none` with no replacement); every form control labelled; every iframe titled; text meets 4.5:1 contrast. Sage, gold, rose FAIL as text on white, use the `-text` variants: `--sage-text:#456546`, `--gold-text:#75592c`, `--rose-text:#94395a`. Responsive: fluid max-widths, no fixed-px text containers, collapses to one column on phones, tap targets big enough.

## Sharing
- Any shareable page needs Open Graph tags with a raster `og:image` (1200x630 PNG at an absolute URL), plus `og:title`, `og:description`, `twitter:card=summary_large_image`. LinkedIn will not render an SVG preview, so covers used as share images must be exported to PNG.
- Never add a `download` attribute or link a `.docx`/`.xlsx`. Every link opens in the browser as HTML.

## Writing
- No em dashes ever (use commas, periods, parentheses, or the middot separator). Curly quotes and apostrophes only. Card descriptions lead with action verbs (Led, Built, Advised), never "I".
- Be honest about status: prototype, in testing, or pilot. Never imply production.

## Before calling any page done
Spot-check against an existing clean page: same nav, same title size and position, same body color/size, same padding, same eyebrow placement. If anything differs, fix it.
