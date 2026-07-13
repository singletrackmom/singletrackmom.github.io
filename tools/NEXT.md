# NEXT: Dial Your Course, pick up here

**Goal:** Prove Dial Your Course end to end on the AVC 100 sandbox: export, check, set seat time, reimport, verify.
**Audience:** Me, next session. Read this before touching the tool.
**Process:** Two cheap tests first, in order. Do NOT start clicking outcomes onto rubrics until Test 1 fails.

**Status as of 13 July 2026.** Parked. The Mines application (closes July 15) outranks this. Nothing on the portfolio overclaims, so the site is safe to be seen in the meantime: it says prototype, in testing, reports only what it can prove.

---

## The blocker

AVC 100 sandbox has **5 outcome groups and 14 verbed outcomes visible in Canvas**, imported via an Outcomes CSV. The `.imscc` export contains **zero** of them. The outcomes file is **absent, not empty**. Reproduced on two separate exports.

Until outcomes reach the export, the outcome-alignment half of the checker cannot run on this course. Seat time and objectives can, because assignments do export.

## ⚠️ The trap (read this before you do anything)

**My working hypothesis was "attach every outcome to a rubric criterion so they get captured in the export." The source read says that is WRONG for a full export.**

`lib/cc/learning_outcomes.rb` walks the entire course outcome tree and writes every group and link, **independent of alignment**. Alignment only controls an optional `<alignments>` child node.

The "outcomes only export if bound to a rubric" belief IS true, but only for **selective** exports (course copy with "select specific content," blueprint/master migrations, API `select[]`). That is almost certainly where the folklore comes from. It does not apply to **Settings → Export Course Content → Course**.

So: do not spend hours binding 14 outcomes to rubric criteria on a theory this document already refutes. Do Test 1 first. It takes 30 seconds.

## Test 1 · bust the cache (DO THIS FIRST, it is free)

Canvas caches a boolean `has_outcomes?`, keyed on the course's `id` + `updated_at`. The CSV importer creates the outcomes and their links but **never touches the Course row**, so a stale `false` cached from before the import can persist. When it does, `create_learning_outcomes` returns nil and **no file is written at all**. That is exactly our symptom: absent, not empty.

1. Open the AVC 100 sandbox → **Settings**
2. Change anything trivial, even just re-save → **Save**  (this bumps `updated_at` and busts the cache)
3. **Settings → Export Course Content → Course**
4. Unzip and look for `course_settings/learning_outcomes.xml`

- **File now appears with the 14 outcomes** → the cache was the cause. Real Canvas defect. Tell CTLE. Proceed to the run-through below.
- **Still absent** → go to Test 2.

## Test 2 · bind one outcome (only if Test 1 fails)

Color Palette Exercise → **Rubric** → pencil → **Find Outcome** → group `2 · Create digital art` → *Build and defend a colour palette* → **Import** → Save. Export again.

- **File appears only after binding** → the source reading is wrong and the folklore is right. Rebuild the flagship check around the paste box as the primary path.

**Also confirm** the package contains `course_settings/canvas_export.txt`, i.e. it is a real Canvas course package and not a Quizzes export.

## Then the actual run-through (the thing I want to prove)

1. Export AVC 100 from the sandbox.
2. Run it through Dial Your Course.
3. Review the findings. Decide which changes to accept.
4. **Set the time estimate on each project.** This was the original reason the tool exists (see below), so this is the part that matters most.
5. Export the corrected package.
6. **Reimport into the sandbox** and verify every change actually landed.
7. Work the "only Canvas can do this" list by hand (institutional outcomes on rubric criteria; see the known defect below).

## Why this tool exists, in order (the build story, for the walkthrough)

1. **Seat time.** The Higher Learning Commission flagged it in online courses here. A credit promises a fixed number of student hours and online there is no classroom to observe, so the course package is the only evidence those hours were delivered. Calculating it by hand was miserable. That was the first thing I wanted.
2. **A style guide that survives.** I wanted accessible, consistent styling that did not get stripped every time HTML was pasted into a Canvas module.
3. **Objectives and Bloom's.** Then: are the objectives even listed, and are they written in verbs a student can be observed performing, at the level the course claims?
4. **OSCQR.** Then: what else can I fold in for free? OSCQR is Creative Commons, so it went in alongside my own alignment and workload criteria.

Save this sequence for the walkthrough, not the overview. The overview stays tight: Goal, Audience, Process.

## Known Canvas defect that will bite on reimport

**Account-level outcomes (the GCC ILOs) serialize as references, not copies.** `lib/cc/rubrics.rb` writes `learning_outcome_external_identifier lo.id` when the outcome's context is not the course. On import the numeric id cannot resolve, the criterion arrives with no outcome attached, and it quietly degrades to a plain criterion. **No tool can fix this from a package.** It is two minutes each, by hand, in Canvas. That is what the post-export to-do list is for.

Full detail: `canvas/reference/CANVAS_OUTCOMES_EXPORT_BUG.md`. The 47 GCC ILOs with their exact Canvas names: `canvas/reference/GCC_ILOs.md`.

## Parked, decided against

- **Automated student outreach / engagement monitoring.** Needs continuous student engagement data, which breaks the no-PII line every project of mine rests on. Canvas New Analytics already does it manually: filter by "haven't submitted" or "haven't viewed recently," message that group. Use that. Do not build a bot that holds student data.
- **Canvas Analytics inside the checker.** The checker reads a course export, which contains no student data by design. Analytics is student behavior data. Keep them separate; the separation is the feature.
