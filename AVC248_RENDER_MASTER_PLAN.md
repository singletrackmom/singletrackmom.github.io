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

## Pilot (Claude access) — status and plan
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
