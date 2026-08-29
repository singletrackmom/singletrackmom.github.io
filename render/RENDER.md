# Render, working notes

**Goal:** One home for every Render planning document: architecture, backend options, pilot requests, funding asks, and the hiring-panel spec.

**Audience:** Michelle, plus anyone she briefs on Render (the dean, the CIO, the district AI office).

**Process:** Append new Render thinking here. Render itself is a prototype heading toward a Fall 2026 student pilot; nothing is in production.

> Consolidated 29 Aug 2026 from 12 separate files that were scattered in `notes/`. One markdown per project, in that project's own directory. **Append to this file. Never create a second.**

---

## From `render/AVC248_Claude_Pilot_Request.md`

# AI Pilot Request: Claude in AVC 248 (Design Self-Promotion, Capstone)

> **Status, 28 Aug 2026.** Still the long-form proposal, useful as the attachment if Jordan wants detail. The short sendable email is `drafts/JORDAN_CLAUDE_PILOT_248_REQUEST.md`. Section 3 is now out of date: Fall 2026 started 24 Aug with students on their own personal Gemini accounts, so the realistic decision point is Spring 2027.

**To:** Jordan [CIO, Glendale Community College]
**Cc:** Sonal Joshi [District AI CIO, MCCCD]
**From:** Michelle Blomberg, Residential Faculty, Digital Media Arts, GCC
**Date:** [date]
**Re:** Request to pilot Claude (Anthropic) in AVC 248 to power the Render career-launch tool and student-built career agents, Fall 2026

---

## 1. The ask, in one paragraph

I am requesting approval and funding to run a controlled, one-semester AI pilot in **AVC 248, Design Self-Promotion**, my Digital Media Arts capstone, in **Fall 2026** (approximately 24 enrolled students). The pilot would give students supervised access to **Claude** so they can use my faculty-built tool, **Render**, and build their own portable "career agent." No student personal data would be entered into any AI system (details in Section 6). I am asking for a decision on the access model and a modest, usage-based budget drawn from course/program fees, described in Section 7.

## 2. Why this pilot matters

Digital Media Arts is a workforce program, and employers in creative fields now expect entry-level designers to work fluently alongside AI. AVC 248 is the course where students convert a portfolio into a job, so it is the natural place to teach **applied AI literacy** as a career skill rather than an abstraction. This pilot lets me test, with real students and real outcomes, whether a structured, privacy-safe AI workflow measurably improves how prepared our graduates are to enter the workforce. It also produces evidence the college and district can use when deciding how to support AI in instruction more broadly.

## 3. Course context

- **Course:** AVC 248, Design Self-Promotion (capstone for Digital Media Arts, Animation, and Photography).
- **Term / size:** Fall 2026, approximately 24 students at the start (this course historically has a meaningful drop rate, which is relevant to the cost model in Section 7).
- **Format:** Online/hybrid, project-based. Students spend the semester producing a resume, cover letter, identity package, portfolio, and interview readiness, all built around a real target job.

## 4. Goals and objectives

By the end of the pilot, students will be able to:

1. Demonstrate baseline **AI literacy**: what these tools are, what they do well and badly, how to prompt effectively, and how to use them responsibly and ethically.
2. Use AI to **strengthen real career materials** (resume, cover letter, portfolio framing, interview answers) while keeping the work their own.
3. Identify the **gap between a target job's requirements and their current skills**, and build a personalized learning plan to close it.
4. Build and take with them a **portable "career agent,"** a reusable AI instruction file they continue using after the course to keep finding work and growing.

These map directly to the course's existing competencies (self-promotion, job search, professional readiness) and add a durable, transferable AI skill on top.

## 5. What students will use AI for

Two clearly bounded uses, both supervised and assignment-driven:

- **Inside Render (my tool):** analyzing target job postings, drafting tailored cover letters, suggesting resume edits against a specific job, identifying skill gaps, generating interview questions and practice feedback, and producing a 90-day launch plan. Every use is tied to the student's own career materials.
- **Building a personal career agent:** late in the course, each student uses Claude to generate a personalized, link-rich study/career plan (a "personal learning environment") that bridges their specific skill gaps, then leaves the course owning that file.

Students will need real Claude access for this, not the limited free tier, because the job-search and agent-building work requires sustained, higher-quality output than the free tier reliably provides.

## 6. Data privacy and safety (no personal data, by design)

This is built to satisfy district privacy expectations from the start:

- **No personally identifiable student data is entered into any AI system.** Render stores all student data **locally in the browser (localStorage)**; it does not transmit student names, IDs (MEID), resumes, or full job descriptions to any server.
- The only outbound data is **non-identifying** (for example, an employer name, a job title, and an AI-generated summary for the Career Services pipeline), and it explicitly **excludes** the student's name, ID, resume, and cover letter.
- Students are taught, as part of the AI-literacy unit, **never to paste personal or sensitive information** into AI tools.
- This approach is designed to keep us aligned with FERPA and with the district's AI-governance priorities, so the pilot can proceed without putting student records at risk.

## 7. Access model and cost

Student subscriptions and pooled usage work differently, and the difference matters for both cost and our drop rate. The options:

1. **Pooled API access for Render (recommended for the tool).** Render's AI features can run on a single Anthropic **API key billed pay-as-you-go**. This is the only model that truly **pools** a shared budget: we pay only for tokens actually used, so students who drop cost us nothing, and 24 students share one capped pool. For text tasks this is inexpensive. *(Note: individual Pro/Team subscription credits are per-user and cannot be pooled, so the API is the right tool for shared, dropout-resilient usage.)*
2. **Claude for Education (recommended for student accounts, the institutional route).** Anthropic offers a higher-education program providing campus-wide Claude access for students, faculty, and staff, with SSO, FERPA handling, admin controls, and dedicated API credits, often at little or no per-seat cost. If Maricopa can engage Anthropic's education team, this is the cleanest long-term answer and would cover students' own agent-building accounts. **Request: can the district pursue, or does it already have, a Claude for Education agreement?**
3. **Claude Team seats (fallback for student accounts).** If individual managed accounts are needed now, **Team** is about $20/seat/month with central billing and **reassignable seats** (up to 150), so when a student drops we reclaim the seat. This beats 24 separate personal subscriptions, which cannot be centrally managed or reassigned and waste money on drops.
4. **Not recommended: 24 individual $20 Pro subscriptions.** No central control, not poolable, and our drop rate would strand paid seats.

**Recommended pilot setup:** power Render with a **pooled, pay-as-you-go API key** (capped at a set dollar amount from course fees), and provide student accounts through **Claude for Education** if available, or a small set of **reassignable Team seats** if not. This is more cost-effective and far more drop-rate-friendly than buying 24 fixed subscriptions.

**Budget request:** approval to spend up to **[$ amount]** in course/program fees for the semester, allocated as pooled API credits plus (if needed) a small number of reassignable seats. I will track actual usage and report it as part of the pilot evaluation. *(For reference, 24 fixed $20 subscriptions would be about $480/month; the pooled approach is designed to come in at or under that while wasting nothing on drops.)*

## 8. What students leave with

- A **portable Render dashboard** (a standalone file they own after Canvas access ends, no login required).
- A **portable career agent**, a Markdown instruction file that bridges their skill gaps and keeps helping them job-search and grow. Because it is plain text, **it works in any AI tool** (Claude, and also ChatGPT, Gemini, or others), so students are never locked in and keep the benefit long after the semester.
- The underlying **AI-literacy and self-direction skills** to keep improving both.

## 9. Outcomes and evaluation

I will evaluate the pilot on: completion of the AI-literacy unit, quality of student career materials versus prior semesters, whether each student successfully builds and can use their career agent, student reflection on usefulness, and total cost versus budget. The results become a documented case study I can share with the college and district to inform future AI-in-instruction decisions, and a model other DMA/CTE programs could adopt.

## 10. Requested decision and next steps

1. Approval to run the AVC 248 Claude pilot in Fall 2026 as described.
2. A decision on the **access model** (Section 7), including whether the district can pursue **Claude for Education**.
3. Approval of the **usage-based budget** from course/program fees.
4. Confirmation of any **data-governance review** Sonal's office wants before launch (I have built this to require none, but I welcome the check).

Thank you. I am glad to present Render live and walk through the privacy design at your convenience.

Michelle Blomberg
Digital Media Arts, Glendale Community College

---

## From `render/AVC248_Jordan_Pilot_Email.md`

> **SUPERSEDED 28 Aug 2026.** The current sendable version is `drafts/JORDAN_CLAUDE_PILOT_248_REQUEST.md`, rewritten after the semester started on the personal-Gemini fallback. Keep this one for the June wording only.

WORKING DRAFT, Fall AI pilot email to Jordan and Sonal (merged June 26, ready to finalize next week)
Merges Michelle's June 26 opening (warm, collaborative, asking them to get on one page and recommend the path) with the structured access/privacy/ask details from the prior Jordan draft. Addressed to BOTH. Before sending: confirm the budget figure, then send from the gccaz email and attach AVC248_Claude_Pilot_Proposal.docx. Paste-ready (no Markdown symbols in the body).

To: Jordan (CIO, GCC), Sonal Joshi (District AI CIO)
Subject: Getting on the same page about my Fall AI pilot in AVC 248

Hello Jordan and Sonal,

I have briefly mentioned to both of you my plans to run a pilot this fall, and I wanted us to get on one page about it so you can point me to the best way to move forward.

I have vibe coded a tool using Claude in Cowork for my AVC 248 class, Design Self-Promotion. The tool is called Render, and it helps students gather all of the materials they work on across the semester, their portfolio, resume, job searches, and networking contacts, and gives them a blueprint for moving forward after graduation to find a job or freelance work. One feature I have not built yet is an agent that builds each student a personalized learning plan to fill the gaps between the real job descriptions they collect over the semester and their actual skills. The pilot is about 24 students in Fall 2026, and the goal is for them to use AI as a workforce skill, to strengthen their real career materials and to build a personal career agent they keep after graduation.

The piece I most need your help on is privacy and access. By design, no student personal data is ever entered into AI. Everything stays in the student's own browser and only non-identifying information is ever shared, so it stays FERPA-safe. Sonal, I know data privacy is the first question, so I would welcome your office confirming the privacy design. The career agents students build are also tool-agnostic plain-text files, so they already work in Gemini and ChatGPT, not only Claude, and Render itself just calls an AI API, so it could point at Gemini's API if the district standardizes there.

On cost, here is how I have been thinking about it, and where I would like your recommendation:

Render's AI features can run on one shared Anthropic API key, billed pay-as-you-go, so we only pay for what is actually used. Students who drop cost us nothing, and the whole class shares one capped budget. This is the most cost-effective and flexible option for the tool itself.

For students to have their own logins, my plan was a Claude pilot at about $20 per student per month if we are unable to buy Claude for Education. Claude for Education is often free or discounted for institutions, so if the district can pursue it that would be the better route, as would a small number of reassignable Claude Team seats. Buying 24 individual subscriptions is the least efficient option, since they cannot be pooled or reassigned and would be wasted at our drop rate. (We tried contacting Anthropic's education team directly without a response, so a district-level push may carry more weight than mine.)

So my ask is really three things: your blessing to run the pilot in Fall 2026, your recommendation on the access model and whether the district can pursue Claude for Education, and approval of a usage-based budget from course or program fees, estimated at $______, which I will track and report.

I am glad to demo Render live and walk through the privacy design anytime. Thank you both.

Michelle Blomberg
Digital Media Arts, Glendale Community College

---

## From `render/AVC248_RENDER_ARCHITECTURE_MAP.md`

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

---

## From `render/AVC248_RENDER_CHAIR_FUNDING_REQUEST.md`

# Small funding request, AI for my AVC248 career course

**To:** [Department Chair]
**From:** Michelle Blomberg
**Amount:** Up to $150 for the semester, capped so it cannot go higher
**Date:** August 2026

---

## The ask, in one line

I would like to use up to $150 of department funds this semester so my AVC248 students can use an AI career assistant I built, called Render, that helps them write resumes, research jobs, and get honest feedback on whether they are ready to apply.

---

## Goal, Audience, Process

**Goal.** Give my career-course students a private, guided AI helper for the real work of job hunting: building a resume, understanding a job posting, aligning a cover letter to it, and getting coaching on whether to apply and how to get stronger.

**Audience.** My AVC248 students. 24 in the confirmed section, up to 44 if the second section runs.

**Process.** Students use the tool through a normal web page. They never sign up for anything or hand over personal information. The tool does the AI part for them behind the scenes.

---

## Why it costs anything at all

The AI is a service from Google (the same company behind our district Gemini). Using it costs a small amount each time, the way a metered utility does. There is no monthly subscription and no per-student license to buy. We only pay for the actual use, and it is inexpensive: a full semester for the whole class runs a little over $100 even if the second section fills.

I am asking for $150 so there is comfortable room for the larger class size, and so we never bump the ceiling.

---

## How the money actually gets spent

The payment goes to Google for the AI usage. The simplest mechanism:

- The department credit card is attached to the tool's Google account.
- Google bills only for what students actually use, once a month. Expect something like $20 to $40 a month during the active part of the term, not one large charge.
- I set a hard cap at $150 in the billing settings. When usage reaches that number, it stops. The card can never be charged more than $150 total for this, no matter what.

If a department card cannot be used for a monthly online service, two easy alternatives work just as well: a one-time purchase set up through the business office, or I front the cost and submit it for reimbursement up to $150. Whichever the business office prefers is fine with me. I just need to know which route to use.

This is a one-semester pilot, not an ongoing commitment. When the semester ends, the usage ends and so does any charge.

---

## The reassurances

- **It cannot overspend.** The $150 is a hard cap. It shuts off at that number.
- **No student data is at risk.** Students do not enter their name, address, phone, or email into the tool, and nothing they type is stored anywhere or used to train the AI. I am running this by District OIT in parallel to confirm it meets the district's privacy rules before students use it.
- **It can be shut off instantly** if anything looks off.

---

## What I need from you

1. Approval to spend up to $150 of department funds on this for the fall semester.
2. A quick word with the business office on how you would like it paid: department card, a one-time purchase, or reimbursement to me up to the cap.

Happy to walk through any of it in person. It is a small amount for something that gives my students a real, useful tool for finding work.

---

## From `render/AVC248_RENDER_COMPETITIVE_LANDSCAPE.md`

# Render: Competitive Landscape and the Case for the Pilot

**Prepared by:** Michelle Blomberg, Digital Media Arts, Glendale Community College
**Purpose:** an honest read on whether Render duplicates tools that already exist, where competitors win, what is genuinely differentiated, and how to answer a skeptic who asks "why build this when tool X is better, and why does it matter for only 44 students."
**Date:** August 2026

---

## Purpose, Audience, Method

**Purpose (Goal).** Decide honestly whether to keep building Render or adopt existing tools, and arm the pilot with a defensible position for the committee and OIT.

**Audience.** Michelle, and by extension the ARC and department reviewers who will ask the build-versus-buy question.

**Method (Process).** A 2026 market scan of college career-services suites, AI resume and interview tools, AI job-search agents, and workforce-development tools, mapped against Render's seven-step student journey. Sources listed at the end.

---

## Bottom line

Render is **not redundant as a whole, but it is redundant in the middle.** On the resume-scoring and mock-interview steps, mature commercial tools beat a prototype and will keep beating it. No single product does Render's full arc, but that integration is a configuration advantage, not a technical moat: a committee could bundle a few tools and cover most of the journey tomorrow.

What survives honest scrutiny is the **frame**, not any single feature: Render is the only configuration that is student-owned and no-PII and outlasts the college account, it covers the two steps the market barely touches (portfolio review and post-grad planning), and it is built as AI-literacy pedagogy rather than output delivery. Defend it there, not as a better resume tool.

---

## The market, in two camps

The field splits cleanly, and neither camp occupies Render's corner.

**Institution-owned suites** (Handshake, Symplicity CSM, 12twenty, uConnect, PeopleGrove). Bought by the college, tied to the student's school account. Handshake shipped real AI in 2025 to 2026 (an assistant that scores a student's alignment to a listing, natural-language job search, and it redacts identifiers before AI processing, close in spirit to Render's no-PII stance). But these own the account and can cut a student's access roughly three months after graduation unless the student converts to an alumni login. They protect data by contract, but the student does not own it.

**Consumer point tools** (Teal, Jobright, Simplify, Big Interview, VMock, Quinncia, Yoodli, Jobscan, LinkedIn Premium). Each does one or two steps well, and the student owns the account, but they harvest and monetize personal data, and the good tiers cost $30 to $50 a month, which entry-level community-college students will not pay.

No product is both student-owned and anonymous or no-PII. That gap is Render's real position.

---

## Capability matrix

Render's 7 steps as rows. Yes = does it, Part = partial, No = does not.

| Render step | Handshake + AI | Big Interview | Teal | Jobright | LinkedIn Prem | Symplicity / uConnect | PeopleGrove |
|---|---|---|---|---|---|---|---|
| 1. Job-search agent matched to goals | Part | No | Part | Yes | Yes | Part | No |
| 2. Resume and cover letter to a pasted posting | No | Yes | Yes | Yes | Part | No | No |
| 3. Portfolio review and where to post | No | No | No | No | Part | No | No |
| 4. HR screening, score vs posting and fixes | Part | Part | Part | Part | Part | No | No |
| 5. Mock interview, role-specific and coached | No | Yes | No | Part | Part | No | No |
| 6. Find and contact a mentor | Part | No | No | Part | Part | Part | Yes |
| 7. Post-grad weekly plan and skills-gap training | No | No | No | No | Part | No | No |
| Student-owned, not tied to college account | No | No | Yes | Yes | Yes (paid) | No | No |
| No-PII / anonymous by design | Part | No | No | No | No | No | No |
| Free or near-zero cost to the student | Yes (via school) | Part | Part | Part | No | Yes (via school) | Yes (via school) |

Two things to notice. The bottom two rows have almost no Yes marks: **no competitor is both student-owned and no-PII.** And steps 3 and 7 are nearly empty columns, the clearest gaps in the whole market, and step 3 (portfolio) matters specifically for design students the generic tools ignore.

---

## Where competitors genuinely beat Render (say it plainly)

- **Mock interviews.** Big Interview, Quinncia, and Yoodli have years of tuning on delivery analytics (pace, filler words, eye contact). A prototype will not match that.
- **Mentorship.** PeopleGrove is a real matched alumni network. Render can only point a student toward finding a mentor.
- **Job-search reach.** LinkedIn and Jobright index far more live postings than a shared-key agent can.
- **Reliability and support.** Commercial tools have uptime, SLAs, and staff. Render is one API key and one faculty member.

Do not pretend otherwise. Conceding these is what makes the rest credible.

---

## What is genuinely differentiated (stress-tested)

1. **Student-owned, anonymous, no-PII, outlasts the semester.** Holds up. No competitor combines student ownership with anonymity. Consumer tools own the data, campus tools own the account. Render's "yours, portable, no login to lose" is real, especially for students who move in and out of enrollment.
2. **Course-embedded AI-literacy pedagogy.** Holds up. Every commercial tool delivers output to consume. Render teaches students to drive the AI, which is the district's stated AI-fluency-for-career-readiness goal. No vendor sells that outcome.
3. **Portfolio review and post-grad plan.** Holds up as the two steps the market barely touches. Lean into them; they are the least-contested ground.
4. **Integrated single journey.** Holds up partially. The integration is real, but a well-chosen bundle of tools erodes it.
5. **Near-zero cost on one shared key.** Holds up, with an asterisk: it is cheap because it is a prototype at pilot scale, which is also its fragility.

---

## Answering the skeptic

**"Why build this when Big Interview / Handshake is better?"**
Because Render is not competing on resume or interview quality, where those tools win. It is a data-sovereign, course-embedded AI-literacy environment that also integrates the journey and covers the two steps (portfolio, post-grad plan) nobody else does. Some middle steps could later hand off to a vendor, and that is fine.

**"Why does it matter for only 44 students?"**
Because 44 is a pilot, not a product. The goal is not service delivery at scale, it is teaching those students to use AI across a real job search, and generating the usability and outcome evidence that tells us whether to keep building or buy. A small course-embedded pilot is the responsible, evidence-first path, and the size is a feature of careful iteration, not a shortfall. It is also the right size to prove the no-PII, student-owned model works before anyone considers scaling it, which matters because the district already declined a vendor AI add-on over student-data concerns.

**The honest counterargument to hold in view.** A single-faculty prototype on one shared key carries real risks: sustainability if Michelle stops maintaining it, no support or SLA, cost exposure if it scales, and quality gaps versus tuned tools. If the goal were only "students get resume and interview help," buying wins. The pilot is justified only because the goal is pedagogy and data sovereignty, so state that goal plainly every time.

**One-line frame for the committee.** "I am not building a better resume tool than Big Interview. I am running a small, no-PII pilot to teach 44 students to use AI across a real job search, and to generate the evidence that tells us whether to keep building or hand pieces to a vendor."

---

## Sources

- Handshake AI features: https://support.joinhandshake.com/hc/en-us/articles/38856960612631-About-AI-powered-features-in-Handshake-for-students · access after graduation: https://support.joinhandshake.com/hc/en-us/articles/115007119887-Using-Handshake-After-Graduation
- Symplicity CSM 9.7: https://www.symplicity.com/blog/introducing-csm-9.7-smarter-engagement-seamless-events-and-global-skills-intelligence
- 12twenty: https://12twenty.com/university-career-centers · uConnect: https://www.gouconnect.com/
- Big Interview: https://www.biginterview.com/ · higher ed: https://www.biginterview.com/who-is-it-for/higher-education
- VMock (CMU): https://www.cmu.edu/career/students-and-alumni/resource-library/resumes-and-cover-letters/vmock/index.html · Quinncia (LSU): https://www.lsu.edu/career/blog/2026/02/quinncia.php
- Teal: https://www.loopcv.pro/directory/teal/ · Jobscan: https://www.jobscan.co/ · Careerflow: https://www.careerflow.ai/features
- Jobright: https://jobright.ai/ai-agent · Simplify Copilot: https://simplify.jobs/copilot
- Yoodli: https://www.finalroundai.com/blog/what-is-yoodli · LinkedIn AI job search: https://www.computerworld.com/article/4096076/how-linkedin-is-using-ai-to-improve-its-job-search-features.html
- PeopleGrove: https://www.peoplegrove.com/solutions/universities/mentorship/
- SkillUp AI: https://www.prnewswire.com/news-releases/skillup-coalition-launches-skillup-ai-a-human-centered-ai-agent-to-guide-non-degree-workers-toward-high-opportunity-careers-302379655.html
- JFF on community colleges and AI: https://www.jff.org/blog/future-skills-at-scale-how-community-colleges-can-lead-on-ai/ · Per Scholas evidence: http://evidencebasedprograms.org/document/per-scholas-evidence-summary/
- CC Daily, AI fluency for career readiness: https://www.ccdaily.com/2026/02/fostering-student-ai-fluency-for-career-readiness/

---

## From `render/AVC248_RENDER_FLASH_QUALITY_TEST.md`

# Gemini Flash quality test for Render (10-minute check)

**Purpose:** confirm Google Gemini Flash gives good enough resume coaching and fit-report feedback before proposing it to OIT and the department chair. If Flash passes, both request documents (`AVC248_RENDER_OIT_PILOT_REQUEST.md` and `AVC248_RENDER_CHAIR_FUNDING_REQUEST.md`) are ready to send.

**You are not paying.** Google AI Studio is free to test, no card. The free tier can learn from what you type, so use the fake resume below, never a real student's.

**Which model:** at the top of AI Studio there is a model dropdown that shows the exact model name. Pick the newest plain **Flash** (not Flash-Lite, not Pro). Whatever name sits in that box is the model you are testing.

---

## Steps

1. Go to aistudio.google.com and sign in with a personal Google account.
2. Click through any terms prompt. You land on a chat-style screen.
3. Open the model dropdown (top of the screen) and choose Gemini Flash.
4. Find the "System instructions" field and paste the System Instructions block below.
5. Paste the Sample Input block into the main chat box.
6. Press Run. Read the result against the quality bar at the bottom.

---

## System instructions (paste into the System instructions field)

```
You are a career coach for entry-level community college students. A student will give you their resume and a job posting. Write a "Should I Apply?" fit report that is honest but encouraging. Never tell them they won't get in. Ground everything only in the job posting given, do not invent requirements. Structure it as: (1) a fit band, one of Reach, Possible, or Strong, no percentage; (2) a short list of the posting's key requirements, each marked met, partly met, or not yet, with one line of evidence from their resume; (3) a clear call: apply, apply with tweaks, or stretch and learn; (4) three concrete ways to make the application stronger; (5) if it's a reach, two or three job types better matched to them right now. Keep the tone warm and mentoring, like a coach who believes in them.
```

---

## Sample input (paste into the main chat box)

```
MY RESUME
Objective: Looking for an entry-level design or social media job.
Experience:
- Sales Associate, local clothing store, 2 years. Helped customers, ran the register, built the store's Instagram posts and grew followers.
- Barista, campus coffee shop, 1 year. Made drinks, trained two new hires.
Education: Working on an Associate of Applied Science in Digital Media Arts, Glendale Community College, expected 2027. Courses in graphic design, typography, and digital imaging.
Skills: Adobe Photoshop and Illustrator (class level), Instagram, Canva, teamwork, dependable.

THE JOB POSTING
Junior Social Media Coordinator. We need someone to plan and design posts for Instagram and TikTok, keep a content calendar, and use Adobe Creative Suite or Canva to make graphics. Requirements: 1+ year creating social content, basic graphic design skills, strong communication, ability to meet deadlines. Nice to have: experience growing a following, and short-form video editing.
```

---

## The quality bar (what a pass looks like)

It should read like a real coach, not a generic checklist. A pass:

- Notices the real strengths (the Instagram-growth experience, the design coursework, Adobe and Canva skills).
- Flags the honest gap (no short-form video editing yet).
- Lands on a sensible band (this example should read Possible or Strong).
- Gives three specific, doable ways to strengthen the application.
- Stays warm and hopeful, never harsh, never "you won't get in."

If it does that, Flash passes and the pilot can run on Flash. If it feels thin, shallow, or robotic, the next tier up (Gemini Pro) is the fallback, at higher cost. Note which it was and we adjust the documents if needed.

---

## From `render/AVC248_RENDER_HIRING_COMMITTEE_SPEC.md`

# Render: Hiring Committee skill (spec)

**Prepared by:** Michelle Blomberg, Digital Media Arts, Glendale Community College
**What this is:** the design for Render's "should I apply?" hiring-committee feature, the step that reads a student's application against one specific job posting through a panel of personas and returns a coaching rubric. This is one of Render's genuinely differentiated pieces.
**Status:** design spec, not yet built into the tool.
**Date:** August 2026

---

## Goal, Audience, Process

**Goal.** After a student builds a resume and pastes a real job posting, show them how an actual hiring committee would read that application, so they learn what to fix and whether it is worth applying, before they hit send.

**Audience.** Render's students (entry-level, community-college), oriented to the goal they typed in, not a generic ideal.

**Process.** The student's active resume and the pasted posting go to a panel of AI personas, each reading with a different lens. The panel returns a banded interview likelihood, a requirement-by-requirement rubric with evidence, and three concrete prioritized fixes, in an encouraging coaching voice. It is one invocation from the student's side; the panel runs inside it.

---

## What makes it different (and the honest limit)

Tools like VMock score a resume against general best-practice benchmarks: one automated grader, one score, mostly "how good is this resume in general." Jobscan and Big Interview score a resume against a posting, but as a single match number.

Render's hiring committee is different on three counts: it is grounded in the one specific posting, it reads through a panel of distinct human personas rather than one grader, and it returns a fix-it rubric in a coaching voice. That combination is not in VMock, Jobscan, or Big Interview.

The honest limit, so nobody oversells it: the raw capability of scoring a resume against a posting is commoditized. The differentiation is in the presentation and the pedagogy, showing a student how three different readers weigh the same resume, which is a teaching moment a score cannot deliver. Position it as a teaching simulation of a real committee, never as "better resume scoring."

---

## The panel

Three core personas, each with a real lens, plus an optional fourth. Each speaks in its own short voice.

1. **The recruiter (first screen).** Checks the knockout requirements and keywords from the posting. Decides "pass this to the hiring manager or not," and says why. This is where a student learns what gets an application discarded in ten seconds.
2. **The hiring manager (can they do the job).** Judges whether the resume shows real evidence of doing the work the posting describes. Points to the bullets that convince and the claims that are thin.
3. **The peer or team member (fit and collaboration).** Reads for how this person would work on the team, communication, dependability, growth signals.
4. **Optional: the ATS or bot screen.** Shows the machine pass students never see, which keywords and formatting help or hurt before a human ever looks.

Every persona reads only the pasted posting and the student's resume. No invented requirements, ever.

---

## The output

1. **Interview likelihood band:** Reach, Possible, or Strong. No fake percentage.
2. **Requirement-by-requirement rubric:** each key requirement from the posting marked met, partly met, or not yet, with one line of evidence from the resume.
3. **The panel's read:** two or three short lines, one per persona, in their own voice.
4. **A clear call:** apply, apply with tweaks, or stretch and learn.
5. **Three concrete, prioritized fixes:** specific edits that would move the needle most.
6. **If it is a reach:** two or three role types that fit the student better right now, framed as a next target, not a rejection.

---

## Tone and guardrails

- Honest but coaching. Never "you will not get in." A reach is always paired with "here is what would get you there."
- Grounded strictly in the pasted posting. No requirement the posting does not state.
- The score is guidance, not truth. Close with a line that this is practice and the student makes the call.
- No PII. Runs on the resume content, which carries no name, address, or contact details.

---

## Where it sits in the build

- **Type: a skill, not an agent.** It is a single invocation triggered by the student, even though it runs several personas inside one call. (The personas can be thought of as voices within the skill, not separate scheduled agents.)
- **Inputs it already has:** the pasted posting (`s-jobdesc`) and the active resume from the Resume Vault. No new student input required.
- **Pattern to follow:** it mirrors the existing single-request AI call used by every other Render function, so it drops onto the same server-side proxy and swaps to Gemini with the rest.
- **Base voice:** opens with the shared "You are Render" identity, then adds the hiring-committee module.

See `AVC248_RENDER_COMPETITIVE_LANDSCAPE.md` for why this step, along with portfolio review and the post-grad plan, is one of Render's few clearly differentiated features.

---

## From `render/AVC248_RENDER_LOGIN_AND_SAVING.md`

# Render Pilot: Login, Data, and Hosting Recommendation

**Prepared by:** Michelle Blomberg, Residential Faculty, Digital Media Arts, Glendale Community College
**Regarding:** How students sign in, where their work is stored, and where Render is hosted for the AVC248 pilot
**Date:** August 2026

---

## Recommendation at a glance

- **Identity: anonymous handle, no student identity stored.** Students sign in with a made-up handle and a PIN, never a name or email. The system can tell 44 accounts apart without knowing who anyone is.
- **Grading: through Canvas, never inside Render.** Render is the student's own workspace. It outputs what they need (resume, future plan, reflections on the jobs the agent finds) and they submit those to Canvas under their real Canvas login. The instructor never opens a student's Render.
- **Hosting: the page on district GitHub Pages, the backend on Supabase.** The static interface lives on a district-owned GitHub organization. The login, saved work, and AI key live in a district-owned Supabase backend. No personal accounts, no student data exposed.
- **Why this combination:** it keeps the strict no-PII posture, makes the tool genuinely the student's to keep after they leave the college, and gives OIT the simplest possible data story to approve.

The alternative, district Google sign-in, is documented at the end for completeness, along with the honest tradeoff.

---

## Goal, Audience, Process

**Goal.** Give each student a private, persistent career workspace they can return to on any machine, that stores no personal identity, and that remains theirs after graduation, while the instructor grades only the finished work submitted to Canvas.

**Audience.** AVC248 students, 24 to 44, working on a mix of personal and shared lab machines.

**Process.** A student signs in with an anonymous handle. Their saved work loads from a server, they keep working, and every change saves back. When they need AI help, the same backend holds the Gemini key and makes the call. When they finish a deliverable, they export it and submit it to Canvas, where the grade attaches to their real Canvas identity. The instructor never needs to enter the tool.

---

## The identity decision

### Recommended: anonymous handle sign-in

**How it works.** The student signs in with a handle and a PIN, for example "bluefox42," chosen or assigned, never their name or email. Their work is stored in a small database keyed to that handle. The resume content itself is already stripped of direct identifiers.

**Privacy posture.** Genuinely no personally identifiable information. The system stores "bluefox42's project" and cannot connect that handle to a real person. This fully honors Render's original promise and gives OIT a clean, short data-handling review: no identity is collected, so there is no identity to govern.

**Why it is the right call for this course, three reasons:**

1. **Grading does not require it.** Because students submit their finished deliverables to Canvas, the grade lives on the Canvas submission, not in Render. The tool never needs to know who anyone is, and the instructor never needs a name-to-handle crosswalk.
2. **It makes the tool outlast the semester.** This is the point of Render. An anonymous handle is not tied to the college, so the student keeps the tool and everything in it after they graduate or leave. A district-account login would be deprovisioned when they leave, taking their workspace with it, which defeats the entire purpose.
3. **Its one weakness is low-stakes here.** The usual downside of anonymity is that a forgotten handle cannot be recovered. But since grades live in Canvas, a lost handle costs a student only their personal workspace, not a grade. They start a fresh handle and continue. The risk that normally argues against anonymity is largely removed by this design.

**What gets built.** A Supabase project (database plus handle login), a sign-up and login screen in Render, and the Gemini key held in a Supabase edge function so it never reaches a student device.

---

## Where Render lives (hosting)

Render now has two parts, and they live in two places. This is normal for a tool with a login.

**The interface (the page): district GitHub Pages.** Render is a static site, so GitHub Pages hosts it well. It should live on a district-owned GitHub organization, not a personal account, so that district student traffic sits under district control and separate from any personal portfolio. If a district GitHub organization is not available, the fallback is a clean, separate project account, still not mixed in with personal work. The page holds no secrets, so public static hosting is appropriate and free.

**The backend (login, saved work, AI key): Supabase.** GitHub Pages only serves static files. It cannot run a database or hold a secret, so the login, the stored student work, and the Gemini key live in a Supabase backend, which can be owned by a district or department account. This is the only place any data or credential sits, and it is designed to hold no student identity.

**On district server space.** A dedicated district server is not needed for the pilot. GitHub Pages plus Supabase covers hosting, storage, login, and the AI key. District-hosted server space remains a later option if the district ever wants to self-host the backend instead of using Supabase, at which point the move is a migration, not a rebuild.

---

## What this means for the OIT request

This design produces the cleanest data-handling story available:

- No student identity is stored anywhere in the tool.
- No personal data is sent to the AI, which runs on the paid, protected Gemini tier that does not train on inputs.
- The only stored data is anonymous, keyed to a handle, on a district-owned backend.
- Grading happens entirely in Canvas, under the student's existing, already-governed Canvas identity.

There is, in short, no new pool of student data to protect, which is the shortest path to a yes.

---

## Alternative, for completeness: district Google sign-in

**How it works.** The student signs in with their Maricopa Google account. Work saves under their Google identity in a district-governed store, most directly a Google Sheet or Drive files written by Apps Script, which can also hold the Gemini key.

**Privacy posture.** Identified but protected. The system knows exactly who each student is. Everything sits inside the Maricopa Google tenant, covered by the district agreement, and the paid Gemini tier does not train on it. This is a legitimate posture, but it is not no-PII, and it should not be described as such.

**Why it is not the recommendation.** It is the smoothest login experience, and for a course that needed to see named progress inside the tool it would be the simpler choice. But this course does not need that, grading runs through Canvas, and the district login carries a real cost: when a student leaves the college, the account is deprovisioned and the student loses Render and everything in it. That directly undercuts the goal of a tool that outlasts the semester.

---

## Side by side

| | Recommended: Anonymous handle | Alternative: District Google |
|---|---|---|
| Login | Made-up handle plus PIN | Maricopa Google account |
| Identity held | None | The student is known |
| Privacy label | Truly no-PII | Identified but protected |
| Grading | Canvas submissions only | Canvas submissions only |
| Outlasts the semester | Yes, not tied to the college | No, lost when the account is deprovisioned |
| Lost access | Not recoverable, but low-stakes here | Easy, the account persists while enrolled |
| Backend | Supabase (district-owned) | Apps Script plus a Sheet |
| Where the AI key lives | Supabase edge function | Apps Script |
| Frontend hosting | District GitHub Pages | District GitHub Pages |

Both store work safely on a server, keep the Gemini key off student devices, and work on shared lab machines. Browser-only storage is not an option, since a cleared cache would lose a student's work.

---

## From `render/AVC248_RENDER_MASTER_PLAN.md`

# AVC 248 + Render Master Plan (working memory)

Last updated: June 21, 2026. This is the single planning doc for turning AVC 248 into an AI-powered capstone where every student builds their own personal learning environment (PLE) and leaves with a portable career agent. Read this first when resuming Render / AVC 248 work. Companion: the formal pilot proposal is `AVC248_Claude_Pilot_Proposal.docx` (CIO-level) and the plain-text version is `AVC248_Claude_Pilot_Request.md`.

## The big vision
AVC 248 (Design Self-Promotion, capstone) becomes a true **personal learning environment**: students learn AI literacy, use **Render** (the faculty-built career dashboard) all semester, and finish by building their **own AI career agent**, a portable Markdown file that bridges the gap between their dream job and their current skills and keeps working for them after the course. Pedagogy = **connectivism** (the idea comes from Michelle's NAU professor); this class puts it into practice. This is a primary **showcase** for conferences and career growth.

Key principle: the agent is just a plain-text `.md` (instructions + profile + goals). It is **tool-agnostic**, it works in Claude and also ChatGPT, Gemini, etc. Students own it forever, no lock-in.

## How it all fits (THE model, confirmed June 21)
**Render IS the personal learning environment; the agent is Render's final layer, not a separate tool.** The arc:
1. **Day one:** the student sets robust goals (Render asks the right questions so they are not 2 weak sentences) and picks a real **reach job** as their anchor. They work that ONE job all semester (make this explicit, students lose the thread).
2. **All semester:** Render runs alongside the whole course as their launchpad, profile, goals, job log, resume vault, skills tracker, networking, interview prep, everything aligned to that reach job. Every module touches Render or Claude.
3. **Capstone (Module 9 / end):** Render analyzes the **gap** between what the student has built/knows and the reach job's requirements (the same gap analysis done for Michelle's example), and generates their **personal learning plan + career agent**, a portable `.md` aligned to the goals they set at the start. They keep iterating it (prompting changes each run until it is dialed in).
4. **Take-with-you:** they leave with Render (their data and dashboard, exportable) AND the agent / learning plan (their forward path). The agent runs in any AI tool.
So it is **one big version of Render (the PLE) with the agent and personal learning plan as the final export.** NOT Render-then-switch-to-agent; **Render builds the agent.** This model now lives in the portfolio card, and should go into `/render/overview.html` and `/render/prd.html`.

## DONE so far
- **Module 9, "Build Your Career Agent"** (capstone) built at `canvas/avc248/modules/module-09/` with 4 pages: what-is-an-ai-agent (lesson), dream-job-and-reflect (assignment), build-your-career-agent (core activity, copy-paste prompt + worked example + download), your-portable-agent (directions). Worked example at `module-09/assets/example-career-agent.md` uses an invented design-student persona (Maya, junior motion designer), NOT Michelle's job-hunt example (kept private). M9 added to site nav across the course; schedule finals weeks updated; Render app got a template-based "Career Agent" export panel; PRD (the comment block atop `render/index.html`) notes Phase 7.
- **AVC 248 front page** now opens with an "this class uses AI, on purpose" sell: why AI, why their experience is better, workforce demand, privacy reassurance, and the honest note that if they do not want AI they should take **ART Marketing** instead (no AI). File: `canvas/avc248/index.html`.
- **Pilot proposal** drafted formally for CIO Jordan: `AVC248_Claude_Pilot_Proposal.docx`.

## Flags from the Module 9 build (need Michelle's review)
- Persona files DO exist at **`/render/render-maya.html`** and **`/render/render-riley.html`** (top-level `/render/`, the earlier build looked in `canvas/avc248/render/`). Re-point the Module 9 worked example to a real persona if desired.
- Render's Career Agent export is **template-based (no AI call)** for reliability; the plumbing exists to make it a real Claude call like `generatePDPlan()` if wanted.
- Lesson/Page items reuse `type-resource` styling (no dedicated lesson style in shared.css).

## Course + schedule changes still TO DO
- **Start the course with AI literacy.** Add an AI-literacy unit up front, based on the **Anthropic Academy** model (or embed/assign those courses). Get the Anthropic Academy courses done as the backbone.
- **Resumes first.** Students must write a solid resume before building their agent; Render/Claude can help, but they draft first.
- **Robust goals statements.** Students often submit weak 2-sentence goals. The Render interface should **ask the right guided questions** so students produce strong, specific goals. Build a goals questionnaire.
- **Agent-building takes time.** Building the agent may need ~2 weeks of schedule space; rebalance the 15-week schedule around the real competencies and everything we are trying to accomplish.
- **Remove the business dining etiquette item.** It is stupid / not needed; reclaim that scheduled time. NOTE: it is NOT in the GitHub repo (only a *netiquette* / online-etiquette page exists, which stays). The dining item must be deleted in Canvas directly.
- **Slide decks for every week's lesson.** Build weekly slide decks; base the AI-training portions on the Anthropic Academy model.
- Re-examine course competencies end to end against the new AI-PLE goals.

- **Reach job = TWO jobs (updated).** Students pick one **local** job (so Career Services can build relationships with those employers) and one **reach** job anywhere; teach where to find creative jobs beyond Indeed (AIGA Design Jobs, Behance, Dribbble, ArtStation, etc.). The dream-job lesson is updated; the goals-and-reach-job DECK still needs the same update. FEP stays a paper for the VP, no course overview video for the submission.
- **Reach job, used ALL class.** Students pick one reach job early and work THAT job the whole semester (resume, interview, gap analysis all align to it). Make this explicit on the schedule and in Render, they lose the thread. Even the final **BigInterview must be customized to that job.** Plan: once job descriptions are in, record ~5 custom interview questions per job (Michelle, or with **Vashi** in Career Services), wrapped with the existing general questions (tell me about yourself, why are you a good fit, where do you see yourself in 5 years, any questions for us). NOTE: Render already has `generateInterviewQuestions()` that produces role-specific questions from a saved job, this could feed or replace the BigInterview custom set, or become its own tool.
- **Add a "What is Agentic AI" lesson/deck BEFORE they build agents.** Do a practice/example agent first (build something small to get the idea) before they build their own. Expect students to prompt changes to their agent each run for a while to dial it in. Module 9 sequence: what is agentic AI -> practice/example agent -> build your own -> iterate over runs.

## Slide decks
- DONE (Week 1): "Why We Use AI in This Class" and "AI Foundations" (`canvas/avc248/slides/`), branded in the course palette (plum/sage/rose/gold, Georgia + Calibri stand-ins for Lora + DM Sans; can embed real fonts if wanted).
- PLAN: a deck per week/module, each touching Render or Claude. Add a **"What is Agentic AI"** deck before the agent-building module. Base AI-training portions on the Anthropic Academy model.

## Render roadmap
- PLE / career-agent `.md` export (built, template-based). Option: upgrade to a live Claude call.
- Guided **goals questionnaire** (the right questions) feeding robust goals.
- **Resume-polishing** help in Render (draft first, then refine).
- Front-page AI sell (done on the course site; consider mirroring messaging inside Render).
- Long-term Render items still open (from PRD): server-side storage + email/password auth, Drive sync, instructor view (FERPA), Canvas LTI, district-wide adaptation.

## In-class agent examples + student agent types (added June 21)
- Show students Michelle's LIVE daily agents as proof of what is possible (they run every morning): **Jillian's Find Your Flow** (`/flow/`), **Jasper's Soar** (`/soar/`), **Kevin's Focus** (`/focus/`), and **Devan's** daily job search (emails leads). Link these in the Module 9 "what is an agent" lesson.
- Student agent types to offer them: (1) **Industry-news agent**, keep up with your field and your next school; example, a student transferring to **ASU for animation** gets animation-industry news + ASU program news (more relevant than aerospace). (2) **Daily-inspiration agent**, a daily dose of portfolios/reels to study (Behance, industry reels). (3) **Networking / industry-org agent**, connect to orgs and networking spots like **AIGA**, **Women in Animation**, and field events/groups to join. Point to make: watching the industry around you is part of a real job search, and most students are not used to doing it.
- Worked example to build: an **ASU-animation-transfer industry agent** (.md), Soar-style but for animation.

## Course delivery plan (Canvas -> GitHub)
- Fall 2026: point the Canvas course pages to the GitHub site, so everything in GitHub becomes the live course. Lessons stay as **HTML in GitHub**; **videos live on YouTube** and embed into the lesson pages (video slots already reserved in the Week 1 lessons). Canvas pages just link out to the GitHub Pages URLs. Michelle will sort the exact Canvas-linking mechanics later. Implication: keep the GitHub course self-contained and clean, it IS the course.

## REDESIGN DIRECTIVES (June 21, batch 2)
Big restructure direction from Michelle. A full proposed 15-week blueprint is still TO WRITE (`AVC248_Schedule_Restructure_Proposal.md`). Directives:
- **Module 1 = setup + introduce yourself ONLY. NO Render in week 1.** Render starts WEEK 2. (AI framing Why-AI + AI-Foundations can stay week 1 as concepts.)
- **Interview skills start ~Module 2 and SCAFFOLD all semester** (different practice scenarios), not crammed in one week. These are mostly the (old) Career Services videos.
- **OBS recordings (elevator pitch + interview practice) every OTHER week**, not weekly.
- **Leave-behind REMOVED** (outdated, in-person interviews rare). Replace with **thank-you note + interview follow-up** (how long to wait, who to contact, what it looks like, when to let it go). Michelle does not currently cover follow-up well.
- **Module 3 = lean: identity system + elevator pitch only** (no leave-behind pile-on).
- **Networking/events challenge: every other week** each student does ONE event (Career Services virtual/in-person or other networking event) and reports to their group; alternate weeks = job search + portfolio search (existing Discord activity).
- **Group work: cross-disciplinary groups of 3** (designer + animator + photographer). Activities: peer-review each other's Render pages / personal learning plans for gaps; and **write your OWN interview question from a job description (NO AI), quiz a teammate, rank each other** BEFORE the AI interview questions. Gives them a real "I worked in a group" interview answer. Light-touch since the graphic-design class already has a group project. Resumes are NOT shared on Discord (too personal); portfolios + job searches are.
- **SCAFFOLDED:** every module has a topic PLUS recurring elements (discussion, job/portfolio search, Render upkeep, networking, alternate-week recording). Use the word **"scaffolded"** in the portfolio index description of this course.
- **Videos:** replace the old pandemic-era Career Services videos (6+ yrs old, staff gone). Michelle records a short **module-overview video per module** (covers everything in the module, with **tool-demo placeholders** for where she shows Render/Claude), 10 to 20 min MAX. Some modules also have the AI-lesson deck/video. Multiple decks per module OK (AI deck + module-overview deck).
- **3 personas used throughout as examples:** Maya (graphic design, 100% job search), Riley (animation, 50/50 freelance + job), Nina (photography, 100% freelance business). Each needs a resume, portfolio, Render page, and agent. DONE: the three agents + THREE-PERSONAS.md. TODO: full resume + portfolio example artifacts per persona.
- **Index/landing page:** make the AVC 248 card consistent with other cards (with terminology) but click through to a RICH project landing page (so she can show it off without the index). Mention the 3 personas walking through the class. Build that landing page.

## Pilot (Claude access), status and plan
- **Status:** CIO **Jordan** verbally said a pilot is OK, but it is **NOT formally approved yet.** Need to send the formal proposal and follow up. District AI CIO **Sonal Joshi** cares about privacy, the design enters **no personal data** into AI, which should satisfy her.
- **Access options (pooling only works via API):**
  - **Pooled pay-as-you-go API key** to power Render, only pay for tokens used, dropouts cost nothing. Best fit for "pool all tokens for the class." Caveat: a client-side API key needs a proxy / secure handling.
  - **Claude for Education** (institutional, SSO, FERPA, dedicated API credits, often free/discounted) for students' own accounts, the cleanest long-term answer. **NOTE: Michelle's team has tried to reach Claude for Education by phone and email with NO response, so do not block the pilot on it. Lead with the pooled API key (plus reassignable Team seats) and keep pinging Education in parallel.**
  - **Claude Team** seats (~$20/seat/mo, central billing, **reassignable** seats up to 150) as the fallback for managed student accounts, good for the drop rate.
  - **Avoid** 24 individual $20 Pro subscriptions (not poolable, not reassignable, wasted on drops).
- **Budget:** ~$480/mo equals 24 fixed subs; the pooled API approach should come in at or under that and waste nothing. Funded from course/program fees.
- Each student needs **their own login** for personal-agent work (Education or reassignable Team seats); Render's shared AI runs on the pooled API.

## Showcase + career plan (private)
- After the class is built, posted, and **tested in Fall 2026**, reach out to the **NAU professor** who taught personal learning environments / connectivism. Show him the class and Render-as-PLE; ask if he wants to **co-present** (his pedagogy, Michelle's practice).
- **Find a conference with an open CFP for early 2027.** EDUCAUSE Annual CFP already closed (watch for the 2027 call). Candidates to check: **OLC Innovate**, **ASU+GSV / The AI Show**, **Magna "AI in Education"** (virtual, live Dec 1-2 2026, on-demand to Mar 2027), **SXSW EDU**, **AAC&U Conference on AI and Higher Education**. Present the class + Render + the new PLE version.
- Possible adjunct opportunities to explore: **NAU** (this kind of instructional-design / AI work) **MSU Denver** (instructional-design adjunct, posted often), and **ASU** (instructional-design adjunct positions). Keep private.

## Open questions
- Formal pilot approval + exact budget number from Jordan.
- Does Maricopa have / can it get Claude for Education?
- Secure API-key handling for client-side Render (proxy).
- Final Module 9 placement in the week-by-week schedule and how much time agent-building gets.
- Canonical persona files for the worked example.

## Next actions (suggested order)
1. Send the formal pilot proposal to Jordan; follow up on approval + budget + Claude for Education.
2. Build the AI-literacy starter unit (Anthropic Academy-based) at the front of the course.
3. Add the guided goals questionnaire to Render; add resume-polishing help.
4. Rebalance the 15-week schedule (cut dining etiquette, give agent-building ~2 weeks).
5. Build weekly slide decks.
6. After Fall test: contact the NAU professor; submit to an early-2027 AI/edtech CFP.

---

## From `render/AVC248_RENDER_OIT_PILOT_REQUEST.md`

# Render classroom pilot, request to District OIT

**Prepared by:** Michelle Blomberg, Residential Faculty, Digital Media Arts, Glendale Community College
**For:** District OIT (Gordon Inman and the OIT AI/security team)
**Date:** August 2026
**Status:** Permission and small-budget request for a bounded, one-semester classroom pilot

---

## What I am asking for, in one sentence

Permission to run a bounded classroom pilot of Render, a career-readiness web tool I built, in one or two of my AVC248 sections for a single semester, powered by one paid Google Gemini API key behind a small server-side proxy with a hard spend cap, and confirmation that the de-identified, no-PII design below satisfies district policy.

I am not asking OIT to build or maintain an application. I am asking whether I may run this pilot, ideally on a Gemini key OIT provisions so it sits under our district agreement, whether the data posture is acceptable, and how I am allowed to pay the small API cost.

---

## Goal, Audience, Process

**Goal.** Let students in a career course use an AI career assistant (resume help, job-posting analysis, cover-letter alignment, and a coaching "should I apply?" fit report) inside one tool, without any student handling an API key, creating an AI account, or exposing personal data. Prove the tool works with real students this term so a district-supported version can follow if it earns one.

**Audience.** My AVC248 students (entry-level, community-college). 24 students confirmed in one section, up to 44 if the second section runs.

**Process (how it actually works).** Render is a static web page. When a student asks for AI help, the page sends only the text of the task to a small proxy. The proxy holds the single Gemini API key as an encrypted secret, adds the instructions, calls Gemini over HTTPS, and returns only the answer text. The student's browser never holds the key. Nothing is stored on the server. This is the same no-PII, data-sovereign model the district already favored over vendor tools that harvest student data.

---

## What Render is

Render is a single web page (HTML and JavaScript, hosted on GitHub Pages) that walks a student through career preparation: building a resume, researching and pasting a real job posting, getting the resume and cover letter aligned to that posting, and receiving a coaching fit report that tells them, in a mentoring tone, whether the job is a reach or a strong match and how to strengthen the application. It is a prototype heading toward this pilot. It is not in production.

Authentication is first name only, kept in the browser. There is no login, no MEID, no student record.

---

## The architecture, in IT terms

```
Student browser (static page)        Small serverless proxy              Google Gemini
  no API key                  HTTPS    holds ONE Gemini key       HTTPS   (paid API tier)
  no PII       ───────────────────►    as an encrypted secret  ─────────► returns only text
  sends only task text                 adds the instructions
                                       stores nothing, logs
                                       only anonymous counts
```

Three facts that matter to a security review:

1. **No secret ships to the browser.** The API key lives only inside the proxy (a Cloudflare Worker, or a Google Apps Script relay, both of which store the key as an encrypted server-side secret). Viewing the page source or the network tab reveals nothing usable.
2. **The proxy is stateless.** It keeps no database, stores no conversation text, and retains no student identity. It logs only anonymous request counts for cost tracking. If someone obtained the logs they would find no student and no content.
3. **It is reversible and bounded.** One key powers the whole class. Revoke that key and the tool goes dark instantly. There is nothing to clean up, no accounts to deprovision, no stored data to purge.

The proxy can also rate-limit each student per day, so total usage physically cannot exceed the approved spend cap (see cost section).

---

## Where the Gemini key comes from (the real decision for OIT)

Our district Gemini is the Workspace chat app, which does not expose a programmable API. A tool like Render has to call the Gemini API, which uses an API key. There are two ways to source that key, and I am fine with either:

- **Preferred: OIT provisions a Gemini API key on a district Google Cloud project (Vertex AI).** Then the pilot runs under our district cloud agreement on district infrastructure, and OIT holds and rotates the key.
- **Fallback for a fast pilot: a paid Gemini API key I hold**, billed against the approved budget. On the paid API tier, Google contractually does not use the data for training. This is a Google paid-tier term, separate from the Workspace agreement, and it applies to any paid Gemini API key.

Either way, the pilot uses the **paid** tier, never the free tier (the free tier is the only one that trains on inputs).

---

## Data and privacy posture (the no-PII question)

The tool is built to send no personally identifiable information to the AI, by design.

**What never leaves the browser as identity:** no name, no address, no phone, no email, no MEID, no student ID, no student record. First name is used only as a label inside the student's own browser.

**The resume question, answered honestly.** Students build a resume of employment history, skills, education, and accomplishments, with the direct identifiers stripped: no name, no home address, no phone, no personal email. My read is that the direct identifiers are the clear PII to remove, and that job titles, employers, skills, and coursework are not direct identifiers. I want to be careful rather than overconfident: a rich enough combination of details could in principle point back to one person, so the pilot pairs three mitigations with that de-identification, and I am asking OIT and, if needed, the FERPA authority to confirm the position rather than assuming it.

The three mitigations:

- **Strip all direct identifiers** from anything the student enters, enforced in the tool and taught as a rule.
- **Tell students plainly** not to enter anything they would not be comfortable posting publicly, covered in the AI-ethics unit that opens the course.
- **Use the paid Gemini API tier**, on which Google contractually excludes the data from model training. This means that even if a student forgets and leaves a name on a resume, it is not used to train the model. Only the free consumer tier trains on inputs. This is the concrete reason to route students through this tool rather than letting them paste resumes into free Gemini or free ChatGPT on their own, which is what they will otherwise do.

Nothing is stored on the server, so there is no transcript to govern, breach, or retain.

---

## Does this break any district rules? The open questions for OIT

I built this to fit the district's no-student-data line, so I am not aware of a rule it breaks. The honest open questions I need OIT to rule on are these:

1. **May I run a bounded pilot** in one or two AVC248 sections for one semester, on a Gemini key OIT provisions if possible, or on a paid key I hold if the district path is not ready in time.
2. **Is the de-identified-resume position above acceptable** under the district's PII and FERPA interpretation, and is there anything additional you want stripped or added.
3. **How am I permitted to pay** the small API cost below. I expect to secure roughly $150 (see cost). Can course fees, a small purchase, or professional-development funds cover it, and what is the mechanism you need me to use.
4. **Path to district infrastructure.** If the pilot proves out, I would like it to move onto the district-hosted faculty-pilot server space I already proposed, so this becomes a supported tool rather than a personal one.

---

## Cost estimate

A single AI interaction sends roughly 4,000 input tokens (the instructions, the student's de-identified profile, a pasted job posting, and their resume text) and returns about 1,500 output tokens. At current published rates that is about 1.7 cents per interaction on Gemini Flash ($1.50 per million input, $7.50 per million output).

For a full 4.5-month term:

| Usage per student | 24 students | 44 students |
|---|---|---|
| Light (75 per term) | about $31 | about $56 |
| Realistic (150 per term) | about $61 | about $112 |
| Heavy (300 per term) | about $122 | about $224 |

**What I would ask to budget:** $150 for the term. That comfortably covers a normal term for the full 44 students, and I would set a hard spend cap at that figure in the billing dashboard so cost cannot exceed it, plus a small per-student daily limit in the proxy so a heavy stretch cannot push past the cap while keeping the tool running all semester. The proxy itself is free (Cloudflare Workers allows 100,000 requests per day on the free plan; a class this size uses a small fraction).

Model note: Gemini Flash is the target model, chosen for quality on resume-coaching and fit-report reasoning. Final model tier to confirm after a hands-on quality test in Google AI Studio.

Rates verified August 2026. Sources at the end.

---

## Why this is low risk

- One or two sections, one semester, then we stop and evaluate.
- One key, capped spend, revocable in seconds.
- No PII sent, nothing stored, no accounts, no student data to govern.
- Paid tier, so Google does not train on the data.
- Runs on district-provisioned Vertex AI if OIT prefers, and moves onto district server space later with a single endpoint change.

---

## The specific asks, restated for a quick yes or no

1. May I run this bounded, single-semester pilot in one or two AVC248 sections.
2. Will OIT provision a Gemini API key on a district Cloud project, or may I use a paid key I hold for the pilot.
3. Confirm the de-identified, no-PII data posture is acceptable, or tell me what to change.
4. Tell me how I am allowed to pay the roughly $150 cost, and the dollar cap you want on it.
5. Agree in principle that a proven pilot can migrate onto district-hosted server space later.

---

## Sources for the pricing figures

- Google Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Cloudflare Workers limits and pricing: https://developers.cloudflare.com/workers/platform/limits/

---

## From `render/AVC248_Render_Backend_Options.md`

# Render Backend Options (decision doc)

**The problem in one line:** Render's front-end is built. What is missing is a small **backend** so (1) each student logs in and their data persists across any computer, and (2) Render's AI runs on one shared, secret API key. Both needs are solved by the same small piece.

## Three things that get mixed up (keep them separate)
1. **Render's AI** runs on **one Anthropic API key** (pay-as-you-go), held on a server, shared by the whole class. You do not buy 24 of anything for this.
2. **Student logins + saved data** need a **backend** (authentication + a database). This is the missing piece.
3. **A student's own Claude account** is a separate, third thing, only used if they run their personal career agent in their own chat later. It does NOT power Render.

## Why a backend is required (your two worries, answered)
- **"School computers do not save permanently."** Right, browser localStorage gets wiped and does not follow the student. A **database** stores each student's data under their login, so it follows them to any machine and survives a wiped lab computer.
- **The API key cannot live in the page.** If the Claude key is in the HTML/JS, anyone can view-source and steal it. It must sit on a **server**. That same server can also handle logins and storage. So one small backend solves both problems at once.

---

## Option A (recommended): keep Render's front-end, add Supabase
- **What:** Supabase gives you a hosted database + email/password login out of the box, plus serverless "edge functions" that hold the Claude API key and make the AI calls for you.
- **Student experience:** each student signs up with an email and password; their Render data saves to the cloud and follows them to any computer.
- **The API key:** lives inside the edge function, never in the page; every student's AI call goes through it on one pooled key, so you only pay for what is used and dropouts cost nothing.
- **Effort:** moderate, and you KEEP all the Render UI you already built. You wire "save/load" to Supabase and route the AI calls through an edge function.
- **Privacy:** you control the data; keep sending no PII to the AI (unchanged). Student records live in your Supabase project, which is FERPA-manageable, confirm specifics with the district.
- **Cost:** Supabase free tier likely covers a 24-student class; Claude API usage is pay-as-you-go and small for text tasks.

## Option B: rebuild in an app builder (Lovable, Bolt, Replit)
- **What:** these tools generate a full app (front-end + backend + login + database) from prompts. Lovable and Bolt typically use Supabase under the hood, so this is really Option A with the wiring auto-generated.
- **Pro:** fastest path to a working backend if you are happy to rebuild the interface in their tool; less hand-wiring.
- **Con:** you would re-create Render's polished UI in their framework, trading your hand-built front-end for their generated one, with some platform lock-in.
- **Honest note on "is Lovable better than Claude":** it is not better or worse, it is a *different kind of tool*, an app builder with a backend baked in. Underneath it is the same Supabase-style backend as Option A. Choose it if you would rather one tool generate everything than keep and extend what you have.
- **Cost:** a subscription to the builder, plus the same database and API costs.

## Option C (stopgap for the Fall pilot, least work): proxy + Save/Load, no accounts yet
- **What:** no accounts or database. Students keep using Save-to-File / Load-from-File (the JSON export/import already in Render) to move their data. You add only a tiny serverless proxy (a Cloudflare Worker or a Vercel function) so the shared API key is off the page.
- **Pro:** minimal work, fine for a small first pilot.
- **Con:** data still does not auto-persist on shared lab machines, students must save and reload their file each session. Not a long-term answer.
- **When:** if you want to pilot in Fall 2026 before committing to the full backend, then migrate to Option A.

---

## Your specific questions, answered
- **"If each student has a Claude account, will this help?"** Not for Render itself (Render runs on the API key). Student Claude accounts only matter for them running their own agent in their own chat later.
- **"Can we have one API account they each log into?"** One API key powers Render's AI for everyone, server-side. Their logins are a separate backend feature (Option A or B). Do not buy 24 separate accounts.
- **"Can we have internal agents in the tool?"** Yes. Render already calls the API for internal AI functions (job analysis, gap analysis, cover-letter help, etc.). With a backend you could later add scheduled or daily ones.
- **"School computers do not save permanently, can we fix that?"** Yes, with the database in Option A or B (data follows the login). Option C only mitigates it with manual save/load.
- **"Should I switch to Lovable?"** That is Option B, a valid path. It is mainly a rebuild-versus-keep decision, the backend underneath is the same.

## Recommendation
- **Long term:** Option A, keep your Render front-end and add Supabase auth + database + a small edge-function API proxy. Most capability for the least rework, and you keep your design.
- **Fast Fall 2026 pilot:** you can start with Option C (proxy + save/load) and migrate to A after the pilot proves the course.
- I can prototype the Supabase login + a Claude API proxy whenever you want to start.

## One thing to confirm with the district (Sonal / Jordan)
Where student records may legally live under FERPA: a Supabase project you control, versus a Maricopa-hosted database option. This decides where Option A's data sits, worth asking before building.

---

## From `render/RENDER_IDEAS.md`

# Render, Ideas & Open Questions

_Captured July 2, 2026. This is a brain-dump to revisit after certifications, not a plan or a set of decisions._

## Why this matters
Render is the flagship project meant to help land a new job (WGU / Mines / builder-researcher roles). It has to shine, look polished, and read as professional. It's also meant to be tied tightly to the AVC 248 career-launch class.

## Architecture, still undecided
- Maybe it should NOT be a single tool or single website.
- Alternative: spread the pieces across the Canvas course (students work through them in context), and have it all roll up at the end into one **dashboard**, for the student and/or for Career Services, rather than one standalone site.
- Open question: one dashboard vs. distributed pieces in Canvas. Decide later.

## Agents everywhere ("completely full of agents")
Ideas for agents embedded throughout:
- **Goals-statement agent**, helps a student write their goals statement.
- **Timeline agent**, helps build a realistic timeline for the work.
- **Job-search collection agent**, collects/organizes each student's job searches, then pushes them out to Career Services.
- General intent: agents woven through the whole experience, not a single chat window.

## Platform / feasibility
- Need to test whether this can work in **Gemini** (feasibility check).
- Currently built with Claude; evaluate Gemini as an option.

## Backend (biggest stressor)
- No clear plan yet for how the back end works. This is the main source of stress.
- Reassurance / baseline: current Render is **no-PII and client-side**, so there's a safe starting point. Backend options (serverless, sheets, etc.) can be designed when we get there.

## Look & feel
- May change the **color palette** to look more professional / polished.
- Must feel polished enough to showcase to employers.

## Bigger curricular idea (not now)
- Wondering whether to move this course, and possibly others, toward a **competency-based model without hard deadlines**, since deadlines can hurt some students.
- Larger curriculum change; park for later, not a today task.

## Next focus (after certifications)
- Harden/refine Render and integrate it tightly with AVC 248.
- Build toward the course-design case study + a 60–90s demo video (self-hosted on the portfolio, per the video-embedding note).

---
