# Site Map, every project and its assets

_Full asset inventory of the singletrackmom.github.io repo, organized by project. Built July 4, 2026 from the real file tree. Pair with `PORTFOLIO_INDEX.md` (the one-line status map) and `PORTFOLIO_REDO_PLAN.md` (the redo plan). Update this when assets are added or a project ships._

Legend: **Pages** = HTML on the site · **Screens** = images/screenshots · **Source** = editable docs (docx/pptx/pdf/md) behind a project · **Data** = csv/xlsx/json · **Private** = noindex, keep unlinked.

---

## Root

- **Pages:** `index.html` (home), `about.html`, `work.html`

## Public portfolio projects

### Render, AI career-launch dashboard, `render/`
- **Pages:** index.html, overview.html, prd.html, walkthrough.html, sample-dashboard.html, render-maya.html, render-riley.html, training-plan-agent.html, mesa-ai-summit-2026.html
- **Screens:** render_cover.png, render-01..06 (profile/jobs/resume/skills/network/launch), render-goals/interview/links.png, sample-01..10 (goals, search-links, jobs, resume, skills, pdlog, network-interview, pdplan, schedule, glance)
- **Source:** Render_PRD.docx, Render_PRD_v0.5.docx/.pdf, Render_PRD_v0.6.docx, mesa-ai-summit-2026.pdf/.pptx
- Note: PRD exists as HTML (prd.html) AND several docx/pdf versions. Pick one canonical PRD; the site should link the HTML, not the docx (per your no-downloadable-docs rule).

### CopaMigo, student services routing, `copamigo/`  (DUPLICATE: `copamigo2/`)
- **Pages:** index.html, overview.html, detail.html, prd.html, deployment.html, testing.html, questionnaire.html, student-resources.html, advisor-form/index.html
- **Screens:** copamigo_cover.png
- **Cleanup:** `copamigo/` and `copamigo2/` are identical. Pick the canonical one, delete or redirect the other. Also `advisor-form/index 2.html` is a stray duplicate in both.

### AIRC SSS study, `airc-sss/`
- **Pages:** index.html, overview.html, ux-study.html, map-the-landscape.html, service-crosswalk.html, persona-library.html, scenario-bank.html, run-sheet.html, methodology.html, fieldwork-plan.html, frustrations-survey.html, coverage-dashboard.html, pilot-findings.html, usage-persistence.html, recommendations-pilots.html, faculty-briefing.html (+ sss.css)
- **Source:** AIRC_Domain5_Student_Support_Success_Plan.docx, SSS_Domain_Meeting_Agenda_June18.docx, Student_Journey_Form_Blueprint.docx, The_Persistence_Imperative.pptx, WORKING-STATE.md, risepoint-sr-director-jd.md
- **Data / build:** Maricopa_Scenario_Bank.xlsx, Maricopa_Student_Journey_Study_Kit.xlsx, Create_Barrier_Log_Form.gs, build/build_scenario_bank.py, build/scenarios.json

### Cultivate, AI/EdTech PD hub, `cultivate/`
- **Pages:** index.html, overview.html, detail.html, prd.html, preview.html, completed.html, pd-plan.html, ux_toolkit.html, scrum.html, whitepaper.html, learning-agents-whitepaper.html, claude-lovable-workflow.html, discord-community.html, cv.html (master CV), ai-fellows/index.html, google-genai/index.html, mesa_conference/mesa-conference.html
- **Screens:** cultivate_cover.png, cultivate-01..05 (newsfeed/trainings/pdplan/toolkit/log), cultivate-preflight.png, cultivate-mesa-summit.png, mblomberg.jpg
- **Source:** Cultivate_PRD.docx, EdTech_PM_Day_in_the_Life.docx, edtech_research.docx, TheSimpleGuideToScrum-1Pager.pdf, mesa_conference/mesa-ai-summit-2026-draft.pdf/.pptx, mesa-speaker-notes.md

### Rough Cut newsletter, `roughcut/`
- **Pages:** index.html, overview.html, form.html, visit/index.html (+ _archive template)
- **Screens:** roughcut_cover.png, images/ (masthead-rough-cut.png, gcc-logo.png, design-studio-set.jpg, steamworks-hero.jpg, stephanie-phoenix.jpg, sticker set: camera.svg, clapperboard/goggles/money/sparkle/trophy.png)
- **Source / backend:** visit/apps-script.gs, visit/README.md

### Canvas courses, `canvas/`  (large; course delivery files)
- **Hubs:** index.html, avc100/index.html, avc183/index.html, avc248/index.html
- **AVC 248:** competencies.html, course-schedule.html, render/index.html, shared.css; 9 modules (module-01..09) each with assignment pages; pages/ (welcome, meet-your-instructor, adobe-software, canvas, discord, zoom, netiquette, qr-code); module-09 assets (THREE-PERSONAS.md, example career agents maya/nina/riley, industry-agent-asu-animation.md); resources/ (GCC-Resume-and-Cover-Letter-Guide.pdf, tailoring-with-ai.html); **slides/** week-01..12 (.pdf + .pptx pairs)
- **AVC 2xx (UX course, in progress):** avc2xx/competencies.html, avc2xx/responsive_project.html
- **Design history:** design-history/ (assignment, slideshow, overview, sorting-room-real-art.html + img/ ~18 art images)
- **Screens:** internships_cover.png, mural_cover.JPG; **Source:** stackable_certificates.pdf

### Teaching portfolio pieces
- **The Traveler** `traveler/overview.html` (+ traveler cover images live in fep/)
- **Murals** `murals/overview.html`
- **Internship** `internship/overview.html`
- **AVC 100** `avc100/overview.html` (+ markdown: All_Projects_and_Exercises, All_Video_Scripts, GettingHelp_Resources_and_Script, Schedule)
- **GCC Cares** `gcc-cares/` (index.html, overview.html; screens avc100_cover.png, cares_cover.png)

### Personal builds (portfolio evidence)
- **Wayfinder** `wayfinder/` (index, overview, prd, builder, builder-prd, frisco-packing; wayfinder_cover.png; its own CLAUDE.md). Canonical design template.
- **Devan travel** `devan/` (index, overview, devan_cover.png)
- **TrailLog** `traillog/` (index.html, PRD.md)
- **Tools** `tools/` (index.html, meeting-scheduler.html)

## Private / unlinked (noindex, keep out of the public index)
- `jobs/` Michelle's job dashboard · `focus/` Kevin · `flow/` Jillian · `soar/` Jasper · `summerwork/` Devan · `scrum/` PSPO study · `wgu/` interview hub · `frisco/` packing list

## Working docs, not on the site
- `notes/portfolio/` (this folder): PORTFOLIO_INDEX.md, SITE_MAP.md, PORTFOLIO_REDO_PLAN.md, mines-flagship-project.md, immersive-ai-assessment-plan.md
- `notes/render/`, `notes/drafts/`, `notes/professional-development/` (instructional-design-study.md), `notes/summer-production-schedule.md`
- `fep/` Faculty Evaluation Plan (docx/pdf/md + evaluation images fp-01..22, eval screenshots, survey csv). Not public.
- `sss_committee/` older SSS committee page. Confirm superseded by `airc-sss/`; retire or repoint.

## Cleanup flagged while mapping (July 4)
- **Duplicate project:** `copamigo/` vs `copamigo2/` (identical). Resolve to one.
- **Stray "index 2.html"** files in copamigo advisor-form (both copies).
- **Junk/temp in `fep/`:** `.fuse_hidden...`, `.~lock.FEP_2026_Blomberg.pdf#`, `lu47anlzi.tmp`, `ziv0bkPG`. Safe to delete.
- **`.DS_Store`** files scattered (airc-sss, canvas, cultivate, gcc-cares, wayfinder). Add to .gitignore and remove.
- **PRD sprawl:** Render has prd.html plus 4 docx/pdf versions; Cultivate/CopaMigo similar. Per your rules the site links HTML PRDs; keep the docx as source only, off the site.
