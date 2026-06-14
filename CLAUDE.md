# CLAUDE.md — Context for working with Michelle

You're opening this folder in Cowork mode with no memory of prior sessions. Read this first. It's the briefing.

**Also read `TASKS.md` in this folder for current priorities, this week's schedule, and pending decisions.** That file is updated more frequently than this one.

**AIRC SSS UX study:** the big committee/UX work lives in `airc-sss/`. To resume it, read `airc-sss/WORKING-STATE.md` first — it has all deliverables, scope, decisions, and the live form link.

## Working files

This file lives in my local clone of the singletrackmom.github.io repo:

**Repo path:** `/Users/michelleblomberg/Documents/GitHub/singletrackmom.github.io`

When I say "the repo," "my docs," "my github," or "push to github," I mean this folder. Both `CLAUDE.md` and `TASKS.md` live at the repo root. Edit them in place — don't write to a scratch directory and ask me to copy-paste. I'll commit and push from terminal once you've saved.

Project subdirectories of interest:
- `cultivate/` — Cultivate AI/EdTech PD hub
- `render/` — Render career services tool
- `copamigo/` — CopaMigo student services routing
- `newsletter/` — Rough Cut DMA newsletter

If you need to work with a project's HTML, ask which file before editing.

## Who I am

I'm Michelle Blomberg, Residential Faculty in Digital Media Arts at Glendale Community College (GCC) in Glendale, Arizona — gccaz.edu, part of the Maricopa Community Colleges district. Not Glendale California. I teach AVC100, AVC182, AVC183, and AVC248. I was DMA Program Director 2011–2022, now faculty only. I co-chair the Student Support and Success domain on the Maricopa District AI Resource Committee (AIRC). 25+ years in higher ed — EdTech PM at ProQuest/XanEdu, led the campus LMS team and an LMS RFP in the Blackboard era, MEd from NAU on connectivism and PLEs. Targeting a transition into EdTech product management, ideally online and Colorado-friendly. GitHub: singletrackmom.

**ACCURACY GUARDRAIL (stop getting this wrong): What is true is on my CV (cultivate/cv.html), use that wording. I led the campus LMS team in the Blackboard era, co-chaired the district eLearning Advisory Group (which represented the ~250,000-user, 10-college system), and contributed to the RFP that led to Canvas adoption. I did NOT lead, own, or run the Blackboard-to-Canvas migration, and I was NOT on the migration team. NEVER write "led the migration," "scaled a platform to 250K users," or anything implying I personally migrated/ran a 250K-user platform. Also: I co-chair the Student Support and Success DOMAIN only, I do not lead the whole district AIRC.**

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

## Design rules (HARD rules, never break)

- I'm a graphic designer. **Solid colors only, and only from the defined palette.** NEVER use gradients or blended / multi-stop colors anywhere (headings, hero bars, backgrounds, swatches). Blends look muddy and AI-generated. If an element needs color, pick one solid palette variable.
- **Never use em dashes** anywhere, in text or in UI. Use commas, periods, parentheses, or the middot ( · ) separator the site already uses.
- **Always use correct typographic quotes, never straight quotes or prime marks.** Use curly double quotes (“ ”) and curly apostrophes / single quotes (‘ ’). Never use straight quotes (" '), and never use prime or double-prime marks (′ ″) that look like foot and inch signs. This applies everywhere: web pages, documents, slide decks, everything.
- Match the existing site palette exactly (the CSS :root variables). Never invent off-palette hex values.
- **Never link a downloadable document on the website.** No `.docx` / `.xlsx` links and no `download` attribute on any link. Every link must open in the browser as an HTML page. If content lives in a Word/Excel doc, convert it to an HTML page and link that. (PDFs that render inline are acceptable, but prefer HTML.)

## Don't include

No student grades, no FERPA-protected info, no Canvas submission content, no login credentials, no API keys, no personal financial details, no family medical info. If you're unsure whether something belongs in a working file, ask.
