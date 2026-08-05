---
name: website-style-guide
description: The single source of truth for the styling and structure of Michelle Blomberg's portfolio site (singletrackmom.github.io). READ AND APPLY on EVERY page create, edit, or review so type, color, headings, nav, footer, lists, callouts, and layout are identical everywhere and nothing drifts. Supersedes older design notes. The only exceptions are actual running tools and presentations (slide decks).
---

# Portfolio design system (singletrackmom.github.io)

The locked visual, structural, and language standard for Michelle's portfolio. Apply every rule from the first draft. When in doubt, clone an existing clean page and use body text; do not invent styles. Accessibility (WCAG 2.1 AA) and consistency are hard gates, not polish.

## Two page types (decide this FIRST)
Getting this wrong (stapling the heading system onto a tool) is the most common mistake.

**Website / content pages** get the full system (heading system, category eyebrow, page anatomy, lists, callouts, footer): the home/work/about pages, every project **overview**, and every **secondary tab** (PRD, "the case", doc tabs).

**Tool pages** get NONE of the heading system: no H2/H3, no eyebrow, no Goal/Audience/Process, no anatomy. They keep their own interface. The ONLY shared element they adopt is the standardized return footer link. Tool pages: the interactive tools (CopaMigo, Render, Dial Your Course, Syllabus Checker, Wayfinder), the built courses (Data Science, Light & Lasers, AVC pages), the family pages (Focus, Flow, Soar, Summer Work, Devan), and the newsletters (Rough Cut, the Flow volumes). If a heading ever got stuck on one (Flow), remove it.

## Fonts
- **Lora** (serif) for H1, H2, and the lead paragraph only.
- **DM Sans** for everything else (body, H3, eyebrow, tabs, footer, lists, callouts). Body base 15px, prose 1.03rem.

## Color roles (solid palette only, never gradients)
- `--ink #26221f` = H1 and body text.
- `--sage-text #456546` (green) = H2 headings, the category eyebrow, and bullet markers.
- `--muted #6d635f` (grey) = H3, captions, tabs/nav, subtitles, and the grey "answer" in a rail box.
- `--plum #7a5080` = **links and only links.**
- Backgrounds `#fff`. Rules/hairlines `--lav-line #d9c9e0` and `--rule #e5ddd1`.

**The link rule (Krug):** purple means link, nothing else. Never color a non-link purple, never a purple box. Headings are green (H2) or grey (H3). Inline links and every clickable thing are purple in all states (hover, active, visited). A reader must never wonder whether colored text is clickable.

## Heading system (levels follow document structure, not size)
One H1 per page, then H2 for top-level sections, H3 nested inside. Never skip levels. Never fake a heading with a styled `<p>`.
- **H1**: Lora, `--ink`, 1.9rem, weight 600, line-height ~1.15. The project or page name.
- **H2**: Lora, `--sage-text` green, 1.2rem, weight 600, **title case** (not uppercase). Short 1-to-4-word labels, never sentences (a sentence goes in the body).
- **H3**: DM Sans, `--muted` grey, 0.8rem, weight 700, **UPPERCASE**, letter-spacing 0.1em. Small-caps sub-label. Not serif, not italic.

Contrast on white: green ~6.6:1, grey ~5.8:1, both pass AA.

## Category eyebrow
Directly under the H1. DM Sans, `--sage-text` green, 0.72rem, weight 600-700, UPPERCASE, letter-spacing 0.12em, middot separators. **The eyebrow LEADS with the page type, then the category labels.** A portfolio work project starts with "Case study" then its categories (e.g. "Case study · AI Tools & Strategy · Learning Design"); the six personal projects (Wayfinder, Soar, Focus, Devan, Summer Work, Flow) use "Personal Projects" alone. After the type word, the category words must match the index page's category labels exactly. The category set is five, hard-coded per page, in this order: AI Tools & Strategy, Learning Design, UX Design, Teaching/Program Design, Personal Projects. **AI Tools & Strategy leads** because Michelle's top targets are AI builder and AI strategy roles; it covers both the tool/agent builds (Dial Your Course, CopaMigo, Render, Syllabus Checker, Cultivate) and the AI-strategy work (ARC domain co-chair, AIAC proposal, pilots-to-production framework, the Student Journey study), and it stands on its own beyond course design. Learning Design is course/experience design (the maker); Teaching/Program Design holds program-level work and classroom teaching (the leader, Program Director). A page may carry more than one label, separated by middots. Mines-style course-design emphasis is handled in the tailored resume/cover letter, not the portfolio order.

## Lead / deck paragraph
The description after the eyebrow/tabs. Lora **serif italic**, `--muted`, ~1.12-1.15rem. Semantically a normal `<p>` (never a heading, no special ARIA), after the H1 in reading order.

## Tabs (section nav)
**Tabs are ALWAYS real links to separate subpage files, never a JavaScript show/hide widget.** Each tab is its own HTML file with its own URL (`scope.html`, `method.html`, and so on), so a reload stays on the current tab and every tab can be bookmarked and shared. NEVER build tabs as in-page panels toggled by script (`role="tab"` buttons that hide and show sections on one file): those reset to the default tab on reload and cannot be linked to. The current tab carries `aria-current="page"`. When a tabbed page has page-specific CSS beyond `/assets/site.css`, put that CSS in ONE linked stylesheet the subpages share (single source of truth), never copied into every file. Reference implementations: the `synthetic-smes/` and `data-science-course/` tab sets. (Any legacy single-file JS-tab pages, for example the ARC hub, jeffco, mines, prep, and the Cultivate hub, should be migrated to this pattern when touched.)

Plain-text, **no pill buttons ever**. DM Sans, ~0.9rem, weight 500, **title case** (Overview, The Case, The Build Skill), `--muted`, a hair of letter-spacing (0.02em). Hover and active: `--plum` text with a 2px plum underline **under the word only** (not full width, not bold). Keep the underline tight to the word: `line-height:1.1` on the tab links and ~0.05rem bottom padding. When tabs wrap, use `gap:.35rem 1.4rem` so the second row isn't pushed far down. The header nav (Work, About; the name on the left IS the Home link, never add a separate Home) uses the identical treatment (purple + underline on hover).

## Header and footer (locked, identical on every page)
- **Header**: name (Lora) left (this is the Home link), a full-width `--lav-line` bottom rule, and Work / About on the right styled like the tabs. No separate Home link in the header.
- **Footer**: left-aligned, one fixed row: Home, Work, About, Email, Top ↑, then "© 2026 Michelle Blomberg. All rights reserved." DM Sans, `--muted`. **Nothing else in the footer.** **No bullets/middots between the footer links** (dropped): the links sit in a `.foot-links` flex row with even 1.4rem spacing.
- **Nav, tabs, and footer links share ONE underline treatment (Krug):** the header nav (Work, About), the tab bar, and the footer links are all DM Sans 0.9rem, weight 500, letter-spacing .02em, `--muted`, line-height 1.1, with a 2px transparent `border-bottom` that turns `--plum` on hover and for the current page, tight to the word (no horizontal padding, ~.05rem bottom padding). Same size and same leading in all three places. The "Work" underline is the reference.
- **Header rule, tab rule, and footer rule all line up.** The header bottom rule and tab bottom rule sit inset 1.5rem inside the 1000px band. The footer's top rule must match: it is an inset `.sitefoot::before` hairline (`left:1.5rem;right:1.5rem`), NOT a full-box `border-top` (which bleeds 1.5rem wider on each side). All three rules share the same left and right edges.

## Tool return link
Tool/course/interactive pages (no tab bar) get one standard return link: DM Sans, 0.8rem, weight 600, `--plum` (a link), UPPERCASE, letter-spacing 0.08em, **left-aligned to the margin**, leading ← arrow, same wording everywhere ("Back to overview"). Never centered, never another font.

## Lists
Real `<ul>`/`<ol>`, never boxes or bars faking bullets. Bullet markers are **green** at the left margin, hanging indent so wrapped text lines up under the first word. Ordered lists use **plain body-text numbers** (native `list-style:decimal`) so 10 and 11 align; do NOT fake numbers with a green ::before counter. **Labeled list:** when an item is a term plus its explanation, lead with the term in bold, then the explanation in body text. A list of items uses bullets, not rails.

```
ul.slist{padding-left:1.25rem;list-style:none}
ul.slist li{position:relative}
ul.slist li::before{content:"\2022";color:var(--sage-text);position:absolute;left:-1.25rem}
ol.slist{padding-left:1.5rem;list-style:decimal}
```

## Callout boxes (sparingly, only to flag something important)
Never the whole page, never nested, never purple. Two treatments:
- **Grey rail box**: a grey left rule beside the content, good for a question-and-answer or a term and its note. First part (question/term) is body text, bold if a label; the second part (the answer) may be grey at the **same size as body text**, never smaller.
- **Green box**: a filled pale-green callout (`#eff4ee` fill, `#cfe0cf` border) with plain body text, for one short important note.

## Layout and margins
Body text has a reading measure and stops part way across (max-width ~700-720px), left-aligned at the page's left margin; never full width. The header text and every rule line (header rule, tab rule, section dividers, footer rule) run the FULL width of the page band; a rule never stops at the text column. Tools are the only place content may span full width.

## Overview page anatomy (exact order, nothing floating loose)
1. Header. 2. H1 (project name). 3. Category eyebrow (green, matches index). 4. Tabs. 5. Lead (serif italic). 6. Hero image (real alt). 7. Goal, Audience, Process and any other sections as H2 with H3 nested. 8. Status line at the bottom, framed toward completion. 9. Footer. The only page with a hero and with Goal/Audience/Process.

## Secondary page anatomy
Identical to the overview minus the hero image. Its own H2/H3 sections (never Goal/Audience/Process). H1 matches its tab label, or a bit longer.

## PRD page (a secondary page with a fixed flow)
Every PRD uses the same numbered H2 flow so they read alike. H1 and browser title: "Product Requirements Document, [Project]". Flow: 1. Summary 2. Goal 3. Users and context 4. How it works 5. Data, privacy, and governance 6. Build and portability 7. Pilot and testing 8. Definition of success 9. Rollout 10. Open questions and risks 11. Roadmap.

## Page titles
Each page's H1 matches its tab label, or a slightly longer form when the tab is shortened (tab "The Case" -> H1 "The case for the method"). **Exception: the Overview tab.** Overview is the project's front page, so its H1 is the project name, not "Overview"; the highlighted active tab is the "you are here." Never write "Overview: Project name."

## Language and content
- **No ornamental drift, body text by default.** Do not invent type or box styles. A caption (small muted grey) is only for an actual image or chart caption. The only sanctioned callouts are the grey rail box and the green box. Everything else is plain body text.
- **Bold is functional, not decorative.** Bold only the short lead-in term of a labeled list item, or a genuine key term, sparingly. Never bold whole sentences; headings carry emphasis.
- **Voice.** Formal and professional, grounded in learning science. Concise, conceptually sharp, never padded. Precise instructional-design and UX vocabulary where accurate.
- **Title length.** H1 fits on one line where possible, two lines maximum, under ~45 characters. Tab labels are 1-3 words.
- **Call out all technology by name.** Adobe apps (Illustrator, Photoshop, After Effects, InDesign), Figma, Canvas, vanilla JS, the model and API, localStorage, IMSCC, AND the Google Workspace tools genuinely used (Docs and Drive folders for group work, Sheets, Forms, Apps Script). Google is a tool like any other. Never say "design software." Only name tools actually used.
- **Cite what needs citing.** External material, a framework, a study, or a course from another institution is attributed by name and linked to its source (e.g. a course from Colorado School of Mines says so and links the page). Follow the Grounding pattern: source, publication, live link.
- **Assessment and outcomes.** Do not include an Assessment or Outcomes section if there is genuinely nothing to report, but make a real effort to find something honest (a planned measure, a pilot metric, a usability result).
- **Status at the bottom**, framed toward the furthest honest state of completion so the work never reads as unfinished. Stay honest; never imply production a tool has not reached.

## Accessibility gate (every content page)
Skip-to-content link; one `<main id="main">`; `lang="en"`; unique descriptive `<title>`; exactly one H1, no skipped levels; every img real alt (decorative `alt=""`); real `<button>`/`<a>` for anything interactive; visible `:focus-visible` outline; labelled form controls; titled iframes; text at 4.5:1. Responsive: fluid widths, one column on phones, big tap targets. Shareable pages need Open Graph tags with a raster PNG `og:image` (1200x630), never SVG.

## Writing marks
No em dashes ever (commas, periods, parentheses, or the middot). Always curly quotes and apostrophes, never straight or prime marks. Never justify body text; always left-aligned ragged right. Card descriptions lead with action verbs (Led, Built, Advised), not "I". Every project, tool, PRD, and card states Goal, Audience, and Process, clearly labeled.


## Preserved exceptions and rules (keep these)
- **Presentations exception.** Slide decks are self-contained and keep their own chrome, like tools. Tools and presentations are the only two exceptions to this style guide.
- **Canvas-view exception.** The styled "Canvas view" of a course uses Montserrat (headings) + Open Sans (body) with the Mines-blue palette, because it must look like Canvas. That is the ONLY place those fonts or that palette appear. Everything else on the site uses Lora + DM Sans and the palette above.
- **Metrics section.** On an overview, include a **Metrics** section ONLY if the project has real metrics; otherwise leave the heading off entirely. Overview section order: Goal, Audience, Process, Technology (always a bulleted list, comprehensive), Metrics (only if any), Status (last).
- **First person.** Use first person ("I", "my") only inside a real quote or on the About page. Everywhere else, write about the work, not "I".
- **Bundled template.** For a new overview/case-study page, clone `page-builder/references/overview-template.html` rather than starting from scratch (note: bring that template to this current system before relying on it).
