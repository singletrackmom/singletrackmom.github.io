---
name: build-a-course
description: Build a complete, standards-aligned online course from vetted open educational resources, backward-designed from stated outcomes, using a panel of synthetic subject-matter-expert, instructional-designer, and synthetic-student agents, with a required human-in-the-loop review before any student sees it. Use when a designer or a teaching-and-learning center needs a rigorous first build of an online course (credit-bearing or professional education), especially an OER build where a human SME has not yet been assigned. Encodes the quality standards up front so every build starts compliant.
---

# Build a course

**Goal:** turn a set of learning outcomes (or a published source course) into a complete, standards-aligned online course draft, assembled from vetted OER by an orchestrated panel of synthetic subject-matter-expert and instructional-designer agents, and hand the designer a rigorous starting point to finish WITH the faculty member who will teach it. Never ship without a human subject-matter expert.

## The non-negotiable: a human closes the loop
The output is a **draft**, never a finished course to drop on students. The build
produces a course plus a review packet, and delivery is gated on a **named human
subject-matter expert** reviewing and signing off. The synthetic SME accelerates the
draft; it does not replace the person who owns accuracy and teaching. Nothing is
scraped without consent, every source is licensed and cited, and no course reaches a
student unreviewed. (This is the deliberate opposite of tools that repackage faculty
content without consent or review.)

## Intake — the parameters (the "Dial" elements)
Collect, or confirm defaults, before building:
- **Outcomes / source course** — published outcomes, or a source course to adapt (attribution only, never claimed as endorsed).
- **Discipline, level, prerequisites.**
- **Credits → seat time** — sized to the accreditor's credit-hour rule (HLC: ~45 hrs/credit); every module and task states its estimated time.
- **Modality** — facilitated or self-paced; LMS target.
- **Assessment stance** — authentic, simulation-based, AI-resistant, apply-level or higher; projects over exams.
- **Standards** — OSCQR (or QM), Regular and Substantive Interaction, WCAG 2.1 AA, UDL.
- **Materials policy** — OER-first; adaptable vs link-only by license.
- **Teaching presence** — getting-started module, communication cadence, feedback, netiquette.
- **Student readiness** — required software and a recording/screencast setup guide.
- **Metrics** — end-of-course improvement survey, seat-time validation, learning measurement, a term-over-term dashboard.
- **Style guide** — brand colors (solid only, no gradients), fonts, layout.

## The agent panel
Spawn, per build, a small panel of expert agents (via the Agent tool). Hold each to the
intake parameters. Have them verify one another adversarially before anything is kept.

### Subject-matter-expert agent (synthetic SME)
- **Persona:** PhD in the course discipline, 10+ years at a top research university, active practitioner.
- **Job:** source the strongest vetted materials (interactive-first, correctly licensed), verify technical accuracy, pin readings to specific chapters/sections, and flag every claim that a *human* SME must confirm. It never asserts unverifiable domain fact as settled.

### Instructional-designer agent
- **Persona:** PhD in instructional design / learning sciences, 10+ years at a top research university.
- **Job:** backward design and constructive alignment (every activity and assessment traces to an outcome), OSCQR/RSI/UDL compliance, authentic simulation-based and AI-resistant assessment design, seat-time budgeting, teaching-presence plan, and the metrics instruments.

### Synthetic-student agent (learner reviewer)
- **Persona:** models the incoming learner by ACADEMIC preparation, not demographics — prior coursework, probable undergraduate pathway, assumable tools and vocabulary.
- **Job:** read each drafted module as that learner would and flag prerequisite gaps, unscaffolded jargon, reading-level and cognitive-load mismatches, and unrealistic workload. Output is *likely friction* for a human to confirm with real learners; it never certifies that learning occurred and does not replace learner testing.

### How they run
For each outcome/module: the ID agent drafts the design and assessment; the SME agent
sources and vets the content and readings; a verification pass has each critique the
other (alignment, rigor, license, accuracy, AI-resistance); only what survives is kept.

## Build sequence
1. Backward-design the outcomes into modules and a seat-time budget.
2. Per module: ID drafts design + assessment; SME sources + vets materials; adversarial verify; synthetic-student agent reviews for learner fit; revise.
3. Author authentic, simulation-based, AI-resistant assessments (formative → summative).
4. Add the teaching-presence layer: getting-started module, RSI plan, communication cadence, feedback, netiquette.
5. Add accessibility (WCAG/UDL), the student software + recording guide, and the metrics instruments.
6. Apply the style guide.
7. Compile the course and a **human-review packet** (what to confirm, where accuracy is unverified, licensing notes).
8. **STOP at the human SME checkpoint.** Do not present the course as delivery-ready until a named human SME has reviewed and signed off.

## Authoring standard (non-negotiable depth and links)
The course is authored to full graduate depth in the LMS view itself, not summarized. A reviewer or a hiring committee should be able to open any module and see a complete two-week (or one-week) unit, not a paragraph of notes. Every module block contains, in this order:

1. **Instructor notes at the very top, grouped in one box.** Recording plan, RSI cadence, seat-time breakdown, common student pitfalls, deck pointer. Everything below the box is what the student sees.
2. **Overview** (what the unit does and which course outcomes it serves).
3. **By the end you will be able to** (module-level outcomes).
4. **Watch** (recorded-lecture outline plus the linked slide deck with speaker notes).
5. **Read** (each OER pinned to specific chapters/sections, with its license chip).
6. **Practice, formative** (numbered, step-by-step, with a stated low-stakes deliverable).
7. **Assessment, summative simulation** (named scenario, numbered do-this-first-then-this steps, what to submit, a grading rubric table, and a "why this resists generative substitution" note).
8. **Discussion, RSI** (prompt, post-by/reply-by cadence, instructor role).
9. **Course tutor** (the course-grounded chatbot note).

Never ship a module that is shorter than the source material a student would expect for the credit hours. If a block reads as "quick notes," it is not done.

**Links: hyperlink the words, never paste a raw URL.** Every resource, tool, dataset, and reading is an anchor on its descriptive name, for example `<a href="URL" target="_blank" rel="noopener">MLU-Explain Linear Regression</a>`. Do not leave a bare `https://…` visible in the text, and do not make the visible link text be the URL itself (`<a href="URL">URL</a>` is wrong). The reader should see the name of the destination, not its address. Verify at build time that zero bare URLs and zero url-as-link-text remain before the file is considered complete.

**Slide decks are real files, not placeholders.** If the deck exists, link it as "slide deck, speaker notes inside"; never label it "(build)" once it is built. Re-check any third-party tool for deprecation notices at build time and swap deprecated tools (for example, replace a retired sandbox with a live equivalent).

## Output
- A complete course draft (structure, materials with licenses, assessments, rubrics, teaching-presence plan, accessibility, metrics).
- A review packet flagging every item a human SME must confirm.
- A short build log naming the standards met and the sources verified.

## Guardrails
- Human sign-off is required before delivery. No exceptions.
- No content is used without consent or license; everything is cited.
- The synthetic SME's accuracy is provisional until a human confirms it.
- Attribution to any source course is factual only; never imply affiliation or endorsement.
