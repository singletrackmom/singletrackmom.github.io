---
name: website-style-guide
description: The single source of truth for the styling and structure of Michelle Blomberg's portfolio site (singletrackmom.github.io). Apply on EVERY page create or edit so type, color, navigation, and layout are identical everywhere. Use whenever building or touching any page, so nothing drifts and no random styles appear. The ONLY exceptions to every rule here are presentations (slide decks) and actual running tools.
---

**Goal:** every page on the site looks like it came from the same hand. Same type, same palette, same header, same navigation, same footer. No exceptions, no one-off styles, no gradients.

## Two page kinds
1. **Content pages** (overviews, case studies, PRDs, docs, sub-pages): get the full standard chrome below, including the tab-nav heading.
2. **Actual tools** (the live interactive apps, e.g. the Dial tool, a builder) and **presentations** (slide decks): keep their own chrome. Tools keep ONLY a single back button at the BOTTOM and do NOT get the tab-nav heading. Presentations are self-contained. These two are the ONLY exceptions to this style guide.

If it is not the running tool itself, it is a content page and takes the standard heading.

## Type (never change)
- Headings (h1, h2, h3) and card titles: **Lora**, serif, weight 600.
- Body, eyebrow, nav, tabs, footer: **DM Sans**, sans-serif.
- Load both from Google Fonts. Exception, documented: the "styled Canvas view" of a course uses **Montserrat** (headings) + **Open Sans** (body) with the Mines-blue palette, because it must look like Canvas. That is the ONLY place those fonts or that palette appear.

## Palette (solid colors only, NO gradients ever)
:root{--ink:#26221f;--rule:#e5ddd1;--lav:#f7f4f8;--lav-line:#d9c9e0;--plum-pale:#f7f4f8;--warm:#f4efe8;--muted:#6d635f;--plum:#7a5080;--sage:#6b8f6e;--sage-text:#456546}
- Body text --ink. Muted/secondary --muted. Accent/links/active-nav underline --plum. Eyebrow green --sage-text. Hairlines --lav-line / --rule.

## Standard page structure (content pages), top to bottom
1. `.site-head` bar: "Michelle Blomberg" (links home) on the left, Primary nav (Home / Work / About) on the right, hairline under it.
2. `<main id="main">` and then, in this exact order with NOTHING above the title:
   - `<h1>` (Lora). The h1 is ALWAYS the first element in main. Never put a back link, step bar, or anything above it.
   - `<p class="eyebrow">` uppercase, letter-spaced, --sage-text green. Format: `Case study &middot; <Project or section>`. Same string on every page of a project.
   - The **tab nav** (see below), sitting between the eyebrow and the opening paragraph.
   - `<p class="lead-sub">` the opening paragraph.
   - Content.
3. `.sitefoot` footer: `Home &middot; Work &middot; About &middot; Email &middot; Top &uarr;` then the copyright line. The `Top &uarr;` link is required.

## The tab nav (the ONLY secondary navigation)
Every content page in a project carries the same horizontal tab bar. Purple hairline underline on the current tab. It replaces ALL of: purple pill buttons, "Next" buttons, floating "← back" links, and numbered step bars. Those are retired everywhere.

CSS (verbatim):
.tabs{border-bottom:1px solid var(--lav-line);margin:1.3rem 0 1.7rem;display:flex;flex-wrap:wrap;gap:0.15rem}
.tabs a.tab{border-bottom:2px solid transparent;font-family:'DM Sans',sans-serif;font-size:0.9rem;font-weight:500;color:var(--muted);padding:0.55rem 0.85rem;margin-bottom:-1px;text-decoration:none;line-height:1.3}
.tabs a.tab:hover{color:var(--ink)}
.tabs a.tab[aria-current="page"]{color:var(--ink);border-bottom-color:var(--plum);font-weight:600}

Markup:
  <nav class="tabs" aria-label="<Project> sections">
    <a class="tab" href="/proj/">Overview</a>
    <a class="tab" href="/proj/page.html" aria-current="page">This page</a>
    ...
  </nav>
- Tabs list that project's content pages, in reading order, Overview first.
- The current page's tab gets `aria-current="page"` (this is what draws the purple underline).
- A minimal project (only an Overview and a PRD) STILL gets the bar, even with just two tabs. Consistency over brevity.
- Deep-dive pages that are not their own tab highlight their parent tab.

## Rules that keep it bulletproof
- No gradients. No new accent colors. No pill-shaped buttons. No inline one-off font sizes for headings.
- Goal / Audience / Technology (and Process / Status) labeled sections belong ONLY on overview pages. Other pages tell their story in prose.
- Cards: work page uses `.card/.thumb/.cbody/.ct/.cd`; homepage featured uses `.feat-*`. Do not invent new card shapes.
- Accessibility: skip link, semantic headings, WCAG AA contrast, visible focus. Alt text that says something.
- First person ("I", "my") only in a real quote or on the About page. Everywhere else, write about the work.
- Curly quotes and apostrophes only. Never em dashes (use commas, periods, parentheses, or a middot).

## Overview page sections (identical on every overview)
Every overview uses these labeled sections, in this order and with these exact names:
1. **Status** — FIRST, and required on every overview. One line on where the project stands (e.g. Prototype, In testing, Built and running).
2. **Goal**
3. **Audience**
4. **Process**
5. **Technology** — always this word. Never "Built with", never "The technology".
6. **Metrics** — LAST, and included ONLY if the project actually has metrics; otherwise leave the heading off entirely.

Do not invent other section names on an overview. If a project has selected work or a client list, that is fine as extra content, but the six above are the standard spine.

## Tab-nav labels
Words only, never numbers. Each tab label is a SHORT version of that page's own title (e.g. "The case for synthetic SMEs" -> "The case"; "Instructor Prep Kit" -> "Instructor prep"). The first tab is always "Overview".

## PRDs and docs
PRDs are content pages. They take the standard header (h1, eyebrow, tab nav) and the site palette and type. If a PRD still uses an older look, bring it to this standard rather than leaving a second style alive.
