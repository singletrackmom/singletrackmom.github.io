# TASKS

## MONDAY 26 OCT · ASU first, before anything else

1. [ ] Finish the ASU I-9.
2. [ ] Call the department HR specialist at Mary Lou Fulton College (number is in the 9 Oct email “ASU/MLFC New Hire Information”; the I-9 email went to her Sunday; a second email about the JR128208 application is sitting in Gmail Drafts in that thread, send it first). Ask: your ASU ID number or when it comes; how to finish the I-9 without a card to reach the floor; and confirm the 16 Oct external application to JR128208 is fine, since your hire is not effective until 11 Jan 2027 (no Jobs Hub until then).
3. [ ] Do NOT withdraw the external application. ASU says a withdrawn application cannot be reactivated.

- Posting: [AI Learning Solutions Architect, JR128208](https://asu.wd1.myworkdayjobs.com/en-US/ASUStaffCareers/job/AI-Learning-Solutions-Architect_JR128208-2). Closes **Tue 27 Oct, 11:59 PM Arizona time.**
- ID card: [Sun Devil Card Services](https://cfo.asu.edu/cardservices). First card free for new employees; needs the ASU ID number first.

**START HERE (phone summary of the 24 to 25 Oct course chat):** `drafts/SESSION_2026-10-24_COURSES.md`, everything done, decided and still open on one page.

**PINNED, Sun 25 Oct (grading):** set up a calendar reminder at every hard close (export submissions, Claude first pass) plus a review block, and switch process work to full/half/zero with no comments now; Complete/Incomplete in Spring. Plan and ideas: `drafts/GRADING_STREAMLINE.md`. Needs the current deadline days confirmed first.

**PINNED, Sun 25 Oct (idea from the hike, don’t lose it):** add STEAMworks options (NFC/RFID objects, laser cutting, AR, VR, drone photography) to AVC150, 183, 190, 248, 283 and 2xx, so STEAMworks and the dean see the equipment money in the courses. Notes and suggestions: `drafts/STEAMWORKS_OPTIONS.md`. Options added to all six course drafts (25 Oct). AVC2xx: its Canvas file numbers modules one higher than the course page (drift from the restructure); rebuild from the course page before import. Still to confirm with STEAMworks: which AR tool, and whether the tags are phone-readable NFC. Note: another session moved the courses to a shared build (`tools/course-build/`), and AVC283 is now 123.5 hours (it was 120 last night); check before committing. When the FAA Part 107 certificate comes through, add it to the CV. STEAMworks grant is awarded and already on the CV; add it to the remaining resume lanes (details at the end of that doc).

**Restructured Sun 11 Oct 2026, at Michelle’s request: “i keep adding and adding and never doing.”**

The old file (3,314 lines, every note since July) is archived privately, unchanged, at `~/Documents/Claude/JobSearch/_tasks/TASKS-archive-2026-10-11.md`. Nothing was deleted. Personal items (money, appointments, family) live in `~/Documents/Claude/JobSearch/_tasks/PERSONAL.md`, never here, because this file is public.

## How this file works

1. **Three goals a week, no more.** They sit in the weekly table below.
2. **Every Monday,** Claude turns that week’s row into daily Apple Notes pages (`Tasks · <Weekday> <D Month YYYY>`). Only this week gets day-by-day plans.
3. **A new idea goes into the Backlog or into Parked, never into this week,** unless Michelle explicitly bumps something else out.
4. **Done means shipped:** sent, submitted, published or posted. Check it off the same day.
5. **Grading comes first every day.** Workout is 2.5 hours. No 10-hour days.

---

## REVIEW AND PUSH: one course build (done Sun 25 Oct, afternoon)

Every course page now comes from ONE build. Nothing is pushed; review in GitHub Desktop, then push.

- [x] New AI Primer (career question, read it like a critic, revised prompt, reflection, AI-use log) in all six AI courses. Technology Setup now comes before it.
- [x] “Where You Stand” and every AI-position discussion removed from every course.
- [x] Module 0 is identical, word for word, in all seven courses (AVC100 without the AI parts). The words live once in `canvas/_shared/module0.html`; only course-specific pieces (competencies, grading, course tools, course-only sections) sit inside each page.
- [x] One shell for every course page: one stylesheet (`canvas/course.css`), one script (`canvas/course.js`), same header and footer. No course page has its own style block any more. Looks the same as before; links are now underlined in AVC190 and AVC283 like the rest.
- [x] Checkers now cover the course pages; preflight runs `course-build/build.py --check` and fails if anyone hand-edits shared text. Preflight: safe to commit.
- [x] Three comments everywhere, introductions included (Michelle, 25 Oct).
- [ ] Review: per-course Module 0 hours stayed as they were (AVC100 3, AVC150 6, AVC183 9.5, AVC190 7.5, AVC248 7.5, AVC283 8, AVC2xx 10). Same Module 0 with very different hours is worth a look.
- [x] Leave alone (Michelle, 25 Oct; courses are for the future). Was: AVC183 and AVC248 also have separate module pages (`modules/`, `pages/welcome/`, `ai-in-this-course/`) that still carry their own older copy of Module 0. Recommendation: once the shared Canvas packager is approved, turn those pages into redirects to the course page, so every course is one page like the others.
- [x] One Canvas packager for every course: `tools/course-build/package.py`. Every graded item in all seven courses now carries the same hidden data (week, points, group, due day), and all seven package with zero problems; item counts and group points match each grading table. Test packages are in `drafts/package-test/final2-<course>/`. No real .imscc in `canvas/` has been overwritten yet.
- [x] Done 25 Oct: moved to Thursday 11 Mar. Was: when a Sunday deadline’s hard close lands on Monday 15 Mar (first day of spring break), the packager pushes the close to Mon 22 Mar. Affects AVC100 (Animation Step 3, Final Project), AVC183 (Milwaukee Step 3), AVC248 (Portfolio and Reel Plan, Industry News). Keep the week-long late window, or move those due dates?
- [x] Done 25 Oct: both moved to Sunday 14 Nov. Was: Thursday 11 Nov 2027 is Veterans Day. AVC190 (Search, Performance and Analytics Pass) and AVC283 (Final Critique of the Guidelines Book) are due that day; the packager moves them to Friday, the pages still say Thursday.
- [x] Done 25 Oct: Thursday of finals week in both terms. Was: finals due day. Spring 2027 packager uses Fri 14 May, AVC248 says Thu 13 May; Fall 2027 uses Fri 17 Dec (marked verify), AVC283 says Thu 16 Dec.
- [ ] AVC100 due days (Thursday or Sunday per item) were inferred from the course rhythm, since the page only says “Week N.” Confirm.
- [ ] Then: run `python3 tools/course-build/package.py --all` to replace the real Canvas files.
- [ ] The old one-off build scripts in `drafts/<course>-build/` are retired. Do not run them; they would bring back the old Primer and the AI-position post.

## THIS WEEKEND, Sat 24 and Sun 25 Oct · grading only

**Goal: every submitted assignment graded and in Canvas by Sunday night. Nothing else starts until it ships.** Claude checks in Saturday morning, Saturday afternoon, Sunday morning and Sunday evening.

1. [ ] Grade everything that’s been turned in, every class.
2. [ ] Scores into the Canvas gradebook, feedback in SpeedGrader.
3. [ ] Workout still happens (2.5 hours). No 10-hour days.

## NEXT WEEK, Mon 26 to Fri 30 Oct · home, time off

Before you leave: schedule this week’s two LinkedIn posts (see `drafts/LINKEDIN_CALENDAR.md`).

Going home to breathe. No conferences, no extra projects. Only what can’t move (check the Fri 30 Oct items below with Claude before the week starts).

## IN PROGRESS: six-course quality pass (started Sat 24 Oct, night)

Courses: AVC150, AVC183, AVC190, AVC248, AVC283, AVC2xx. Nothing committed yet; review, then push.

**Done**
- [x] Reconciled the two sessions: nothing clobbered. AVC183, 190, 248, 283 committed at 7:47pm (“classes again”).
- [x] AVC150: Project 1 hard close moved to Tuesday at noon (Labor Day), approved. Old film drafts moved to `drafts/avc150-before-storyteller/AVC150-film-history.md`.
- [x] AVC248: “genuinely” swapped for “really” on four student pages.
- [x] Eight synthetic student testers (personas P01, P04, P05, P06, P12, P15, P22, P34 from the journey study) walked all six courses.
- [x] OSCQR review and seat-time check for all six courses.
- Findings (private, not in this repo): `~/Documents/Claude/Personal/course-tests/` (P*.md, OSCQR_*.md, BLOOMS_AI_AUDIT.md).

**Running**
- [ ] Bloom’s audit: revised taxonomy (Anderson and Krathwohl) on every objective, plus an AI-exposure check on every assessment (Oregon State “Bloom’s Taxonomy Revisited” lens).
- [x] All six fixers finished. One fixer per course applied every finding. AVC2xx DONE: real h2 module headings and jump list, Start Here and Syllabus built, rubrics on all 34 graded items, Revision folded into Modules 13 and 14, 120 hours, Canvas file validated. AVC248 DONE: Module 0 and AI Primer, Welcome page fixed, Discord only, rubrics and tagged objectives on every page, under-16 LinkedIn path, about 119 hours, Spring 2027 Canvas file validated. AVC183 DONE: one source (Spring 2027 pages), real home page, Module 0 and AI Primer, every objective tagged, 119.8 hours, new Canvas file validated. AVC150 DONE: Bloom’s objectives tagged to competencies, graded AI Primer recording, policies and contact, Chromebook paths gone, about 122 hours, Canvas file rebuilt and validated. AVC190 DONE: 16 modules, 39 pages, 36 assignments each with a rubric, Canvas file validated, 121 hours. AVC283 DONE: 16 modules, Canvas file validated (37 pages, 28 graded items, all with rubrics), exactly 120 hours, Gemini image generation removed. Each course backed up first to `drafts/<course>-before-oscqr/`. AVC190 and AVC283 are being built into real student pages and Canvas files (they only existed as markdown). AVC183 gets one source of truth (three versions disagreed) and a real home page.

**Rules set tonight (apply to all six)**
- Revised Bloom’s for objective verbs; check every assessment for AI exposure.
- Every course gets the OSCQR review; adjust seat time to 120 hours (about 8 per module).
- No Chromebook path. Students without a computer request one through the OIT form in the syllabus. Every such line is marked `<!--OIT-LINK-->` for the URL.
- Students never see markdown. Instructor notes and answer keys never show in student view.
- Instructor contact is Canvas Inbox and Discord (never Slack). No invented email, no dead “#” links.
- AVC2xx: Revision module folded into its neighbors to hit seat time.

**Open issues for Sunday morning (one at a time, most important first; grading still comes first)**
1. [ ] Check the fixers’ results: which of the six finished, and anything they flagged. Each course’s backup is in `drafts/<course>-before-oscqr/` if something looks wrong.
2. [ ] OIT form: confirm GCC’s Student Technology Request (help.maricopa.edu/TDClient/44/GCC/Requests/ServiceOffering/24/Student-Technology-Request) is the form in the syllabus. The round 2 cleanup puts it in all six courses.
3. [ ] Discord invite: confirm the one real program invite to use in every course (fixers reuse the AVC248 invite if one exists; otherwise a placeholder is left).
4. [ ] AVC150 first offered Fall 2027 or Spring 2028? TASKS and the course disagree.
5. [ ] AVC2xx: okay to fold the Revision module into its neighbors (the alternative was cutting the Week 7 user test to two participants)?
6. [ ] AVC190: the merges shrink the Exercises group (25%) to about 30 points. Keep two exercises or lower the weight? (Fixer picks whichever keeps the house groups intact and notes it in AVC190.md.)
7. [ ] AVC248: LinkedIn requires age 16+. Approve the under-16 alternative (a portfolio About page with the same content).
8. [ ] Instructor contact on every course is Canvas Inbox (reply within one business day) plus Discord. Okay, or add office hours?
9. [ ] Leftover “genuinely”: two AVC248 slide decks (fixer tries to fix) and the working notes for AVC100, AVC183 and AVC2xx (not student-facing).
10. [ ] AI Primer standard (`canvas/AI_PRIMER_STANDARD.md`, shared by every course): the Bloom’s audit says the Primer is easy to hand to Gemini and objectives 1.1 and 1.4 (AI costs, the student’s own AI position) aren’t graded. Proposed: make the position statement a graded part and record one fact-check as a narrated screen recording. Approve before it changes in the standard.
11. [ ] AVC2xx allows disclosed AI placeholder assets in prototypes. Keep as an exception to “Gemini never designs,” or remove?
12. [ ] Discord invite on public pages: the fixers are reusing the real program invite (already public on the AVC248 login page). Keep it public, or put placeholders on the site and keep the real link only in the Canvas files?
13. [ ] AVC283: Fall 2027 (how it’s built) or spring only (what CLAUDE.md says)? And the site title: “Graphic Design and Digital Publishing II” or “Graphic Design 2”?
14. [ ] AVC283 items marked [instructor to create]: welcome video, office hours, client packets, templates, mockup files.
15. [ ] Preflight is blocked by broken links inside the gitignored `drafts/*-before-oscqr/` backups. Fix: make preflight skip gitignored folders, or move the backups to `~/Documents/Claude/Personal/course-backups/` after the fixes are approved.
16. [ ] Canvas .imscc files in the repo: publish-guard flags every one (AVC150, 183, 190, 248, 283) as a downloadable file. Keep them in the repo with an allow-list reason, or move them to the private Claude folder?
17. [ ] Instructor name, photo and office hours: the courses point to the welcome announcement instead of writing them into the pages. Okay?
18. [ ] Under-18 rule when a Gemini feature is blocked: the student messages the instructor, who sends an instructor-written brief or copy draft instead. Is that the rule for every course?
19. [ ] Fall 2027 dates assume Week 1 starts Mon 23 Aug 2027 (Labor Day, Veterans Day, Thanksgiving week built in). Check against the 2027 to 2028 MCCCD calendar when it’s out.
20. [ ] AVC190 to create: instructor videos and the Juniper Street Bikes demo site.
21. [ ] AVC150: D3 was removed and D4 to D8 renumbered as D3 to D7. Keep the renumbering?
22. [ ] AVC150 under-18 fallback: if Gemini Notebook is blocked, the instructor runs the student’s Teller from their sources and instructions. Acceptable?
23. [ ] AVC150 placeholders: McCloud e-reserve link, and [instructor name], [term] and [verify] terms in the consent documents. Also click through the GCC and Maricopa policy links once (the sites block automated checks).
24. [x] Build scripts and backups in `drafts/` are gitignored, so they stay private. Nothing to move.
25. [ ] AVC183 trims: Logo Step 3 down to four concepts, apparel/signage piece cut, Recipe Step 1 folded into Step 2. Keep?
26. [ ] AVC183 finals all at 30 points now (Behance went from 15 to 30). Keep?
27. [ ] AVC183 placeholders: eleven instructor videos, the Discord office-hours day and time, two [verify] notes on the Thinking with Type edition, one on the AIGA link.
28. [ ] `canvas/index.html` (the course hub) is stale: it lists only four courses, calls AVC183 “In Development… a blank slate,” and has a “Canvas link coming” dead end. Rework it to list all six courses with their real status and links?
29. [ ] AVC248: is `discord.gg/fyzAXNS4yF` the right Discord invite for Spring (now used in every course)?
30. [ ] AVC248: Final Portfolio Presentation due in finals week (Thu 13 May). Okay?
31. [ ] AVC248: some objectives under Competencies 5 and 6 use “Identify” to stay at that competency’s Remember level, which undersells the contract work. Keep, or note the stretch in `competencies.html`?
32. [ ] AVC248: old `AVC248_Fall2026.imscc` kept because `AVC183.md` points to it. Retire it and fix that reference?
33. [ ] AVC248 placeholders: instructor videos and slide walkthroughs, audio introduction, mid-semester survey link, and building the syllabus quiz in Canvas.
34. [ ] AVC2xx: Module 2 is only 4 hours because of the one-deadline Week 1 rule. Add content or leave it light?
35. [ ] AVC2xx starter kits: listed as optional on the instructor build list; student pages no longer promise them. Build or drop?
36. [ ] AVC2xx placeholders: 16 instructor videos, unconfirmed GCC support and district policy links, a [verify] letter-grade scale, and whether Gemini Canvas works with a screen reader.
37. [ ] AVC2xx still shows “AVC 2xx” as its number. Get the real course number once curriculum assigns it.
38. [ ] Review the diffs for all six courses (git diff canvas/), then commit and push. Nothing is committed yet.

**Next**
- [ ] Michelle: send the OIT computer request form URL.
- [x] Round 2 testers done (`~/Documents/Claude/Personal/course-tests/round2/`): every round 1 dead end fixed; no course above severity 3. Left: instructor notes visible on AVC183 and AVC248 module pages, placeholders showing to students (worst in AVC283), missing calendar dates, unlinked computer form, no basic-needs link.
- [x] Round 2 cleanup DONE on all six, every Canvas file rebuilt and validated: hide instructor notes and placeholders, real OIT link, GCC Cares link, dates, 14px minimum type, AVC283 AI-use log template and three client packets written, AVC248 mentor under-18 guidance.
- [x] Reviewed note added under Outcomes on all six course overviews (Bloom’s and AI-exposure lines were already there): “Before launch, the course was checked against the SUNY OSCQR online course quality rubric and walked through by eight synthetic student agents, built from the Student Journey Barriers Study personas, in two rounds of testing.” Check the wording.
- [ ] Michelle reviews the diffs; commit and push.
- [ ] Open question: TASKS says AVC150 is first offered Spring 2028, but the course is built for Fall 2027. Which is right?

## REGROUP AFTER GRADING (left off Sun 25 Oct, late morning)

**Push first.** Everything below is saved but not committed. Checks at stopping time: design-lint 0 critical, a11y-lint 0 critical, preflight “Safe to commit.” Commit everything, including new files: `program-design/degrees.html`, `avc100/avc100_cover.jpg`, `program-design/PROGRAM_NOTES.md`, `canvas/avc283/OLD_AVC182_INVENTORY.md` (if it finished).

**Done Sun 25 Oct (for reference)**
- Program Design: Course Method section (11 steps, incl. Open materials / Near Z Degree), Student Safety section removed, course grid removed, tabs Overview · Degrees.
- Degrees tab replaces the microcredentials card and PDF (PDF in `_to_delete`). Old microcredentials and credentials links redirect.
- Home cards: Programs “AI and XR” (short); AVC100 “Once the program’s lowest-success course, redesigned for retention, belonging and connection…”
- New line-drawing covers for AVC100 and the UX course.
- Breadcrumbs on 86 pages; one-word course tabs (Design · extras · Course) everywhere; Canvas footers removed from course pages.
- AVC150: Kurzweil book no longer required; her free video preview + NPR + “Projects Like This” instead.
- All holidays removed from course pages and schedules; “about” removed from module bars; “made up/fake/invented” → fictitious (clients) or fabricated (AI); dual enrollment removed.

**First job after grading (approved in chat, not started):** strip planning codes from every student-facing course page (S11, D4, P1, PW18 and similar) and use plain titles; change “Rubric (10):” to “Grading (10 points):”; remove objective numbers like “(7.2)” from rubric lines (objectives are already listed at the top of each item). Scan all seven courses, then rebuild the Canvas packages.

**Stopped mid-run Sun 25 Oct (spend limit hit). Resume these, in order:**
- [ ] Google sweep of all seven courses STOPPED PARTWAY: Zoom → Google Meet, office hours on Meet booked through your Google Calendar booking page (in every Module 0), Gemini skills (18+) vs Gems for agents (verify), Google tools only where they do real work. Some files may be half-done: check `_to_delete/google-sweep/` for what was touched, finish, then run lint and preflight before pushing.
- [ ] Portfolio Google pass (may also have stopped): About and Bio show your district leadership in Gemini for Education and “completed Google’s Generative AI Leader training” (training, not certified; exam not taken). Name Google tools in each project’s Technology section only where actually used (CopaMigo stays Claude). Backups in `_to_delete/google-portfolio/`.
- [ ] AVC248 restructure (you asked; plan shown, waiting on your OK): do one job search by hand in Weeks 1 to 2, build the Job Search and Career Counselor agents in Weeks 2 to 3, agent tune-up every module, Mock Hiring Panel mid-course, Mentor Finder later, export to a personal account in the last module. Show the new module order before rebuilding.
- [ ] Apps Script: Render’s Career Services Sheet connection is planned, not built. Tell Claude if you built it outside the repo.
- [ ] Before pushing anything: run design-lint, a11y-lint and preflight, since two passes stopped partway.

**Questions for you, most important first**
1. [ ] Degrees page: do animation students transfer through the AAFA (Associate in Arts, Fine Arts, Emphasis in Art, not animation-specific) into ASU’s Art (Animation) BFA? GCC’s AAFA page lists only Ceramics, Painting, Photography and Sculpture BFAs. Is there a pathway agreement to link? Also: is the DMA AAS → ASU Polytechnic Graphic Information Technology BAS a formal pathway or just eligibility?
2. [ ] AVC100 card says “lowest-success course.” Keep, or soften to “Redesigned for retention…”? Make sure the AVC100 page backs it up.
3. [ ] AVC183 official new title: “Graphic Design” or “Graphic Design and Digital Publishing I”? (Degrees page uses what the course page says.)
4. [ ] AVC183 *Thinking with Type*: found the GCC Library ebook (ProQuest Ebook Central docID 31362672, one reader at a time, chapters downloadable) in your Fall 2026 AVC183. Relabel “Textbook” to a free library reading with that link. Old AVC181 shells say “Please purchase” and link a Dropbox PDF of the 2nd edition; drop that link.
5. [ ] Check the AVC150 “Projects Like This” list (Dimensions in Testimony, NPR Dadbot, Laurie Anderson) and the Pinchas Gutter interactive (couldn’t confirm it opens without login).

**Next build: AVC283 from your real AVC182 course** (Claude skipped this the first time; fix it)
- [ ] Read `canvas/avc283/OLD_AVC182_INVENTORY.md` (pulled read-only from Canvas: AVC182 Spring 2026 + AVC283 sandbox; Lupton from AVC181).
- [ ] Weekly *Designing Brand Identity* (Wheeler, GCC Library ebook link you give students) chapter or case study + short reflection, as a reference, not cover to cover.
- [ ] Finding: the old AVC182 identity project is pick-your-own (about 6 weeks, Steps 1 to 6, manual with six applications). Espressoism is a past student’s sample manual, not a given brief, and no real clients were used (The Traveler was extra credit). Decide: write a new short given-brand warm-up, or keep pick-your-own and use Espressoism as the model.
- [ ] Wheeler, *Designing Brand Identity* 6th ed., ProQuest Ebook Central docID 31064160. Your old pattern: five chapter readings with short reflections in weeks 2 to 4 (Brand Basics, Section 3 case studies, Brand Ideals, Brand Elements, Brand Dynamics). Spread these across the term so there’s reading most weeks.
- [ ] Also bring back: the Social Issue or nonprofit campaign (about 6 weeks) if it fits AVC283.
- [ ] Hours: AVC283 is already about 123.5 hours (target 120). Claude shows the trade-off with real numbers before changing anything (fold the Figma warm-up into the given brand, shorten it, or trim generator weeks).

**Later**
- [ ] Rebuild every Canvas package (.imscc): they still have the old book, holiday text and dates.
- [ ] AVC248 career agent system rebuild (Mock Hiring Panel etc.), Career File in all courses, agent ladder in the AI Primer.

## AFTER THE BREAK, in this order

1. [ ] **The Traveler:** confirm the production team (names and roles) by a set date, then put the kickoff meeting on the calendar.
2. [ ] **Spring grading restructure:** process work becomes check, plus or minus (one process check per project, not dozens of small items); written critique on final work only. Canvas: Complete/Incomplete on process assignments, weighted assignment groups. Build it for Spring, don’t change grading mid-semester.
3. Keep moving the current classes forward through Thanksgiving.
4. [x] Portfolio pages built 24 Oct: AVC150 course design, Traveler AR edition tab, GCC Cares update with tower production photos. Still to add: Monday’s tower assembly and event photos. Plan: best assembled-towers shot goes full size at the top of the Towers section, or becomes the GCC Cares Overview hero with the empty-room photo moved into the Open House story as the “before.” Then change “stacked” to “assembled” in the Open House outcome.
5. [ ] **GCC Cares report for the dean and chair** (after the open house): a Google Doc, NOT online, covering the same story as the site (phases, open house, towers, team, photos, next steps). Rewrite it in fresh internal wording, never copy site text, and never link or mention the website.

Parked until January: AVC190 Introduction to Web Design and UX sandbox, built in the GCC red style from the new competencies (`canvas/avc190/AVC190.md`); sandboxes requested from GCC 23 Oct. Check the articulation concern first.

Parked until January: AVC150, built out for whoever teaches it (notes in `canvas/avc150/AVC150.md`); goes in the portfolio once the design package is finished. Check the district faculty agreement on who owns course materials first.

---

## (OLD) TODAY, Thu 15 Oct · frog first, in this order

1. [ ] **Grades into the Canvas gradebook.** Export the gradebook CSV (Grades › Export), Claude fills the scores into a copy, Michelle reviews every row in the file, then Grades › Import once. Canvas shows a preview of changed scores before it saves. Feedback comments still go in SpeedGrader (the CSV doesn’t carry comments).
2. [ ] **Send applications from `JobSearch/_READY_TO_SEND`, ASU first (closes 27 Oct), CVS (closes 17 Oct).** Tell Claude “sent <company>” after each.
3. [ ] **Push the AVC248 revisions** (`canvas/avc248/AVC248.md`, the 14 Oct mid-semester rebuild) in GitHub Desktop. `course-schedule.html` still shows the August plan.

Nothing else starts until these three ship.

## This week, Sun 11 to Sat 17 Oct

**Goals:** (1) BoodleBox (SENT 11 Oct) and CVS applications sent · (2) AI inventory launched at the CoP · (3) League proposal outlined

| Day | Do |
| --- | --- |
| **Sun 11** | BoodleBox: confirm the deadline story (under-18 study, see below), finish the open items, send. Log it in the tracker. |
| **Mon 12** | Grading first. ~~Send transcripts to ASU HR~~ DONE (transcript ordered, background check done). CopaMigo: ask an executive sponsor, check in with Eric, request a meeting with Genesis, Meghan and the college CIO. Send the CoP agenda. Put up the Traveler production-team flyers. Schedule the paid STEAMworks tools training. |
| **Tue 13** | CVS Health, Manager, AI User Enablement: rebuild from the status table, read it, submit. |
| **Wed 14** | **FIRST: AVC183 Module 4 (Milwaukee) into Canvas.** Paste the 4 steps from **[MODULE4_PASTE_INTO_CANVAS.md](canvas/avc183/MODULE4_PASTE_INTO_CANVAS.md)** (HTML plus a rubric under each). Full path: Documents › GitHub › singletrackmom.github.io › canvas › avc183 › MODULE4_PASTE_INTO_CANVAS.md. Dates: Mon 19, Thu 22, Mon 26, Thu 29 Oct. Then ask Claude to update `AVC183.md` and `course-schedule.html` to match. Module 5’s 50 sketches stay on Thu 29 (her call). **CoP Meeting Three: [Links page and agenda, Google Doc](https://docs.google.com/document/d/1rONvJMx0hnx3Ipm0DB40NMh6fZHDzvD7YHjI1aYz3Gk/edit).** Copy both pages into the top of the running agenda doc (newest first). Fill in the [paste link] spots: group chat, district AI website, office hours, CTLE/library survey. Pull the League call requirements. |
| **Thu 15** | League proposal outline. Confirm the CGCC conference date (the calendar entry is unverified). |
| **Fri 16** | **FIRST THING: EDUCAUSE conference reimbursement.** Then **send applications from `JobSearch/_READY_TO_SEND`, ASU first (closes 27 Oct).** CVS, if not already sent (closes 17 Oct). Two-line note to the Element451 contact. 15-minute week review. |

### BoodleBox: SENT Sun 11 Oct 2026

- [x] Application emailed to careers@boodle.ai with the resume; logged in the tracker. Final text in `~/Documents/Claude/JobSearch/BoodleBox_Application/application_email_SENT_2026-10-11.md`.
- [ ] Short personal note to Jess Awtrey, if not already sent.
- [x] Finish the Wiley customer success course (on the resume as 2026). DONE 13 Oct.
- [ ] Interview prep lives in `boodlebox/index.html` (Who’s in the room, Customer success, Questions).

---

## Weekly goals through December

| Week of | Goal 1 | Goal 2 | Goal 3 |
| --- | --- | --- | --- |
| **12 Oct** | BoodleBox and CVS sent | AI inventory launched at the CoP (Wed 14) | League proposal outlined |
| **19 Oct** (ASU summit, volunteering Tue 20 to Thu 22) | League proposal full draft, through the review panel | 1 application (State of Colorado OIT Sr Technical PM or CU Anschutz 41327, both close 21 Oct) | Network at the summit |
| **26 Oct** | **League proposal submitted, Fri 30 Oct** · **Dial Your Course test version to the CGCC ID Fellows contact by Fri 30 Oct, PROMISED** (build days Fri 23 and Mon 26, scope in `~/Documents/Claude/JobSearch/DialYourCourse/BUILD_NOTES.md`) | UCAR / NCAR ML Educational Trainer (closes 30 Oct) | Personal block (see PERSONAL.md) |
| **2 Nov** | CopaMigo: sponsor confirmed, approved hosting and AI path asked of the district | 2 applications (Element451 blind resume counts) | Rough Cut: issue refreshed, email version built, Gmail drafts made |
| **9 Nov** | Journey study rescoped around Salesforce, restarted | 2 applications (D2L blind resume counts) | Rough Cut sent in three batches before Thanksgiving week |
| **16 Nov** | Dial Your Course: fold in the CGCC tester’s feedback (v2 becomes Pilot once a tester has run a real course) | 2 applications | CopaMigo office training plan drafted (ADKAR, using the Prosci modules, 3 hours max) |
| **23 Nov** (Thanksgiving Thu 26) | 1 application | Rest | |
| **30 Nov and 7 Dec** | Finals grading | CopaMigo ready for the January pilot | Review what shipped, plan spring |

**The December outcomes these add up to** (set 10 Oct): AI inventory running at the CoP · CopaMigo in a sponsored pilot with verified answers · Dial Your Course proposal submitted and another faculty member using it · a new job by 1 May 2027, two applications a week.

---

## Deadlines

| Date | What |
| --- | --- |
| 12 Oct | WGU Program Development Owner · Google AI Solution Builder (“until at least 12 Oct”), both not planned |
| 13 Oct | Auraria Technical Program Manager, not planned |
| ~15 Oct | Children’s Hospital Colorado Foundation, Business Solutions and Automation (wants Power Platform), not planned |
| 16 Oct | WGU Senior Educational Program Designer, not planned |
| **17 Oct** | **CVS Health, Manager, AI User Enablement** |
| 18 Oct | CSU Director of Learning Design (off the list, Fort Collins on site) |
| **27 Oct** | **ASU EdPlus AI Learning Solutions Architect (built, in `_READY_TO_SEND`) · University of Michigan AI Enablement Lead (not built)** |
| 20 to 22 Oct | ASU Agentic AI and the Student Experience summit, volunteering |
| 21 Oct | State of Colorado OIT Sr Technical PM · CU Anschutz Business Applications Analyst 41327 |
| 23 and 26 Oct | **Dial Your Course build days** (Fri 23: suite menu and the one-check flow; Mon 26: Seat-Time-o-Meter plus AI-Use Level and AI-Completable Check) |
| **30 Oct** | **League Innovations 2027 proposal (Dial Your Course)** · **Dial Your Course test version to the CGCC ID Fellows contact, promised** · UCAR / NCAR ML Educational Trainer |
| Late Oct or early Nov | EDUCAUSE Taking Charge of Change microcredential arrives; then add it to the CV |
| 2 Nov | EDUCAUSE 2027 CFP check |
| 14 to 16 Mar 2027 | League Innovations conference, Chandler (confirm dates) |
| 26 Apr 2027 | ADA Title II / WCAG 2.1 AA deadline for any piloted tool |
| 1 May 2027 | Target: new job |

---

## Waiting on Michelle

Answer one at a time, most important first.

1. BoodleBox story: is the “measuring the wrong thing” beat right?
2. Nelnet UX Researcher requires a federal security clearance. Do you have one, or is it a no?
3. Cengage “Program Manager, AI Operations”: any contract experience? If not, drop it.
4. AI-use badge for Dial Your Course: three lights or five levels?
5. Which day of the week is the AI tools day (about 10 hours)?
6. Branding workload: the Basic Needs Hub is eating your class time. What gets cut?
7. Who is the CopaMigo executive sponsor?
8. Which Dial Your Course build is the tool, `course-dialer/index.html` or `v2.html`? (Blocks the demo video.)
9. Simulations license: CC BY or CC BY-NC-SA?
10. The name of the resume-matching tool someone mentioned at EDUCAUSE (for the Render decision, parked).

---

## Backlog, by project

Not this week. Pulled into a week only by bumping something else out.

### Job search
**Parked 13 Oct evening, teaching first. Pick up here.** Six applications are ready to send in **`JobSearch/_READY_TO_SEND`** (one folder per job: cover letter PDF, resume PDF, APPLY HERE note with the link). Nothing sent yet. **New morning builds are PAUSED until these six are sent** (scheduled task “Morning application drafts” is turned off; turn it back on after). When one is sent, tell Claude “sent <company>”: log it in the tracker, move its folder to `_SENT`.
- [x] ASU EdPlus AI Learning Solutions Architect (JR128208): sent 16 Oct (external site, as a pre-hire).
- [x] Univ. of Michigan AI Enablement Lead: dropped 16 Oct.
- [ ] UCAR ML Educational Trainer: built. Closes **31 Oct**. Hybrid Boulder, mostly training delivery.
- [ ] Nelnet UX Researcher (R22931): rebuilt 13 Oct to the new rules.
- [ ] Trimble CX Researcher & Information Designer: built. In office, Westminster.
- [ ] Wikimedia Lead Learning Experience Designer: built. Remote.
- [ ] CVS Manager, AI User Enablement: built in another chat 13 Oct; add the Wiley certificate if wanted.
- [ ] Faculty Developer, Office of Teaching and Learning: send Claude the link to rate.
- [ ] Sonal pitch, Google Doc "Proposed Role · AI Enablement Lead (draft)": review before sending.
- [ ] Push the `jobs/` folder in GitHub Desktop.
- [ ] New LinkedIn headline (13 Oct): match the website headline and the resume summary lead to it so it is one story everywhere. After grading.
- [ ] CV cleanup: the 13 corrections from the 10 Oct chat into `cultivate/cv.html`, then the new resume template (Mines and CU format).
- [ ] Blind resume to the Element451 contact (after the CV and template), then D2L (confirm where D2L hires).
- [ ] Element451 Customer Success Engineer role: raise it with the contact.
- [ ] HigherEdJobs “Executive Director for AI Strategy & Enablement” (job code 179329096): open it by hand.
- [ ] Alchemy Director of Instructional Design, Guild Manager of Enablement: no deadline, decide.
- [ ] Wikimedia, UMGC, Code for America results: show her before adding to `jobs/index.html`.
- [ ] `jobs/JOB_AGENT_RULES.md`: add the Workday and governmentjobs.com board list from the 10 Oct run. Next run reads every open role at Google and Instructure.
- [ ] Coursera: ~~Customer Success: Reducing Churn & Growing Revenue (Wiley)~~ DONE 13 Oct. Still to do: the Gainsight end-user intro (1 hour).
- [ ] LinkedIn post: a digital media student hired at Workday (studio designer, led The Traveler student team, sponsor internship). NOT posted yet. Wait until she starts the job, and ask her OK to name her.
- [ ] **LinkedIn: 2 to 3 posts a week, from the calendar in `drafts/LINKEDIN_CALENDAR.md`** (private, never publishes). Claude drafts that week’s posts every Monday; schedule them in LinkedIn.

### Dial Your Course and the League proposal
- [ ] League proposal, due 30 Oct.
- [ ] Bugs before it goes public: due dates are never written; report and changes not connected; download disappears when Step 4 is hidden; file picker wants .imscc.zip instead of .imscc.
- [ ] Live tool tab shows an old version.
- [ ] Run the two Canvas outcomes-export tests (`canvas/reference/CANVAS_OUTCOMES_EXPORT_BUG.md`, 5 minutes, needs her Canvas login).
- [ ] AI-use badge: settle three or five levels, then add to `course-dialer/prd.html`.
- [ ] Get one other faculty member using it.
- [ ] Read the Maricopa intellectual property policy (15 minutes) before offering Dial Your Course to any company. Built on her own time and machine; it is in use in her program, so confirm the policy agrees.

### CopaMigo
- [ ] **The Anthropic API key in the CopaMigo page must move behind a proxy before any student outside the pilot uses it.** Confirm whether the July rotation happened.
- [ ] Executive sponsor; approved AI hosting path; run it through the ARC tri-chair’s pilot system.
- [ ] Staff knowledge builder saves only in the browser: build a return path for answers.
- [ ] Launch in the Canvas Student Resources button; find who owns that button.
- [ ] Training plan for collecting and verifying answers from each student services office.
- [ ] `copamigo/overview.html` still says sunsetting (check it was fixed in the 10 Oct cleanup).
- [ ] Close the “where does the pilot run” question in the requirements page.

### AI intake, inventory and ARC Domain 5
- [ ] Rebuild the intake on the work Google account (about 15 minutes left: paste `tools/aip-intake-v2.gs`, run setup, deploy, update the endpoint, test, retire the personal Sheet). Then fix the PRD.
- [ ] Delete the three example rows in the Sheet. Deploy the new email-notification version. Add the Sheet screenshot to the overview (no dates, Submitted column hidden).
- [ ] Pick one set of scoring criteria and make the other pages match.
- [ ] Model fixes from the OIT AI director’s review (gates, dispositions, value measure and baseline at intake).
- [ ] Buy or build: ask OIT which service-management platform the district owns.
- [ ] Domain 5 stakeholder letter: was it ever sent?

### Basic Needs Hub open house, Mon 26 to Thu 29 Oct 2026
Status page (public, no dates): `campus-cares/open-house.html`. Update its Status table as pieces move. Facts and copy: GCC_Cares_Source_of_Truth.docx.
- [x] Source of truth (facts, brochure copy, tower copy)
- [x] Brochure copy approved by GCC Cares
- [ ] Brochure layout (InDesign) · design lead
- [ ] Brochure printed
- [ ] Tower layouts, 4 towers × 8 panels (InDesign + Illustrator)
- [ ] Email Phoenix Forge about large-format paper, reservation and file setup
- [ ] Tower prints done
- [ ] Towers fabricated with the 3D fine art instructor and STEAMworks
- [ ] Wayfinding signs designed and printed
- [ ] Everything installed before Mon 26 Oct

### AI Design Studio grant (SSS Goal 5)
- [ ] Keep on the SSS goals: proof-of-concept year, then NSF ATE Track 1 on 7 Oct 2027. Plan: `~/Documents/Claude/JobSearch/_Grants/AI_Studio_NSF_ATE_Plan.md`.
- [ ] Meet the GCC grants office. Line up 1 to 2 employer partners. Pick first free test projects with the ARC tri-chair.

### Journey study
- [ ] Rescope around Salesforce, then restart. Salesforce notes and the task-by-task rescope: `~/Documents/Claude/ARC-SSS/Salesforce_Student_Journey_Notes.md` (“the Salesforce study”).
- [ ] Named contacts for the other nine colleges; verify the crosswalk.
- [ ] IRB determination and consent before any human testing.
- [ ] Settle the numbers (52 agents vs 50 personas, raters) before anything public.

### Gemini under-18 study
- [ ] Watch for committee changes. Re-read Google’s access-by-age page before the report goes anywhere new.

### Render
- [ ] Resume-alignment assignment for students (prompt plus one page), after the CV cleanup.
- [ ] Raw JavaScript showing in the Launch Plan panel.

### Portfolio site
- [ ] About 30 fact questions in `~/Documents/Claude/JobSearch/_site_cleanup_2026-10-10/`, one at a time.
- [ ] `tools/PRD_AUDIT.md`: about 100 contradictions, one at a time.
- [ ] Old pages with wrong claims: delete `prep/index.html`; fix or delete `wgu/cheatsheet.html` and `wgu/mock-interview.html` (migration claim); `capabilities/index.html` overstates three things.
- [ ] Real 1200x630 PNG social image.
- [ ] Accessibility backlog in `tools/ACCESSIBILITY.md`.

### Rough Cut (first issue, November 2026)
Sent from Michelle’s personal Gmail so first-round bounces and rejections go to her; every “contact us” link and button points to dmarts@gccaz.edu so real responses reach the program. Moved up from January so the news is current.
- [ ] **Week of 2 Nov:** refresh the issue: Fall 2026 date; name Glendale Community College everywhere (remove the leftover “a community college”); real preview line; STEAMworks is open (present tense, what is in it now); the student hired at Workday (via the studio and a sponsor internship), if she agrees to be named.
- [ ] **Week of 2 Nov:** email version: a short personal note, one image, a link to the newsletter on the web, “Email us” to dmarts@gccaz.edu. Test-send to herself. Claude creates one Gmail draft per contact from the private contact list.
- [ ] **Week of 9 Nov:** send in three batches (high, medium, then low priority schools), fixing bounced addresses between batches. Done before Thanksgiving week.
- [ ] **Early December:** count replies and visits; decide on a spring issue.

### Teaching
- [ ] **Instructor AI statement for Spring 2027:** add “Instructor Use of AI” to the syllabus and the short version to resume and cover letter pages. Decide on the opt-out line first. Drafts: `drafts/INSTRUCTOR_AI_STATEMENT.md`.
- [ ] **Syllabus quiz rebuild (Module 0, every course):** write a stronger quiz on the grading format: noon deadlines, each class’s due days, the 24-hour grace window with 10% off, the hard close. Not urgent.
- [ ] **Spring 2027 syllabi, paste in what left Module 0:** everything cut from Module 0 (course rules, the course intro paragraphs, and the reference sections like Consent and Privacy, Recordings, Research Ethics, the AI-Use Log Template) is in `drafts/SYLLABUS_REVIEW.md`, under each course in the Appendix. Move it into each course’s syllabus before the term. Course intro paragraphs are also in `drafts/MODULE0_REMOVED_SLOTS.md`.
- [ ] **Curriculum paperwork: add AVC150 Multimedia Storytelling and AVC190 (web design; confirm the exact title in the course bank) to the Digital Media Arts and Animation programs,** as the option in place of the journalism course. First offered Spring 2028. The program-change form and deadlines are in the CCTA Curriculum Handbook on the Maricopa Employee Portal (login required; the public search at curriculum.maricopa.edu points there). Ask the GCC curriculum committee chair which deadline gets it into the catalog for Spring 2028. Notes: `canvas/avc150/AVC150.md`.
- [ ] Export the “Grids are your Friends” Prezi before Prezi shuts down.
- [ ] AVC 183 week 11: pick a brand manual (NASA 1976, USWDS, Mailchimp).
- [ ] AVC 183 rubric fixes (name the six rubrics, 3 or 4 classmates, one submission format).
- [ ] AVC 248: check the makerspace-track claims about the Dean; verify or remove.
- [ ] Internships: reply to Marc with host-company requirements; email the student without an internship.

### Community of practice
- [ ] Wed 14 Oct meeting, then write up the minutes.

### Branding and design
- [ ] Traveler production-team flyers (Mon 12 Oct).
- [ ] STEAMworks tools training, scheduled.

### The Traveler AR (scanning 40 contest pieces, about 2 weeks in November)
Guide, every step plus drawings: [/arscan](https://michelleblomberg.com/arscan/) (site page, sent to a faculty reviewer) · working copy: [Claude doc](https://claude.ai/code/artifact/ce6cafe3-71af-4442-a02e-29e9568eeece)
- [ ] Ask STEAMworks and the DMA photo studio to borrow a light tent, softboxes, LED lights or a motorized turntable; build or buy only what’s missing.
- [ ] Week 1 (Oct 19 to 25): Lessons 1 to 3, scan a pot, view in AR, make a 360° spin.
- [ ] Week 2 (Oct 26 to Nov 1): Lessons 4 to 6, printed page trigger, QR backup, hard pieces.
- [ ] Week 3 (Nov 2 to 8): permission form, tracking sheet, folders, timed practice day.
- [ ] Confirm when page layouts lock and when The Traveler goes to print.

---

### Email (added Mon 12 Oct, not this week)

- [ ] Personal Gmail cleanup, about 10 minutes in Gmail on the web (Claude can drive it in Chrome, confirming each batch): delete all of Promotions; delete Updates older than 2 months while protecting job terms (application, interview, offer, HireRight, Workday, ASU, NAU, transcript); mark everything left as read.
- [ ] Unsubscribe from the repeat senders through Gmail’s Manage subscriptions page (course marketers, news lists, retail, the old sports-recruiting site). Keep the ones still read.
- [ ] Starred mail, done by hand because the Gmail connection is read-only: 22 junk to Trash, 5 records to a new Keep label. Three personal follow-ups are in PERSONAL.md.
- [ ] Work email: confirm whether GCC mail is Outlook or Google, and ask whether the district license includes Microsoft 365 Copilot. Then set up a Flagged-mail review every Monday.

### Productivity setup (added Thu 15 Oct)

Running now: daily email triage (scheduled task, weekdays 6:56am, personal Gmail only, labels and drafts, never sends) · weekday 9am “grades” reminder on the phone.

- [ ] Work email (GCC Outlook): finish connecting the Microsoft 365 connector so triage can read it. It’s search and read only, so no labels or drafts in Outlook.
- [ ] Focusmate body doubling (50-minute sessions) for grading and applications.
- [ ] WIP limit: three open items max, nothing new until one ships.
- [ ] Friday “did 2 applications go out?” nudge.
- [ ] Sunday weekly goal setter: three goals from this file into Apple Notes.
- [ ] Five-minute end-of-day shutdown review: what shipped, not what got touched.
- [ ] Optimize for Claude tokens (notes: `notes/TOKEN_SAVING.md`). Split CLAUDE.md and TASKS.md so a session only reads what it needs (root rules short, course rules in `canvas/CLAUDE.md`, project backlogs in their folders), and start one session per topic.
- [ ] Before AVC150 runs: break it into its own repo (a colleague’s advice) so collaborators don’t see the whole site repo. Create an empty repo, give Claude the URL, and Claude populates it and leaves a redirect from /canvas/avc150/. Do it after Version 6 is merged. Steps are in `notes/TOKEN_SAVING.md`.

## Parked until January

Deliberately not happening this semester. Moving something out of here means bumping a weekly goal.

GAIL exam · ITIL · Figma files (CopaMigo, Traveler) · walkthrough videos · Render “is it the right tool” analysis · whitepaper · email triage assistant · Text Blaze snippets · Fathom setup · UX course build · Render hiring panel · Dial Your Course maker mode and v2 extras · AVC 150 AI storytelling course build (notes: `canvas/avc150/AVC150.md`) · site nav, footer and lint cleanup · LinkedIn twice a week · personal training certs (revisit Dec 2026 or May 2027) · fitness-industry job lane.

### Idea parking lot

**Brand plus design generator (maybe what AVC283 becomes).** Students build a brand the usual way (logo, colors, type, assets), then build a design generator that applies it: an AI tool, a Figma setup, or a small site built with Figma, with the brand rules written into it as the prompt or system. The generator cranks out a batch of posters or social posts. Students then critique the output: did it follow the rules, and would it be usable at a job? The idea behind it: computers don’t make the brand, but they can apply it; the designer makes the brand, the rules and the templates. Michelle has seen designers posting generator experiments on LinkedIn and thinks this is the future of design. Questions to answer later: which tool (Gemini, Figma with AI or plugins, a vibe-coded web generator), how students write rules a generator can follow, and how the critique rubric judges “usable at a job.” Ties to GCC Cares (brand rules and Canva templates for non-designers).

---

## Where things live

| Thing | Path |
| --- | --- |
| The old task file, unchanged | `~/Documents/Claude/JobSearch/_tasks/TASKS-archive-2026-10-11.md` |
| Personal to-dos | `~/Documents/Claude/JobSearch/_tasks/PERSONAL.md` |
| Project status labels (one per project) | `CLAUDE.md`, the 10 Oct status table |
| Job tracker and every application | `~/Documents/Claude/JobSearch/` |
| Michelle’s job board | `jobs/index.html` |
| BoodleBox application | `boodlebox/` and `~/Documents/Claude/JobSearch/BoodleBox_Application/` |
| Evidence bank and interview stories | `~/Documents/Claude/JobSearch/CAREER_AND_INTERVIEW_PREP.md` |
| LinkedIn drafts | `~/Documents/Claude/JobSearch/linkedin_post_drafts_2026-10-10.md` |
| Site cleanup log and fact questions | `~/Documents/Claude/JobSearch/_site_cleanup_2026-10-10/` |
| AI Design Studio and the NSF ATE grant (“the NSF grant,” “the AI Studio grant”) | `~/Documents/Claude/JobSearch/_Grants/AI_Studio_NSF_ATE_Plan.md` (private). Next deadline 7 Oct 2027. Ties to SSS Goal 5, student project teams. |
| Student journey study, Salesforce rescope (“the Salesforce study”) | `~/Documents/Claude/ARC-SSS/Salesforce_Student_Journey_Notes.md` (private notes, outside the repo). Run sheet: `airc-sss/run-sheet.html`. Public pages: `studies/journey/` |
| CoP | `community-of-practice/` |
| DMA jobs Discord agent | `discord/DMA_JOBS_AGENT.md` |
| Family job agents | `agents/FAMILY_AGENTS.md` |
| Portfolio v3 (generated, never hand-edit `v3/`) | `tools/build-v3.py`, `portfolio/PORTFOLIO.md` |
| Course pages: one build for every course (shell, styles, script, Module 0) | `tools/course-build/build.py`; Module 0 words in `canvas/_shared/module0.html`; styles `canvas/course.css`; script `canvas/course.js` |
| Quality gate, run before calling anything done | `tools/preflight.py` |
| Accessibility backlog | `tools/ACCESSIBILITY.md` |
