# The quality system, plan of record

**Goal:** make correctness automatic instead of remembered, so Michelle never again spends half a day cleaning up file placement, wrong headings, or pages that were built without accessibility.

**Audience:** Michelle, and every future Claude session. A session that reads this file should be able to finish the build without re-deriving any of the reasoning.

**Process:** convert rules from prose into gates. Build the gate, then start every new page from a compliant template, then make "done" mean "the gate passed."

> **Opened 29 August 2026**, after a session in which nearly every rule broken was a rule that existed in writing, and every rule kept was one enforced by a program.

---

## The diagnosis, do not skip this

On 29 Aug 2026 a single long session produced: twelve pages missing a `<main>`, an `<h1>`, or a working skip link; 257 links opening new tabs without `rel="noopener"`; a broken `<h1>...</h2>` shipped inside every exported student dashboard; a reference document written into `TASKS.md`, which is a state file; and a new markdown created where an existing one should have been appended to.

**Every one of those rules was already written down.** They are in `CLAUDE.md` and in the `website-style-guide` skill. They were read at the start of the session and then drifted from over the following six hours.

Meanwhile `tools/design-lint.py` was never once violated, across dozens of edits, because it runs and it fails.

**The conclusion, and the whole basis of this system: a rule that is not checked is not a rule, it is a wish.** Prose degrades across a long session. A check re-reads its rules on every run. So the fix is never "write the instruction more firmly." The fix is always "add a gate."

---

## Part 1, BUILT 29 Aug 2026

### `tools/preflight.py`, the one gate

One command running four checks. Exit 0 means safe to commit, exit 1 means something CRITICAL.

```
python3 tools/preflight.py          portfolio surface
python3 tools/preflight.py --all    every page
```

| Check | What it catches |
| --- | --- |
| `design-lint.py` | the locked design system: widths, nav, palette, curly quotes, em dashes, gradients |
| `a11y-lint.py` | WCAG 2.1 AA: structure, alt text, form labels, heading order, duplicate ids, `rel="noopener"`, iframe titles, focus states |
| link check | every internal `href` and `src` resolves, scripts excluded so template literals are not false positives |
| tidy check | the `CLAUDE.md` file-placement rules, as checks: no markdown at the repo root, one project markdown per project directory, no `.bak` or `_tmp` files |

### `tools/a11y-lint.py`, new

Written 29 Aug. Same shape and scope rules as the design linter. Three classes of false positive were found and fixed during its first run, and the fixes are commented in the file so nobody reintroduces them:

1. Form controls using the **wrapping-label** pattern (`<label>Course level <select>`) are correctly labelled. Checking only for `for=` produced 500+ false failures.
2. A `<div onclick>` carrying `role`, `tabindex` and a key handler is a **correctly built ARIA widget**, not a violation. A modal backdrop that dismisses on `event.target===this` is not a control at all.
3. An `<img alt="...">` inside a link **supplies that link's accessible name**.

**Rule for anyone editing these linters:** when the checker reports something that is fine, fix the checker's scope. Never ignore the finding and move on. That rule is already in the `website-style-guide` skill and it is what kept the design linter trustworthy.

### `tools/design-lint.py`, one fix

It counted an `<h1>` inside a `<script>` template string as a duplicate heading. Those headings belong to a **different document** that the script generates, not to the page being linted. Now strips scripts before counting. The comment in the file explains why, so it does not get reverted.

### The git pre-commit hook

- **Installed at** `.git/hooks/pre-commit`
- **Tracked master copy at** `tools/hooks/pre-commit`, because git does not version `.git/hooks/`. **If the repo is ever re-cloned, that copy must be put back and made executable, or the gate silently disappears.**
- **Blocks only on CRITICAL.** Warnings never block.
- **Verified 29 Aug** against a deliberately broken page: it caught a missing `<h1>` and a dead internal link and refused the commit.

**The escape hatch, and why it exists.** GitHub Desktop has no "skip hooks" option, and the normal bypass is a Terminal flag Michelle does not use. So the hook checks for a file: create an empty `tools/.skip-preflight` in Finder and the gate warns instead of blocking. Delete it to re-arm. **Never remove this escape hatch.** Without it a failing hook could lock her out of committing her own work.

---

## Part 2, STILL TO BUILD

### 2.1 Page templates, the highest-value remaining piece

**Why this matters most:** the twelve broken pages were each hand-written by a different session. A template makes a broken page impossible to create, which removes the need to audit for it later. Prevention over audit.

Build `tools/templates/`:

- **`page.html`**, a content page. Ships already carrying: `lang="en"`, a unique `<title>`, a meta description, Open Graph tags including a 1200x630 PNG `og:image` at an absolute URL, `twitter:card`, the skip link, the locked `site-head` header, `<main id="main">`, exactly one `<h1>`, the category eyebrow under the h1, and the locked footer.
- **`tool.html`**, a running tool. Same universal requirements, but no heading system, no eyebrow, no Goal/Audience/Process, per the two-page-types rule in the style guide. Carries the standardized return link instead.

Then add a tidy-check rule: a new HTML file that does not match a template's required skeleton fails preflight.

### 2.2 The contract block in `CLAUDE.md`

Five lines at the top, so file placement is never a judgement call again:

| File | Holds | Never holds |
| --- | --- | --- |
| `CLAUDE.md` | who she is, guardrails, voice, the router | procedures, specs, backlogs |
| `TASKS.md` | what is open, due, next | reference material, run logs, tables of file paths |
| a skill | the procedure for doing a thing | data that changes often |
| `<project>/PROJECT.md` | that project's working notes, one file | anything belonging to another project |
| `tools/` | the checkers, and the reference docs they generate | project planning |

### 2.3 Update two skills so the procedure ends in the gate

- **`page-builder`**: step one becomes "copy the template," and the final step becomes "run `python3 tools/preflight.py` and paste the output." Remove any language that lets a page be declared done on an assistant's judgement.
- **`website-style-guide`**: replace the design-lint instruction with preflight, since preflight runs it plus three more checks.

**The wording that matters, and it should be blunt:** *never tell Michelle a page is done without pasting preflight output. Not "I checked." Not "it looks right." The actual output.*

### 2.4 Two open decisions, both already evidenced

- **Header nav, two links or three.** 95 portfolio pages use the two-link version, the name acting as Home. The linter's rule says three, but it never fires on those pages because it matches the literal string `<nav class="site-nav">` and the pages write `<nav class="site-nav" aria-label="Primary">`. **The live pages are the truth; fix the linter to match reality and to match the tag with attributes.**
- **The accessibility backlog** in `tools/ACCESSIBILITY.md`: 17 heading-level jumps and 49 missing meta descriptions. Left deliberately, because changing a heading level changes how a page looks and that is a designer's call.

---

## How to pick this up in a new session

1. Read this file and `tools/ACCESSIBILITY.md`.
2. Run `python3 tools/preflight.py --all` to see the current state.
3. Build Part 2 in order: templates, contract block, skill updates.
4. Confirm `.git/hooks/pre-commit` still exists and is executable. If not, copy it from `tools/hooks/pre-commit`.
5. Never run git. Save files and stop; Michelle reviews in GitHub Desktop and pushes.
