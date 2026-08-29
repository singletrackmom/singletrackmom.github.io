# CLAUDE.md, context for working with Michelle

You are opening this folder in Cowork mode with no memory of prior sessions. Read this first. It is the briefing.

> ## 🧭 THIS FILE IS A ROUTER, NOT A RULEBOOK
>
> **Claude orchestrates. The skills and agent files hold the instructions.** This file carries who Michelle is, the accuracy guardrails, her voice, and a map of where everything lives. It does **not** hold design specs, resume formatting, or agent procedures. Those live in the files below and those files win.
>
> Restructured 28 Aug 2026, after 275 lines of duplicated agent instructions in this file drifted out of sync with the skills that already owned them and produced a day of wrong work.
>
> **When you are asked to do X, INVOKE the skill named below.** A name in `code` with the word "skill" is a real, invocable Cowork skill. A path is a file to open with the Read tool.
>
> | Asked to&hellip; | Use this |
> | --- | --- |
> | Build, edit, or review **any page on the site** | the `website-style-guide` skill, then the `page-builder` skill |
> | Write a **PRD** | the `prd` skill |
> | **Start any new build** | the `research-first` skill |
> | Write a **resume or cover letter**, or apply to a job | the `job-application-builder` skill, plus **`cultivate/cv.html`** |
> | Decide **whether a job is worth applying to** | the `job-fit-assessment` skill |
> | Anything about her **job history, titles, dates, accomplishments** | **`cultivate/cv.html`. Always. See rule zero below.** |
> | Run or fix **her job search** (the Tue/Fri dashboard run) | `jobs/JOB_AGENT_RULES.md` |
> | Run or fix the **DMA student jobs Discord** | the `dma-jobs` skill, and `discord/DMA_JOBS_AGENT.md` |
> | Run or fix a **family job agent** (Kevin, Devan, Jasper) | `agents/FAMILY_AGENTS.md` |
> | Run **Jillian&rsquo;s job page** | the `jillian-job-search` skill |
> | Build or revise **one course module** | the `course-dialer` skill |
> | Build a **whole course from outcomes or OER** | the `build-a-course` skill |
> | Find **OER for a course** | the `oer-course-finder` skill |
> | Refresh the **assessment reference library** | the `assessment-library-refresh` skill |
> | Know **what is going on right now** | `TASKS.md`, which opens with a where-things-live index |
> | Resume the **student journey study** | `airc-sss/WORKING-STATE.md`, then `airc-sss/BARRIER_REGISTER_2026-08-27.md` |
> | Work on the **FEP** | `fep/fep-2026.md` and `fep/fep-guidance.md` |
> | Work on a **course** | `canvas/avc183/AVC183.md` or `canvas/avc248/AVC248.md`. One markdown per course. Never create a second. |
> | Fix the **domain or the site being down** | `tools/DNS_michelleblomberg.md`. Check the `CNAME` file first. |

---

> ## 🧩 HOW SKILLS WORK HERE. READ THIS BEFORE LOOKING FOR A SKILL FILE.
>
> **Skills live in Cowork&rsquo;s own skill store, NOT in this repo.** They are invoked by name with the Skill tool. You will see them listed as available skills at the start of a session.
>
> **There is no `.claude/skills/` directory in this repo any more.** It was deleted 29 Aug 2026. It held seven skills with perfect frontmatter that Cowork **never loaded**, because Cowork reads its own store and not a mounted folder&rsquo;s `.claude/skills/`. That is the root cause of the recurring &ldquo;I don&rsquo;t have access to that skill&rdquo; error: the file was readable, so a session would open it as plain text and then run the work inline in the chat instead of inside the skill. Seven skills looked real and none of them were.
>
> **The skill files you can see at a `/var/folders/&hellip;/skills/` path are a READ-ONLY CACHE.** Editing one there changes nothing. **The only way to change a saved skill is the `save_skill` tool with `overwrite: true`.** Past sessions &ldquo;fixed&rdquo; skills by editing that cache and the fixes silently evaporated. That is a second source of the drift.
>
> **The division of labor, and it is not negotiable:**
>
> | Where | What lives there |
> | --- | --- |
> | **The skill** (Cowork store) | The PROCEDURE. How to do the thing. Stable, rarely changes. |
> | **The repo** | The DATA and the RULES that change often (`jobs/JOB_AGENT_RULES.md`, `cultivate/cv.html`, the course markdowns). The skill points at these by path. |
> | **`CLAUDE.md`** (this file) | A ROUTER ONLY. Who Michelle is, the accuracy guardrails, her voice, and the map above. **No procedures. No design specs. No agent instructions.** |
> | **`TASKS.md`** | STATE. What is open, what is done, what is next. |
> | **Scheduled tasks** (`~/Documents/Claude/Scheduled/<name>/SKILL.md`) | POINTERS ONLY to a repo rules file. Never a second copy of the rules. Openable by full path with the Read tool even though the folder cannot be mounted. |
>
> **Never state a rule in two places.** If a rule needs changing, change it in the one file that owns it. Three files claiming authority over the job agent cost a full day of wrong work on 28 Aug 2026.

---

> ## 🧹 STAY TIDY. THIS IS A STANDING RULE, NOT A ONE-TIME CLEANUP.
>
> Michelle&rsquo;s words, 29 Aug 2026: *&ldquo;You have a habit of creating a new markdown instead of looking for a markdown that already exists.&rdquo;* She is right. Before writing any file:
>
> 1. **LOOK FIRST.** Search the project&rsquo;s directory for an existing markdown. `ls` it. Read the where-things-live index in `TASKS.md`.
> 2. **ONE MARKDOWN PER PROJECT, INSIDE THAT PROJECT&rsquo;S OWN DIRECTORY.** If one exists, **append to it.** Never create a second, not a notes file, not an outline file, not a scratch file, not a dated file, not a `_v2`.
> 3. **No new file at the repo root**, and nothing dumped loose into `notes/`. A project gets a directory.
> 4. **No `.bak`, `.pre-*`, `_tmp*`, or `_old` files.** Michelle reviews diffs in GitHub Desktop; that is the version history.
> 5. **A finished document is HTML on the site design system**, not a markdown, not Word, not Excel. Markdown is for working notes only.
> 6. **When something new IS made, add a row to the where-things-live index in `TASKS.md` the same day.** She should never have to remember a filename.
>
> **Published paths are load-bearing.** 35 of the top-level directories are live GitHub Pages URLs. **Never move or rename a directory that contains an `index.html`** without being asked; those links are on her resume and in things she has already sent.

---

> ## 📄 RULE ZERO: READ THE CV BEFORE ANY CLAIM ABOUT HER BACKGROUND
>
> **`cultivate/cv.html` is the single source of truth for job history, titles, dates, and accomplishments.** Open the actual file. Never work from the summary below, and never assert a gap in her experience without searching the CV for it first. When briefing a subagent, **paste the relevant CV text into the brief**; a subagent cannot reliably fetch the public URL.
>
> **What this prevents:** on 28 Aug 2026 an agent rule claiming she has &ldquo;no formal PM title history&rdquo; produced a page of wrong job ratings, scored a community-college Academic Dean at 2 stars when she exceeds both its minimum and preferred bars, and removed 22 roles on a false premise. The CV says **Product Manager, Higher Education, ProQuest/XanEdu, 1999 to 2002** and **Director of Instructional Technology, GCC Innovation Center, 2004 to 2011.**
>
> Her words: **&ldquo;I can&rsquo;t rely on just my faculty position to get me into these jobs because they want someone actually doing this work as their job. Rely on my committee assignments and extra projects.&rdquo;**

---

## Who I am

Michelle Blomberg, Residential Faculty in Digital Media Arts at Glendale Community College (GCC) in Glendale, **Arizona**, gccaz.edu, part of the Maricopa Community Colleges district. Not Glendale California. I teach AVC100, AVC182, AVC183, and AVC248. DMA Program Director 2011 to 2022, now faculty only. I co-chair the Student Support and Success domain of the Maricopa district AI Resource Center. 25+ years in higher ed. MEd from NAU on connectivism and PLEs, BFA in Visual Communications. I live in Golden, Colorado. GitHub: singletrackmom. Targeting a transition into online, mission-driven EdTech, learning experience, UX systems, or AI-build roles, ideally Colorado-friendly.

### Accuracy guardrails, hold these

**LMS and the district.** I led the campus LMS team in the Blackboard era, co-chaired the district eLearning Advisory Group (which represented the ~250,000-user, 10-college system), and contributed to the RFP that led to Canvas adoption. I did **NOT** lead, own, or run the Blackboard-to-Canvas migration, and was **NOT** on the migration team. Never write &ldquo;led the migration&rdquo; or &ldquo;scaled a platform to 250K users.&rdquo; I co-chair a **domain**, not the whole ARC.

**The Design Studio.** I started it as a course and taught and led it from 2011, a real credential, past tense. Present it as **ending 2023** and say it &ldquo;lives on as a grant-funded, paid studio led by other faculty.&rdquo; Never say I lead, run, relaunched, or currently advise it, and never date it to Present.

**The Traveler.** I am the **design** faculty advisor only, since 2011, coaching the student design team through branding, typography, print production, and launch. Nothing to do with the editorial side or the art-contest judging. The award is the **College Media Association Pinnacle Award for College Literary Magazine** (2015, 2016, 2025), never &ldquo;Literary Magazine of the Year.&rdquo; Also a repeat AIGA Best of Phoenix selection, 2017 to 2022.

**Status honesty.** Render is a prototype heading toward a Fall 2026 pilot. CopaMigo is an early prototype in testing. Nothing is in production. Do not imply production or use numbers I cannot verify.

**AVC course codes.** AI hallucinates these constantly. Never trust training data. Ask DMA versus Animation first, then use only checksheet-verified courses.

---

## Active projects

**Render (v0.3)**, career services tool, 7 phases, single HTML, vanilla JS, Sonnet API. Auth is first name only, no PII, localStorage. Usability tested March 2026, pilot Fall 2026. Hosted at singletrackmom.github.io/render/.

**CopaMigo**, student-facing campus services routing for GCC, 14 modules, multilingual, 100+ verified GCC URLs. Prototype. The Maricopa AI CIO wants to see it.

**Cultivate (v1.3)**, my AI/EdTech PD hub, 6 pages, RSS feed across 62 sources. Stable. **Holds the master CV.**

**ARC student journey study**, the ten-college usability and service-crosswalk study. Live work in `airc-sss/`.

**AI Community of Practice**, launching. `community-of-practice/`.

**GCC Cares Hub**, I lead the brand identity, with a student running production through a paid 300-hour AmeriCorps internship.

**STEAMworks Center**, new STEAM and creative-media space, identity project in progress.

**AVC100 redesign**, built and taught. The central move is a student success module inside every course module, tied to institutional learning outcomes.

**FEP**, due to the VPAA by 30 June 2026. Master doc `fep/fep-2026.md`.

**Rough Cut**, GCC DMA newsletter. Live, needs migrating off my personal account.

---

## Key people

- **Kevin**, my husband. We run Berg Berg Photography, wedding photojournalism.
- **Deb**, UX design instructor at ASU. Working toward an adjunct position with her.
- **The Dean** means my GCC dean, not a person named Dean.
- **Darrel Huish**, retired Maricopa CIO, reference. **Theresa Hilding**, Software Engineer, Maricopa, reference. **Kristin Bennes**, Student Services Advisor, PVCC, reference.

## Vocabulary

- **GCC** = Glendale Community College, **Arizona**. Never glendale.edu, never California.
- **Maricopa** = the 10-college district. **MEID** = Maricopa login.
- **DMA** = Digital Media Arts, distinct from Animation/Time-Based Media.
- **ARC** = the Maricopa district **AI Resource Center**. A center, never a &ldquo;committee,&rdquo; and ARC not AIRC. I co-chair its Student Support and Success domain (Domain 5). In any committee-facing or portfolio document, refer to people by **title**, never by personal name. The `airc-sss/` folder name stays as-is; only the displayed name changes.
- **AIAC** = GCC&rsquo;s campus AI committee.
- **Data-governance hard line:** any AI fix must collect **no student data and no PII**. The district declined a vendor AI add-on specifically because it would collect student data, so building data-sovereign tools beats buying data-harvesting ones.
- **Staff buy-in framing:** the SSS domain members **are** advisors and support staff, so the study must read as making their jobs easier, never replacing them. Frame automation as taking routine work off staff. No one is replaced. Never call anything a &ldquo;staffing problem.&rdquo;
- **Syllabus+** = where I write all my syllabi, fresh every semester. **Rules only, never assignments.** It does not export from Canvas, so any `syllabus.html` inside an `.imscc` is stale. Never draft one, never call a missing syllabus a blocker.
- **CTLE** = Center for Teaching, Learning and Engagement. **Sommarverken** = Swedish, &ldquo;summer works,&rdquo; a portfolio section, no subtitle.
- **Render, Cultivate, CopaMigo, Rough Cut** are codenames, capitalize them.

## Through-lines

- **Tools that outlast the semester.** Students leave with something they keep using.
- **No PII, minimum data.** First names, localStorage, anonymized aggregates.
- **Data-informed iteration.** Usability test, pilot, revise.
- **Stackable, modular, low-lift adoption.** Fits existing course structures, no new platforms.
- **Connectivism and PLEs.** The theoretical floor under everything.
- **AI as scaffolding, not replacement.** Humans still decide.

---

## My voice

- **Concise above all.** No filler, no explanatory boxes or hints I did not ask for. Say the thing and stop.
- Direct and conversational, not corporate. Contractions and sentence fragments are fine.
- **Never use em dashes.** Commas, periods, parentheses, or the middot.
- **Always curly quotes and apostrophes**, never straight quotes or prime marks.
- Avoid &ldquo;genuinely&rdquo; and &ldquo;straightforward.&rdquo;
- Kind but improvement-focused, especially in student feedback.
- **Push back on me.** Play devil&rsquo;s advocate first: name the weakest points, the hidden cost, or a simpler alternative before we commit. Skip flattery and &ldquo;great idea&rdquo; openers.
- **Show me proposed changes before editing files.**
- Zipped downloads preferred, and only zip changed files.

## House style, applies to everything I make

Full web specifics live in the `website-style-guide` skill. These apply everywhere, including documents, decks, and boards:

- **Solid colors only, from a defined palette. Never gradients.** I am a graphic designer and blends look muddy and AI-generated.
- **Never justify body text.** Always left-aligned, ragged right. Everywhere, every format.
- **GOAL, AUDIENCE, PROCESS on everything, forever.** Every project, tool, agent, PRD, and portfolio card states all three, clearly labeled. Same structure I require of my students.
- **Be honest about status.** Label prototypes as prototypes.
- **PRDs and documents are HTML pages**, never Word or Excel. Never link a downloadable document on the site.
- **Social sharing images are PNG, never SVG.** LinkedIn will not render an SVG preview.

## Don&rsquo;t include

No student grades, no FERPA-protected info, no Canvas submission content, no login credentials, no API keys, no personal financial details, no family medical info. If unsure whether something belongs in a working file, ask.

---

## ⛔ NEVER RUN GIT. EVER.

No `git commit`, no `git add`, no `git push`, no `git` anything, ever. **I do all committing and pushing myself.** Command-line commits from a session on 21 Jul 2026 spammed `.git` lock files, corrupted HEAD, crashed GitHub Desktop, and rolled my working tree back, costing uncommitted work.

**Never give me Terminal instructions.** Do not mention Terminal, do not hand me git commands, do not offer a copy-paste block. I do not use Terminal and I am not going to start. When files are saved, tell me they are saved and stop. I want to see changed files on the **left** in GitHub Desktop, then I push on the **right**. That is the whole flow. If something truly cannot be done without a command line, say so plainly and let me decide.

## Working files

**Repo:** `/Users/michelleblomberg/Documents/GitHub/singletrackmom.github.io`. When I say &ldquo;the repo,&rdquo; &ldquo;my docs,&rdquo; or &ldquo;my github,&rdquo; I mean this folder. Edit in place, never write to a scratch directory and ask me to copy-paste.

**Outside the repo, private:** job search at `~/Documents/Claude/JobSearch/` (resumes, cover letters, the tracker, per-company application folders). Scheduled agents at `~/Documents/Claude/Scheduled/`.

**Private in-repo:** `command/index.html` is my projects dashboard (noindex, unlinked). `command/todo.html` is git-ignored and local only, never publish it. `jobs/index.html` is my stealth job page, noindex and unlinked, and **is never wiped**.
