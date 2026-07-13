# Simulation as Assessment

**Goal:** Build authentic, AI-resistant assessment with faculty, in their own disciplines, where they bring the subject expertise and I bring the learning design. Turn a fear they arrive with into an instrument they leave with.

**Audience:** Faculty who teach and who are frightened of what generative AI has done to their assessments. Their students, second. Institutions that certify competency, third, because their claims depend on assessments that still measure something.

**Process:** A faculty member arrives with a worry. We take one real assessment from their course apart, establish what it was supposed to measure, and rebuild it as a scenario where the reasoning is the evidence. They are the subject-matter expert throughout. I never pretend to be.

**Status, July 2026:** Working model, early. Two faculty partnerships in motion. No simulation instrument built yet, and none validated. This document supersedes `mines-flagship-project.md`, which centered a freshman free-body-diagram piece that my own catalog check refuted.

---

## The problem faculty actually arrive with

They do not arrive asking about assessment theory. They arrive frightened.

*A model can write my final paper. It can pass my exam. I do not know what my grades mean anymore, and I do not know what to do about it.*

The fear is correct, and it deserves to be taken seriously rather than soothed. When a generative model can produce the artifact, the artifact has stopped being evidence of who produced it. That is not an academic-integrity problem, it is a **construct validity** problem: an assessment that something other than the student can satisfy has stopped measuring the student. The score still appears. It no longer means anything.

The instinctive institutional answer is detection software. It fails three ways: the detectors are unreliable, they accuse students, and they do nothing at all about the student who used AI *well*, who is the student we actually want to graduate.

The answer that works is to change what the assessment asks for. **A model produces a finished thing. It does not produce a trail of having thought.**

## The model: they are the SME, I am the designer

This is the part that makes it work, and it is why it lives at a college.

I am not a physicist, an economist, or an exercise scientist. I do not need to be. I am a learning experience designer, and I work in a building full of people who have spent their careers becoming subject-matter experts. The pairing is the whole method:

- **The faculty member owns the discipline.** What competence actually looks like in their field. What a practitioner really has to decide. What a novice gets wrong, and why. Which shortcuts are fatal.
- **I own the instrument.** Backward design from the outcome. What counts as evidence. How to build a scenario that cannot be satisfied without the reasoning. How to write a rubric that scores judgment rather than the artifact. Accessibility from the first draft. Whether it can be built, and how.

Neither of us could produce the result alone, and neither of us has to.

This is also, precisely, what an online learning experience designer does: partner with faculty and subject-matter experts to turn what they know into something that teaches and measures. I have been doing it without the title.

## The evidence that faculty want this

I presented at the Mesa AI Summit on building career tools that outlast the semester. I did not pitch assessment consulting. It came back to me anyway.

- An **exercise science** faculty member approached me about building something like Render for their discipline.
- An **economics** faculty member did the same.

Unprompted, from two fields with nothing in common, after one talk. That is not me selling a service. That is faculty recognizing their own problem in someone else's work and coming to find help.

That demand is why I founded the **Faculty AI Community of Practice** at my college. It is the venue for exactly this: bring the fear into a room where somebody can do something about it, and let the disciplines cross-pollinate. A college is an unusually good place to attempt this, because the subject-matter expertise is already sitting down the hall, and it is free.

## Where Dial Your Course fits

Dial Your Course came out of this work; it did not cause it.

I needed to know, concretely, which assessments in a real course would survive contact with a generative model, and I did not want to argue about it. So I built a tool that reads a Canvas course export and asks one question of every graded item: could an AI model complete this, correctly, in under a minute? Where the answer is yes, it names the process evidence the rubric already collects, so an instructor can see which assignments still hold up and which do not.

It is a prototype, in testing across my department. It produces a report and changes nothing without the instructor's approval, and its corrections are rule-based checks against a rubric, never AI-generated. It was built with an AI model and deliberately does not run on one, which is why it cannot invent a finding.

It is useful because it makes the conversation concrete instead of anxious. It is not the point. **The point is what you build with the faculty member afterward.**

---

## The instrument we build toward

Scenario-based, with the reasoning as the evidence. The shape is the same across disciplines; only the scenario changes.

The learner receives a real situation with genuine constraints, incomplete information, and no clean answer. Across the task they:

1. **State the decision** and their assumptions, before seeing everything.
2. **Commit** to a course of action in writing.
3. **Justify** it against the alternatives they rejected, and say what evidence would change their mind.
4. **See the consequence** as the scenario advances and conditions shift.
5. **Revise**, and account for what changed and why.
6. **Defend** it to an AI examiner that probes the reasoning ("you weighted schedule risk over cost, why?"). **The transcript of that exchange is the evidence.**

The scored object is never the final answer. It is the reasoning, the revision, and the defense.

### Why a model cannot simply complete it

- The **situated context** of the scenario is in no training set.
- The learner must **commit before knowing**, and is held to the commitment.
- The **revision must respond to a consequence they actually encountered.**
- The **defense is live and unrehearsed**, against questions generated from what they themselves said.
- **The process is the deliverable.** A model produces a finished thing, not a trail.

A student can and should use AI throughout. What they cannot do is skip the thinking, because the thinking is what is being collected.

### The rubric

Analytic, AAC&U VALUE style, mastery thresholds rather than an averaged grade:

1. Framing the problem and stating assumptions
2. **Quality of the reasoning, not correctness of the outcome**
3. Engagement with the alternatives rejected
4. Response to new information; coherence of the revision
5. Defense under questioning
6. Communication and accessibility of the artifact (UDL)

Criterion 2 matters most. A well-reasoned decision that turns out badly should score well. That is what professional judgment is, and it is the criterion a model cannot game.

### Accessibility

The construct stays fixed, the means of expression flexes: written rationale, recorded walkthrough, or oral defense. WCAG 2.1 AA from the first draft, not retrofitted.

---

## Applied to Mines

Mines Online is entirely graduate and professional. There is no undergraduate audience, which is why the freshman free-body-diagram concept is retired.

The strongest anchor is **Engineering and Technology Management**, their #17-ranked online marquee, aimed at working professionals, with a specific reason to prefer it over Data Science: **in data science a model is excellent at the artifact.** It writes the code and the analysis. In a decision under ambiguity, the defensible judgment *is* the deliverable, and the reasoning trail is the only thing that can carry it. The assessment target and the AI-resistant property coincide. Candidates: EBGN560 Decision Analytics, EBGN525 Business Analytics.

**Extend, do not indict.** Mines runs a mature operation: an OLED guides faculty through a 16-week build, with the MODLs Canvas course, a Foundations of Curriculum Design prerequisite, an approved Online Course Design Guide, the Trefny Center behind it, and the HIVE studio for media. I am not proposing to fix any of that. I am proposing the next rung, and proposing to build it the way they already work: **with the faculty member as the SME.**

Their published assessment baseline is projects, discussions, quizzes, and video presentations. There is no public evidence of scenario-based or simulation-based assessment in the online DS or ETM courses. That is a gap, and generative AI is about to make it expensive.

---

## What I do not know, and will not pretend to

- **No simulation instrument is built.** This is a design, scoped to a short sprint.
- **Nothing is SME-validated.** The next action is a twenty-minute pressure-test with a subject-matter expert, *before* building anything. If the scenario does not read as credible to someone who does the work, it is decoration.
- **I have not seen inside a live Mines Online course.** Everything above is inferred from public process and catalog pages. Asking to see a sample MODL or course shell is a question I would genuinely want answered.
- **Whether it measures better is untested.** The first question is only whether it reads as credible and new to the faculty who teach it. Whether it actually measures the skills a real project would is a much later, empirical question.

## Next actions

1. Pressure-test one scenario with a subject-matter expert. Before building. This gates everything.
2. Take the exercise science and economics conversations from interest to a scoped first project.
3. Build **one** scenario end to end. Not four.
4. Write the case study: the fear the faculty member arrived with, the assessment we took apart, what we built, what it measures, and what remains unproven.

## Sources behind the design

- Wiggins, authentic assessment: does the task replicate the contextual demands the discipline places on a practitioner
- Biggs, constructive alignment: outcome, activity, and assessment must cohere
- AAC&U VALUE rubrics: validated, published, openly licensed
- CAST / UDL: fix the construct, flex the expression
- SUNY OSCQR standards 31 and 45 on authentic assessment, which Dial Your Course already checks against
