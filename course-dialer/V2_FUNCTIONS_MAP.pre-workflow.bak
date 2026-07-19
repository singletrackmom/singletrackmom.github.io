# Dial Your Course · v2 Functions Map

A synthesis of Michelle’s v2 brain-dump into a clear map of functions and modules. This sits alongside `prd.html` section 7 and `V2_RESEARCH_LANDSCAPE.md`; it does not replace them. It reframes v2 as one site “holder” with a front-page launcher, a set of toggleable checker modules, a background institution-settings layer, a live research repository, and a new student-agent usability test.

**Two conventions run through everything below:**

- **[CORE · no AI needed]** runs deterministically in the browser (string matching, lookup tables, package parsing, the grounded reference library). No credential, no server, no model call. This is most of the tool.
- **[AI-ENHANCED]** needs a connected model. On the front page these functions are present but hidden (or shown as locked) until an AI is connected. Each has a “With the AI plug-in” note describing what deepens.

**The v1 vs v2 rule (say it plainly on the front page):** the same sections appear whether or not an AI is connected. v1 (no AI) shows the CORE layer of every section. v2 (AI connected) reveals the AI-ENHANCED deeper layer inside each of those same sections. Nothing is hidden that changes what the sections are; only the depth changes.

---

## (A) Shared shell · the one site holder

The container every module lives inside. LMS-independent, browser-resident, no-account, no-PII, bridge-or-proxy for any model call.

### A1 · Front-page launcher
- **Goal:** One page where the user chooses to run all checks or just one.
- **Audience:** faculty (primary); CTLE overseer (sees the same shell, plus the settings layer in D/C).
- **Process:** Lists every checker module (group B) as a row with a checkbox beside each action. Run-all, or run-one. Re-run a single check after a fix to confirm it, or skip checks that do not apply. State persists in-browser so a user can dial one thing at a time.
- **[CORE · no AI needed]**
- **With the AI plug-in:** AI-only sections un-hide and each row gains its deeper “with AI” layer; a short “what changed since your last run” summary can be generated.

### A2 · Toggle system
- **Goal:** Every check is independently switchable on/off.
- **Audience:** faculty, CTLE overseer.
- **Process:** A checkbox per action controls whether that check runs in a batch and whether it appears on the report. Supports the “fix one thing, re-run just that check” loop and the “I do not care about this one” skip. CTLE defaults (group C) can pre-set which toggles are on for an institution.
- **[CORE · no AI needed]**

### A3 · LMS-independent ingestion
- **Goal:** Accept a course in whatever form it exists, never depend on the LMS.
- **Audience:** faculty.
- **Process:** Accepts a Canvas export (`.imscc` Common Cartridge), a Word doc, a Google Doc, or other LMS export formats, plus a syllabus that is either uploaded on its own or embedded inside the course export. The tool depends on OSCQR, accessibility guidelines, and learning science, not on any one LMS. Parses to a common internal structure the modules read. (Blackboard and D2L/Brightspace export formats vs Common Cartridge is an open research item, see the Open Questions list.)
- **[CORE · no AI needed]**
- **With the AI plug-in:** messy or non-standard inputs (a loosely formatted Word doc, an odd export) can be normalized into the internal structure by the model when deterministic parsing falls short.

### A4 · AI-connection panel
- **Goal:** Let a user connect a model, or run fully without one.
- **Audience:** faculty, CTLE overseer.
- **Process:** Connect the school’s Gemini account, or whatever account/key the user supplies (endpoint is a contract, not a vendor: Gemini on Vertex, Claude, or a district-hosted model all satisfy it). No credential ever sits in the static page: the pilot pastes a composed prompt into the sanctioned model (bridge); to scale, a minimal institutional proxy holds one server-side credential behind single sign-on. Much of the non-AI work runs purely in the browser regardless.
- **[CORE · no AI needed]** to run the connection UI; the connection unlocks the [AI-ENHANCED] layer everywhere.

### A5 · Two faculty entry modes (two interfaces)
- **Goal:** Serve the “new course” builder and the “existing course” auditor as distinct experiences.
- **Audience:** faculty.
- **Process:** A fork at entry. **“Build a new course / start from scratch”** walks module-by-module and produces a course. **“My course is already built / audit it”** ingests the export and runs the checkers against it. Same modules underneath, two different front doors and flows.
- **[CORE · no AI needed]** for structure, checks, and scaffolds.
- **With the AI plug-in:** builder mode drafts prose, objective rewrites, quiz items, and grounded module arcs; auditor mode adds the redesign suggestions on top of the deterministic findings.

### A6 · Online vs in-person branch
- **Goal:** Treat modality as a first-class branch, because requirements differ.
- **Audience:** faculty, CTLE overseer.
- **Process:** A top-level choice that changes which checks fire and how. Online adds RSI (regular and substantive interaction) requirements and folds in-class studio hours into outside work; in-person does not. Connects to the accreditation model set in the institution layer (C). HLC feeds requirements, though some institutions differ, and competency-based institutions handle seat time differently (see Open Questions).
- **[CORE · no AI needed]**

---

## (B) The checker modules · each its own tab/subpage/tool

Every module is a subpage inside the holder, launchable alone or as part of run-all, each toggleable.

### B1 · Syllabus checker
- **Goal:** Confirm the syllabus carries required, verbatim language.
- **Audience:** faculty.
- **Process:** Accepts an uploaded syllabus OR one embedded in the course export. Checks the institution’s specific syllabus requirements (from layer C), including seat-hours language (required verbatim, high severity if missing or altered) and, for online, the RSI paragraph. Detects Simple Syllabus use and caveats “missing course-info” findings, since that content is not in a Canvas export.
- **[CORE · no AI needed]**
- **With the AI plug-in:** drafts a drop-in RSI statement and interaction plan the instructor edits and pastes in; rewrites weak required-section wording against the grounded reference blocks.

### B2 · Seat-time / seat-hours checker
- **Goal:** Verify the course’s hour budget against the credit-hour rule.
- **Audience:** faculty.
- **Process:** Reads the seat-hour lookup table (total student hours = credits × 40; load changes the split, not the total). Compares the course’s workload against the allowance for its credits, load, modality, and activity type. Reports over/under against the outside-work allowance. Modality-aware (online folds studio hours into outside work). Competency-based institutions are a flagged exception (Open Questions).
- **[CORE · no AI needed]**

### B3 · AI authentic-assessment alignment (its own page)
- **Goal:** Find graded items a model could complete unaided, and offer redesigns at equal cognitive demand.
- **Audience:** faculty.
- **Process:** Reads rubric criteria (not assignment titles). Bands each assessment strong / adequate / exposed against the AI-resistance framework (process evidence, secured evidence, situated context, live defense). Names the exposed items. Consults the research repository (group D) when the user asks for more on improving assessments.
- **[CORE · no AI needed]** for the banding and the grounded substitution menu (two-lane model, replacement ladder).
- **With the AI plug-in:** proposes a discipline-aware redesign for each flagged item as an editable draft under the approval gate (sends only the flagged passage, prompt, and rubric criteria; never the package, never student data). Interconnected-problems and specs-with-process-gate suggestions become one-click drafts.

### B4 · Accessibility checks
- **Goal:** Flag structural accessibility issues and frame them with legal weight.
- **Audience:** faculty.
- **Process:** Structural checks on the export: alt text, heading structure, tables, contrast, link text. Frames findings against WCAG 2.1 AA and the ADA Title II rule (compliance driver). Hands PDF/caption/alt-format work off to the institution’s existing tool (Panorama/Ally) rather than rebuilding it. Distinguishes accessibility (can a student reach content) from UDL (multiple means), which is a separate lens.
- **[CORE · no AI needed]**
- **With the AI plug-in:** drafts alt text and remediation copy for flagged items; explains a fix in plain language.

### B5 · OSCQR + learning-science / ID-model checks
- **Goal:** Read the course through the online-quality rubric and a chosen instructional-design lens.
- **Audience:** faculty.
- **Process:** Runs the deterministic third of OSCQR (with the OSCQR↔QM crosswalk, and an OLC Scorecard crosswalk to add since OLC is sunsetting OSCQR). A lens selector reframes findings through Backward Design, ADDIE, SAM, Merrill, Dick & Carey, Gagne, or connectivism; the findings do not change, the vocabulary and emphasis do. Caveat stated in the UI: popular models change over time, so the lens set is maintained, not fixed. Adds learning-science flags (retrieval-practice gap, spaced-practice gap) where detectable. Includes the Bloom’s objectives check (banned verbs, level-appropriateness, objective↔competency mapping both directions).
- **[CORE · no AI needed]** for detection, crosswalks, lens vocabulary, verb banks.
- **With the AI plug-in:** writes the last-mile sentence (e.g. rewriting “understand color theory” into a measurable objective) and attaches a grounded “why” rationale to each finding.

---

## (C) Institution-settings / CTLE layer · background

A background configuration layer fed by a campus person who oversees courses, likely in the CTLE (Center for Teaching, Learning, and Engagement). NOT fed by faculty or instructional designers. It sets the ground truth every faculty run is measured against.

### C1 · Institution profile (the settings store)
- **Goal:** Hold the institution-specific rules so the checkers are correct for this campus.
- **Audience:** CTLE overseer.
- **Process:** The overseer feeds: (1) specific syllabus requirements; (2) the accreditation model (HLC or otherwise); (3) OSCQR plus whatever else the CTLE values (OLC Scorecard, QM, ECP, local additions); (4) the institutional learning outcomes (ILOs), which differ by institution; (5) a LINK to where course competencies live (the curriculum website, which varies by district). Faculty runs read this profile; faculty never edit it.
- **[CORE · no AI needed]**
- **With the AI plug-in:** can help the overseer draft or crosswalk a new rubric block into the checkable format.

### C2 · Competency-source link (not competency entry)
- **Goal:** Point faculty to the authoritative competencies without pretending to hold them.
- **Audience:** CTLE overseer sets the link; faculty use it.
- **Process:** The overseer supplies the link to the district curriculum site (competencies are board-approved and live there, e.g. the Maricopa Curriculum Office). Faculty still must input their course competencies by looking them up on that curriculum website; the tool does not invent or store them. This preserves the “never fabricate an outcome” rule and handles the fact that outcomes do not reliably survive an export.
- **[CORE · no AI needed]**

### C3 · Accreditation-model binding
- **Goal:** Connect the institution to the right accreditation requirements.
- **Audience:** CTLE overseer.
- **Process:** Selects the accreditation model that feeds requirements (HLC by default in this region, with room for institutions that differ). Drives the online-vs-in-person branch (A6) and the seat-time checker (B2), including the competency-based exception that must be handled differently from seat-time institutions.
- **[CORE · no AI needed]**

---

## (D) The authentic-assessment research repository + its updater agent

A live-updated body of scholarship the assessment module draws on, so recommendations are grounded, not invented.

### D1 · Research repository
- **Goal:** A current, vetted store of books, articles, scholarly journals, and research on authentic assessment.
- **Audience:** faculty (consumed indirectly, through the assessment module).
- **Process:** When a user clicks “give me more information about ways to improve my assessments,” the assessment module (B3) consults this repository and returns grounded suggestions with citations, not model-invented text. Runtime is deterministic retrieval: a finding type selects a block. Seeded from the existing reference corpus (`AUTHENTIC_ASSESSMENT.md`, `ALTERNATE_ASSESSMENTS.md`, and the wider `tools/reference/` library) and the overnight landscape research (`V2_RESEARCH_LANDSCAPE.md`).
- **[CORE · no AI needed]** at runtime (retrieval only, no live scholarly calls in the trust path).

### D2 · Repository updater agent / skill
- **Goal:** Keep the repository current so it never goes stale.
- **Audience:** the tool maintainer (background); serves faculty.
- **Process:** An agent or skill periodically searches news and scholarly sources for newly published work on authentic assessment, using the open, keyless indexes already identified (OpenAlex, ERIC, Semantic Scholar, CORE, Crossref). New material is vetted before it enters the repository, and every change is versioned so the advice is auditable. This is a build-time refresh loop, not a runtime call.
- **[AI-ENHANCED]** (the search/summarize/triage step uses a model; a human vets before publish).
- **With the AI plug-in:** the agent drafts candidate summaries and proposed repository entries from the newly found sources for human vetting.

---

## (E) The student-agent usability test · new section

A usability test that runs the course through synthetic students, modeled on what WGU does: train agents on demographic information, then have them test the course for understanding. There is working precedent in the repo (the `airc-sss/` student-journey study already runs 50 in-character synthetic-student agents against live sites; see Open Questions for the exact location).

### E1 · Demographic-trained student agents
- **Goal:** Reveal where a real student like this one would struggle in the course.
- **Audience:** student-agent (the test participant); results go to faculty and CTLE.
- **Process:** Agents are instantiated from demographic profiles and behave with that student’s exact knowledge, habits, patience, device, and reading level, never with an AI’s competence. They attempt a real task in the course (find the objective, start the first assignment, understand what is due) and think aloud, stopping where a real student would give up. Default population: Maricopa student demographics, so the course is checked against Maricopa students.
- **[AI-ENHANCED]** (agents require a connected model).
- **With the AI plug-in:** this whole section only exists with AI connected; without it, the section shows as a locked/preview row on the front page.

### E2 · Department-specific demographic feed
- **Goal:** Let the test reflect the actual student who takes this course.
- **Audience:** CTLE overseer or faculty feed it; student-agents consume it.
- **Process:** CTLE or faculty feed in department-specific demographics (e.g. what a psychology major looks like), sourced from Institutional Research. This tunes the agent population beyond the campus-wide default so a course is tested against its real audience, not a generic student.
- **[CORE · no AI needed]** to store/manage the demographic profiles; **[AI-ENHANCED]** to run the agents against them.

### E3 · Usability findings report
- **Goal:** Turn agent runs into course fixes.
- **Audience:** faculty, CTLE overseer.
- **Process:** Aggregates each agent’s think-aloud into where students got confused, what they misread, and where they quit, mapped back to the specific module or page. Feeds the same report the other modules write into, toggleable like the rest.
- **[AI-ENHANCED]**
- **With the AI plug-in:** clusters findings across agents and proposes the specific wording or structure change that would unblock the confused students.

---

## Open questions / research needed

- **Blackboard and D2L/Brightspace export formats vs Common Cartridge.** Confirm what Blackboard and Desire2Learn/Brightspace use for course export/import, and whether it is consistent with Canvas Common Cartridge (`.imscc`). The ingestion layer (A3) is built to be LMS-independent, so this determines how much per-format parsing is needed. Not yet verified.
- **WGU / HLC accreditation and competency-based seat time.** Is WGU accredited by HLC, and how do competency-based institutions handle seat-time requirements? Michelle’s WGU prep material notes WGU is competency-based, online, ~192,000 students, which is exactly the case that breaks the credits × 40 seat-time rule. Note the competency-based vs seat-time accreditation difference as an open item feeding B2, A6, and C3.
- **Where the overnight research data and the WGU transcript currently live.**
  - *Overnight research data: FOUND.* The data gathered “the other night” is `course-dialer/V2_RESEARCH_LANDSCAPE.md` (compiled July 18, 03:49) plus the reference library refreshed the same night (`tools/reference/ALTERNATE_ASSESSMENTS.md`, `UDL_3.md`, `RSI.md`, `ID_MODELS.md`, `OSCQR_QM_CROSSWALK.md`, `README.md`, all July 18, 03:24 to 03:26). There is no separate JSON/CSV scholarly dataset in the dial directory; the “data” is these vetted markdown files. Confirm this is what she meant.
  - *WGU presentation transcript: NOT FOUND.* No interview or presentation transcript file exists. What exists is Michelle’s WGU interview-prep hub in `wgu/` (`index.html`, `flashcards.html`, `mock-interview.html`, `cheatsheet.html`) for a “Future of Education Strategist, AI Innovator” role. The student-agent usability idea modeled on WGU is realized in `airc-sss/agents/` (50 synthetic-student agents plus `airc-sss/synthetic-student-agent.md`, the template). If a transcript exists, it is outside this repo. Ask Michelle where it lives.

---

## How this changes the current PRD (deltas from section 7 · do not edit the PRD)

- **From four tabs to a launcher of toggleable modules.** Section 7 frames v2 as a four-tab shell (Audit / Builder / Syllabus / Report). This map reframes the front page as a launcher where every check is an on/off row you can run alone or all at once, so a user can re-run one check to confirm a fix. Bigger organizing idea than “tabs.”
- **v1-vs-v2 as a visibility layer, not two products.** New framing: the same sections show whether or not AI is connected; AI-only functions are hidden/locked until connected, and each section carries a separate “with the AI plug-in” deeper layer. Section 7 treats v2 as the generative layer added to v1; this makes it one interface that reveals depth.
- **AI authentic-assessment alignment becomes its own page.** Section 7 embeds the redesign work in the audit; here it is a standalone module with its own tab, wired to the live research repository.
- **A live research repository plus an updater agent.** Section 7’s reference library is refreshed by hand at build time. This adds a user-facing “give me more on improving my assessments” repository and an agent/skill that periodically pulls new scholarship from the open indexes for vetting. New moving part.
- **An institution-settings / CTLE layer.** Section 7 has faculty type objectives by hand but does not name a separate overseer role. This adds a background settings layer fed by a CTLE overseer (syllabus rules, accreditation model, rubric set, ILOs, competency-source link), distinct from faculty and IDs.
- **LMS-independence stated as a first principle.** Section 7 is Canvas-`.imscc`-centric. This makes ingestion explicitly format-independent (Canvas export, Word, Google Doc, other LMS exports; syllabus uploaded or embedded) and depends on OSCQR, accessibility, and learning science rather than any LMS.
- **Online vs in-person elevated to a top-level branch, tied to accreditation.** Section 7 handles RSI and seat-hours modality inside checks; this promotes modality to a front-page fork bound to the accreditation model (HLC), and flags competency-based institutions (e.g. WGU) as a seat-time exception.
- **A new student-agent usability test.** Not in section 7 at all. Demographic-trained synthetic students (Maricopa default, department-specific via IR) run the course and report where a real student would struggle, modeled on WGU’s approach and on the existing `airc-sss/` agent study.
- **Two faculty entry modes as two interfaces.** Section 7 has builder mode; this makes “start from scratch” and “audit my built course” two distinct front doors over the shared modules.

---

## v2 additions (July 19, second brain-dump)

### B6. Course-level assessment module  [CORE, with an AI-ENHANCED layer]
Goal: give every course a place to do its course-level assessment, and generate feedback for the many courses that currently get none.
- Current process is simple and the college is actively improving it: pick a competency, describe what you are doing and how it is working, then after you assess, note what you will improve. Build this flexibly so it can follow the college's evolving model. Do NOT hard-code the current steps.
- Michelle to co-develop the actual page with the campus assessment coordinator.
- Build in an optional end-of-course student survey the tool can generate and drop into the course, so every course can collect feedback (many never do).
- Output can include a robust feedback instrument (like the AVC100 survey), beyond the basic department-level teacher evaluation adjuncts already receive.
- With the AI plug-in: help draft the competency narrative, suggest survey questions aligned to the course objectives, and summarize returned survey data into "what to improve" prompts.

### B7. RSI (Regular and Substantive Interaction) module  [CORE, with an AI-ENHANCED layer]
Goal: help online courses describe and meet RSI.
- Explain what RSI is and what it means, in plain terms.
- Offer a suggestion, or simply ask the instructor how they are implementing it.
- With the AI plug-in: evaluate the described approach and respond that it looks adequate, or offer specific additional suggestions.

### Seat-time display convention (for the style guide)
When the tool writes the dialed seat time back into the course, every module gets a consistent time-on-task note at the top.
- Accessibility rule: meaning must live in the words, not the styling (WCAG 1.3.1 and 1.4.1). Italics alone is not enough.
- Pattern: a short line led by a bold label, e.g. "Estimated time: about 2 hours on this assignment."
- May be visually set off (muted color or a light box in the palette fill) so it does not read as body content, but the label text is what carries the meaning.
- Add to the style guide as a defined component, "Time-on-task note," with fixed markup so every module renders it identically.

### Writeback / export logistics (honest status)
- Read side works: the tool parses a Canvas Common Cartridge (.imscc) export.
- Content writeback is mechanically feasible: unzip the .imscc, edit the module HTML (for example inject the time-on-task note at the top of each module page), update the manifest as needed, re-zip as .imscc, and the instructor re-imports via Canvas's Common Cartridge import.
- Known blocker: learning outcomes/objectives do not reliably survive the Canvas export (see canvas/reference/CANVAS_OUTCOMES_EXPORT_BUG.md). That is why alignment relies on objectives entered by hand in builder mode, not read from the export. Content and seat-time writeback is solvable; outcomes writeback is not yet.
