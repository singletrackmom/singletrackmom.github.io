# Mines Flagship Portfolio Project, "Reading the Forces"
### A beautifully designed, competency-based free-body-diagram assessment (with an XR vision)

_Built July 3, 2026 from a deep research pass. This is the single home for this project. Working titles: "Reading the Forces," "See the Forces," "Free Body," "Force Field."_

---

## The decision, topic + format (and why it's bulletproof)

**Topic:** freshman **forces / free-body diagrams (FBDs)**, the core skill of Physics I *and* the first step in intro engineering / statics. Universal, so it reads as "typical," and the audience (instructional designers) cares about the *design*, not exotic content.

**Why this is bulletproof (research-backed):**
- **Force Concept Inventory** (Hestenes, Wells & Swackhamer 1992): ~80% can *state* Newton's 3rd law at course start; **<15% understand it by the end** of traditional instruction.
- **Hake 1998** (6,542 students): traditional lecture normalized gain **g≈0.23** vs. interactive engagement **g≈0.48**, passive lecture + MCQ barely repairs misconceptions.
- **Rosengrant, Van Heuvelen & Etkina 2009** (PRST-PER): students who *construct* a correct FBD solve problems far better; **handing them a completed FBD did not help and actually impeded performance**. → Multiple-choice / "pick the right diagram" tests *recognition*, not the generative skill. Construct-and-justify is the authentic assessment.
- **The gap (confirmed by survey):** free/OER tools split into *simulate-and-observe* (PhET, oPhysics), *explain* (OpenStax, Khan), *check-the-final-diagram* (Physics Classroom, binary correctness only), and *MCQ concept inventories* (FCI/FMCE/RFCI). **None** is a well-designed, competency-based performance assessment where a student builds an FBD from a novel scenario, **justifies each force**, and gets **reasoning-level feedback** against a rubric. That is the unfilled niche, and a genuine OER contribution.

**Format:** a **self-authored, visually stunning WEB interactive** as the centerpiece (proves it's *your* design + craft, buildable in 3 weeks, hostable on your site) **+ a storyboarded Unity/XR "immersive vision"** as the forward-looking layer (cutting-edge signal, student-built later, low risk). For an ID hiring team, flashy tech with thin pedagogy backfires; a rigorously designed, gorgeous piece you clearly authored wins.

---

## The student experience

Scenario-based, mastery-oriented. The student gets a real situation, a crate on a ramp, a rock climber on a rope, a sign hanging from two cables, a bridge pin joint, and:
1. **Builds the FBD** by placing and labeling force vectors on an illustrated scene (direction + relative magnitude).
2. **Names the agent** of each force (what object causes it) and its Newton's-3rd-law partner.
3. **Justifies** why each force is included/excluded.
4. **Predicts the motion**, then the scene **animates the consequence**, the crate slides or tips if a force is wrong/missing. Immediate, visual, diagnostic feedback.
5. An **AI "lab partner/TA"** probes the reasoning ("you drew friction pointing uphill, why?") and the transcript becomes evidence.
6. The completed artifact + a short reflection is saved to the student's **PLE / ePortfolio**; they iterate across the term (process portfolio). Mastery thresholds, not a letter grade (CBE).

---

## Learning design (the ID showcase)

**Backward design (Wiggins & McTighe):** outcomes → evidence → activity. **Measurable competencies** (Bloom verbs): *identify* the interacting bodies; *construct* a conventionally-correct FBD; *justify* each force as an interaction; *evaluate* the result for physical reasonableness.

**Competency rubric (analytic, AAC&U-VALUE-style; scores process + justification, not just the drawing):**

| Criterion | 4 Mastery | 3 Proficient | 2 Developing | 1 Emerging |
|---|---|---|---|---|
| 1. System & context (isolate the body, state assumptions) | | | | |
| 2. Force identification & interaction reasoning *(process)* | | | | |
| 3. Diagram construction & conventions (direction, relative magnitude, point of application, labels) | | | | |
| 4. Justification of inclusion/exclusion & direction *(justification)* | | | | |
| 5. Strategy & self-evaluation (predict motion, check reasonableness) *(process)* | | | | |
| 6. Communication & accessibility of the artifact (UDL) | | | | |

Mastery = all criteria ≥ 3 (CBE thresholds, not averaged to a grade).

**Misconceptions weaponized as traps (FCI-based; each is a selectable path that fails instructively):** "motion implies a net force"; "normal force always = weight"; treating N and mg as an action-reaction pair; inventing a "force of motion" / forgetting tension/normal/friction; friction pointing the wrong way; drawing a force *and* its x/y components as three separate forces; "bigger object pushes harder" (N3L).

**UDL / accessibility (CAST):** the construct (FBD competency) stays fixed; the *means of expression* flexes, annotate the diagram + written rationale, or a screencast/oral defense. Sufficient contrast, meaning never carried by color alone, keyboard operable, alt text, captions.

---

## The visual / craft plan (the WOW, your Adobe showcase)

**Craft bar to hit (benchmarks from the research):**
- **Ciechanowski (ciechanow.ski)**, near-white canvas, thin precise strokes, *text tinted to match the object it names*, one-idea-per-widget progressive build, everything draggable with a gentle Undo.
- **PhET Forces & Motion**, force-vector arrows that **scale in real time** with a **net-force sum** and numeric readout (the FBD core interaction).
- **Matter.js**, grabbable objects with real momentum; a clean **wireframe "forces" overlay** aesthetic.
- **3Blue1Brown**, **draw-on construction** and smooth **morph transitions** so nothing just "appears."
- **Kurzgesagt**, one cohesive high-contrast palette, flat geometric vector art, relentless consistency.

**What you make in Adobe:** the illustrated scenarios (Illustrator vector scenes + objects), the force-vector + UI system / design language, an **After Effects hero animation** (draw-on forces; the crate sliding when a force is missed) that doubles as the trailer, the **storyboards** for the full experience, and a style frame / mini design system.

---

## The XR / Unity "vision" layer (cutting-edge, low risk)

Storyboard the same assessment as an **immersive XR experience**, walk around the structure, reach out and *place* force vectors in 3D, watch the body respond, and cut a **short After Effects animatic** of it. Frame it as the roadmap for the campus XR lab; your student builds the real Unity/WebXR version later. This shows you can *design* for immersive learning (and storyboard it, a listed job requirement) without gambling the 3-week demo on a heavy build.

---

## Delivery / tech
- **Web** (HTML/CSS/JS; Matter.js or hand-coded vectors for the force feel), vibe-coded, hostable on singletrackmom.github.io. WebXR-capable path optional.
- **Capture a 60–90s narrated demo video** as the portfolio centerpiece; keep the live interactive + rubric as proof it works and assesses.
- Package the design as an **OER** (open license), fills the documented gap.

---

## Maps to EVERY Mines OLED requirement
- **Aligned outcomes/assessment + coherent design** → backward-designed competencies → rubric → task.
- **Learning theory / adult & inclusive design** → PER evidence base, UDL, CBE, ePortfolio.
- **Learning analytics** → the interaction log + AI transcript as evidence.
- **OER / copyright** → released as an openly-licensed learning object.
- **Build within an LMS** → embeddable web object; can package for Canvas.
- **Visual design, storyboarding, Adobe CC** → the whole craft plan (Illustrator + After Effects + storyboards).
- **Instructional copy + video/audio scripts** → the hero-animation script + demo narration.
- **ADA / accessibility** → the UDL/WCAG pass, built in from the first draft.
- **Manage complex projects independently** → you design + author it solo.
- **AI-assisted development** → the AI lab-partner examiner, human-in-the-loop.
- **STEM familiarity (preferred)** → freshman physics/engineering mechanics.

---

## 3-week build
- **Week 1, Design:** competencies + rubric; pick 1 hero scenario (crate on a ramp) + 2 more; script the misconception traps; style frame + palette; storyboard the flow. Optional 15-min sanity check with any physics/engineering friend (FBDs are trivial for a SME to validate, no exotic-science risk).
- **Week 2, Build + illustrate:** Illustrator scenes/UI; build the interactive slice end-to-end for the hero scenario; wire the AI lab partner; produce the After Effects hero animation.
- **Week 3, Vision + ship:** XR-vision storyboard + animatic; record the demo video; write the case-study page (problem → evidence → design → how it assesses → alignment → accessibility → XR vision → OER); accessibility pass.

---

## Key sources
- FCI: Hestenes, Wells & Swackhamer 1992 (https://davidhestenes.net/modeling/R&E/FCI.PDF); Hestenes 1998 "<15% N3L" (https://en.wikipedia.org/wiki/Force_Concept_Inventory)
- Hake 1998, 6,000-student interactive-engagement study: https://web.mit.edu/jrankin/www/Active_Learning/hake_active_phys.pdf
- Rosengrant, Van Heuvelen & Etkina 2009, "Do students use and understand free-body diagrams?": https://www.researchgate.net/publication/26624673_Do_students_use_and_understand_free-body_diagrams
- Tool/gap survey: PhET (https://phet.colorado.edu/en/simulations/forces-and-motion-basics), Physics Classroom FBD Interactive (https://www.physicsclassroom.com/interactive/newtons-laws/free-body-diagrams), OpenStax Univ. Physics §5.7 (https://openstax.org/books/university-physics-volume-1/pages/5-7-drawing-free-body-diagrams), PhysPort FCI/FMCE/RFCI (https://www.physport.org)
- Design frameworks: Backward design/UbD; Wiggins authentic assessment (https://eric.ed.gov/?id=ed328611); AAC&U VALUE rubrics (https://www.aacu.org/value/rubrics); UDL/CAST (https://udlguidelines.cast.org/); CBE (https://library.educause.edu/topics/teaching-and-learning/competency-based-education-cbe)
- Craft benchmarks: Ciechanowski (https://ciechanow.ski/), 3Blue1Brown (https://www.3blue1brown.com/), Matter.js (https://brm.io/matter-js/), Kurzgesagt style (https://midlibrary.io/styles/kurzgesagt)

---

## What you actually draw + the production pipeline
**Tools: Illustrator (draw) + After Effects (motion). No 3D modeling, no Unity required.**

Draw in **Illustrator** (flat vector):
- **Scenario scenes**, crate on a ramp, climber on a rope, hanging sign on two cables, bridge pin joint (reusable components).
- **Force-vector system**, arrows per force type (weight, normal, tension, friction, applied), color-coded + labeled. The visual heart.
- **UI**, the force palette (drag arrows from here), control panel, live net-force readout/meter, AI lab-partner chat bubble, feedback/rubric panel.
- **Style frame / design system** (palette, type, icons) + **storyboard frames**.

Animate in **After Effects**: import the Illustrator layers; forces draw on, the crate slides/tips when a force is wrong, the net-force arrow resolves → the 60–90s hero/trailer.

Interactivity: export **SVG/PNG** from Illustrator → vibe-coded into the clickable web sim (Claude wires it). **You draw; Claude wires. No coding by Michelle.**

3D / Unity: **not needed for the centerpiece.** Real 3D = Blender/Unity models (a different skill; the student's later build). The "XR vision" shown to reviewers is **faked as 2.5D in Illustrator + After Effects** (immersive look, no engine). Learn Unity later as a growth goal; keep it OFF the 3-week critical path.

---

## Project-selection decision (July 4, 2026): the climate-science OER idea

**Context.** Michelle raised a new idea: build openly-licensed (Creative Commons) climate-science OER, possibly a game or simulation, inspired by NOAA scientists who stood up an independent site with dated, non-interactive teaching toolkits after the official government resources went offline. Question asked: is this a good use of scarce time for the Mines application, and is it relevant to beginning college-level science?

**Decision: do NOT make the climate OER the Mines flagship, and do not start it now. Finish ONE of the two existing flagships instead.** The reasoning, honestly:

1. **Opportunity cost.** Two flagships (this FBD project and "Water from the Moon") are already deeply researched and scoped to 3 weeks. The Mines review opens ~July 16, across a camping week and a vacation week. A third flagship this late risks three half-finished pieces instead of one shipped one.
2. **Audience mismatch.** Climate teaching toolkits serve K-12 and informal-science educators. Mines hires for rigorous assessment design aimed at selective engineering undergrads and grad students. Michelle flagged it herself as "below the Mines level." A portfolio piece is read as evidence of the audience you design for; this one points away from the job.
3. **Domain-credibility risk.** Michelle is not a climate scientist. The existing flagships use trivially-validatable STEM content plus a 20-minute SME check. Climate content is neither trivial to validate nor politically neutral, and it competes with the actual NOAA experts on their turf, where her real edge (learning design + AI assessment) is invisible.
4. **Signal weight.** "I build OER for fun because I care about the climate" is a values garnish, not a flagship. Best hours should go to the entrée reviewers hire on.
5. **Scope.** "Make a game or simulation" is unbounded, and educational games fail badly and slowly. A mediocre climate game hurts more than it helps.

**Where the climate idea CAN live (later, reframed, her call).** The transferable asset is not climate content; it is a **reusable simulation-assessment pattern** demonstrated on a climate scenario and released as OER, where the METHOD is the star and climate is the demo skin. Fits the post-Mines AI-futurist positioning as a second data point that the method generalizes beyond engineering. Aim at least at intro-college level; the career value is in the write-up, not the artifact. Highest-leverage climate-cause version: contribute an assessment layer to the NOAA-scientists' existing OER effort rather than build a competing toolkit. Phase 2, after the Mines materials ship, budgeted honestly as a values project.

**Still open (Michelle to decide):** which of the two flagships to finish for Mines, "Reading the Forces" (FBD) or "Water from the Moon" (lunar ISRU). Both are ready to build. Pick one, ship it, do not split the hours. **See the July 4 catalog check below, which reframes this decision.**

---

## Mines Online catalog check (July 4, 2026), this reframes the project choice

**The role is "Online Learning Experience Designer" at Mines Online, which is ENTIRELY graduate and professional. There is no undergraduate / gen-ed audience.** That single fact changes the analysis. Verified against mines.edu (online.mines.edu/programs/, gradprograms.mines.edu, catalog.mines.edu), July 2026.

**What Mines Online actually offers (online / hybrid):**
- **Engineering & manufacturing:** Additive Manufacturing (MS, cert), Mechanical Engineering (MS), FEA Professional (cert), Electrical Engineering (MS + certs in Information & Systems Science, Microwave, Power & Energy Systems), Underground Construction & Tunnel Engineering (cert).
- **Data / computing / cyber (the biggest cluster):** Data Science (MS + 5 certs: Computer Science, Earth Resources, Foundations, Statistical Learning, Petroleum Data Analytics), Computer Science (MS), Cybersecurity (cert).
- **Management / business / product:** Engineering & Technology Management (MS, ranked US News #17 online, the marquee program), Business Analytics (cert), Product Management (cert), Mining Industry Management (MS).
- **Energy / earth / geoscience:** Carbon Capture Utilization & Storage (MS, cert), Chemical Engineering Processes in Energy Transitions (cert), Energy Geophysics (cert), GIS & Geoinformatics (MS, cert).
- **Space:** Space Resources (MS non-thesis and graduate certificate are ONLINE-ONLY; PhD is online + on-campus). SPRS courses; ISRU, space systems engineering, economics/policy. Director: Angel Abbud-Madrid.
- No general aerospace degree online; Robotics and Quantum are on-campus, not online.

**Dominant online programs (where the ID actually spends time):** Data Science + Computer Science/Cybersecurity, and Engineering & Technology Management. Then core engineering (EE, Mechanical, Additive) and energy-transition (CCUS, GIS). Mining/petroleum show up as niche certs. **Space Resources is a small, prestige, interdisciplinary program, not a volume driver.**

**Honest verdict on the two concepts:**
- **"Water from the Moon" (ISRU):** your worry was half-right. The subject is NOT off-target, Space Resources is a real ONLINE Mines program and a famous one. But it is tiny and niche. Leading with it risks reading as "designed for the coolest program, not the ones we staff." It undersells breadth.
- **"Reading the Forces" (FBD):** the bigger problem. Free-body diagrams are freshman/intro-physics. **Mines Online has no undergraduate audience.** As the centerpiece it signals intro-undergrad teaching, exactly the wrong level. It only works if reframed hard as a reusable graduate-level competency-assessment PATTERN, with the physics as incidental.

**Revised recommendation (build for a flagship online program, make the METHOD the star):**
1. **Primary piece: anchor to a dominant program.** Best options: a **Data Science / analytics scenario assessment** (maps to the largest cluster) or an **Engineering & Technology Management decision simulation** (the #17 marquee, adult-professional case style). Same simulation-as-assessment method already designed, applied to a subject Mines Online actually runs at volume, pitched at graduate/professional level.
2. **Optional secondary showpiece: keep the Space Resources ISRU sim, reframed** as "the same reusable simulation-assessment pattern applied to your signature program." That turns its niche-ness into proof the method travels, instead of a liability.
3. **Do not center the freshman forces piece.** Wrong level for a grad/professional online shop.

**Decision needed from Michelle:** pick the primary subject, Data Science analytics case or ETM decision simulation. The build mechanics (outcomes -> scenario -> rubric -> AI examiner -> illustrated UI -> accessibility -> demo video) are unchanged from the plans above; only the subject skin changes.

---

## What Mines Online courses actually look like + the "show and tell" angle (July 4, 2026)

Researched from Mines' own pages (olfaculty.mines.edu, econbus.mines.edu, gradprograms.mines.edu, catalog.mines.edu, trefnycenter.mines.edu).

**Format (documented):** Canvas (elearning.mines.edu) + DesignPLUS/CidiLabs. Asynchronous **8-week** terms, ~15-20 hrs/week per 3-credit course. Assessment baseline = assignments + quizzes + discussions + exams, with a heavy emphasis on **real-dataset projects and video presentations** (DSCI503, DSCI570, DSCI576 are all project-based; ETM "many courses culminate in team projects rather than final exams"). The inside of a live DS/ETM course is NOT publicly viewable; this is inferred from official process + catalog pages (strong, but not the same as seeing a shell).

**Simulations?** No public evidence Mines Online DS/ETM courses use pedagogical simulations, virtual decision-sims, or scenario-based auto-graded assessment. ("Simulation" in course titles like EBGN528 or PEGN513 means subject-matter modeling, not learning-design simulation, do not conflate.) So a polished simulation-as-assessment piece would genuinely be new to what they show.

**Michelle's hypothesis, honestly:** half right, half wrong.
- Right: assessment likely tops out at video + quizzes + projects; no visible simulation-as-assessment.
- Wrong: these are NOT faculty-uploaded-and-left courses. Mines has a mature in-house operation, the **Trefny Innovative Instruction Center** (10+ yrs, includes assessment experts), and the very role she wants, **Online Learning Experience Designer (OLED)**, guides faculty through a **16-week course build** (MODLs Canvas course, Foundations of Curriculum Design prerequisite, an approved Online Course Design Guide / course map before an OLED is assigned), plus the **HIVE** multimedia studio for video. Design is in-house, not an OPM (Noodle appears to be marketing/recruitment only, unconfirmed on scope).

**Strategic frame (important): extend, do NOT indict.** Lead with "Mines already runs a strong OLED/Trefny build process; here is the next rung, examinable, AI-resistant simulation-as-assessment." Speak their vocabulary in the interview: OLED, MODLs, FoCD, Online Course Design Guide, HIVE, DesignPLUS. Build the demo to **plug into Canvas** (the way MobLab/Labster do), and it is smart to ASK to see a sample MODL/course shell, that is a strong interview question and gets ground truth.

**Best target course to prototype against:** DS = **DSCI503 Advanced Data Science** (already project-based, real datasets, easy to convert its project into a scenario/case). ETM = **EBGN525 Business Analytics** or **EBGN560 Decision Analytics** (natural fit for a decision simulation).

**Models to study (viewable examples of simulation/scenario assessment):**
- Data science: DataCamp Signal (adaptive skill checks), DataCamp Professional Certification (proctored live-coding + human-graded case), DataCamp Projects (scenario-framed real-dataset tasks).
- Engineering management / business: Harvard Business Analytics Simulation via Forio (act as an executive on evolving data), Harvard Business Impact sims (Everest, Balanced Scorecard, Beer Game), MobLab (browser decision games, gradebook syncs to Canvas).
- Structural model for LMS-integrated auto-graded checks: Labster (virtual labs with embedded quiz gating, Canvas-compatible).
