# Immersive & AI Simulation for Assessment — Learning Plan + Research

_Captured July 2, 2026. Head-start prep for the EDUCAUSE Immersive & Experiential Learning symposium, and a plan to turn the campus XR lab into a career differentiator._

## Why this matters (the career thesis)

The "future of assessment" conversation (see the WGU **Evolving Assessments in the Age of AI** panel) is moving toward **authentic, simulation-based, AI-mediated assessment** instead of tests and discussion boards. Michelle already believes this and says it on her About page.

The opening: campus has a **new XR lab that is underused** and nobody quite knows what to do with it. If Michelle pairs the XR lab + AI to build **simulation-based assessments**, she owns a rare, *demonstrable* capability at exactly the frontier that WGU-type roles (Future of Education Strategist / AI Innovator) hire for. Her own words: "if I were actually doing this work I'd get the WGU job right now."

**Goal:** get a visible prototype + short case study up on the portfolio within ~1 month, so it strengthens the WGU application (and similar roles) while they're live.

## The workshop (the head-start target)

**EDUCAUSE Symposium — Immersive and Experiential Learning in Online Environments.** Aug 10 & 12, 2026, 12:00–3:30 p.m. ET, online. It will:
- Frame the landscape of immersive/experiential learning (trends, research, examples).
- Cover design principles + pedagogy centering **learner experience, accessibility, and assessment alignment**.
- Show how to **evaluate impact**, integrate immersive practice into curricula, and build institutional capacity.

Show up with a point of view, sharp questions, and a candidate project already sketched (below), so you extract maximum value and network as someone who is *building*, not just attending.

## What to learn (skill map)

1. **XR fundamentals** — VR / AR / MR / XR concepts; headset vs **WebXR** (runs in a browser); and critically, *when immersion actually improves learning* vs. when it's overkill. (Pedagogy first, tech second — that's your edge.)
2. **Build path / tools**
   - **A-Frame (WebXR)** — HTML-like framework for 3D/VR/AR scenes in the browser. Closest to how you already build (HTML/JS + Claude API), and web-based means shareable and self-hostable on your portfolio. **Recommended starting point.**
   - **Unity** — the dominant engine; "no programming" WebXR courses exist; heavier lift, headset-oriented.
   - **Unreal** — high-fidelity, professional training sims; overkill to start.
   - **No-code**: Minsar and similar (AR/VR, exports to WebXR).
3. **AI + simulation** — generative AI powering **adaptive, improvisational** scenarios (not pre-scripted branches): AI characters/role-play, real-time feedback, adaptive difficulty, "virtual client/patient/stakeholder." This is where your Claude-building skill is a direct advantage.
4. **Simulation-based assessment design** — start from **learning objectives**, build an **authentic scenario** that mirrors real work, learner applies skills, capture **evidence of competency**; map every XR/AI activity to **specific competencies** (not bolted-on novelty); design authentic assessment that stays valid even when students have AI.
5. **Evaluation** — how to measure whether the simulation actually improved learning (impact, not just engagement). Note the **AIMS** framework (AI-Integrated Method for Simulation) for evaluating AI chatbot simulations.

## The fast win (you may already be doing this)

Your **AVC 183 branding course already uses an AI-simulated client** — students design against an AI that role-plays the client. **That is already a simulation-based assessment.** The quickest, most credible project is to **formalize and extend that** into a documented simulation-assessment prototype:

- A browser-based **AI role-play scenario** (Claude API + a simple interface): the student navigates a simulated client/stakeholder, and performance is scored against a **rubric** tied to outcomes. No headset required — ships fast, self-hosts on the portfolio like your other tools.
- **Then** add an immersive layer: a simple **A-Frame / WebXR** 3D environment the scenario plays out in, viewable in the browser and on a headset in the XR lab.

**Vehicle:** the new **UX course (AVC 2xx, working files in `canvas/avc2xx/`)** won't be live for years, so it's a safe sandbox to design a simulation-based assessment module end to end and document the design (outcomes → scenario → rubric → immersive layer).

## One-month plan

- **Now → Aug 10:** read the primers below; lock the project (recommend: formalize the AI-simulated-client branching scenario as a simulation-assessment prototype); sketch the design (outcomes, scenario, rubric).
- **Aug 10 & 12:** attend the symposium with the project in hand; ask targeted questions on assessment alignment + evaluating impact; network.
- **Aug → +1 month:** build v1 (browser AI scenario + rubric), record a 60–90s demo, write a one-page case study, put it on the portfolio and link from the About "AI-powered simulation" line.
- **Later:** add the WebXR/immersive layer in the XR lab; consider a conference talk (this is exactly the kind of thing OLC / EDUCAUSE / ASU+GSV want).

## How it connects to the positioning

- Directly backs the About line: "AI-powered simulation … where assessment is going … learning to build immersive simulations for assessment in our new campus XR lab."
- The differentiator: not *talking* about future assessment — *building* it, with a lab most people can't access. That is the WGU "AI Innovator" story with receipts.

## Background reading (primers before Aug 10)

- Simulation trends in higher ed (2026): https://www.magicedtech.com/blogs/simulation-trends-for-2026-why-u-s-higher-ed-is-entering-its-infrastructure-moment/
- Adaptive XR + AI immersive learning (2026 overview): https://www.creote.com/blogs/adaptive-xr-training-ai-immersive-learning-2026/
- AI + XR integrations (medical ed, transferable principles): https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1740557/full
- XR + AI for remote STEM education and assessment: https://arxiv.org/pdf/2509.03812
- GenAI-enhanced VR simulation for teacher education (usability + instructional utility): https://www.mdpi.com/2227-7102/15/8/997
- Simulation-based assessment method (design basics): https://coursensu.com/methods/simulation-based-assessment
- AIMS evaluation framework for AI chatbot simulations: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12389130/
- Build tools: WebXR/Unity/Unreal course (U-Michigan, Coursera): https://www.coursera.org/learn/develop-augmented-virtual-mixed-extended-reality-applications-webxr-unity-unreal ; A-Frame (WebXR): https://aframe.io ; curated XR dev guide: https://github.com/authorTom/ultimate-XR-dev-guide

## Reminder
Don't overstate on the public site: this is a direction you're **learning and building toward**, not finished work — until a prototype ships. Then it becomes proof.

---

## FLAGSHIP CONCEPT — "Water from the Moon": a lunar ISRU experiment as the final (illustrated web/XR)

**One-line pitch:** Instead of a multiple-choice final, the student becomes a mission specialist at the lunar South Pole and runs an in-situ resource utilization (ISRU) experiment — extract water/oxygen from regolith, hit a mission yield target under a power/time budget, interpret the telemetry, and defend the decisions to an AI "Mission Control." The assessment IS the simulation.

**Why it fits Mines (strongly):** maps to Mines Online's **Space Resources** program (SPRS 501 Fundamentals, SPRS 508 Regolith Properties & Processing, SPRS 509 Space Robotics) and the **Center for Space Resources** ISRU work + Moon/Mars vacuum-chamber labs. Frontier and on-brand, not a gimmick.

**Student experience (the task):**
1. **Briefing** — mission goal (produce X liters water / Y kg oxygen for the habitat) with constraints: limited power, limited time/battery, limited regolith batches.
2. **Set up** — choose parameters: reactor temperature, batch size, process (e.g., hydrogen reduction vs. molten-regolith electrolysis — simplified), power allocation.
3. **Run** — watch telemetry: yield curve, power draw, temperature, elapsed time.
4. **Read the data** — did yield hit the target? at what efficiency?
5. **Diagnose + adjust** — if short, figure out why (too little power? wrong temp? poor batch?) and re-run within budget.
6. **Justify** — report to Mission Control (AI), which probes the reasoning ("why raise temp instead of batch size?").

**Measurable outcomes:** (1) explain the basic ISRU pathway to water/oxygen from lunar regolith; (2) choose experiment parameters appropriate to a resource goal + constraints; (3) interpret data (yield vs. power/temp/time) to evaluate success; (4) diagnose why a result fell short and propose an evidence-based adjustment; (5) justify decisions under resource constraints.

**Rubric (replaces MCQ) — 4 criteria × Emerging/Developing/Proficient/Exemplary:** Experiment design · Data interpretation · Diagnosis & iteration · Justification. Evidence = the parameter/telemetry log + the AI Mission-Control transcript. Score the *reasoning under follow-up* — AI-cheat-resistant, human-in-the-loop (instructor reviews flagged runs).

**What Michelle draws (the Adobe showcase, folded in):** the lunar South Pole surface + habitat, the ISRU reactor/apparatus, a control panel with gauges (power, temp, yield), the yield-vs-time data plot, and the Mission Control comms UI. Illustrated 2.5D scene in Illustrator, made interactive on the web (vibe-coded). This piece doubles as the "shows Adobe skills" artifact.

**Delivery (no goggles required):** MVP = illustrated web 2.5D/3D in the browser (runs on any laptop, hostable on the site); WebXR-capable for immersion later; full VR = the vision. Capture a 60–90s narrated video as the portfolio "trailer," paired with the live slice + rubric as proof.

**Accessibility:** captions, data not carried by color alone, keyboard/non-VR path, alt text, readable contrast.

**Science guardrails (verify with SME):** keep the model simplified but directionally correct — more energy → more yield up to a point; regolith water content caps it; power budget is the real constraint. This is exactly what a SME should sanity-check.

**Questions for Sian / Madisen (~20-min SME review):**
1. Is the ISRU framing (water/oxygen from South Pole regolith) accurate enough for a teaching sim? Any glaring errors?
2. Which 3–4 parameters would a real specialist actually trade off (temperature, power, batch size, method)?
3. A believable mission yield target + a realistic failure mode a student should reason about?
4. What does a strong vs. weak justification to Mission Control sound like?
5. OK to reference Sian / her Mars-habitat + geology work as inspiration and credibility?

**Build split:** Michelle = outcomes, task flow, rubric, AI-Mission-Control prompt, all illustration/UI, accessibility. Student = web interactivity/3D. SME (Sian via Madisen; materials-PhD friend as backup) = science plausibility.

**3-week plan:** Wk1 — lock scenario + outcomes + rubric, sketch the scene, send SME note. Wk2 — illustrate the scene/UI + vibe-code the interactive slice + wire AI Mission Control. Wk3 — record the demo video + write the case-study page.

**Backup concepts (if the space path stalls):** (a) materials/additive "ship it or scrap it" XR — SME = MTB materials-PhD friend, maps to Mines Additive Manufacturing; (b) geology XR outcrop/core interpretation — form & defend a geologic history, fills the documented 3D subsurface-reasoning gap.

---

## VERDICT (after deep research): is this a good, credible project?

**Yes — with precision.** Two things the research settled:
- **The gap is real.** Existing lunar/space sims are either *rigorous-but-not-assessed* (NASA Moon Trek, Astromaterials 3D, JSC VR geology training) or *gamified-but-scientifically-shallow* (Surviving Mars, Astroneer, KSP, ESA's IMPACT). Nobody has combined **ISRU process fidelity + embedded, validated assessment + undergrad/early-pro pedagogy**. That's the white space.
- **Simulation-as-assessment is a serious, established field** — not fringe. Credible precedents: Body Interact and Oxford Medical Simulation (virtual patients scored on reasoning), Osso VR / PrecisionOS / Mimic MScore (VR procedures with objective, benchmarked scoring), Labster (STEM labs graded on process), and Valerie Shute's "stealth assessment" (FSU) as the academic backbone; EDUCAUSE flags immersive-with-feedback assessment as an emerging priority.

**Graphic / storyboard references to draw from:** ESA **IMPACT** (best match — polished stylized lunar-base ISRU pipeline), **Surviving Mars** (AAA habitat-management UI), **Astroneer** (approachable stylized extraction), and for photoreal data: NASA **Moon Trek**, **Eyes on the Solar System**, **Astromaterials 3D**. For the assessment UI: **Body Interact** and **Osso VR**.

---

## SME BRIEF — written in the voice of the (role-played) PhD engineering professor
*Frame: I'm a Mines faculty member who teaches lunar ISRU / space resources and I want a real assessment for my course. This is the assignment I'd hand my instructional designer. It's also your homework so you don't say anything elementary to actual PhDs — every number below is sourced in the research pass.*

### The teaching problem
My students can recite "there's water at the poles" and "you can make oxygen from regolith," and a multiple-choice exam measures exactly that — recall — which AI now makes trivially cheatable. What they CAN'T do, and what the field actually demands, is reason about the systems tradeoff: **a resource being *present* is not the same as *accessible* or *economic*, and ENERGY — not chemistry — is the binding constraint.** I want an assessment that makes students make and defend a real resource-strategy decision under realistic constraints, so I can see their *reasoning*, not their memory.

### The competency I'm assessing (judgment, not facts)
A student who gets it can: (1) distinguish the forms of lunar water/oxygen and tie each to location + temperature; (2) pick an extraction strategy appropriate to the goal and site — and reject the wrong ones; (3) reason quantitatively about the **energy budget and duty cycle**; (4) interpret result data, diagnose a shortfall, and iterate; (5) defend the decision under questioning and revise when a premise is challenged.

### The scenario
"You are the ISRU lead for an Artemis surface base. Mission need: e.g., 1,000 kg O₂/yr for life support, or LOX/LH₂ propellant. Given a site, a power source, and a budget — choose your resource + method, set parameters, run it, read the telemetry, and defend your plan to the Mission Review Board."
- **Sites:** polar PSR floor (ice present, ~40–110 K, permanently dark) · sunlit polar rim ("peak of eternal light") · equatorial mare (essentially dry).
- **Methods (choosing wrong is the lesson):** thermal ice mining (polar PSR only) · H₂ reduction of ilmenite · molten regolith electrolysis (MRE) · carbothermal reduction.
- **Power:** rim solar (great sun, but far from the dark ice — you must beam/pipe power into the PSR) vs. fission surface power (runs through the 14-day night and inside PSRs), each with a **duty cycle**.
- **AI "Mission Review Board"** interrogates the justification ("you sited solar to mine a PSR floor — walk me through the power path").

### The science the sim MUST encode (or experts will dismiss it)
- **Forms are distinct — never merge them:** water ice (only in <~110 K cold traps) ≠ molecular H₂O adsorbed in sunlit soil (SOFIA: ~100–412 ppm) ≠ mineral-bound OH ≠ solar-wind-implanted H ≠ hydrated salts ≠ interior/magmatic water. OH ≠ H₂O ≠ ice.
- **Location ↔ temperature:** stable ice only in polar cold traps (and cm-to-km "micro cold traps"); sunlit/equatorial regolith is ppm-level bound hydration — **effectively dry** for mining.
- **"Ore grades" with uncertainty and context:** LCROSS Cabeus plume **5.6 ± 2.9 wt%** water (one crater, one impact — not a global average); modeled polar ice ~0.1–a few wt%; sunlit H₂O 100–412 ppm; ilmenite reduction yields ~1–2 wt% O of *bulk* regolith.
- **Two unrelated process families — do NOT conflate:** (a) **mining existing ice** = a physical phase-change process (thermal sublimation → cold-trap capture → electrolysis), polar-only; (b) **oxygen from dry regolith** = metallurgical reduction (H₂ reduction ~800–1100 °C; MRE ~1600–1800 °C; carbothermal ~1600–1800 °C), works anywhere sunlit.
- **Energy is the bottleneck — the headline numbers:** oxygen from dry regolith ≈ **~24 kWh per kg O₂** all-in (PNAS 2025 model); water electrolysis ≈ ~6 kWh/kg water (plus ~50 kWh/kg H₂); ice mining sublimation on the order of ~1–2+ kWh/kg water before electrolysis. ISRU loads run tens to ~100 kW; NASA Fission Surface Power targets ~40 kWe; solar duty cycle ~45–50% equatorially and geometry-limited at the poles vs. fission ~90%+.
- **Ground-truth honesty:** as of 2026 there is **no direct in-situ measurement of polar ice concentration** — VIPER was canceled then revived (~2027), and IM-2/PRIME-1's data were contaminated by lander propellant. Present ice numbers as inferences.

### Assessment mechanic (rubric replaces MCQ)
Four analytic criteria × Emerging/Developing/Proficient/Exemplary: **Strategy fit** (resource+method+site match the goal) · **Energy reasoning** (treats power/duty cycle as the constraint) · **Data interpretation & iteration** (reads telemetry, diagnoses shortfall, adjusts) · **Justification** (defense to the Review Board holds up under follow-up). Evidence = the decision/telemetry log + the AI transcript. Score reasoning under questioning — that's what's AI-cheat-resistant and human-in-the-loop.

### Misconceptions to weaponize as traps (teach through failure)
Make these *selectable* choices that fail instructively: "heat equatorial regolith to get water" (it's dry) · "put the solar farm on the PSR floor" (no sunlight) · "ice = OH = hydration, so any 3-µm signal = mineable water" · "the resource is present, so we're done" (present ≠ accessible) · "hydrogen map = ice map."

### The assignment to you, the instructional designer
Deliver: (1) learning outcomes + a validated rubric mapped to the competency; (2) the scenario logic + a **simplified-but-directionally-correct** parameter/energy model (I validate the numbers); (3) the AI Review-Board examiner (prompt + rubric-linked probing); (4) the illustrated interface — site map, method/apparatus, control panel with power/temp/yield gauges, telemetry plot, comms; (5) WCAG accessibility; (6) a 60–90s demo video + case-study writeup. I (SME) supply/validate: realistic parameter ranges, a believable yield target + failure mode, a model expert answer, and a "nothing elementary-wrong" sanity check.

### 3-week portfolio MVP
Web, illustrated 2.5D, no goggles: one site + two method choices + the energy/duty-cycle mechanic + the AI Review Board + the rubric. Full multi-site XR = the vision.

### Do-not-claim guardrails
No claim of measured polar ice; show ± and location/method on every number; don't imply easy/proven extraction; keep the origin of lunar water ambiguous (solar wind + micrometeorites + volcanism + impactors).
