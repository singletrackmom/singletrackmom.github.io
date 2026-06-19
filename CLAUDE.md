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

**AVC183 (Digital Graphic Design 1)** — teaching practice to remember: for the BRANDING projects, students write their own questions (I require them to generate the questions). I want to use AI to ANSWER those student-written questions for them, as design guidance that steers their branding decisions. So whenever I am working on Graphic Design 1, the move is to take the questions the students came up with and have AI answer them to guide their design, not leave the questions hanging.

**Portfolio site (this repo root)** — singletrackmom.github.io. Restructured April 2026. Includes "Sommarverken" section (Swedish, no subtitle) with Google Cloud GenAI Leader training and League for Innovation AI Fellows Bootcamp cards, both in cultivate/ subdirectories. CopaMigo lives under Community & Student Services next to a Discord card.

**Maricopa AIRC committee work** — Co-chairing Student Support and Success domain. Summer deliverable: district usability study across all 10 colleges — tool inventory, service crosswalk (same functions, different names per college), standardized usability form covering staff workflow pain + student barriers. 5 hrs/week paid all summer. Form-building summer, fieldwork fall. Open question: Salesforce AI tool Maricopa declined for data reasons may be the real answer over CopaMigo — worth honest assessment.

**Mesa AI Summit** — "Building Career Tools That Outlast the Semester," virtual, May 18, 2026. Outline done, screenshots in progress, working with speech coach.

**Job search** — Targeting online EdTech PM. Acceptable in-person: CO, UT, NM, Flagstaff, Tahoe (NV side), Oceanside. Recent activity: EdPlus UX PM AI screening late April, Mary Lou Fulton adjunct app, Los Rios Director of Student Services Innovation role on radar. Master CV: singletrackmom.github.io/cultivate/cv.html — fetch this, don't ask me to upload.

**Job-search agent (source of truth = `Documents/Claude/Scheduled/daily-job-search/SKILL.md`).** Broadened beyond PM into all higher-ed / edtech: learning experience and instructional design, UX, AI-in-education, faculty development, program management, student success, plus attainable product roles. Sweeps every run: target edtech companies (Canvas/Instructure on Ashby, edX/2U, Coursera, Khan, Duolingo, D2L, Pearson, McGraw Hill, Cengage, Guild, Pathstream, Newsela, Handshake, PowerSchool, Ellucian, EAB, Top Hat, Turnitin, etc.), AI labs' education teams (Anthropic Claude for Education, OpenAI, Google for Education, Microsoft, CodePath), higher-ed orgs (EDUCAUSE, League for Innovation, OLC, WCET), ALL Colorado universities + Denver-area community colleges (NO Christian schools, skip Regis and Colorado Christian), Denver/Boulder local (Built In CO, onsite/hybrid OK), and AI-using nonprofits (Idealist, camps, museums, foundations). Discovery via Built In, LinkedIn, HigherEdJobs, EDUCAUSE, but the published link must always be the company's OWN careers page, verified live that day (a web search is not verification; Instructure is on Ashby not Lever). Salary: $80K hard floor for everyone EXCEPT CU Boulder and CSU (tuition-discount exception), $100K realistic, $150K target. Output is a CUMULATIVE dashboard (keeps still-live prior matches, sorted by fit, networking/reach group for 5+ yr formal-PM reqs, short subtitle, no methodology text) rebuilt daily to `Documents/Claude/JobSearch/Michelle_job_dashboard.html` AND the phone view at singletrackmom.github.io/jobs/ (noindex, unlinked, stealth). Applied so far: Guild Applied Learning Manager (6/17), Instructure Canvas CSM. Do not resurface applied roles in the apply-now list. FAVORITE LANE to rank high: "build-with-people" roles where I vibe-code, build agents, and help others build with AI, AI Solutions Engineer/Architect, Forward-Deployed Engineer, Developer Advocate / Developer Education, AI Enablement / Adoption / Trainer, Solutions or Implementation (Education), especially at AI labs (Anthropic, OpenAI, Google, Microsoft, CodePath) and AI-edtech companies. I am weighing consulting but prefer a salaried build-with-people role first.

**EXPANSION + REFRAME (June 19):** explode the feed beyond higher-ed PM. I have NO formal PM experience and feel stuck chasing "PM-wannabe" roles, so LEAD with my real strengths: learning experience / instructional design, UX research and UX SYSTEMS / service design (the AIRC SSS 10-college, ~140K-student usability + service-crosswalk study is the flagship), and AI-SYSTEMS building (Render, CopaMigo, Wayfinder are systems, not just tools). Broaden sectors well beyond higher ed: nonprofits, foundations, WORKFORCE development / economic mobility (JFF, Year Up, Per Scholas, Strada, Merit America, Climb Hire, Social Finance, Generation, Guild, National Skills Coalition), mission-driven and AI-for-good orgs, libraries / museums / science education, national labs outreach (NREL is in Golden, NCAR/UCAR + NIST in Boulder), associations (EDUCAUSE, ISTE, OLC, Digital Promise, New America), and broad-reach info/learning companies like ProQuest/Clarivate and ETS (ProQuest was never purely higher ed). NOT banks or pure finance. GEOGRAPHY widened: remote-first, but I am NOT married to Golden and would relocate for the right role to Carbondale / Roaring Fork Valley, Mancos / Durango / Cortez, Fruita / Grand Junction (Western Slope), or Flagstaff, on top of CO/UT/NM (I do not want to keep flying to Phoenix for years). Keep the $80K hard floor (target $150K).

## Family job-search agents (run for my family, not just me)

Five daily agents live at `Documents/Claude/Scheduled/<name>/SKILL.md` and publish to this repo. They are scheduled ~6 AM but I turn my computer off overnight, so they often miss the cron and need a manual run when I sign on. To run one, read its SKILL.md and execute it. Each keeps ALL still-live leads day to day (re-verify, drop only closed ones); not everyone applies daily.

- **Me** `daily-job-search` → `jobs/` (stealth, noindex). On the dashboard, flag what is NEW vs carried-over so I do not miss new ones; I have already looked up the old ones.
- **Kevin** `kevin-daily-job-search` → page is **`/focus/`** (renamed from /kevin/), titled "Focus," photography theme with a camera-lens SVG in the hero and subtle bike accents. NO email anymore, he just refreshes https://singletrackmom.github.io/focus/.
- **Devan** `devan-daily-job-search` → `summerwork/`.
- **Jillian** `jillian-find-your-flow` → `flow/`.
- **Jasper** `jasper-soar` → `soar/`.

**Kevin bike-brand memory (hard):** four bike brands sit ~1 mile from our house, **Revel, Commencal, Spot, Yeti**. Keep close watch on all four as photography outreach targets. His fit is staged PRODUCT / parts / frame / website shots and ARCHITECTURAL building photography (he is an architecture expert), NOT influencer or content-creator work (he applied to Revel's content-creator role but a following is not his thing). **ALCHEMY BIKES IS OUT OF BUSINESS (June 2026), never suggest it.** Watch for a possible Italian brand relocating to Golden (unconfirmed, confirm before listing). Bike-brand outreach copy should also offer to follow up for a shop ride out to Apex (our local trail) to stage action shots, AND offer professional event photography (covering races, team / sponsored-rider days, launches, since the brands all have sponsored riders), on top of the staged product/parts/frame and building photography. He is a professional event photographer, not the phone-clip content-creator type. **HARD PAY FLOOR: Kevin will not work for under $20/hour, no matter what.** Never surface sub-$20 or low per-gig work (the mortgage/field-inspection gig at ~$5-15 per inspection is OUT, removed). **Growth strategy for slow wedding years (a standing "growth ideas" section on his focus page):** build a Colorado-destination portrait business for visiting families and couples, beyond Denver/Golden/Boulder into Rocky Mountain National Park + Estes Park, Grand Lake, Winter Park, and Frisco/Breckenridge/Dillon. Get found via one web page per destination (ranks on Google AND feeds AI search like "Colorado portraits while on vacation"), a complete Google Business Profile with reviews, and Pinterest boards. Run Meta (Instagram/Facebook) ads to Texas (Dallas, Houston, Austin) and other feeder markets (OK, KS, NE, AZ, Chicago), plus Google Search ads for high-intent queries. Apply to host an Airbnb Photography Service (Airbnb relaunched Experiences + Services in 2025, photography is a category, stay-then-session hookup, NOT set up yet, real to-do). Use Adobe Stock to monetize his 20-year Colorado archive (we know someone who does Adobe Stock, warm intro). Build lodging/venue referral partnerships in the mountain towns (offline version of the Airbnb hookup). Pivot existing wedding contacts toward elopements + destination family sessions. Be realistic on too-good-to-be-true gigs (mortgage/field inspection like FAR is a real industry but pay is modest and per-inspection, work is inconsistent): keep them but label honestly as fill-in income and include the safety rule (never pay upfront or cash-and-wire).

**Jillian flow rules (hard):** every career edition MUST include a "How to get qualified" box with real, accredited, verified links, framed as a small first step. Prefer the least-school path and LOCAL Colorado community-college programs; if a 4-year degree is the only route, use a community-college transfer / 2+2 path (she is ADHD/school-averse and cost-smart, not chasing the hardest school). Check what employers actually require, never send her after something unattainable. PTA path = Arapahoe Community College (AAS). Personal trainer path = one NCCA-accredited cert (NASM/ACE), the local Community College of Denver NASM program, or Life Time Academy (note: some Life Time trainer roles prefer a degree, so start entry-level). Career lanes she specifically wants explored next: the many ways to use criminal justice, and how to become a paralegal (certificate/associate, not law school). PTA specifics: she has already attended the Arapahoe CC info session and toured Pima Medical Institute (Denver, ~18-mo associate, more money but Michelle would help pay) but has NOT applied; prereqs can be taken at Red Rocks CC (closest to the house). IMPORTANT framing: Jillian pulled back when she felt Michelle was deciding her life for her, so always present these paths neutrally as HER choice (coming from Flow, not Mom), low-pressure, next step is small and hers.

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
- **GOAL, AUDIENCE, PROCESS on everything, forever.** Every project, tool, agent, PRD, and portfolio card I make ALWAYS states three things, clearly labeled: Goal (specific, not vague), Audience (exactly who it serves), and Process / How it works. Never ship a card or PRD missing any of the three. This is the same structure I require of my students, keep it consistent across the whole portfolio.
- **Be honest about status, never overclaim.** Label prototypes as prototypes and tools in testing as in testing. Render is a prototype heading toward a Fall 2026 pilot; CopaMigo is an early prototype in testing; nothing is in production yet. Do not imply production or use numbers I cannot verify.
- **PRDs and all documents are HTML pages, never Word or Excel.** Build and link `.html`, not `.docx` / `.xlsx`.

## Don't include

No student grades, no FERPA-protected info, no Canvas submission content, no login credentials, no API keys, no personal financial details, no family medical info. If you're unsure whether something belongs in a working file, ask.

## Resume and cover letter rules (job applications)

Learned June 17, 2026. Follow these every time I build Michelle's resume or cover letter.

- DO include a short, tailored narrative Professional Summary at the very top (about 4 to 5 lines, executive tone, drawn from Michelle’s own mission language). Tailor it in substance, but do NOT name the specific posting or say “this role”; it should not look written for one job. Do NOT use a skills-list or "Areas of Expertise" block. What she dislikes is the generic skills-summary opener, not a narrative summary.
- All skills go in a Technical Skills section at the BOTTOM, and they must align to the specific job's required skills, not a generic or arbitrary list.
- Never lift phrasing from the job description into the resume. It reads as AI-written. Write accomplishments in Michelle's own words.
- Every job entry must be thorough and must demonstrate the relevant skills through concrete accomplishments, not abstract skill statements. The skills a section is meant to show should be visible in the bullets themselves.
- Pull real depth from the CV (cultivate/cv.html): relevant trainings, presentations, awards, and service. The resume should be a full, robust 3 pages.
- Dates flush right (right tab). No em dashes anywhere. Curly quotes and apostrophes. Header shows name, Golden, Colorado, email, and singletrackmom.github.io. Never invent URLs (no github.com/singletrackmom).
- Cover letter: formal business-letter format (letterhead, date, recipient block, "Dear...", "Sincerely"). Do NOT mention proximity to the employer's city; the address already shows location. Avoid "genuinely," "straightforward," and casual asides.
- Leave out dated or irrelevant certifications (for example the 2014 Quality Matters certificate). The current Quality Matters / OSCQR lead-reviewer service role is fine to keep.


### Resume formatting (LOCKED, every time, do not relitigate)

- ONE entry format across ALL sections (experience, projects, education, certifications, presentations, awards, service): the TITLE comes first and is the only bold text, then a comma, then the organization in regular weight, and the date sits alone in its own right-aligned column. Pattern: **Title**, Organization [tab to right] Date.
- Only the title, role, or credential name is bold. Organizations are never bold, anywhere, including education and certifications.
- Dates are ALWAYS right-aligned in one consistent column, on every entry. Never put a date in parentheses, never inside the body of a line. Ranges use an en dash with spaces (for example, 2011 – Present).
- Separators inside a line are commas. Never middots, pipes, or bullet characters in the middle of a line.
- Experience entries: the Title, Organization line, then an italic line for any prior title and the location, then accomplishment bullets that show the skills through concrete results.
- Technical Skills: a bulleted list at the very bottom, each bullet leads with a bold category label before the colon, and the categories align to the target job.
- Education and Certifications: same Title, Organization format, organization not bold, no bullets.
- Headings and entry titles use keep-with-next so a heading or job title never strands alone at the bottom of a page; it breaks to the next page instead.
- Full 3 pages. Calibri. Name centered at the top, contact line beneath it: Golden, Colorado, email, singletrackmom.github.io. No em dashes. Curly apostrophes and quotes.
- City and state for a job go on an italic line directly under the title, unless they fit on the title line without pushing the date to wrap. No period after the state.
- When an entry has two date ranges, list them in ascending order with the range ending in "Present" on the RIGHT (for example, 2010 – 2016, 2025 – Present).
- Be honest about status: label tools still in progress as prototypes or "in testing," never imply production. Do not use numbers Michelle cannot verify (no invented percentages or counts); if unsure, say "improved" without a figure.
- Only list skills Michelle actually uses; remove anything she does not recognize. Split genuinely different categories (for example, Data and analytics separate from Accessibility). Technical-skill bullets lead with a bold category label before the colon.
- Page breaks: every page must BEGIN with a title (the name header, a job title, or a section heading), never an orphaned bullet or a lone heading. A small gap at the bottom of a page is fine and is preferred over an awkward break; force a page break before a role if needed, and keep the Certifications block whole. Tighten spacing (margins and paragraph spacing) to hold three pages.
- The cover letter header is CENTERED to match the resume (centered name, centered contact line), then the date and recipient block are left-aligned. The contact line separates items with spaces, no middots.
- To reuse: copy `RESUME_FORMAT_generator.js`, keep every helper (head, entry/entK/entKB, ent, sub, b, skill) and all the spacing and margin values exactly, and only swap the content inside the calls. Build with `npm install docx` then `node`, convert to PDF with the docx skill's soffice script, and verify page breaks with `pdftotext -layout`.

- A working generator that produces exactly this format is saved at `Documents/Claude/Applications/RESUME_FORMAT_generator.js`. Reuse and re-point it for the next job rather than reinventing the layout.
