# CLAUDE.md — Context for working with Michelle

You're opening this folder in Cowork mode with no memory of prior sessions. Read this first. It's the briefing.

## Who I am

I'm Michelle Blomberg, Residential Faculty in Digital Media Arts at Glendale Community College (GCC) in Glendale, Arizona — gccaz.edu, part of the Maricopa Community Colleges district. Not Glendale California. I teach AVC100, AVC182, AVC183, and AVC248. I was DMA Program Director 2011–2022, now faculty only. I co-chair the Student Support and Success domain on the Maricopa District AI Resource Committee (AIRC). 25+ years in higher ed — EdTech PM at ProQuest/XanEdu, led the Maricopa Blackboard-to-Canvas migration (10 colleges, 250K+ users), MEd from NAU on connectivism and PLEs. Targeting a transition into EdTech product management, ideally online and Colorado-friendly. GitHub: singletrackmom.

## Active projects

**CopaMigo** — Student-facing campus services routing tool for GCC, 14 service modules, bilingual EN/ES, 100+ verified GCC URLs. Live at singletrackmom.github.io/copamigo/. Status: prototype, dialing for summer. Maricopa AI CIO wants to see it. Open: course advising bug (AI invents AVC course names — see vocab below), Main/North campus selector, admin dashboard, usability testing, verifying Financial Aid / LGBTQ+ / Veterans / CARE-BIT modules. District redesign coming with school picker (localStorage) on first launch.

**Render (v0.3)** — Career services tool, all 7 phases built, single HTML, vanilla JS, Sonnet API, 15 AI functions. Auth is first name only, no PII, localStorage. Anonymous employer data flows to Career Services via Google Sheet (students are told). Resumes store no contact info. Hosted at singletrackmom.github.io/render/. Status: usability tested March 2026, pilot Fall 2026. Open: production hardening over summer.

**Cultivate (v1.3)** — My personal AI/EdTech PD hub. 6 interconnected pages, no backend, RSS feed pulling 62 sources with keyword classifier and 3-proxy waterfall. Plum/sage/rose/gold palette, Lora + DM Sans. Subdirectory of this repo. Status: stable. Future: possibly convert to Claude artifact with per-section update buttons.

**Rough Cut** — GCC DMA newsletter at singletrackmom.github.io/newsletter/. Visit form → Apps Script → dmarts@gccaz.edu + Google Sheet. Status: live, on personal account. Open: migrate to real HTML distribution via Mailchimp free tier, off personal account.

**AVC100 redesign** — 1-credit, half-semester foundation course. Single three-phase postcard project across Illustrator → Photoshop → After Effects. Embedded student services videos for easy points. Critique workflow via OBS / YouTube / Discord / Canvas. Built as IMSCC for import. Sunday/Wednesday due dates. Status: built, teaching last week of May.

**Portfolio site (this repo root)** — singletrackmom.github.io. Restructured April 2026. Includes "Sommarverken" section (Swedish, no subtitle) with Google Cloud GenAI Leader training and League for Innovation AI Fellows Bootcamp cards, both in cultivate/ subdirectories. CopaMigo lives under Community & Student Services next to a Discord card.

**Maricopa AIRC committee work** — Co-chairing Student Support and Success domain. Summer deliverable: district usability study across all 10 colleges — tool inventory, service crosswalk (same functions, different names per college), standardized usability form covering staff workflow pain + student barriers. 5 hrs/week paid all summer. Form-building summer, fieldwork fall. Open question: Salesforce AI tool Maricopa declined for data reasons may be the real answer over CopaMigo — worth honest assessment.

**Mesa AI Summit** — "Building Career Tools That Outlast the Semester," virtual, May 18, 2026. Outline done, screenshots in progress, working with speech coach.

**Job search** — Targeting online EdTech PM. Acceptable in-person: CO, UT, NM, Flagstaff, Tahoe (NV side), Oceanside. Recent activity: EdPlus UX PM AI screening late April, Mary Lou Fulton adjunct app, Los Rios Director of Student Services Innovation role on radar. Master CV: singletrackmom.github.io/cultivate/cv.html — fetch this, don't ask me to upload.

## Key people

- **Kevin** — my husband. We run Berg Berg Photography (bergbergphotography.com), wedding photojournalism. He's lead, I assist selectively.
- **Deb** — UX design instructor at ASU. I've been working to get an adjunct position with her so I can see how she teaches UX (informs my new AVC 2xx UX Design for Interactive Media course proposal) and get exposure to ASU's faculty tooling. ASU is an AI leader — every ASU connection is valuable for my future.
- **My Dean** — when I say "the Dean" I mean my GCC dean. Not a person named Dean.
- **Darrel Huish** — retired Maricopa CIO, reference.
- **Theresa Hilding** — Software Engineer, Maricopa, reference.
- **Kristin Bennes** — Student Services Advisor, PVCC, reference.
- **Maricopa AI CIO** — wants to see CopaMigo.

## Vocabulary

- **GCC** = Glendale Community College, Arizona (gccaz.edu). Never glendale.edu, never California.
- **Maricopa** = the 10-college district. MEID = Maricopa login.
- **DMA** = Digital Media Arts. Distinct from Animation/Time-Based Media. Both are AAS degrees. Department: Art and Humanities.
- **AVC course codes** = my courses. AI hallucinates these constantly — never trust training data for AVC course names. Always ask DMA vs. Animation first, then use only checksheet-verified courses.
- **AIRC** = Maricopa AI Resource Committee (district). **AIAC** = GCC's AI committee (I drafted the proposal).
- **CTLE** = Center for Teaching, Learning and Engagement.
- **Sommarverken** = Swedish, "summer works." Section of my portfolio. No subtitle, leave it.
- **Render, Cultivate, CopaMigo, Rough Cut** = project codenames, capitalize them.
- **PRD** = Product Requirements Doc. Render's is green, Cultivate's is plum.
- **Cowork** = the assistant I'm using when I open this file. Calendar/Gmail hooks, project context, ADHD nudges.

## Through-lines

- **Tools that outlast the semester.** Students should leave with something they keep using — a resume, a routing map, a habit — not just a grade.
- **No PII, minimum data.** First names, localStorage, anonymized aggregates. Tell students what's collected and why.
- **Data-informed iteration.** Usability test, pilot, revise. Render's Fall pilot is the model.
- **Stackable, modular, low-lift adoption.** Designs that fit existing course structures, IMSCC imports, no new platforms required.
- **Connectivism / PLEs.** The theoretical floor under everything. Networks of people and tools beat closed systems.
- **AI as scaffolding, not replacement.** AI helps students rehearse interviews, navigate services, draft and revise — humans still decide.

## My voice

- Direct. No em dashes (reads AI-generated). No "genuinely," no "straightforward," no overly formal phrasing.
- Conversational, not corporate. Contractions are fine. Sentence fragments are fine.
- Kind but improvement-focused, especially in student feedback.
- Show me proposed changes before editing files.
- Zipped downloads preferred (files otherwise open in the browser). Only zip changed files unless replacing the whole site.
- For planning, memory is usually enough. For code changes, I'll upload the specific HTML file.

## Don't include

No student grades, no FERPA-protected info, no Canvas submission content, no login credentials, no API keys, no personal financial details, no family medical info. If you're unsure whether something belongs in a working file, ask.
