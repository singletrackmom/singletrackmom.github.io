# Mines Flagship Portfolio Project — "Reading the Forces"
### A beautifully designed, competency-based free-body-diagram assessment (with an XR vision)

_Built July 3, 2026 from a deep research pass. This is the single home for this project. Working titles: "Reading the Forces," "See the Forces," "Free Body," "Force Field."_

---

## The decision — topic + format (and why it's bulletproof)

**Topic:** freshman **forces / free-body diagrams (FBDs)** — the core skill of Physics I *and* the first step in intro engineering / statics. Universal, so it reads as "typical," and the audience (instructional designers) cares about the *design*, not exotic content.

**Why this is bulletproof (research-backed):**
- **Force Concept Inventory** (Hestenes, Wells & Swackhamer 1992): ~80% can *state* Newton's 3rd law at course start; **<15% understand it by the end** of traditional instruction.
- **Hake 1998** (6,542 students): traditional lecture normalized gain **g≈0.23** vs. interactive engagement **g≈0.48** — passive lecture + MCQ barely repairs misconceptions.
- **Rosengrant, Van Heuvelen & Etkina 2009** (PRST-PER): students who *construct* a correct FBD solve problems far better; **handing them a completed FBD did not help and actually impeded performance**. → Multiple-choice / "pick the right diagram" tests *recognition*, not the generative skill. Construct-and-justify is the authentic assessment.
- **The gap (confirmed by survey):** free/OER tools split into *simulate-and-observe* (PhET, oPhysics), *explain* (OpenStax, Khan), *check-the-final-diagram* (Physics Classroom — binary correctness only), and *MCQ concept inventories* (FCI/FMCE/RFCI). **None** is a well-designed, competency-based performance assessment where a student builds an FBD from a novel scenario, **justifies each force**, and gets **reasoning-level feedback** against a rubric. That is the unfilled niche — and a genuine OER contribution.

**Format:** a **self-authored, visually stunning WEB interactive** as the centerpiece (proves it's *your* design + craft, buildable in 3 weeks, hostable on your site) **+ a storyboarded Unity/XR "immersive vision"** as the forward-looking layer (cutting-edge signal, student-built later, low risk). For an ID hiring team, flashy tech with thin pedagogy backfires; a rigorously designed, gorgeous piece you clearly authored wins.

---

## The student experience

Scenario-based, mastery-oriented. The student gets a real situation — a crate on a ramp, a rock climber on a rope, a sign hanging from two cables, a bridge pin joint — and:
1. **Builds the FBD** by placing and labeling force vectors on an illustrated scene (direction + relative magnitude).
2. **Names the agent** of each force (what object causes it) and its Newton's-3rd-law partner.
3. **Justifies** why each force is included/excluded.
4. **Predicts the motion**, then the scene **animates the consequence** — the crate slides or tips if a force is wrong/missing. Immediate, visual, diagnostic feedback.
5. An **AI "lab partner/TA"** probes the reasoning ("you drew friction pointing uphill — why?") and the transcript becomes evidence.
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

**UDL / accessibility (CAST):** the construct (FBD competency) stays fixed; the *means of expression* flexes — annotate the diagram + written rationale, or a screencast/oral defense. Sufficient contrast, meaning never carried by color alone, keyboard operable, alt text, captions.

---

## The visual / craft plan (the WOW — your Adobe showcase)

**Craft bar to hit (benchmarks from the research):**
- **Ciechanowski (ciechanow.ski)** — near-white canvas, thin precise strokes, *text tinted to match the object it names*, one-idea-per-widget progressive build, everything draggable with a gentle Undo.
- **PhET Forces & Motion** — force-vector arrows that **scale in real time** with a **net-force sum** and numeric readout (the FBD core interaction).
- **Matter.js** — grabbable objects with real momentum; a clean **wireframe "forces" overlay** aesthetic.
- **3Blue1Brown** — **draw-on construction** and smooth **morph transitions** so nothing just "appears."
- **Kurzgesagt** — one cohesive high-contrast palette, flat geometric vector art, relentless consistency.

**What you make in Adobe:** the illustrated scenarios (Illustrator vector scenes + objects), the force-vector + UI system / design language, an **After Effects hero animation** (draw-on forces; the crate sliding when a force is missed) that doubles as the trailer, the **storyboards** for the full experience, and a style frame / mini design system.

---

## The XR / Unity "vision" layer (cutting-edge, low risk)

Storyboard the same assessment as an **immersive XR experience** — walk around the structure, reach out and *place* force vectors in 3D, watch the body respond — and cut a **short After Effects animatic** of it. Frame it as the roadmap for the campus XR lab; your student builds the real Unity/WebXR version later. This shows you can *design* for immersive learning (and storyboard it — a listed job requirement) without gambling the 3-week demo on a heavy build.

---

## Delivery / tech
- **Web** (HTML/CSS/JS; Matter.js or hand-coded vectors for the force feel), vibe-coded, hostable on singletrackmom.github.io. WebXR-capable path optional.
- **Capture a 60–90s narrated demo video** as the portfolio centerpiece; keep the live interactive + rubric as proof it works and assesses.
- Package the design as an **OER** (open license) — fills the documented gap.

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
- **Week 1 — Design:** competencies + rubric; pick 1 hero scenario (crate on a ramp) + 2 more; script the misconception traps; style frame + palette; storyboard the flow. Optional 15-min sanity check with any physics/engineering friend (FBDs are trivial for a SME to validate — no exotic-science risk).
- **Week 2 — Build + illustrate:** Illustrator scenes/UI; build the interactive slice end-to-end for the hero scenario; wire the AI lab partner; produce the After Effects hero animation.
- **Week 3 — Vision + ship:** XR-vision storyboard + animatic; record the demo video; write the case-study page (problem → evidence → design → how it assesses → alignment → accessibility → XR vision → OER); accessibility pass.

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
- **Scenario scenes** — crate on a ramp, climber on a rope, hanging sign on two cables, bridge pin joint (reusable components).
- **Force-vector system** — arrows per force type (weight, normal, tension, friction, applied), color-coded + labeled. The visual heart.
- **UI** — the force palette (drag arrows from here), control panel, live net-force readout/meter, AI lab-partner chat bubble, feedback/rubric panel.
- **Style frame / design system** (palette, type, icons) + **storyboard frames**.

Animate in **After Effects**: import the Illustrator layers; forces draw on, the crate slides/tips when a force is wrong, the net-force arrow resolves → the 60–90s hero/trailer.

Interactivity: export **SVG/PNG** from Illustrator → vibe-coded into the clickable web sim (Claude wires it). **You draw; Claude wires. No coding by Michelle.**

3D / Unity: **not needed for the centerpiece.** Real 3D = Blender/Unity models (a different skill; the student's later build). The "XR vision" shown to reviewers is **faked as 2.5D in Illustrator + After Effects** — immersive look, no engine. Learn Unity later as a growth goal; keep it OFF the 3-week critical path.
