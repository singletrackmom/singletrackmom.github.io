# Render: Hiring Committee skill (spec)

**Prepared by:** Michelle Blomberg, Digital Media Arts, Glendale Community College
**What this is:** the design for Render's "should I apply?" hiring-committee feature, the step that reads a student's application against one specific job posting through a panel of personas and returns a coaching rubric. This is one of Render's genuinely differentiated pieces.
**Status:** design spec, not yet built into the tool.
**Date:** August 2026

---

## Goal, Audience, Process

**Goal.** After a student builds a resume and pastes a real job posting, show them how an actual hiring committee would read that application, so they learn what to fix and whether it is worth applying, before they hit send.

**Audience.** Render's students (entry-level, community-college), oriented to the goal they typed in, not a generic ideal.

**Process.** The student's active resume and the pasted posting go to a panel of AI personas, each reading with a different lens. The panel returns a banded interview likelihood, a requirement-by-requirement rubric with evidence, and three concrete prioritized fixes, in an encouraging coaching voice. It is one invocation from the student's side; the panel runs inside it.

---

## What makes it different (and the honest limit)

Tools like VMock score a resume against general best-practice benchmarks: one automated grader, one score, mostly "how good is this resume in general." Jobscan and Big Interview score a resume against a posting, but as a single match number.

Render's hiring committee is different on three counts: it is grounded in the one specific posting, it reads through a panel of distinct human personas rather than one grader, and it returns a fix-it rubric in a coaching voice. That combination is not in VMock, Jobscan, or Big Interview.

The honest limit, so nobody oversells it: the raw capability of scoring a resume against a posting is commoditized. The differentiation is in the presentation and the pedagogy, showing a student how three different readers weigh the same resume, which is a teaching moment a score cannot deliver. Position it as a teaching simulation of a real committee, never as "better resume scoring."

---

## The panel

Three core personas, each with a real lens, plus an optional fourth. Each speaks in its own short voice.

1. **The recruiter (first screen).** Checks the knockout requirements and keywords from the posting. Decides "pass this to the hiring manager or not," and says why. This is where a student learns what gets an application discarded in ten seconds.
2. **The hiring manager (can they do the job).** Judges whether the resume shows real evidence of doing the work the posting describes. Points to the bullets that convince and the claims that are thin.
3. **The peer or team member (fit and collaboration).** Reads for how this person would work on the team, communication, dependability, growth signals.
4. **Optional: the ATS or bot screen.** Shows the machine pass students never see, which keywords and formatting help or hurt before a human ever looks.

Every persona reads only the pasted posting and the student's resume. No invented requirements, ever.

---

## The output

1. **Interview likelihood band:** Reach, Possible, or Strong. No fake percentage.
2. **Requirement-by-requirement rubric:** each key requirement from the posting marked met, partly met, or not yet, with one line of evidence from the resume.
3. **The panel's read:** two or three short lines, one per persona, in their own voice.
4. **A clear call:** apply, apply with tweaks, or stretch and learn.
5. **Three concrete, prioritized fixes:** specific edits that would move the needle most.
6. **If it is a reach:** two or three role types that fit the student better right now, framed as a next target, not a rejection.

---

## Tone and guardrails

- Honest but coaching. Never "you will not get in." A reach is always paired with "here is what would get you there."
- Grounded strictly in the pasted posting. No requirement the posting does not state.
- The score is guidance, not truth. Close with a line that this is practice and the student makes the call.
- No PII. Runs on the resume content, which carries no name, address, or contact details.

---

## Where it sits in the build

- **Type: a skill, not an agent.** It is a single invocation triggered by the student, even though it runs several personas inside one call. (The personas can be thought of as voices within the skill, not separate scheduled agents.)
- **Inputs it already has:** the pasted posting (`s-jobdesc`) and the active resume from the Resume Vault. No new student input required.
- **Pattern to follow:** it mirrors the existing single-request AI call used by every other Render function, so it drops onto the same server-side proxy and swaps to Gemini with the rest.
- **Base voice:** opens with the shared "You are Render" identity, then adds the hiring-committee module.

See `AVC248_RENDER_COMPETITIVE_LANDSCAPE.md` for why this step, along with portfolio review and the post-grad plan, is one of Render's few clearly differentiated features.
