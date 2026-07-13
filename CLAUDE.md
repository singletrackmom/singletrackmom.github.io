# CLAUDE.md, Context for working with Michelle

You're opening this folder in Cowork mode with no memory of prior sessions. Read this first. It's the briefing.

**Also read `TASKS.md` in this folder for current priorities, this week's schedule, and pending decisions.** That file is updated more frequently than this one.

**AIRC SSS UX study:** the big committee/UX work lives in `airc-sss/`. To resume it, read `airc-sss/WORKING-STATE.md` first, it has all deliverables, scope, decisions, and the live form link.

## ⚠️ DESIGN CONSISTENCY, NON-NEGOTIABLE (read before building anything)

Every time you build a new page, product, or project, it MUST be completely consistent with the existing design system from the very first draft. Do NOT invent per-page styles, do NOT let padding, heading sizes, body color, navigation, or eyebrows drift. Inconsistency (some pages with pill nav, some with eyebrows above vs below, different body colors, different margins) is the #1 recurring problem, stop it before it starts. Clone an existing clean page instead of starting fresh. The canonical template to clone is `wayfinder/overview.html`.

**The one design system (use these EXACT values, no exceptions):**
- **Fonts:** Lora (serif) for headings/titles ONLY; DM Sans for everything else. Body base 15px.
- **Colors (CSS vars):** `--ink:#26221f` (headings + body prose), `--muted:#6d635f` (subtitles, captions, nav), `--rule:#e5ddd1` (borders), `--warm:#f4efe8` (thumbnails), `--plum:#7a5080` + `--sage:#6b8f6e` (accents). Background always `#fff`.
- **Type sizes (exact):** page title h1 = 1.9rem Lora `--ink`; homepage hero = 2rem Lora; subtitle/lead-in = **1.08rem `--muted`**; body prose = **1.03rem `--ink`**; eyebrow = 0.72rem uppercase, letter-spacing 0.12em, `--sage` or `--muted`; card description = 0.82rem `--muted`.
- **Layout:** `main` and `header` both `max-width:1000px; margin:0 auto; padding: 2.4rem 1.5rem …`. Left edge of header and content MUST line up, never double-wrap content in a second padded container. Title sits at the same top spot on every page (2.4rem below the header, first element, no eyebrow pushing it down).
- **Navigation:** IDENTICAL on every page, plain-text `Home · Work · About` (`.site-nav`, `--muted`, no borders/background). NEVER pill buttons on some pages and text on others. No leftover old CSS (e.g. `header nav a` pills) leaking in.
- **Eyebrow:** if used, place it UNDER the title (not above), same style everywhere. Consistent category labels ("AI tools & strategy", "In the classroom", "Agentic & personal build", "Experiential learning").
- **Writing:** NO em dashes (,/,) ever, use commas/colons/periods. Use curly quotes (`&rsquo; &ldquo; &rdquo;`), never straight quotes in visible text. Card descriptions don't start with "I", use action verbs (Led, Built, Advised).

Before calling any new page done, spot-check it against an existing page: same nav, same title size + position, same body color/size, same padding, same eyebrow placement. If anything differs, fix it. ALWAYS make everything consistent, no matter what.

## Working files

This file lives in my local clone of the singletrackmom.github.io repo:

**Repo path:** `/Users/michelleblomberg/Documents/GitHub/singletrackmom.github.io`

When I say "the repo," "my docs," "my github," or "push to github," I mean this folder. Both `CLAUDE.md` and `TASKS.md` live at the repo root. Edit them in place, don't write to a scratch directory and ask me to copy-paste. I'll commit and push from terminal once you've saved.

Project subdirectories of interest:
- `cultivate/`, Cultivate AI/EdTech PD hub
- `render/`, Render career services tool
- `copamigo/`, CopaMigo student services routing
- `newsletter/`, Rough Cut DMA newsletter

If you need to work with a project's HTML, ask which file before editing.

**File map, where working docs live (so nobody has to hunt):**
- **Course tooling handoff:** `tools/NEXT.md` is the pick-up-here file, written at the end of a session. Read it before touching Dial Your Course. `canvas/reference/CANVAS_OUTCOMES_EXPORT_BUG.md` holds the research into why Canvas outcomes do not reach an `.imscc` export (source read, cause identified, two tests queued). `canvas/reference/GCC_ILOs.md` holds all 47 GCC Institutional Learning Outcomes with their exact Canvas names.
- Portfolio site pages: `index.html`, `about.html`, `work.html` (repo root)
- Working notes / plans / study docs all live under `notes/` (one home)
- Instructional-design study guide: `notes/professional-development/instructional-design-study.md`
- Render ideas + AVC 248 pilot plans: `notes/render/` (RENDER_IDEAS.md, AVC248_RENDER_MASTER_PLAN.md, AVC248_Render_Backend_Options.md, AVC248_Jordan_Pilot_Email.md, AVC248_Claude_Pilot_Request.md)
- Portfolio redo plan: `notes/portfolio/PORTFOLIO_REDO_PLAN.md`
- DMA brochure draft: `notes/drafts/dma_brochure_content_draft.md`
- FEP: `fep/` (start at `fep/fep-2026.md`)
- AIRC SSS study: `airc-sss/WORKING-STATE.md`
- AVC 100 redesign: `avc100/`
- Master CV: `cultivate/cv.html`
- Command Center (PRIVATE self-PM view): `command/index.html` = public projects dashboard (singletrackmom.github.io/command, noindex + unlinked, 8 ranked projects with roadmaps/metrics/North Star). `command/todo.html` = git-ignored, LOCAL ONLY, holds this-week + personal/family tasks (never publish it). Rebuilt from TASKS.md on request ("update my dashboard"); auto-refresh task runs Sundays.
- Job search (PRIVATE, outside this repo): `~/Documents/Claude/JobSearch/`, resumes, cover letters, tracker, `BULLETPROOF_FORMAT_SPEC.md`, per-role application folders
- Scheduled job-search + family agents (PRIVATE): `~/Documents/Claude/Scheduled/`

## Who I am

I'm Michelle Blomberg, Residential Faculty in Digital Media Arts at Glendale Community College (GCC) in Glendale, Arizona, gccaz.edu, part of the Maricopa Community Colleges district. Not Glendale California. I teach AVC100, AVC182, AVC183, and AVC248. I was DMA Program Director 2011–2022, now faculty only. I co-chair the Student Support and Success domain on the Maricopa District AI Resource Committee (AIRC). 25+ years in higher ed, EdTech PM at ProQuest/XanEdu, led the campus LMS team and an LMS RFP in the Blackboard era, MEd from NAU on connectivism and PLEs. Targeting a transition into EdTech product management, ideally online and Colorado-friendly. GitHub: singletrackmom.

**ACCURACY GUARDRAIL (stop getting this wrong): What is true is on my CV (cultivate/cv.html), use that wording. I led the campus LMS team in the Blackboard era, co-chaired the district eLearning Advisory Group (which represented the ~250,000-user, 10-college system), and contributed to the RFP that led to Canvas adoption. I did NOT lead, own, or run the Blackboard-to-Canvas migration, and I was NOT on the migration team. NEVER write "led the migration," "scaled a platform to 250K users," or anything implying I personally migrated/ran a 250K-user platform. Also: I co-chair the Student Support and Success DOMAIN only, I do not lead the whole district AIRC.**

## Active projects

**CopaMigo**, Student-facing campus services routing tool for GCC, 14 service modules, bilingual EN/ES, 100+ verified GCC URLs. Live at singletrackmom.github.io/copamigo/. Status: prototype, dialing for summer. Maricopa AI CIO wants to see it. Open: course advising bug (AI invents AVC course names, see vocab below), Main/North campus selector, admin dashboard, usability testing, verifying Financial Aid / LGBTQ+ / Veterans / CARE-BIT modules. District redesign coming with school picker (localStorage) on first launch.

**Render (v0.3)**, Career services tool, all 7 phases built, single HTML, vanilla JS, Sonnet API, 15 AI functions. Auth is first name only, no PII, localStorage. Anonymous employer data flows to Career Services via Google Sheet (students are told). Resumes store no contact info. Hosted at singletrackmom.github.io/render/. Status: usability tested March 2026, pilot Fall 2026. Open: production hardening over summer.

**Cultivate (v1.3)**, My personal AI/EdTech PD hub. 6 interconnected pages, no backend, RSS feed pulling 62 sources with keyword classifier and 3-proxy waterfall. Plum/sage/rose/gold palette, Lora + DM Sans. Subdirectory of this repo. Status: stable. Future: possibly convert to Claude artifact with per-section update buttons.

**Rough Cut**, GCC DMA newsletter at singletrackmom.github.io/newsletter/. Visit form → Apps Script → dmarts@gccaz.edu + Google Sheet. Status: live, on personal account. Open: migrate to real HTML distribution via Mailchimp free tier, off personal account.

**AVC100 redesign**, 1-credit, half-semester foundation course. Single three-phase postcard project across Illustrator → Photoshop → After Effects. Embedded student services videos for easy points. Critique workflow via OBS / YouTube / Discord / Canvas. Built as IMSCC for import. Sunday/Wednesday due dates. Status: built, teaching last week of May.

**FEP (Faculty Evaluation Plan)**, due to the VPAA via the GCC dynamic form (employees.gccaz.edu/faculty-evaluation-plan) by **June 30, 2026**, internal target ~June 25 for signatures. The MASTER doc is `fep/fep-2026.md` (start there, it has a Control Panel at the top tracking status, team, deadline, and open items). The official section rubric (what each Required and Elective area must answer, plus the team and process rules) is `fep/fep-guidance.md`. The student-evaluation summary is `fep/fep-evaluations.html`. Structure: 3 Required Areas (Teaching/Learning/Service · Course Assessment/Program Development · Governance/Committee) + 2 Electives (Professional Development · Acquisition of New Skills), with Service to the Community / Career ILO / DEI as optional add-ons. It is reflective ("what I did, what I learned, where I am going"), NOT a list. FEP Resource Person: Lori Walk. Governed by RFA Article 18. When working on the FEP, read fep-2026.md AND fep-guidance.md first. Do not overclaim (LMS-team wording, "more than two decades," Domain 5 co-chair only); keep personal projects out.

**AVC183 (Digital Graphic Design 1)**, teaching practice to remember: for the BRANDING projects, students write their OWN client-discovery questions (I require them to generate the questions themselves, NOT with AI). Then they use AI as a FICTITIOUS CLIENT that answers those questions, so the client's responses steer their branding decisions the way a real client brief would. The questions and thinking stay theirs; AI plays the client they design against. NOTE: AVC183 starts Fall 2026; the historical course taught this cycle (e.g. in the FEP) is AVC181 Graphic Design I. Never say AI generates the questions or that students run AI surveys.

**Portfolio site (this repo root)**, singletrackmom.github.io. Restructured April 2026. Includes "Sommarverken" section (Swedish, no subtitle) with Google Cloud GenAI Leader training and League for Innovation AI Fellows Bootcamp cards, both in cultivate/ subdirectories. CopaMigo lives under Community & Student Services next to a Discord card.

**Maricopa AIRC committee work**, Co-chairing Student Support and Success domain. Summer deliverable: district usability study across all 10 colleges, tool inventory, service crosswalk (same functions, different names per college), standardized usability form covering staff workflow pain + student barriers. 5 hrs/week paid all summer. Form-building summer, fieldwork fall. Open question: Salesforce AI tool Maricopa declined for data reasons may be the real answer over CopaMigo, worth honest assessment.

**Mesa AI Summit**, "Building Career Tools That Outlast the Semester," virtual, May 18, 2026. Outline done, screenshots in progress, working with speech coach.

**Job search**, Targeting online EdTech PM. Acceptable in-person: CO, UT, NM, Flagstaff, Tahoe (NV side), Oceanside. Recent activity: EdPlus UX PM AI screening late April, Mary Lou Fulton adjunct app, Los Rios Director of Student Services Innovation role on radar. Master CV: singletrackmom.github.io/cultivate/cv.html, fetch this, don't ask me to upload.

**Job-search agent (source of truth = `Documents/Claude/Scheduled/daily-job-search/SKILL.md`).** Broadened beyond PM into all higher-ed / edtech: learning experience and instructional design, UX, AI-in-education, faculty development, program management, student success, plus attainable product roles. Sweeps every run: target edtech companies (Canvas/Instructure on Ashby, edX/2U, Coursera, Khan, Duolingo, D2L, Pearson, McGraw Hill, Cengage, Guild, Pathstream, Newsela, Handshake, PowerSchool, Ellucian, EAB, Top Hat, Turnitin, etc.), AI labs' education teams (Anthropic Claude for Education, OpenAI, Google for Education, Microsoft, CodePath), higher-ed orgs (EDUCAUSE, League for Innovation, OLC, WCET), ALL Colorado universities + Denver-area community colleges (NO Christian schools, skip Regis and Colorado Christian), Denver/Boulder local (Built In CO, onsite/hybrid OK), and AI-using nonprofits (Idealist, camps, museums, foundations). Discovery via Built In, LinkedIn, HigherEdJobs, EDUCAUSE, but the published link must always be the company's OWN careers page, verified live that day (a web search is not verification; Instructure is on Ashby not Lever). Salary: $80K hard floor for everyone EXCEPT CU Boulder and CSU (tuition-discount exception), $100K realistic, $150K target. Output is a CUMULATIVE dashboard (keeps still-live prior matches, sorted by fit, networking/reach group for 5+ yr formal-PM reqs, short subtitle, no methodology text) rebuilt daily to `Documents/Claude/JobSearch/Michelle_job_dashboard.html` AND the phone view at singletrackmom.github.io/jobs/ (noindex, unlinked, stealth). Applied so far: Guild Applied Learning Manager (6/17), Instructure Canvas CSM. Do not resurface applied roles in the apply-now list. FAVORITE LANE to rank high: "build-with-people" roles where I vibe-code, build agents, and help others build with AI, AI Solutions Engineer/Architect, Forward-Deployed Engineer, Developer Advocate / Developer Education, AI Enablement / Adoption / Trainer, Solutions or Implementation (Education), especially at AI labs (Anthropic, OpenAI, Google, Microsoft, CodePath) and AI-edtech companies. I am weighing consulting but prefer a salaried build-with-people role first.

**EXPANSION + REFRAME (June 19):** explode the feed beyond higher-ed PM. I have NO formal PM experience and feel stuck chasing "PM-wannabe" roles, so LEAD with my real strengths: learning experience / instructional design, UX research and UX SYSTEMS / service design (the AIRC SSS 10-college, ~140K-student usability + service-crosswalk study is the flagship), and AI-SYSTEMS building (Render, CopaMigo, Wayfinder are systems, not just tools). Broaden sectors well beyond higher ed: nonprofits, foundations, WORKFORCE development / economic mobility (JFF, Year Up, Per Scholas, Strada, Merit America, Climb Hire, Social Finance, Generation, Guild, National Skills Coalition), mission-driven and AI-for-good orgs, libraries / museums / science education, national labs outreach (NREL is in Golden, NCAR/UCAR + NIST in Boulder), associations (EDUCAUSE, ISTE, OLC, Digital Promise, New America), and broad-reach info/learning companies like ProQuest/Clarivate and ETS (ProQuest was never purely higher ed). NOT banks or pure finance. GEOGRAPHY widened: remote-first, but I am NOT married to Golden and would relocate for the right role to Carbondale / Roaring Fork Valley, Mancos / Durango / Cortez, Fruita / Grand Junction (Western Slope), or Flagstaff, on top of CO/UT/NM (I do not want to keep flying to Phoenix for years). EXCEPTION for a top-tier AI lab (Anthropic, OpenAI, and similar) or another dream job: I would relocate to the Bay Area / SF or anywhere in California, so surface their California onsite roles as real options. HARD GEOGRAPHIC NO: NYC and anywhere on the East Coast is out, even for a dream job, never surface East Coast onsite/commute roles (this killed the Instructure Senior Learning Consultant role, which needed a NYC commute). California yes for the right role; Utah and the West possible; East Coast never. Keep the $80K hard floor (target $150K).

## Family job-search agents (run for my family, not just me)

Five daily agents live at `Documents/Claude/Scheduled/<name>/SKILL.md` and publish to this repo. They are scheduled ~6 AM but I turn my computer off overnight, so they often miss the cron and need a manual run when I sign on. To run one, read its SKILL.md and execute it. Each keeps ALL still-live leads day to day (re-verify, drop only closed ones); not everyone applies daily.

**HANDS-OFF POLICY (June 19): Michelle should NOT spend her time running or iterating the family agents (she wasted hours doing that).** They run automatically and publish to their pages; if a run was missed because the computer was off, Claude runs them when she signs on, it is not her job. Family members can iterate their own page in their OWN Claude (Kevin's focus page has ready-to-paste prompts at the bottom for exactly this). **Michelle's OWN job search is now TWICE WEEKLY (Tue + Fri, cron updated), with a recurring 3:00-5:00 PM Mountain block on the shechelleb calendar for reviewing/applying; mornings are reserved for the League bootcamp + EDUCAUSE coursework. Apply only to strong fits, no daily pressure.**

- **Me** `daily-job-search` → `jobs/` (stealth, noindex). On the dashboard, flag what is NEW vs carried-over so I do not miss new ones; I have already looked up the old ones.
- **Kevin** `kevin-daily-job-search` → page is **`/focus/`** (renamed from /kevin/), titled "Focus," photography theme with a camera-lens SVG in the hero and subtle bike accents. NO email anymore, he just refreshes https://singletrackmom.github.io/focus/.
- **Devan** `devan-daily-job-search` → `summerwork/`.
- **Jillian** `jillian-find-your-flow` → `flow/`.
- **Jasper** `jasper-soar` → `soar/`.

**Kevin bike-brand memory (hard):** four bike brands sit ~1 mile from our house, **Revel, Commencal, Spot, Yeti**. Keep close watch on all four as photography outreach targets. His fit is staged PRODUCT / parts / frame / website shots and ARCHITECTURAL building photography (he is an architecture expert), NOT influencer or content-creator work (he applied to Revel's content-creator role but a following is not his thing). **ALCHEMY BIKES IS OUT OF BUSINESS (June 2026), never suggest it.** Watch for a possible Italian brand relocating to Golden (unconfirmed, confirm before listing). Bike-brand outreach copy should also offer to follow up for a shop ride out to Apex (our local trail) to stage action shots, AND offer professional event photography (covering races, team / sponsored-rider days, launches, since the brands all have sponsored riders), on top of the staged product/parts/frame and building photography. He is a professional event photographer, not the phone-clip content-creator type. **HARD PAY FLOOR: Kevin will not work for under $20/hour, no matter what.** Never surface sub-$20 or low per-gig work (the mortgage/field-inspection gig at ~$5-15 per inspection is OUT, removed). **Growth strategy for slow wedding years (a standing "growth ideas" section on his focus page):** build a Colorado-destination portrait business for visiting families and couples, beyond Denver/Golden/Boulder into Rocky Mountain National Park + Estes Park, Grand Lake, Winter Park, and Frisco/Breckenridge/Dillon. Get found via one web page per destination (ranks on Google AND feeds AI search like "Colorado portraits while on vacation"), a complete Google Business Profile with reviews, and Pinterest boards. Run Meta (Instagram/Facebook) ads to Texas (Dallas, Houston, Austin) and other feeder markets (OK, KS, NE, AZ, Chicago), plus Google Search ads for high-intent queries. Apply to host an Airbnb Photography Service (Airbnb relaunched Experiences + Services in 2025, photography is a category, stay-then-session hookup, NOT set up yet, real to-do). Use Adobe Stock to monetize his 20-year Colorado archive (we know someone who does Adobe Stock, warm intro). Build lodging/venue referral partnerships in the mountain towns (offline version of the Airbnb hookup). Pivot existing wedding contacts toward elopements + destination family sessions. Be realistic on too-good-to-be-true gigs (mortgage/field inspection like FAR is a real industry but pay is modest and per-inspection, work is inconsistent): keep them but label honestly as fill-in income and include the safety rule (never pay upfront or cash-and-wire).

**Jillian flow rules (hard):** every career edition MUST include a "How to get qualified" box with real, accredited, verified links, framed as a small first step. Prefer the least-school path and LOCAL Colorado community-college programs; if a 4-year degree is the only route, use a community-college transfer / 2+2 path (she is ADHD/school-averse and cost-smart, not chasing the hardest school). Check what employers actually require, never send her after something unattainable. PTA path = Arapahoe Community College (AAS). Personal trainer path = one NCCA-accredited cert (NASM/ACE), the local Community College of Denver NASM program, or Life Time Academy (note: some Life Time trainer roles prefer a degree, so start entry-level). Career lanes she specifically wants explored next: the many ways to use criminal justice, and how to become a paralegal (certificate/associate, not law school). PTA specifics: she has already attended the Arapahoe CC info session and toured Pima Medical Institute (Denver, ~18-mo associate, more money but Michelle would help pay) but has NOT applied; prereqs can be taken at Red Rocks CC (closest to the house). IMPORTANT framing: Jillian pulled back when she felt Michelle was deciding her life for her, so always present these paths neutrally as HER choice (coming from Flow, not Mom), low-pressure, next step is small and hers.

## Key people

- **Kevin**, my husband. We run Berg Berg Photography (bergbergphotography.com), wedding photojournalism. He's lead, I assist selectively.
- **Deb**, UX design instructor at ASU. I've been working to get an adjunct position with her so I can see how she teaches UX (informs my new AVC 2xx UX Design for Interactive Media course proposal) and get exposure to ASU's faculty tooling. ASU is an AI leader, every ASU connection is valuable for my future.
- **My Dean**, when I say "the Dean" I mean my GCC dean. Not a person named Dean.
- **Darrel Huish**, retired Maricopa CIO, reference.
- **Theresa Hilding**, Software Engineer, Maricopa, reference.
- **Kristin Bennes**, Student Services Advisor, PVCC, reference.
- **Maricopa AI CIO**, wants to see CopaMigo.

## Vocabulary

- **GCC** = Glendale Community College, Arizona (gccaz.edu). Never glendale.edu, never California.
- **Maricopa** = the 10-college district. MEID = Maricopa login.
- **DMA** = Digital Media Arts. Distinct from Animation/Time-Based Media. Both are AAS degrees. Department: Art and Humanities.
- **AVC course codes** = my courses. AI hallucinates these constantly, never trust training data for AVC course names. Always ask DMA vs. Animation first, then use only checksheet-verified courses.
- **ARC** = the Maricopa district **AI Resource Center** (it is a CENTER, never a "committee," and it is ARC, NOT AIRC, fix this everywhere). I co-chair its Student Support and Success domain (Domain 5). The district AI CIO / OIT AI lead is a tri-chair of the ARC. In any committee-facing or portfolio document, refer to people by TITLE (e.g. "the district AI CIO"), NEVER by personal name. **AIAC** = GCC's campus AI committee (I drafted the proposal). **DATA-GOVERNANCE HARD LINE:** any AI fix must collect NO student data / no PII. The district declined a vendor AI add-on (e.g. the Salesforce AI connector) specifically because it would collect student data, so the preferred path is BUILDING data-sovereign tools (the CopaMigo / Render no-PII model) over BUYING data-harvesting ones. "AI closing the gaps" can mean an agent, a bot, a tool we build, or something we buy/add on, always screened against that no-student-data line. **The `airc-sss/` FOLDER name stays as-is (the link was already shared); only the displayed committee name changes to ARC, never rename the folder.** **STAFF BUY-IN FRAMING (hard): the SSS domain members ARE advisors, financial-aid, and other support staff, so the study must read as making THEIR jobs easier, never replacing them. Frame automation as taking routine, repetitive work (easy factual questions, the "we'll get back to you in a few days" booking email) off staff so they focus on individual problems and human connection. No one is replaced. Do NOT call things "staffing problems."**
- **CTLE** = Center for Teaching, Learning and Engagement.
- **Sommarverken** = Swedish, "summer works." Section of my portfolio. No subtitle, leave it.
- **Render, Cultivate, CopaMigo, Rough Cut** = project codenames, capitalize them.
- **PRD** = Product Requirements Doc. Render's is green, Cultivate's is plum.
- **Cowork** = the assistant I'm using when I open this file. Calendar/Gmail hooks, project context, ADHD nudges.

## Through-lines

- **Tools that outlast the semester.** Students should leave with something they keep using, a resume, a routing map, a habit, not just a grade.
- **No PII, minimum data.** First names, localStorage, anonymized aggregates. Tell students what's collected and why.
- **Data-informed iteration.** Usability test, pilot, revise. Render's Fall pilot is the model.
- **Stackable, modular, low-lift adoption.** Designs that fit existing course structures, IMSCC imports, no new platforms required.
- **Connectivism / PLEs.** The theoretical floor under everything. Networks of people and tools beat closed systems.
- **AI as scaffolding, not replacement.** AI helps students rehearse interviews, navigate services, draft and revise, humans still decide.

## My voice

- Direct. No em dashes (reads AI-generated). No "genuinely," no "straightforward," no overly formal phrasing.
- Conversational, not corporate. Contractions are fine. Sentence fragments are fine.
- Kind but improvement-focused, especially in student feedback.
- Show me proposed changes before editing files.
- Zipped downloads preferred (files otherwise open in the browser). Only zip changed files unless replacing the whole site.
- For planning, memory is usually enough. For code changes, I'll upload the specific HTML file.
- **I do NOT use Terminal, ever, and I am not comfortable with it.** Any time a step needs Terminal (git commit/pull/push, etc.), always walk me through it exactly: how to open Terminal (Spotlight: Command+Space, type "Terminal", Return), and the precise commands to paste, one block, with what each does in plain words. Never assume I know a command or where to run it. Offer a copy-paste block.

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
- Dates flush right (right tab). No em dashes anywhere. Curly quotes and apostrophes. Header shows name, Golden, Colorado, email, and michelleblomberg.com (the real domain, NOT the github.io address). Never invent URLs (no github.com/singletrackmom).
- Cover letter: formal business-letter format (letterhead, date, recipient block, "Dear...", "Sincerely"). Do NOT mention proximity to the employer's city; the address already shows location. Avoid "genuinely," "straightforward," and casual asides.
- **REQUIREMENTS-MATCH TECHNIQUE (use on EVERY cover letter, this is what beats the AI/ATS screen, Michelle loves it):** include a clearly-labeled mapping block (e.g. "How I meet what you are looking for") that addresses EVERY minimum qualification in the job description, one bold lead-in per requirement, answered in Michelle's OWN words (never lift the JD's phrasing, that reads AI-written). A human screener can then check every box in seconds. CRITICAL companion step: the ATS usually scans the RESUME, not the letter, so for each requirement make sure the real keywords (the exact skill names/terms the posting uses, wherever genuinely true) ALSO appear naturally in the resume (Technical Skills + bullets). So: cover letter = explicit human-readable mapping; resume = keyword coverage; the two reinforce each other on every requirement. The Anthropic CSM build (June 19) is the reference example.
- Leave out dated or irrelevant certifications (for example the 2014 Quality Matters certificate). The current Quality Matters / OSCQR lead-reviewer service role is fine to keep.


### Resume formatting (LOCKED, every time, do not relitigate)

- ONE entry format across ALL sections (experience, projects, education, certifications, presentations, awards, service): the TITLE comes first and is the only bold text, then a comma, then the organization in regular weight, and the date sits alone in its own right-aligned column. Pattern: **Title**, Organization [tab to right] Date.
- Only the title, role, or credential name is bold. Organizations are never bold, anywhere, including education and certifications.
- Dates are ALWAYS right-aligned in one consistent column, on every entry. Never put a date in parentheses, never inside the body of a line. Ranges use an en dash with spaces (for example, 2011 to Present).
- DATE-ON-TOP-LINE RULE (hard, Michelle asked for this June 23): the date ALWAYS sits on the TOP line at the right margin and NEVER drops to a second line. When the title plus organization is too long to fit beside the date on one line, break it between the TITLE and the ORGANIZATION: keep the bold title and the date together on the top line, and move the organization down to its own line below. Only the organization moves, never the date.
- Separators inside a line are commas. Never middots, pipes, or bullet characters in the middle of a line.
- Experience entries: the Title, Organization line, then an italic line for any prior title and the location, then accomplishment bullets that show the skills through concrete results.
- Technical Skills: a bulleted list at the very bottom, each bullet leads with a bold category label before the colon, and the categories align to the target job.
- Education and Certifications: same Title, Organization format, organization not bold, no bullets.
- Headings and entry titles use keep-with-next so a heading or job title never strands alone at the bottom of a page; it breaks to the next page instead.
- Full 3 pages. Calibri. Name centered at the top, contact line beneath it: Golden, Colorado, email, michelleblomberg.com. No em dashes. Curly apostrophes and quotes.
- City and state for a job go on an italic line directly under the title, unless they fit on the title line without pushing the date to wrap. No period after the state.
- When an entry has two date ranges, list them in ascending order with the range ending in "Present" on the RIGHT (for example, 2010 to 2016, 2025 to Present).
- Be honest about status: label tools still in progress as prototypes or "in testing," never imply production. Do not use numbers Michelle cannot verify (no invented percentages or counts); if unsure, say "improved" without a figure.
- Only list skills Michelle actually uses; remove anything she does not recognize. Split genuinely different categories (for example, Data and analytics separate from Accessibility). Technical-skill bullets lead with a bold category label before the colon.
- Page breaks: every page must BEGIN with a title (the name header, a job title, or a section heading), never an orphaned bullet or a lone heading. A small gap at the bottom of a page is fine and is preferred over an awkward break; force a page break before a role if needed, and keep the Certifications block whole. Tighten spacing (margins and paragraph spacing) to hold three pages.
- The cover letter header is CENTERED to match the resume (centered name, centered contact line), then the date and recipient block are left-aligned. The contact line separates items with spaces, no middots.
- COVER LETTER BUSINESS-LETTER FORMAT (hard, Michelle called this out repeatedly, use EVERY time): NO rule/line/border under the header (name + contact line only, nothing underneath, same for the resume header). After the header, the body is a standard block business letter, left-aligned, in this exact order with ONE blank line between blocks and NO blank lines inside the recipient address block: (1) date; (2) recipient address block as FOUR TIGHT lines with NO blank lines between them and NO "Human Resources"/"Attn"/department line: organization/office name (the real one, e.g. "Mines Online"), then the parent institution, then the street address, then "City, ST ZIP" (look up the real address); (3) salutation "Dear Hiring Committee:" with a COLON; (4) a subject line "RE: [exact job title]" with the title in bold; (5) the body paragraphs; (6) "Sincerely," then the name. EXACTLY one blank line after the date and one blank line before the salutation; zero blank lines inside the four-line address block. Full locked detail (and the generator spacing rule) is in JobSearch/BULLETPROOF_FORMAT_SPEC.md. NEVER open a cover letter with any version of &ldquo;I have been watching for a role like this&rdquo; or any eager or informal hook. Michelle finds it lame and desperate. It is a formal business letter: open with the single most important, most relevant qualification that establishes she is the ideal candidate, stated as fact and evidence, without ever writing &ldquo;I am the perfect candidate,&rdquo; and without mentioning proximity to the employer&rsquo;s city. Her BACHELOR'S IS NOT in education (it is a BFA in Visual Communications), so never say "my degrees are in education"; let the M.Ed. in educational technology carry the degree requirement and frame the BFA as her user-experience and design foundation.
- To reuse: copy `RESUME_FORMAT_generator.js`, keep every helper (head, entry/entK/entKB, ent, sub, b, skill) and all the spacing and margin values exactly, and only swap the content inside the calls. Build with `npm install docx` then `node`, convert to PDF with the docx skill's soffice script, and verify page breaks with `pdftotext -layout`.

- **WHERE FINAL RESUMES AND COVER LETTERS LIVE (canonical, set June 29):** every final resume and cover letter goes in ONE home, `Documents/Claude/JobSearch/`, with a per-company subfolder named `<Company>_Application/` (e.g. `JobSearch/Playlab_Application/`). Each subfolder holds the final `Blomberg_Resume_<Company>.docx` + `.pdf`, `Blomberg_CoverLetter_<Company>.docx` + `.pdf`, and that build's generator `.js`. Do NOT scatter final apps into `Documents/Claude/Applications/` anymore. Keep build junk (chk*.png, *.tmp, lock files, node_modules) OUT of the final subfolder. The reusable master template `RESUME_MASTER_BOMBPROOF.js` is a tool, not an application, and stays in `Documents/Claude/Applications/`. Consolidated existing apps (CodePath, Per Scholas, WGU, Anthropic, Guild, GCC Dean, Playlab) into JobSearch on June 29.
- **PREFERRED REFERENCE BUILDS (Michelle's favorite format):** the Per Scholas and WGU applications (June 2026) are the best examples, not the Anthropic one. They nail the requirements-match cover letter (a labeled block mapping every minimum qualification, answered in her own words) plus matching keyword coverage in the resume. Model new applications on those.
- **FROZEN BOMBPROOF TEMPLATE (use this, do NOT re-engineer formatting ever again):** the locked, fully-dialed generator is saved at `Documents/Claude/Applications/RESUME_MASTER_BOMBPROOF.js` (and mirrored at `RESUME_FORMAT_generator.js`). It already encodes every hard-won formatting decision: 2-cell borderless table per entry; an ADAPTIVE per-entry date column (date cell sized to its own date, right edge flush at the content margin so ALL dates align in one column and never wrap to a second line); long titles wrap with the date staying top-right; ALL text black, NO grey anywhere; even section/entry spacing; most-recent-first in every section; Calibri; presentations use org-on-its-own-second-line (no comma on the title line) when long. **For the next resume: COPY RESUME_MASTER_BOMBPROOF.js, swap ONLY the content, rebuild docx then PDF, and do a quick visual (pdftoppm to PNG) to confirm. Do NOT rebuild or relitigate the layout, spacing, date logic, or colors. The Anthropic build (June 19) is the reference output.**
