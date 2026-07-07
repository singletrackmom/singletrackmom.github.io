# Simulation as Assessment · the PROCESS (PRIVATE)

**For Michelle and Claire. Not linked on the public site.** This is the repeatable process for how we would design and build the flagship simulation, tuned to the Mines Online Learning Experience Designer role. It pairs with `_research-dossier.md` (the field scan) and `mines-flagship-project.md` (the earlier decision log). Built July 7, 2026.

**DISCOVERY PHASE, subject NOT chosen yet.** We are still looking at what is out there before committing to a subject. The steps, theory, rubric, accessibility, and build path below are the durable process and apply to ANY engineering or physical-science subject (engineering, physics, chemistry, earth and energy science, data science). The data-science predictive-maintenance scenario further down is ONE worked example to make the process concrete; it is illustrative, not a decision. Swap the subject skin and the process holds.

---

## Goal, Audience, Process (labeled, per the rule)

**Goal.** Build one visually impressive, browser-based simulation in which a graduate learner performs authentic data-science work for a real industry decision, and is assessed on the reasoning, not a final answer a chatbot could hand back. It has to hold up as a rigorous instructional-design artifact (adult-learning theory, accessibility, Bloom's-aligned outcomes, a real competency rubric) AND look like a professional tool, not a web page.

**Audience.** Two at once. The real user is a fully online graduate learner in a Mines-type program (Data Science, Business Analytics, Engineering and Technology Management) who never sets foot on campus. The evaluating audience is the Mines Online design team reading it as portfolio evidence that Michelle can design and build examinable, AI-resistant, accessible online assessment.

**Process (how it works).** The learner is dropped into an industry scenario with a messy real dataset and a decision a stakeholder needs. They frame the question, explore the data, choose a method, catch the trap built into the data, make a call, and defend it to an AI stakeholder who pushes back. The scene then plays the consequence of their decision. The graded artifact is the trace of what they did plus the defense transcript, scored against a competency rubric with mastery thresholds.

---

## The scenario (authentic task, Mines-relevant industry)

**Skin: predictive maintenance for an energy or mining operation.** This keeps data science tied to an industry Mines Online actually teaches (Data Science, plus the energy and engineering programs). The learner is the data scientist on call.

**The setup.** A facility (wind farm, processing plant, or mine hoist) streams sensor data. Something is starting to fail. Leadership wants a recommendation by end of shift: which asset to pull for maintenance, and can we keep running the rest through the weekend. Pulling an asset costs money and downtime; a wrong "keep running" call risks a failure.

**The built-in trap (this is what makes it un-fakeable).** The obvious signal is misleading. Options to design in, pick one or rotate them for per-learner variation:
- **Data leakage:** a feature that looks predictive is actually a proxy for the maintenance log itself, so a naive model looks perfect and is useless in production.
- **Simpson's paradox:** the aggregate trend reverses inside the real operating subgroups.
- **A misleading metric:** high accuracy hides that the model never catches the rare failure that matters (class imbalance), so accuracy is the wrong scoreboard.
- **Distribution shift:** the training data was a calm season; the weekend forecast is not.

**What the learner produces.** A recommendation with a stated confidence, the evidence for it, the risk they are accepting, and what would change their mind. Not a single number, a defensible judgment.

**Per-learner personalization (the anti-cheat + andragogy move).** Each run seeds different data (Capsim "snowflake" pattern), a different trap, and a stakeholder who reacts to that learner's specific choices. No two runs are the same, so a shared answer is worthless, and each learner gets a scenario that fits their level.

---

## Backward design (Wiggins and McTighe: outcomes, then evidence, then activity)

**Stage 1, desired results.** By the end, the learner can frame an ambiguous business problem as an analyzable question, interrogate data for validity before trusting it, select and justify a method against the decision context, diagnose the trap, and defend a recommendation under uncertainty.

**Stage 2, acceptable evidence.** The interaction log (what they inspected, in what order, what they ruled out) plus the recorded defense against the AI stakeholder. Process evidence, scored to a rubric, not a right-answer key.

**Stage 3, learning plan.** The simulation itself, scaffolded, replayable, with feedback at each decision point.

---

## Measurable outcomes across Bloom's taxonomy (real verbs, all six levels)

1. **Remember.** Identify the relevant variables, the target, and the operating subgroups in the dataset.
2. **Understand.** Explain what each candidate signal represents and how it was generated.
3. **Apply.** Use an appropriate exploratory and modeling method for a rare-event, mixed-quality dataset.
4. **Analyze.** Differentiate real signal from artifact; detect leakage, imbalance, paradox, or shift.
5. **Evaluate.** Judge the recommendation against cost, risk, and consequence, and defend it under stakeholder challenge.
6. **Create.** Construct a decision brief: recommendation, confidence, evidence, accepted risk, and the condition that would change the call.

Each outcome is written as a measurable performance and maps to a rubric row below. This is the "aligned outcomes and assessment" the OLED role asks for.

---

## Competency rubric (analytic, CBE thresholds, AAC&U VALUE style)

Scores process and justification, not just the final pick. Mastery equals every criterion at 3 or above (competency thresholds, not averaged to a letter).

| Criterion | 4 Mastery | 3 Proficient | 2 Developing | 1 Emerging |
|---|---|---|---|---|
| 1. Problem framing (turn an ambiguous ask into an analyzable question with the right target and constraints) | | | | |
| 2. Data validity and interrogation (check provenance, quality, and fitness before trusting the data) | | | | |
| 3. Method selection and justification (fit the method to a rare-event, imperfect, decision-driving context) | | | | |
| 4. Trap diagnosis (detect and name leakage, imbalance, paradox, or shift, with evidence) | | | | |
| 5. Reasoning under uncertainty and defense (justify the call, state confidence and risk, respond to challenge) | | | | |
| 6. Communication and accessibility of the decision brief (clear, audience-fit, UDL-compliant artifact) | | | | |

The rubric is published to the learner up front (transparency, per the Oxford AI-patient finding). Rows 4 and 5 are the AI-resistant core: they grade the judgment chain over this run's specific evidence, which a chatbot cannot supply.

---

## Adult-learning theory (Knowles andragogy, mapped to design decisions)

- **Need to know.** The scenario opens with the stakes (money, downtime, risk), so the learner sees why the work matters before doing it.
- **Self-concept and autonomy.** No fixed path. The learner decides what to inspect and in what order; the sim never says "go here next."
- **Experience as a resource.** Learners bring their own domain read; the debrief connects their moves to prior knowledge rather than lecturing.
- **Readiness to learn.** The task is a real on-the-job decision, the kind of problem a working professional actually faces.
- **Problem-centered orientation.** The whole assessment is one authentic problem, not a set of decontextualized items.
- **Internal motivation.** Consequence, not points: the scene plays out the result of the learner's call, which is more motivating than a grade.

This is the "learning theory and adult, inclusive design" the OLED role names.

---

## Accessibility and inclusive design (UDL and WCAG 2.1 AA, built in from the first draft)

- **UDL (CAST).** The competency stays fixed (defensible data reasoning); the means flex. A learner can annotate the data and write the rationale, record a spoken defense, or type it. Multiple representations of every data view (chart, table, and plain-language summary).
- **WCAG 2.1 AA.** Sufficient contrast, meaning never carried by color alone (critical for a data viz, so encode with shape and label too), full keyboard operability, alt text on every scene and chart, captions and transcripts on any audio or animation, respects reduced-motion preferences.
- **From anywhere, with or without VR.** The core runs in any browser on a normal connection (low-bandwidth path, no headset required). An optional WebXR layer lets a learner walk the facility in 3D, but it is strictly additive; the full assessment is completable in 2D. This directly answers "doable from anywhere."
- **Low-stakes accommodations.** Unlimited practice runs before the graded attempt; extended time is a non-issue because the clock is narrative, not punitive.

---

## AI's role (scenario engine, simulated stakeholder, examiner, with a human in the loop)

- **Scenario engine.** Generates the per-learner dataset, trap, and framing over an API.
- **Simulated stakeholder.** Plays the operations manager who reacts to the learner's choices and pushes back ("why this model, what happens when the weekend load spikes, what would change your mind"). This is the AVC183 "AI as client" pattern, turned into assessment.
- **Examiner (assist, not autopilot).** Applies the published rubric to the transcript and interaction log to draft a score and evidence-linked feedback. A human confirms, because AI scoring of judgment and communication is still the weakest link (the honest Oxford finding). Name that human-in-the-loop as a deliberate design choice.

---

## Learning analytics (the OLED requirement, and the assessment substrate)

Every action is logged: what the learner inspected, the order, what they ruled out, time-to-decision, revisions, and the defense transcript. That log is both the score's evidence and a dashboard signal (where do most learners miss the trap, which prompt from the stakeholder produces the best reasoning). Score the trace, not a bolted-on quiz.

---

## The visual concept (why it does NOT look like a web page)

The design language is an operations console, a decision room, not a form with fields. Solid colors only, from a defined palette, never gradients (hard rule). Craft bar set by Ciechanowski (precise, draggable, text tinted to the object it names), ASU Dreamscape Learn (a named, story-driven world), 3Blue1Brown (draw-on construction, smooth morphs so nothing just appears), and Kurzgesagt (one cohesive high-contrast flat-vector palette).

- **The scene.** A full-bleed illustrated facility (wind farm, plant, or hoist) with live sensor panels the learner drives. Data does not sit in a table; it flows through the scene.
- **The stakeholder.** A character who appears and reacts on screen, so the defense feels like a conversation in a room, not a text box.
- **The consequence.** When the learner commits, the scene animates the outcome: the pulled asset, or the failure the model missed. Immediate, visual, diagnostic.
- **The artifact.** The learner leaves with a clean decision brief they could show an employer, which doubles as the "outlasts the semester" keepsake.

The 60 to 90 second narrated demo of this is the portfolio centerpiece; the live interactive plus the rubric is the proof it actually assesses.

---

## Build path (what Michelle actually makes, and with what)

- **Craft and scenes:** Illustrator vector facility, data-panel and console UI system, an After Effects hero animation (data flowing, the consequence playing out) that doubles as the trailer, plus storyboards and a style frame. This is the Adobe and storyboarding evidence the OLED role wants.
- **Interactive:** a browser build in HTML, CSS, and vanilla JS, vibe-coded with Claude Design and AI coding help. You design and build the interface and interaction; AI handles the reasoning parts.
- **Reasoning:** the stakeholder, the examiner, and the scenario generation run through an AI model over its API.
- **Optional later:** a WebXR "walk the facility" layer, storyboarded now as the immersive vision, built by a student or collaborator later. Off the critical path.
- **Release as OER** (open license) and package it to embed in an LMS (Canvas), both explicit OLED requirements.

---

## Mines OLED requirement map (check every box)

- Aligned outcomes and assessment, coherent design: backward design, Bloom's outcomes, competency rubric.
- Learning theory, adult and inclusive design: Knowles andragogy, UDL, CBE, published rubric.
- Learning analytics: the interaction log and dashboard signal.
- OER and copyright: released under an open license.
- Build within an LMS: embeddable web object, packageable for Canvas.
- Visual design, storyboarding, Adobe CC: the whole craft plan.
- Instructional copy and video or audio scripts: the hero-animation script and demo narration.
- ADA and accessibility: UDL and WCAG 2.1 AA from the first draft.
- Manage complex projects independently: designed and authored solo.
- AI-assisted development: the AI scenario engine, stakeholder, and examiner, human-in-the-loop.
- STEM familiarity (preferred): graduate data science on an energy or engineering problem.

---

## What we are actually trying to get done in 3 weeks

**The deliverable is a proof-of-concept demo video for the portfolio website, backed by an early research prototype. Not a finished tool, not production.** The video is the thing people see; the prototype only has to work well enough to film a convincing 60 to 90 second walkthrough of ONE scenario, one trap, one stakeholder exchange, one consequence. Label it plainly as an early research prototype. Everything below is scoped to hit that, nothing more.

- **Week 1, design.** Lock outcomes and rubric, choose one hero scenario and one trap, script the stakeholder, build the style frame and palette, storyboard the flow. A 20-minute sanity check with a data-science friend or Claire validates the domain.
- **Week 2, build and illustrate.** Illustrator scenes and console UI, the interactive slice end to end for the hero scenario, wire the AI stakeholder and examiner, produce the After Effects hero animation.
- **Week 3, ship.** Record the 60 to 90 second demo, write the case-study page (problem, evidence, design, how it assesses, alignment, accessibility, OER), accessibility pass, and the optional WebXR storyboard as the vision layer.

---

## Open questions for Claire and for the next work session

1. Industry skin: wind-farm sensors, processing-plant, or mine-hoist predictive maintenance? Which reads as most credibly Mines and most visual?
2. Which trap leads (leakage is the most defensible and the most teachable; imbalance is the most real-world).
3. How far to take the AI examiner before the human takes over.
4. Do we build the 2D console first and storyboard the VR, or does Claire think Mines would want the immersive layer shown live.
5. Next tangible step: I can produce a visual style frame or a clickable console mockup (Claude Design or an SVG concept) so you have the impressive visual in hand to react to.
