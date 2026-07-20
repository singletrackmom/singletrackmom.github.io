# Mines portfolio audit and spruce-up

**Written:** July 20, 2026, for the current Mines OLED posting (JR108710, the newer JD, no DesignPLUS / no Canvas-plugin requirement).
**Supersedes:** the July 13 GAP_FILL_PLAN (that was WGU + Mines on the old JD). This one is Mines-only, current JD.

**Goal:** make the two course case studies read, in ten seconds, as a full ID cycle (outcomes, aligned assessment, scaffolded modules, UDL, accessibility, measured iteration), and reorder the Work page so the course/ID work leads and the personal agents stop crowding it.
**Audience:** a Mines Online reviewer (Sam Spiegel, Megan Sanders) scanning fast, plus you, editing.
**Process:** ready-to-paste blocks below. Approve or edit, and I apply them. Nothing is edited until you say go (your rule).

---

## Priorities, in order

1. **Add the scannable "design, end to end" block to both course pages.** Highest-value edit for Mines. Blocks below.
2. **Label AVC100's evidence as an assessment instrument, and add the respondent count.** You have real data; make it read like assessment science.
3. **Add AVC248 a "how I will measure it" block.** It runs Fall 2026, so this is an honest plan, not numbers.
4. **Reorder Work so Learning design leads,** and thin the personal-agents section for the Mines window.
5. (Still open from the old plan, still valid) **a short course-review / accessibility page.** Mines names ADA/WCAG; your fifteen years as QM/OSCQR lead reviewer has no home on the site. One hour, high payoff. Say the word and I build it.

---

## The dashboards question, answered honestly

You asked for dashboards. Here is the honest split, because a fabricated number in front of an assessment scientist ends the interview:

- **AVC100 has real data already.** The pre/post bars are on the page (intimidation 3.3 to 2.0, "know where to get help" 3.4 to 4.8, end-of-term measures 4.6 to 4.9). Do not invent more. Do two things: (a) **label the instrument** ("end-of-course survey, Likert, pre/post design"), and (b) **add the respondent count** (n = the real number who completed it). n is what makes it read as measurement instead of vibes. Pull it from the survey.
- **Pull your Canvas New Analytics numbers for a second, harder metric.** As the instructor you have New Analytics on your own sections: on-time submission rate, grade distribution, weekly activity. Course &rarr; New Analytics &rarr; export CSV. One line like "on-time submission rose from X to Y after the redesign" is the metric a reviewer respects most, because it is behavior, not self-report. If you can get the district success-rate (pass / DFW) for AVC100 before and after from Institutional Research, that is the gold one.
- **AVC248 has no data yet and that is fine.** It runs Fall 2026. Its "dashboard" is a measurement plan (below), stated as a plan. Honesty here is a strength, it shows you design the measurement before the course runs.
- **Tableau: only if it is real.** If Maricopa IR gives you a real course-success dashboard, screenshot it and we embed the image. Do not build a Tableau-looking chart with invented numbers.

---

## CASE STUDY 1 · AVC 248 (`learning-design/avc248.html`)

The page is already good (Goal, Audience, Process, authentic assessment, WCAG + UDL, Status). Two adds.

### Add A · the scannable cycle block
Paste this **right after the `<div class="links">...</div>` block and before `<div class="prose">`** so a reviewer sees the whole cycle before reading. Uses existing classes, bold lead-ins only (your rule).

```html
  <div class="prose">
    <p class="sec">The design, end to end</p>
    <p><strong>Outcomes.</strong> Designed backward from measurable competencies, with a competency map tying every module to the program outcome it serves.</p>
    <p><strong>Aligned assessment.</strong> Each outcome is evidenced by a real artifact and a spoken project walkthrough, so the proof is the student&rsquo;s own performance, not an exam a model could sit.</p>
    <p><strong>Scaffolded modules.</strong> Nine modules move students from AI literacy to a finished portfolio, a career plan, and a portable career agent, each module a step built on the last.</p>
    <p><strong>Universal Design for Learning.</strong> The construct stays fixed while the way students demonstrate it flexes, a written rationale or a recorded walkthrough, so the same competency is reachable more than one way.</p>
    <p><strong>Accessibility.</strong> Built to WCAG 2.1 AA from the first draft and packaged as a clean IMSCC import, so another instructor can adopt it without rebuilding.</p>
    <p><strong>Measured iteration.</strong> The full structure runs first in Fall 2026; the measurement plan is below.</p>
  </div>
```

### Add B · the measurement plan (honest, no numbers yet)
Paste this as a new section **just before the `Status` section**:

```html
    <p class="sec">How I will measure it</p>
    <p>The course is designed to be evaluated against its outcomes, not against completion alone. In the Fall 2026 run I will track competency mastery from the artifact rubrics, a pre and post measure of AI confidence and career readiness, on-time submission and engagement from Canvas analytics, and Render&rsquo;s first usability data. The measurement is designed before the course runs, so the first cohort produces a baseline the next one is compared against.</p>
```

---

## CASE STUDY 2 · AVC 100 (`avc100/overview.html`)

Already strong: real pre/post charts, an unsolicited student quote, honest small-n framing. Three surgical adds, no restructure.

### Add A · the scannable cycle block
Paste **right after the `<div class="hero-media">...</div>` and before `<div class="prose">`** (matches AVC248, so the two pages read as a pair):

```html
  <div class="prose">
    <p class="sec">The design, end to end</p>
    <p><strong>Outcomes.</strong> Backward-designed from the reasons students actually fail the course, with the college&rsquo;s Personal and Community Well-Being outcome assessed here rather than saved for a capstone most of these students never reach.</p>
    <p><strong>Aligned assessment.</strong> One project carried across three tools, each stage assessed by a four-step critique and closed by an end-of-course instrument that measures the outcomes the redesign targeted.</p>
    <p><strong>Scaffolded modules.</strong> A single project moves Illustrator to Photoshop to After Effects, with student-support touchpoints built into the high-risk early weeks rather than offered on the side.</p>
    <p><strong>Universal Design for Learning.</strong> Multiple means of engagement and expression, grounded in the persistence literature (Tinto, Astin), so support reaches the students least likely to seek it out.</p>
    <p><strong>Accessibility.</strong> WCAG 2.1 AA built into every page from the first draft, packaged as a clean IMSCC import.</p>
    <p><strong>Measured iteration.</strong> Evaluated with a pre and post survey design; a week-one baseline was added so later cohorts compare against their own start. Results below.</p>
  </div>
```
Note: this repeats a couple of lines that already appear lower in the prose. That is intentional, the block is the ten-second summary and the prose below is the detail. If you would rather not repeat, I can trim the lower prose when I apply it.

### Add B · label the instrument and add n
In the `Evidence` section, change the first sentence from:
> The redesign is evaluated against its stated aims rather than against completion counts alone, using a pre and post design.

to (fill in the real n):

```html
    <p><strong>Assessment instrument.</strong> An end-of-course survey (Likert scale, pre and post design) administered to the first section in its final week, n = [FILL IN]. It measures the outcomes the course was built to move, and a week-one baseline was added in the fall so cohorts can be compared against their own starting point.</p>
```

### Add C · the behavioral metric (if you can pull it)
If Canvas New Analytics or IR gives you a real number, add one line to Evidence:

```html
    <p><strong>Behavioral signal.</strong> Beyond self-report, [on-time submission rose from X to Y / the course success rate moved from X to Y] between the pre-redesign section and the redesigned one. (Pull from Canvas New Analytics or Institutional Research; use only the real figure.)</p>
```

---

## WORK PAGE reorder (`work.html`)

Right now it leads with "AI tools & strategy" and ends with six personal agents. For a Mines ID reviewer that buries the course work and pads the page. Your instinct is right, here is the surgical version, reversible, and still fine for your broader job search.

**1. Reorder the sections** so learning design leads:
- Learning design (AVC248, AVC100, Design history)
- AI-assisted design (rename "AI tools & strategy" &rarr; the same cards, reframed: Dial Your Course, Syllabus Checker, Student Journey study, Render, CopaMigo, Cultivate, these ARE your ID work done with AI, which the JD lists as a preferred qualification)
- Current research (Authentic Assessment leads, very on-target for Mines)
- Program development
- Experiential learning
- Agentic & personal build (last)

**2. Rewrite the intro line.** Current: "The AI tools come first because that is where my attention is now." Proposed:

```html
  <p class="page-sub">Decades of online course design and instructional design, now built with AI. The course and learning-design work comes first; the tools below are the same practice, extended, an AI course reviewer, a student-journey study, a career-launch environment. The Traveler, the Design Studio, and the internship program still run every year.</p>
```

**3. Thin the personal agents for the Mines window (your call).** The six-card "Agentic & personal build" section (Wayfinder, Soar, Focus, Devan, Summer Work, Find Your Flow) is the least relevant to Mines, a road-trip planner and a photo-gig board do not read as learning design. Options, least to most aggressive:
- **Keep all six at the bottom** (they are already last). Lowest effort, still pads the page.
- **Recommended: keep Wayfinder only** as proof you build agentic tools, cut the family agents from this page (they live at their own URLs regardless, and are shared directly with family, not via Work). One card, framed as "an agentic build," carries the signal without the clutter.
- **Cut the whole section** for now. Cleanest for Mines, but you lose the "I build agents" proof entirely.

Do NOT delete the pages, just which cards show on Work. And remember this page serves your whole search, not only Mines, so leading with learning design is a good default for the ID / LX / UX roles you are targeting anyway.

---

## What I did NOT change, and why
- **The personal builds are not hobby clutter in general,** they are your rarest asset (AI-assisted building, a preferred qual almost no ID candidate has). The fix is ordering and framing, not deletion.
- **AVC100's data stays exactly as measured.** I am labeling and adding n, not touching a number.
- **No new design system,** every block above uses the page&rsquo;s existing classes and your bold-lead-in rule.

## Ready when you are
Say which blocks to apply (all, or pick), give me the AVC100 n and any Canvas number, and tell me the personal-agents choice. I apply the edits, back up each file first, and commit them for your push.
