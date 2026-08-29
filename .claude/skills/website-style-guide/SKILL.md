---
name: website-style-guide
description: The single source of truth for the styling, structure, accessibility, and language of Michelle Blomberg's portfolio site (singletrackmom.github.io). READ AND APPLY on EVERY page create, edit, or review so type, color, headings, nav, footer, lists, callouts, and layout are identical everywhere and nothing drifts. Also holds the mandatory design-lint procedure, the WCAG 2.1 AA gate, the exact palette and type values, and the hard document rules (no gradients, no em dashes, curly quotes, never justify text, PNG social images, no downloadable-document links, PRDs as HTML). Supersedes older design notes. The only exceptions are actual running tools and presentations (slide decks).
---

# Portfolio design system (singletrackmom.github.io)

The locked visual, structural, and language standard for Michelle's portfolio. Apply every rule from the first draft. When in doubt, clone an existing clean page and use body text; do not invent styles. Accessibility (WCAG 2.1 AA) and consistency are hard gates, not polish steps.

The canonical page to clone is `wayfinder/overview.html`. For a new overview or case-study page, clone an existing clean page rather than starting fresh.

---

## RUN THE DESIGN CHECK. MANDATORY, EVERY TIME, NO EXCEPTIONS.

There is an automated checker. Run it. Do not eyeball the design rules, do not promise Michelle the pages are consistent, RUN IT and paste the result.

```
python3 tools/design-lint.py
```

Add `--all` to include the family and tool pages.

**When to run it, all of these:**
- **BEFORE** telling Michelle any page is done, finished, fixed, or ready.
- **AFTER** creating any new HTML page.
- **AFTER** editing any existing page, even a one-line change.
- **AFTER** any bulk or find-and-replace operation across files. (A blind find-and-replace corrupted body copy on 16 Aug 2026. The checker exists because of that.)
- Any time Michelle says "run the design check," "audit the site," or asks whether the pages are consistent.

**What it catches:** header/main/footer width mismatches that shift content sideways, the old `.tabs` padding that indents tabs 14px right of the h1, double padding inside `main`, footers stuck inside `<main>`, `--ink` overrides, em dashes, straight quotes in prose, gradients, missing `lang`, missing or duplicate `<h1>`, missing skip links, `<main>` without `id="main"`, clickable divs, images without alt, eyebrows above the title instead of under it, nav link drift, sage/gold/rose used as text where they fail 4.5:1 contrast, broken internal links, unbalanced containers, unrendered `${...}` template literals outside `<script>`, curly quotes used as JS string delimiters, unfilled placeholders, and find-and-replace leftovers.

**Rules for using it:**
- It exits non-zero if anything CRITICAL is found. **CRITICAL must be fixed before shipping.**
- Fix what it names, then **run it again** to confirm. Never fix-and-assume.
- If it reports something that is a false positive (redirect stubs, Canvas course exports, family tool pages), **fix the checker's scope**, do not ignore the finding and move on.
- Michelle never runs this herself and never opens the file. It is an assistant tool. Report results in plain language: what was broken, what was fixed, what is clean.

**Scope.** Full chrome rules apply to the portfolio surface: root `index.html` / `work.html` / `about.html`, plus `render/`, `copamigo/`, `course-dialer/`, `wayfinder/`, `cultivate/`, `airc-sss/`, `style-guide/`, and every `overview.html` and `prd.html`.

Family and tool pages (`flow/`, `focus/`, `soar/`, `summerwork/`, `jobs/`, `command/`, `lunch/`) get **universal rules only**, no portfolio chrome, and **no eyebrows**. Their `overview.html` case-study pages are NOT exempt and DO carry eyebrows.

Deliberately standalone pages that must NOT carry portfolio chrome (do not "fix" them): `copamigo/widget.html` (embeddable widget in an iframe on another site), `render/render-maya.html` and `render/render-riley.html` (exported student dashboards that must work offline). Redirect stubs, `.private.html` working sheets, and Canvas page fragments (no `<html>`/`<body>` by design) are also exempt from document-level rules.

---

## Two page types (decide this FIRST)
Getting this wrong (stapling the heading system onto a tool) is the most common mistake.

**Website / content pages** get the full system (heading system, category eyebrow, page anatomy, lists, callouts, footer): the home/work/about pages, every project **overview**, and every **secondary tab** (PRD, "the case", doc tabs).

**Tool pages** get NONE of the heading system: no H2/H3, no eyebrow, no Goal/Audience/Process, no anatomy. They keep their own interface. The ONLY shared element they adopt is the standardized return footer link. Tool pages: the interactive tools (CopaMigo, Render, Dial Your Course, Syllabus Checker, Wayfinder), the built courses (Data Science, Light & Lasers, AVC pages), the family pages (Focus, Flow, Soar, Summer Work, Devan), and the newsletters (Rough Cut, the Flow volumes). If a heading ever got stuck on one (Flow), remove it.

**Overview vs tool, the split.** An overview page is the case study: cover image, Goal / Audience / Process prose, and a primary link out to the real tool. The tool itself carries NO Goal / Audience / Process description; it just does its job. **Do not duplicate the description on both.**

## Fonts
- **Lora** (serif) for headings and titles ONLY: H1, H2, and the lead paragraph.
- **DM Sans** for everything else (body, H3, eyebrow, tabs, footer, lists, callouts). **Body base 15px**, prose 1.03rem.

## Color roles (solid palette only, never gradients)
Use these EXACT values. Never invent off-palette hex values.

| Variable | Value | Role |
|---|---|---|
| `--ink` | `#26221f` | H1, headings, and body prose. **Never override it.** |
| `--muted` | `#6d635f` | H3, subtitles, captions, tabs and nav, the grey "answer" in a rail box |
| `--rule` | `#e5ddd1` | borders |
| `--warm` | `#f4efe8` | thumbnails |
| `--plum` | `#7a5080` | **links and only links** |
| `--sage` | `#6b8f6e` | accent (not text) |
| `--lav` / `--plum-pale` | `#f7f4f8` | the one box fill, see below |
| `--lav-line` | `#d9c9e0` | borders on filled boxes, header/tab/footer rules |
| `--sage-text` | `#456546` | green as TEXT: H2, category eyebrow, bullet markers |
| `--gold-text` | `#75592c` | gold as TEXT |
| `--rose-text` | `#94395a` | rose as TEXT |

Background is always `#fff`.

**Accessible text variants are mandatory.** `--sage`, `--gold`, and `--rose` FAIL 4.5:1 as text on white. Use `--sage-text #456546`, `--gold-text #75592c`, `--rose-text #94395a` instead. Contrast on white: green about 6.6:1, grey about 5.8:1, both pass AA.

**BOX FILL, ONE COLOR, NO EXCEPTIONS.** Every filled box on the site (cards, callouts, notes, panels, stat boxes, definition boxes) is the screened purple `#f7f4f8`, the exact value already used by the cards on `index.html` and `work.html`. It is available as both `--lav` and `--plum-pale`; they are the same color on purpose. Never `#ede4f2`, never `--warm`, never a second tint, never a percentage variation. Borders on those boxes are `--lav-line #d9c9e0`. Controls that sit ON a filled box (pill links) are white `#fff` so they read as controls. **Do not put non-clickable pills or chips on a card: a pill means it is a link.**

**The link rule (Krug):** purple means link, nothing else. Never color a non-link purple, never a purple box. Headings are green (H2) or grey (H3). Inline links and every clickable thing are purple in all states (hover, active, visited). A reader must never wonder whether colored text is clickable.

## Heading system (levels follow document structure, not size)
One H1 per page, then H2 for top-level sections, H3 nested inside. Never skip levels. Never fake a heading with a styled `<p>`.
- **H1**: Lora, `--ink`, **1.9rem**, weight 600, line-height about 1.15. The project or page name. (The homepage hero is 2rem Lora.)
- **H2**: Lora, `--sage-text` green, 1.2rem, weight 600, **title case** (not uppercase). Short 1-to-4-word labels, never sentences (a sentence goes in the body).
- **H3**: DM Sans, `--muted` grey, 0.8rem, weight 700, **UPPERCASE**, letter-spacing 0.1em. Small-caps sub-label. Not serif, not italic.

**Other exact type sizes:** subtitle / lead-in = **1.08rem `--muted`**; body prose = **1.03rem `--ink`**; eyebrow = 0.72rem uppercase, letter-spacing 0.12em; card description = 0.82rem `--muted`.

The title sits at the same top spot on every page (2.4rem below the header, first element, no eyebrow pushing it down).

## Category eyebrow
Directly under the H1 (never above it). DM Sans, `--sage-text` green, 0.72rem, weight 600 to 700, UPPERCASE, letter-spacing 0.12em, middot separators.

**The eyebrow LEADS with the page type, then the category labels.** A portfolio work project starts with "Case study" then its categories (for example "Case study · AI Tools & Strategy · Learning Design"); the six personal projects (Wayfinder, Soar, Focus, Devan, Summer Work, Flow) use "Personal Projects" alone.

After the type word, the category words must match the index page's category labels exactly. The category set is five, hard-coded per page, in this order: **AI Tools & Strategy, Learning Design, UX Design, Teaching/Program Design, Personal Projects.** **AI Tools & Strategy leads** because Michelle's top targets are AI builder and AI strategy roles; it covers both the tool/agent builds (Dial Your Course, CopaMigo, Render, Syllabus Checker, Cultivate) and the AI-strategy work (ARC domain co-chair, AIAC proposal, pilots-to-production framework, the Student Journey study), and it stands on its own beyond course design. Learning Design is course/experience design (the maker); Teaching/Program Design holds program-level work and classroom teaching (the leader, Program Director). A page may carry more than one label, separated by middots. Mines-style course-design emphasis is handled in the tailored resume and cover letter, not the portfolio order.

Older label wording still in use on some pages: "AI tools & strategy," "In the classroom," "Agentic & personal build," "Experiential learning." Bring those to the five-category set when a page is touched.

## Lead / deck paragraph
The description after the eyebrow/tabs. Lora **serif italic**, `--muted`, about 1.12 to 1.15rem. Semantically a normal `<p>` (never a heading, no special ARIA), after the H1 in reading order.

## Tabs (section nav)
Plain-text, **no pill buttons ever**. DM Sans, about 0.9rem, weight 500, **title case** (Overview, The Case, The Build Skill), `--muted`, a hair of letter-spacing (0.02em). Hover and active: `--plum` text with a 2px plum underline **under the word only** (not full width, not bold). Keep the underline tight to the word: `line-height:1.1` on the tab links and about 0.05rem bottom padding. When tabs wrap, use `gap:.35rem 1.4rem` so the second row is not pushed far down.

**Never use the old `.tabs a.tab{padding:0.55rem 0.85rem}`**, it indents the tabs about 14px right of the h1. The linter flags it as CRITICAL.

**Tabs are ALWAYS real links to separate subpage files, never a JavaScript show/hide widget.** Each tab is its own HTML file with its own URL (`scope.html`, `method.html`, and so on), so a reload stays on the current tab and every tab can be bookmarked and shared. NEVER build tabs as in-page panels toggled by script (`role="tab"` buttons that hide and show sections on one file): those reset to the default tab on reload and cannot be linked to. The current tab carries `aria-current="page"`. When a tabbed page has page-specific CSS beyond `/assets/site.css`, put that CSS in ONE linked stylesheet the subpages share (single source of truth), never copied into every file. Reference implementations: the `synthetic-smes/` and `data-science-course/` tab sets. (Any legacy single-file JS-tab pages, for example the ARC hub, jeffco, mines, prep, and the Cultivate hub, should be migrated to this pattern when touched.)

## Layout and margins (locked)
- `main`, `header`, and `footer` all share **`max-width:1000px; margin:0 auto`**, with `padding: 2.4rem 1.5rem` on the content band. The linter treats any mismatch as CRITICAL.
- The left edge of the header and the content MUST line up. **Never double-wrap content in a second padded container** (an inner `.wrap` re-padding inside an already padded `main` shifts content right; CRITICAL).
- Body text has a reading measure and stops part way across (max-width about 700 to 720px), left-aligned at the page's left margin; never full width. **Tools are the only place content may span full width.**
- The header text and every rule line (header rule, tab rule, section dividers, footer rule) run the FULL width of the page band; a rule never stops at the text column.

## Header and footer (LOCKED, identical on every page, never stray)
Every page on the site (home, work, about, every overview page, and every tool page) uses the IDENTICAL header and footer markup and styles. Do not change widths, borders, colors, or link sets on a per-page basis.

**Header** = `.site-head` (max-width 1000px, padding `1.4rem 1.5rem 0`) containing `.site-bar` (bottom border `--lav-line`) with the name link (Lora) on the left and `.site-nav` on the right.

**Navigation is IDENTICAL on every page:** `.site-nav` holds exactly three plain-text links, **Home, Work, About**, in `--muted`, with no borders or background. NEVER pill buttons on some pages and text on others. **Never add a page-specific link** (no "Overview," no tool name) to the nav. No leftover old CSS (for example `header nav a` pills) leaking in. The linter checks the nav link list and flags drift.

> **Open tension to confirm with Michelle before changing anything.** A newer draft of this guide described the header as the name-on-the-left acting AS the Home link with only Work and About on the right, and no separate Home link. The live pages and `tools/design-lint.py` both enforce the three-link Home / Work / About set. **Follow the linter (three links) unless Michelle says otherwise**, and if the two-link version is what she wants, update the linter's nav check in the same pass so the rule stays enforceable.

**Footer** = `.sitefoot` (max-width 1000px), sitting **OUTSIDE** the content wrapper so its left edge lines up. A footer stuck inside `<main>` is CRITICAL. Left-aligned, one fixed row: **Home, Work, About, Email, Top ↑**, then "© 2026 Michelle Blomberg. All rights reserved." DM Sans, `--muted`. **Nothing else in the footer.**

**No bullets or middots between the footer links** (dropped): the links sit in a `.foot-links` flex row with even 1.4rem spacing. (Older pages using `Home · Work · About · Email · Top ↑` at 0.85rem with middot separators are the superseded form; bring them to `.foot-links` when touched.)

**Nav, tabs, and footer links share ONE underline treatment (Krug):** the header nav, the tab bar, and the footer links are all DM Sans 0.9rem, weight 500, letter-spacing .02em, `--muted`, line-height 1.1, with a 2px transparent `border-bottom` that turns `--plum` on hover and for the current page, tight to the word (no horizontal padding, about .05rem bottom padding). Same size and same leading in all three places. The "Work" underline is the reference.

**Header rule, tab rule, and footer rule all line up.** The header bottom rule and tab bottom rule sit inset 1.5rem inside the 1000px band. The footer's top rule must match: it is an inset `.sitefoot::before` hairline (`left:1.5rem;right:1.5rem`), NOT a full-box `border-top` (which bleeds 1.5rem wider on each side). All three rules share the same left and right edges.

Portfolio pages must load `/assets/site.css` so the shared header and footer styles apply.

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

Any other filled box on the site uses the one box fill `#f7f4f8` with a `--lav-line` border.

## Overview page anatomy (exact order, nothing floating loose)
1. Header. 2. H1 (project name). 3. Category eyebrow (green, matches index). 4. Tabs. 5. Lead (serif italic). 6. Hero image (real alt). 7. Goal, Audience, Process and any other sections as H2 with H3 nested. 8. Status line at the bottom, framed toward completion. 9. Footer. The only page with a hero and with Goal/Audience/Process.

**The Goal heading ALWAYS comes directly under the hero image.** Never place a paragraph, a specs/fact line, or any body text between the hero and the Goal heading. Anything that would otherwise land there (a specs line, a method note) goes above the hero (right under the lead) or into the relevant section (Technology, Process), never between hero and Goal.

## Secondary page anatomy
Identical to the overview minus the hero image. Its own H2/H3 sections (never Goal/Audience/Process). H1 matches its tab label, or a bit longer.

## PRD page (a secondary page with a fixed flow)
Every PRD uses the same numbered H2 flow so they read alike. H1 and browser title: "Product Requirements Document, [Project]". Flow: 1. Summary 2. Goal 3. Users and context 4. How it works 5. Data, privacy, and governance 6. Build and portability 7. Pilot and testing 8. Definition of success 9. Rollout 10. Open questions and risks 11. Roadmap.

**PRDs and all documents are HTML pages, never Word or Excel.** Build and link `.html`, not `.docx` or `.xlsx`. Render's PRD is green; Cultivate's is plum.

## Page titles
Each page's H1 matches its tab label, or a slightly longer form when the tab is shortened (tab "The Case" becomes H1 "The case for the method"). **Exception: the Overview tab.** Overview is the project's front page, so its H1 is the project name, not "Overview"; the highlighted active tab is the "you are here." Never write "Overview: Project name."

## Language and content
- **No ornamental drift, body text by default.** Do not invent type or box styles. A caption (small muted grey) is only for an actual image or chart caption. The only sanctioned callouts are the grey rail box and the green box. Everything else is plain body text.
- **Bold is functional, not decorative.** Bold only the short lead-in term of a labeled list item, or a genuine key term, sparingly. Never bold whole sentences; headings carry emphasis.
- **Voice.** Formal and professional, grounded in learning science. Concise, conceptually sharp, never padded. Precise instructional-design and UX vocabulary where accurate.
- **Title length.** H1 fits on one line where possible, two lines maximum, under about 45 characters. Tab labels are 1 to 3 words.
- **Call out all technology by name.** Adobe apps (Illustrator, Photoshop, After Effects, InDesign), Figma, Canvas, vanilla JS, the model and API, localStorage, IMSCC, AND the Google Workspace tools genuinely used (Docs and Drive folders for group work, Sheets, Forms, Apps Script). Google is a tool like any other. Never say "design software." Only name tools actually used.
- **Cite what needs citing.** External material, a framework, a study, or a course from another institution is attributed by name and linked to its source (for example, a course from Colorado School of Mines says so and links the page). Follow the Grounding pattern: source, publication, live link.
- **Assessment and outcomes.** Do not include an Assessment or Outcomes section if there is genuinely nothing to report, but make a real effort to find something honest (a planned measure, a pilot metric, a usability result).
- **Status at the bottom**, framed toward the furthest honest state of completion so the work never reads as unfinished. Stay honest; never imply production a tool has not reached.
- **Card descriptions** do not start with "I". Use action verbs (Led, Built, Advised).

## Accessible and responsive from the FIRST draft (non-negotiable)
Every page is built WCAG 2.1 AA accessible and mobile-responsive from the very first draft. **Never ship a page that is not compliant and then fix it later, that wastes hours.** This is a hard gate, not a polish step.

Before calling any page done it MUST have:
- a skip-to-content link
- one `<main id="main">`
- exactly one `<h1>`, with no skipped heading levels
- `lang="en"`
- a unique, descriptive `<title>`
- every `<img>` with real alt text (decorative ones `alt=""`)
- every interactive thing a real `<button>` or `<a>`, **never a clickable div**
- a visible `:focus-visible` outline (never `outline:none` with no replacement)
- every form control labelled
- every iframe titled
- all text meeting 4.5:1 contrast (use the `-text` variants for sage, gold, rose)

**Responsive:** fluid max-widths, no fixed-px text containers, layouts collapse to one column on phones, tap targets big enough.

**Social sharing:** any page Michelle might share (LinkedIn especially) needs Open Graph tags with a **raster `og:image` (a 1200x630 PNG at an absolute URL)**, plus `og:title`, `og:description`, and `twitter:card=summary_large_image`. **Always a PNG, never an SVG.** LinkedIn and other platforms will not render an SVG as a preview image, so covers used as share images must be exported to PNG.

## Hard document and writing rules (never break)
- **Solid colors only, and only from the defined palette. NEVER use gradients** or blended / multi-stop colors anywhere (headings, hero bars, backgrounds, swatches). Blends look muddy and AI-generated. If an element needs color, pick one solid palette variable. The linter treats any `gradient(` as CRITICAL.
- **Never use em dashes** anywhere, in text or in UI. Use commas, periods, parentheses, or the middot ( · ) separator the site already uses.
- **Always use correct typographic quotes.** Curly double quotes (“ ”) and curly apostrophes / single quotes (‘ ’). Never straight quotes (" ') and never prime or double-prime marks (′ ″). This applies to web pages, documents, slide decks, everything. (Exception in code: a curly quote used as a JavaScript string delimiter breaks the parser and renders raw code on screen; the linter flags it.)
- **Never justify body text in any document, ever.** Always left-aligned, ragged right. Justified text is not acceptable in docx, PDF, slides, HTML, or anything. Permanent, global rule.
- **Never link a downloadable document on the website.** No `.docx` or `.xlsx` links and no `download` attribute on any link. Every link must open in the browser as an HTML page. If content lives in a Word or Excel doc, convert it to an HTML page and link that. (PDFs that render inline are acceptable, but prefer HTML.)
- **GOAL, AUDIENCE, PROCESS on everything, forever.** Every project, tool, agent, PRD, and portfolio card states three things, clearly labeled: **Goal** (specific, not vague), **Audience** (exactly who it serves), and **Process / How it works**. Never ship a card or PRD missing any of the three. This is the same structure Michelle requires of her students; keep it consistent across the whole portfolio.
- **Be honest about status, never overclaim.** Label prototypes as prototypes and tools in testing as in testing. Render is a prototype heading toward a Fall 2026 pilot; CopaMigo is an early prototype in testing; nothing is in production yet. Do not imply production or use numbers that cannot be verified.

## Consistency check before calling anything done
Spot-check the new page against an existing clean page: same nav, same title size and position, same body color and size, same padding, same eyebrow placement, same header and footer. If anything differs, fix it. Inconsistency (some pages with pill nav, some with eyebrows above vs below, different body colors, different margins) is the number one recurring problem. Clone an existing clean page instead of starting fresh. Then run `python3 tools/design-lint.py` and paste the result.

## Preserved exceptions and rules (keep these)
- **Presentations exception.** Slide decks are self-contained and keep their own chrome, like tools. Tools and presentations are the only two exceptions to this style guide.
- **Canvas-view exception.** The styled "Canvas view" of a course uses Montserrat (headings) and Open Sans (body) with the Mines-blue palette, because it must look like Canvas. That is the ONLY place those fonts or that palette appear. Everything else on the site uses Lora + DM Sans and the palette above.
- **Metrics section.** On an overview, include a **Metrics** section ONLY if the project has real metrics; otherwise leave the heading off entirely. Overview section order: Goal, Audience, Process, Technology (always a bulleted list, comprehensive), Metrics (only if any), Status (last).
- **First person.** Use first person ("I", "my") only inside a real quote or on the About page. Everywhere else, write about the work, not "I".
- **Bundled template.** For a new overview/case-study page, clone `page-builder/references/overview-template.html` rather than starting from scratch (note: bring that template to this current system before relying on it). The canonical live page to clone is `wayfinder/overview.html`.
- **Style guide page.** The rendered visual reference lives at `style-guide/index.html`; open it in a browser.
