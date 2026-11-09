# CLAUDE.md, context for working with Michelle

A router, not a rulebook. Who Michelle is, the guardrails, her voice, and where everything lives. Procedures live in skills; data and project notes live in each project’s one markdown file. Full history of this file: `~/Documents/Claude/JobSearch/_tasks/CLAUDE-archive-2026-11-08.md` (private).

## Token rules (set 8 Nov 2026)

1. **One chat per task.** When the topic changes, Michelle starts a new chat. Say so if a chat has drifted across many topics.
2. **Work only in the project named.** Open that project’s folder and its one markdown. No repo-wide searches or reads unless asked. Read line ranges or grep, never a whole large file.
3. **One copy of everything.** No private mirrors, backups, `_v2`, dated or scratch copies.
4. **Keep the always-loaded files small:** this file under 10 KB, `TASKS.md` an index of project titles with links only. Details go in the project’s own markdown.

## Router

| Asked to… | Use |
| --- | --- |
| Build, edit or review any site page | `website-style-guide` skill, then `page-builder` skill; site rules in `portfolio/PORTFOLIO.md` |
| Write a PRD | `prd` skill |
| Start any new build | `research-first` skill |
| Resume, cover letter, apply | `job-application-builder` skill plus `cultivate/cv.html` |
| Is a job worth applying to | `job-fit-assessment` skill |
| Her history, titles, dates | `cultivate/cv.html`, always (rule zero below) |
| Job search run | `jobs/JOB_AGENT_RULES.md` |
| DMA jobs Discord | `dma-jobs` skill, `discord/DMA_JOBS_AGENT.md` |
| Family job agents | Jillian’s page: `jillian-job-search` skill |
| Any course, module, assignment or Canvas package | `course-build-standard` skill, then the course’s `canvas/<course>/<COURSE>.md`. Shared Module 0 and shell: edit `canvas/_shared/module0.html` or `tools/course-build/build.py`, run `python3 tools/course-build/build.py --all`. Canvas HTML format: unzip the course `.imscc`, never guess from site CSS |
| One module / whole course / OER | `course-dialer` / `build-a-course` / `oer-course-finder` skills |
| Assessment reference library | `assessment-library-refresh` skill |
| Portfolio v2 | `portfolio/PORTFOLIO.md`, the START HERE block |
| What’s open now | `TASKS.md` (index) |
| Grants · journey study · FEP | `~/Documents/Claude/JobSearch/_Grants/AI_Studio_NSF_ATE_Plan.md` · `~/Documents/Claude/ARC-SSS/` and `airc-sss/` · `fep/` (frozen) |
| Domain or site down | `tools/DNS_michelleblomberg.md`, check `CNAME` first |
| Accessibility | `tools/ACCESSIBILITY.md`, then `tools/design-lint.py` and `tools/a11y-lint.py` |
| Call anything done | run `python3 tools/preflight.py` and report the result; plan of record `tools/QUALITY_SYSTEM.md` |

New pages start from `tools/templates/page.html` or `tools/templates/tool.html`.

## Skills

Skills live in Cowork’s skill store and are invoked by name. Copies at a `/var/folders/…/skills/` path are a read-only cache: editing them changes nothing. Change a skill only through the skill-saving tool. Procedure lives in the skill; rules and data that change often live in the repo file the skill points to. Never state a rule in two places.

## Tidy

Look for an existing markdown before writing one. One markdown per project, inside its folder. No new files at the repo root or loose in `notes/`. No `.bak`, `.pre-*`, `_tmp`, `_old`. Finished documents are HTML on the site design system. Add any new project to `TASKS.md` the same day. Never move or rename a folder with an `index.html` without asking; those URLs are on her resume.

## Public by default

Every committed file is served at its URL (`.nojekyll`, public repo). Private means not committed: it goes in `~/Documents/Claude/<Project>/` on her Mac (any subfolder mounts; `Scheduled` cannot). Do not switch to Jekyll. Never commit phone numbers, personal emails, credentials, family, health, money, appointments, or named third parties. `python3 tools/publish-guard.py` blocks inside preflight; a deliberate public file goes in `tools/publish-allow.txt` with a reason.

**Frozen:** `fep/` is the submitted FEP. Never edit, restyle, move or lint-fix anything in it until Michelle says (about 2029). Exclude it from every repo-wide find-and-replace. `tools/frozen-guard.py` enforces it; re-freeze only on her explicit request.

## Rule zero: the CV and the site are the truth

Read `cultivate/cv.html` before any claim about her background; paste the relevant CV text into any subagent brief. The website is the source of truth for project status: one label per project everywhere, and when a status changes on the site, change the CV in the same pass. If two places disagree, ask her, then fix both.

| Project | Label |
|---|---|
| Render | Pilot (in phases), starting with resume alignment; full tool once the district turns on student Gemini. No AI service behind it, no names collected |
| CopaMigo | Pilot, in the DMA Discord. Claude API. 24+ service areas, 100+ verified links |
| Dial Your Course v1 | In use in DMA |
| Dial Your Course v2 | In development (model-assisted review, designed to run in the instructor’s own Gemini account) |
| Syllabus Checker | In use in Art and Humanities |
| AI Opportunity Pipeline | Built, not yet launched; off résumés unless the job is about intake |
| Student Journey Barriers Study | In progress, phase one complete, no published findings |
| Gemini Access Study | Complete |
| AI pilot framework | Adopted (revised and released district-wide by the district AI CIO) |
| AI Community of Practice | Active, monthly |
| Digital Media Discord · jobs feed · family agents | Live · in production · in production |
| Wayfinder | Finished |

Fixed facts: pool mural 95 feet, internship 120 hours, emergency move online more than 45 faculty.

## Who I am

Residential Faculty, Digital Media Arts, Glendale Community College, Glendale, **Arizona** (gccaz.edu, Maricopa). Program Director 2011 to 2022. Co-chair of the Student Support and Success domain (Domain 5) of the Maricopa AI Resource Center. MEd NAU (connectivism, PLEs), BFA Visual Communications. Lives in Golden, Colorado. GitHub: singletrackmom. Targeting online, mission-driven EdTech, learning experience, UX systems or AI-build roles, Colorado-friendly.

### Accuracy guardrails

- Led the campus LMS team in the Blackboard era, co-chaired the district eLearning Advisory Group, contributed to the RFP that led to Canvas. Did **not** lead or run the Canvas migration and was not on the migration team. Never “led the migration” or “scaled a platform to 250K users.”
- Co-chairs a **domain**, never the whole ARC. ARC = AI Resource **Center**.
- Design Studio: founded it as a course, taught and led it 2011 to 2023. Now grant-funded and led by other faculty; she is one of several advisors.
- The Traveler: design faculty advisor only, since 2011. Award: College Media Association Pinnacle Award for College Literary Magazine (2015, 2016, 2025), never “Literary Magazine of the Year.” AIGA Best of Phoenix 2017 to 2022.
- Status honesty: use the table above. Never “built,” “tested” or “first pass” for the pipeline. No numbers she cannot verify.
- AVC course codes: never trust training data. Ask DMA versus Animation first.
- Data governance: AI work collects no student data and no PII. Frame automation as taking routine work off staff; no one is replaced; never a “staffing problem.”

## Two voices

| Where | Voice |
| --- | --- |
| Chat with Michelle | Direct, conversational, concise. Contractions and fragments fine. Push back first: weakest point, hidden cost, simpler alternative. No flattery. Show proposed file changes before editing. |
| Anything others read (site, Canvas, PRDs, resumes, LinkedIn, committee or district documents) | Formal and professional. Headings are short noun phrases, no periods, no questions. No chat vocabulary. Instruction, not reassurance. Contractions sparingly in student-facing prose, none in committee, portfolio or employer documents. `tools/prose-lint.py` reports (does not block). |

Everywhere: no em dashes; curly quotes and apostrophes; never “genuinely” or “straightforward”; never justify text.

## House style

Solid colors from a defined palette, never gradients. Goal, Audience, Process on every project, tool, agent, PRD and portfolio card. PRDs and documents are HTML pages, never Word or Excel; no downloadable documents on the site. Social images are PNG. No faculty, colleague or family names anywhere in the repo (roles only); the online CV may keep names. No grades, FERPA data, Canvas submissions, credentials or financial or medical details.

## Vocabulary

GCC = Glendale Community College, Arizona. Maricopa = the 10-college district; MEID = Maricopa login. DMA = Digital Media Arts (not Animation). AIAC = GCC’s campus AI committee. CTLE = Center for Teaching, Learning and Engagement. Syllabus+ = where she writes syllabi each semester; rules only; never draft one, never call a missing syllabus a blocker. The Dean = her GCC dean (she/her). Sommarverken = a portfolio section, no subtitle. Render, Cultivate, CopaMigo, Rough Cut are capitalized codenames.

## Working rules

- **One Claude session in the repo at a time.** If files you are about to touch changed in the last hour and you did not change them, stop and ask. Phone notes go to `~/Documents/Claude/`, not repo edits. Never run a retired build script (`drafts/<course>-build/`).
- **Never run git.** She commits and pushes in GitHub Desktop. One exception: the scheduled cloud “Job sweep” may commit and push `jobs/index.html` only. Never give her Terminal instructions; when files are saved, say so and stop.
- **To-do list** = Apple Notes, one note a day titled `Tasks · <Weekday> <D Month YYYY>`, cherry-picked from `TASKS.md`. Do not rebuild `command/todo.html` unless asked by name.
- **Repo:** `/Users/michelleblomberg/Documents/GitHub/singletrackmom.github.io`. Edit in place. Private, unlinked and noindex: `command/index.html`, `command/todo.html` (git-ignored), `jobs/index.html` (never wiped).
