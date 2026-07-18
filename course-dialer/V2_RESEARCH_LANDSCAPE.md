# Dial Your Course v2, research landscape

A single decision document. What is out there in instructional design and course-quality tooling, what each tool does, and what the Dialer should plug in, differentiate against, or leave alone. Built to be scanned and marked up.

**Compiled:** July 2026 · for v2 planning (`prd.html` section 7) · sources cited inline.

## How to read this and what it does NOT repeat

This builds ON the existing v2 design and the reference library. It does not re-explain material already written up in those files. Assume the following is already decided and go from there:

- The v1 tool, its 19 deterministic checks, the seat-hour math, the AI-resistance audit, the no-PII / no-server / bridge-or-proxy model. See `prd.html`.
- The v2 feature set already specified: alternate-assessment menu, UDL recommendations, RSI writer, ID-model lens, builder mode, rolled-in syllabus checker, four-tab shell, multi-format export, the grounded reference library. See `prd.html` section 7.
- The reference library content: `ALTERNATE_ASSESSMENTS.md`, `UDL_3.md`, `RSI.md`, `ID_MODELS.md`, `OSCQR_QM_CROSSWALK.md`, `BLOOMS.md`, `SEAT_HOURS.md`.

New here: the competitor/adjacent tool map, the standards and rubrics beyond OSCQR/QM, deeper assessment scholarship, the learning-science layer that could power recommendations, the state of AI-in-ID, and a synthesized, prioritized feature wishlist.

**The one-line differentiator to protect:** almost everything below does audit OR build. Very little does both, and nothing does both as a static, browser-resident, no-account, no-PII file that returns a reimportable Canvas package. That gap is the whole opportunity.

---

## 1. Competitor and adjacent tools (the landscape the Dialer sits in)

Read the AUDIT / BUILD / BOTH tag first. The Dialer is aiming at BOTH, which almost no one occupies.

### 1a. Canvas accessibility and design tools (the Dialer's closest neighbors)

**Cidi Labs DesignPLUS** — *audit + build (design), commercial LTI*
Sidebar tools inside the Canvas editor: templated page/course design, plus live accessibility and usability checkers (heading structure, alt text, link text, color contrast) that flag issues while you edit. 2025 added interactive elements, an "External Assets" importer, and a table-to-responsive-columns converter. Meets WCAG 2.1.
- **Learn from:** design-time-not-review-time checking (catch it while editing, not after export). Responsive-columns idea maps directly onto the Dialer's inline-CSS constraint.
- **Differentiate:** DesignPLUS is a paid, per-seat, live-in-Canvas product that requires institutional licensing and edits in place. The Dialer is a free static file that works on an export with no account and no LTI, and it reasons about pedagogy (seat hours, objective alignment, AI-resistance) that DesignPLUS does not touch.
- https://cidilabs.com/ · https://cidilabs.com/accessibility/

**UDOIT (Universal Design Online content Inspection Tool)** — *audit only, open source + commercial*
Scans Canvas pages, announcements, discussions, assignments, quizzes for accessibility issues and offers guided fixes. Original UDOIT is GPLv3 open source (UCF). "UDOIT Advantage" (now Cidi Labs, SaaS) extends scanning to uploaded PDF/Word files. Universities of Wisconsin folded Advantage into their checker in June 2025.
- **Learn from:** the open-source posture, the clear "here is the issue, here is the fix" report grammar, and the file-format coverage (scanned/untagged PDFs).
- **Differentiate:** accessibility only, live in Canvas, no pedagogy, no build side. The Dialer's accessibility is one of many lenses and it runs on a portable export.
- https://cidilabs.com/landing/udoit/ · https://github.com (UCF UDOIT, GPLv3) · https://cdl.ucf.edu/teach/accessibility/udoit/

**Anthology Ally (formerly Blackboard Ally)** — *audit + remediate (accessibility), commercial*
LMS-agnostic. Scores content accessibility, gives instructors guided remediation, and auto-generates alternative formats for students (audio, ePub, electronic braille, tagged PDF, translated, Immersive Reader). 2025 improved math accessibility and video-format support.
- **Learn from:** the alternative-formats concept is the strongest expression of "representation" (a UDL principle) in the market. The instructor-facing accessibility score is a good motivator pattern.
- **Differentiate:** Ally is a paid, always-on institutional integration focused solely on content accessibility and student-facing formats. It never touches objectives, assessment validity, seat time, or course build.
- https://ally.ac/ · https://help.anthology.com/ally-lms/en/about-ally-and-accessibility.html

**YuJa Panorama** — *audit + remediate (accessibility), commercial*
The tool the Dialer PRD already routes PDF work to. Analyzes uploaded documents, HTML pages, and WYSIWYG content for headings, alt text, contrast, untagged PDFs; offers inline remediation without re-upload; generates 20+ alternative formats; auto-checks embedded videos for captions; institutional dashboard. GCC/the district already licenses it.
- **Learn from:** the "don't reimplement what the institution owns" boundary the PRD already draws. Panorama's caption-presence check and alt-format generation are exactly what the Dialer should NOT rebuild.
- **Differentiate:** same as Ally, plus the Dialer explicitly hands PDF/caption work off to Panorama and spends its effort on pedagogy and build.
- https://www.yuja.com/panorama/canvas-lms-accessibility-solution/

### 1b. Quality-review rubric tooling (the Dialer's methodological neighbors)

**Quality Matters — Course Review Management System (CRMS)** — *audit only (workflow), membership-gated*
The official QM platform for managing peer course reviews against the QM Higher Ed Rubric (7th ed., 8 General Standards, 43 Specific Review Standards). Includes a Self-Review Tool with annotations and note-taking. Requires a MyQM account and paid membership.
- **Learn from:** the annotation-per-standard structure, the self-review-before-formal-review workflow (the Dialer's exact "private rehearsal" pitch), and the essential-standards threshold model.
- **Differentiate:** CRMS is a human review-management system behind a paywall and login; it does not parse a course or compute anything. The Dialer automates the countable third of that same rubric for free, with no account, and returns fixes rather than a checklist. The reference library already carries the OSCQR↔QM crosswalk.
- https://www.qualitymatters.org/qm-membership/faqs/course-review-management-system · https://www.qualitymatters.org/qa-resources/rubric-standards/higher-ed-rubric

**OLC Course Review Scorecard (2025, replaces the OLC Quality Scorecard + QCTIP and, per OLC, is meant to supersede OSCQR)** — *audit only (rubric), free/open*
Released March 2025. 50 measurable objectives across three categories: Essential Design (20 indicators), Advanced Design (15), and Course Delivery. Free, open-access, adopt-as-is or adapt. This is a significant standards event: **the rubric the Dialer maps to (OSCQR) is being sunset in favor of this one.**
- **Learn from / act on:** add an OLC-Scorecard crosswalk alongside the existing OSCQR/QM one. The Essential-vs-Advanced split is a natural severity model for findings. This is the most important 2025 standards development for the Dialer to track.
- https://onlinelearningconsortium.org/olc-insights/2025/03/new-course-review-scorecard/ · https://onlinelearningconsortium.org/quality/scorecards/course-review/

**Anthology (Blackboard) Exemplary Course Program (ECP) Rubric** — *audit only (rubric), free rubric*
Dichotomous Met/Not-Met rubric, 53 standards in 4 categories (course design, interaction & collaboration, assessment, learner support), 191 points, weighted 1–5 with 5 = compulsory; 85% = Exemplary. Freely downloadable.
- **Learn from:** the weighted-standard model (compulsory 5s vs. nice-to-have 1s) is a cleaner severity scheme than OSCQR's flat 3-2-1, and it foregrounds interaction/collaboration, the Dialer's biggest gap area.
- https://www.anthology.com/blackboard-exemplary-course-program · https://www.niu.edu/blackboard/exemplary-course-program/rubric.shtml

### 1c. Curriculum-mapping and syllabus tooling (the Dialer's build-side neighbors)

**Coursetune** (owned by Academic Partnerships since 2021, not Intellidemia) — *build (design/mapping), commercial*
Visual, learner-centered curriculum-mapping and course-design tool: map outcomes, align assessments, communicate complex curriculum across a team. Backward-design oriented.
- **Learn from:** the visual alignment map (objective → assessment) is the polished version of the Dialer's alignment matrix, and the program/curriculum level is where the Dialer's outcome work wants to go once the export problem is solved.
- **Differentiate:** Coursetune is a paid, team, cloud design environment that does not audit an existing exported course or return a package. The Dialer starts from a real course file.
- https://app.coursetune.com/ · https://www.prnewswire.com/news-releases/academic-partnerships-acquires-coursetune-inc-a-leading-edtech-provider-of-curriculum-mapping-software-for-higher-education-301360670.html

**Intellidemia Concourse Syllabus** — *build (syllabus), commercial*
Cloud, template-based syllabus management: create, revise, audit, and report on syllabi; integrates with LMS/SIS; template-driven compliance for accreditation. Partnered with Modern Campus.
- **Learn from:** template-enforced required language and syllabus-level accreditation reporting is exactly the job of the Dialer's rolled-in syllabus checker (seat-hours verbatim language, RSI paragraph). Concourse proves institutions will pay for template compliance; the Dialer can do the checkable part for free.
- **Differentiate:** Concourse is a paid institutional syllabus repository, not a course-content auditor or builder.
- https://www.intellidemia.com/

**Simple Syllabus** — *build (syllabus), commercial*
Canvas-embedded, centralized syllabus repository; pulls catalog descriptions, policies, instructor details, and assignment schedules out of Canvas to auto-populate; template-driven compliance; accreditation reporting. Already flagged in `prd.html` section 11 as a source of the "info lives in Simple Syllabus, not in the export" false-negative risk.
- **Learn from / act on:** the Dialer should detect when a course uses Simple Syllabus and suppress or caveat the "missing course-info" findings, since that content will not be in the export. This is a real accuracy fix, not just a competitor note.
- https://simplesyllabus.com/canvas-syllabus/

### 1d. Native Canvas features (the free baseline to build around, not against)

**Canvas Blueprint, Outcomes, Learning Mastery Gradebook, Mastery Paths** — *build + track, native/free*
Blueprint pushes a locked master course to many sections. Outcomes attach to rubric criteria; the Learning Mastery Gradebook tracks mastery over time rather than percentages; Mastery Paths route students by performance.
- **Learn from / act on:** these are the rails the Dialer's outcome-alignment and multi-section consistency features ride on. The Blueprint model is the institutional answer to "one approved course, many sections" that the Dialer's departmental pilot targets. Note the hard constraint already documented in `prd.html` section 11: Outcomes do not reliably survive an `.imscc` export, which is why the builder takes objectives by hand.
- https://community.canvaslms.com/ (Outcomes / Learning Mastery) · https://teaching.pitt.edu/resources/track-student-progress-with-outcomes-and-the-learning-mastery-gradebook/

### 1e. AI course/lesson generators (2025–2026, the build-side frontier)

These are where "build a course from an idea" is happening now. None audit an existing exported course against a quality rubric, and none are data-sovereign. They are the build-side bar to clear.

**Coursebox AI** — *build only, commercial SaaS*
Turns a PDF, video, or URL into a structured course with lessons, quizzes, an AI chat-tutor, and AI-avatar video; AI grading against a rubric. Named a 2025 top AI authoring tool.
- **Learn from:** document-to-scaffold speed, rubric-based auto-feedback, "ask a small amount, return a useful draft fast" (the Dialer's builder-mode ethos).
- **Differentiate:** corporate-LMS oriented, cloud, no pedagogy-rubric audit, no data sovereignty, no Canvas package. Quality is generic.
- https://www.coursebox.ai/

**LearnWorlds AI Course Creator** — *build only, commercial SaaS*
AI woven through the whole platform: drafts outlines, lessons, quizzes, page copy; generates SMART objectives; Socratic dialogues; 200+ course-creation prompts.
- **Learn from:** the SMART-objective generation and the prompt-library approach. Their "generate objectives" step is exactly the Bloom's-verb + measurability logic the Dialer already does deterministically, with the last-mile rewrite being the only AI part.
- https://www.learnworlds.com/ai-course-creator/

**MagicSchool AI** — *build only, freemium, K-12/higher-ed*
80+ teacher tools: lesson-plan generator (objectives, materials, differentiation, assessment, standards-aligned), unit-plan designer (multi-week arcs, formative assessments, culminating projects), rubric maker, quiz builder, IEP generator.
- **Learn from:** the unit-plan designer's "arc with formative checkpoints and a culminating project" is a good template for builder-mode module sequencing. The standards-alignment input field is the pattern for tying a generated lesson to a competency.
- https://www.magicschool.ai/

**Khanmigo for Teachers (Khan Academy)** — *build + tutor, freemium*
20+ teacher tools: lesson hooks, exit tickets, class summaries, differentiated tasks, rubric generators, quiz questions; Socratic student tutor tied to Khan's content library.
- **Learn from:** lesson hooks map to Gagne's "gain attention" and Merrill's "activation"; exit tickets are retrieval practice and formative checks. These are concrete, sequence-aware building blocks the builder could offer per module.
- https://blog.khanacademy.org/webinar-recap-introducing-khan-academys-magical-ai-tool-for-teachers/

**Adjacent LMS AI (Docebo, D2L, Instructure, etc.)** — *build + author, enterprise*
Most major LMSs now ship AI authoring/summarization/quiz-generation. Broadly the same shape as above: cloud, enterprise, no independent quality audit, no data-sovereign posture.

### 1f. Landscape summary table

| Tool | Audit | Build | Both | Free / open | No account | Data-sovereign | Returns a course file |
|---|---|---|---|---|---|---|---|
| **Dial Your Course (target)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (Canvas `.imscc`) |
| Cidi Labs DesignPLUS | ✅ | ✅ (design) | partial | ✕ | ✕ | ✕ | ✕ |
| UDOIT | ✅ (a11y) | ✕ | ✕ | ✅ (core) | ✕ | ✕ | ✕ |
| Anthology Ally | ✅ (a11y) | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| YuJa Panorama | ✅ (a11y) | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| QM CRMS | ✅ (workflow) | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| OLC Course Review Scorecard | ✅ (rubric) | ✕ | ✕ | ✅ | ✅ | n/a | ✕ |
| Coursetune | ✕ | ✅ (mapping) | ✕ | ✕ | ✕ | ✕ | ✕ |
| Concourse / Simple Syllabus | ✅ (syllabus) | ✅ (syllabus) | partial | ✕ | ✕ | ✕ | ✕ |
| Coursebox / LearnWorlds AI | ✕ | ✅ | ✕ | freemium | ✕ | ✕ | ✕ |
| MagicSchool / Khanmigo | ✕ | ✅ | ✕ | freemium | ✕ | ✕ | ✕ |

**The empty column is the top row.** No competitor combines audit + build + free + no-account + data-sovereign + returns-a-file. That is the Dialer's defensible position.

---

## 2. Quality rubrics and standards beyond OSCQR / QM

The reference library already crosswalks OSCQR and QM. These extend that set. Each becomes a block of checkable recommendations the same way OSCQR standards do.

**OLC Course Review Scorecard (2025).** The most consequential: OLC intends it to replace OSCQR. 50 objectives, three tiers (Essential Design / Advanced Design / Course Delivery). **Recommendation:** author an `OLC_SCORECARD.md` crosswalk; the Essential/Advanced/Delivery split gives the Dialer a ready-made severity and "deterministic vs. human-review" partition. https://onlinelearningconsortium.org/quality/scorecards/course-review/

**Anthology/Blackboard Exemplary Course Program rubric.** 53 standards, 4 categories, weighted 1–5 with compulsory 5s. Its weighted model is a better severity scheme than OSCQR's flat scale, and its interaction/collaboration emphasis targets the Dialer's weakest area. https://www.niu.edu/blackboard/exemplary-course-program/rubric.shtml

**iNACOL / Aurora Institute — National Standards for Quality Online Courses / Teaching / Programs (now hosted at nsqol.org).** K-12 and blended, but the course-design and assessment standards translate cleanly and are widely used for dual-enrollment and early-college. Useful if the Dialer ever serves K-12 or CTE dual-credit courses. https://nsqol.org/the-standards/quality-online-courses/ · https://aurora-institute.org/resource/inacol-national-standards-for-quality-online-teaching-v2/

**WCAG 2.2 (W3C Recommendation, Oct 2023).** The current accessibility standard. Adds nine success criteria over 2.1 (focus appearance, dragging movements, target size minimum, consistent help, redundant entry, accessible authentication). **Note the regulatory gap:** the ADA rule (below) mandates 2.1 AA, but 2.2 is the current best practice. The Dialer's structural checks (alt text, headings, tables, contrast, link text) already satisfy the overlap; the 2.2 additions (target size, focus appearance) mostly concern live UI rather than exported content, so most are out of scope for a package auditor, but worth stating. https://www.w3.org/TR/WCAG22/

**ADA Title II web rule (DOJ final rule, April 2024) + Section 508.** Public colleges must conform to **WCAG 2.1 Level AA**. Compliance dates were extended in April 2026: entities serving 50,000+ people now must comply by **April 26, 2027**; smaller entities and special districts by **April 26, 2028**. The substantive obligation is already in force regardless of deadline. Maricopa (10 colleges, ~140K+ students) is well over the 50,000 threshold, so the 2027 date applies. **This is the compliance driver that gives the Dialer's accessibility findings legal weight**, exactly as HLC seat-hours pressure drives the workload findings. State it in the report. https://www.ada.gov/resources/2024-03-08-web-rule/ · https://www.federalregister.gov/documents/2026/04/20/2026-07663/ (deadline extension) · https://edtechmagazine.com/higher/article/2025/06/guide-ada-title-ii-accessibility-rule-perfcon

**How each becomes a checkable recommendation:** the pattern is already proven with OSCQR. For each standard, decide deterministic-checkable (fires with figures) vs. human-review (enumerated with the method), tag a severity (borrow ECP's compulsory-vs-optional weighting), and, where a fix is generable, route it through the grounded reference block. The OLC Scorecard crosswalk is the one to build first because it is replacing the rubric the tool currently maps to.

---

## 3. Assessment in the AI era (deeper than the existing file)

`ALTERNATE_ASSESSMENTS.md` already carries the two-lane model, the substitution menu, and Michelle's checklist. This adds the grading-structure and program-level scholarship the file does not, plus the newest 2025–2026 AI-resilience research.

### Grading structures the tool could recognize and suggest

**Specifications grading (Nilson, 2014).** Pass/Not-Yet/Fail against clearly defined specs, assignments bundled into letter-grade tiers. Pairs naturally with AI-resilience: specs can require process evidence as a pass condition ("submit with version history"). **Tool move:** detect all-points-weighted rubrics and offer a specs-style alternative where a graded item's spec includes a process-evidence requirement. https://idaltoona.psu.edu/2025/04/21/rethinking-grading-structures/

**Ungrading (Blum, 2020).** Minimize/eliminate marks; emphasize feedback and student self-evaluation. Directly serves UDL self-regulation and OSCQR 47 (self-assessment). **Tool move:** where a module has no self-assessment/reflection, offer an ungrading-style reflective self-evaluation as the UDL/engagement fix.

**Programmatic / program-level assessment.** The scholarship is explicit that fixing one assignment in isolation fails; AI-resilience is a program-coordination problem (already one of the five design principles in the reference file). **Tool move (bigger lift):** the "batch across many courses" idea is out of scope in `prd.html` for consent reasons, but a *single-course* program-alignment view (which competencies this course carries, where the program expects them to escalate on Bloom's) is in scope and ties to the Bloom's level-appropriateness check.

### The newest AI-resilient assessment scholarship (2025–2026)

**Interconnected-problems framework (2025).** Empirically validated finding: **modular** assessments inflate scores when GenAI is allowed, so high modular scores stop reflecting learning; **interconnected, semi-open-ended** designs resist AI without requiring full proctoring. This is a concrete, citable design pattern beyond "make it authentic." **Tool move:** flag assessments built as independent modular items and suggest interconnecting them (each part depends on the student's own prior part), a substitution that does not require secured/proctored delivery. https://arxiv.org/html/2512.10758

**Socio-technical / AI-vulnerability-exposure framework (2026).** Three-layer governance: assessment-design archetypes + an AI vulnerability-exposure rating. This is essentially a more formal version of the Dialer's existing AI-resistance banding (strong/adequate/exposed). **Tool move:** cite it as the scholarly backing for the exposure banding already in v1. https://aisel.aisnet.org/pacis2026/is_education/is_education/6/

**Constructive-alignment-under-AI framework (2025).** Argues AI shifts what "aligned" assessment means and offers a framework for realigning objectives, activities, and assessment when AI is in the loop. Grounds the builder's alignment logic. https://arxiv.org/pdf/2506.23815

**Process-over-product consensus (Northeastern CATLR, MIT Sloan, UMN).** All converge on the same rule already in the reference file: assess the decisions, iterations, and thinking, not the finished artifact. MIT Sloan's "4 steps to design an AI-resilient learning experience" and UMN's "GenAI-resilient assignments" are practical, citable checklists to fold into the menu. https://learning.northeastern.edu/ai-assessment/ · https://mitsloanedtech.mit.edu/ai/teach/4-steps-to-design-an-ai-resilient-learning-experience/ · https://teachingsupport.umn.edu/genai-resilient-assignments

### Concrete assessment patterns the tool could suggest (additions to the existing menu)

- **Interconnect modular items** so each part builds on the student's own previous output (2025 interconnected-problems evidence).
- **Specs-grade with a process gate** (a pass requires version history / commit log / draft trail).
- **Two-stage exam** (individual then group, or draft then defense) to move part of the grade onto a secured/live moment.
- **Ungrading reflective self-evaluation** as the self-regulation/UDL fix for modules with no self-check.
- **AI-disclosure appendix graded on delineation** (already in the file; reinforce with the UMN/Northeastern patterns).

---

## 4. Learning science that could power recommendations

This is the layer the reference library does not yet have. Each principle below implies a specific, checkable suggestion a course-checker could make. Most are deterministic-detectable from an export (presence/absence, spacing of items), which fits the Dialer's model. Candidate for a new `LEARNING_SCIENCE.md` reference file.

| Principle | What it says | What it implies for the Dialer's suggestions | Detectable from export? |
|---|---|---|---|
| **Retrieval practice** | Recalling from memory strengthens retention far more than re-reading. | Flag modules with content but no low-stakes retrieval check (quiz, brain-dump, exit ticket). Suggest adding one. Reframes low-stakes quizzes as pedagogy, not just points. | Yes (graded/ungraded item presence per module) |
| **Spaced practice** | Revisiting material across spaced sessions beats massing it. | Flag a competency assessed only once, in one module. Suggest a spaced re-encounter later in the term. Ties to the due-date distribution check already in v1. | Yes (where each objective is assessed across the schedule) |
| **Interleaving** | Mixing problem types beats blocking one type. | Flag purely blocked practice sets; suggest interleaving related problem types. Note: also an AI-resilience move (interconnected problems, §3). | Partial (item structure) |
| **Cognitive load theory (Sweller)** | Working memory is limited; manage intrinsic/extraneous/germane load. | Flag a module that front-loads many new elements with no scaffold; ties to the seat-hour "what this module costs" work and to worked examples. Flag extraneous load (cluttered pages, redundant media). | Partial |
| **Worked examples / faded guidance** | Novices learn more from studying worked examples than unguided problem-solving. | Flag a module that jumps to an open assignment with no worked example (also Merrill's "demonstration"). Suggest adding one, then fading it. | Partial |
| **UDL (CAST 3.0)** | Multiple means of engagement, representation, action & expression. | Already fully specified in `UDL_3.md`. | Yes (single-modality, single-format detection) |
| **Fink's Taxonomy of Significant Learning** | Six non-hierarchical dimensions: foundational knowledge, application, integration, human dimension, caring, learning how to learn. | A complement to Bloom's for the objectives lens: flag a course that only hits foundational knowledge + application and never integration, human dimension, or learning-how-to-learn. Good for capstones (AVC248). | Partial (objective analysis) |
| **Merrill's First Principles** | Problem-centered; Activation → Demonstration → Application → Integration. | Already in `ID_MODELS.md`. Learning-science backing for the "jumped to application with no demonstration" flag. | Partial |
| **Backward design (Wiggins & McTighe)** | Results → evidence → activities. | The Dialer's native logic; already in `ID_MODELS.md`. | Yes (alignment matrix) |
| **Constructive alignment (Biggs)** | Objectives, activities, and assessment must mutually align; students "construct" meaning through aligned activities. | The scholarly name for the alignment matrix. Cite Biggs and the 2025 constructive-alignment-under-AI paper (§3) as the backing. | Yes |

**Sources:** UMN CEI, Spaced and interleaved practice, https://cei.umn.edu/teaching-resources/leveraging-learning-sciences/spaced-and-interleaved-practice-improves-recall · Evidence Based Education, retrieval + spaced practice, https://evidencebased.education/resource/retrieval-and-spaced-practice-study-strategies-that-must-be-combined/ · Fink, Creating Significant Learning Experiences (Dee Fink & Associates), https://www.deefinkandassociates.com/ · Biggs, constructive alignment (see the 2025 arXiv framework, https://arxiv.org/pdf/2506.23815) · Sweller cognitive load (widely summarized; pair with the worked-examples effect).

**The framing that fits the Dialer:** learning science lets a finding say *why*, not just *what*. "This module has no retrieval check" lands harder as "spaced retrieval is one of the most replicated findings in learning science, and this module has no low-stakes recall opportunity." Deterministic detection, grounded recommendation, last-mile sentence only from the model. Same architecture as everything else.

---

## 5. AI in instructional design, current state 2025–2026

Where the field is, so the Dialer's build side is credible and its cautions are honest.

**What AI is being used for in ID right now.** Generating candidate learning objectives (reducing early-stage cognitive load), aligning activities to objectives, drafting content and quizzes, generating SMART objectives with Bloom's-verb reward engineering, and checking/improving objective measurability. The consensus efficacy finding: AI is strong at generating objectives and aligning activities, and weak on contextual feasibility (it proposes activities that do not fit the real constraints of the course). Human judgment plus AI beats either alone. https://www.umass.edu/ideas/digest/planning-precision-developing-learning-objectives-ai · https://elearningindustry.com/the-golden-triangle-of-instructional-design-learning-objectives-content-and-assessments

**Notable frameworks and directions (2025–2026).**
- **Multi-agent instructional design.** Multiple papers propose agent teams as "learning designers" applying learning-sciences rules, and "Instructional Agents" that reduce faculty workload through multi-agent course design. Relevant as a horizon, not a near-term fit for a static file, but validates the builder direction. https://arxiv.org/pdf/2508.16659 · https://arxiv.org/pdf/2508.19611
- **Teacher-AI co-design.** The literature is moving from "AI generates, human accepts" to genuine co-design with distributed agency, and critiques classic linear ID models (ADDIE) for assuming a single designer. Supports the Dialer's editable-draft-under-approval posture. https://www.nature.com/articles/s41599-026-06981-y
- **Co-creative AI + learning analytics.** Combining generation with analytics to close the design-evaluation loop (the ADDIE "E" the reference file flags as usually missing). https://edtechbooks.org/jaid_14_3/yqdqercqzk
- **Philippa Hardman's ID+AI work** is the widely-read practitioner voice on where this is going. https://drphilippahardman.substack.com/p/ai-in-instructional-design-reflections

**Cautions the Dialer should keep stating.**
- **Contextual feasibility is AI's weak spot** — it invents activities that do not fit real constraints (seat hours, tools available, class size). The Dialer's answer is already right: deterministic structure + grounded library, model writes only the last sentence.
- **Fabrication in a trust-critical tool** — the PRD's whole architecture (no generated findings, grounded suggestions only) is the correct response to the known hallucination risk. Keep it.
- **Generic output** — every AI course generator produces plausible-but-generic material. The Dialer's differentiator is that its suggestions are grounded in a curated library and anchored to *this* course's parsed structure, not generated from nothing.
- **Efficacy evidence is still thin.** Most 2025–2026 work is framework and case-study, not controlled efficacy studies. Do not overclaim that AI-designed courses learn better; claim time savings and consistency, which is what the evidence supports.

**Where this leaves builder mode:** the field validates the ask-for-objectives-and-a-topic, return-a-grounded-scaffold approach. The Dialer's edge over Coursebox/LearnWorlds/MagicSchool is not generation quality (they will win on polish) but *grounding* (real rubric, real seat-hour math, real Bloom's logic, real UDL/RSI), *data sovereignty*, and *round-tripping to a real Canvas package*.

---

## 6. Synthesized feature wishlist, "the best course builder + auditor ever"

Prioritized candidate features for v2 and beyond. Every one is tagged with its source idea and a feasibility note for a **static, browser-based, no-personal-API-key** tool (bridge/proxy model only). "Plug in soon" = deterministic or bridge-friendly, low lift. "Bigger lift" = needs the proxy, new parsing, or new reference authoring.

### Already specified in prd.html §7 (not re-listed as new)
Alternate-assessment menu, UDL recommendations, RSI writer, ID-model lens, builder mode, rolled-in syllabus checker, four-tab shell, multi-format export, grounded reference library. This wishlist is what to add ON TOP.

### PLUG IN SOON (deterministic or bridge-friendly, low lift)

| # | Feature | Source idea (§) | Side | Feasibility for a static tool |
|---|---|---|---|---|
| 1 | **OLC Course Review Scorecard crosswalk** (`OLC_SCORECARD.md`) — OSCQR is being replaced | §2 | Audit | Reference authoring + a crosswalk table. Deterministic. Do this first; the mapped rubric is sunsetting. |
| 2 | **ADA Title II / WCAG 2.1 AA compliance framing** on every accessibility finding, with the April 2027 date | §2 | Audit | Pure copy/logic. Adds legal weight to existing checks, like HLC does for seat hours. |
| 3 | **Retrieval-practice gap flag** — module with content but no low-stakes recall check | §4 | Audit | Deterministic (item presence per module). New reference block. |
| 4 | **Spaced-practice flag** — a competency assessed only once | §4 | Audit | Deterministic; extends the due-date + alignment checks. |
| 5 | **Interconnected-problems suggestion** for modular assessments (AI-resilience without proctoring) | §3 | Audit→redesign | Bridge-generable suggestion, grounded in the 2025 evidence. |
| 6 | **Specs-grading / process-gate suggestion** for all-points rubrics | §3 | Audit→redesign | Deterministic detection + grounded menu item. |
| 7 | **Severity weighting** borrowed from the ECP compulsory-1-to-5 model, replacing flat 3-2-1 | §2 | Audit | Pure logic. Makes the report triage-able. |
| 8 | **Simple Syllabus detection** to suppress false "missing course-info" findings | §1c, §5 | Audit | Deterministic; fixes a known false-negative in `prd.html` §11. |
| 9 | **Fink's Taxonomy complement** to the Bloom's objectives lens (flag capstones missing integration / learning-how-to-learn) | §4 | Both | Deterministic verb/dimension analysis + reference block. Good for AVC248. |
| 10 | **"Why" grounding on every finding** — attach the learning-science or standard rationale to each flag | §4 | Both | Reference authoring. Turns findings into teaching moments. |
| 11 | **Builder module-arc template** (hook → activation → demonstration → application → retrieval check → integration) drawn from Merrill/Gagne/Khanmigo/MagicSchool | §1e, §4 | Build | Deterministic scaffold; model fills prose via bridge. |
| 12 | **Alternative-formats routing note** — detect content types Panorama/Ally already handle and hand off rather than reimplement | §1a | Audit | Deterministic; extends the existing Panorama handoff. |

### BIGGER LIFT (needs the proxy, new parsing, or substantial authoring)

| # | Feature | Source idea (§) | Side | Why it's bigger |
|---|---|---|---|---|
| A | **Visual alignment map** (objective ↔ assessment ↔ activity), Coursetune-style, rendered in-browser | §1c | Both | New interactive rendering; depends on outcomes surviving export (`prd.html` §11 open problem). |
| B | **Single-course program-alignment view** — which competencies this course carries and where the program expects Bloom's to escalate | §3, §4 | Both | Needs program-outcome data Canvas does not export; blocked on the account-level Outcomes question in `prd.html` §11. |
| C | **Full builder-mode content drafting** (lesson prose, quiz items, rubrics) to match Coursebox/LearnWorlds polish | §1e, §5 | Build | Heavy generation; only viable through the institutional proxy at scale; must stay grounded to avoid generic output. |
| D | **Cognitive-load / extraneous-clutter analysis** of pages (redundant media, wall-of-text, too many new elements at once) | §4 | Audit | Requires heuristics on page structure that are hard to make non-arbitrary; false-positive risk. |
| E | **Worked-example detection** (does a module model the task before assigning it) | §4 | Audit | Semantic, not structural; needs the model to judge, so bridge/proxy + careful grounding. |
| F | **Two-stage / secured-moment assessment redesign generator** | §3 | Audit→redesign | Generation-heavy; sits in the same proxy tier as the alternate-assessment writer. |
| G | **Multi-rubric mode** — audit against OSCQR *or* OLC Scorecard *or* QM *or* ECP by toggle | §2 | Audit | Needs all crosswalks authored and a mapping engine; valuable but a lot of reference work. |
| H | **Cross-LMS export** (Common Cartridge to non-Canvas targets) | §1e | Build | New serialization targets; out of the current Canvas-only scope. |

### The prioritization logic

The cheap, high-value moves are the **standards refresh** (OLC Scorecard crosswalk #1, ADA framing #2, severity weighting #7) and the **learning-science layer** (#3, #4, #10), because they are deterministic, they deepen the audit's credibility, and they need no model at run time. The **build side's** near-term win is the grounded module-arc template (#11), which beats the generic AI generators on grounding without needing polish. Everything gated on the Outcomes-export problem (A, B) stays parked behind the two cheap tests already queued in `prd.html` §11. The generation-heavy items (C, E, F) all wait for the institutional proxy and pilot evidence, exactly as the PRD already sequences the generative layer.

---

## Appendix: full source list

**Accessibility / design tools:** Cidi Labs https://cidilabs.com/ , https://cidilabs.com/accessibility/ ; UDOIT https://cidilabs.com/landing/udoit/ , https://cdl.ucf.edu/teach/accessibility/udoit/ ; Anthology Ally https://ally.ac/ , https://help.anthology.com/ally-lms/en/about-ally-and-accessibility.html ; YuJa Panorama https://www.yuja.com/panorama/canvas-lms-accessibility-solution/

**Rubrics / standards:** QM CRMS https://www.qualitymatters.org/qm-membership/faqs/course-review-management-system ; QM Higher Ed Rubric https://www.qualitymatters.org/qa-resources/rubric-standards/higher-ed-rubric ; OLC Course Review Scorecard https://onlinelearningconsortium.org/quality/scorecards/course-review/ , https://onlinelearningconsortium.org/olc-insights/2025/03/new-course-review-scorecard/ ; Anthology ECP rubric https://www.niu.edu/blackboard/exemplary-course-program/rubric.shtml , https://www.anthology.com/blackboard-exemplary-course-program ; iNACOL/Aurora / NSQOL https://nsqol.org/the-standards/quality-online-courses/ , https://aurora-institute.org/resource/inacol-national-standards-for-quality-online-teaching-v2/ ; WCAG 2.2 https://www.w3.org/TR/WCAG22/ ; ADA Title II web rule https://www.ada.gov/resources/2024-03-08-web-rule/ , deadline extension https://www.federalregister.gov/documents/2026/04/20/2026-07663/ , guide https://edtechmagazine.com/higher/article/2025/06/guide-ada-title-ii-accessibility-rule-perfcon

**Curriculum / syllabus tools:** Coursetune https://app.coursetune.com/ , acquisition https://www.prnewswire.com/news-releases/academic-partnerships-acquires-coursetune-inc-a-leading-edtech-provider-of-curriculum-mapping-software-for-higher-education-301360670.html ; Concourse https://www.intellidemia.com/ ; Simple Syllabus https://simplesyllabus.com/canvas-syllabus/ ; Canvas Outcomes / Mastery https://teaching.pitt.edu/resources/track-student-progress-with-outcomes-and-the-learning-mastery-gradebook/

**AI course generators:** Coursebox https://www.coursebox.ai/ ; LearnWorlds https://www.learnworlds.com/ai-course-creator/ ; MagicSchool https://www.magicschool.ai/ ; Khanmigo https://blog.khanacademy.org/webinar-recap-introducing-khan-academys-magical-ai-tool-for-teachers/

**Assessment scholarship:** specs/ungrading overview https://idaltoona.psu.edu/2025/04/21/rethinking-grading-structures/ ; interconnected-problems framework https://arxiv.org/html/2512.10758 ; socio-technical AI-resilient assessment https://aisel.aisnet.org/pacis2026/is_education/is_education/6/ ; constructive alignment under AI https://arxiv.org/pdf/2506.23815 ; Northeastern CATLR https://learning.northeastern.edu/ai-assessment/ ; MIT Sloan https://mitsloanedtech.mit.edu/ai/teach/4-steps-to-design-an-ai-resilient-learning-experience/ ; UMN GenAI-resilient assignments https://teachingsupport.umn.edu/genai-resilient-assignments

**Learning science:** UMN CEI spaced/interleaved https://cei.umn.edu/teaching-resources/leveraging-learning-sciences/spaced-and-interleaved-practice-improves-recall ; Evidence Based Education https://evidencebased.education/resource/retrieval-and-spaced-practice-study-strategies-that-must-be-combined/ ; Fink https://www.deefinkandassociates.com/

**AI in instructional design:** learning-objective design with AI https://www.umass.edu/ideas/digest/planning-precision-developing-learning-objectives-ai ; golden triangle https://elearningindustry.com/the-golden-triangle-of-instructional-design-learning-objectives-content-and-assessments ; multi-agent learning designers https://arxiv.org/pdf/2508.16659 ; instructional agents https://arxiv.org/pdf/2508.19611 ; teacher-AI co-design https://www.nature.com/articles/s41599-026-06981-y ; co-creative AI + analytics https://edtechbooks.org/jaid_14_3/yqdqercqzk ; Hardman https://drphilippahardman.substack.com/p/ai-in-instructional-design-reflections
