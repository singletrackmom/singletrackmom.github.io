# STEM Simulation as Assessment, Brainstorm Brief

_Canonical hub for the STEM simulation portfolio project. Written to hand to a STEM faculty member or engineer collaborator ahead of a brainstorm session, so they can follow it cold._

_Consolidates three earlier notes: `mines-flagship-project.md` (the fully worked "Reading the Forces" example), the flagship section of `../portfolio/PORTFOLIO_REDO_PLAN.md` (topic options + the SME collaborator as co-creator), and `immersive-ai-assessment-plan.md` (the simulation-assessment method and AI role-play). Read those for depth; this is the front door._

---

## 1. The big idea

Online professional and technical programs are fully remote. Students never set foot on campus, and increasingly they never meet in real time. That was already true before AI. Now add this: the assessments those programs have leaned on, multiple choice, written exams, short-answer quizzes, can be one-shot answered by a chatbot in seconds. A remote student with a text box and ChatGPT can pass a traditional exam without demonstrating that they can actually do the work. The summative assessment, the thing that is supposed to certify competence, is the part AI breaks most cleanly.

The answer is not to police AI harder. It is to change what we ask students to do. Simulation-based summative assessment puts the student inside a convincing, authentic professional problem and makes them work it through: gather what matters, make judgment calls, justify each one, and live with the consequences the scenario hands back. You cannot fake your way through a well-built simulation by pasting in a chatbot answer, because the thing being graded is the process and the reasoning, not a final number you could look up.

To be concrete about the format: this is a summative, capstone-style assessment, the graded piece that replaces the final exam and certifies that the student can actually do the work. It is not a low-stakes practice activity along the way. That is settled; the brainstorm is about which problem it assesses and how, not whether it is summative.

Here is the reframe that makes this exciting instead of grim. In these classes, AI is genuinely useful, just not where people fear it. Point it at the assessment itself and it becomes the engine that makes authentic simulation possible: an interactive lab partner that probes a student's reasoning, a simulated client or stakeholder who reacts and pushes back, a scenario engine that adapts instead of running a fixed script. That is a real, defensible use of AI in a technical course. It moves AI from "the thing students cheat with" to "the thing that lets us assess what actually matters." Same technology, opposite role.

Short version to say out loud: remote programs cannot proctor their way out of this, and they should not want to. Build the assessment as a simulation of real professional work, and let AI play the parts of that world.

---

## 2. Goals for the brainstorm

By the end of the session, aim to walk away with:

1. **A chosen flagship topic** (see the candidates in section 5), picked because it is authentic to real work and something the SME collaborator can vouch for as a subject matter expert.
2. **One authentic problem defined**, the specific scenario a student would work through, in one or two sentences.
3. **A sketch of what the student actually does**, the moves they make and what they produce (a decision, a built artifact, a defended recommendation).
4. **A first cut at how competence is judged**, the three to five things a competent professional would get right that a bluffer would not.
5. **The AI's role named**, what part the AI plays in the scenario (lab partner, client, regulator, skeptical senior engineer) and what its transcript proves.
6. **A build scope for the prototype**, what the first shippable slice is, so it stays a three-week web interactive and not a semester of engineering.

If we get topic, problem, student moves, and AI role locked, the session is a win. Everything else can follow.

---

## 3. What is in this for the collaborator

This is not the SME collaborator donating expertise to Michelle's portfolio. It is a shared artifact that lives in both portfolios.

The STEM faculty member or engineer is the subject matter expert and co-creator, which means they get a demonstrable teaching-innovation piece with their name on it: proof that they can take real technical content and turn it into a modern, AI-resistant, simulation-based assessment. For anyone hiring in teaching, faculty development, curriculum, edtech, or technical training, that is a strong, concrete thing to show, and most subject experts do not have one. They contribute the domain judgment (what a real problem looks like, what separates a competent answer from a plausible-sounding wrong one, where students actually go wrong); Michelle contributes the learning design, the build, and the polish. Both names, one artifact, two portfolios.

It also doubles as a talking point for the collaborator in their own search: "I co-designed a simulation-based competency assessment that a student cannot fake with a chatbot" is a sentence that gets follow-up questions in a good way.

Be honest with her about the ask and the payoff: a couple of brainstorm sessions plus some SME review, in exchange for a finished, showable piece she did not have to build herself.

---

## 4. What makes a convincing problem

A quick rubric for choosing and shaping the assessment problem. A strong candidate hits all five.

- **Authentic to real professional work.** It mirrors a task the field actually does, not a textbook exercise. A practitioner should look at it and nod.
- **AI-resistant.** A chatbot cannot one-shot it. This usually means the problem has no single lookup answer, depends on context the student has to interpret, and rewards judgment across several linked decisions.
- **Process and judgment, not just the final answer.** The student has to show their reasoning, defend inclusions and exclusions, and make tradeoffs out loud. Two students can reach defensible but different endpoints and both earn credit for sound process.
- **Gradeable against competencies.** You can write a short analytic rubric where each row is a real professional skill, and score the process and the justification, not only the artifact.
- **Feasible as a web interactive prototype.** The first version ships in about three weeks as a browser piece, self-hosted, embeddable in an LMS. No headset required to prove the concept.

A useful test: if a smart student with a chatbot and no domain understanding could pass it, it fails criterion two and needs more judgment built in.

---

## 5. Candidate topics

Several options, so the brainstorm has real choices. Each lists the real-world task, what the student produces, and how AI plays a role in the world of the problem. Lead candidate first.

### A. Additive manufacturing / materials selection (the SME collaborator's lane, lead option)
**The task:** the student is handed a part with a job to do (a bracket, a housing, a lightweight structural component) plus its real constraints: load case, thermal environment, cost target, quantity, timeline. They must choose a material and a process (which alloy or polymer, which AM process, key parameters like build orientation, infill, post-processing) and defend the choice against the constraints.
**What they produce:** a specified build plus a written or spoken justification of the tradeoffs (strength versus weight versus cost, anisotropy from build direction, porosity and post-processing needs, why the rejected options were rejected).
**AI's role:** a design-review engineer or client who interrogates the choices ("you oriented it that way, what does that do to the load-bearing direction?") and a scenario response that shows the consequence, the part warps, delaminates, or fails at the weak axis if the reasoning was off. AI-resistant because the defense of tradeoffs under specific constraints is the graded thing, and there is no single correct part.

### B. Failure analysis / root cause (materials-adjacent, also fits a materials SME)
**The task:** the student receives a component that failed in service, plus evidence (fracture-surface images, load history, environment, a timeline). They must diagnose the root cause and recommend a fix.
**What they produce:** a diagnosis with a reasoning chain from evidence to conclusion, and a recommendation that would prevent recurrence.
**AI's role:** a skeptical senior engineer who keeps asking "what rules out fatigue?" or "why not a material defect?", forcing the student to reason from the evidence rather than guess. Strongly AI-resistant, because it is a judgment chain over specific evidence, not a lookup.

### C. Reading the Forces, free-body diagrams (carried over as a worked example)
**The task:** the student builds a free-body diagram from a novel scene (crate on a ramp, sign on two cables, bridge pin joint), names the agent of each force, justifies each inclusion, predicts the motion, and watches the scene animate the consequence.
**What they produce:** a constructed and justified diagram plus a short reasoning transcript, scored against a competency rubric.
**AI's role:** a lab partner or TA that probes the reasoning ("you drew friction pointing uphill, why?").
**Note:** this one is fully designed already (see `mines-flagship-project.md`), which makes it the best proof of the method. Its catch is that free-body diagrams are intro-physics level, so for a graduate or professional audience it works best framed as a reusable pattern demonstrated on simple content, with the design as the star, not the physics.

### D. Data science case (maps to the largest online technical cluster)
**The task:** the student gets a messy, realistic dataset and a business or research question. They must frame the question, choose an approach, catch the traps (leakage, bias, a misleading metric), and defend the analysis.
**What they produce:** an analysis plus a defense of the method and its limits, "here is what I did, here is what could go wrong, here is why I trust it this far."
**AI's role:** a stakeholder or product manager who keeps asking "why this model, what happens if the data shifts, what would change your mind?" The transcript of that defense is the evidence. AI-resistant because a chatbot can produce a plausible analysis but not a student's live, context-specific defense of judgment calls.

### E. Engineering and technology management decision simulation (professional case style)
**The task:** the student plays a manager in an evolving project, budget, risk, and staffing scenario. They make a sequence of decisions with real tradeoffs, and the simulation reacts and changes the state.
**What they produce:** a decision trail plus the rationale at each fork, judged on the quality of reasoning under uncertainty, not on hitting one "right" ending.
**AI's role:** the stakeholders in the room, an executive, a client, a team lead, each with their own pressure, that the student has to read and respond to. This mirrors adult professional case teaching and is hard to fake because the decisions are sequenced and interdependent.

### F. Environmental / energy-transition or mining scenario (site decision under constraints)
**The task:** the student evaluates a site or process (a carbon-capture retrofit, a mine reclamation plan, a tailings or water-management decision) and must choose an approach under layered constraints: regulatory limits, cost, technical feasibility, community impact.
**What they produce:** a recommended approach with a defense that weighs the competing constraints honestly.
**AI's role:** a regulator, a community stakeholder, or a review board that pushes on the weak points of the plan. AI-resistant because the tradeoffs are specific to the site and the defense has to hold up to challenge.

Across all six, the shared skeleton is the same and only the domain skin changes: outcomes, then an authentic scenario, then a rubric that scores process and justification, then an AI counterpart that probes or reacts, then an illustrated interface, then an accessibility pass, then a short demo video. That reusable pattern is the real portfolio asset. Pick the skin that the SME collaborator can stand behind and that reads as real professional work.

---

## 6. Open questions and session agenda

A suggested order for the meeting, roughly the same order as the goals in section 2.

1. **Align on the thesis** (5 min). Do we both buy the "simulation as the AI-proof summative, with AI playing the world" framing? Adjust if the collaborator sees it differently from inside the field.
2. **Pick the topic** (15 min). Walk the candidates in section 5. Default toward additive manufacturing or failure analysis, since that is the collaborator's expertise and gives them the strongest co-creator credit. Decide.
3. **Define the authentic problem** (15 min). Nail the specific scenario in one or two sentences. What is the part, the dataset, the site, the failed component? What is the student being asked to do?
4. **Sketch the student's moves** (15 min). What does the student actually do step by step, and what do they produce at the end?
5. **Draft the competence criteria** (15 min). List the three to five things a competent professional gets right that a bluffer would not. This becomes the rubric.
6. **Name the AI's role** (10 min). Which character does AI play, and what does its transcript prove about the student?
7. **Set the prototype scope and split the work** (10 min). What is the first shippable slice? Who owns what? The SME collaborator on domain accuracy and "does this scenario feel real," Michelle on design, build, and polish. Agree on the next checkpoint.

Parking lot for later, not the first session: the immersive / XR layer (a browser or headset version in the campus XR lab), packaging it as open educational resource, and how it plugs into an LMS. All of that is real and documented in the source notes, but it comes after the core problem and the rubric are settled.
