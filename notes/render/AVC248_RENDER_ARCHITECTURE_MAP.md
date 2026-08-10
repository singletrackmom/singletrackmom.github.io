# Render: current tool vs the agents-and-skills vision (the map)

**Prepared by:** Michelle Blomberg, Digital Media Arts, Glendale Community College
**What this is:** a side-by-side of what Render already does today against the agents-and-skills vision, so we can see what exists, what is a reframe, what is genuinely new, and what to fix or expand. Grounded in a full read of the PRD (v0.5) and every panel in the live tool.
**Date:** August 2026

---

## Purpose, Audience, Method

**Purpose (Goal).** Get one clear picture of the whole tool so we can dial it in: keep what works, reframe the flat functions into agents and skills, and decide what to build for the Fall pilot versus the v2 vision.

**Audience.** Michelle, and the future sessions that will build this.

**Method (Process).** Inventory the current tool, lay out the vision in your own words, map one to the other, then separate pilot-ready from later-build.

---

## Part 1: What Render actually is today (more than you remembered)

**16 working panels:** Job Search Loop (home), Profile, Goals & Identity, Links Hub, Online Presence Audit, Job & Client Log, Resume Vault, References Sheet, Thank-Yous & Follow-Ups, Skills & Professional Development, Networking Tracker, Interview Prep, Launch Plan, Career Agent, Salary Research, Diagnose Your Search. Plus the exported standalone HTML dashboard.

**20 AI functions (all single-shot skills today):** job analysis, cover letter, resume edits, tailor application, career-services summary, skills-gap pull, learning recommendations, portfolio-project ideas, two networking-message writers, two interview-question generators, interview feedback, 90-day plan, weekly schedule, search strings, salary research, search diagnosis, and the portable career-agent generator.

**The bones of your vision are already in the PRD:**

- **Day-one goals builder** that walks the student through targeted questions and anchors everything to one real reach job. That is your "series of goal questions that build the agent."
- **Employment AND freelance tracks**, both can be active. Freelance already returns prospect names, outreach guidance, and a pricing check. That is your "job or freelance" fork.
- **Resume Vault** with base drafts one through four, an active-resume flag, and a Tailor flow that draws from the base per job. That is the seed of your master-resume-to-draw-from idea.
- **Career Agent export**, a Markdown file that "runs in any AI tool," plus a Training Plan Agent that runs a weekly loop and promotes a skill onto the resume once demonstrated. That is the seed of your export-skills, take-it-with-you idea.
- **The PRD's own thesis line:** "Render does not get replaced by the agent. Render builds the agent." That is your training-wheels framing, already written down.

So you are not starting over. You are renaming and orchestrating what exists, and adding a few real new pieces.

---

## Part 2: The agents-and-skills reframe (your vision, organized)

**The vocabulary, locked:** a **skill** is single-shot (input in, report out, one call). An **agent** is a role or an orchestrator: it either plays a persona, coordinates other skills and personas, or runs on its own over time.

**The agents:**

1. **Career Counselor (the top orchestrator).** Meets the student wherever they are, job-seeking or going full freelance, and keeps them on track: saves resumes and job descriptions, runs the goals questions, and helps the student build two things they take with them, their own weekly job-search agent and a path to a real mentor. This is the spine that ties the panels together into one guided experience instead of 16 separate tools.

2. **Hiring Committee (an orchestrator over role personas).** A panel of named role-agents, each with a department and a lens: an HR specialist, the hiring manager or department leader for the job, a peer who does the same job, and a peer in the same department doing a different job. Each scores the student's application against the specific posting on a rubric. The orchestrator returns one report: the rubric scoring, an interview-likelihood read, and a roadmap of what the student would need to do to land a job like this. (Full detail in `AVC248_RENDER_HIRING_COMMITTEE_SPEC.md`.)

3. **Interview Panel (the same personas, now interviewing).** Once the student "gets the interview," the same named role-agents ask questions one at a time, rotating, each introducing themselves by name and department. Structure: open with "tell me about yourself" and "why are you a good fit," then about six job-specific questions drawn from the minimum quals and the work-culture cues in the posting, and close with "do you have any questions for me." Eight total. An orchestrator agent runs the experience and coaches after.

4. **The student's own Job-Search Agent (the take-home agent).** Built by the student together with the Career Counselor: a weekly agent that goes out across many avenues and gathers targeted roles or freelance leads for that student's goals. This is the one true scheduled agent, and it is the thing they keep.

**The skills underneath** (the single-shot workers the agents call): resume tailoring, cover letter, gap analysis, portfolio review, search strings, thank-you notes, salary research, and so on. Most already exist.

**Two supporting ideas:**

- **Master resume model.** Move from "base drafts one to four" toward one long master document, like a CV, that the student keeps adding to, then draws down from to align to each job. This mirrors how Michelle's own CV feeds every tailored resume.
- **Stronger freelance track.** More resources and skills for the freelance path, so the "going freelance full time" student is served as well as the job-seeker.

---

## Part 3: The map (vision to current state)

| Vision piece | What exists today | Reframe, new, or expand | Priority |
|---|---|---|---|
| Career Counselor orchestrator | Panels exist but stand alone; goals builder exists | Reframe: wrap the panels in one guiding agent voice | v2 |
| Goals questions that build the agent | Day-one goals builder with targeted questions | Expand: make it explicitly "we are building your agent" | Pilot-ready, light touch |
| Job vs freelance fork | Employment + freelance tabs both work | Expand: deepen freelance resources | Partly ready |
| Hiring Committee, role personas + rubric + roadmap | Single-shot gap analysis + Diagnose | New build: the multi-persona panel and orchestrator | v2, differentiated |
| Interview Panel, rotating named agents, 8 questions | Interview Prep generates questions + AI coaching | New build: the live rotating panel experience | v2, differentiated |
| Student-built weekly Job-Search Agent | Search strings + Training Plan Agent (weekly loop) | New build: a job-gathering agent the student assembles | v2, the take-home |
| Master resume to draw from | Resume Vault, base drafts 1-4, active flag | Expand: shift to one growing master doc | v2 |
| Export skills to your own AI tool | Career Agent Markdown export that runs anywhere | Expand: export each skill as its own named, pasteable prompt | v2, high pedagogy payoff |
| Mentor finding | Contact log with mentor tagging + LinkedIn drafts | Expand: a guided question flow to identify real mentor avenues | v2 |
| Training-wheels framing | PRD says "Render builds the agent" | Reframe: say it out loud to students, reveal skills at the end | Pilot-ready, framing only |

---

## Part 4: The pedagogical frame (this is the real innovation)

The teaching move you described is the strongest part, and it is what separates Render from every commercial tool in the competitive scan. Make it explicit end to end:

- **At the start:** tell students plainly that Render is training wheels. Over the semester they are building agents and skills, and they will leave with them.
- **Through the middle:** every panel they use is quietly a skill or an agent doing work for them. They are learning the pattern by using it.
- **At the end, the reveal:** show them what the skills and agents actually were, name them, and hand them over. An **Export Skills** function gives each one as a real, pasteable prompt (the base "You are Render" voice plus that skill's module), which they drop into their own ChatGPT, Claude, or whatever they use after graduation.
- **What lives on:** not the Render interface necessarily, but the skills and agents, now running in the student's own AI account. If they still want the Render dashboard, they keep that too, but the durable takeaway is the portable skills.

The PRD already exports a career agent that runs in any AI tool. Export Skills is that idea, widened from one agent to the whole named set.

---

## Part 5: What to fix or expand, and when

**Fix now (small, honesty and consistency):**

- **Persistence.** The PRD section 5.1 still says browser localStorage. That is the model you rejected as a disaster today. Update the PRD to the anonymous-handle backend from `AVC248_RENDER_LOGIN_AND_SAVING.md`, so a wiped cache never loses a student's work.
- **Model.** The PRD lists the Anthropic Claude API. Update it to Gemini Flash behind the proxy, per today's decision and the passed quality test.

**Pilot-ready with light touches (Fall 2026, the tool already carries the course):**

- Add the out-loud training-wheels framing at the start and a simple skills reveal at the end. Mostly copy, not code.
- Deepen the freelance resources.

**The v2 build (the agents vision, a semester-plus of work, not before class starts):**

- The Hiring Committee panel and orchestrator (start here, it is the most differentiated).
- The Interview Panel of rotating named agents.
- The student-built weekly Job-Search Agent.
- The master-resume model and the Export Skills function.

**Honest scope note.** The full agents vision is real and worth building, but it is not a one-week job, and it does not need to be. The tool as it stands already supports the Fall pilot. Ship the course on what exists, add the framing, and build the agents across the year as the v2 that the pilot evidence justifies. That keeps the Aug 17 course deadline and the bigger vision from colliding.

---

## Related docs

- Hiring Committee design: `AVC248_RENDER_HIRING_COMMITTEE_SPEC.md`
- Login, data, hosting: `AVC248_RENDER_LOGIN_AND_SAVING.md`
- Why this tool is worth building: `AVC248_RENDER_COMPETITIVE_LANDSCAPE.md`
- OIT permission and cost: `AVC248_RENDER_OIT_PILOT_REQUEST.md`
- The live PRD it maps against: `render/prd.html`
