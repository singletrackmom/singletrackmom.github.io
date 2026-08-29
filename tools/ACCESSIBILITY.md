# Website accessibility, the standing backlog

**Goal:** get michelleblomberg.com to WCAG 2.1 AA with nothing left that a hiring manager, a screen-reader user, or an accessibility reviewer could catch. This is Michelle&rsquo;s industry, so the site has to be exemplary rather than merely passing.

**Audience:** Michelle, working through this with time and a fine-toothed comb. Not a today job.

**Process:** run both linters, work one section below, run them again. Nothing here is guessed at; every item was found by a tool and verified by hand.

> **This file is the reference. `TASKS.md` only points at it.** Append findings here as they are found. **One accessibility document. Never create a second.**

**Where this stands.** Both linters pass with **zero CRITICAL** and all 5,346 internal links resolve. The site is shippable today. Everything below is a MAJOR or MINOR polish item that needs a design judgement, so it was deliberately left rather than guessed at.

**How to check your work at any point:**

```
python3 tools/design-lint.py --all
python3 tools/a11y-lint.py --all
```

`tools/a11y-lint.py` is new as of 29 Aug. It catches what the design linter does not: alt text, link text, form labels, heading order, duplicate ids, new-tab safety, iframe titles, focus states, and meta descriptions. It exits non-zero if anything CRITICAL appears, so it can gate a build.

---

## 1. Heading-level jumps, 17 pages (MAJOR)

A screen-reader user navigates by heading level. A jump from h1 straight to h3 tells them a section was skipped.

**This needs your eye, not a script.** In the design system h2 is Lora sage title case and h3 is DM Sans grey uppercase, so demoting or promoting a heading changes how the page looks. **The usual correct fix is adding the missing h2, not changing an existing h3.** `airc-sss/method.html` is the typical case: four `<h3 class="sec">` headings sit under the h1 with no h2 above them.

| Page | Jump |
| --- | --- |
| `airc-sss/method.html` | h1 to h3 |
| `airc-sss/scope.html` | h1 to h3 |
| `copamigo/student-resources-plain.html` | h1 to h3 |
| `copamigo/student-resources.html` | h1 to h3 |
| `course-dialer/index.html` | h1 to h5 |
| `course-dialer/report-sample.html` | h1 to h4 |
| `course-dialer/v2.html` | h1 to h5 |
| `cultivate/claude-lovable-workflow.html` | h2 to h4 |
| `cultivate/cv.html` | h1 to h4 |
| `cultivate/mesa_conference/mesa-conference.html` | h1 to h3 |
| `cultivate/pd-plan.html` | h1 to h3 |
| `cultivate/scrum.html` | h1 to h3 |
| `render/agents-lab.html` | h1 to h3 |
| `render/index.html` | h2 to h4 |
| `style-guide/index.html` | h2 to h4 |
| `wayfinder/frisco-packing.html` | h1 to h3 |
| `wayfinder/index.html` | h2 to h4 |

## 2. Missing meta descriptions, 49 pages (MINOR)

The description is what Google and LinkedIn show under the link. Done already: `index.html`, `about.html`, and the five project overview pages, which are the ones a hiring manager actually lands on. The rest are deeper subpages.

One or two sentences each, written from what the page actually says. Not urgent, but they are the difference between a search result that reads as considered and one that reads as unfinished.

- `airc-sss/sss-goals-and-groups.html` &middot; `copamigo/advisor-form/index.html` &middot; `copamigo/detail.html`
- `copamigo/index.html` &middot; `copamigo/knowledge-builder.html` &middot; `copamigo/prd.html`
- `copamigo/question-intake.html` &middot; `copamigo/questionnaire.html` &middot; `copamigo/student-resources-plain.html`
- `copamigo/student-resources.html` &middot; `course-dialer/ilo-test.html` &middot; `course-dialer/index.html`
- `course-dialer/prd.html` &middot; `course-dialer/report-sample.html` &middot; `course-dialer/styleguide.html`
- `course-dialer/todo-sample.html` &middot; `course-dialer/v2.html` &middot; `course-dialer/workload.html`
- `cultivate/ai-fellows/index.html` &middot; `cultivate/claude-lovable-workflow.html` &middot; `cultivate/completed.html`
- `cultivate/cv.html` &middot; `cultivate/detail.html` &middot; `cultivate/discord-community.html`
- `cultivate/google-genai/index.html` &middot; `cultivate/index.html` &middot; `cultivate/learning-agents-whitepaper.html`
- `cultivate/mesa_conference/mesa-conference.html` &middot; `cultivate/pd-plan.html` &middot; `cultivate/prd.html`
- `cultivate/scrum.html` &middot; `cultivate/ux_toolkit.html` &middot; `cultivate/whitepaper.html`
- `render/agents-lab.html` &middot; `render/career-counselor.html` &middot; `render/hiring-panel.html`
- `render/index.html` &middot; `render/interview-panel.html` &middot; `render/job-search-agent.html`
- `render/mesa-ai-summit-2026.html` &middot; `render/prd.html` &middot; `render/sample-dashboard.html`
- `render/training-plan-agent.html` &middot; `render/walkthrough.html` &middot; `style-guide/index.html`
- `wayfinder/builder.html` &middot; `wayfinder/frisco-packing.html` &middot; `wayfinder/index.html`
- `wayfinder/prd.html`

## 3. Open Graph images (MAJOR for a job search)

**Only 8 pages in the whole repo carry Open Graph tags, and the home page was not one of them until 29 Aug.** Text tags (`og:title`, `og:description`, `og:url`, `twitter:card`) are now on `index.html` and `about.html`. **What is still missing is `og:image` everywhere on the portfolio.**

That is a design task, not a code task, so it was left for you:

- Design a **1200x630 PNG**, never an SVG, because LinkedIn will not render an SVG preview.

- Reference it at an **absolute URL** (`https://michelleblomberg.com/assets/og-home.png`).

- The pattern already exists in the repo: `airc-sss/og-cover.png` and `airc-sss/og-journey.png` are both correctly sized.

- Priority order: `index.html`, `about.html`, then the five project overview pages.


## 4. Already done 29 Aug, for the record

- Broken `<h1>...</h2>` in the Render export template, which shipped inside every student dashboard. Fixed in four files.

- Three Render pages had no document heading at all; their only `<h1>` was inside a script template. Visually-hidden `<h1>` added.

- 257 links opened new tabs without `rel="noopener"`, across 52 files.

- Twelve pages had no `<main>`, no `<h1>`, or a skip link pointing at a target that did not exist, including `work.html`, which 21 pages link to.

- Eight form controls had no accessible label. `aria-label` added.

- `tools/design-lint.py` was counting an `<h1>` inside a script template as a duplicate heading. Fixed.
