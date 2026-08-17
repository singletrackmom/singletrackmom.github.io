# Dial Your Course: the export and re-import roundtrip

**Goal:** prove the whole loop. Download a Canvas course, run it through the dialer, apply changes, re-upload to Canvas, and see the style guide, the seat time, and the course objectives actually land. Nobody has done this end to end yet, including me.

**Audience:** me, next session. This is the pick-up-here file for the roundtrip work and the walkthrough video that depends on it.

**Process:** resolve the version problem first, then answer the three open questions below, then record.

**Captured:** August 16, 2026, from a working conversation. Nothing here is built yet.

---

## Read these first, they already exist

- `tools/NEXT.md` , the standing pick-up-here file for Dial Your Course.
- **`canvas/reference/CANVAS_OUTCOMES_EXPORT_BUG.md`** , this is the important one. It already holds researched findings on **why Canvas outcomes do not reach an `.imscc` export**, with the cause identified and two tests queued. The objectives problem described below is very likely the same bug. Do not re-research it from scratch.
- `canvas/reference/GCC_ILOs.md` , all 47 institutional learning outcomes with exact Canvas names.

---

## Problem 1: the wrong version is live

The site is showing an **older version** of the tool. The newer build got too complicated and was set aside.

To decide next session:
- Which version is actually on `michelleblomberg.com/course-dialer` right now.
- Is the newer build salvageable by cutting scope, or is the older one the better base to move forward from.
- Whatever wins, the other should be archived clearly, not left where a reviewer can stumble into it.

**Do not record the walkthrough video until this is settled.** A hiring reviewer clicking into an outdated tool is worse than no video.

---

## Problem 2: seat time does not survive the export

The seat-time-o-meter works inside the tool. What is unknown is whether any of it comes back out.

Open questions:
- When a course is exported as `.imscc` after edits, **where does the seat time live**? Is it written into the package at all?
- Should each assignment carry its own **timestamp / time estimate** visible in Canvas, rather than the total living only in the tool?
- What is the right Canvas surface for it: assignment description, a page, a module item, or a rubric field?

**Michelle's stated want:** actual time stamps on each project in the course, not just an aggregate readout inside the dialer.

---

## Problem 3: course objectives are not coming down

**The likely cause, and it is a good product finding.** The objectives live in the **Syllabus tool inside Canvas**, not in the course content. So when a course is exported, the objectives are not in the package, which is why the dialer cannot see them to check alignment.

Two candidate fixes, both worth testing:
1. **Require the syllabus as an attached PDF** rather than only living in Syllabus+. If the syllabus is a real file in the course, it exports with the package and the dialer can read it.
2. **Add a syllabus upload slot to the dialer** so a user can attach the syllabus separately when the export does not carry it.

Option 2 is the better product answer, because it does not depend on every faculty member changing their habits. Option 1 is the better institutional answer. They are not exclusive.

Cross-check this against `CANVAS_OUTCOMES_EXPORT_BUG.md` before building anything, since the outcomes and objectives problems may share a root cause.

---

## The video this unlocks

This is the walkthrough that has never been recorded because the loop has never been run.

Shot list, once the above is resolved:
1. Export a real course from Canvas as `.imscc`.
2. Drop it into Dial Your Course.
3. Show the findings, each traced to its standard and location.
4. **Show it refusing to report something it cannot compute.** Say why the constraint exists.
5. Apply the fixes, including the style guide.
6. Export the corrected package.
7. **Re-import into Canvas.**
8. Show the style guide applied, the seat time visible, and the objectives present.

Step 7 and 8 are the payoff and the part nobody has proven yet. If it does not work, that is the finding, and the honest version of the video says so.

---

## Order of operations

1. Settle which version is live and archive the other.
2. Run one manual roundtrip by hand, no video, just to see what survives. Take notes on what breaks.
3. Fix the objectives path (syllabus upload slot is the fastest).
4. Decide where per-assignment time stamps get written.
5. Then record.

Do not skip step 2. The video needs to be a demonstration, not a discovery.
