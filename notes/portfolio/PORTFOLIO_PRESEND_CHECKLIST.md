# Portfolio, dial it in before EAB clicks through

Written 17 Aug 2026. **STATUS: design-lint is CLEAN, 0 violations across 316 pages.**
Everything in Tier 1 and Tier 2 below was fixed on 17 Aug. Kept as a record of what
was wrong and how it was found.

---

## ✅ What was fixed, 17 Aug

Started at 224 violations (188 on the portfolio surface). Now 0.

| Fixed | Count |
|---|---|
| `--ink` overridden to a non-locked value | 32 pages |
| Contrast: sage, gold, rose used as body text | 36 pages |
| Missing skip-to-content link | 25 pages |
| Site-nav missing Home | 46 pages |
| `main` max-width not 1000px (sideways content shift) | 15 pages |
| Old `.tabs` padding indenting tabs 14px | 10 pages |
| Missing site footer | 10 pages |
| Missing site header | 11 pages |
| Not loading `/assets/site.css` | 11 pages |
| `<main>` without `id="main"` | 11 pages |
| Multiple `<h1>` (Render app had 17) | 5 pages |
| Clickable divs not keyboard reachable | 7 pages |
| `outline:none` with no focus-visible | 7 pages |
| Straight apostrophes in prose | 15 pages |
| Unbalanced `<div>` tags | 3 pages |
| Missing lang, title, img alt, iframe title | 8 pages |
| CSS gradient (banned) | 1 page |

## ✅ Three false-positive classes fixed in the checker itself

A checker that cries wolf gets ignored, which is how this backlog grew. These are
now correctly exempt rather than permanently flagged:

1. **Self-contained pages** (`copamigo/widget.html`, `render/render-maya.html`,
   `render/render-riley.html`). The widget is iframed into another site and the two
   dashboards are the exported files a student keeps and opens offline. Injecting
   site chrome or `/assets/site.css` breaks them. I broke all three mid-pass and
   restored them.
2. **Canvas page fragments** (`avc100/pages/*`). HTML bodies pasted into an LMS,
   with no `<html>`, `<head>`, or `<body>` by design, so document-level rules
   cannot apply.
3. **Correct ARIA controls.** A `<div onclick>` that carries `role` and `tabindex`
   is properly authored markup, not a violation.

## ✅ Four new structural checks added

`design-lint.py` now also catches, and each was verified with a planted fault:

- unbalanced `<div>`, `<main>`, `<section>`, `<table>`
- unrendered `${...}` sitting in static HTML (renders as raw code on screen)
- unfilled placeholders in visible text (`PASTE_`, `_URL_HERE`, `Lorem ipsum`)
- broken internal links, across all 316 pages

---

## Still to do, needs Michelle

- [ ] **Open the three tools in a browser and click every tab.** Claude cannot do
      this. Render, CopaMigo, Dial Your Course. Hard-refresh first.
- [ ] **Delete `render/agents-lab.html`.** Orphan, asks visitors for an API key.
- [ ] **Swap the Knowledge Builder seeded data** for the real crosswalk. It is
      still Claude&rsquo;s reconstruction, the one remaining place the site says
      something Michelle did not author.
- [ ] Consolidate the four overlapping CopaMigo staff pages.

---

## How this happened

Worth knowing, so it does not happen again:

1. **Pages were cloned from whatever page was nearby**, not from one canonical
   template. Each project folder inherited a different ancestor, which is why
   `--ink` had four different values and `main` was 1080px in cultivate, 860px in
   render, and 780px in the whitepapers.
2. **The design system and the checker were written after most pages existed.**
   They codified the rules but nobody back-applied them.
3. **The backlog was mischaracterised.** `TASKS.md` said &ldquo;224, almost all Canvas
   course exports, nothing on the critical path.&rdquo; 188 were on the portfolio
   surface. That note gave permission to ignore it for weeks.

**The rule going forward:** `python3 tools/design-lint.py` must exit 0 before any
page is called done. It now checks structure and links, not just style, so one
command covers it.

---

## Original checklist, kept for reference

## Tier 1, before anyone from EAB clicks

### 1. Confirm the three tools actually work

Cannot be skipped and cannot be done by Claude. Open each in a browser, hard-refresh
(`Cmd+Shift+R`), click every tab.

- [ ] **Render** &middot; confirm the Launch Plan panel no longer prints raw JavaScript
      on screen. That was fixed 17 Aug but has never been viewed in a browser.
      Click all ten tabs.
- [ ] **CopaMigo** &middot; ask three real student questions, confirm the handoff card
      renders with contact, hours, and map.
- [ ] **Dial Your Course** &middot; run one real `.imscc` end to end.

### 2. Content jumps sideways between pages (most visible problem)

**15 pages** set `main` to 1080px or 780px while the header and footer are locked at
1000px, and **10 of those** produce a measurable horizontal shift. A reviewer clicking
through watches the content slide left and right. Same class of problem as the
eyebrow drift, one level up.

Mostly `cultivate/`: `ai-fellows`, `completed`, `detail`, `google-genai`, `index`,
`learning-agents-whitepaper`, `mesa_conference`, `pd-plan`, `scrum`, `ux_toolkit`,
`whitepaper`. Plus `airc-sss/sss-goals-and-groups`.

### 3. Tab bars indent 14px right of the title

**10 pages** still carry the old `.tabs` padding of 0.55/0.85. Same `cultivate/`
cluster plus `discord-community`.

### 4. Colour contrast failures, including on the home page

- **13 pages** use `--sage` as text (needs `--sage-text` `#456546`)
- **12 pages** use `--gold` as text (needs `--gold-text` `#75592c`)
- **11 pages** use `--rose` as text (needs `--rose-text` `#94395a`)

`index.html` is in all three lists. The front door fails WCAG AA on a job where
accessibility is table stakes.

---

## Tier 2, cleanup

- [ ] **`--ink` overridden on 32 pages** to values like `#3a2e3f`, `#212121`,
      `#2e2426`. Body text colour varies subtly across the whole site. Locked value
      is `#26221f`.
- [ ] **18 pages missing a skip-to-content link**
- [ ] **12 pages** have site-nav of `['Work','About']` instead of the locked
      `Home, Work, About`
- [ ] **11 pages** have `<main>` without `id="main"`
- [ ] **7 pages missing the site footer**
- [ ] **5 pages with clickable `<div>`** instead of a real button or link:
      `cultivate/index`, `cultivate/pd-plan`, `render/index`, `render-maya`, `render-riley`
- [ ] **5 pages do not load `/assets/site.css`** at all, so shared header and footer
      styles never apply: `copamigo/widget`, `cultivate/cv`, `render-maya`, `render-riley`
- [ ] **4 pages with `outline:none`** and no `:focus-visible` replacement, which
      breaks keyboard navigation
- [ ] **3 pages with multiple `<h1>`** elements: `render/index` has 17,
      `render-maya` and `render-riley` have 10 each
- [ ] **2 images without alt**, **2 iframes without title** in `course-dialer`

## Tier 3, content decisions

- [ ] **Delete `render/agents-lab.html`.** Orphan, nothing links to it, and it asks
      visitors to paste their own Gemini API key. Its content is documented on the
      Skills tab. Claude cannot delete files; do it in Finder or GitHub Desktop.
- [ ] **Four overlapping CopaMigo staff pages**: `knowledge-builder`,
      `question-intake`, `advisor-form`, `questionnaire`. Only the first two are
      coherent with each other now. Consolidate to one.
- [ ] **Knowledge Builder seeded data is still Claude&rsquo;s reconstruction**, not the
      real crosswalk. If an EAB reviewer opens that tab they see plausible-looking
      department content that Michelle did not author. This is the one remaining
      place the site says something not hers.
- [ ] **`render/mesa-ai-summit-2026.html`** kept its own h1 rather than the product
      name, because it is a slide deck rather than a project page. Decide whether it
      should join the Render tab system.

---

## Then, and only then

1. **Three walkthrough videos.** 60 to 90 seconds each, narrated, no intro slate.
   CopaMigo first, then Render, then Dial Your Course. Scripts live in
   `~/Documents/Claude/JobSearch/EAB_PXD_SrAnalyst_Application/WALKTHROUGH_VIDEO_TODO.md`.
   The one rule: do not narrate features. Narrate one decision made and the
   alternative rejected, and show one non-happy-path state.
2. **The Figma file.** Full spec at `notes/portfolio/FIGMA_TRAVELER_SPEC.md`.
3. **Push everything.**

---

## Standing rule

Run `python3 tools/design-lint.py` after every change and before calling anything
done. Fix what it names, then run it again. Never fix-and-assume.
