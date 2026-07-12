# Canvas outcomes do not reach the course export

**Goal:** Establish why a Canvas course with visible learning outcomes exports an `.imscc` containing none, and determine whether the alignment matrix can be built from a course package at all.

**Audience:** Me, tomorrow. CTLE, when I email them. Anyone who later tries to build a course-quality tool on a Canvas export.

**Process:** Reproduce the symptom, read the Canvas source, discriminate between the competing explanations with two cheap tests.

**Status as of 11 July 2026, late.** Source read. Cause identified with high confidence but not yet proven on our instance. Two tests queued.

---

## The symptom

AVC100 sandbox, GC Blomberg. Outcomes are visibly present in Canvas: **5 outcome groups** (`1 · Operate a computer` … `5 · Prepare images for print and presentation`), created by importing an Outcomes CSV at the course level, with **14 verbed outcomes** inside them.

None of the outcomes are aligned to a rubric criterion.

Export via **Settings → Export Course Content → Course**. The resulting `.imscc` contains:

- **No `course_settings/learning_outcomes.xml` at all.** Not empty. Absent.
- **Zero `learning_outcome_id`** elements on any rubric criterion.

Reproduced on **two separate exports** taken at different times.

---

## What we assumed, and why it is wrong

> *"Canvas only exports outcomes that are bound to a rubric criterion."*

**Refuted, for a full course export.**

`lib/cc/learning_outcomes.rb` walks the **entire course outcome tree** and writes every group and every outcome link, independent of alignment. Alignment only controls an optional `<alignments>` child node inside each `<learningOutcome>`.

```ruby
def create_learning_outcomes(document = nil)
  return nil unless @course.has_outcomes?
  root_group = @course.root_outcome_group(force: false)
  return nil unless root_group
  ...
  process_outcome_group_content(outs_node, root_group)
```

`process_outcome_group_content` recurses `child_outcome_groups.active` and `child_outcome_links.active`, gated only by `export_object?`.

And in `app/models/content_export.rb`:

```ruby
def export_object?(obj, asset_type: nil, ignore_updated_at: false)
  return false unless obj
  return true unless selective_export?
```

A **Settings → Export Course Content → Course** export has empty `selected_content`, so `selective_export?` is `false` and `export_object?` returns **true for everything**. An unaligned, CSV-imported course outcome *should* serialize.

**Where the bind-first belief is actually true:** *selective* exports. Course copy with "Select specific content," blueprint and master migrations, API `select[]`. There, `export_object?` is false for outcomes not explicitly ticked, and the only outcomes that survive are the ones `lib/cc/rubrics.rb` pulls in:

```ruby
rubric.learning_outcome_alignments.each do |align|
  add_item_to_export(align.learning_outcome, "learning_outcomes")
end
```

So in a selective export, *aligned to a rubric* is effectively the survival condition. **That is almost certainly the origin of the folklore, and it does not apply to a full export.**

---

## The likely actual cause: a stale cache

Only two gates can suppress `learning_outcomes.xml` **entirely**:

1. `@course.has_outcomes?` is false
2. no root outcome group

`has_outcomes?` in `lib/learning_outcome_context.rb` is a **cached boolean**:

```ruby
def has_outcomes?
  Rails.cache.fetch(["has_outcomes", self].cache_key) do
    linked_learning_outcomes.exists?
  end
end
```

The cache key is the course's `id` + `updated_at`.

**The CSV import (`lib/outcomes/import.rb`) creates the `LearningOutcome` and its `ContentTag` links but never touches the Course row.** So a `false` cached *before* the import can persist, `create_learning_outcomes` returns `nil`, and **no file is written at all**.

That is exactly our symptom: **absent, not empty.**

> **This is inference from reading master, not a proven fact about our instance, and not an acknowledged Instructure defect.** It is the only code path I can find that produces "file absent rather than empty." Do not state it as fact to CTLE. State the symptom, state that the source says a full export should carry unaligned outcomes, ask them to check.

---

## The two tests, first thing

They discriminate cleanly. Do both, in this order.

**Test 1 · bust the cache.**
Open the AVC100 sandbox → **Settings** → change anything trivial (even just re-save) → **Save**. That bumps `updated_at` and invalidates the `has_outcomes?` cache. Then **Settings → Export Course Content → Course**.

- If `learning_outcomes.xml` **now appears** with the 14 outcomes → **the cache was the cause.** Real Canvas defect. Worth reporting to CTLE and to Instructure.

**Test 2 · bind one outcome.**
Color Palette Exercise → **Rubric** → pencil → **Find Outcome** → group `2 · Create digital art` → *Build and defend a colour palette* → **Import** → Save. Export again.

- If the file appears **only after binding** → the source reading is wrong and the folklore is right. Rebuild the flagship check around the paste box as the primary path.

**Also confirm** the package contains `course_settings/canvas_export.txt`, i.e. that it is a real Canvas course package and not a Quizzes export.

---

## A separate, confirmed defect that matters for ILOs

**Account-level outcomes serialize as references, not copies.**

`lib/cc/rubrics.rb` writes `learning_outcome_external_identifier lo.id` when `lo.context != @course`. On import into a **different Canvas instance**, the numeric id cannot resolve. `LearningOutcomeImporter` emits:

> *The external Learning Outcome couldn't be found for "%{title}", creating a copy.*

and the rubric criterion is written with **no `learning_outcome_id`** — it degrades to a plain criterion.

**Consequence for us:** ILOs are account-level. Within Maricopa they resolve. **Export a course outside the district and every ILO-bound criterion quietly loses its outcome.** That is a real constraint on sharing courses, and it is worth knowing before recommending ILO attachment across the department.

Thread: <https://community.canvaslms.com/t5/Canvas-Question-Forum/How-do-you-get-around-the-quot-external-Learning-Outcome-couldn/td-p/226119>

> **Do not repeat the "outcomes are packed after rubrics, that is the bug" claim.** It appears in that thread as a community member's theory and it does **not** match current source. On import, `course_content_importer.rb` runs `LearningOutcomeImporter` (progress 48→50) **before** `RubricImporter` (50→52), and rubric criteria resolve through `migration.outcome_to_id_map`. Course-context outcome-to-criterion links do survive a Canvas-to-Canvas import. I found no Instructure acknowledgement of an ordering defect.

---

## CSV vs "+ Outcome" vs "Find"

| Method | What it creates | Exports as |
|---|---|---|
| **Course-level CSV import** | Outcome owned by the course (`model.context = context`) plus `learning_outcome_link` ContentTags | Full `<learningOutcome>` element |
| **+ Outcome** | Same shape as CSV | Full `<learningOutcome>` element |
| **Find** (account-level) | A **link** to an account or global outcome | A **reference** (`is_global_outcome` + `external_identifier`) |

**One gotcha in `lib/outcomes/import.rb`:** `find_prior_outcome` matches `LearningOutcome.where(vendor_guid:)` **globally**. If a CSV `vendor_guid` collides with an existing account outcome, the import **links that account outcome** instead of creating a course-owned copy. Worth checking our `vendor_guid` values (`avc100_c1`, `avc100_o01`, …) are not colliding with anything district-wide.

---

## Reliable ways to move outcomes between courses

1. **Re-import the same Outcomes CSV** into the target course. Most deterministic, needs no export at all.
2. **Course Copy with All content** (non-selective, so the full-tree path applies). But it hits the same `has_outcomes?` cache gate.
3. **API:** `GET /api/v1/courses/:id/outcome_groups` and `outcome_group_links`, then `POST /api/v1/courses/:id/outcome_imports` on the target.
4. **Structural:** define outcomes at sub-account level and link them in. One canonical outcome instead of fourteen copies per course. Carries the cross-instance caveat above.

**There is no course-level "Export Outcomes" button.** The Outcomes export report exists only at the account level (Account → Settings → Reports).

---

## What this changes in Dial Your Course

**Nothing structural, if Test 1 confirms.** The parser is correct. The setup check's stage 1 / stage 2 distinction stands.

**Add to PRD §2.3 schema table:** a full course export *should* carry unaligned outcomes; a missing `learning_outcomes.xml` on a course that visibly has outcomes is a Canvas-side defect, not a design constraint of the format.

**If Test 2 contradicts it:** the alignment matrix can never come from an `.imscc` by any tool, the paste box becomes the primary path rather than a fallback, and that is a significant redesign and a genuinely publishable finding.

---

## Sources

- `lib/cc/learning_outcomes.rb` — <https://github.com/instructure/canvas-lms/blob/master/lib/cc/learning_outcomes.rb>
- `app/models/content_export.rb` — <https://github.com/instructure/canvas-lms/blob/master/app/models/content_export.rb>
- `lib/learning_outcome_context.rb` — <https://github.com/instructure/canvas-lms/blob/master/lib/learning_outcome_context.rb>
- External Learning Outcome thread — <https://community.canvaslms.com/t5/Canvas-Question-Forum/How-do-you-get-around-the-quot-external-Learning-Outcome-couldn/td-p/226119>
- Outcomes CSV format — <https://developerdocs.instructure.com/services/canvas/outcomes/file.outcomes_csv>
- Find an existing outcome — <https://community.instructure.com/en/kb/articles/660943>

## Caveats

- Compared against canvas-lms **master**, not a pinned release. Instructure ships continuously; MCCCD's build may differ.
- The `has_outcomes?` cache explanation is **inference**. No bug report exists for "learning_outcomes.xml missing from a full export."
