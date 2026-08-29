# AI Pilot Request: Claude in AVC 248 (Design Self-Promotion, Capstone)

> **Status, 28 Aug 2026.** Still the long-form proposal, useful as the attachment if Jordan wants detail. The short sendable email is `notes/drafts/JORDAN_CLAUDE_PILOT_248_REQUEST.md`. Section 3 is now out of date: Fall 2026 started 24 Aug with students on their own personal Gemini accounts, so the realistic decision point is Spring 2027.

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
