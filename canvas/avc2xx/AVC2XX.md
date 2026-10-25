# AVC2xx UX Design for Interactive Media

One markdown for this course. Source competencies and the build live here.

**Status (25 Oct 2026): OSCQR revision built, not yet reviewed by Michelle.** `course.html` is now the source of truth for modules, objectives, points and seat time; where sections 3, 5, 6 and 10 below disagree with it, `course.html` wins. Canvas import file: `AVC2XX_Fall2027_DRAFT.imscc` (16 modules, everything unpublished, Fall 2027 dates). Backup of the pre-revision folder: `drafts/avc2xx-before-oscqr/`. Build scripts (not served): `drafts/avc2xx-build-scripts/` (`python3 page.py` writes `course.html`, `python3 cc.py` writes the `.imscc`).

What this revision did:
- 16 modules, Module 0 to Module 15, met in order. Week 1 holds Module 0 (one Thursday deadline) and opens Module 1, the AI Primer, due Thursday of Week 2. The Revision module was folded into Modules 13 and 14 (reviewer Option A). Old Module 16 is now Module 15.
- Seat time 120 hours: M0 4, M1 6, M2 4, M3 7, M4 8, M5 8.5, M6 8, M7 8.5, M8 9, M9 8, M10 8.5, M11 8, M12 8, M13 8.5, M14 8, M15 8. The reviewer’s 12 cuts applied; the five Build and AI-Use Logs retired (the Process Work rubric’s process-evidence criterion now covers “what broke and hours spent” from Module 10 on).
- Graded items: Process Work 27 × 10 = 270 (40%); Projects 2 × 30 = 60 (35%); Exercises, Quizzes and Reflections 5 items = 30 (25%). Every item shows its rubric with each criterion tagged to its objective, and a “This assignment measures…” line.
- Start Here and Syllabus written (schedule, competencies with Bloom’s levels, alignment map, technology requirements with the OIT request form, grading, AI in This Course, Access in This Course, research ethics with the under-18 supervised path and consent script, college policies, Your Instructor, help resources). Instructor notes moved to a separate “For instructors” section at the end of the page, with an Instructor build list.
- Bloom’s and AI-exposure audit applied: objective 1.4 rewritten (Justify, Evaluate) and 1.1 and 1.4 graded in AI Primer part 3; 2.1 measured by the Experience Teardown; one fact-check in the AI Primer is a narrated recording; Comparative Critique requires a capture from the student’s own session per priority change; Final Reflection is a recording by default.
- Discord: the Digital Media Arts server invite from AVC183 and AVC248 (`discord.gg/fyzAXNS4yF`); students find the course channel in the welcome announcement.
- 25 Oct 2026: AI Primer replaced with the program-wide version in canvas/AI_PRIMER_STANDARD.md. Canvas package not yet rebuilt.
- 25 Oct 2026: STEAMworks deliverable options added inside existing assignments, same rubric, online and non-visual paths, no added hours: laser-cut cardboard prototype (Week 7 concept), NFC tap interaction (Week 11 Prototype 1), AR prototype (Week 12 Prototype 2), VR usability test in the XR lab (Week 13 Test Round 2), plus a Technology/Equipment paragraph and a Week 7 instructor note. Edited in course.html (build:main) and in the build scripts (d2.py, d3.py, syl.py); package rebuilt. Note: course.html numbers these Modules 6, 10, 11, 12, the package still numbers them 7, 11, 12, 13 (pre-existing drift), so the new text refers to weeks. Backup: drafts/avc2xx-before-steamworks/.

# AVC2xx UX Design for Interactive Media · source material for the build

## A. REVISED competencies (team-revised at the curriculum meeting; Google Doc "3-Course Competency Work"). THIS IS AUTHORITATIVE.

Course: AVC2xx · UX Design for Interactive Media
Lec + Lab · 3.0 Credits · 6.0 Periods · 6.0 Load · Occupational · Load Formula T
IC(s): Art, VGP (video game production)

Description: Principles and methods of user experience design applied to interactive media across disciplines. Includes usability, accessibility, user research, prototyping, and user testing. Investigation of emerging technologies and interaction methods, including technology-assisted development and augmented, virtual, and spatial interfaces. Culminates in an original, interactive project in the student's discipline.

Prerequisites: A grade of C or better in AVC183, AVC184, AVC190, AVC200, CIS151, or MUC122, or permission of Instructor.
(MUC122 is a music/audio course, which is how sound design students enter.)

MCCCD Official Course Competencies (proposed)
1. Analyze interactive experiences using foundational UX principles. (I)
2. Create a project brief based on user research. (II)
3. Evaluate various technologies and interaction methods to meet user needs. (IV)
4. Develop a design concept using a pre-production process. (III)
5. Design a prototype of an interactive experience. (III, V)
6. Synthesize user testing and peer feedback into design iterations. (V, VI)
7. Create an original, functional interactive project that integrates user research, testing and an emerging technology or interaction method. (V, VI)

Outline
I. UX Principles and Critique: A. UX compared with visual design; B. Human-centered design; C. Usability heuristics; D. Cognitive load and principles of perception; E. Accessibility and inclusive design; F. Critique of interactive experiences in the student's discipline
II. User Research and the Project Brief: A. Research methods: interviews, surveys, observation; B. Synthesis: affinity mapping, personas, problem statements; C. Research ethics and consent; D. Project brief: goals, audience, method, timeline
III. Structure and Flow: A. User flows and task analysis; B. Information architecture; C. Low-fidelity iteration: sketches, storyboards, wireframes, paper prototypes
IV. Emerging Technologies and Interaction Methods: A. Design and development; B. Evaluation for accuracy, accessibility and bias; C. Augmented, virtual and mixed reality; D. Spatial, voice, and gesture interfaces; E. Ethics of emerging technology: privacy, manipulative patterns, inclusion; F. Matching a technology or method to user needs
V. User Testing and Critique: A. Planning and running usability tests; B. Heuristic and accessibility review; C. Peer critique; D. Prioritizing and implementing revisions
VI. Capstone Project: A. Proposal and project brief; B. Prototyping at increasing fidelity; C. Functional build; D. Testing and revision; E. Presentation and defense to peers; F. Recorded presentation for portfolio and interviews

Open questions the team listed: how programs outside AVC offer it (elective, cross-list, requirement); whether competency on technologies is met by analysis alone with the capstone being where every student builds; whether students who completed AVC190 need a different on-ramp in weeks 1 to 3.

## B. Michelle's INITIAL draft (meeting draft, superseded where it conflicts with A; use for detail only)
Disciplines table (initial draft had five; the course must ALSO serve sound design and AR/VR):
- Game design: analyze menus, HUDs, onboarding, controls; structure via paper prototypes, greyboxing, level sketches; capstone ideas: playable prototype of one mechanic tested with classmates; a VR or controller-free interaction
- Digital media arts: interactive media, installations, kiosks, interactive video; wireframes, user flows, storyboards; capstone: AR guide for a museum or campus space; interactive installation that responds to visitors
- Animation: interactive stories, motion in interfaces, viewer experience; storyboards, animatics; capstone: interactive or branching animated story; AR character placed in physical space
- Graphic design: brand experiences across print, screen, environment; thumbnails, sketches, rough comps; capstone: AR activation on packaging or poster; brand experience from print to screen to space
- App design: mobile and tablet apps, onboarding, task flows; wireframes, user flows, paper prototypes; capstone: functional app built with AI-assisted development for a community need; app with voice or AI-agent interface
Pacing in the initial draft: weeks 1 to 3 UX principles; week 4 research and brief; week 5 structure and flow; weeks 6 to 7 emerging tech; week 8 testing and critique, capstone proposal due; weeks 9 to 16 capstone. (Course is 15 weeks; adjust.)
Backward design (Wiggins and McTighe). Relationship to AVC190: AVC190 (Intro to Web Design and UX) teaches UX through websites; AVC2xx does not teach web building; AVC190 students find weeks 1 to 3 a review applied to their own discipline.
References used: CCS CDS-365 XR Design; CIID Interaction Design Programme; Northwestern Vibe Coding course; AHO Interaction Design 1; PNCA BFA Interaction Design; Politecnico di Milano Interaction Design; SCAD BFA UX; Anderson and Krathwohl 2001; Brennan 2026 Harvard Gazette vibe coding; UNESCO 2024 AI competency framework; Wiggins and McTighe 2005.

## C. Michelle's decisions and teaching conventions
- Shared across Maricopa colleges and disciplines; list DISCIPLINES, never college names, in anything shared: game design, digital media arts, animation, graphic design, app design, sound design. AR/VR is a technology option open to every discipline.
- Competencies are about abilities, not technology; stay vague and cross-disciplinary so any program's faculty can teach it with their own tools.
- Students do not all arrive with UX fundamentals: first half of the course = learn UX fundamentals through short exercises applied to their own discipline; second half = ONE big forward-thinking capstone in the student's own discipline.
- Students present the capstone to the class (not a professional audience) and record the presentation for portfolio and job interviews.
- Goal of prerequisites: no first-semester students.
- 15 weeks, fully online asynchronous Canvas course (GCC online). 3 credits, 6 load hours: seat time = 40 hours direct + 80 hours outside = 120 hours total; keep honest per-week hour estimates for a student new to the tool.
- Deadline rhythm, all at noon Arizona time: Saturday noon post to Discord for critique, Sunday noon deadline (work plus three critique comments on classmates), Monday noon hard close; Wednesday noon post, Thursday noon deadline, Friday noon hard close. The 24-hour late window costs 10%; nothing accepted after the hard close. Week 1 has a single Thursday deadline. Three critique comments required; commenting on late posts during the window is ungraded "good karma" community citizenship. Discord approved; screen names allowed.
- No work due on holidays or breaks. Do not put calendar dates in; use Week numbers (no term picked yet).
- Grading: all process steps go in ONE "Process Work" category, usually 10 points each; the capstone final is 30 points in "Projects". Exercises/quizzes/reflections category exists too. Weighted groups.
- Tools: the district pays for Google Gemini (students get it January 2027; Gems retire for education in June 2027, so use Gemini Notebook and Gemini Canvas, not Gems) and Adobe Creative Cloud (online students have it at home). Capitalize on Gemini and Adobe first, but do not limit: Figma (free education), Unity/Unreal for game students, Blender, Adobe Aero is DISCONTINUED (do not use), MindAR / model-viewer for WebAR, Reality Composer, Audition / Reaper / Audacity for sound, After Effects, Premiere, vibe coding with Gemini Canvas or similar for functional prototypes. Firefly availability unconfirmed: treat as optional.
- Canvas page format: student-facing text is formal; each page opens with a title box in GCC red #CB3338 with white text (the box is the title), then an Objectives heading and list, then the overview/instructions.
- Every resource referenced must be a real working link; mark anything unverified [verify] and anything that does not exist yet [instructor to create].
- Writing: no em dashes anywhere; curly quotes and apostrophes; avoid the words "genuinely" and "straightforward".
- Quality frameworks she uses: backward design, Bloom's (revised), OSCQR, Regular and Substantive Interaction, UDL, WCAG 2.1 AA, authentic assessment (grade what the student authors and defends).


---

# AVC2xx UX Design for Interactive Media · Course Design V1

Lec + Lab · 3.0 credits · 6.0 periods · 6.0 load · Fully online, asynchronous (Canvas) · 15 weeks
Prerequisites (proposed): a grade of C or better in AVC183, AVC184, AVC190, AVC200, CIS151, or MUC122, or permission of instructor.

First draft for Michelle and the curriculum team. Competencies and outline follow the team-revised version (section A of the source). Built to the course build standard: noon deadline rhythm, title box, fixed module order, competency callouts, weighted grading groups. This is the public build, so title boxes are purple (#7a5080, white text); they change to GCC red (#CB3338) only at GCC export. Links were checked with web tools on the build date; anything that could not be confirmed is marked [verify], and anything that does not exist yet is marked [instructor to create].

---

## 1. Course design summary

### Design concept

The course teaches user experience design as a set of abilities, not a set of tools. Students arrive from multiple disciplines, for example game design, animation, sound design, graphic design, app design, digital media arts, and others. Each of those disciplines already makes interactive work; few of them teach students to design it around the people who will use it. AVC2xx gives every student the same UX method and asks each one to practice it in their own medium.

The course has two halves.

- **Weeks 1 to 7, UX fundamentals in your own medium.** Short, scaffolded exercises that cover outline sections I to V. Each exercise is one step of a small “Studio Project”: analyze experiences, research real users, write a brief, map a flow, build a low-fidelity concept, evaluate emerging technologies, then test and revise. The half closes with the Studio Project (Projects, 30 points), which is the first complete pass through the UX cycle and the rehearsal for the capstone. Evidence for Course Competencies 1 to 4, with practice toward 5 and 6.
- **Weeks 8 to 15, one capstone in the student’s own discipline.** An original, functional, interactive project that integrates user research, two rounds of testing, and an emerging technology or interaction method (outline section VI). Students present to the class, answer classmates’ questions in a recorded defense, and keep the recording for their portfolio and job interviews. Evidence for Course Competency 7, with 5 and 6 inside it.

Backward design (Wiggins and McTighe) drove the order: the capstone final and its defense were written first, then every earlier step was placed where it builds a skill the capstone needs.

### How the cross-disciplinary model works

1. **One method, many media.** Every assignment states the UX task in medium-neutral terms, then gives a “What you produce in your discipline” table with examples for game design, animation, sound design, graphic design, app design and digital media arts. Students in other programs choose the closest row and confirm with the instructor. Faculty in any program can teach the course with their own tools, because the competencies and rubrics grade the thinking, not the software.
2. **Sound design is a full discipline in every step.** Sound students analyze audio experiences, interview listeners and players, map adaptive-audio state diagrams and sound maps, prototype in FMOD, Wwise, Unity, Unreal MetaSounds or the Web Audio API, and run listening tests. A heuristics-to-audio translation table (Week 2) and an audio testing protocol (Week 10) remove the “there is no screen” problem.
3. **Emerging technology is open to everyone.** AR, VR, spatial, voice, gesture and AI-assisted development are interaction options, not a separate track. A graphic design student can build an image-tracked AR poster; a sound student can build a location-based sonic AR walk; an app student can build a voice-first or agent-assisted app.
4. **Mixed critique groups.** Discord critique channels mix disciplines on purpose. A game student reviewing an animation student’s branching story sees UX from a new angle, and the critique protocol (section 6) gives everyone a shared vocabulary.
5. **Shared rhythm.** Every week runs on the same two noon deadlines, so students learn the pattern once.

### How students use AI, and where they may not

The district provides Google Gemini (student access expected January 2027) and Adobe Creative Cloud; the course uses both first. AI use is permitted and taught as a design material and a production aid. It is never a substitute for the student’s own research, judgment, or voice.

| Students may use AI to | Students may not use AI to |
|---|---|
| Generate functional prototype code from their own designs (“vibe coding”) in Gemini Canvas or similar | Replace real participants with simulated users, or invent research data, quotes, or test results |
| Brainstorm variations after they have sketched their own first ideas | Write their critique comments on classmates’ work |
| Draft a test script or survey that they then revise and justify | Perform the affinity sort or write the problem statement before the student has done a first version by hand |
| Check accessibility (contrast, captions, reading level) and suggest fixes | Write reflections, design rationales, or defense answers |
| Produce disclosed placeholder assets (images, sounds, voice) for prototypes | Process identifiable participant data in any tool that is not district-approved |
| Critique a student-written draft, with the student recording what they accepted and rejected | Present AI-generated work as hand-made, or omit it from the AI-use log |

Every submission carries a short AI-use log (tool, purpose, what was kept, what was changed). Week 7 also asks students to evaluate AI-driven interaction methods for accuracy, accessibility, and bias, so AI is studied as well as used. Full rules are in section 11.

### Relationship to AVC190

AVC190 (Introduction to Web Design and UX) teaches UX through websites. AVC2xx does not teach web building. It assumes no web skills, applies UX to the student’s own medium, and adds research, emerging technology, and a capstone. Web technology may appear only as a delivery vehicle (for example WebAR with model-viewer, or a browser-based audio prototype).

Students who completed AVC190 will find Weeks 1 to 3 partly familiar. They follow the **extension path** in those weeks: the same assignments, applied to a non-web experience (a game, an installation, an XR app, a voice interface, an audio UI), with one extra heuristic set from their discipline (for example the Game Accessibility Guidelines or the Xbox Accessibility Guidelines). This keeps one gradebook and one rubric while respecting prior learning. The team should decide whether this is enough (see section 12).

### How this draft was reviewed

The first draft was critiqued from five seats. The findings and the fixes made are below.

| Seat | Main findings | Fixes made in this version |
|---|---|---|
| UX faculty member from industry | Research happened only once, so capstones would rest on borrowed data. Tests were opinion surveys, not task-based. No severity ratings. | Capstone brief requires a research addendum (at least two new sessions). Every test plan requires tasks, success criteria, and a severity scale. Prioritization matrix added in Week 13. |
| Game design faculty member | Usability testing is not playtesting. Unity or Unreal setup can take a full evening and would derail Week 9. “Functional” was undefined for games. | Playtest guidance added beside usability testing. Tool Setup Check moved to Week 1 Practice. Functional defined as a playable vertical slice of one core loop (section 8). |
| Sound design and audio faculty member | Sound read as “add audio to someone else’s project.” Remote tests over video calls destroy audio quality. No audio accessibility. | Sound rows in every translation table with concrete artifacts (audio flowchart, sound map, adaptive-audio state diagram, earcon set). Audio testing protocol (headphones, local playback, loudness check). Audio accessibility (captions for sound cues, visual alternatives, mono option, separate volume controls) added to Week 3 and the capstone rubric. |
| Instructional designer (alignment, seat time, RSI) | Week 7 ran past 11 hours. Two objectives were above their competency’s Bloom level. Instructor-initiated interaction was implied, not scheduled. | Midpoint reflection folded into the Studio Project. Objective verbs checked against Bloom levels. RSI plan schedules weekly instructor contacts and three capstone check-ins (section 4). |
| Synthetic second-year sound design student (Reaper user, no Figma, never coded) | “What is a heuristic evaluation of a game mix?” “Who are my users?” “Do I have to code to pass the capstone?” | Heuristics-to-audio table in Week 2. User examples for sound (players, listeners, blind and low-vision users of audio UI). Capstone does not require coding: FMOD or Wwise inside an instructor-provided Unity starter project [instructor to create], or a Gemini Canvas Web Audio prototype from the student’s own sound design, both count as functional. |

---

## 2. Competency alignment

Bloom’s levels follow the revised taxonomy (Anderson and Krathwohl, 2001). Every module objective uses a verb at or below its competency’s level.

| # | Official course competency | Bloom’s level | Outline | Evidence (assessed) | Weeks |
|---|---|---|---|---|---|
| 1 | Analyze interactive experiences using foundational UX principles. | Analyze | I | Experience Teardown, Heuristic Evaluation, Perception and Cognitive Load Redline, Accessibility and Inclusion Audit, Comparative Critique, Peer Heuristic and Accessibility Review, Capstone Final criterion 1 | 1 to 3, 11, 15 |
| 2 | Create a project brief based on user research. | Create | II | Research Plan and Consent Materials, Research Sessions and Field Notes, Research Synthesis, Studio Project Brief, Capstone Proposal, Capstone Brief and Research Addendum, Studio Project, Capstone Final criterion 2 | 4, 5, 7, 8, 15 |
| 3 | Evaluate various technologies and interaction methods to meet user needs. | Evaluate | IV | Technology and Interaction Method Evaluation, Capstone Design Concept (technology justification), Capstone Final criterion 3 | 7, 9, 15 |
| 4 | Develop a design concept using a pre-production process. | Create | III | Task Analysis and Flow, Design Concept and Low-Fidelity Prototype, Studio Project, Capstone Design Concept, Pre-Production Package, Capstone Final criterion 4 | 6, 7, 9, 15 |
| 5 | Design a prototype of an interactive experience. | Create | III, V | Practice: Design Concept and Low-Fidelity Prototype (Week 6). Assessed: Prototype 1, Prototype 2, Capstone Final criterion 5 | 6, 10, 11, 15 |
| 6 | Synthesize user testing and peer feedback into design iterations. | Create | V, VI | Practice: Studio Project test and revision (Week 7). Assessed: Test Round 1, Test Round 2, Synthesis and Revision Plan, Beta Build and Change Log, Capstone Final criterion 6 | 7, 10, 12, 13, 15 |
| 7 | Create an original, functional interactive project that integrates user research, testing and an emerging technology or interaction method. | Create | V, VI | Functional Build: Alpha, Presentation Rehearsal, Release Candidate and Process Book, Capstone Presentation to the Class, Capstone Final criterion 7 | 12, 14, 15 |

**Orphan check.** Every competency has assessed evidence in at least two weeks, and the Capstone Final has one rubric criterion per competency. Every assignment in section 6 maps to a module objective, and every module objective maps to one competency.

---

## 3. Fifteen-week map

PW = Process Work (10 points each). P = Projects (30 points). E = Exercises, Quizzes and Reflections (5 or 10 points). Thu = Thursday deadline (Discord post Wednesday noon). Sun = Sunday deadline (Discord post Saturday noon).

| Week | Theme | Outline | Deliverables (points) | Hours |
|---|---|---|---|---|
| 1 | What UX is in your discipline | I.A, I.B | Thu: E1 Start Here Acknowledgement (10); E2 Tool Setup Check (5); PW1 Experience Teardown (10) | 7.5 |
| 2 | Heuristics, perception and cognitive load | I.C, I.D | Thu: PW2 Heuristic Evaluation (10); E3 Heuristics in Your Medium (5). Sun: PW3 Perception and Cognitive Load Redline (10) | 8 |
| 3 | Accessibility, inclusion and critique | I.E, I.F | Thu: PW4 Accessibility and Inclusion Audit (10); E4 Constraint Walkthrough (5). Sun: PW5 Comparative Critique and Studio Problem Area (10) | 8 |
| 4 | User research methods and ethics | II.A, II.C | Thu: E5 Research Ethics Check (5); PW6 Research Plan and Consent Materials (10). Sun: PW7 Research Sessions and Field Notes (10) | 8.5 |
| 5 | Synthesis and the project brief | II.B, II.D | Thu: PW8 Research Synthesis (10); E6 AI Critique of a Problem Statement (5). Sun: PW9 Studio Project Brief (10) | 8 |
| 6 | Structure, flow and low-fidelity iteration | III.A to III.C | Thu: PW10 Task Analysis and Flow (10); E7 Flow Notation Practice (5). Sun: PW11 Design Concept and Low-Fidelity Prototype (10) | 8 |
| 7 | Emerging technologies; test and iterate | IV.A to IV.F; V.A to V.D | Thu: E8 Emerging Technology Tryout (5); PW12 Technology and Interaction Method Evaluation (10). Sun: P1 Studio Project (30) | 9 |
| 8 | Capstone launch: proposal and brief | VI.A; II.D | Thu: PW13 Capstone Proposal (10). Sun: E9 Scope Self-Check (5); PW14 Capstone Brief and Research Addendum (10) | 7.5 |
| 9 | Concept and pre-production | VI.A; III | Thu: PW15 Capstone Design Concept (10). Sun: PW16 Pre-Production Package (10); E10 Build and AI-Use Log 1 (5) | 8 |
| 10 | Prototype at low fidelity; Test Round 1 | VI.B, VI.D; V.A | Thu: PW17 Prototype 1 (10). Sun: PW18 Test Round 1 (10); E11 Build and AI-Use Log 2 (5) | 8 |
| 11 | Prototype at mid fidelity; peer review | VI.B; V.B, V.C | Thu: PW19 Prototype 2 with Technology Spike (10). Sun: PW20 Peer Heuristic and Accessibility Review (10); E12 Build and AI-Use Log 3 (5) | 8 |
| 12 | Functional build; Test Round 2 | VI.C, VI.D | Thu: PW21 Functional Build: Alpha (10). Sun: PW22 Test Round 2 (10); E13 Build and AI-Use Log 4 (5) | 8.5 |
| 13 | Revision | VI.D; V.D | Thu: PW23 Synthesis and Revision Plan (10). Sun: PW24 Beta Build and Change Log (10); E14 Build and AI-Use Log 5 (5) | 8 |
| 14 | Presentation and portfolio | VI.E, VI.F | Thu: PW25 Presentation Rehearsal (10); E15 Caption and Accessibility Check (5). Sun: PW26 Release Candidate and Process Book (10) | 8 |
| 15 | Presentation and defense | VI.E, VI.F | Thu: PW27 Capstone Presentation to the Class (10). Sun: P2 Capstone Final and Defense (30); E16 Final Reflection (10) | 7 |
| | **Totals** | | **PW 270 · P 60 · E 90** | **120** |

---

## 4. Deadline rhythm, calendar conventions, feedback and interaction

### Deadline rhythm

All times are **noon, Arizona time** (Arizona does not observe daylight saving time, so the time never shifts). Every deadline has three moments.

| Moment | Thursday deadline | Sunday deadline |
|---|---|---|
| Post the work to the Discord critique channel | Wednesday, 12:00 p.m. | Saturday, 12:00 p.m. |
| Deadline: submit to Canvas (work, process evidence, AI-use log, and three critique comments on classmates) | Thursday, 12:00 p.m. | Sunday, 12:00 p.m. |
| Hard close: work in the 24-hour window loses 10%; nothing is accepted after | Friday, 12:00 p.m. | Monday, 12:00 p.m. |

- Week 1 has one deadline (Thursday).
- Exercises (E items) are due at the same noon deadline as the week’s Process Work and follow the same late window, but they are not posted to Discord unless the page says so.
- Students are encouraged to comment on classmates who post late during the 24-hour window. This is ungraded “good karma” community citizenship and is never extra credit.
- Discord is the critique space. Screen names are allowed; students tell the instructor their screen name in the Start Here acknowledgement so critique can be credited.
- Every assignment page states all three times in a date box with a purple border (red at GCC export).

### Calendar conventions

- The course uses **week numbers only**. No calendar dates appear in this design or on Canvas pages until a term is chosen.
- Weeks are instructional weeks. A break week (for example spring break) is not numbered; the schedule resumes with the next week number after the break.
- Nothing is due on a holiday or during a break. If a noon deadline, Discord post time, or hard close falls on a college holiday, all three moments for that deadline shift one day later, and the shift is announced in Canvas at least one week ahead. Students are never asked to work through a closure.
- A week that loses a weekday to a holiday keeps its two deadlines but carries the lighter of its two Process Work steps; the instructor checks this when the term is set.

### Feedback turnaround

| Item | Instructor feedback returned |
|---|---|
| Process Work (Thursday items) | By the following Tuesday at noon |
| Process Work (Sunday items) | By the following Friday at noon |
| Capstone Proposal (Week 8, Thursday) | Within 48 hours (by Saturday noon), so the brief can use it |
| Test plans inside Test Round 1 and 2 | Within 48 hours when a student requests early review before testing |
| Studio Project and Capstone Final | Within seven days, with rubric scores and a recorded or written comment |
| Discord questions and Canvas inbox | Within one business day |

### Regular and Substantive Interaction plan

The instructor initiates interaction on a predictable schedule; it is not left to students to ask.

| Interaction | Frequency | Substantive because |
|---|---|---|
| Weekly announcement (text plus short video) | Every week, Monday afternoon | Previews the week, names common patterns from the last critique round, links examples from student work |
| Module introduction video [instructor to create] | Every week | Direct instruction and a worked example in at least two disciplines |
| Individual feedback on every Process Work and Project submission | Every deadline | Rubric scores plus at least one specific, actionable comment tied to the objective |
| Instructor comments in Discord critique | Every deadline, rotating so each student receives an instructor critique comment at least every other week | Models the critique protocol and corrects misconceptions in public |
| Capstone check-ins (asynchronous video reply, or an optional live call) | Weeks 8, 11 and 13 | Scope, risk, and test-plan coaching at the three points where capstones most often fail |
| Office hours (live, recorded and posted) | Weekly, at two different times of day | Open questions; recordings serve students who cannot attend |
| Outreach to students who miss a hard close | Within two days of the close | Personal message with options to get back on rhythm |

---

## 5. Seat-time reconciliation

Credit-hour standard: 3 credits × 40 hours = 120 hours, about 40 direct and 80 outside. In this asynchronous course, **direct hours** are instructor-designed instructional activity: module pages and readings, instructor and open videos, guided practice exercises, the Discord critique exchange, and reviewing instructor feedback. **Outside hours** are the student’s independent production: research sessions, assignments, builds, testing, and recording.

Estimates assume a second-year student who is new to the tool named in the assignment. Students who already know their engine or audio middleware will often finish faster; students who choose an unfamiliar technology for the capstone should expect the build weeks to run one to two hours over, which is why the capstone scope guardrails exist (section 8).

| Week | Direct: read and watch | Direct: practice exercise | Direct: critique and feedback | Direct total | Outside: assignments and builds | Week total |
|---|---|---|---|---|---|---|
| 1 | 1.0 | 0.5 (setup check) | 1.0 | 2.5 | 5.0 (tool installs 1.5, Experience Teardown 3.5) | 7.5 |
| 2 | 1.25 | 0.5 | 1.25 | 3.0 | 5.0 | 8.0 |
| 3 | 1.25 | 0.5 | 1.25 | 3.0 | 5.0 | 8.0 |
| 4 | 1.5 | 0.5 | 1.0 | 3.0 | 5.5 (recruiting and three sessions 3.0) | 8.5 |
| 5 | 1.0 | 0.5 | 1.0 | 2.5 | 5.5 | 8.0 |
| 6 | 1.25 | 0.5 | 1.25 | 3.0 | 5.0 | 8.0 |
| 7 | 1.5 | 1.0 (tryout) | 1.0 | 3.5 | 5.5 (three test sessions 2.0) | 9.0 |
| 8 | 1.0 | 0.5 | 1.0 | 2.5 | 5.0 | 7.5 |
| 9 | 0.75 | 0.25 | 1.5 | 2.5 | 5.5 | 8.0 |
| 10 | 1.0 | 0.25 | 1.25 | 2.5 | 5.5 (three to five test sessions 2.0) | 8.0 |
| 11 | 0.75 | 0.25 | 1.5 (peer review exchange) | 2.5 | 5.5 | 8.0 |
| 12 | 0.5 | 0.25 | 1.25 | 2.0 | 6.5 (build 4.0, tests 2.5) | 8.5 |
| 13 | 0.75 | 0.25 | 1.5 | 2.5 | 5.5 | 8.0 |
| 14 | 1.0 | 0.5 | 1.0 | 2.5 | 5.5 (recording and editing 2.5) | 8.0 |
| 15 | 0.5 | 0.5 (reflection) | 1.5 (watching and questioning classmates) | 2.5 | 4.5 | 7.0 |
| **Total** | | | | **40.0** | **80.0** | **120.0** |

Honest pressure points: Week 4 depends on participants showing up (students recruit in Week 3 to protect it); Week 7 and Week 12 are the heaviest at 9 and 8.5 hours; Week 12 build time is the most variable in the course.

---

## 6. Assessment plan

### Assignment groups (Canvas, weighted)

| Group | Weight | Items | Points |
|---|---|---|---|
| Process Work | 40% | 27 steps (PW1 to PW27), 10 points each | 270 |
| Projects | 35% | P1 Studio Project (Week 7), P2 Capstone Final and Defense (Week 15), 30 points each | 60 |
| Exercises, Quizzes and Reflections | 25% | 16 items (E1 to E16), 5 or 10 points | 90 |

Weights are the course build standard defaults. The team may adjust them with Michelle (see section 12).

### Every assignment

| ID | Assignment | Week, deadline | Group | Points | Measures objective(s) | Competency |
|---|---|---|---|---|---|---|
| E1 | Start Here Acknowledgement (syllabus, AI use, research ethics, Discord name) | 1 Thu | E | 10 | Course orientation | n/a (orientation) |
| E2 | Tool Setup Check | 1 Thu | E | 5 | 1.2 (practice) | 1 |
| PW1 | Experience Teardown | 1 Thu | PW | 10 | 1.1, 1.2 | 1 |
| PW2 | Heuristic Evaluation | 2 Thu | PW | 10 | 2.1 | 1 |
| E3 | Heuristics in Your Medium | 2 Thu | E | 5 | 2.3 | 1 |
| PW3 | Perception and Cognitive Load Redline | 2 Sun | PW | 10 | 2.2 | 1 |
| PW4 | Accessibility and Inclusion Audit | 3 Thu | PW | 10 | 3.1 | 1 |
| E4 | Constraint Walkthrough | 3 Thu | E | 5 | 3.1 (practice) | 1 |
| PW5 | Comparative Critique and Studio Problem Area | 3 Sun | PW | 10 | 3.2 | 1 |
| E5 | Research Ethics Check (must be passed before sessions) | 4 Thu | E | 5 | 4.2 | 2 |
| PW6 | Research Plan and Consent Materials | 4 Thu | PW | 10 | 4.1, 4.2 | 2 |
| PW7 | Research Sessions and Field Notes | 4 Sun | PW | 10 | 4.3 | 2 |
| PW8 | Research Synthesis | 5 Thu | PW | 10 | 5.1, 5.2 | 2 |
| E6 | AI Critique of a Problem Statement | 5 Thu | E | 5 | 5.2 | 2 |
| PW9 | Studio Project Brief | 5 Sun | PW | 10 | 5.3 | 2 |
| PW10 | Task Analysis and Flow | 6 Thu | PW | 10 | 6.1 | 4 |
| E7 | Flow Notation Practice | 6 Thu | E | 5 | 6.1 (practice) | 4 |
| PW11 | Design Concept and Low-Fidelity Prototype | 6 Sun | PW | 10 | 6.2 | 4 |
| E8 | Emerging Technology Tryout | 7 Thu | E | 5 | 7.1 (practice) | 3 |
| PW12 | Technology and Interaction Method Evaluation | 7 Thu | PW | 10 | 7.1, 7.2 | 3 |
| P1 | Studio Project | 7 Sun | Projects | 30 | 5.3, 6.2, 7.3 | 2, 4, 6 |
| PW13 | Capstone Proposal | 8 Thu | PW | 10 | 8.1 | 2 |
| E9 | Scope Self-Check | 8 Sun | E | 5 | 8.2 (practice) | 2 |
| PW14 | Capstone Brief and Research Addendum | 8 Sun | PW | 10 | 8.2 | 2 |
| PW15 | Capstone Design Concept | 9 Thu | PW | 10 | 9.1 | 4 |
| PW16 | Pre-Production Package | 9 Sun | PW | 10 | 9.2 | 4 |
| E10 to E14 | Build and AI-Use Log 1 to 5 | 9 to 13 Sun | E | 5 each | 9.2, 10.1, 11.1, 12.1, 13.2 (documentation) | 4, 5, 5, 7, 6 |
| PW17 | Prototype 1 | 10 Thu | PW | 10 | 10.1 | 5 |
| PW18 | Test Round 1 | 10 Sun | PW | 10 | 10.2 | 6 |
| PW19 | Prototype 2 with Technology Spike | 11 Thu | PW | 10 | 11.1 | 5 |
| PW20 | Peer Heuristic and Accessibility Review | 11 Sun | PW | 10 | 11.2 | 1 |
| PW21 | Functional Build: Alpha | 12 Thu | PW | 10 | 12.1 | 7 |
| PW22 | Test Round 2 | 12 Sun | PW | 10 | 12.2 | 6 |
| PW23 | Synthesis and Revision Plan | 13 Thu | PW | 10 | 13.1 | 6 |
| PW24 | Beta Build and Change Log | 13 Sun | PW | 10 | 13.2 | 6 |
| PW25 | Presentation Rehearsal | 14 Thu | PW | 10 | 14.1 | 7 |
| E15 | Caption and Accessibility Check | 14 Thu | E | 5 | 14.1 (practice) | 7 |
| PW26 | Release Candidate and Process Book | 14 Sun | PW | 10 | 14.2 | 7 |
| PW27 | Capstone Presentation to the Class | 15 Thu | PW | 10 | 15.1, 15.2 | 7 |
| P2 | Capstone Final and Defense | 15 Sun | Projects | 30 | All capstone objectives | 1 to 7 |
| E16 | Final Reflection | 15 Sun | E | 10 | 15.1 (reflection) | 7 |

E1 is the only item not tied to a competency; it is orientation and acknowledgement, which OSCQR expects.

### Process Work rubric (all PW items, 10 points)

Each PW assignment page names the objective the rubric evaluates in place of “[objective]”.

| Criterion | Full | Partial | Missing |
|---|---|---|---|
| Step requirements met: every required component is present and follows the instructions for your discipline (Objective [objective]) | 4 | 2 | 0 |
| Quality of reasoning: decisions are explained with UX principles, research, or test evidence, not preference (Objective [objective]) | 3 | 1.5 | 0 |
| Process evidence and AI-use log: sketches, versions, notes, or files show how the work developed; AI use is disclosed (Objective [objective]) | 1 | 0.5 | 0 |
| Critique: three substantive comments on classmates’ posts that follow the critique protocol (Objective [objective], applied to peers’ work) | 2 | 1 (one or two comments) | 0 |
| **Total** | **10** | | |

### Studio Project rubric (P1, 30 points)

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Brief grounded in research: goals, audience, method and timeline trace to real participant evidence (Objective 5.3) | 7 | 5 | 3 | 0 to 1 |
| Concept and flow: concept, flow, and low-fidelity prototype fit the brief and use the notation of the student’s medium (Objective 6.2) | 7 | 5 | 3 | 0 to 1 |
| Test conducted: at least three participants, task-based, with consent, and observations recorded (Objective 7.3) | 7 | 5 | 3 | 0 to 1 |
| Synthesis and iteration: findings are prioritized by severity and the revised prototype shows specific changes tied to findings and peer feedback (Objective 7.3) | 9 | 7 | 4 | 0 to 2 |
| **Total** | **30** | | | |

### Capstone Final and Defense rubric (P2, 30 points; one criterion per competency)

Each criterion is scored on what the student built **and** how the student explains and defends it in the recorded presentation and the defense responses.

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Course Competency 1: Analysis. Uses UX principles, heuristics, and accessibility guidelines to analyze the final experience and its competitors (Objective 15.2) | 4 | 3 | 2 | 0 to 1 |
| Course Competency 2: Research and brief. Final experience traces back to the brief and to real participant evidence (Objective 8.2) | 4 | 3 | 2 | 0 to 1 |
| Course Competency 3: Technology evaluation. Choice of technology or interaction method is justified against user needs, accuracy, accessibility, bias, and ethics, including what was rejected and why (Objective 9.1) | 4 | 3 | 2 | 0 to 1 |
| Course Competency 4: Design concept and pre-production. Pre-production artifacts show how the concept was developed and how it changed (Objective 9.2) | 4 | 3 | 2 | 0 to 1 |
| Course Competency 5: Prototyping. Prototypes increase in fidelity and each one answers a stated question (Objectives 10.1, 11.1) | 4 | 3 | 2 | 0 to 1 |
| Course Competency 6: Synthesis and iteration. Two test rounds plus peer feedback are synthesized into prioritized, implemented changes, with before and after evidence (Objective 13.1) | 5 | 4 | 2 | 0 to 1 |
| Course Competency 7: Original functional project. The build is original, functional by the definition for the student’s discipline (section 8), integrates research, testing, and an emerging technology or interaction method, and is defended clearly and accurately in response to classmates’ questions (Objective 15.1) | 5 | 4 | 2 | 0 to 1 |
| **Total** | **30** | | | |

### How the defense is graded

The defense is how the instructor confirms that the student authored and understands the work (authentic assessment). It is graded inside the Capstone Final rubric, not as a separate performance score.

1. **Week 15, Wednesday noon:** the student posts the recorded presentation (8 to 10 minutes, captioned) to Discord.
2. **Week 15, Thursday noon:** each student posts three defense questions to classmates’ presentations (this is the critique requirement for PW27). The instructor adds one question to every presentation.
3. **Week 15, Saturday noon:** the student posts defense responses, as a recorded video (3 to 5 minutes) or a written response, answering every question received.
4. **Week 15, Sunday noon:** the student submits the Capstone Final package in Canvas.

The instructor reads the build, the process book, the presentation, and the defense together. A defense that answers questions with evidence and names trade-offs lifts criteria 3, 6 and 7; a defense that cannot explain how a feature works, or that contradicts the process book, caps criterion 7 at Developing and triggers a short follow-up conversation before the grade is final. Unanswered questions lower criterion 7 by one level.

### Critique protocol (used every week)

Every critique comment has three parts and names at least one principle.

1. **I notice:** describe what you saw, heard, or did, in neutral terms. (“When I pressed the jump button, there was no sound until I landed.”)
2. **Because:** name the principle or evidence. (“Heuristic 1, visibility of system status: I could not tell if my input registered.”)
3. **What if:** offer one specific, testable suggestion. (“What if a short rising cue played on input, separate from the landing sound?”)

Rules: critique the work, not the person; no “looks good” or “nice” without the three parts; comment outside your own discipline at least once per week; disagree with evidence, not volume. The instructor models the protocol in Week 1 and comments in Discord throughout.

---

## 7. Discipline translation table

The disciplines below are examples. Students in other programs (for example film, music production, interior design, or computer science) choose the closest column and confirm with the instructor in the Start Here acknowledgement.

| Assignment | Game design | Animation | Sound design | Graphic design | App design | Digital media arts |
|---|---|---|---|---|---|---|
| PW1 Experience Teardown | Onboarding of a released game | A branching interactive story or animated UI | The audio UI of a game, app, or device (menus, notifications, feedback) | A brand experience that spans print and screen | A mobile app’s first-run experience | A museum kiosk, installation, or interactive video |
| PW2 Heuristic Evaluation | Menus, HUD, controls | Viewer controls and pacing of an interactive animation | Audio feedback, earcons, mix clarity, using the audio heuristics table | Wayfinding or packaging with a QR or AR layer | Core task in an app | An interactive exhibit |
| PW3 Perception and Cognitive Load Redline | Annotated HUD screenshots | Annotated frames: motion hierarchy, timing, staging | Annotated waveform or session map: masking, loudness hierarchy, cue frequency | Annotated layout: Gestalt grouping, hierarchy | Annotated screens | Annotated photos or video stills of a space |
| PW4 Accessibility and Inclusion Audit | Game Accessibility Guidelines, XAG | Captions, motion sensitivity, flashing | Captions for sound cues, mono option, separate volume sliders, visual alternatives | Contrast, type size, color reliance | WCAG 2.1 AA on mobile | Physical reach, audio description, multilingual access |
| PW7 Research Sessions | Interview or observe players | Interview viewers of interactive animation | Interview players, listeners, podcast or game-audio users, or blind and low-vision users of audio UI | Interview customers or passersby | Interview potential app users | Observe visitors in a public space |
| PW10 Task Analysis and Flow | Player flow, level flow diagram, core loop diagram | Branching storyboard flow | Audio flowchart, sound map, adaptive-audio state diagram (states, transitions, parameters) | Touchpoint flow across print, screen, space | User flow and wireflow | Visitor flow and space map |
| PW11 Low-Fidelity Prototype | Paper prototype or greybox | Thumbnail storyboard or rough animatic | Audio storyboard (radio-play sketch) or Wizard-of-Oz soundboard | Thumbnails and rough comps with a click-through | Paper prototype or Figma wireframes | Storyboard, scale model, or bodystorming video |
| PW12 Technology Evaluation | VR, hand tracking, controller-free input, AI NPCs | AR character placement, real-time engines, AI motion tools | Spatial audio, adaptive middleware, voice UI, AI voice and sound generation | WebAR image tracking, generative identity, AI imagery | Voice, AI agents, AI-assisted development | Projection, sensors, WebAR, gesture |
| PW17 and PW19 Prototypes | Greybox, then playable core mechanic | Animatic, then interactive branching cut | Wizard-of-Oz soundboard, then FMOD or Wwise prototype in an engine, or Web Audio prototype | Comp click-through, then working AR trigger | Wireframe, then clickable or coded prototype | Storyboard, then working sensor or WebAR prototype |
| PW18 and PW22 Testing | Playtest plus usability tasks | Viewer comprehension and choice tests | Listening tests: cue identification, eyes-closed navigation, A/B mix tests (headphones, local playback) | Task tests on site or in context | Task-based usability test | In-space observation test |
| PW21 Functional Build | Playable vertical slice of one loop | Interactive animated piece with working choices | Adaptive audio system running in a build, or a working audio UI or sonic AR walk | Working AR or multi-touchpoint experience | Working app (coded or AI-assisted) | Working installation or WebAR guide |
| P2 Capstone Final | See section 8 for capstone examples and “functional” definitions in each discipline | | | | | |

---

## 8. Capstone guide

### Milestones

| Week | Milestone | What it proves |
|---|---|---|
| 8 | Capstone Proposal; Capstone Brief and Research Addendum | The idea serves real users and fits seven weeks |
| 9 | Design Concept; Pre-Production Package | The concept is developed and the technology choice is justified |
| 10 | Prototype 1 (low fidelity); Test Round 1 | The core task or loop works for people other than the designer |
| 11 | Prototype 2 with Technology Spike; Peer Heuristic and Accessibility Review | The risky technology works at a basic level; a peer has reviewed it |
| 12 | Functional Build: Alpha; Test Round 2 | The experience runs end to end |
| 13 | Synthesis and Revision Plan; Beta Build and Change Log (feature freeze) | Testing and feedback drive specific changes |
| 14 | Presentation Rehearsal; Release Candidate and Process Book | The story of the project is clear and the build is stable |
| 15 | Presentation to the Class; Capstone Final and Defense | The student can defend every decision |

Students are strongly encouraged to grow the capstone from the Studio Project problem area, which lets the Week 4 research carry forward. A student who pivots to a new problem must complete the research addendum in full (at least two new sessions) in Week 8.

### Sample capstone ideas

Each idea is a starting point; students adapt it to their research.

**Game design**
1. A controller-free VR interaction for one mechanic (for example hand-tracked climbing or spellcasting), tested for comfort and learnability, built in Unity or Unreal.
2. An accessible onboarding sequence for one mechanic, with assist options and remappable controls, tested with players who have different motor or sensory needs.
3. A voice-commanded or AI-driven companion character for one level, with clear limits on what it understands and fallback controls.
4. A mixed-reality tabletop layer that adds rules help and scorekeeping to a physical board game.

**Animation**
1. A short branching animated story where viewer choices change the outcome, built in Twine with embedded animation, or in Unity.
2. An AR character placed in physical space (model-viewer or Reality Composer) that reacts to the viewer’s taps or position.
3. A motion system for an app’s onboarding: animated transitions and feedback states, with a reduced-motion alternative, tested for comprehension.
4. An animated explainer kiosk that responds to gesture or proximity.

**Sound design**
1. An adaptive game soundtrack system in FMOD or Wwise inside a Unity starter scene, where music and ambience respond to player state, with an accessibility mode (mono, visual cue indicators, separate volume sliders).
2. A location-based sonic AR walk for a campus or museum space, using spatial audio (Resonance Audio, Web Audio API, or an engine), tested with listeners on site.
3. An earcon and audio UI system for an app or device that lets blind and low-vision users navigate without the screen, tested with eyes-closed task trials.
4. A voice interface for a music practice tool (tuner, metronome, loop recorder) prototyped in Voiceflow or a Gemini Canvas Web Audio build.

**Graphic design**
1. An AR activation on packaging or a poster using image tracking (MindAR), tested with people in a store or hallway context.
2. A brand experience that moves from print to screen to space, with a wayfinding system tested by first-time visitors.
3. An interactive data poster: printed piece plus a WebAR or web layer that lets the viewer explore the data.
4. A generative identity system where users customize a brand mark within rules, built with AI-assisted code.

**App design**
1. A functional app for a community need, built with AI-assisted development in Gemini Canvas from the student’s own flows and wireframes.
2. A voice-first or AI-agent interface for a task with clear guardrails, tested for trust, error recovery, and accessibility.
3. An accessibility-first app (for example a transit or campus helper) tested with users of screen readers or switch access.
4. An offline-first field tool for workers or volunteers, tested in the real setting.

**Digital media arts**
1. An interactive installation that responds to visitors (webcam, microphone, or sensor input through p5.js), tested in a public space.
2. An AR guide for a museum or campus space using WebAR, with audio description and multilingual options.
3. An interactive video or kiosk experience with branching content, tested for wayfinding and dwell time.
4. A projection-mapped or spatial piece with a clear interaction model that first-time visitors can learn without instructions.

### Scope guardrails (so seven weeks is realistic)

- **One user, one core task or loop.** The capstone serves one primary persona doing one main thing. Everything else goes on a “later” list in the process book.
- **Three to five minutes of experience.** The tested experience should take a first-time user three to five minutes.
- **One emerging technology or interaction method.** Choose one (AR, VR, spatial audio, voice, gesture, AI-assisted development, AI interaction). Combining two requires instructor approval in Week 8.
- **Use the tools you know for everything except the one new thing.** The technology spike in Week 11 is where the new tool is proven; if it fails, the student switches to the fallback named in the proposal.
- **No networking, accounts, payments, or personal data collection.** No multiplayer, logins, or stored user data.
- **Reuse and placeholder assets are allowed** when disclosed; the grade is for the experience design, not asset volume.
- **Feature freeze at the end of Week 13.** Week 14 is for fixes, recording, and the process book only.
- **Fallback plan required.** Every proposal names a lower-tech fallback (for example a Wizard-of-Oz version of the voice interface) that still meets the “functional” definition.

### What “functional” means in each discipline (examples)

| Discipline | Functional means |
|---|---|
| Game design | A playable build (desktop, web, or headset) in which a first-time player can complete one core loop without the designer’s help |
| Animation | An interactive animated piece in which every choice point works and leads to a complete path |
| Sound design | An audio system that responds to user input or state in real time (middleware in an engine, Web Audio build, or a working sonic AR walk); a linear mix alone does not count |
| Graphic design | A working interactive layer (for example an image-tracked AR trigger or a live web experience) connected to the printed or spatial pieces |
| App design | An app that runs on a device or in a browser and completes the core task end to end; AI-generated code is allowed and disclosed |
| Digital media arts | An installation, kiosk, or WebAR piece that responds to visitors without the designer operating it |

A Wizard-of-Oz prototype (the designer secretly operates the system) is a valid **prototype** in Weeks 10 and 11, but it is not a functional final build unless the instructor approves it as the fallback.

---

## 9. Tool stack by discipline and stage

Gemini and Adobe Creative Cloud come first because the district provides both. Free alternatives are always allowed. Adobe Aero is discontinued and is not used. Gemini Gems are retiring for education and are not used; use Gemini Notebook and Gemini Canvas. Adobe Firefly is optional until district access is confirmed. Adobe product pages blocked automated checking and are marked [verify]; the products themselves are current.

### Shared tools (all disciplines)

| Stage | District-provided first | Free alternatives |
|---|---|---|
| Research planning and notes | [Gemini Notebook](https://notebook.google.com/) for organizing de-identified notes and sources; [Gemini](https://gemini.google.com/) for drafting interview guides the student then revises | [Excalidraw](https://excalidraw.com/), [draw.io](https://www.drawio.com/) |
| Synthesis (affinity maps, personas) | [Adobe Express](https://www.adobe.com/express/) [verify] for persona sheets | [FigJam](https://www.figma.com/figjam/) (free for education via [Figma for Education](https://www.figma.com/education/)), [Miro for Education](https://miro.com/education-whiteboard/) |
| Flows and pre-production | Adobe Illustrator, Photoshop ([Creative Cloud](https://www.adobe.com/creativecloud.html) [verify]) | [draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/), [Penpot](https://penpot.app/) |
| Wireframes and clickable prototypes | Adobe Express [verify]; Figma via education plan | [Figma](https://www.figma.com/education/), [Penpot](https://penpot.app/), [ProtoPie](https://protopie.io/) (education pricing [verify]) |
| AI-assisted functional prototypes | [Gemini Canvas](https://gemini.google/overview/canvas/) ([help page](https://support.google.com/gemini/answer/16047321)); [Google AI Studio](https://aistudio.google.com/) if enabled for students [verify] | [p5.js web editor](https://editor.p5js.org/), published in [Google Sites](https://sites.google.com/) with Embed code or a Gemini Canvas export |
| Testing and recording sessions | Google Meet [verify district access] with consent | [OBS Studio](https://obsproject.com/), [MeasuringU SUS guide](https://measuringu.com/sus/) |
| Accessibility checks | Gemini for caption and reading-level checks | [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/), [Coblis color-blindness simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/) |
| Presentation recording and captions | Adobe Premiere Pro (speech to text) [verify] | [OBS Studio](https://obsproject.com/), [Loom](https://www.loom.com/) (free tier [verify]) |
| Optional generative imagery | Adobe Firefly (availability unconfirmed) [verify] | Disclosed placeholder assets only |

### Discipline build tools (examples)

| Discipline | Pre-production | Prototype | Functional build |
|---|---|---|---|
| Game design | Paper, Illustrator, [draw.io](https://www.drawio.com/) for loop diagrams | Greybox in [Unity](https://unity.com/products/unity-student) (free student plan), [Unreal Engine](https://dev.epicgames.com/community/unreal-engine/learning), or [Godot](https://godotengine.org/) | Same engine; XR through Unity or Unreal; [Unity Learn: Unity Essentials](https://learn.unity.com/pathway/unity-essentials) for new users |
| Animation | Storyboards in Photoshop or [Krita](https://krita.org/) | Animatic in After Effects or Premiere [verify]; [OpenToonz](https://www.opentoonz.com/); [Blender](https://www.blender.org/) | Branching in [Twine](https://twinery.org/) or Unity; AR placement with [model-viewer](https://modelviewer.dev/) or [Reality Composer](https://developer.apple.com/augmented-reality/reality-composer/) (Apple devices) |
| Sound design | Sound maps and adaptive-audio state diagrams in [draw.io](https://app.diagrams.net/) or Illustrator; session planning in Audition [verify] | Audio storyboard in [Adobe Audition](https://www.adobe.com/products/audition.html) [verify], [Reaper](https://www.reaper.fm/) (discounted license, full trial), or [Audacity](https://www.audacityteam.org/); Wizard-of-Oz soundboard; [bfxr](https://www.bfxr.net/) for quick UI sounds | [FMOD Studio](https://www.fmod.com/) ([learning resources](https://www.fmod.com/learn)) or [Wwise](https://www.audiokinetic.com/en/wwise/) ([Wwise 101 course](https://www.audiokinetic.com/en/courses/wwise101/)) in Unity; [Unity audio](https://docs.unity3d.com/Manual/Audio.html); [Unreal MetaSounds](https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-in-unreal-engine); [Godot audio](https://docs.godotengine.org/en/stable/tutorials/audio/index.html); browser builds with the [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API), [Tone.js](https://tonejs.github.io/), or [Resonance Audio](https://resonance-audio.github.io/resonance-audio/) for spatial audio; voice prototypes in [Voiceflow](https://www.voiceflow.com/). Middleware licensing for education [verify]. |
| Graphic design | Thumbnails, Illustrator, InDesign [verify] | Comps in Illustrator or Photoshop; click-through in Figma | WebAR image tracking with [MindAR](https://hiukim.github.io/mind-ar-js-doc/) or [AR.js](https://ar-js-org.github.io/AR.js-Docs/); 3D placement with [model-viewer](https://modelviewer.dev/); vector work in Inkscape (https://inkscape.org/ [verify]) |
| App design | Flows and wireframes in Figma or Penpot | Clickable prototype in Figma or ProtoPie | Coded or AI-assisted build in Gemini Canvas; voice and agent interfaces in Voiceflow |
| Digital media arts | Storyboards, space plans, [Excalidraw](https://excalidraw.com/) | Video sketch in Premiere [verify]; bodystorming | Sensor and camera interaction in [p5.js](https://p5js.org/); WebAR with [A-Frame](https://aframe.io/), [WebXR samples](https://immersive-web.github.io/webxr-samples/), or model-viewer |

### XR, spatial and voice design guidance (all disciplines)

- [Google ARCore design guidelines](https://developers.google.com/ar/design) (CC BY 4.0)
- [Apple Human Interface Guidelines: Augmented reality](https://developer.apple.com/design/human-interface-guidelines/augmented-reality) and [Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos) (free to read, Apple copyright)
- [Android XR design](https://developer.android.com/design/ui/xr) (free to read [verify license])
- [Microsoft mixed reality design](https://learn.microsoft.com/en-us/windows/mixed-reality/design/design) (free to read [verify license])
- Meta Horizon design guidelines (https://developers.meta.com/horizon/design/ [verify])
- [W3C XR Accessibility User Requirements](https://www.w3.org/TR/xaur/) (W3C document license)
- Voice: [Voiceflow](https://www.voiceflow.com/); [NN/g: Voice Interaction UX](https://www.nngroup.com/articles/voice-interaction-ux/)


---

## 10. Module-by-module content

### Page conventions used below

- Every Canvas page opens with the title box (purple `#7a5080`, white text, the box is the h2 title), then Objectives (h3), then Overview (h3). In this public build the title boxes are purple; at GCC export every title box and date box changes to GCC red `#CB3338` and nothing else changes.
- Every module follows the same order: title box, Objectives, Overview, Watch, Read, Practice, Assessment, Critique / Discussion, Due.
- Every assignment page opens with its title box, then the line “This assignment measures Module Objective N.x, which supports Course Competency N,” then Objectives, Overview, Instructions, What you produce in your discipline, Rubric, and the date box.
- The Start Here page lists all seven competencies and the alignment map (section 2). Module and assignment pages name only the competencies they address.
- Reading times are estimates for a second-year student. NN/g articles are free to read and copyrighted by Nielsen Norman Group; Apple pages are free to read and copyrighted by Apple; licenses for other resources are given where confirmed.
- Every Process Work assignment uses the Process Work Rubric in section 6 (10 points). On each assignment page, every criterion is tagged with the objective named in the measures line.

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Start Here: Welcome to AVC2xx UX Design for Interactive Media</h2>

### Objectives

By the end of Start Here, you will be able to:

- Locate the course competencies, schedule, deadline rhythm, and grading groups.
- State the course rules for AI use, research ethics, and Discord critique.

### Overview

This course teaches user experience (UX) design as a method you can apply in any interactive medium. Your classmates come from multiple disciplines, for example game design, animation, sound design, graphic design, app design, digital media arts, and others. You will learn the same UX method together and apply it in your own medium. In Weeks 1 to 7 you complete short exercises that build a small Studio Project. In Weeks 8 to 15 you design, build, test, present, and defend one original capstone project in your discipline, and you keep the recorded presentation for your portfolio and job interviews.

### Official course competencies

1. Analyze interactive experiences using foundational UX principles.
2. Create a project brief based on user research.
3. Evaluate various technologies and interaction methods to meet user needs.
4. Develop a design concept using a pre-production process.
5. Design a prototype of an interactive experience.
6. Synthesize user testing and peer feedback into design iterations.
7. Create an original, functional interactive project that integrates user research, testing and an emerging technology or interaction method.

### Alignment map

| Course Competency | Modules | Process steps that build toward it | Final evidence |
|---|---|---|---|
| 1 | Weeks 1, 2, 3, 11, 15 | PW1, PW2, PW3, PW4, PW5, PW20 | Capstone Final criterion 1 |
| 2 | Weeks 4, 5, 8 | PW6, PW7, PW8, PW9, PW13, PW14; Studio Project | Capstone Final criterion 2 |
| 3 | Weeks 7, 9 | PW12, PW15 | Capstone Final criterion 3 |
| 4 | Weeks 6, 9 | PW10, PW11, PW15, PW16; Studio Project | Capstone Final criterion 4 |
| 5 | Weeks 6, 10, 11 | PW11 (practice), PW17, PW19 | Capstone Final criterion 5 |
| 6 | Weeks 7, 10, 12, 13 | Studio Project (practice), PW18, PW22, PW23, PW24 | Capstone Final criterion 6 |
| 7 | Weeks 12, 14, 15 | PW21, PW25, PW26, PW27 | Capstone Final criterion 7 |

### How the week works

Two deadlines a week, always at noon, Arizona time.

| | Thursday deadline | Sunday deadline |
|---|---|---|
| Post your work to the Discord critique channel | Wednesday, noon | Saturday, noon |
| Submit in Canvas: your work, process evidence, AI-use log, and three critique comments on classmates | Thursday, noon | Sunday, noon |
| Hard close: submissions in the 24-hour window lose 10%; nothing is accepted after | Friday, noon | Monday, noon |

Week 1 has one deadline (Thursday). Nothing is due on a holiday or during a break; shifted deadlines are announced at least one week ahead. You are encouraged to comment on classmates who post during the 24-hour window. This is ungraded “good karma” community citizenship and is not extra credit.

### Grading

| Group | Weight |
|---|---|
| Process Work (each step of the Studio Project and capstone, 10 points each) | 40% |
| Projects (Studio Project and Capstone Final, 30 points each) | 35% |
| Exercises, Quizzes and Reflections (5 or 10 points each) | 25% |

### Tools

The district provides Google Gemini and Adobe Creative Cloud. Use them first. Free alternatives are listed on the Tools page [instructor to create from section 9]. You will not need to buy software.

### AI use, research ethics, and Discord

Read the AI Use and Disclosure page, the Research Ethics and Consent page, and the Discord Critique Guide [instructor to create from sections 6 and 11] before Week 1’s deadline. E1 Start Here Acknowledgement checks that you have read them.

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 1: What UX Is in Your Discipline</h2>

### Objectives

Module 1 objectives. By the end of this module, you will be able to:

- 1.1 Distinguish user experience design from visual design using examples from your discipline (Course Competency 1)
- 1.2 Analyze an interactive experience in your discipline using human-centered design principles (Course Competency 1)

### Overview

Visual design asks how something looks. User experience design asks what it is like to use: whether people can understand it, accomplish what they came to do, and want to come back. Every interactive medium has users. A player learns a control scheme, a viewer chooses a branch in an animated story, a listener recognizes a notification sound without looking, a passerby scans an AR poster, a visitor approaches a kiosk. This week you meet your classmates from other disciplines, set up your tools, and take apart one experience from your own field to see the design decisions behind it.

If you completed AVC190, follow the extension path: choose an experience that is not a website (a game, installation, XR app, voice interface, or audio UI).

### Watch

- Week 1 introduction: UX across disciplines, with worked examples from a game menu and an audio notification system (12 minutes) [instructor to create]
- Course tour and Discord walkthrough (8 minutes) [instructor to create]

### Read

- [The Definition of User Experience (UX)](https://www.nngroup.com/articles/definition-user-experience/), Nielsen Norman Group (10 minutes)
- [What designers do](https://faculty.washington.edu/ajko/books/design-methods/designers), from *Design Methods* by Amy J. Ko, CC BY-ND 4.0 (20 minutes)
- [Design Thinking 101](https://www.nngroup.com/articles/design-thinking/), Nielsen Norman Group (12 minutes)
- Browse: [Design Kit](https://www.designkit.org/), IDEO.org, free to read [verify license] (10 minutes)

### Practice

**E2 Tool Setup Check (Exercises, 5 points).** Install or confirm access to the tools you expect to use, so a slow install never costs you a deadline later. Submit a screenshot of each tool open on your computer and one sentence on what you will use it for.

- Everyone: Gemini (when district access is active), Adobe Creative Cloud, Discord, and Figma or Penpot.
- Game design: Unity, Unreal, or Godot, with one template project opened.
- Sound design: Reaper, Audition, or Audacity; and FMOD Studio or Wwise if you expect an adaptive-audio capstone.
- Animation: your animation tool plus Twine or Blender if you expect interactivity or AR.
- Graphic design, app design, digital media arts: Illustrator or Photoshop; a phone that can open WebAR links if you expect an AR project.

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW1 Experience Teardown</h2>

This assignment measures Module Objectives 1.1 and 1.2, which support Course Competency 1.

### Objectives

- 1.1 Distinguish user experience design from visual design using examples from your discipline.
- 1.2 Analyze an interactive experience in your discipline using human-centered design principles.

### Overview

You will take apart one existing interactive experience from your discipline and explain who it is for, what they are trying to do, and how its design helps or gets in their way.

### Instructions

1. Choose one released interactive experience in your discipline that you can use for at least 15 minutes. It cannot be your own work.
2. Use it as a first-time user would. Capture three to six screenshots, short screen recordings, or audio clips of key moments.
3. Write 400 to 600 words, or record a 4-to-6-minute narrated video, that answers:
   - Who is the user, and what are they trying to accomplish?
   - Which three decisions are UX decisions (behavior, flow, feedback, clarity), and which are mainly visual or aesthetic? Explain the difference using your examples.
   - Where does the experience support the user well, and where does it fail them? Name the human-centered design principle at stake.
4. Begin your post with two sentences introducing yourself: your discipline and one interactive experience you admire.
5. Post to the Week 1 critique channel by Wednesday noon. By Thursday noon, submit your file in Canvas and leave three critique comments, at least one on a classmate from another discipline.

### What you produce in your discipline

| Discipline (examples) | Experience to tear down |
|---|---|
| Game design | The onboarding or first ten minutes of a released game |
| Animation | An interactive or branching animated story, or motion in an app interface |
| Sound design | The audio UI of a game, app, or device: menu sounds, notifications, feedback cues, adaptive music |
| Graphic design | A brand experience that moves between print and screen (packaging with a QR or AR layer, event identity with an app) |
| App design | The first-run experience of a mobile or tablet app |
| Digital media arts | A museum kiosk, interactive installation, or interactive video |
| Other disciplines | The closest equivalent; confirm with the instructor |

### Rubric

Process Work Rubric, 10 points. Criteria: Step requirements (Objective 1.2), 4; Quality of reasoning (Objective 1.1), 3; Process evidence and AI-use log (Objective 1.2), 1; Critique, three comments (Objective 1.2, applied to peers’ work), 2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

**E1 Start Here Acknowledgement (Exercises, 10 points).** A short Canvas quiz on the syllabus, deadline rhythm, AI-use rules, research ethics rules, and critique protocol. Enter your Discord screen name. Unlimited attempts until the hard close.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 1 critique channel. Use the critique protocol (I notice, Because, What if). This week, the “Because” should name a human-centered design principle from the readings.

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> E1 Start Here Acknowledgement, E2 Tool Setup Check, PW1 Experience Teardown (post Wednesday noon). Hard close Friday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 2: Heuristics, Perception and Cognitive Load</h2>

### Objectives

Module 2 objectives. By the end of this module, you will be able to:

- 2.1 Analyze an interactive experience in your discipline using the ten usability heuristics (Course Competency 1)
- 2.2 Analyze how principles of perception and cognitive load shape a user’s experience (Course Competency 1)
- 2.3 Apply the usability heuristics in the vocabulary of your medium (Course Competency 1)

### Overview

Usability heuristics are rules of thumb that experienced designers use to find problems quickly. They were written for software screens, but they apply to any interactive medium once you translate them. This week you learn the ten heuristics, learn how people perceive and process information (Gestalt grouping, hierarchy, attention, memory limits), and apply both to an experience in your discipline. Sound design students: the heuristics apply to what people hear as much as what they see. Use the table below.

### Heuristics in sound: a translation table

| Heuristic | What it means for audio |
|---|---|
| 1. Visibility of system status | Every input gets an audible confirmation; states (loading, low health, recording) have distinct cues |
| 2. Match between system and the real world | Sounds map to familiar meanings (rising pitch for success, falling for error) or to real sources |
| 3. User control and freedom | Listeners can skip, mute, or replay; separate volume for music, effects, and voice |
| 4. Consistency and standards | The same action always makes the same sound family; platform sounds are not repurposed |
| 5. Error prevention | Warning cues before irreversible actions; cues distinct enough not to be confused |
| 6. Recognition rather than recall | Earcons are few, distinct, and learnable; not 20 similar beeps |
| 7. Flexibility and efficiency of use | Experienced users can shorten or turn off tutorial narration |
| 8. Aesthetic and minimalist design | Only meaningful sounds play; the mix leaves room for the important cue |
| 9. Help users recognize, diagnose, and recover from errors | Error sounds are paired with spoken or visual explanation |
| 10. Help and documentation | Audio cues are explained once, in context, with a visual alternative |

### Watch

- Heuristic evaluation demonstrated on a game HUD, an app screen, and an audio UI (15 minutes) [instructor to create]

### Read

- [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/), Nielsen Norman Group (15 minutes)
- [How to Conduct a Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/), Nielsen Norman Group (10 minutes)
- [Minimize Cognitive Load to Maximize Usability](https://www.nngroup.com/articles/minimize-cognitive-load/), Nielsen Norman Group (10 minutes)
- [Proximity Principle in Visual Design](https://www.nngroup.com/articles/gestalt-proximity/) and [Similarity Principle in Visual Design](https://www.nngroup.com/articles/gestalt-similarity/), Nielsen Norman Group (15 minutes)
- Browse: [Laws of UX](https://lawsofux.com/), Jon Yablonski, CC BY-NC-ND 4.0 (10 minutes)
- Sound design and anyone using audio: [About sound](https://m2.material.io/design/sound/about-sound.html) and [Applying sound to UI](https://m2.material.io/design/sound/applying-sound-to-ui.html), Material Design (Google), free to read [verify license] (15 minutes); [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio), Apple Human Interface Guidelines (5 minutes)

### Practice

**E3 Heuristics in Your Medium (Exercises, 5 points).** Choose three heuristics. For each, write one sentence translating it into your medium and give one real example that follows it and one that breaks it (screenshots, clip, or audio file). Sound students may extend the table above rather than start from scratch.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW2 Heuristic Evaluation</h2>

This assignment measures Module Objective 2.1, which supports Course Competency 1.

### Objectives

- 2.1 Analyze an interactive experience in your discipline using the ten usability heuristics.

### Overview

You will run a heuristic evaluation of one experience in your discipline and rate the severity of each problem you find.

### Instructions

1. Choose an experience in your discipline (you may reuse your Week 1 choice).
2. Use it twice: once to learn it, once to evaluate it.
3. Record at least six issues in a table with these columns: issue, where it happens (screenshot, timestamp, or clip), heuristic violated, severity (0 = not a problem, 1 = cosmetic, 2 = minor, 3 = major, 4 = blocks the user), and a one-sentence recommendation.
4. Include at least one strength: a place where the design follows a heuristic well.
5. Post your table to Discord by Wednesday noon; submit in Canvas with three critique comments by Thursday noon.

### What you produce in your discipline

| Discipline (examples) | What you evaluate |
|---|---|
| Game design | Menus, HUD, control mapping, pause and settings screens |
| Animation | Viewer controls, branch choices, pacing, and feedback in an interactive animation |
| Sound design | Audio feedback, earcons, mix clarity, and volume controls, using the translation table |
| Graphic design | A wayfinding system or packaging with a digital layer |
| App design | One core task in an app, from start to finish |
| Digital media arts | An interactive exhibit, kiosk, or projection piece |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 2.1.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW3 Perception and Cognitive Load Redline</h2>

This assignment measures Module Objective 2.2, which supports Course Competency 1.

### Objectives

- 2.2 Analyze how principles of perception and cognitive load shape a user’s experience.

### Overview

A redline is an annotated image of a design. You will mark up one moment of an experience to show how perception and cognitive load affect what the user notices, understands, and remembers.

### Instructions

1. Choose one moment that asks the user to make a decision or notice something important.
2. Annotate it with at least five callouts. Each callout names a principle (proximity, similarity, figure and ground, hierarchy, attention, working memory, Hick’s law, or another from the readings) and explains the effect on the user.
3. Propose one change that would lower cognitive load, and sketch or mock it up quickly (paper photo is fine).
4. Post by Saturday noon; submit with three critique comments by Sunday noon.

### What you produce in your discipline

| Discipline (examples) | What you annotate |
|---|---|
| Game design | A HUD screenshot during combat or a busy menu |
| Animation | Two or three frames that show staging, motion hierarchy, and timing |
| Sound design | A waveform, spectrogram, or session screenshot of a busy moment, annotated for masking, loudness hierarchy, frequency space, and cue density; include the audio clip |
| Graphic design | A layout or package, annotated for Gestalt grouping and hierarchy |
| App design | A dense screen, such as a settings page or checkout |
| Digital media arts | A photo or video still of an installation or kiosk in its space |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 2.2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 2 critique channel. In each comment, the “Because” names a heuristic or perception principle by name.

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> PW2 Heuristic Evaluation, E3 Heuristics in Your Medium (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> PW3 Perception and Cognitive Load Redline (post Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 3: Accessibility, Inclusion and Critique</h2>

### Objectives

Module 3 objectives. By the end of this module, you will be able to:

- 3.1 Analyze an interactive experience for accessibility barriers using WCAG 2.1 AA and guidelines for your discipline (Course Competency 1)
- 3.2 Compare two interactive experiences in your discipline and identify priority changes using UX vocabulary (Course Competency 1)

### Overview

Accessibility means people with disabilities can perceive, understand, navigate, and interact with your work. Inclusive design goes further: it designs with people who are excluded and finds solutions that help everyone. This week you audit an experience for barriers, then write a comparative critique that pulls Weeks 1 to 3 together. You also choose the problem area for your Studio Project, because Week 4 starts research with real people.

### Watch

- [Web Accessibility Perspectives videos](https://www.w3.org/WAI/perspective-videos/), W3C Web Accessibility Initiative, W3C document license (watch any four, 10 minutes)
- Accessibility across media: captions for sound cues, motion sensitivity, color, and input (14 minutes) [instructor to create]

### Read

- [Introduction to Web Accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/), W3C WAI, W3C document license (15 minutes)
- [How People with Disabilities Use the Web](https://www.w3.org/WAI/people-use-web/), W3C WAI (15 minutes)
- [WCAG 2.1 Understanding documents](https://www.w3.org/WAI/WCAG21/Understanding/): read [Use of Color](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html) and [Audio Control](https://www.w3.org/WAI/WCAG21/Understanding/audio-control.html) (10 minutes)
- [Microsoft Inclusive Design](https://inclusive.microsoft.design/), free to read [verify license] (10 minutes)
- Choose the guideline set for your discipline (15 minutes):
  - Games and interactive media: [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/full-list/), CC BY-NC-ND 4.0; [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines), free to read [verify license]; [Accessible Player Experiences](https://accessible.games/accessible-player-experiences/), AbleGamers [verify license]
  - Sound design: [Making Audio and Video Media Accessible](https://www.w3.org/WAI/media/av/), W3C WAI; [Xbox Accessibility Guideline 104: Subtitles and captions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104) and [Guideline 105: Audio accessibility](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105)
  - AR, VR and spatial: [XR Accessibility User Requirements](https://www.w3.org/TR/xaur/), W3C
- [Design Critiques: Encourage a Positive Culture to Improve Products](https://www.nngroup.com/articles/design-critiques/), Nielsen Norman Group (10 minutes)
- [How to be critical](https://faculty.washington.edu/ajko/books/design-methods/critique), *Design Methods*, Amy J. Ko, CC BY-ND 4.0 (15 minutes)

### Practice

**E4 Constraint Walkthrough (Exercises, 5 points).** Use an experience in your discipline for ten minutes under one constraint: sound off; eyes closed (screen reader or audio only); one hand only; a color-blindness simulator ([Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/)); or captions only. Log what you could not do. This is not the same as living with a disability; reflect in two sentences on what the exercise cannot tell you.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW4 Accessibility and Inclusion Audit</h2>

This assignment measures Module Objective 3.1, which supports Course Competency 1.

### Objectives

- 3.1 Analyze an interactive experience for accessibility barriers using WCAG 2.1 AA and guidelines for your discipline.

### Overview

You will audit one experience against WCAG 2.1 AA principles (perceivable, operable, understandable, robust) and the guideline set for your discipline.

### Instructions

1. Choose an experience in your discipline.
2. Check at least eight guidelines: four from WCAG 2.1 AA and four from your discipline’s set. For each, record pass, fail, or not applicable, with evidence.
3. For each failure, name who is excluded and propose a fix.
4. Note one inclusive design opportunity: a change that would help people with and without disabilities.
5. Post by Wednesday noon; submit with three critique comments by Thursday noon.

### What you produce in your discipline

| Discipline (examples) | Audit focus |
|---|---|
| Game design | Remappable controls, subtitles, difficulty and assist options, color reliance, flashing |
| Animation | Captions, audio description, flashing and motion sensitivity, reduced-motion options |
| Sound design | Captions or subtitles for meaningful sound cues, visual alternatives to audio-only information, mono audio option, separate volume sliders, loudness and sudden peaks |
| Graphic design | Contrast, type size, color reliance, alternative text for the digital layer |
| App design | WCAG 2.1 AA on mobile: touch targets, labels, screen reader order, contrast |
| Digital media arts | Physical reach and height, seating, audio description, multilingual access, quiet alternatives |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 3.1.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW5 Comparative Critique and Studio Problem Area</h2>

This assignment measures Module Objective 3.2, which supports Course Competency 1.

### Objectives

- 3.2 Compare two interactive experiences in your discipline and identify priority changes using UX vocabulary.

### Overview

You will compare two experiences that serve a similar purpose in your discipline, then name the problem area you will research for your Studio Project.

### Instructions

1. Choose two experiences that serve a similar user goal (for example two rhythm games’ tutorials, two meditation apps’ audio onboarding, two museum AR guides).
2. In 500 to 700 words or a 5-to-7-minute narrated video, compare them using at least three heuristics, two perception principles, and two accessibility findings.
3. Identify the three highest-priority changes across both experiences, with severity ratings.
4. Studio problem area: in one paragraph, name a user group and an experience problem in your discipline that you want to research in Week 4. It should be a group you can reach (classmates outside this course, friends, coworkers, family, community members who are 18 or older).
5. Post by Saturday noon; submit with three critique comments by Sunday noon.

### What you produce in your discipline

| Discipline (examples) | Sample comparison | Sample problem area |
|---|---|---|
| Game design | Two games’ first-time tutorials | New players quit before learning a core mechanic |
| Animation | Two interactive stories’ choice moments | Viewers miss that a choice is available |
| Sound design | Two games’ adaptive music systems, or two apps’ notification sound sets | Players cannot tell game-state changes by sound alone; listeners confuse notification sounds |
| Graphic design | Two brands’ packaging with digital layers | Shoppers ignore QR or AR prompts |
| App design | Two apps that do the same task | Older adults abandon sign-up |
| Digital media arts | Two museum interactives | Visitors walk past an installation without engaging |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 3.2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 3 critique channel. Comment on at least one classmate’s problem area: is the user group reachable in Week 4?

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> PW4 Accessibility and Inclusion Audit, E4 Constraint Walkthrough (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> PW5 Comparative Critique and Studio Problem Area (post Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 4: User Research Methods and Ethics</h2>

### Objectives

Module 4 objectives. By the end of this module, you will be able to:

- 4.1 Plan user research with methods matched to your research questions (Course Competency 2)
- 4.2 Prepare informed consent materials that meet the course research ethics rules (Course Competency 2)
- 4.3 Conduct interviews, surveys, or observations and record de-identified field notes (Course Competency 2)

### Overview

Designers who skip research design for themselves. This week you plan and run a small research study with real people. You will choose methods (interviews, surveys, observation), write questions that ask about behavior rather than opinions about your idea, and treat participants ethically: informed consent, privacy, and the right to stop. AI cannot stand in for your participants; you must talk with or observe real people.

### Watch

- Running a good interview: a demonstration and a bad-interview blooper reel (15 minutes) [instructor to create]
- Consent in practice: reading the consent script and handling a participant who wants to stop (6 minutes) [instructor to create]

### Read

- [User Interviews 101](https://www.nngroup.com/articles/user-interviews/), Nielsen Norman Group (12 minutes)
- [Field Studies](https://www.nngroup.com/articles/field-studies/), Nielsen Norman Group (10 minutes)
- [28 Tips for Creating Great Qualitative Surveys](https://www.nngroup.com/articles/qualitative-surveys/), Nielsen Norman Group (15 minutes)
- [Obtaining Consent for User Research](https://www.nngroup.com/articles/informed-consent/), Nielsen Norman Group (10 minutes)
- [How to understand problems](https://faculty.washington.edu/ajko/books/design-methods/understand), *Design Methods*, Amy J. Ko, CC BY-ND 4.0 (20 minutes)
- [The Belmont Report](https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html), U.S. Department of Health and Human Services, public domain [verify link] (skim the three principles, 10 minutes)
- Course page: Research Ethics and Consent, with consent script template [instructor to create from section 11]

### Practice

**E5 Research Ethics Check (Exercises, 5 points).** A short quiz on consent, recording, de-identification, participants under 18, and AI use with research data. You must score 100% (unlimited attempts) before you run sessions for PW7.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW6 Research Plan and Consent Materials</h2>

This assignment measures Module Objectives 4.1 and 4.2, which support Course Competency 2.

### Objectives

- 4.1 Plan user research with methods matched to your research questions.
- 4.2 Prepare informed consent materials that meet the course research ethics rules.

### Overview

You will write a one-page research plan and adapt the course consent script for your study.

### Instructions

1. Write two or three research questions about your problem area (what you need to learn, not what you want to build).
2. Choose methods: at least three interviews or observations, or one survey (at least ten responses) plus two interviews.
3. Write your interview guide (eight to twelve open questions about past behavior) or survey.
4. Adapt the course consent script: purpose, what you will record, how notes will be de-identified, how long you keep them, and the right to stop.
5. List who you will recruit and how. Participants must be 18 or older.
6. You may ask Gemini to critique your interview guide after you have written it. Record what you changed in your AI-use log.
7. Post by Wednesday noon; submit with three critique comments by Thursday noon. Instructor feedback on plans flagged “early review” is returned within 48 hours.

### What you produce in your discipline

| Discipline (examples) | Sample research question |
|---|---|
| Game design | How do new players learn controls when no tutorial is shown? |
| Animation | How do viewers decide whether a moment in a video is interactive? |
| Sound design | How do players or listeners notice and interpret game-state changes by sound alone? How do blind or low-vision users navigate apps by audio? |
| Graphic design | What makes shoppers stop and engage with a package’s digital layer? |
| App design | Where do first-time users get stuck in a sign-up flow? |
| Digital media arts | What draws visitors to approach an installation, and what makes them leave? |

### Rubric

Process Work Rubric, 10 points. Criteria: Step requirements (Objective 4.2), 4; Quality of reasoning (Objective 4.1), 3; Process evidence and AI-use log (Objective 4.1), 1; Critique (Objective 4.1, applied to peers’ work), 2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW7 Research Sessions and Field Notes</h2>

This assignment measures Module Objective 4.3, which supports Course Competency 2.

### Objectives

- 4.3 Conduct interviews, surveys, or observations and record de-identified field notes.

### Overview

You will run your study and submit de-identified notes and a short summary of what surprised you.

### Instructions

1. Obtain consent before every session (written or recorded verbal consent).
2. Run at least three sessions (or your survey plus two interviews).
3. Take notes during or immediately after each session. Replace names with codes (P1, P2, P3). Remove any detail that could identify a person.
4. If you record audio or video, store it only in your district Google account and delete it at the end of the course.
5. Submit: de-identified notes for each session, a 200-word summary of surprises, and your consent records (kept private, submitted only to the instructor).
6. Post only your summary to Discord (never notes or recordings) by Saturday noon; submit with three critique comments by Sunday noon.

### What you produce in your discipline

| Discipline (examples) | Sessions |
|---|---|
| Game design | Watch players try a game they have not played; interview afterward |
| Animation | Interview viewers about interactive video they have used |
| Sound design | Interview players or listeners about audio cues they rely on; observe someone playing with sound only, then with sound off |
| Graphic design | Observe shoppers or passersby with a package or poster; short intercept interviews |
| App design | Interview people who use apps for the task you are studying |
| Digital media arts | Observe visitors in a public space for 30 minutes; interview two |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 4.3.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 4 critique channel. Post only summaries. Comment on what a classmate should ask in a follow-up session.

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> E5 Research Ethics Check, PW6 Research Plan and Consent Materials (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> PW7 Research Sessions and Field Notes (post summary Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 5: Synthesis and the Project Brief</h2>

### Objectives

Module 5 objectives. By the end of this module, you will be able to:

- 5.1 Synthesize research findings using an affinity map and a persona (Course Competency 2)
- 5.2 Write a problem statement grounded in research evidence (Course Competency 2)
- 5.3 Create a project brief that states goals, audience, method, and timeline (Course Competency 2)

### Overview

Raw notes do not design anything. Synthesis turns them into patterns, a persona, and a clear problem statement, and the brief turns those into a plan. This week you sort your own notes by hand first; only then may you ask AI to challenge your problem statement. The brief you write this week drives the rest of your Studio Project.

### Watch

- Affinity mapping from real notes, start to finish, in FigJam (14 minutes) [instructor to create]

### Read

- [Affinity Diagramming](https://www.nngroup.com/articles/affinity-diagram/), Nielsen Norman Group (10 minutes)
- [Personas Make Users Memorable for Product Team Members](https://www.nngroup.com/articles/persona/), Nielsen Norman Group (12 minutes)
- [Problem Statements in UX Discovery](https://www.nngroup.com/articles/problem-statements/), Nielsen Norman Group (10 minutes)
- [Journey Mapping 101](https://www.nngroup.com/articles/journey-mapping-101/), Nielsen Norman Group (10 minutes)
- [How to define problems](https://faculty.washington.edu/ajko/books/design-methods/problems), *Design Methods*, Amy J. Ko, CC BY-ND 4.0 (20 minutes)

### Practice

**E6 AI Critique of a Problem Statement (Exercises, 5 points).** After you write your problem statement for PW8, paste only the statement (no participant data) into Gemini and ask it to critique the statement for clarity, bias, and testability. Submit the original, the AI’s critique, your revised statement, and two sentences on which suggestions you rejected and why.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW8 Research Synthesis</h2>

This assignment measures Module Objectives 5.1 and 5.2, which support Course Competency 2.

### Objectives

- 5.1 Synthesize research findings using an affinity map and a persona.
- 5.2 Write a problem statement grounded in research evidence.

### Overview

You will turn your de-identified notes into an affinity map, a persona, and a problem statement.

### Instructions

1. Write each observation or quote from your notes on its own sticky note (FigJam, Miro, or paper). Aim for 30 or more.
2. Group them by hand into themes; name each theme. Photograph or export each stage.
3. Build one persona from the patterns (goals, behaviors, frustrations, context, access needs). Do not invent details the research does not support; mark assumptions.
4. Write a problem statement: “[User] needs a way to [need] because [insight from research].”
5. Post by Wednesday noon; submit with three critique comments by Thursday noon.

### What you produce in your discipline

All disciplines produce the same three artifacts. Sound design students should include sonic context in the persona: listening environment (headphones, speakers, noisy room), hearing profile if shared, and how the person uses sound to make decisions.

### Rubric

Process Work Rubric, 10 points. Criteria: Step requirements (Objective 5.1), 4; Quality of reasoning (Objective 5.2), 3; Process evidence and AI-use log (Objective 5.1), 1; Critique (Objective 5.2, applied to peers’ work), 2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW9 Studio Project Brief</h2>

This assignment measures Module Objective 5.3, which supports Course Competency 2.

### Objectives

- 5.3 Create a project brief that states goals, audience, method, and timeline.

### Overview

You will write a one-to-two-page brief for a small Studio Project that addresses your problem statement. You will build and test a low-fidelity version of it by Week 7.

### Instructions

1. Use the brief template [instructor to create]: problem statement, goals (user goals and design goals), audience (your persona), success criteria (how you will know it works), method (what you will make and in what medium), constraints, and a two-week timeline.
2. Cite at least three findings from your research by participant code.
3. Keep the scope small: one user, one task.
4. Post by Saturday noon; submit with three critique comments by Sunday noon.

### What you produce in your discipline

| Discipline (examples) | Sample Studio Project scope |
|---|---|
| Game design | A redesigned tutorial for one mechanic |
| Animation | One branching choice moment, clearly signaled |
| Sound design | An earcon set of five to eight cues for one app or game state system, or an adaptive-audio concept for one level |
| Graphic design | A package with a clear AR or QR prompt |
| App design | A redesigned sign-up or core task flow |
| Digital media arts | An approach-and-engage sequence for one installation |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 5.3.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 5 critique channel. For each brief you comment on, check that every goal traces to research evidence.

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> PW8 Research Synthesis, E6 AI Critique of a Problem Statement (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> PW9 Studio Project Brief (post Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 6: Structure, Flow and Low-Fidelity Iteration</h2>

### Objectives

Module 6 objectives. By the end of this module, you will be able to:

- 6.1 Construct a task analysis and a flow in the notation of your medium (Course Competency 4)
- 6.2 Develop a design concept and a low-fidelity prototype through pre-production iteration (Course Competency 4)

### Overview

Before anyone builds, designers map how a person moves through an experience: the steps, the decisions, the states, and what happens when something goes wrong. Then they sketch fast and cheap so they can throw ideas away. Every medium has its own notation. Game designers draw loop and level flow diagrams; animators draw branching storyboards; sound designers draw audio flowcharts, sound maps, and adaptive-audio state diagrams; app designers draw user flows and wireflows. This week you learn the shared logic and use your medium’s notation.

### Watch

- Flows in five notations: a user flow, a wireflow, a core loop diagram, a branching storyboard, and an adaptive-audio state diagram (16 minutes) [instructor to create]
- Low-fidelity prototyping in paper, greybox, animatic, and Wizard-of-Oz soundboard form (12 minutes) [instructor to create]

### Read

- [Task Analysis: Support Users in Achieving Their Goals](https://www.nngroup.com/articles/task-analysis/), Nielsen Norman Group (10 minutes)
- [User Journeys vs. User Flows](https://www.nngroup.com/articles/user-journeys-vs-user-flows/), Nielsen Norman Group (8 minutes)
- [Wireflows](https://www.nngroup.com/articles/wireflows/), Nielsen Norman Group (8 minutes)
- [The Difference Between Information Architecture and Navigation](https://www.nngroup.com/articles/ia-vs-navigation/) and [Card Sorting](https://www.nngroup.com/articles/card-sorting-definition/), Nielsen Norman Group (15 minutes)
- [Storyboards Help Visualize UX Ideas](https://www.nngroup.com/articles/storyboards-visualize-ideas/) and [Paper Prototyping](https://www.nngroup.com/articles/paper-prototyping/), Nielsen Norman Group (15 minutes)
- [How to prototype](https://faculty.washington.edu/ajko/books/design-methods/prototype), *Design Methods*, Amy J. Ko, CC BY-ND 4.0 (20 minutes)
- Sound design: [FMOD learning resources](https://www.fmod.com/learn) (browse the adaptive audio examples, 15 minutes)

### Practice

**E7 Flow Notation Practice (Exercises, 5 points).** Diagram a familiar task in your medium’s notation in 20 minutes: making toast as a user flow; a pause menu as a state diagram; a doorbell as an audio flowchart. Post a photo or export.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW10 Task Analysis and Flow</h2>

This assignment measures Module Objective 6.1, which supports Course Competency 4.

### Objectives

- 6.1 Construct a task analysis and a flow in the notation of your medium.

### Overview

You will break your persona’s task into steps and map the flow of your Studio Project, including errors and alternate paths.

### Instructions

1. Write a task analysis: the persona’s goal, the steps, the decisions, and the information or feedback needed at each step.
2. Map the flow in your medium’s notation. Include the happy path, at least two alternate or error paths, and entry and exit points.
3. Note which research findings shaped the flow.
4. Post by Wednesday noon; submit with three critique comments by Thursday noon.

### What you produce in your discipline

| Discipline (examples) | Flow artifact |
|---|---|
| Game design | Core loop diagram plus a player flow for the tutorial; optional level flow sketch |
| Animation | Branching storyboard flow showing every choice point and outcome |
| Sound design | Adaptive-audio state diagram (states such as explore, danger, combat, victory; transitions; the game or app parameters that trigger them; fade and crossfade times), or an audio flowchart for an audio UI, or a sound map of a space for a sonic AR walk |
| Graphic design | Touchpoint flow across print, screen, and space |
| App design | User flow and wireflow |
| Digital media arts | Visitor flow on a floor plan, with approach, engage, and exit zones |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 6.1.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW11 Design Concept and Low-Fidelity Prototype</h2>

This assignment measures Module Objective 6.2, which supports Course Competency 4.

### Objectives

- 6.2 Develop a design concept and a low-fidelity prototype through pre-production iteration.

### Overview

You will sketch at least three concept directions, choose one, and build a low-fidelity prototype you can test with people next week.

### Instructions

1. Sketch three different concept directions by hand before using any AI tool. Then you may ask Gemini for variations; log what you used.
2. Choose one direction and write a 100-word concept statement that links it to your brief.
3. Build a low-fidelity prototype that a person can try (paper, greybox, rough animatic, Wizard-of-Oz soundboard, clickable wireframe).
4. Write the test question your prototype is meant to answer.
5. Post by Saturday noon; submit with three critique comments by Sunday noon.

### What you produce in your discipline

| Discipline (examples) | Low-fidelity prototype |
|---|---|
| Game design | Paper prototype or greybox scene of the mechanic |
| Animation | Thumbnail storyboard or rough animatic with choice points |
| Sound design | Audio storyboard (a radio-play-style sketch of the experience) or a Wizard-of-Oz soundboard: you trigger cues live in Reaper, Audition, or a sampler while a participant uses a paper or greybox version |
| Graphic design | Thumbnails and rough comps with a click-through of the digital layer |
| App design | Paper prototype or Figma wireframes |
| Digital media arts | Storyboard, scale model, or bodystorming video |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 6.2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 6 critique channel. Try classmates’ prototypes where you can; comment on the flow, not the polish.

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> PW10 Task Analysis and Flow, E7 Flow Notation Practice (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> PW11 Design Concept and Low-Fidelity Prototype (post Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 7: Emerging Technologies, Testing and Iteration</h2>

### Objectives

Module 7 objectives. By the end of this module, you will be able to:

- 7.1 Evaluate at least three technologies or interaction methods against user needs, accuracy, accessibility, and bias (Course Competency 3)
- 7.2 Assess the ethical risks of an emerging technology, including privacy, manipulative patterns, and inclusion (Course Competency 3)
- 7.3 Revise a low-fidelity prototype based on usability test findings and peer feedback (Course Competency 6)

### Overview

New interaction methods (augmented, virtual, and mixed reality; spatial, voice, and gesture interfaces; AI-assisted design and development) open new possibilities and new ways to fail people. This week you try one, then evaluate several against your persona’s needs. You also complete the first full UX cycle: you test your low-fidelity prototype with real people, prioritize what you learn, revise, and submit the Studio Project. This is your rehearsal for the capstone.

### Watch

- Emerging interaction methods tour: WebAR, VR, spatial audio, voice, gesture, and AI-assisted development, with one example from each discipline (18 minutes) [instructor to create]
- Running a three-person usability test or playtest of a low-fidelity prototype (10 minutes) [instructor to create]

### Read

- [People + AI Guidebook](https://pair.withgoogle.com/guidebook/), Google PAIR, free to read [verify license] (read the overview and one chapter, 20 minutes)
- [AI for UX: Getting Started](https://www.nngroup.com/articles/ai-ux-getting-started/), Nielsen Norman Group (10 minutes)
- [Augmented Reality: What Does It Mean for UX?](https://www.nngroup.com/articles/augmented-reality-ux/) and [Voice Interaction UX](https://www.nngroup.com/articles/voice-interaction-ux/), Nielsen Norman Group (20 minutes)
- [ARCore design guidelines](https://developers.google.com/ar/design), Google, CC BY 4.0 (15 minutes); or [Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos), Apple (15 minutes)
- [Deceptive Patterns in UX](https://www.nngroup.com/articles/deceptive-patterns/), Nielsen Norman Group, and browse [Deceptive Design](https://deceptive.design/) [verify license] (15 minutes)
- [AI competency framework for students](https://www.unesco.org/en/articles/ai-competency-framework-students), UNESCO [verify license] (skim, 10 minutes)
- [The Wizard of Oz Method in UX](https://www.nngroup.com/articles/wizard-of-oz/), Nielsen Norman Group (8 minutes)
- Sound design: [Resonance Audio](https://resonance-audio.github.io/resonance-audio/) overview, open source (10 minutes)

### Practice

**E8 Emerging Technology Tryout (Exercises, 5 points).** Spend 45 minutes hands-on with one emerging technology or interaction method you have not used: build a model-viewer AR scene, ask Gemini Canvas to generate a working prototype from your own sketch, make a Voiceflow voice flow, place a spatialized sound in Resonance Audio or an engine, or try a WebXR sample. Submit a screenshot or recording and three observations about what a user would experience.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW12 Technology and Interaction Method Evaluation</h2>

This assignment measures Module Objectives 7.1 and 7.2, which support Course Competency 3.

### Objectives

- 7.1 Evaluate at least three technologies or interaction methods against user needs, accuracy, accessibility, and bias.
- 7.2 Assess the ethical risks of an emerging technology, including privacy, manipulative patterns, and inclusion.

### Overview

You will evaluate three technologies or interaction methods for your Studio Project’s persona and recommend one, using a decision matrix.

### Instructions

1. Choose three candidate technologies or methods, at least one of which is emerging (AR, VR, mixed reality, spatial audio, voice, gesture, AI interaction, or AI-assisted development).
2. Score each in a decision matrix against: fit to persona needs; accuracy and reliability; accessibility; bias risk; privacy; manipulative-pattern risk; cost and device access for your users; and your ability to build it in seven weeks.
3. For any AI-driven method, test it at least five times with varied input and record accuracy and any biased or inaccessible output.
4. Recommend one method and explain what you rejected and why (300 to 500 words).
5. Post by Wednesday noon; submit with three critique comments by Thursday noon.

### What you produce in your discipline

| Discipline (examples) | Sample candidates |
|---|---|
| Game design | Controller, hand tracking in VR, voice commands, AI-driven NPC dialogue |
| Animation | Linear video, AR character placement, real-time engine, AI motion assistance |
| Sound design | Stereo mix, binaural or ambisonic spatial audio, adaptive middleware (FMOD or Wwise), voice UI, AI voice or sound generation |
| Graphic design | QR to web, WebAR image tracking, generative AI imagery, NFC |
| App design | Touch UI, voice-first UI, AI agent, AI-assisted development of a functional prototype |
| Digital media arts | Touchscreen kiosk, camera-based gesture, proximity sensors, WebAR, projection |

### Rubric

Process Work Rubric, 10 points. Criteria: Step requirements (Objective 7.1), 4; Quality of reasoning (Objective 7.2), 3; Process evidence and AI-use log (Objective 7.1), 1; Critique (Objective 7.1, applied to peers’ work), 2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">P1 Studio Project</h2>

This assignment measures Module Objectives 5.3, 6.2 and 7.3, which support Course Competencies 2, 4 and 6.

### Objectives

- 5.3 Create a project brief that states goals, audience, method, and timeline.
- 6.2 Develop a design concept and a low-fidelity prototype through pre-production iteration.
- 7.3 Revise a low-fidelity prototype based on usability test findings and peer feedback.

### Overview

The Studio Project completes your first full UX cycle: research, brief, concept, prototype, test, revise. You will test your Week 6 prototype with three people, prioritize what you learn, revise, and present the whole cycle in a short case summary.

### Instructions

1. Write a short test plan: the task(s) participants will attempt, what success looks like, and what you will observe. Reuse your consent script.
2. Test your low-fidelity prototype with at least three people (18 or older, not in this course). Use think-aloud. Do not explain or defend the design during the session.
3. Record observations in a table: participant code, task, success or failure, what happened, severity (0 to 4).
4. Prioritize findings with peer feedback from Weeks 5 and 6. Choose the top three changes.
5. Revise the prototype. Show before and after.
6. Write a case summary (one to two pages, or a 5-minute narrated video): brief, concept, flow, prototype, test findings, changes, and what you would test next. End with a short midpoint reflection: what you learned about UX in your discipline and what you will do differently in the capstone.
7. Post the case summary by Saturday noon; submit the full package with three critique comments by Sunday noon.

### What you produce in your discipline

| Discipline (examples) | How to test the low-fidelity prototype |
|---|---|
| Game design | Paper or greybox playtest: can players learn the mechanic without help? |
| Animation | Show the animatic and pause at choice points: do viewers notice the choice and predict the outcome? |
| Sound design | Wizard-of-Oz or audio storyboard listening test, on headphones: can participants identify each cue’s meaning? Can they complete the task with eyes closed? |
| Graphic design | Hallway test with the comp and click-through: do people notice and act on the prompt? |
| App design | Paper or wireframe task test |
| Digital media arts | Bodystorming or scale-model walkthrough: where do visitors go and stop? |

### Rubric

Studio Project Rubric (section 6), 30 points: Brief grounded in research (Objective 5.3), 7; Concept and flow (Objective 6.2), 7; Test conducted (Objective 7.3), 7; Synthesis and iteration (Objective 7.3), 9.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 7 critique channel. Studio Project summaries post Saturday. In your comments, name one finding from a classmate’s test you would have expected and one that surprised you.

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> E8 Emerging Technology Tryout, PW12 Technology and Interaction Method Evaluation (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> P1 Studio Project (post Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 8: Capstone Launch, Proposal and Brief</h2>

### Objectives

Module 8 objectives. By the end of this module, you will be able to:

- 8.1 Propose an original capstone project that integrates user research and an emerging technology or interaction method (Course Competency 2)
- 8.2 Create a capstone project brief supported by a research addendum (Course Competency 2)

### Overview

The second half of the course is one capstone project in your discipline: original, functional, interactive, tested with real people, and built around an emerging technology or interaction method. You will present it to the class and defend it in a recorded presentation you can use in your portfolio and in job interviews. Most students grow the capstone from their Studio Project problem area, which lets your research carry forward. If you choose a new problem, you must complete a full research addendum this week. Read the Capstone Guide before you write your proposal.

### Watch

- Capstone launch: what “functional” means in each discipline, scope guardrails, and three strong past-style proposals (15 minutes) [instructor to create]

### Read

- Capstone Guide: milestones, sample ideas for each discipline, scope guardrails, and the definition of functional [instructor to create from section 8]
- [UX Prototypes: Low Fidelity vs. High Fidelity](https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/), Nielsen Norman Group (10 minutes)
- Review your Studio Project feedback and your PW12 technology evaluation (20 minutes)

### Practice

**E9 Scope Self-Check (Exercises, 5 points).** Complete the scope checklist for your capstone: one user, one core task or loop, three to five minutes of experience, one emerging technology or method, no networking or personal data, a named fallback. Submit the checklist with any item you cannot check and your plan to fix it.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW13 Capstone Proposal</h2>

This assignment measures Module Objective 8.1, which supports Course Competency 2.

### Objectives

- 8.1 Propose an original capstone project that integrates user research and an emerging technology or interaction method.

### Overview

You will propose your capstone in one page and a 90-second pitch. The instructor responds within 48 hours so you can write your brief by Sunday.

### Instructions

1. Use the proposal template [instructor to create]: working title, discipline, persona and problem statement, what the user will do, the emerging technology or interaction method and why (cite PW12), what “functional” will mean for this project, risks, and a lower-tech fallback.
2. Record a 90-second pitch (video or audio with slides).
3. Post the pitch by Wednesday noon; submit the proposal and pitch with three critique comments by Thursday noon.

### What you produce in your discipline

See the Capstone Guide for sample ideas. Examples: a hand-tracked VR mechanic (game design); an AR character that reacts to the viewer (animation); an adaptive soundtrack system in FMOD inside a Unity starter scene, or a location-based sonic AR walk (sound design); an image-tracked AR poster (graphic design); an AI-assisted functional app for a community need (app design); a visitor-responsive installation (digital media arts).

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 8.1.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW14 Capstone Brief and Research Addendum</h2>

This assignment measures Module Objective 8.2, which supports Course Competency 2.

### Objectives

- 8.2 Create a capstone project brief supported by a research addendum.

### Overview

You will write the brief that governs your capstone and add new research that tests whether your proposal fits real users.

### Instructions

1. Research addendum: run at least two new sessions (interviews, observations, or a concept test of your proposal) using the course consent process. If you changed problem areas, run at least three. Add de-identified notes and update your affinity map and persona.
2. Write the brief (two pages): problem statement, persona, user and design goals, success criteria, chosen technology or method, scope (in and out), test plan outline for two rounds, accessibility commitments, and a week-by-week timeline through Week 15.
3. Incorporate the instructor’s proposal feedback; note what you changed.
4. Post by Saturday noon; submit with three critique comments by Sunday noon.

### What you produce in your discipline

All disciplines produce the same brief. Sound design students state the listening context (headphones, speakers, headset, or open air), the platform that will run the audio system, and the parameters that will drive it.

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 8.2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 8 critique channel. Comment on scope: is the proposal small enough to finish and test in seven weeks? Capstone check-in 1: the instructor replies to every proposal with a short video or written note.

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> PW13 Capstone Proposal (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> E9 Scope Self-Check, PW14 Capstone Brief and Research Addendum (post Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 9: Design Concept and Pre-Production</h2>

### Objectives

Module 9 objectives. By the end of this module, you will be able to:

- 9.1 Develop a capstone design concept and justify the choice of technology or interaction method (Course Competency 4)
- 9.2 Produce a pre-production package for your capstone (Course Competency 4)

### Overview

Pre-production is where you make your mistakes on paper. This week you develop your concept, justify your technology choice against alternatives, and produce the plans you will build from: flows, storyboards or state diagrams, an asset list, and a production schedule. You also start a weekly Build and AI-Use Log, which becomes part of your process book and helps you answer questions in your defense.

### Watch

- From brief to concept to pre-production: one capstone shown in game, sound, and app versions (14 minutes) [instructor to create]

### Read

- [How to be creative](https://faculty.washington.edu/ajko/books/design-methods/creative), *Design Methods*, Amy J. Ko, CC BY-ND 4.0 (15 minutes)
- [The Role of Animation and Motion in UX](https://www.nngroup.com/articles/animation-purpose-ux/), Nielsen Norman Group (10 minutes; animation and app design especially)
- Discipline starting points (15 minutes): game design, [Unity Essentials](https://learn.unity.com/pathway/unity-essentials); sound design, [Wwise 101](https://www.audiokinetic.com/en/courses/wwise101/) or [FMOD learning resources](https://www.fmod.com/learn); graphic design and digital media arts, [MindAR documentation](https://hiukim.github.io/mind-ar-js-doc/) or [model-viewer](https://modelviewer.dev/); app design, [Gemini Canvas help](https://support.google.com/gemini/answer/16047321); animation, [Twine](https://twinery.org/)

### Practice

**E10 Build and AI-Use Log 1 (Exercises, 5 points).** A short weekly entry: what you made, what broke, what you learned, hours spent, and every AI use (tool, purpose, what you kept, what you changed). Logs E10 to E14 use the same template [instructor to create].

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW15 Capstone Design Concept</h2>

This assignment measures Module Objective 9.1, which supports Course Competency 4.

### Objectives

- 9.1 Develop a capstone design concept and justify the choice of technology or interaction method.

### Overview

You will develop your concept and justify your technology choice with evidence.

### Instructions

1. Show at least two concept directions you considered and the one you chose.
2. Write a concept statement (150 words) and an experience description told from the persona’s point of view.
3. Present a look-and-feel or sound-and-feel reference board.
4. Justify your technology or interaction method against at least one alternative, citing user needs, accuracy, accessibility, bias, and ethics (update your PW12 matrix).
5. Post by Wednesday noon; submit with three critique comments by Thursday noon.

### What you produce in your discipline

| Discipline (examples) | Concept artifacts |
|---|---|
| Game design | Mechanic one-sheet, mood board, control scheme |
| Animation | Style frames, character sheet, branching outline |
| Sound design | Sonic palette (reference clips and timbres), cue list with intended meanings, spatial or adaptive concept |
| Graphic design | Identity and layout direction across touchpoints |
| App design | Style tile, key screen sketches |
| Digital media arts | Concept render or sketch in the real space, interaction model |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 9.1.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW16 Pre-Production Package</h2>

This assignment measures Module Objective 9.2, which supports Course Competency 4.

### Objectives

- 9.2 Produce a pre-production package for your capstone.

### Overview

You will assemble the plans you will build from.

### Instructions

1. Final flow in your medium’s notation (update PW10 or start fresh).
2. Storyboard, animatic plan, wireframes, or state diagram for the core experience.
3. Asset list (made, reused, AI-generated placeholder, or licensed), with licenses for reused assets.
4. Production schedule for Weeks 10 to 15, including two test rounds.
5. Accessibility plan: which guidelines you will meet and how.
6. Post by Saturday noon; submit with three critique comments by Sunday noon.

### What you produce in your discipline

| Discipline (examples) | Pre-production artifacts |
|---|---|
| Game design | Level or loop diagram, greybox plan, control map, asset list |
| Animation | Storyboard with branch map, animatic plan, asset list |
| Sound design | Adaptive-audio state diagram with parameters and transition rules, cue sheet (cue, trigger, meaning, loudness target), sound map for spatial projects, middleware or engine setup plan |
| Graphic design | Touchpoint map, comps plan, AR target images |
| App design | Wireflow, screen inventory, component list |
| Digital media arts | Floor plan, sensor and hardware plan, content map |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 9.2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 9 critique channel. Comment on risk: which part of a classmate’s plan is most likely to fail, and what is the fallback?

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> PW15 Capstone Design Concept (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> PW16 Pre-Production Package, E10 Build and AI-Use Log 1 (post Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 10: Prototype 1 and Test Round 1</h2>

### Objectives

Module 10 objectives. By the end of this module, you will be able to:

- 10.1 Design a low-fidelity prototype of your capstone’s core task or loop (Course Competency 5)
- 10.2 Synthesize findings from a usability test or playtest into prioritized issues (Course Competency 6)

### Overview

Your first capstone prototype should be fast and rough, and it should answer one question about your core task or loop. Then you test it with three to five people. Game students run a playtest (is it fun, is it learnable) alongside usability tasks (can players use the controls and HUD). Sound students run listening tests under controlled conditions. Everyone uses task-based testing, not “do you like it” questions.

### Audio testing protocol (sound and any audio-heavy project)

1. Participants use headphones unless the project is designed for speakers or open air; record which.
2. Play the build or files locally on the participant’s device, or in person. Do not judge audio quality through a video call.
3. Normalize loudness before testing so no cue is a surprise peak; tell participants how to stop playback.
4. Test meaning (can they identify what each cue means?), task (can they complete the task by ear?), and preference (A/B comparison) separately.
5. Record setup details in your notes (device, headphones, room noise).

### Watch

- Testing a rough prototype: a playtest, a listening test, and an app task test side by side (15 minutes) [instructor to create]

### Read

- [Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/), Nielsen Norman Group (10 minutes)
- [Thinking Aloud: The #1 Usability Tool](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/), Nielsen Norman Group (10 minutes)
- [Remote Usability Tests: Moderated and Unmoderated](https://www.nngroup.com/articles/remote-usability-tests/), Nielsen Norman Group (10 minutes)
- [Why You Only Need to Test with 5 Users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/), Nielsen Norman Group (8 minutes)
- [How to evaluate empirically](https://faculty.washington.edu/ajko/books/design-methods/empirical), *Design Methods*, Amy J. Ko, CC BY-ND 4.0 (15 minutes)

### Practice

**E11 Build and AI-Use Log 2 (Exercises, 5 points).** Same template as E10.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW17 Prototype 1</h2>

This assignment measures Module Objective 10.1, which supports Course Competency 5.

### Objectives

- 10.1 Design a low-fidelity prototype of your capstone’s core task or loop.

### Overview

You will build a rough prototype that answers one question about your core experience.

### Instructions

1. State the question this prototype answers (for example, “Can players learn the climb gesture without instructions?” or “Can listeners tell the danger cue from the reward cue?”).
2. Build the prototype at the lowest fidelity that can answer it.
3. Write the test plan for Test Round 1: tasks, success criteria, what you will observe, severity scale, and consent. Request early review if you want instructor feedback within 48 hours.
4. Post by Wednesday noon; submit with three critique comments by Thursday noon.

### What you produce in your discipline

| Discipline (examples) | Prototype 1 |
|---|---|
| Game design | Greybox of the core mechanic, playable with placeholder art |
| Animation | Animatic with working choice points (Twine or clickable video) |
| Sound design | Wizard-of-Oz soundboard driven live during a greybox or paper session, or a first FMOD or Wwise event set triggered by keys |
| Graphic design | Comps with a working QR or test AR trigger |
| App design | Clickable Figma prototype of the core task |
| Digital media arts | Mock installation in a room or a WebAR test scene |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 10.1.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW18 Test Round 1</h2>

This assignment measures Module Objective 10.2, which supports Course Competency 6.

### Objectives

- 10.2 Synthesize findings from a usability test or playtest into prioritized issues.

### Overview

You will test Prototype 1 with three to five people and turn what you see into a prioritized issue list.

### Instructions

1. Run your test plan with three to five participants (18 or older, consent obtained, not in this course).
2. Record observations by participant code: task, success or failure, time, quotes, and behavior.
3. Synthesize: group issues, rate severity (0 to 4), and rank the top five.
4. State what you will change in Prototype 2 and what you will leave alone, and why.
5. Post a summary by Saturday noon (no recordings or identifying details); submit with three critique comments by Sunday noon.

### What you produce in your discipline

| Discipline (examples) | Test focus |
|---|---|
| Game design | Playtest plus usability tasks on controls and HUD |
| Animation | Choice recognition and outcome prediction |
| Sound design | Listening test using the audio testing protocol: cue identification, eyes-closed task completion, A/B preference |
| Graphic design | In-context test (store shelf, hallway, desk) of the prompt and trigger |
| App design | Task completion and errors |
| Digital media arts | Approach, engage, and exit behavior |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 10.2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 10 critique channel. Comment on the test itself: were the tasks fair? Did the design or the test cause the problem?

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> PW17 Prototype 1 (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> PW18 Test Round 1, E11 Build and AI-Use Log 2 (post Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 11: Prototype 2 and Peer Review</h2>

### Objectives

Module 11 objectives. By the end of this module, you will be able to:

- 11.1 Design a mid-fidelity prototype that integrates your chosen technology or interaction method (Course Competency 5)
- 11.2 Analyze a classmate’s prototype using heuristic and accessibility review (Course Competency 1)

### Overview

Prototype 2 raises fidelity and proves the risky part: the technology spike. If your capstone depends on hand tracking, image-tracked AR, spatial audio, a voice model, or AI-generated code, this is the week you prove it works at a basic level, or switch to your fallback. You also review a classmate’s prototype in depth using the heuristics and accessibility guidelines from Weeks 2 and 3.

### Watch

- Technology spikes: how to prove the risky part in a day, and when to switch to the fallback (10 minutes) [instructor to create]

### Read

- Re-read [How to Conduct a Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/), Nielsen Norman Group (10 minutes)
- Re-read your discipline’s accessibility guideline set from Week 3 (15 minutes)
- [How to evaluate analytically](https://faculty.washington.edu/ajko/books/design-methods/analytical), *Design Methods*, Amy J. Ko, CC BY-ND 4.0 (15 minutes)

### Practice

**E12 Build and AI-Use Log 3 (Exercises, 5 points).** Same template as E10. Include the result of your technology spike.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW19 Prototype 2 with Technology Spike</h2>

This assignment measures Module Objective 11.1, which supports Course Competency 5.

### Objectives

- 11.1 Design a mid-fidelity prototype that integrates your chosen technology or interaction method.

### Overview

You will build a mid-fidelity prototype that fixes the top Test Round 1 issues and proves your chosen technology works.

### Instructions

1. Address the top issues from Test Round 1; list which ones and how.
2. Integrate your technology or interaction method at a basic working level (the spike).
3. If the spike fails, document what you tried, switch to your fallback, and say so in your post.
4. Share the prototype so a classmate can use it (build file, link, video walkthrough for headset-only projects, or audio files with instructions).
5. Post by Wednesday noon; submit with three critique comments by Thursday noon.

### What you produce in your discipline

| Discipline (examples) | Prototype 2 and spike |
|---|---|
| Game design | Mechanic with the new input working (hand tracking, voice, controller-free) |
| Animation | Interactive cut with real animation in key moments; AR placement working |
| Sound design | FMOD or Wwise events driven by game parameters in the Unity starter scene, or a Web Audio or Resonance Audio prototype with spatialized cues; earcon set implemented in a clickable prototype |
| Graphic design | Image-tracked AR working on the printed piece |
| App design | Coded or AI-assisted prototype of the core task running on a device |
| Digital media arts | Sensor or camera input triggering content |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 11.1.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW20 Peer Heuristic and Accessibility Review</h2>

This assignment measures Module Objective 11.2, which supports Course Competency 1.

### Objectives

- 11.2 Analyze a classmate’s prototype using heuristic and accessibility review.

### Overview

You will review one assigned classmate’s Prototype 2 in depth, preferably from another discipline. Your classmate will use your review in their revision plan.

### Instructions

1. Use your assigned classmate’s prototype for at least 20 minutes.
2. Complete a heuristic evaluation (at least six issues with severity ratings) and an accessibility check (at least six guidelines from WCAG 2.1 AA or their discipline’s set).
3. Write three strengths and three priority recommendations.
4. Post your review in your classmate’s Discord thread by Saturday noon; submit it in Canvas with three critique comments (on any reviews) by Sunday noon.

### What you produce in your discipline

The same review for every discipline. When you review a sound design project, use the heuristics-in-sound table from Week 2 and the audio testing protocol from Week 10.

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 11.2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 11 critique channel. Capstone check-in 2: the instructor reviews every technology spike and confirms the build plan or the switch to the fallback.

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> PW19 Prototype 2 with Technology Spike (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> PW20 Peer Heuristic and Accessibility Review, E12 Build and AI-Use Log 3 (post Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 12: Functional Build and Test Round 2</h2>

### Objectives

Module 12 objectives. By the end of this module, you will be able to:

- 12.1 Create a functional alpha build of your capstone’s core experience (Course Competency 7)
- 12.2 Synthesize findings from a second test round using task-based measures (Course Competency 6)

### Overview

The alpha build runs from start to finish for a first-time user, even if parts are rough. Then you test it with new participants. This is the busiest build week of the course; protect your time and use your fallback if you need it.

### Watch

- Getting to alpha: cutting scope without cutting the experience (8 minutes) [instructor to create]

### Read

- [System Usability Scale (SUS)](https://measuringu.com/sus/), MeasuringU, free to read (10 minutes)
- [Unmoderated User Tests](https://www.nngroup.com/articles/unmoderated-usability-testing/), Nielsen Norman Group (10 minutes; optional, for remote tests)

### Practice

**E13 Build and AI-Use Log 4 (Exercises, 5 points).** Same template as E10.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW21 Functional Build: Alpha</h2>

This assignment measures Module Objective 12.1, which supports Course Competency 7.

### Objectives

- 12.1 Create a functional alpha build of your capstone’s core experience.

### Overview

You will submit a build that a first-time user can run from start to finish.

### Instructions

1. Build the core experience end to end, meeting the definition of functional for your discipline in the Capstone Guide.
2. Record a 2-to-3-minute capture of someone other than you using it (with consent), or of yourself if no tester is available before the deadline.
3. List known issues and what you will fix before Test Round 2.
4. Post the capture by Wednesday noon; submit the build (a file or a Google Sites link) with three critique comments by Thursday noon.

### What you produce in your discipline

| Discipline (examples) | Alpha build |
|---|---|
| Game design | Playable vertical slice of one core loop |
| Animation | All branches playable end to end |
| Sound design | Adaptive audio system responding to state in a running build, a working audio UI, or a sonic AR walk running on a phone |
| Graphic design | AR or multi-touchpoint experience working with the printed piece |
| App design | App completing the core task on a device or browser |
| Digital media arts | Installation or WebAR guide responding to visitors without the designer operating it |

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 12.1.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW22 Test Round 2</h2>

This assignment measures Module Objective 12.2, which supports Course Competency 6.

### Objectives

- 12.2 Synthesize findings from a second test round using task-based measures.

### Overview

You will test the alpha build with three to five new participants and compare results with Test Round 1.

### Instructions

1. Update your test plan; keep at least one task identical to Round 1 so you can compare.
2. Test with three to five new participants (consent, 18 or older, not in this course). Add the SUS questionnaire or a discipline-appropriate measure (for example, cue identification rate for audio).
3. Record task success, time, errors, severity, and quotes by participant code.
4. Compare with Round 1 in a short table: what improved, what did not, what is new.
5. Post a summary by Saturday noon; submit with three critique comments by Sunday noon.

### What you produce in your discipline

Use the Test Round 1 focus for your discipline. Sound design students repeat the audio testing protocol and report cue identification rate and eyes-closed task completion against Round 1.

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 12.2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 12 critique channel. Comment on a classmate’s comparison table: is the improvement real, or did the test change?

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> PW21 Functional Build: Alpha (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> PW22 Test Round 2, E13 Build and AI-Use Log 4 (post Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 13: Revision</h2>

### Objectives

Module 13 objectives. By the end of this module, you will be able to:

- 13.1 Synthesize user testing and peer feedback into a prioritized revision plan (Course Competency 6)
- 13.2 Implement design revisions and document each change with evidence (Course Competency 6)

### Overview

You now have two rounds of testing, a peer review, and weeks of critique. This week you decide what matters most, make the changes, and freeze features. After Sunday, you only fix bugs, record, and document.

### Watch

- Prioritizing revisions with an impact and effort matrix (8 minutes) [instructor to create]

### Read

- [Using Prioritization Matrices to Inform UX Decisions](https://www.nngroup.com/articles/prioritization-matrices/), Nielsen Norman Group (12 minutes)

### Practice

**E14 Build and AI-Use Log 5 (Exercises, 5 points).** Same template as E10.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW23 Synthesis and Revision Plan</h2>

This assignment measures Module Objective 13.1, which supports Course Competency 6.

### Objectives

- 13.1 Synthesize user testing and peer feedback into a prioritized revision plan.

### Overview

You will combine every source of feedback into one prioritized plan.

### Instructions

1. List every finding from Test Rounds 1 and 2, the peer review, and critique comments, with its source.
2. Place each on an impact and effort matrix.
3. Choose what you will change this week and what you will not, with reasons.
4. Post by Wednesday noon; submit with three critique comments by Thursday noon.

### What you produce in your discipline

The same plan for every discipline.

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 13.1.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW24 Beta Build and Change Log</h2>

This assignment measures Module Objective 13.2, which supports Course Competency 6.

### Objectives

- 13.2 Implement design revisions and document each change with evidence.

### Overview

You will implement your plan and show before and after evidence for each change.

### Instructions

1. Implement the planned changes.
2. Write a change log: change, the finding that caused it, before and after (screenshots, clips, or audio), and how you checked it worked.
3. Declare feature freeze.
4. Post by Saturday noon; submit the beta build and change log with three critique comments by Sunday noon.

### What you produce in your discipline

The same change log for every discipline. Sound design students include before and after audio clips, loudness measurements where relevant, and updated state diagrams.

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 13.2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 13 critique channel. Capstone check-in 3: the instructor reviews every revision plan and flags any risk to the Week 15 presentation.

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> PW23 Synthesis and Revision Plan (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> PW24 Beta Build and Change Log, E14 Build and AI-Use Log 5 (post Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 14: Presentation and Portfolio</h2>

### Objectives

Module 14 objectives. By the end of this module, you will be able to:

- 14.1 Construct a presentation that explains design decisions with research and test evidence (Course Competency 7)
- 14.2 Produce a release candidate build and a process book (Course Competency 7)

### Overview

Your recorded presentation is both a class presentation and a portfolio piece you can send to employers. It should tell the story of a problem, the people you designed for, what you tried, what testing taught you, and what you built. This week you rehearse, get feedback, finish the build, and assemble your process book.

### Presentation structure (8 to 10 minutes)

1. The user and the problem (with research evidence)
2. The concept and why this technology or interaction method
3. Two or three key decisions and the evidence behind each
4. What testing changed (before and after)
5. A live or recorded demonstration of the functional build
6. What you would do next

### Watch

- Presenting UX work for portfolios and interviews (12 minutes) [instructor to create]

### Read

- [Making Audio and Video Media Accessible](https://www.w3.org/WAI/media/av/), W3C WAI: captions and transcripts sections (10 minutes)
- [OBS Studio](https://obsproject.com/) quick start, or Adobe Premiere Pro speech-to-text captions [verify link] (10 minutes)

### Practice

**E15 Caption and Accessibility Check (Exercises, 5 points).** Caption your rehearsal recording, check contrast on every slide with the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/), and confirm that any sound essential to understanding your demo is described in captions or narration.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW25 Presentation Rehearsal</h2>

This assignment measures Module Objective 14.1, which supports Course Competency 7.

### Objectives

- 14.1 Construct a presentation that explains design decisions with research and test evidence.

### Overview

You will post a rehearsal recording and get targeted feedback before the final.

### Instructions

1. Record a full rehearsal (8 to 10 minutes) following the presentation structure.
2. Ask your critique group two specific questions you want feedback on.
3. Post by Wednesday noon; submit with three critique comments by Thursday noon. In your comments, answer the presenter’s questions and ask one question a hiring manager might ask.

### What you produce in your discipline

The same presentation for every discipline. Headset-only and audio projects include a captured demonstration (headset view recording, or a screen recording with system audio and captions).

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 14.1.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW26 Release Candidate and Process Book</h2>

This assignment measures Module Objective 14.2, which supports Course Competency 7.

### Objectives

- 14.2 Produce a release candidate build and a process book.

### Overview

You will submit the build you intend to present and the process book that documents how you got there.

### Instructions

1. Release candidate: bug fixes only since feature freeze. Include run instructions so another person can use it.
2. Process book (PDF or web page, about 10 to 20 pages): brief, research, concept, pre-production, prototypes, test rounds, peer review, change log, Build and AI-Use Logs, accessibility statement, and asset and license list.
3. Post a link by Saturday noon; submit with three critique comments by Sunday noon.

### What you produce in your discipline

The same process book for every discipline; the build follows the functional definition for your discipline.

### Rubric

Process Work Rubric, 10 points. Every criterion evaluates Objective 14.2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 14 critique channel. Rehearsal feedback first; then process book comments.

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> PW25 Presentation Rehearsal, E15 Caption and Accessibility Check (post Wednesday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> PW26 Release Candidate and Process Book (post Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">Week 15: Presentation and Defense</h2>

### Objectives

Module 15 objectives. By the end of this module, you will be able to:

- 15.1 Present and defend an original, functional capstone project to peers using research and test evidence (Course Competency 7)
- 15.2 Critique classmates’ capstone projects with evidence-based questions grounded in UX principles (Course Competency 1)

### Overview

This week you present your capstone to the class and defend it. You post your recorded presentation on Wednesday, classmates and the instructor ask questions by Thursday, you record or write your defense responses by Saturday, and you submit the final package on Sunday. Keep the final recording; it is built to show employers.

### Watch

- Your classmates’ presentations (at least three, plus any posted in your critique group)

### Read

- Review the Capstone Final and Defense rubric (section 6) (10 minutes)

### Practice

**E16 Final Reflection (Exercises, 10 points).** 400 to 600 words or a 4-to-6-minute recording: how your understanding of UX in your discipline changed, the decision you are proudest of and the one you would make differently, and how you used AI and where you chose not to. Due with the Capstone Final.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Due in Canvas:</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Assessment

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">PW27 Capstone Presentation to the Class</h2>

This assignment measures Module Objectives 15.1 and 15.2, which support Course Competencies 7 and 1.

### Objectives

- 15.1 Present and defend an original, functional capstone project to peers using research and test evidence.
- 15.2 Critique classmates’ capstone projects with evidence-based questions grounded in UX principles.

### Overview

You will post your final recorded presentation and ask defense questions of three classmates.

### Instructions

1. Post your final presentation (8 to 10 minutes, captioned) to the Week 15 presentation channel by Wednesday noon.
2. Watch at least three classmates’ presentations, at least one from another discipline. Post one defense question on each by Thursday noon. A good defense question asks about evidence or trade-offs (“What did testing show that made you drop the voice option?”), not opinion.
3. Submit your presentation link in Canvas by Thursday noon.

### What you produce in your discipline

The same presentation for every discipline.

### Rubric

Process Work Rubric, 10 points. Criteria: Step requirements (Objective 15.1), 4; Quality of reasoning (Objective 15.1), 3; Process evidence and AI-use log (Objective 15.1), 1; Critique: three defense questions (Objective 15.2), 2.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Wednesday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Thursday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Friday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

<h2 style="background-color: #7a5080; color: #FFFFFF; padding: 12px 16px;">P2 Capstone Final and Defense</h2>

This project evidences all seven course competencies:

1. Analyze interactive experiences using foundational UX principles.
2. Create a project brief based on user research.
3. Evaluate various technologies and interaction methods to meet user needs.
4. Develop a design concept using a pre-production process.
5. Design a prototype of an interactive experience.
6. Synthesize user testing and peer feedback into design iterations.
7. Create an original, functional interactive project that integrates user research, testing and an emerging technology or interaction method.

This assignment measures Module Objectives 8.2, 9.1, 9.2, 10.1, 11.1, 13.1, 15.1 and 15.2, which support Course Competencies 1 to 7.

### Objectives

- 8.2 Create a capstone project brief supported by a research addendum.
- 9.1 Develop a capstone design concept and justify the choice of technology or interaction method.
- 9.2 Produce a pre-production package for your capstone.
- 10.1 Design a low-fidelity prototype of your capstone’s core task or loop.
- 11.1 Design a mid-fidelity prototype that integrates your chosen technology or interaction method.
- 13.1 Synthesize user testing and peer feedback into a prioritized revision plan.
- 15.1 Present and defend an original, functional capstone project to peers using research and test evidence.
- 15.2 Critique classmates’ capstone projects with evidence-based questions grounded in UX principles.

### Overview

You will answer every question you received, then submit your final capstone package.

### Instructions

1. Defense responses: by Saturday noon, post in your presentation thread a recorded response (3 to 5 minutes) or a written response answering every question you received, including the instructor’s. Cite evidence from your process book.
2. Leave three closing comments on classmates’ defense responses by Sunday noon.
3. Submit in Canvas by Sunday noon:
   - Final build (a file or a Google Sites link) with run instructions
   - Final recorded presentation (captioned), revised if you choose, for your portfolio
   - Defense responses (link or file)
   - Final process book
   - Final AI-use log
4. The instructor may request a short follow-up conversation if the build or defense leaves a question about authorship or understanding.

### What you produce in your discipline

See the Capstone Guide for what “functional” means in your discipline.

### Rubric

Capstone Final and Defense Rubric (section 6), 30 points, one criterion per competency: Course Competency 1 (Objective 15.2), 4; Course Competency 2 (Objective 8.2), 4; Course Competency 3 (Objective 9.1), 4; Course Competency 4 (Objective 9.2), 4; Course Competency 5 (Objectives 10.1, 11.1), 4; Course Competency 6 (Objective 13.1), 5; Course Competency 7 (Objective 15.1), 5.

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Post to Discord for critique:</strong> Saturday, 12:00 p.m. Arizona time<br><strong>Due in Canvas (work plus three critique comments):</strong> Sunday, 12:00 p.m. Arizona time<br><strong>Hard close:</strong> Monday, 12:00 p.m. Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

### Critique / Discussion

Week 15 presentation channel. Questions by Thursday noon; defense responses by Saturday noon; closing comments by Sunday noon.

### Due

<p style="border: 2px solid #7a5080; padding: 12px 16px;"><strong>Thursday deadline:</strong> PW27 Capstone Presentation to the Class (post presentation Wednesday noon; three defense questions by Thursday noon). Hard close Friday, 12:00 p.m.<br><strong>Sunday deadline:</strong> P2 Capstone Final and Defense, E16 Final Reflection (post defense responses Saturday noon). Hard close Monday, 12:00 p.m.<br>All times are noon, Arizona time. Work submitted after the deadline and before the hard close loses 10%. Nothing is accepted after the hard close.</p>

---

## 11. Accessibility, UDL, research ethics and consent, and AI-use disclosure

### Course accessibility (WCAG 2.1 AA, OSCQR)

- Every instructor video is captioned and has a transcript. Every image on Canvas pages has alternative text; decorative images are marked decorative.
- Title boxes and date boxes meet WCAG 2.1 AA contrast (white on `#7a5080` in the public build; white on `#CB3338` at GCC export) [verify contrast ratios with the WebAIM checker at build].
- Headings follow a logical order (h2 title box, h3 sections). Tables have header rows. Links describe their destination.
- Discord is the critique space, but nothing graded happens only in Discord: every post is also submitted in Canvas, and a student who cannot use Discord may post critique in a Canvas discussion mirror [instructor to create] with no penalty.
- Students using assistive technology are not required to use any tool that does not work with it; the instructor approves an equivalent.
- Student work is held to accessibility standards too: captions on presentations, contrast on slides, captions or visual alternatives for meaningful sound, and the accessibility plan in the capstone brief.

### Universal Design for Learning ([CAST UDL Guidelines](https://udlguidelines.cast.org/) [verify license])

| UDL principle | How the course applies it |
|---|---|
| Multiple means of engagement | Students choose their discipline, medium, problem area, and technology; mixed-discipline critique builds belonging; the rhythm is predictable every week |
| Multiple means of representation | Every module has an instructor video, text readings, and worked examples in more than one discipline; sound concepts are shown in audio, visual, and written form |
| Multiple means of action and expression | Written or recorded options for teardowns, critiques, reflections, and defense responses; discipline-specific artifacts for every step |

### Research ethics and consent (user testing with real people)

The course includes interviews, observations, surveys, and usability tests with real people. These are classroom learning activities, not research intended to produce generalizable knowledge. The instructor confirms with the district’s institutional review process whether any approval or exemption is needed before the course runs [verify with district IRB]. Until confirmed, these rules apply.

1. **Adults only.** Participants are 18 or older. Students do not recruit minors, including younger siblings or classmates under 18.
2. **No one in this course.** Classmates in this course give critique, not test data, so testing reflects first-time users.
3. **Informed consent every time.** Before each session the student reads or shares the course consent script: purpose, what is recorded, how notes are de-identified, how long data is kept, that participation is voluntary, and that the participant may stop at any time without explanation. Consent is written or recorded verbally.
4. **Minimal data.** Collect only what the research question needs. No health, financial, immigration, or other sensitive information. No identifying details in notes; participants become P1, P2, P3.
5. **Recordings.** Only with explicit consent. Stored only in the student’s district Google account, never posted to Discord, and deleted at the end of the course. Clips used in a presentation require separate consent and must not show faces or names unless the participant agrees in writing.
6. **Vulnerable groups and accessibility research.** Students who want to test with people with disabilities, older adults, or other groups who may face extra risk discuss their plan with the instructor first, design sessions to be comfortable and accessible, and never ask participants to disclose a diagnosis.
7. **Audio safety.** Normalize loudness before listening tests and tell participants how to stop playback; avoid sudden peaks.
8. **XR safety.** Headset sessions are short (under ten minutes), seated or in a cleared space, and stop at the first sign of discomfort or motion sickness.
9. **AI and participant data.** De-identified notes may be organized in Gemini Notebook under the district account. Identifiable participant data never goes into any AI tool. AI is never used to generate participants, quotes, or results.
10. **Honesty.** Reporting a test that did not happen, or inventing data, is academic misconduct.

### AI-use disclosure rules

1. **Log every use.** Each submission includes an AI-use log: tool, what you asked it to do, what you kept, what you changed, and why. “None” is a valid entry.
2. **You first, then AI.** For research synthesis, problem statements, concept sketches, and test plans, you produce your own first version before asking AI for critique or variations. Submit both versions.
3. **Never a substitute for your thinking.** AI may not write your critique comments, reflections, design rationales, or defense answers, and may not stand in for research participants (see section 1).
4. **AI-generated code and assets are allowed and disclosed.** Functional prototypes built with Gemini Canvas or similar tools count as your work when the design, flows, and decisions are yours, the log shows your prompts and revisions, and you can explain how the build works in your defense.
5. **Label AI-generated assets** in the process book and asset list. Respect licenses and do not generate content that imitates a living artist’s identifiable style or a real person’s voice without permission.
6. **Use district tools for course data.** Use Gemini and Adobe under district accounts first. If you use another AI tool, never paste participant data or classmates’ work into it.
7. **Evaluate AI as a design material.** When your project includes an AI-driven interaction, test it for accuracy, accessibility, and bias (Week 7 method) and report what you found.
8. **Undisclosed AI use** is handled under the college academic integrity policy. When the instructor has a question about authorship, the first step is a conversation, not an accusation; the defense format is designed to make that conversation natural.

---

## 12. Open questions for Michelle and the team (most important first)

1. **Research approval.** Do user interviews and usability tests with adults outside the course need any review or exemption under the district’s institutional review process, or can the course consent script cover them? This affects Weeks 4, 7, 8, 10 and 12 for every college that offers the course.
2. **Grading weights.** This draft uses the build standard defaults (Process Work 40, Projects 35, Exercises 25) and adds a 30-point Studio Project at Week 7 so the Projects group holds two items. Keep the Studio Project as a Project, or move it into Process Work and leave the Capstone Final as the only Project?
3. **Competency 3 and the capstone.** The team asked whether technology evaluation can be met by analysis alone. This draft says yes for Competency 3 (Week 7 evaluation, Week 9 justification) and requires every student to build with an emerging technology or interaction method in the capstone (Competency 7). Does the team agree that a student whose spike fails may present a fallback that uses an emerging interaction method at a lower technical level (for example Wizard-of-Oz voice)?
4. **AVC190 on-ramp.** Is the Weeks 1 to 3 extension path (same assignments, non-web subject, one extra discipline guideline set) enough for students who completed AVC190, or should they receive a separate track or credit for Weeks 1 to 3?
5. **Gemini timing.** Students receive district Gemini in January 2027. If the first offering starts earlier, which AI tool do students use for Gemini Canvas tasks, and is Google AI Studio available to students under district accounts?
6. **How other programs offer the course.** Elective, cross-listed, or required in each program? This affects prerequisites (for example whether MUC122 alone prepares sound design students for the UX writing load) and whether discipline faculty co-teach or provide starter projects.
7. **Starter projects.** Who builds the instructor-provided starter projects (a Unity scene with FMOD or Wwise for sound students, a WebAR template, a Twine template), and who maintains them each term?
8. **Middleware and device access.** Confirm FMOD and Wwise education licensing terms, headset availability for VR projects (loaner program or desktop-only XR), and whether online students without a capable computer can complete engine-based builds.
9. **Discord mirror.** Is a Canvas discussion mirror required at every college for students who cannot or will not use Discord?
10. **Firefly and Adobe products.** Confirm Firefly access for online students and the current Adobe app list in the student plan (several Adobe pages could not be checked automatically and are marked [verify]).
11. **Recorded presentation privacy.** Students may post their recorded presentation publicly for portfolios. Confirm that presentations include no participant faces or voices without written consent, and whether the college needs a release for student work shown in course examples.
12. **Instructor-created media.** About 20 short instructor videos and 6 templates are marked [instructor to create]. Should these be produced once and shared across colleges, and by whom?
25 Oct 2026: course.html moved onto the shared build (tools/course-build/build.py); Module 0 comes from canvas/_shared/module0.html.
