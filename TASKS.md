# Tasks, Summer 2026

## 🔴 #1 PRIORITY, RESUME HERE TOMORROW: Student Journey study, master-doc sync + Phase 1 launch

**MEMORY NOTE TO THE ASSISTANT: you will not remember today&rsquo;s (26 Jul) conversation. THIS BLOCK is your memory. Read it fully before touching this project.**

**Michelle&rsquo;s goal:** run and finish **Phase 1** so she can say &ldquo;Phase 1 is done&rdquo; in her **Jeffco interview on Friday**, an easy win that shows a finished piece, not another half-done project. Phase 1 touches nothing (public web only) and the tri-chairs already approved it, so it can run now.

**Today only the WEBSITE (`airc-sss/index.html`) changed; the master Google Doc was intentionally NOT changed.** The site is now AHEAD of the doc. Going forward the **Google Doc is the source of truth**, and we roll the site&rsquo;s new content into it.

**TOMORROW step 1, before launching: give Michelle a clear BEFORE/AFTER changelog of every change going into the master doc, so she understands it before she replaces the content.** She will re-upload the current master (`Student_Journey_Gap_Analysis.docx`, ~138 pages, appendices A to I). Do NOT blind-regenerate it, edit surgically and preserve all content. Deliver the rollup ONE ITEM AT A TIME (she asked; it is a lot).

**The rollup items (roll SITE content into the DOC). Newest text is on the SITE tabs noted; write items 7 to 10 fresh:**
1. Three-phase test plan (P1 external, no login, no enrollment; P2 enrolled by hand, still external site; P3 login + student intranet + Salesforce). Replaces &ldquo;The two waves.&rdquo; Each phase states what it touches and what approval it needs. On site Testing tab.
2. Between-phase review/audit (after P1, check synthetic-vs-human agreement, tune personas/tasks/agent scaffold/rubric before P2; same before P3). On site Testing tab.
3. &ldquo;The evidence this method rests on,&rdquo; 6 cited sources (UXAgent, Looma.ai/ACM, GPT-4o comparison, ACM complement study, simulating-students review, Nielsen Norman Group + MeasuringU). On site Testing tab.
4. Reach times severity ranking + per-gap record (barrier, reach, severity, rank, recommended fix, fix type/cost). On site Prioritize tab.
5. Budget fix ladder (1 workflow fix free, 2 share an existing fix free, 3 build in house low cost, 4 configure Salesforce already-bought, 5 buy new last resort). On site Prioritize tab.
6. Transparency safeguard (notify dept director before touching them; label every test form/email as a test). Already in repo `_paper-source.html` Guardrails and site Technology. Confirm in the uploaded doc.
7. Data storage/access, ANSWERED: the study lives on the **district GitHub account Michelle runs, ARC has access**. Write into the doc&rsquo;s data-protection section. WRITE FRESH.
8. Consolidated **&ldquo;Ethics and responsible use&rdquo;** section + FERPA line. DONE on the site (new **Ethics tab**, 2nd tab, ~8 sections) and in the repo paper `_paper-source.html` (new &ldquo;Ethics and responsible use&rdquo; H2 before &ldquo;What is needed to proceed&rdquo;). PENDING: add the same section to the master Google Doc.
9. **IRB + consent, OPEN ITEMS** (Michelle: &ldquo;we need to figure out irb and consent&rdquo;). Now written responsibly as a &ldquo;Research permission and human-subjects care&rdquo; item in the Ethics section (site + repo paper): the study will confirm IRB-review-vs-exempt determination BEFORE any human testing (the ~10 validation testers + 80 in-person walk-ins), and participants give informed consent. STILL A REAL OPEN ITEM Michelle must actually resolve with the college/district; the text just states the intent to do it correctly.
10. Close-the-loop re-test (after a pilot ships, re-run the same scenario to confirm the gap closed). WRITE FRESH.

**Site changes made today (so you know what is already done on `airc-sss/index.html`):** Overview on the standard spine (Goal/Audience/Process/Technology/Outcomes/Status); Technology is now 8 explicit bullets (what the AI is, what it touches + no real data, where the model runs + Domain 1 governance, kept-honest discipline, structured JSON output, the Barrier Log form, humans hold judgment, how gaps get decided); a dedicated **Ethics tab** (2nd tab, consolidating the responsible-use points, this is the website match for doc rollup item 8; an earlier under-hero &ldquo;Responsible by design&rdquo; callout was REMOVED because nothing goes between the hero and Goal); corrected the &ldquo;public pages only&rdquo; overclaim everywhere (the account DOES log into the SIS and student intranet, but only as ONE sanctioned OIT test account with no real data); the &ldquo;Decide&rdquo; tab is renamed **&ldquo;Prioritize&rdquo;**; NO vendor names anywhere (no Claude/Cowork/Sonnet, not official school); Domain 1 (Strategy, Security & Governance) named as the security domain Michelle coordinates with; she leads Domain 5 (Student Support & Success).

**Phase gating:** Phase 1 = touches nothing, tri-chairs approved, RUN NOW. Phase 2 = first system touch (enroll the test account), needs Domain 1 sign-off. Phase 3 = deepest access, after Salesforce is live + Domain 1.

**To actually say &ldquo;Phase 1 is done&rdquo; Friday:** Phase 1 = run the synthetic persona agents on the public, no-login tasks (Stage 0 Find Maricopa + Stage A decide/apply + any public findability) across personas/tasks/colleges, and log results to the Barrier Log form. The paper&rsquo;s &ldquo;Instrument demonstration, public-site walkthrough&rdquo; is an existing proof; scaling a first real batch of logged runs is what makes Phase 1 genuinely done. Tomorrow: help Michelle execute/advance Phase 1 to a defensible &ldquo;done.&rdquo;

### Exact Google-Doc ethics edits (the two changes, ready to paste)

The website (`airc-sss/index.html`) and the repo copy of the paper (`airc-sss/_paper-source.html`) are now corrected and ethics-clear. The Google Doc is the last place out of date. Two changes, both in the **Guardrails → &ldquo;What the study holds to&rdquo;** section. Both are ALREADY DONE in `airc-sss/_paper-source.html`, so you can copy from there or make the two edits by hand.

**Why this matters:** the old framing implied the study only reads &ldquo;public pages.&rdquo; That is not true, the test account logs into the SIS, enrolls in a class, and uses the student intranet. And the new transparency safeguard (notify directors, label test emails) was not written down anywhere. Both are fixed below.

**CHANGE 1, replace the &ldquo;Minimal data&rdquo; bullet.**
- OLD: &ldquo;Minimal data. Public tasks run with no login, and authenticated tasks run on the single OIT-controlled test account, never a real student&rsquo;s data. Records key to the scenario, and personas are research instruments, not real people.&rdquo;
- NEW: &ldquo;Minimal data. Public tasks run with no login; the authenticated tasks, logging into the student information system (SIS) to enroll in a class, the student intranet, and the signed-in help paths, run on the single OIT-controlled test account, never a real student&rsquo;s account and never a real student&rsquo;s data. Records key to the scenario, and personas are research instruments, not real people.&rdquo;

**CHANGE 2, add a new bullet right after &ldquo;Human contact is the metric of success.&rdquo;**
- ADD: &ldquo;Transparency to staff. Before any run touches a department, the director of that department is notified in advance. Whenever the test account submits a form or a message that reaches a real staff inbox, it carries a clear identifying line stating that it is a test from a test student account for the district ARC Student Journey Barriers study, not a real student request. Staff always know a test is a test.&rdquo;

**Also scan the doc** for any place that claims the WHOLE study is &ldquo;public pages only&rdquo; and fix it, EXCEPT the limited instrument-demonstration sections (those say &ldquo;public pages only, by design&rdquo; about the demo, which is correct, leave them).

Done on the site + repo paper 26 Jul. This task is only the Google Doc copy.

## ✅ Jul 25: site accessibility + style-guide sweep (review these changed files, then push)
Fixed and verified across all 85 pages reachable from index. All changes are color/semantic/off-screen only, no margins, widths, or divider rule-lines were touched (verified: lines still inset and stop at the margin, content still `max-width:1000px` centered).
- **Green bullets sitewide.** Every prose bullet is now green (`--sage-text`) per the style guide; it was black or grey on ~44 pages. Recolor only, zero layout change.
- **Purple headings removed.** The `.subsec` / `.sec` / `h2.sec` labels were rendering in the link-purple; now grey H3 or green H2. Faux `<p>` headings on the UX Design, Data Science, and Light &amp; Lasers pages converted to real `<h3>`.
- **Structural accessibility:** added a real `<main>` + skip-link to `data-science-course/canvas.html`, `light-and-lasers/canvas.html`, and `copamigo/question-intake.html`; added a missing `<h1>` to `flow/index.html` and `roughcut/index.html`; fixed a double `<h1>` on `canvas/design-history/sorting-room-real-art.html` via `aria-level`.
- **Copy:** Light &amp; Lasers and Data Science outcome bullets capitalized and ended with periods (were lowercase with semicolons).
- Note: Course Dialer &ldquo;missing alt / untitled iframe&rdquo; and several &ldquo;heading-skip&rdquo; flags were false positives (regex strings in the tool&rsquo;s own JS, and pages that use `aria-level`).

**Still to do, needs supervision (own-interface pages, do NOT fix blind):**
- [ ] `render/index.html`: 17 `<h1>`s and 2 `<main>`s (flagship app, multi-screen; restructure carefully together).
- [ ] `canvas/design-history/index.html` and `design-history-slideshow.html`: no `<main>` or skip-link, custom full-bleed layouts.
- [ ] Heading-skips inside the CopaMigo, Wayfinder, Syllabus Checker, and Course Dialer app UIs (low severity, partly JS-generated headings).

## 🌅 TOMORROW MORNING (do these first)
**Work, first:**
- [ ] **🌐 FIX michelleblomberg.com (custom domain) — high priority, it is on your resume + Mines materials.** Full diagnosis in `notes/DNS_ISSUE_michelleblomberg.md`: the flapping is Network Solutions&rsquo; two nameservers (ns39/ns40 worldnic) disagreeing, so resolution is a coin toss (intermittent NXDOMAIN). You pulled the domain to stop it. **Recommended durable fix: move DNS to Cloudflare (free), keep the domain registered at Network Solutions.** Steps: (1) create a free Cloudflare account, add michelleblomberg.com; (2) at Network Solutions, change the two nameservers to the Cloudflare pair Cloudflare gives you (this removes worldnic from the path — the actual root cause); (3) in Cloudflare add the GitHub Pages records: four apex A records 185.199.108.153 / .109.153 / .110.153 / .111.153, and CNAME `www` &rarr; `singletrackmom.github.io`; (4) re-add the custom domain in the repo (CNAME file `michelleblomberg.com` + GitHub Pages settings) and turn Enforce HTTPS back on; (5) verify with a couple of resolvers. Claude can do the repo/CNAME side and walk you through the Cloudflare + Network Solutions clicks — have your logins ready.
- [ ] **🎯 MINES INTERVIEW (Thursday), pull the real metrics and put them into the answers.** Open Canvas **Course Analytics** for AVC100 and AVC248 and back up the STAR answers on `mines/index.html`.
  - **AVC100, validity is the headline (this is what you redesigned to measure).** Course Grade tab: click the OLD vocab quiz and the NEW applied-identification task; screenshot each box-and-whisker. The point is the *spread*: old quiz at the ceiling with no spread (measured nothing), new task has real spread (it discriminates). **Do NOT say grades went up**, a lower, spread-out average is the win for a validity redesign. Secondary: hand-count completion as a **rate** (__ of __ enrolled last summer vs __ of __ this summer; define "completed"; call it your own small-sample count you are confirming with IR). Drop Tableau DFW/success screenshots in later.
  - **AVC248, the trend is the headline.** Course Grade tab: note the median on each AI-integrated assignment (resume, cover letter, portfolio). If the earlier AVC248 terms open, compare the same assignment term over term to show the rise ("resume median went from X to Y as I built the AI workflow in"). Screenshot the scatter; use the download arrow to export the raw numbers. Pair with a student work sample.
  - **AVC248 mock-interview completion (the distributed-practice win).** Pull the before/after: after breaking the mock interview into low-stakes reps all term, near-full completion, vs barely getting anyone to attempt it before. Get the real numbers and add it to the AVC248 portfolio page and to STAR answer 7.
  - **Then fill it in:** put the real numbers into the Metrics tab blanks and back the Q&A answers on `mines/index.html`. Honesty rule: number + artifact, do not over-attribute. Everything else is already written and committed; this is just the numbers.
- [ ] **Send the Student Journey Gap Analysis to the SSS team + Sonal.** Drafts written (team note + Sonal email; asks = one test account + permission to run in Claude Cowork). Starts the ARC permission moving. ~20 min.
- [ ] **Rotate the exposed CopaMigo API key** at console.anthropic.com. 2 min, the one real security item.

**Sign-ups + money:**
- [ ] **GCC finance office:** chase the reimbursement for courses I paid for but never received.
- [ ] **Sign up for the ASU conference.**
- [ ] **Sign up for Chandler-Gilbert** (confirm which event).
- [x] EDUCAUSE, already signed up.
- [ ] **Pay bills.**
- [ ] **Email Jimmy with the taxes.**

**When there's time:**
- [ ] **Write the real synthetic-SME white paper, once there is data.** The current "The case for synthetic SMEs" page is a method/position piece, not research. A genuine academic white paper needs empirical results: Fall-pilot outcomes, the synthetic-student usability-test data compared against real-student results, OSCQR/quality-standard pass rates, and an AI-built vs hand-built quality comparison. Gather that from the pilots + synthetic-student testing, then write it up. Until then, do not call it a white paper or research.
- [ ] **Run the UX Design course through the builder + publish (after the interview).** The course is not designed yet, only the competencies are written from the advisory panel. Run it through Dial Your Course to draft the design, then put a page up. This is the course-design example I lead with for Mines, so getting it built strengthens the story. **On the overview, show the industry-validation loop concretely but WITHOUT personal names, describe the advisors by role or field (e.g. “UX practitioners on our advisory board”) and show that I run the course past them several times through the iterative design. No individual names. Seed content already exists at `canvas/avc2xx/competencies.html`.**
  - [ ] **Build the full UX course in my own format:** scaffolded modules, Discord critique loop (post early, feedback to classmates, log it, submit), Miro screenshots, the same rhythm I use across the program. Backward-designed from the advisory-panel competencies.
  - [ ] **Build the agent panel for this course (Claude will build after the interview):** a subject-matter-expert agent (or a few, split by UX subfield: research, IA/interaction, visual/prototyping), a designer/instructional-design agent, and a synthetic student agent, same model as Light & Lasers. Use `canvas/avc2xx/competencies.html` as the grounding.
- [ ] **AVC 100 Photoshop module: add a short copyright / Creative Commons lesson.** This is where students source the background photo and the cut-out animal, so it is the natural place. Cover: do not just copy an image straight off the internet (Google Images is for inspiration/tracing, not for final use); what Creative Commons is and how its license types + attribution work; why the free-license sites (Unsplash/Pexels/Pixabay) are safe to pull final photos from. Right now the assignment only points them to those sites with "no credit required," which is not the same as teaching *why*. Once it is in, the portfolio can honestly say the course covers copyright. **Draft lesson text ready to adapt: `avc100/copyright-cc-lesson-draft.md`.**
- [ ] GAIL certification exam. Study guide: `cultivate/gail-study.md`.
- [ ] **Subscribe to the AI-in-higher-ed thinkers (Substack/newsletters).** Backs the Mines Q24 "staying current" answer, so only name the ones you actually read. Set these up before you forget:
  - [ ] **Ethan Mollick**, "One Useful Thing" (Substack). The one to prioritize.
  - [ ] **Lance Eaton**, "AI+Edu=Simplified" (Substack).
  - [ ] **Anna Mills** (AI + writing, community college). Find her newsletter/where she posts.
  - [ ] **Michelle Miller**, "Minds Online" (cognition + online learning; she is at NAU, where your M.Ed. is from). Find her newsletter/Chronicle columns.
  - [ ] **Maha Bali**, "Reflecting Allowed" (equity + critical AI). Pairs with your inclusive-practices answer.
  - [ ] **Phil Hill**, "On EdTech" newsletter (ed-tech market/industry view).
  - [ ] **Jose Antonio Bowen** newsletter + **C. Edward Watson** (authors of "Teaching with AI", the book you read).
  - Already following: Nielsen Norman Group (NN/g), Bryan Alexander (Substack).

**This week, second tier (not tomorrow, maybe Tuesday):**
- [ ] **Page titles must match the tab/link you clicked (usability).** Every page should announce what it is, in both the on-page heading and the browser `<title>`.
  - **PRD pages specifically:** the PRD tab should read **"Product Requirements Document"** + the product name (e.g. "Product Requirements Document, Dial Your Course"), not just "PRD". Fix across every section that has a PRD: course-dialer, copamigo, render, syllabus-checker, cultivate, wayfinder, and any others.
  - **General rule:** if a tab says "Sample report," "Student workload," "Walkthrough," etc., the page it opens should carry that same name up top, so a visitor is never guessing what they clicked into. Sweep all sections for tab-label vs page-heading mismatches.
- [ ] Resolve the michelleblomberg.com domain / DNS issue (move off Network Solutions to Cloudflare). Background: `notes/DNS_WHAT_HAPPENED.md`.
- [ ] **Next job sweep (needs browser):** verify if the Colorado OIT "AI Program Manager" role is still open, pull real duties + salary, add to the dashboard if live. Compare head-to-head with the OIT **Senior Service Designer** already listed (5-star, $115K-$145K, verified 7/17).

---

> 🧭 **START HERE, any new session, 30 seconds. Do NOT say you are lost, it is all written down.**
> 1. You are in Michelle's repo `singletrackmom.github.io`. Read `CLAUDE.md` (who she is, the accuracy guardrails, the file map), then finish this block.
> 2. **The current plan is the red TOP PRIORITIES block directly below.** #1 is the Sonal email chain. The build priorities are Dialer, Render, and the LinkedIn profile.
> 3. **Everything done on 17 July and every file it produced is in the green "PICK UP HERE, 17 July" block right under the priorities** (the ARC study paper + website, the LinkedIn plan + profile docs in `~/Documents/Claude/JobSearch/`, the Dialer v2 PRD + `course-dialer/IP_AND_SELLING_PLAN.md` + `course-dialer/V2_RESEARCH_LANDSCAPE.md` + `tools/reference/`, and `copamigo/PILOT_HOSTING_OPTIONS.md`).
> 4. If Michelle says "look at tasks," those two blocks are the answer. Read them before asking what to do.
>
> 🗂️ **PROJECT INDEX, say a keyword and go straight to the files (updated 17 July):**
> - **Dialer / Dial Your Course** → `course-dialer/prd.html` (product + v2), `course-dialer/NEXT.md` (build handoff), `course-dialer/IP_AND_SELLING_PLAN.md` (protect + sell), `course-dialer/V2_RESEARCH_LANDSCAPE.md` (market), `course-dialer/NDA_TEMPLATE.md`, `tools/reference/` (grounding corpus), `tools/index.html` (working tool)
> - **Render** → `notes/render/` (plans), `render/prd.html`, `render/` (tool)
> - **CopaMigo** → `copamigo/prd.html`, `copamigo/PILOT_HOSTING_OPTIONS.md` (hosting/API), `copamigo2/student-resources.html`
> - **SSS study / ARC / journey** → `airc-sss/WORKING-STATE.md`, `airc-sss/_paper-source.html` (the paper source), `airc-sss/index.html` + `airc-sss/overview.html` (site), `airc-sss/export/` (build the docx/pdf)
> - **LinkedIn** → `~/Documents/Claude/JobSearch/LinkedIn_Content_Plan.md` (posts + schedule), `~/Documents/Claude/JobSearch/LinkedIn_Audit_and_ToDo.md` (profile + About)
> - **Job search** → `~/Documents/Claude/JobSearch/` (dashboards, resumes), `~/Documents/Claude/Scheduled/daily-job-search/`
> - **Master CV** → `cultivate/cv.html`.  **Cultivate** → `cultivate/`
> - **AVC100** → `avc100/` (redesign + `AVC100_All_Video_Scripts.md`).  **AVC183 / AVC248** → `canvas/avc183/`, `canvas/avc248/`
> - **FEP** → `fep/fep-2026.md`.  **Rough Cut** → `roughcut/`.  **Pilots framework** → `pilots/framework.html`
> - **Command Center** → `command/index.html` (public), `command/todo.html` (local only)
> - **Family agents** → `~/Documents/Claude/Scheduled/<name>/`; pages `focus/` (Kevin), `flow/` (Jillian), `soar/` (Jasper), `summerwork/` (Devan)
>
> 📅 **CONFERENCE CFP TRACKER (new 19 July).** Full list: `cultivate/CONFERENCE_TRACKER.md`. A scan runs about every two weeks and drops new open CFPs here.
> **Open now:** Magna “AI in Education” (deadline **Aug 14**, virtual Dec 2026, has an “Integrating AI into Course Design” track, best near-term fit) · SXSW EDU 2027 PanelPicker (deadline **~Jul 26**, a stretch pre-build) · UPCEA Annual 2027 (**Aug 14**) · Maricopa Student Success (**Sept 11**, local).
> **Watch (CFPs open Aug–Oct):** QM Connect 2027, League Innovations 2027, OLC Accelerate/Innovate 2027, Online Teaching Conference 2027.
>
> 🟣 **SSS JOURNEY PAPER, open items (added 19 July).**
> 1. **Contacts for the usage-data email.** Build the full named-contact roster (service owner / director + email per college) so Michelle can email each college requesting usage numbers. Per the data rule this goes in the PRIVATE team spreadsheet (`Maricopa_Student_Services_Inventory.xlsx`), NOT the public paper. the paper keeps offices/titles only. Real research pass across 10 colleges; GCC sample done, 9 to go, then verify every crosswalk cell.
> 2. **Double-check the crosswalk in Appendix B** (the full per-service tables) against each college once contacts are in.
> 3. **Mini-study origin paragraph.** The paper explains WHY synthetic AI testers over humans (strong: WGU model, validation gate, literature), but does NOT tell the story of the first small pilot that did not really work and why it led to the AI-agent method. Michelle to give the facts (what was tried, why it fell short); then add a short honest paragraph in Method.
>
> 🎓 **Finish the near-complete credentials, priority order: League, Google, Anthropic, UM.** League for Innovation AI Fellows (in progress, capstone through Oct 2026); Google GAIL (take the certification exam; study guide at `cultivate/gail-study.md`); Teaching AI Fluency, Anthropic Academy (almost done, finish next week); U-Michigan "Gen AI as a Learning Design Partner" Coursera (almost done, finish next week). Then the extra Coursera courses already signed up for, if time. (Done: QM earned, EDUCAUSE earned, Purdue course completed; Scrum removed from CV, not started.)
>
> 🗓️ **SUMMER TIMELINE (added 19 July, ~3 weeks to semester). Holding this so Michelle does not have to remember it.**
> **Immovable anchor:** AVC100 and AVC183 ready before students arrive. Everything else (Dialer, paper, overviews, LinkedIn) yields to the courses.
> - **FIRST, tomorrow AM:** send the Student Journey Gap Analysis to the team + Sonal to start the ARC permission moving. Drafts written; the asks are one test account + permission to run in Claude Cowork. ~20 min, not a build.
> - **This week (Jul 20-26): courses only.** Close out AVC100 and AVC183. If both cannot fully close, finish the one taught first, get the second to a teachable draft, finish it early next week. Also rotate the exposed CopaMigo key (10 min, urgent, not a project).
> - **Jul 27 - Aug 9: AVC248 + tools.** AVC248 walkthrough-video rework, then heads-down Dialer v1 build (spec is ready). The Dialer is the flex: it has no deadline, so a course fix always wins.
> - **Vacation: 1 week (TELL CLAUDE WHEN, it removes a week).**
> - **Semester start: ~Aug 10 (CONFIRM the exact date).**
> - **Paper to Sonal / ARC approval:** on their clock, not Michelle's build time.
>
> 🟠 **DMA JOBS AGENT, one-time on-computer fix (added 19 July). REMIND MICHELLE.** The DMA jobs agent now runs off the repo (`discord/DMA_JOBS_AGENT.md` + private `discord/.webhook.local`), and the corrected 4-year rule is live in CLAUDE.md, so manual runs work today. BUT the old scheduled task still reads a stale protected file the cloud cannot write. To finish it: start a Cowork task **ON MICHELLE'S COMPUTER** (not the cloud) and say *"Fix the DMA scheduler file. Read `discord/ON_COMPUTER_FIX.md` and do exactly what it says."* That is a ~5-minute one-time cleanup. Until then, the startup catch-up covers it. If a new session sees this and Michelle is on her computer, offer to knock it out.
>
> 🔴 **TOP PRIORITIES (reset 17 July, late, Michelle's brain-dump). THIS IS THE PLAN. Sort the 4-week schedule tomorrow. Vacation is in the middle of those 4 weeks.**
>
> 🔐 **URGENT, ~2 minutes, do before anything else: ROTATE THE EXPOSED ANTHROPIC KEY.** Overnight research found a LIVE Anthropic API key hardcoded (obfuscated char-code array, ~line 568) in `copamigo/index.html`, which calls api.anthropic.com from the browser (~line 1792). It is publicly readable on the live site and in git history, so it can be abused and billed to Michelle's account. **Revoke/rotate it at console.anthropic.com immediately.** Deleting it from the file does NOT un-expose it (git history + live cache); rotation is the only fix. CopaMigo's AI should stay off until the key moves to a server-side proxy (see #4).
>
> **#1, MOST IMPORTANT, the Sonal chain (do first, in order). Nothing gets sent without Michelle's approval.**
> 1. **Read the SSS study document one more time, end to end, confirm 100% accurate** before anything goes out. (`airc-sss/_paper-source.html`; the .docx/.pdf come from `airc-sss/export/build.sh`.) She forgot to send it; this is the gate.
> 2. **Send the long "student journey" email + the document to Sonal (OIT).** The three asks: permission to use Claude/Cowork, one OIT-controlled test account, and the Salesforce owner contact. (Locate/confirm the drafted Sonal email first.)
> 3. **After Sonal replies/approves: email the SSS committee** with a link to the document, telling them they are not the ones running the student journeys. CONFIRM the exact framing with Michelle before drafting.
> 4. **After Sonal's approval: email the head-of-student-services leadership roster** (the outreach list in the paper) to get them onboard.
>
> **#2, the three build priorities:**
> - **Dialer**, finish v1, then the v2 build (v2 PRD + reference library are written, see the 17 July block below).
> - **Render**, production hardening; the Fall 2026 pilot depends on it.
> - **Fix the LinkedIn profile**, paste the drafted Projects, About, and job descriptions from `JobSearch/LinkedIn_Audit_and_ToDo.md`.
>
> **#3, server space** to put the new **Student Resources button up in Canvas** (needs hosting).
>
> **#4, CopaMigo is NOT expected to launch by Fall** (district still defining a pilot format). Deprioritized, BUT overnight research on getting it off Michelle's personal GitHub with a safe API is in **`copamigo/PILOT_HOSTING_OPTIONS.md`**. Recommended: move the frontend to a GitHub org she controls (ideally Maricopa's) and put the Anthropic key in a **server-side proxy she owns (Cloudflare Worker, free, 100k req/day)**; fastest-pilot fallback is a **Google Apps Script relay** (the pattern she already uses for Render + Rough Cut). Avoid Vercel free tier (non-commercial terms). **KEY INSIGHT: this ONE proxy pattern solves the same API-key problem for the Dialer v2, Render, and Rough Cut too, build it once, reuse everywhere.** See the urgent key-rotation note at the top.
>
> **Overnight research also done (both saved, ready for tomorrow):** `course-dialer/V2_RESEARCH_LANDSCAPE.md` (the full instructional-design + course-tooling landscape for the Dialer; headline: no competitor does BOTH audit and build in one free, data-sovereign tool, that is the open lane; OLC's new 2025 scorecard is replacing OSCQR; the ADA WCAG 2.1 AA deadline gives the accessibility checks legal teeth) and `copamigo/PILOT_HOSTING_OPTIONS.md` (above).
>
> **Dialer IP + business/selling plan (NEW, 17 July night):** `course-dialer/IP_AND_SELLING_PLAN.md` is the chronological plan, Phase 0 (confirm ownership) → Phase 1 (fall faculty pilot, the must-do) → Phase 2 (job search: warm intros over cold, finish the LinkedIn profile, target roles she fits) → Phase 3 (EDUCAUSE) → Phase 4 (pick the vehicle) → Phase 5 (approach companies) → Phase 6 (honest odds), plus a target list (companies = Instructure then Cidi Labs; nonprofits = EDUCAUSE/OLC/QM/League, connectors not buyers). `course-dialer/NDA_TEMPLATE.md` is the mutual NDA for company demos. **Ownership: Michelle built it off-contract (9-month employee, summer), on her own computer + own paid Claude account, tested only on her sandbox archive (no live Maricopa course or student data), started last week, so she very likely owns it outright, just confirm the RFA/IP policy language.** Live-tool links are OFF the portfolio (overview now says it is IP, demo on request); "© 2026 Michelle Blomberg. All rights reserved." added to all 241 page footers. Honest read: a retire-money sale is very low odds; the tool's real payoff is as proof that lands a job.
>
> **Fall course crunch (~4 weeks, vacation in the middle, sort the schedule tomorrow):**
> - **AVC100 videos**, never made, and she hates making video, so **break them out one per day** to force it. Scripts exist at `avc100/AVC100_All_Video_Scripts.md`.
> - **AVC183 fully dialed** for Fall (net-new). Can **test it through the Dialer tool**.
> - Both courses bulletproof BEFORE moving on. Then **Render + AVC248**.
>
> **After the Dialer is done:** make the **League final capstone video**, and **email the League** to ask why she cannot sign up for the next level of the capstone (she tried, it did not work).
>
> **Financial / reimbursements (batch):** file reimbursement for the 2 things already taken + paid; turn in reimbursement paperwork for the **EDUCAUSE conference** (paid); **register + pay** for the **ASU conference** and the **Chandler-Gilbert conference**, then reimburse.

> 🟢 **PICK UP HERE (written 17 July 2026, Cowork session). NEWEST BLOCK, supersedes below. Big session, here is where every piece stands.**
>
> **1. ARC SSS study PAPER, heavily dialed and re-exported.** Source `airc-sss/_paper-source.html`; build with `airc-sss/export/build.sh` → docx + pdf. The headline fix: the account model now reads ONE way everywhere, a single **OIT-controlled test account** (a sanctioned test account, no real student data, not even Michelle's, NOT member MEIDs). Synthetics run authenticated tasks on that one account. Removed every "OIT won't provision / member's own account" contradiction. Also: fixed the timeline table overflow, replaced the plain demographics table with an embedded **graphic** (`airc-sss/demographics.png`, source `demographics.svg`), gave the docx tables borders (`export/finish_docx.py`), added the online-attrition weighting rationale, and both letters now read as the co-chair sending them. **Salesforce stays IN the paper** (deferred second-wave limitation); it was only stripped from the website. Delivered as a zip; Michelle is uploading the .docx to Google Docs.
>
> **2. ARC SSS WEBSITE (`airc-sss/index.html` tabs + `overview.html`), aligned to the paper.** Same one-test-account model. Removed ALL WGU mentions, all citations and the "evidence" section, and the Salesforce / "district declined a vendor" lines (paper keeps them, site does not). Rebuilt the demographics chart (race + modality bars + figures + a "what each persona carries" line). Beefed the thin tabs (Metrics, Pilots). Removed the duplicate status-note from the study page (it lives on `overview.html`, the case study, which is the shareable page). Added Open Graph share tags + **`airc-sss/og-cover.png`** (rendered from `cover.svg`) so LinkedIn previews show the journey image. NEW HARD RULE now in `CLAUDE.md`: every shareable page needs a PNG og:image, never an SVG.
>
> **3. LinkedIn (PRIVATE, `~/Documents/Claude/JobSearch/`), two files.**
> - `LinkedIn_Content_Plan.md`, the posting engine. **Mon + Thu**, alternate a **student win** and a **tool**, dated through Aug 13. **Post 1 (Journey study) is POSTED** with og-cover.png. Next up: **Mon Jul 20 = AVC100 at-sea student win (drafted, ready)**, **Thu Jul 23 = DMA Jobs Discord agent (drafted, ready)**. Tool order: Journey → Discord → Dialer → Render → CopaMigo → Wayfinder (Cultivate already posted). Banks inside: student wins, post ideas (Rough Cut newsletter, tool walkthroughs), timely posts (EDUCAUSE cert caption, the community-of-practice post, "summer of agents").
> - `LinkedIn_Audit_and_ToDo.md`, the profile build. Findings: **Projects section is EMPTY** (biggest, fastest win), 5 of 6 jobs have no description. Ready to paste: all Project blurbs (+ the experiential ones) and the **About** (short, AI/ID-forward; corrected to "AI Resource Center" not committee, "XanEdu, a startup division of ProQuest," XR-lab claim removed, measurable-assessment not over-claimed since she says it is not a strength). Talks go in the **Publications** section (already on the CV `cultivate/cv.html`), never Projects. Tasks #21-23.
> - Follow button (free, not paid): Settings & Privacy → Visibility → Followers → Make follow primary.
>
> **4. Dial Your Course v2, PRD written + reference library built.** `course-dialer/prd.html` section 7 now holds the full v2 vision: the alternate-assessment menu, UDL recommendations, the RSI writer, the ID-model lens checkboxes, **builder mode** (takes course + lesson objectives typed by hand, because outcomes do not survive the export), the four-tab shell (Audit / Builder / Syllabus / Report) with the syllabus checker rolled in, multi-format export (HTML / PDF / Word / Canvas), and the reference-library architecture. **Research repository built at `tools/reference/`** (README + ALTERNATE_ASSESSMENTS, UDL_3, RSI, ID_MODELS, OSCQR_QM_CROSSWALK, alongside the existing BLOOMS / SEAT_HOURS / AUTHENTIC_ASSESSMENT). Model without Michelle's personal key = the bridge for the pilot, a district proxy to scale. Pointer added to `course-dialer/NEXT.md`. STILL the first move: the two 5-minute outcomes-export tests. Task #16.
>
> **Open loops for next time:** Wayfinder needs a one-line description (for LinkedIn + the PRD). Run the two Canvas outcomes-export tests. The LinkedIn profile build (Projects, About, job descriptions) is drafted and waiting for Michelle to paste. Aligning the website About and LinkedIn About to one voice is offered, not yet done.
>
> **Also 17 July night (portfolio + IP + housekeeping):** Removed "Near Z Degrees" from the homepage bio (kept OER). Corrected the math-mural caption (`studio/overview.html`). Added "© 2026 Michelle Blomberg. All rights reserved." to all 241 page footers. Added Open Graph share tags + `airc-sss/og-cover.png` (PNG) so LinkedIn previews show the journey image. Pulled the Dialer's live-tool links off `course-dialer/overview.html` and replaced with an "it's IP, demo on request" note. Built the Dialer **IP + selling/business plan** (`course-dialer/IP_AND_SELLING_PLAN.md`, chronological Phase 0-6 + target list + "what if Canvas copies it, can I sue" + NDA at `course-dialer/NDA_TEMPLATE.md`). **Ownership confirmed strong:** Michelle built it off-contract, own computer, own paid Claude account, tested on her sandbox archive only, started last week, so she very likely owns it outright. App-update fix + session/login best practices saved at `notes/CLAUDE_APP_UPDATE_FIX.md`.

> ⭐ **PRIORITY STACK (16 July 2026), read top to bottom. Fall is one month out; everything below competes for that month.**
>
> **1. TODAY (time-sensitive):**
> - Finish the DMA Discord jobs agent (relay setup or manual post today). Saved and scheduled; just needs the posting path closed.
> - Portfolio format research (case study vs. overview, and an outcomes/results section). This jumps ahead of the classes ONLY because **Tommy Bishop (WGU) is reading the portfolio today.** Research and decide, no full rebuild yet, timebox it.
>
> **2. NEXT 2 DAYS (hard deadline, non-class, must not slip):**
> - Taxes: mine and Mom&rsquo;s. Pay bills.
>
> **3. THIS MONTH, the big block, CLASSES FIRST (each about a week minimum to build out):**
> - **AVC183 (Digital Graphic Design 1)** fully dialed for Fall. Net-new for Fall 2026, so it needs the most runway, start here.
> - **AVC100** fully dialed for Fall. Already built, needs dialing and polish, so it should move faster.
> - The point of finishing both: free up attention for 248 and Render.
>
> **4. AFTER 183 and 100 are dialed:**
> - **AVC248** build and prep.
> - **Render** production hardening (badly needs attention; Fall 2026 pilot depends on it).
>
> **Reality check:** ~4 weeks total. Two class weeks + 248 + Render leaves almost no slack, so taxes/bills stay in their 2-day slot and the portfolio work stays research-only. If a class week slips, 248 and Render are the casualties, protect the class weeks. (Order of 183 vs. 100 is my call based on 183 being net-new; flip it if 100 is actually further from done.)

> 🟣 **PICK UP HERE (written 16 July 2026). NEWEST BLOCK, supersedes below.**
>
> **DMA Discord jobs agent: SAVED and scheduled today (the fix for the &ldquo;it disappeared&rdquo; problem).** It is now a real scheduled task `dma-jobs-daily` (in the Scheduled folder), runs every morning around 7 AM, finds up to 3 fresh entry-level/internship digital-media jobs and posts them to the DMA student Discord jobs board. Dedupe memory lives at `discord/posted-jobs.json`, seeded with yesterday&rsquo;s 11 posts so nothing reposts. Now covers **game design** plus a **software keyword sweep** (Photoshop, Illustrator, InDesign, After Effects, Premiere, Figma, Cinema 4D, Blender, Unity). Hard filter: entry-level or intern only, bachelor&rsquo;s &ldquo;preferred&rdquo; ok but &ldquo;required&rdquo; out, 2 years experience max.
> - **OPEN:** Discord is firewalled from the agent&rsquo;s sandbox, so hands-off posting needs a **Google Apps Script relay** (about 10 minutes, browser only, same pattern as Render and Rough Cut). Until the relay URL is set, the agent queues its picks to `discord/queue.json` and posting happens through the browser. Relay code + steps provided 16 July.

> 🔵 **Portfolio format study (NEW 16 July, research and decide, do NOT rebuild pages yet):** Compare my **Goal / Audience / Process** &ldquo;overview&rdquo; format against the &ldquo;case study&rdquo; format used by Angelique (design-by-angelique.lovable.app): **Problem / What she did / Software used / Outcomes.** Answer: (1) Is &ldquo;case study&rdquo; the industry-standard page label, should I rename &ldquo;overview&rdquo;? (2) Do most edtech/UX portfolios use problem-solution-outcomes, or is my Goal/Audience/Process fine as-is? (3) Should I add a **Software used** line? (4) Should I add an **Outcomes / Results** section (she shows outcomes at the bottom, I show none)? **My AVC100 survey results just came in, use them as the first test of an outcomes/results section.**
>
> **Find more education-focused BUILDER people to model (NEW 16 July):** UX / design / tool-builders (not pure developers), ideally degrees in education or edtech but not required. Pull their resumes and note whether they use case studies. Feeds both the resume format and the portfolio-format decision above.
>
> **Coursera certificate for &ldquo;measuring learning effectiveness&rdquo; (NEW 16 July):** Angelique did a LinkedIn Learning course on this; I don&rsquo;t pay for LinkedIn Learning but I do pay for **Coursera**. Find a Coursera certificate or program equivalent (learning measurement, evaluation, analytics, Kirkpatrick, and similar).

> 🌐 **Network Solutions / michelleblomberg.com domain (TODAY priority, 16 July):** The custom domain has a persistent Network Solutions DNS problem. It resolved once, then went down about half a day later, so I unhooked it from GitHub Pages and am handing out **singletrackmom.github.io** for now. I pay for **michelleblomberg.com** and want it actually working. There is an open Network Solutions ticket and a full DNS report already on file (find it, it has the ticket number). Goal: diagnose the recurring failure and get michelleblomberg.com reliably pointing at the GitHub Pages site.

> 🧭 **AI pilot-to-production framework (NEW 16 July, TODAY, first draft DONE):** The real gap, faculty are building AI tools with no safe, shared way to get them off personal servers into a district-hosted pilot with real faculty/staff/students, then into production. Campuses are not helping, so this is pitched as district-hosted. Draft lives at `pilots/framework.html` (noindex, shareable link). Covers: why it exists, a one-page pilot-request intake, what to ask the district for (safe sandbox hosting + an approved API path + a right-sized review), guardrails (data minimization, FERPA, isolation from the SIS, approved AI only, human-in-the-loop, sunset date), data/API rules (default no student PII, data-sovereign by design, no personal keys, nothing sent to a model that trains on it), what counts as success to move a pilot to production, a plain-English Docker explainer (Gordon&rsquo;s faculty expert recommended Docker), and the existing frameworks it adapts (NIST AI RMF, EDUCAUSE AI governance + ethics, WCET, FERPA). TO DO: Michelle reviews, then sends to the district AI CIO (from Intel, will know this space) for input; refine the intake fields and review timeline with OIT.

> 📷 **Traveler cover photo (do when back in the office, ~Aug 17):** shoot and swap in a new cover image for the Traveler case study. Current cover is a placeholder/thin; replace it once Michelle has camera access to campus again.

> ⭐ **PICK UP HERE (written 14 July 2026, late night). THIS BLOCK IS NEWEST AND SUPERSEDES THE ONES BELOW.**
>
> **WGU interview: Wednesday July 15, 3:00 PM Mountain, Director Tommy Bishop.** Everything to walk in with lives in `~/Documents/Claude/JobSearch/WGU_Application/`:
> - **`WGU_INTERVIEW_MASTER.md`** ← read this first, it maps the other four and gives the game plan.
> - `WGU_qual_study_guide.md` (every qual as a Q + answer, Why WGU, my questions, the self-funded-R&D story), `WGU_interview2_prep.md` (the validity conversation), `director-questions-answers.md` (futurist Qs), `WGU_assessment_deep_dive.md` (people + field + the Kate Smith / Rio Salado opener).
> - Mines application submitted (merged PDF in `JobSearch/Mines_Application/`). Done.
>
> **Barriers study tester tool: BUILT and live-ready** at `airc-sss/run.html` (auto-assigns 1 of 169 scenarios, tester picks their college, 15-min rules, no login/API). How-we-run-it doc + the exact team message: **`airc-sss/RUNNING-THE-STUDY.md`**.
> - **OPEN (needs Michelle): create the Google Form** (fields listed in RUNNING-THE-STUDY.md), send Claude the link, Claude pastes it into `LOG_FORM_URL` in `run.html`. Until then the Log button says &ldquo;link pending.&rdquo;
> - Optional next: pre-fill the form with Scenario ID + persona + campus (needs one &ldquo;Get pre-filled link&rdquo; sample).
> - Study-page polish done tonight: tab tops fixed (3px hairline), broken run-sheet link repointed to `#instruments`.
>
> **Domain (michelleblomberg.com): DO NOT resolve tonight. Start tomorrow AFTER the interview.** It is a Network Solutions DNS problem with an open ticket (see the full DNS report / ticket number already on file). The GitHub site itself works fine at **singletrackmom.github.io**, keep using that URL on everything. What looked like the site being &ldquo;gone&rdquo; in the browser was a stale cached redirect, not the server.
>
> **Render:** started the &ldquo;less purple/cream&rdquo; color pass (page + `--warm` now white/neutral). Left at a safe stopping point; revisit the pill/accent tones later if still too purple. CopaMigo left as-is per Michelle.

> 🚨 **PICK UP HERE (written 13 July 2026, late night). THIS BLOCK SUPERSEDES THE ONE BELOW.**
>
> **The site is FROZEN until Wednesday July 15.** Mines closes Wednesday. The WGU second
> interview with Tommy Bishop is **Wednesday July 15 at 3:00 PM**, and he is likely reading the
> portfolio right now. Do not push half-finished pages.
>
> **Three documents hold everything and MUST be read before touching the portfolio:**
> - **`notes/portfolio/STUDIO_ASSETS.md`** · ⭐ **EVERY YouTube link, Miro board, brief, and
>   photo still needed, in ONE place.** Nothing else is organized, so this file is the source
>   of truth. Add to it the moment anything is found. Includes the redaction list.
> - **`notes/portfolio/STUDIO_PLAN.md`** · the argument and the phased to-do. A decade of
>   student client work found in Miro boards and old briefs.
> - **`notes/portfolio/GAP_FILL_PLAN.md`** · where the words *pilot*, *accessible*,
>   *competency*, and *adult learner* go.
>
> **⛔ NO DATES ANYWHERE ON THE PORTFOLIO.** Not career dates, not project years, not "recently."
> Every piece stands undated. Do not re-litigate this.
>
> **THE HEADLINE FINDING:** Michelle has been running a design studio with a **student project
> manager, a written brief, a client approval cycle, and real stakeholders since at least
> 2014**, and running **faculty-SME builds with student developers since her Director of
> Instructional Technology years.** The Traveler 60th Anniversary Edition ran the full arc,
> concept, primary research, a design system, a presentation to the **college president**, a
> print purchase order, delivery, and **three Pinnacle Awards from the College Media
> Association.** She has been telling herself she has "no formal PM experience." That is false,
> and correcting it is the single biggest change to how she should talk on Wednesday.
>
> **ORDER OF WORK:**
> 1. **Mines OLED application, closes Wednesday.** Resume + cover letter already updated with
>    the studio, the OER-evaluation reframe, and the reusable-learning-objects history.
>    **Both `.md` files are edited. The `.docx` and `.pdf` still need a REBUILD from
>    `build_mines.js`.** That is the next concrete task.
> 2. **WGU prep.** `~/Documents/Claude/JobSearch/WGU_Application/WGU_Interview_Prep.md`.
> 3. **Thursday and after:** the studio page rebuild, per `STUDIO_PLAN.md`.
>
> **⚠️ DNS IS NOT FIXED. IT IS INTERMITTENT.** Ticket **I-26067315**. The registrar dropped the
> NS delegation, re-added it at 2:27 PM July 13, and **the domain STILL failed on cellular at
> 6:25 PM** with `ERR_NAME_NOT_RESOLVED`. An intermittent domain is more dangerous than a dead
> one, because it works every time Michelle checks and fails for the person who matters.
> **Everything, including the exact escalation message and the Cloudflare fallback, is in
> `notes/DNS_WHAT_HAPPENED.md`. Read it before calling them.**
>
> ### ✍️ MINES APPLICATION, CARRY THESE IN (July 14)
> When the Mines resume and cover letter are opened, weave in the language developed on the portfolio today:
> 1. **The closing line from the study:** the people closest to the problem should be building the answer. A student who has been lost in the financial aid pages understands that barrier in a way a vendor never will. This is the strongest sentence available for the cover letter.
> 2. **Everything added to `about.html` today**, because it was written against the Mines requirements: build IN the LMS (courses ship as clean Canvas packages), design from OER and licensed materials (cost off students, copyright clean), course-level learning analytics and persistence, the hard no-PII line, storyboarding + writing the scripts + recording the video + writing the instructional copy, running the pilot AND the professional development that follows.
> 3. **Assessment that a model cannot complete** (Mines requirement 5). The Design Studio line: the assessment IS the professional task, there is nothing a model can hand back that a client will accept. Plus the authentic-assessment research thread.
> 4. **Multidisciplinary student build teams** on the district study (computer science, information systems, digital media, business, communication), which is the "by students, for students" claim she has always been strongest at.
> 5. Make sure the RESUME carries the Mines keywords too (LMS/Canvas, OER, copyright, accessibility/ADA/WCAG, learning analytics, storyboarding, Adobe, HTML/CSS, adult learning, curriculum), since the ATS scans the resume, not the letter.
>
> ### 🔴 DNS, PARKED ON PURPOSE. DO NOT LOSE THIS. (July 14)
> **July 14:** the domain failed again (`DNS_PROBE_FINISHED_NXDOMAIN`). Michelle **detached the
> custom domain in GitHub Pages**, which is the emergency lever. GitHub deleted the `CNAME` file
> on the remote, so `singletrackmom.github.io` now serves the site directly with no redirect.
> **Use `singletrackmom.github.io` on the Mines application. Do NOT put michelleblomberg.com on
> anything submitted until it is proven stable for a full day.**
>
> **AFTER the portfolio is done and the Mines app is sent, do this, in this order:**
> 1. **Call or write Network Solutions. Ticket `I-26067315`.** The escalation message is already
>    written, ready to copy, in `notes/DNS_WHAT_HAPPENED.md`. It ends with the two questions they
>    cannot dodge: confirm that **both** ns39.worldnic.com and ns40.worldnic.com are serving an
>    identical, correct zone for michelleblomberg.com, and explain how the NS delegation came to
>    be removed from a domain she never modified. "It works on our end" is not an answer.
> 2. **If they cannot prove both nameservers serve the same zone, move DNS to Cloudflare (free).**
>    The domain stays registered at Network Solutions; only the nameservers change, so their
>    broken servers are never asked again. It is a web form, no Terminal, but it takes 24 to 48
>    hours to take effect, so **do it after the WGU interview, never in a hurry.**
> 3. **Only then** re-attach the custom domain in GitHub Pages and re-test on **cellular with
>    Wi-Fi off**, more than once, across a full day, before trusting it on an application.

---

# ☀️ TOMORROW MORNING, IN THIS ORDER. NO DEVIATION.

### 0 · FIRST THING: check the domain (5 minutes)
Load **michelleblomberg.com** on the phone, **Wi-Fi OFF, cellular only**, and then again on the
laptop.

- **It loads, both** → good, leave it, move on to the resume.
- **ANY failure** (`ERR_NAME_NOT_RESOLVED`, `NXDOMAIN`, "cannot be reached") → **CUT IT.**
  Michelle's own words: *"if not, cut it."*
  **GitHub → repo → Settings → Pages → Custom domain → clear the box → Save.**
  That instantly restores `singletrackmom.github.io` as a rock-solid link.

**Why this is task zero:** the custom domain being attached means `singletrackmom.github.io`
**redirects to it**. So if the domain is flaky, BOTH links are flaky, and the resume goes out
with a link that may be dead when a Mines reviewer clicks it. It failed on cellular at 6:25 PM,
hours after the registrar's "fix." Ticket **I-26067315**.

**Whatever link is proven working at that moment is the link that goes on the resume.**
(Cloudflare migration is the permanent fix. AFTER Wednesday, it needs 24 to 48 hours.)

### 1 · GET THE RESUME AND COVER LETTER OUT THE DOOR. NO MORE STALLING.
Michelle's words. **This is the number one thing tomorrow.** Mines closes Wednesday.

- [ ] **Rebuild `.docx` + `.pdf` from `build_mines.js`.** The `.md` files are DONE and edited.
- [ ] Confirm the Creative Commons question (name the license types only if she actually uses them)
- [ ] Check page breaks (was 4 pages, the new Technical Skills block adds length)
- [ ] Put the WORKING link in the header (see task 0)
- [ ] Read once. **SUBMIT.** Do not reopen it. Do not improve it. Submit it.

### 2 · The dialer
Test v1 end to end with a real Canvas export. Then make `course-dialer/overview.html` tell the
truth about what it actually does. See the BLOCKER section below.

### 3 · Dial in the student projects
The Design Studio + Traveler split. See `notes/portfolio/STUDIO_ASSETS.md`.

### 4 · RENDER. Fall is looming.
Her own words: *"one of these days I really need to get back to Render, fall is looming."*
It is ranked #1 on her own dashboard, the pilot is Fall 2026, and it has been getting starved by
everything else. **Do not let another week go by.** After Wednesday, it gets a real block of time.

---

# 🎯 THE PRIORITIZED LIST (written 13 July 2026, night)

## ⛔ BLOCKER, do tonight or first thing: the Dial Your Course honesty problem

The live overview describes a **working tool in the present tense**: *"Nineteen of them run…
the tool writes them back and hands you a package ready to reimport."* And its headline claim
is *"is every outcome the course claims actually evidenced by something it grades?"*

**That check cannot currently run.** `canvas/reference/CANVAS_OUTCOMES_EXPORT_BUG.md` documents
that Canvas Outcomes never reach the `.imscc` export. Michelle: *"I have no idea if it works."*

**This is the single biggest risk on the site**, because it is the tool most aligned to both
jobs, so it is the one a hiring manager opens first.

- [ ] **TEST v1 end to end.** Drop a real Canvas export in. Record exactly what runs, what
      reports, what writes back, and what fails.
- [ ] **Rewrite the overview to match reality.** "A prototype that reports, with writeback in
      development" is respectable. A tool that claims what it cannot do is not.
- [ ] If the outcomes check is blocked, **say so on the page.** Naming the Canvas export bug is
      a credibility gain, not a loss. It shows she read the source.

---

## 1 · MINES (closes Wednesday July 15)
- [ ] **Rebuild `.docx` + `.pdf` from `build_mines.js`.** The `.md` files are already updated:
      studio bullet, reusable-learning-objects bullet, OER-evaluation rewrite, video/sound-off
      constraint, project-management paragraph, and a **new Technical Skills block (it was
      missing entirely, so the ATS had nothing to scan)**.
- [ ] Confirm: **do we name Creative Commons license types?** Only if she actually uses them.
- [ ] Check page breaks (was 4 pages, skills block adds length).
- [ ] Read once. **Submit.**

## 2 · WGU, Tommy Bishop, Wednesday 3:00 PM
- [ ] `~/Documents/Claude/JobSearch/WGU_Application/WGU_Interview_Prep.md`
- [ ] **The new answer:** she has been running a studio with a student PM, a written brief,
      client approval gates, and stakeholders since 2014, and faculty-SME builds since her
      Director of Instructional Technology years. **Stop saying "I have no PM experience."**
- [ ] **The closing line, spoken, no dates:** *"Because I built one. An online student
      assembling a computer from a 3D model, with a faculty SME supplying the content. The idea
      was right and the tooling wasn't. It is now."*
- [ ] Ask permission before recording. If he says no, debrief immediately after.

## 3 · SITE FREEZE until Wednesday
No pushes. Tommy is reading it. Exceptions already made and finished: the OER video on
`murals/overview.html`, the command-center fixes, and the Dial Your Course wording fix above
(that one is a correction, not a feature).

---

## 4 · THURSDAY: the portfolio, in order

### 4a · Truth and consistency pass (do first, it is cheap)
- [ ] **Dial Your Course wording** matched to what v1 actually does
- [ ] Word-level insertions per `notes/portfolio/GAP_FILL_PLAN.md`: **pilot** (render, avc100,
      course-dialer, airc-sss, copamigo2, authentic-assessment), **accessible** (avc100,
      course-dialer, about), **competency** (course-dialer, authentic-assessment, avc100),
      **adult learner** (about, avc100)
- [ ] **Rewrite "Call for collaborators" into "The faculty partnership model"** on
      `authentic-assessment/`. Highest-value single edit on the whole list. Tommy will read it.

### 4b · The two missing pages
- [ ] **`/course-review/overview.html`** · QM + OLC/OSCQR campus-wide lead reviewer since 2011,
      WCAG 2.1 AA, ADA, Yuja Panorama, CidiLabs UDoIt, faculty coaching. **Biggest Mines hole.**
      It is also the origin story of Dial Your Course, currently buried mid-paragraph.
- [ ] **`/oer/overview.html`** · she serves on the committee, **evaluates** OER, runs the faculty
      workshops, built Near Z, won the Gaucho Globe. Honest note: adoption across the college is
      uneven. Her selection criterion (will this resource still exist in October) is the best
      line in it.

### 4c · The studio page (see `notes/portfolio/STUDIO_PLAN.md` for the full evidence log)
- [ ] **REDACT the Miro boards first.** Three colleagues' work email addresses are on the OER
      board. Student full names on the Traveler decade assignments. Avatars everywhere.
- [ ] Export: full board as JPG, section crops as PNG, into `/assets/studio/`
- [ ] **Rename the page.** "Murals and client projects" undersells a decade-long studio.
- [ ] **Lead with The Traveler 60th.** Only complete arc with a national outcome (3 Pinnacle
      Awards, College Media Association).
- [ ] Then OER promo, Healthcare Technology, STEAM, Fitness app (dated, framed as the course
      that preceded the grant-funded studio).
- [ ] **The method is the point:** student PM, written brief, client proof cycle, approval gate,
      delivery. Show the International brief as the artifact.
- [ ] Keep the mural photo as the `work.html` thumbnail. Still the strongest image on the site.

### 4d · Photo shot list
- [ ] **Astronomy pin** (it is in her desk at work; ask Kevin to shoot it)
- [ ] Science Olympiad + Odyssey of the Mind shirts
- [ ] Harry Potter library map (ask the library if the file survives)
- [ ] Theatre and dance posters
- [ ] Fitness app screens (stills from the video)
- [ ] Clean photo of the 90-foot mural (only on Instagram now)

---

## 5 · WALKTHROUGH VIDEOS, in priority order
1. [ ] **Render** · flagship, Fall pilot, both jobs care
2. [ ] **District UX study (ARC)** · biggest thing she has run, and it is Tommy's world
3. [ ] **The Traveler** · only complete arc with a national outcome. **Doubles as the After
       Effects video she already owes herself.** Board flythrough.
4. [ ] **CopaMigo** · strong, story tells itself
5. [ ] **Dial Your Course** · ONLY once v1 actually works. Do not film a broken tool.
6. [ ] **Wayfinder** · last, optional, it is a road-trip planner
7. [ ] **AVC 248 capstone example video** · record your own portable career agent walkthrough for the AVC 248 signature-project page (the instructor example that sits alongside student work). Low priority, not happening soon; the page is built with a placeholder until this exists.

---

## 6 · AFTER ALL OF THAT
- [ ] **Dial Your Course v2 → BOTTOM OF THE LIST.** You cannot build v2 of a tool whose v1 does
      not run. This is not close.
- [ ] **Dial Your Course, add a maker mode.** A competitor exists that only builds courses.
      Differentiate by offering BOTH: import an existing course to check and tune it, or build a
      course from scratch from a template. Add build-from-scratch as a second path alongside the
      import-and-check path.
- [ ] The two Canvas outcome tests (5 minutes, they settle the export bug)
- [ ] **AVC 100 survey results** → this is the first project to reach **Measure**. Analyze and
      write it up. It is the evidence the whole portfolio is missing.
- [ ] ARC SSS meeting notes + the checking form
- [ ] **Build `agents/overview-page.md`.** There is no overview/design-consistency agent, which
      is why the drift keeps happening. Encode the CLAUDE.md rules and the clone-wayfinder rule.
- [ ] CSPO study (the command center is now built in real Scrum vocabulary as the practice tool)
- [ ] CV: decide the `$2 million` OER line (the real district figure is $36M, and neither number
      is hers to carry). Recommend cutting the number entirely.

---

> 🔴 **(older) Read `tools/NEXT.md` FIRST.**
>
> That file is the handoff: where we stopped, what to do next and in what order, the state of Dial Your Course, and the rules I keep breaking. It exists because the task list may not survive a session and the files do.
>
> **Two companion files, both required reading before touching the course tool:**
> - **`tools/NEXT.md`** · the handoff. Start here.
> - **`canvas/reference/CANVAS_OUTCOMES_EXPORT_BUG.md`** · why Canvas outcomes do not reach the `.imscc`. Source code read, cause identified, two tests queued. This blocks the alignment matrix.
>
> **First thing tomorrow, in order:** Mines OLED application (closes **15 July**). Then the two Canvas outcome tests, five minutes, they settle it. Then top nav on every subpage, then the assessment section.

> 🟢 **STARTUP · READ ME FIRST (Claude, every session, no excuses):**
> 1. **You are in Michelle's repo `singletrackmom.github.io`. This is home base.** Her `CLAUDE.md` (same folder) has who she is, the accuracy guardrails, and the full file map. Read `CLAUDE.md`, then finish reading THIS file. Do this before asking "what do you want to do."
> 2. **Do not act lost. Everything is written down.** Projects, notes, the ARC SSS study, the courses, the FEP, and the job + family agents are all mapped in `CLAUDE.md` and below. If you think you have no context, you skipped step 1.
> 3. **Where things live:** working docs are in THIS repo (root, plus `notes/`, `airc-sss/`, `stem-project/`, `render/`, `copamigo/`, `avc100/`, `fep/`, `cultivate/`). PRIVATE job + family material is OUTSIDE this repo at `~/Documents/Claude/JobSearch/` (resumes, dashboards) and `~/Documents/Claude/Scheduled/` (the daily agents). Scheduled is a protected folder and cannot be mounted, but you can still list and run those agents through the scheduled-tasks tools without it.
> 4. **This week's priorities are in the "THIS WEEK" block right below. Start there.**
> 5. **House rules before you touch anything:** show proposed changes before editing files; no em dashes; curly quotes only; solid palette colors, never gradients; Goal, Audience, Process labeled on everything.
> 6. **On startup, quietly check the agents.** The ~6 AM cron misses whenever the computer was off overnight (usual), so the daily family agents (Kevin, Jillian, Jasper, Devan) may be stale. Run any that missed and publish to their pages; do NOT make Michelle manage them (hands-off policy). Michelle's OWN job search is Tue + Fri only and she reviews and applies on her own block, so never auto-apply. If nothing is stale, say nothing.

> 🗺️ **DIRECTORY MAP (built from disk July 7, 2026, so Claude always knows where everything is and what to read).**
>
> **Repo root files:** `CLAUDE.md` (who Michelle is + guardrails), `TASKS.md` (this hub), `index.html` / `about.html` / `work.html` (the live portfolio site), `daily-focus.md` (auto-generated). Staged review drafts: `*.review.html`.
>
> **Project folders in this repo (open the file listed first):**
> - `airc-sss/`, ARC Domain 5 student-journey usability study. START at `airc-sss/WORKING-STATE.md`. This week: `meeting-agenda-2026-07-09.md`, form builder `build/build_tester_form.gs`, data `Maricopa_Scenario_Bank.xlsx`, `persona-library.html`, `run-sheet.html`.
> - `stem-project/`, Simulation-as-Assessment research (Mines). Private vault `_research-dossier.md`, process `data-science-sim-spec.md`, `mines-flagship-project.md`; public page `index.html`.
> - `render/`, Render career tool. Plans live in `notes/render/` (`AVC248_RENDER_MASTER_PLAN.md`, `RENDER_IDEAS.md`).
> - `copamigo/` + `copamigo2/`, CopaMigo student-services routing tool.
> - `cultivate/`, Cultivate PD hub; master CV at `cultivate/cv.html`.
> - `avc100/`, AVC 100 redesign + video scripts (`avc100/AVC100_All_Video_Scripts.md`).
> - `fep/`, Faculty Evaluation Plan. START at `fep/fep-2026.md`; rubric `fep/fep-guidance.md`.
> - `roughcut/` (newsletter), `tools/` (Course Auditor + Syllabus Checker), `learning-design/` (course-build case studies), `traveler/ murals/ internship/ gcc-cares/` (experiential-learning cards), `wayfinder/` (trip planner), `scrum/` (PSPO study, unlinked).
> - `command/`, self-PM Command Center. `command/index.html` = public projects dashboard (noindex, at /command; 8 ranked projects, North Star, now/next/later, roadmaps + metrics). `command/todo.html` = git-ignored LOCAL-ONLY to-do (this week + personal/family; NEVER publish). Rebuilt from THIS file on request or by the Sunday auto-refresh task.
> - Agent output pages (published BY the agents, do not hand-edit): `focus/` (Kevin), `flow/` (Jillian), `soar/` (Jasper), `summerwork/` + `devan/` (Devan), `jobs/` (Michelle, stealth/noindex). Camping: `frisco/ traillog/`.
> - `notes/`, all planning docs: `notes/render/`, `notes/portfolio/` (`PORTFOLIO_REDO_PLAN.md`, `SITE_MAP.md`, `mines-interview-strategy.md`), `notes/professional-development/instructional-design-study.md`, `notes/drafts/`, `notes/summer-production-schedule.md`.
>
> **PRIVATE, OUTSIDE this repo (never on the public site):**
> - `~/Documents/Claude/JobSearch/`, resumes, cover letters, `Michelle_job_dashboard.html`, tracker, per-company `<Company>_Application/` folders, `BULLETPROOF_FORMAT_SPEC.md`.
> - `~/Documents/Claude/Scheduled/`, the daily agents (PROTECTED, cannot be mounted, but reachable through the scheduled-tasks tools).
>
> **AGENTS · how to fire them up:** they run on a cron around 6 AM; if the computer was off they miss it, so Claude runs them when Michelle signs on. To run one: use the scheduled-tasks tools (list them, then read its `SKILL.md` at the printed path and execute it). Current agents and where they publish:
> - `daily-job-search` (Michelle, Tue + Fri) → `jobs/` + JobSearch dashboard.
> - `kevin-daily-job-search` (daily) → `focus/`.
> - `jillian-find-your-flow` (daily) → `flow/`.
> - `jasper-soar` (Mondays) → `soar/`.
> - `devan-daily-job-search` (daily) → drafts an email to Devan.
> - `daily-focus` (daily) → rebuilds `daily-focus.md` from this file.
> - `daily-portfolio-video` (daily) → morning briefing + 60-second video nudge.
> - Paused: `frisco-peak-one-watcher`, `yosemite-cancellation-watcher`, `devan-travel-dashboard-weekly`.

Last updated: July 10, 2026

> 🟢 **UPDATE (Fri July 10), job to apply AFTER EDUCAUSE (kept here so the daily rebuild does not lose it):**
> - **Western Veterinary Partners · Senior Director of Learning &amp; Development** (Denver, on-site/hybrid, $165K-$200K). Michelle flagged this to apply once the EDUCAUSE class is done. A flagged card is on `jobs/`, but the daily agent may drop a hand-added card, so it lives here too. Caveats: reach and off-lane (corporate L&amp;D at a vet-practice group, JD wants 10+ yrs organizational-development experience), and it is promoted via LinkedIn, NOT on WVP&rsquo;s own careers board, with JD text referencing a July 2025 window, so CONFIRM it is still live before applying. Positioning: lead with the campus LMS-team + district eLearning-advisory leadership, the ARC study, and Cultivate. Do NOT overclaim (never &ldquo;led the migration&rdquo;).

> 💵 **MONDAY (July 13), meet the financial people to file conference reimbursements. Bring these three:**
> - **EDUCAUSE Annual**, ALREADY PAID (~$889). File the reimbursement; bring the confirmation + itemized receipt.
> - **ASU conference**, NOT registered/paid yet. Register and pay first, THEN submit for reimbursement.
> - **Chandler-Gilbert conference**, NOT registered/paid yet. Register and pay first, THEN submit for reimbursement.
> - First nail down the ONE GCC reimbursement process (which form, whether pre-approval was required, the deadline, where receipts go) so all three go through the same path. While there, also batch the already-paid EDUCAUSE cohort course + League bootcamp.

> 🔴 **TOMORROW (Sat July 11), #1 PRIORITY: make the After Effects video.** Michelle forgot this and wants it first thing tomorrow. Scripts already exist in `avc100/AVC100_All_Video_Scripts.md` (the AE ones: Make It Move, Storyboard, Build). The class needs it. Claude can turn the script into a plain shot list / screen-record plan tonight so she just hits record tomorrow.

> 🟣 **CRITIQUE TOOLS, active build thread to resume (started late July 10).** Michelle shut down mid-build. Priority note: the After Effects video above is Saturday&rsquo;s stated #1; this critique-tools thread is what we pick back up after that (or whenever she says &ldquo;let&rsquo;s work on the critique tool&rdquo;). State to pick up:
> - **Goal:** help students give real, response-based critique, name what is working and what is not quite landing IN the design vocabulary, WITHOUT prescribing fixes. HARD RULE (Michelle): no &ldquo;move this here,&rdquo; no &ldquo;make it blue.&rdquo; A prescribed fix can be wrong and a student changes good work for the worse. Describe, don&rsquo;t prescribe; the maker solves it.
> - **BUILT today (NOT pushed yet, she publishes via the GitHub app):**
>   - `tools/design-principles.html`, reference page, 8 animated Principles of Design cards (contrast, hierarchy, alignment, proximity, repetition, white space, balance, emphasis), each a muddy-vs-clear example + a &ldquo;say what you see&rdquo; descriptive stem. Her design system, solid palette colors, no gradients, CSS-only animation.
>   - `tools/critique-helper.html`, current combined draft (three critique moves: What&rsquo;s working / What&rsquo;s not landing / Ask-don&rsquo;t-tell, plus the vocab). PLAN: rebuild THIS into an interactive drag-and-drop challenge.
> - **NEXT BUILD:** turn critique-helper into a drag-and-drop challenge (vanilla JS, no backend, palette). Round 1 &ldquo;Spot the critique&rdquo; = drag sample feedback lines into two bins, Describes (helpful) vs Prescribes/vague (skip). Round 2 &ldquo;Build a critique&rdquo; = drag a principle chip + a stance into a sentence frame, name the effect. BUILD ROUND 1 FIRST (it directly fixes the bad-advice problem). Link it to design-principles.html for vocab.
> - **Vocabulary architecture (decided):** Core = Principles of Design (loads every class) + per-class sets on top. First per-class set to build = the 12 Principles of Animation (can embed Alan Becker&rsquo;s videos); then branding vocab (AVC 183), imaging vocab (Photoshop). Populate via a start-of-unit activity where students build + define the terms, Michelle verifies, then it loads into the tool.
> - **Format decided:** animated web mini-explainers (Option B), NOT recorded video. Use real student examples only with permission (FERPA).
> - **Fits with:** the AVC 100 discussions redesign + AVC 183 critique workflow; also a portfolio piece next to the Course Auditor. Consider linking from Canvas/Discord and possibly a Work-page card later.
> 🟢 **UPDATE (Thu July 9), CTLE meeting outcome + CopaMigo path.**
> - **CTLE (Meghan) is fine posting the new Student Resources page.** Green light to publish it.
> - **CopaMigo does NOT go on that page yet.** It gets added only after a sanctioned pilot and testing. Keep the page CopaMigo-free until then.
> - **Meghan does not want Michelle to OWN the Student Resources page.** Open item: identify who owns and maintains it (CTLE or a student-services owner). Until an owner is named, the monthly link-check agent (below) reports to Michelle.
> - **BLOCKER for CopaMigo direction: waiting on the outcome of Gordon's (ARC) meeting with leadership about running pilots.** That decision gates where CopaMigo goes next. TO DO: follow up with Gordon for the leadership pilot decision, then decide CopaMigo's next step.
> - **NEW monthly agent (`student-resources-link-check`):** sweeps the Student Resources page (`copamigo2/student-resources.html`) about once a month and flags any broken or redirected links to Michelle (and the page owner once named).
> - **BOOKMARK / FUTURE FEATURE for CopaMigo, anonymous question + gap logging (Michelle asked for this, do not forget):** collect what students actually ask, where it routed, and the 👍/👎, so staff can see gaps and write the missing answers (the intake form is where they write them). Buildable in the prototype NOW via a Google Sheet + Apps Script (same pattern as Render and Rough Cut), no real backend needed; also the natural Stage 1 analytics feature (PRD R-12 / R-20). Stays anonymous, no PII, add a disclosure line. NOT built yet. When ready: Michelle creates the Sheet + Apps Script (Claude gives the script + click steps), sends the web-app URL, Claude wires it into `copamigo2/index.html` and connects the existing thumbs button. Also add it to the PRD + hosting plan as a feature.
> - **BOOKMARK (NOT TODAY), portfolio project backlog + sparse overviews:** Murals and Traveler overview pages are thin, and there are ~100 projects from 16 years that could join the portfolio. Michelle will dig up old project photos + write short descriptions when she has time (not today). Then bring those overviews up to the standard 4-section format (What it is / Who it&rsquo;s for / The goal / How it works). READY TO BUILD ON HER GO: AVC 100 overview enrichment + a linked class-outline page (source material exists in `avc100/`). PENDING her files: Design History page (needs her 2 student examples + link the assignment as the description). Confirmed: every project that has a PRD already links it.

> 🟢 **UPDATE (Wed July 8): today’s actions and open loops (captured so nothing is lost).**
> - **EDUCAUSE Annual: REGISTERED today** (Denver, Sept 29 to Oct 2, about $889 at the member rate with the extra 25% off). Save the confirmation email and itemized receipt to a folder. **Reimbursement is pending.** A one-time reminder is set for **Mon July 13, 9:30 AM** to (1) confirm the GCC reimbursement process (dean’s admin, division office, or Lori Walk: which form, was pre-approval required, deadline, where receipts go), then (2) batch-file EDUCAUSE Annual plus the already-paid EDUCAUSE cohort course and the League bootcamp together.
> - **EDUCAUSE cohort course: DUE Thu July 9, still not started. This is the #1 priority.** Reimbursement-critical (the certificate ties to the reimbursement). Paste an assignment into Cowork and finish it tonight or Thursday morning.
> - **Preconference microcredential: DECISION PENDING, not urgent (pricing holds to Sept 2).** Decide only after confirming GCC reimburses a preconference add-on ($589 full-day, $299 half-day). Best fits: **Designing AI-Scoreable Assessments** (afternoon half, feeds the simulation-as-assessment research), **From Panic to Practice** (morning half, faculty-development fuel for the COP), or **Lean Meets AI** (full day, AI-assistant build plus the UC San Diego network). Leaning toward the two half-days.
> - **COP kickoff: SENT.** A Google Form went out via its responder link (name, an availability grid for Mon Aug 17 and Thu Aug 20 from 3 to 5, plus Fri Aug 21 from 8 to 5, each time carrying an in-person vs virtual checkbox, plus an open question), and a Google group chat is started. Idea board is Google for now (revisit FigJam or Padlet only if the group asks). **NEXT:** pick the winning slot, get it onto the Week of Learning / accountability calendar, and invite others.
> - **Mines application (Online Learning Experience Designer, "OLED," closes July 15, gated by the domain).** New interview-prep research doc lives at `notes/portfolio/mines-online-interview-prep.md` (team, leadership, the Trefny tie, the OLED-vs-instructional-designer positioning). **HARD GUARDRAIL: on the Mines resume and cover letter, use "learning experience designer / learning designer," NEVER "instructional design."** When building the resume and cover letter, fold in EVERYTHING from that doc: the people to research and identify with, the Engineering Learning framework, and Trefny’s 2023 generative-AI classroom guidelines.
> - **Job agent tweak PENDING (not done yet):** add an **AI-enablement / AI-strategy lane** (NOT sales or revenue enablement), qualified leads only (a small stretch is ok), and **skip anything that requires a mandatory 5 or more years of formal product management**. Edtech-preferred but open, especially if online or Denver / Golden / Boulder hybrid, less so fully in person. Before editing `daily-job-search/SKILL.md`, pull the Jeffco job description to lift the real keyword set.
> - **Mines resume + cover letter: POLISHED today** (in `~/Documents/Claude/JobSearch/Mines_Application/`). Scrubbed every "instructional design" to "learning experience design / learning design" (Mines rejects the ID term), reworded the qualification lead-in off their verbatim phrasing, and sharpened the close to echo the OLED "both design and learning theory" distinction. Rebuilt docx + pdf, verified zero "instructional design" left. **OPEN:** resume builds to 4 pages (skills land on their own page after the forced page break); decide whether to tighten to 3 (do not relitigate the locked format without deciding this first).
> - **Website instructional-design scrub: DONE** on `index.html` and `about.html` (swapped to "learning experience design," which keeps ATS weight for other jobs). Degree line already correct ("master’s in Educational Technology").
> - **Course Auditor tool, BIG expansion idea (captured, not built):** grow the accessibility/objectives checker into a full course-polish tool. Alongside the WCAG and objective-alignment check, let me check off a COLOR PALETTE and TYPE preference and have it clean up the CSS so a course copied from Claude looks designed and consistent (mine look boring, no color), AND auto-name / suggest alt text for images missing it (do the fix, not just flag it). Overlaps with what Mines’ third-party tool (DesignPLUS / CidiLabs) does. Label Goal/Audience/Process when built.
> - **Learning list: take the free DesignPLUS / CidiLabs trainings on their site.** Mines uses this tool; good to speak it in the interview and it informs the Course Auditor idea.
> - **Practice-what-I-pitch (red flag to close):** make sure my own AVC courses visibly use the outcomes-first / Engineering-Learning model I claim. AVC 100 redesign already does; document it and align AVC 183 and 248. Do not interview or apply claiming a model my own courses do not show.
> - **Experiential-learning portfolio build-out (to-do, needs my materials):** the site shows only one mural, but there have been 100+ real student client projects since I started. Collect images, short project descriptions, and dates so we can build out that section.
> - **Simulation-as-assessment guardrails:** keep it TOPIC-AGNOSTIC until the research is done and I pick a subject; do NOT publish specific project ideas yet. The "SME is a Claude project" idea is promising but unproven with real learning designers, so treat it as an open question to test, not a selling point yet.
> - **Domain: DECIDED on `michelleblomberg.com`** (.com over .ai: professional, cheap ~$12/yr, trusted by higher-ed employers; .ai is ~$70 to $110/yr and reads gimmicky for a personal site). Availability looked open on a quick check, confirm at the registrar. NEXT (about 20 min, when EDUCAUSE gives a break): buy the name (Cloudflare or Namecheap), point DNS at GitHub Pages (apex A records to GitHub’s IPs plus a www CNAME to singletrackmom.github.io), add the custom domain in the repo Pages settings (writes a CNAME file), and enforce HTTPS. This gates sending the Mines application (Mines closes July 15).
> - **AVC 248 idea (capture, do not forget):** build AI mentors that talk with students in AVC 248, and have those AI mentors help each student find a real HUMAN mentor. AI as the bridge to human connection, not a replacement. Fits the Render capstone, the ASU Salik embedded-mentor model, and the "AI as scaffolding, not replacement" throughline. No student PII.
> - **AVC 100 discussions + Gemini Gem redesign (capture):** convert the three Industry Inspiration video "comment a paragraph" items into Canvas group discussions with Checkpoints (initial post + reply due dates), pods with rotating roles (Summarizer, Challenger, Connector, The Client, The Working Pro, Synthesizer), and a Gemini Gem as a side-coach a human posts from (labeled), NOT a vendor AI in the thread. The "true AI in the discussion" path (Packback / Harmonize LTIs, or an ASU-CreateAI-style governed platform) routes student data to a vendor, so it is an ARC / data-governance decision, not a fall-course build. Good COP + Mines-interview narrative: build data-sovereign, do not buy data-harvesting.
> - **Job note:** still very interested in Instructure / Canvas remote roles and other forward-thinking edtech doing embedded-AI work (already on the daily-job-search target list). Surface and flag any qualifying remote fits on the next Tue/Fri sweep. ADDED July 8: Instructure **Product Manager, Canvas** (US-remote, ~$130K, jobs.ashbyhq.com/instructure/ddffa558-ca81-4803-be30-fa61e5770038). REACH role, likely requires formal PM experience Michelle is honest about not having, so treat as networking/reach, not a straight apply.

> 🔵 **THIS WEEK (July 7), Michelle's active list:**
> **Day map:** Tue + Wed = EDUCAUSE (finish it, reimbursement-critical). Thu = ARC SSS meeting (2 PM Arizona) and EDUCAUSE due that night. Fri = TAXES. Build the tester form (steps below) sometime before Thursday. The AVC After Effects videos are the looming class item, parked below for right after this week.
> - [ ] **AVC After Effects videos, the class needs these built and Michelle is unsure how.** Scripts already exist at `avc100/AVC100_All_Video_Scripts.md` (the AE ones: Make It Move, Storyboard, Build). Claude can turn them into a plain step-by-step build plan or shot list, or simplify the assignment so it is fast to produce. NOT this week (EDUCAUSE + taxes own it); tackle right after.
> - [x] **DONE (July 10), EDUCAUSE instructional design class finished and submitted.** ✅ Final module (reflections + Community of Practice artifact) complete. 💰 STILL TO DO: file the reimbursement / turn in the certificate (the Mon July 13 reminder covers this) so the money is not left on the table.
> - [ ] **League for Innovation, MEETING NEXT WEEK: present your project.** Your AI Fellows project IS the ARC Domain 5 (Student Support &amp; Success) student-journey usability study across all 10 Maricopa colleges (see `airc-sss/WORKING-STATE.md`). You HAVE a real, documented project (crosswalk, live Jotform tester form, 3 personas, GCC Frustrations Survey), you just need talking points. Claude can draft a one-page meeting brief. Separately, finish the League bootcamp coursework (due Oct 1) for reimbursement, not urgent yet.
> - [ ] **GAIL exam, Michelle DOES want to take it** (already sat through the long class, so cash in the effort). Cert is not reimbursement-tied (the class was free), but she wants the credential. Next: confirm the real exam deadline + cost, then Claude builds a study guide + practice questions (same setup as the Scrum/PSPO guide). Lower priority than the League meeting prep.
> - [ ] **Email Marc (internship coordinator) about Beau&rsquo;s evaluation.**
> - [ ] **Read + revise the Simulation as Assessment research project** (the &ldquo;Current research&rdquo; card on `work.html`, page lives in `stem-project/`). Built quick-and-dirty for Claire; decide if it holds together and tighten it.
> - [ ] **Send the Mines resume + cover letter** (materials in `~/Documents/Claude/JobSearch/Mines_Application/`; Mines closes July 15). ⚠️ domain first.
> - [ ] **Get the domain** (buy + point DNS at GitHub Pages; gates the Mines send).

> 🟣 **ARC SSS TESTER FORM, BUILD IT BEFORE THURSDAY (July 9 meeting). Do it on your PERSONAL Google so Claude can read the results.** The code is verified and ready at `airc-sss/build/build_tester_form.gs` (10 campuses, 91 scenarios). Kindergarten steps:
> 1. Open the file `airc-sss/build/build_tester_form.gs` in your repo folder. Select ALL the text (Cmd+A) and copy it (Cmd+C).
> 2. In a browser go to **script.google.com**. Sign in with your PERSONAL Google (michelle.blomberg@gmail.com), NOT work.
> 3. Click **New project** (top left). A code box opens with a few sample lines.
> 4. Click inside that box, select all (Cmd+A), delete it, then PASTE your code (Cmd+V).
> 5. Click the **Save** icon (looks like a floppy disk).
> 6. At the top, make sure the little function dropdown says **buildTesterForm**, then click **Run** (the play arrow).
> 7. First time only: a permission box appears. Click **Review permissions**, choose your personal account, click **Advanced**, then **Go to (project name)**, then **Allow**. (Google warns because it is your own script; it is safe.)
> 8. At the bottom an **Execution log** appears with THREE links: FORM TO FILL OUT, FORM TO EDIT, RESPONSES SHEET. Copy all three.
> 9. **TEST IT:** open the FORM TO FILL OUT link, pick a college, run through it as a pretend tester, and hit Submit. Then open the RESPONSES SHEET link and confirm your test row landed. If it did, it works.
> 10. In the meeting, share the FORM TO FILL OUT link with the committee.
>
> **Paste your 3 links here when done (so we never lose them, and Claude can pull results next session):**
> - Form to fill out: 
> - Form to edit: 
> - Responses sheet: 

> 💵 **REIMBURSEMENT + CONFERENCE SIGN-UPS (money owed to you, do NOT leave it on the table). Sort the process this week.**
> **Find the ONE reimbursement path at GCC first, then use it for everything:**
> - [ ] **Ask your dean's admin assistant or the division office (or Lori Walk) how faculty professional-development / conference reimbursement works:** which form, whether pre-approval was required, the deadline, and where receipts go. This one answer unlocks all the items below.
> - [ ] **Gather every receipt/confirmation in one folder:** EDUCAUSE cohort course, League bootcamp, EDUCAUSE Annual registration, the Immersive & Experiential symposium (Aug 10 & 12), the Chandler-Gilbert conference, the ASU conference.
> **Then the individual to-dos:**
> - [ ] **EDUCAUSE:** submit the application/registration AND file the cohort-course reimbursement (the course is the reimbursement that ties to the certificate, so it is deadline-sensitive).
> - [ ] **Chandler-Gilbert conference:** submit the application/registration and log the cost to reimburse.
> - [ ] **ASU conference:** submit the application/registration and log the cost to reimburse.
> - [ ] **Already-paid items (EDUCAUSE course, League bootcamp):** file for reimbursement of what you already did, once you know the process.
> Rule: nothing gets reimbursed if it is never submitted. Do the "find the process" step first, then batch-file everything at once.

> 🔬 **SIMULATION AS ASSESSMENT, 2-week strategy (July 7-21). Page: `stem-project/`, card on `work.html`.**
> **Frame:** this is an ONGOING research thread, not a finished piece. Label it honestly as &ldquo;prototype in progress.&rdquo; It is a STEM-adjacent research interest for the portfolio, NOT a gate on the Mines application.
> - [ ] **Mines resume goes out regardless (by July 15).** Do NOT wait on this project to send. The research page can be live and honest about being early.
> - [ ] **Retire the FBD (free-body-diagram / &ldquo;Reading the Forces&rdquo;) as the centerpiece.** Freshman physics is the wrong level for Mines Online (100% graduate). Keep FBD only as a generic method example if useful. Reconcile `mines-flagship-project.md` with the page so they stop contradicting each other.
> - [ ] **Anchor any built demo to a dominant Mines Online grad program:** ETM decision simulation (the #17 marquee, adult-professional case style) or a Data Science scenario case. Pitch at grad/professional level.
> - [ ] **Phone call with Claire (PhD from Mines, friend) to pressure-test the concept BEFORE building.** She offered to talk by phone. Bring her: which subject skin (ETM vs. Data Science), whether the simulation-as-assessment idea reads as credible/new to Mines, and any SME gut-check on the scenario. Also a good chance to ask what a real Mines online course + MODL build looks like.
> - [ ] **IF (and only if) time allows after EDUCAUSE:** build ONE tight, grad-level micro-demo (one scenario, not four) + a 60-second video. Let the essay shrink to support the artifact, not stand in for it. Get a 20-min SME check before shipping.
> - [ ] **Do not let this cannibalize EDUCAUSE (due Thursday) or the Mines send.** This is second priority to both.

> 📍 **START HERE (morning): open THIS file.** It's the hub. Everything is either below, or linked here. All working docs live inside the GitHub repo (`Documents/GitHub/singletrackmom.github.io/`): quick tasks/schedule here in `TASKS.md`; long design docs in the `notes/` subfolder.
>
> **Project docs (the detailed plans):**
> - 🚀 **Mines flagship portfolio project**, "Reading the Forces" free-body-diagram assessment (the bulletproof build): `notes/portfolio/mines-flagship-project.md`
> - 🌙 Immersive / AI-simulation-for-assessment plan + lunar "Water from the Moon" + EDUCAUSE symposium prep: `notes/portfolio/immersive-ai-assessment-plan.md`
> - 🎬 Daily 60-sec portfolio videos: queue is below in the schedule (start with CopaMigo).
> - 🧩 Render + AVC 248 flagship: `notes/render/AVC248_RENDER_MASTER_PLAN.md`
> - 💼 Job search (private, separate folder): `~/Documents/Claude/JobSearch/`
>
> To point Claude in the morning, just say **"open TASKS.md / what's next"**, this index leads to the rest.

> 🗓️ **MONDAY (July 6) AGENDA, a build + strategy day (Michelle is also holding the Mines resume until Monday).**
> - **Branding simulation agent, build it out for real (big lift).** Turn the AI-simulated client in the branding course (the fictitious client students consult all semester for feedback) into a real, documented simulation-based assessment: scope outcomes to scenario to rubric, the agent behavior, and how students use it across the whole project. THEN figure out how to apply the same idea in the new **STEAMworks center** (the campus makerspace) as a hands-on, on-site version. This is the WGU-differentiator project; plan + background in `notes/portfolio/immersive-ai-assessment-plan.md`.
> - **CopaMigo, really fix / harden it.** Dial in the tool (running fix list is in the CopaMigo section below: course-advising bug, campus selector, admin dashboard, usability testing, verify modules). **Brand it as GCC now** (it was intentionally unbranded so it could serve any Maricopa college; switch to GCC branding). And **send questionnaires to the leaders of every Student Services department** to gather and verify their services, feeding both CopaMigo's routing content and the SSS study.
> - **Canvas student Help button, find out WHO OWNS it**, then get a meeting with that person or team to rework CopaMigo into the Help button (put the help where the student already is).
> - **Nudge the current-chatbot owner (again).** He never responded to the earlier meeting request; follow up so you can discuss CopaMigo vs. the existing chatbot and where it should live. (Claude can draft the follow-up email.)
> - **Send the Mines OLED resume + cover letter.** Materials ready in `~/Documents/Claude/JobSearch/Mines_Application/`; application review begins ~July 16, so Monday is fine. Final read, add phone if needed, upload on the Mines site.
>
> **▶ PRIORITY SEQUENCE (where to start so it is not overwhelming):**
> 1. **This weekend:** finish EDUCAUSE assignments + AVC 100 videos.
> 2. **Monday:** send Mines application; and KICK OFF the CopaMigo outreach that waits on other people, follow up with the chatbot owner, and email the Student Services dept leaders with the intake form. Start these early because they progress in the background.
> 3. **Main thrust, weeks of July:** AVC 248 + Render fully dialed = the FLAGSHIP, first priority. Deep-work blocks.
> 4. **Mid-to-late July (as responses land):** CopaMigo fixes + GCC re-brand + the Help-button integration.
> 5. **After the EDUCAUSE symposium (Aug 10 & 12):** build the branding simulation-agent prototype (target a demo ~4 weeks out); then adapt for STEAMworks.
> Rule of thumb: the flagship (AVC 248 + Render) is the priority; the CopaMigo track mostly runs on other people, so send those emails early and let them cook while you build.

> 💼 **JOB APPLICATIONS, prioritized list (Jul 6, 2026). Read this before sending anything; the sequence matters.**
> This updates the Monday-agenda Mines line above. Newest understanding: **Mines closes July 15**, and Michelle wants the **domain done before she applies**, so it is a tight sequence, in this order:
>
> 1. 🥇 **TOP PRIORITY, Mines application (Online Learning Experience Designer, Colorado School of Mines, Mines Online).** Golden, ~$90–100K. **Closes July 15.** This is the #1 focus. Materials are ready in `~/Documents/Claude/JobSearch/Mines_Application/` (resume + cover letter). ⚠️ **Do the domain FIRST (item 2), she does not want to send Mines until the site is on a custom URL.** Final read, add phone if needed, upload on the Mines site.
> 2. 🌐 **BUY A DOMAIN / CUSTOM URL and point the site to it, MUST be done BEFORE sending Mines (item 1).** Buy the domain, point DNS at GitHub Pages, confirm the site resolves on the custom URL. **This gates the Mines application, and Mines closes July 15, so clear it first.** (Cross-ref the weekend "buy the domain" + "point domain DNS at GitHub" notes in the schedule below.)
> 3. 🎯 **DECIDE WHETHER TO CHANGE THE PORTFOLIO**, the dual-audience "what I do, not who I do it for" reframe. Review drafts are staged locally (not pushed): `index.review.html`, `work.review.html`, `about.review.html`. **Decision still pending**, review the staged drafts and decide whether to publish the reframe or keep the current site. (Ideally settle this before/with the domain switch so the site launches the way she wants it.)
> 4. 🏛️ **Senior Service Designer (State of Colorado, Office of Information Technology / OIT), IN PROGRESS.** Remote-from-anywhere-in-Colorado, **$115K–$145K**, **closes July 27, 2026** (this is an EXTENDED / re-posted listing, they have struggled to fill it, which is positioning leverage). Tailored draft resume + cover letter, a copy of the full job description, and an interview-study-guide placeholder are all in `~/Documents/Claude/JobSearch/ColoradoOIT_ServiceDesigner_Application/`. **Drafts only, nothing submitted; for Michelle's review.** Angle: bridges service design + emerging tech + public-sector work, exactly what a hard-to-fill pod role rewards. Apply link: https://www.governmentjobs.com/careers/colorado/jobs/5356310/senior-service-designer-remote-from-anywhere-in-colorado
> 5. 🗂️ **APPLICATION-ORGANIZATION CONVENTION (keep using this).** One central home, one directory per application, so nothing scatters: **`~/Documents/Claude/JobSearch/<Employer>_Application/`** (the existing pattern, `Mines_Application`, `Jeffco_Application`, `WGU_Application`, and now `ColoradoOIT_ServiceDesigner_Application`; add the role when one employer has several). Each application directory holds: **(a)** the tailored resume (`Blomberg_Resume_<Role>.docx` + `.md`), **(b)** a copy of the full job description (`*_JD.md`), **(c)** the tailored cover letter, and **(d)** an interview-study-guide **placeholder** (`*_Interview_Study_Guide_PLACEHOLDER.md`), only filled in IF/when an interview is scheduled (model it on `Jeffco_Application/Jeffco_Interview_Study_Guide.html`). Build every resume from the LOCKED bulletproof format (`JobSearch/BULLETPROOF_FORMAT_SPEC.md` / the Guild-format generator). Note: this is the private `JobSearch/` home; the separate `Documents/Claude/Applications/` folder holds only the frozen master résumés, do not confuse the two.

## ☀️ SUMMER PRODUCTION SCHEDULE (now → Aug 15)
Fall starts ~Aug 17, so Aug 15 is the finish line. **Camping week (Jul 6–12): ≤2 hrs/day, async only. Last week of July (~Jul 27–31): VACATION, no work.** Confirm exact dates.

> ⏰ **HARD DEADLINE, register by JULY 8 (early-bird discount):**
> - [ ] **Immersive & Experiential Learning in Online Environments symposium** (Aug 10 & 12), https://events.educause.edu/symposiums/2026/immersive-and-experiential-learning-in-online-environments
> - [ ] **EDUCAUSE Annual 2026** (Denver, no travel cost), early-bird 25% off closes Jul 8, https://events.educause.edu/annual-conference
> - [ ] **Reimbursement:** file for the already-approved items I registered for (see reimbursement steps below).

> 🎬 **DAILY (start Sun Jul 5, not the 4th): record ONE ~60-second portfolio video.**
> Queue: 1) **CopaMigo** · 2) **UX student project** · 3) then other Work-page projects as short explainers (Cultivate, the agents, Rough Cut, etc.). **Skip Render for now, it needs major work first.** Claude can draft/tighten each day's ~60-sec script the night before.

- **This weekend (Jul 3–5):** finish EDUCAUSE assignments; start recording the short AVC 100 videos (scripts ready); final-read resume + add phone and **send to Marla**; **buy the domain**. (Accessibility is already on the About page. ✔)
- **Jul 6–12 (CAMPING, light):** send Mines app (Mon); email the chatbot owner + Student Services leaders (intake form); point domain DNS at GitHub; record 1–2 short AVC 100 videos/day.
- **Jul 13–19 (build):** AVC 248 assessment rework (spec below) + record its instructional videos; finish AVC 100 build videos; start AVC 183 rework.
- **Jul 20–26 (build):** Render dialed for the fall pilot (flagship); build/record AVC 183; record the AVC 100 "meet CopaMigo" video; CopaMigo fixes as responses land.
- **Jul 27–31:** VACATION (off).
- **Aug 1–8:** Render pilot-ready; AVC 248 fully assembled in Canvas; AVC 183 done; AVC 100 videos posted.
- **Aug 8–15:** EDUCAUSE Immersive symposium (Aug 10 & 12); final QA on all three courses; buffer.

**VIDEO CHECKLIST (every video to make):**
- AVC 100 (scripts in `avc100/AVC100_All_Video_Scripts.md`): Illustrator, Color Palette (~3m), Pen & Shape (~4m), Poster Plan/Develop/Finalize (~4/9/5m); Photoshop, Cut It Out (~4m), Postcard Plan/Build (~4/8m); After Effects, Make It Move (~4m), Storyboard/Build (~4/8m); **NEW: Getting Help / Student Success → intro CopaMigo** (see spec).
- AVC 248 (instructional): course + AI-literacy intro; Render intro; **NEW: "How to record a project walkthrough"**; **NEW: "Build your portfolio, pick a track"**; **NEW: "Register a domain, how + real cost."**
- AVC 183: videos TBD during the rework (branding-project intro, AI-simulated-client how-to, per-phase demos).

**AVC 248 ASSESSMENT REWORK (spec):** remove the single midterm + 3-min final presentation. Replace with (1) **three project-walkthrough videos** (each student walks one of their 3 best projects, explaining process/decisions, like Michelle's own portfolio), spaced across the term; (2) a **fully dialed portfolio** on a chosen track, GitHub Pages (free, template + light vibe-coding) / Behance / from-scratch / paid Squarespace-Wix; (3) a **domain lesson** (how to register + real cost ~$12–15/yr vs free GitHub; rationale: after graduation they may lose Adobe, so a pay-once URL or free host keeps work live). Touches (do as ONE consistent pass): `module-08/.../final-portfolio-presentation`, `module-03/.../midterm-portfolio-prep-plan`, `module-06/.../portfolio-check-in`, `course-schedule.html`, + new portfolio-tracks and domain-how-to pages. (Task #13.)

**AVC 100 "Getting Help / Student Success" video (spec):** short video that introduces campus supports **by introducing CopaMigo**, show the tool, tell students to play with it and **report what it did NOT answer** (fall students become CopaMigo user-testers). Buys time while the Canvas Help-button integration is worked out.

> 🟢 **UPDATE (Thu July 2, 2026), READ ME FIRST.**
> - **🔴 TODAY, #1: EDUCAUSE, 5 assignments DUE MIDNIGHT TONIGHT (July 2).** Push to finish them tonight. An extension email to the program is drafted as a backup, but assume the midnight deadline unless they grant more time.
> - **#2 today: AVC 100 videos** (the VP will review them, so they count).
> - **League for Innovation project EXTENDED to OCTOBER 1, 2026**, no longer urgent or overdue. Do it after EDUCAUSE; stop treating it as behind.
> - **Portfolio + LinkedIn refreshed and pushed:** `index.html`, `about.html`, and the LinkedIn About now lead with AI strategist / learning experience designer, adult learning, and simulation-as-assessment. Honest NEW line in both: "This fall I am building an AI-simulated client into my branding course ... my goal is to extend that toward immersive simulation in our new campus XR lab." Do NOT overstate it as already built.
> - **Files reorganized:** all working/planning/study docs now live under `notes/` (file map is in CLAUDE.md). Two study guides ready in `notes/professional-development/`: `instructional-design-study.md` and `immersive-ai-assessment-plan.md`.
> - **NEXT BIG BUILD (after EDUCAUSE): the AI-simulated-client simulation-as-assessment prototype** for the branding course, the WGU differentiator (plan in `notes/portfolio/immersive-ai-assessment-plan.md`). Prep for the EDUCAUSE Immersive & Experiential Learning symposium, Aug 10 & 12.
> - **Job-search agent fix PENDING:** it missed the local Mines OLED because Mines and the local colleges run Workday boards it cannot scrape, so it silently drops them. Paste the LOCAL-PRIORITY block into `Documents/Claude/Scheduled/daily-job-search/SKILL.md` and set a local no-commute salary floor (pick the number). Mines OLED (JR108710) review begins ~July 16; resume + cover letter drafted in `JobSearch/Mines_Application/`, on hold pending WGU.
> - **WGU:** screening interview done July 1; awaiting word on the next round.

> 🔴 **TODAY (Sat June 27), READ ME FIRST. Hard deadlines + a captured list so nothing slips.**
>
> 1. **FEP, SEND TODAY by 5:00 PM. Hard deadline, no more delay.** Master `fep/fep-2026.md` (read its Control Panel first), rubric `fep/fep-guidance.md`. This is the priority today. **Render is NOT a today task (Michelle's call), only capture the notes below.**
>
> 2. **📧 PILOT LETTER to Sonal AND Jordan, SEND MONDAY (June 29).** This is the one that cannot slip, or the Fall 2026 AVC 248 Render pilot has no path by the **Aug 15 semester start**. Merged, paste-ready draft already lives at `notes/render/AVC248_Jordan_Pilot_Email.md` (needs the $______ budget figure filled in + a final read in Michelle's voice; attach `AVC248_Claude_Pilot_Proposal.docx`). **THE ASK / LOGIC to make explicit in the letter:** we need a sanctioned pilot to run Render this fall. **If they will not pay for a Claude pilot, propose a GEMINI pilot instead.** Gemini is supposed to roll out to students in fall, but there is **no guarantee**; if it does not roll out, Michelle still needs an approved pilot (Claude or Gemini) to get Render running. Lock the path with Sonal and Jordan NOW, before Aug 15, or she is out of luck once the semester starts. (Render is already API-based and can point at Gemini's API; the take-with-you career agents are tool-agnostic `.md` files and already work in Gemini.)
>
> 3. **🛠️ RENDER, future features to CAPTURE (do NOT build today):**
>    - **Add Gemini as a future feature in the Render PRD** (`render/prd.html` plus the build-status block atop `render/index.html`): document that Render can run on Gemini's API / be made Gemini-compatible, so it works whichever AI the campus standardizes on.
>    - **NEW feature idea: end-of-semester skills-gap analysis to a learning plan.** Students input their resume + skills all semester (and Render saves jobs all semester; maybe they also build their own job-search agent). At the end, the AI runs a **skills-gap analysis** against the jobs they want, then **builds a personalized learning plan**, either AI-generated or by recommending **free Coursera or other courses** to fill each gap. ❓ **CHECK FIRST whether Render or the PRD already includes this** before building (Claude to verify in `render/` and the PRD next session).
>
> 4. **🎨 AVC 100, get it dialed (it is behind right now).** Specifically: **build a Photoshop lesson** and keep the class current. Not today (FEP comes first), but high priority this week.
>
> 5. **🔵 AFTER THE WGU INTERVIEW (July 1): build out LinkedIn properly (NOT before the interview).** Beef up the whole profile to match the WGU Future of Education Strategist / AI Innovator JD: (a) add REAL accomplishment bullets to every job, not just titles; (b) add a Projects/Featured section listing each project specifically WITH LINKS, Render, CopaMigo, the SSS district student-journey study, Cultivate, the AVC 100 data-informed redesign, and the portfolio site; (c) RESTORE the faculty-training items that were trimmed from the resume (maps to the JD's "develop and deliver training to educate faculty and staff on technologies, best practices, and ethical considerations", frame via the launching AI Community of Practice + CTLE sessions); (d) foreground **data-informed decision-making** (AVC 100 redesign grounded in retention research, measured by success-rate change + Canvas analytics) and **piloting/evaluating** new tech (the JD says "implement and evaluate pilots," not ship products). The aligned **About summary + headline** are already drafted and saved in `Documents/Claude/JobSearch/WGU_Application/` (paste-ready). Keep honesty guardrails: co-chair of the SSS DOMAIN only, CoP LAUNCHING, Render's FIRST pilot is Fall 2026, "eager to design within CBE" (not claiming CBE experience), no invented numbers.

> 🟢 **CURRENT STATE, READ ME FIRST (June 25, night).** The WGU application (Future of Education Strategist, AI Innovator) is DONE and SUBMITTED today; the finalized, reusable package is saved at `Documents/Claude/JobSearch/WGU_Application/` (see its `WGU_STATUS.md`). Jillian's flow is pushed and live. Focus now is COURSES + the FEP. This is more than one day of work; clear the courses and the time opens back up.
>
> 🔴 **FIRST THING: call the pharmacy to order/refill the prescription.** Quick, knock it out before the deep work.
>
> **PRIORITY ORDER FOR THE MORNING:**
> 1. **FEP, finish and SEND. Hard deadline.** Due to the VPAA by June 30 (GCC dynamic form); internal target out for signatures is basically now. Master file `fep/fep-2026.md` (read its Control Panel first), rubric `fep/fep-guidance.md`. The one with a real date and real stakes, so it leads. Claude can pull it most of the way with Michelle.
> 2. **EDUCAUSE course assignments, 6 days left and NOTHING turned in yet.** The course has ended; assignments are overdue. Highest-urgency coursework. Claude can help draft and organize what is due.
> 3. **League for Innovation course, catch up.** Behind; finish the cohort work (account mblomberf, league.org). Claude can map what is left.
> 4. **Update the AVC class, students have nothing to do right now.** Quick win: post a lesson/assignment so the class is current.
> 5. **Google GAIL exam, study and take it.** First confirm the real deadline from the voucher email in the gccaz inbox (the old June 22 date was never verified). Claude can build a tight study guide + practice questions.
> 6. **Scrum / PSPO I, never started.** The project-management cert referenced on the resume; ~2 weeks of light study, 80 questions / 85% to pass / $200, based on the ~20-page Scrum Guide. Claude can build a plan + practice tests.
> 7. **AIRC usability study, reorganize for distribution (half-day, high leverage).** Dial the capture format so each committee member can spend ~30 minutes and the study captures all of it, then send it out widely to keep gathering data; AI can run some of the testing too. Read `airc-sss/WORKING-STATE.md` first. Do this right after the courses clear.
>
> **Personal (Michelle's own, weighing on her):** pay bills, do taxes, start Mom's taxes. These do not need to fight the work items tomorrow; take the FEP first.
>
> ✅ **APPLIED June 26: Per Scholas, Director, AI Product Management** (remote, Colorado-eligible, $90,000-$95,000). Resume + cover letter sent (final files at `Documents/Claude/JobSearch/PerScholas_Application/_final/`). Do NOT resurface in the apply-now list.
>
> ⏰ **IF/WHEN PER SCHOLAS CALLS: learn Scrum Product Owner (PSPO I) BEFORE the interview.** The resume and cover letter both say PSPO I is "in progress," so it has to be real before any interview. ~2 weeks of light study off the ~20-page Scrum Guide; 80 questions, 85% to pass, $200. Michelle's standing note: "do not let me forget to learn Scrum Product Owner before I get called for an interview."
>
> 📚 **DAILY (one hour, evenings, may replace the AI book club reading): study for PSPO I.** Study guide is built and live at **singletrackmom.github.io/scrum/** (condensed Scrum Guide 2020 + Product Owner value focus), with two self-grading practice tests linked at the bottom. Routine: read one section a night, then take the linked tests, and retake until consistently 85% or higher. After that, do the free Scrum.org Scrum Open and Product Owner Open until 95%+, then book the $200 exam. Local files: `scrum/index.html`, `scrum/test-1.html`, `scrum/test-2.html` in this repo (noindex, unlinked).
>
> **📧 NEXT WEEK (deadline ~July 2), AFTER the current course/FEP work clears: send the Fall AI-pilot email to BOTH Sonal and Jordan.** One email to both describing the Fall 2026 AVC 248 AI pilot, what it is, what students will do, the no-PII / no-student-data design, and the access/cost ask. A MERGED, paste-ready draft addressed to BOTH already lives at `notes/render/AVC248_Jordan_Pilot_Email.md` (June 26, blends Michelle's warm "let's get on one page, recommend the path" opening with the structured privacy/access/ask details). It just needs the budget figure filled in (the $______ line) and a final read in Michelle's voice, then send from the gccaz email with `AVC248_Claude_Pilot_Proposal.docx` attached. It already addresses Sonal's data-privacy concern head-on (no-PII by design, FERPA-safe) and notes the career agents are tool-agnostic and already work in Gemini and ChatGPT.
>
> **Standing morning check:** if the computer was off at ~6 AM, the daily agents did not run, run them if needed (Jillian's is already pushed). Michelle's own job search is twice-weekly (Tue + Fri), not daily.

> 🔴 **TOMORROW, FIRST THING (June 22): decide the Render / Claude access question, then circle back to the Jordan email. (Parked here at Michelle's request, do NOT spiral on it tonight.)**
> - **Claude access, the simple answer:** Claude for Education has not answered our calls or emails. The easy fallback is totally fine, just **buy each student a $20 Claude account** (about $480/month for ~24 students) and move on. This is NOT hard and is the likely plan. (Pooled API / reassignable seats were options for efficiency, but paying per student for a small pilot is a perfectly normal, simple choice, do not overthink it.)
> - **The Gemini question (Sonal context):** Sonal is not excited about Claude and is pushing students onto **Gemini**. Two real, low-stress options to talk through: (1) the take-with-you career **agents are already tool-agnostic plain-text `.md` files, so they ALREADY work in Gemini** (and ChatGPT, etc.), no rebuild needed; (2) **Render** itself just calls an AI API, so it could be pointed at **Gemini's API** or adapted to work in Gemini if the campus standardizes there. Decision to make: keep Render on Claude or make it Gemini-compatible. THINK ABOUT THIS TOMORROW.
> - **Jordan email:** reformat `notes/render/AVC248_Jordan_Pilot_Email.md` into a clean, paste-ready version that does NOT look like a Markdown file (drop the ##, **, and - symbols), or a Word doc, before sending. Send it after settling the access + Gemini question above.
>
> 🟢 **CURRENT STATE, READ ME FIRST (June 20).** If you are a fresh session or Michelle returning, this is where we are.
>
> **PRIORITY ORDER right now:**
> 1. **AVC 100 grading** (number one, every day).
> 2. **FEP, SUPER HIGH PRIORITY (just under grading).** Due June 30, 2026 via the GCC dynamic form (employees.gccaz.edu/faculty-evaluation-plan); internal target out for signatures by ~June 25.
> 3. League for Innovation bootcamp + EDUCAUSE coursework (mornings).
> 4. Everything else: own job search Tue + Fri (3 to 5 PM block), family agents run automatically.
>
> **FEP STATUS (in good shape, master file = `fep/fep-2026.md`, read its Control Panel first).** Companion files: rubric `fep/fep-guidance.md`, evaluations `fep/fep-evaluations.html`. Built today: a full reflective draft across all 3 Required + 2 Elective areas with REAL teaching foregrounded and the AI prototypes as supporting evidence; The Traveler (advisor, CMA Pinnacle winner); Rough Cut + the AI-built distribution spreadsheet; Internship Coordinator; the new UX course (in the curriculum-committee approval process); the stackable Animation/DMA certificates; the AVC 100 redesign; 27 calendar PD items in the appendix; a personal-reflection draft atop the appendix; Category 1 (official evals: AVC 297AC + AVC 181 shown clean) and Category 2 (Michelle's own surveys, with a combined bar visual and pulled comments, AVC 182's 2020 responses excluded). Purdue Prompt Engineering fixed to 2025. Team: **Casey Farina = faculty peer; the chair can be the third person (no fourth needed); students = the surveys.**
>
> **FEP STILL NEEDS MICHELLE:** name the third team member (chair is fine); the exact "For Academic Year" value; the GAIL exam status; decide whether to add the Career-ILO/Render related area; **SEND the Rough Cut newsletter before submitting** (completed deliverable); finish the reflection in her own voice; and the call on whether to include AVC 248 in the official-eval showcase (left off for now due to one harsh outlier, her call).
>
> **INDEX PAGE (homepage) QA done (typography + palette clean). Needs Michelle's decision:** (a) broken internal link `/canvas/avc297/` (no such folder), fix or repoint; (b) a student name is spelled two ways, "Madisen Whorle" (Traveler card) vs "Madisen Wohrle" (internship card), which is correct?; (c) a few cards lack labeled Goal/Audience/Process (The Traveler, Murals & On-Campus Client Projects, the two Sommarverken cards, the AVC Course Portfolio tile); (d) optional: fold the Canvas-green and gold color subsystems into the palette.
>
> **AUTONOMOUS WORK done while Michelle was out (June 20):**
> - **FEP polish:** Purdue fixed to 2025, AVC 100 tense fixed (it has launched and is running its first session), personal-reflection draft added atop the appendix (for Michelle to revise in her voice), typography cleaned. Both file copies in sync.
> - **Index page:** typography + palette QA done. Open decisions for Michelle: broken link `/canvas/avc297/`; the "Madisen Whorle" vs "Madisen Wohrle" spelling; a few cards missing labeled Goal/Audience/Process; optional palette folding of the Canvas-green/gold subsystems.
> - **UX study (`airc-sss/`):** made cohesive and consistent. Relabeled the run-sheet task groups from "Phase 0 to 5" to "Stage A to F" so they stop colliding with the project's Pilot/Phase 1-3 timeline; fixed the ux-study lede endpoint to "the goal they came for"; removed the disliked "nothing in production" phrasing from the fieldwork footer; confirmed Jax, the Pilot rename, the AI disclosure, and ARC naming are consistent everywhere. Flag: the site runs a Phase timeline AND an Initiative 1/2/3 framing in parallel (coherent, but could be unified someday).
> - **Anthropic resume + cover letter REFRESHED** as NEW dated files in `Documents/Claude/Applications/`: `Blomberg_Resume_Anthropic_2026-06-20.docx/.pdf` (clean 3 pages) and `Blomberg_CoverLetter_Anthropic_2026-06-20.docx/.pdf`. The frozen `2026-06` originals were NOT overwritten. Added (true) Internship Coordinator, The Traveler (CMA Pinnacle winner), the stackable certificate, and strong student-eval results; kept all locked formatting and guardrails (LMS wording, more-than-two-decades, requirements-match block).
>
> 🔖 **WHERE WE LEFT OFF (June 20):** Long session with Claude (Michelle should be on her FEP, not more job/plan tweaking, so this is parked here). Done today: SSS case study polished (renamed "Phase 0" to "Pilot" so the small "0" stops reading as an "o"; added an AI-authored disclosure that an AI agent ran the pilot and drafted most of the writing and findings are preliminary pending human verification; reframed endpoint from "graduation" to "the goal they came for"; added the usage-baseline + year-later impact-evaluation as Phase 1; renamed persona Alex to Jax, nonbinary; attributed and linked CopaMigo). CopaMigo PRD: simplified the R-23/accessibility callout (it is the WCAG 2.1 AA / ADA Title II rule, deadline extended a year to April 2027/2028) and added a note that branding follows whichever college it serves (intentionally unbranded on the personal site). CopaMigo tool: stripped all specific years from the financial-aid content. Job agent: added an AI-ENABLEMENT title lane (coach, not trainer), capped at up to 40 matches / 3-star-and-above, and re-ran it (26 live roles, 1 new: Intuit Principal L&D Technologist, AI Enablement). Portfolio index: split the Campground Watcher into its own card, aligned the SSS card and fixed "AI Resource Center" to "AI committee (the ARC)." Soar: shrank internships to a small Summer-2027 watch. Jillian: new Vol. 5 modeling deck with real model photos.
>
> 📸 **PORTFOLIO VISUAL POLISH (new, do in a focused session, NOT during FEP time):**
> - Add screenshots or relevant images to nearly every portfolio card. The agents are already branded and the Wayfinder trip page looks great; capture clean screens of every tool that looks good and place them on the cards.
> - **Devan travel page map, fix big time.** Replace the "blob" map with a REAL map base (Leaflet + OpenStreetMap tiles, or a clean static map image) and overlay the numbered dots on top of it, so it is an actual map, not a shapeless blob.
> - **Traveler (Devan):** a documentary is coming, use that as the image on that page.
> - **Render:** add the conference-presentation VIDEO once it is finished. DO THIS BEFORE END OF SUMMER.
> - Rebalance the front page: less text, more images (it is text-heavy right now).
> - **Teaching portfolio card ("AVC Course Portfolio"):** decide whether to trim hard or temporarily remove until the courses are dialed, so it does not distract from the AI work. Leaning toward removing/trimming. (Less is more.)
> - **🆕 ADD WIREFRAMES / FIGMA (or FigJam) ARTIFACTS TO THE PORTFOLIO (for the Senior Product Designer / CodePath applications).** Recruiters need to SEE design-process artifacts, not just read "Figma" on the resume. The CodePath JD explicitly wants "a portfolio that shows your thinking on flows and structure and the process behind your work." Add real wireframes, user flows, or a FigJam journey map to a few projects and embed/screenshot them on the cards or case study, with a link to the Figma/FigJam file: **Render** (a flow or wireframe of the Learner Hub, plus an IA/navigation sketch), the **AIRC student-journey UX study** (a natural FigJam service-crosswalk / journey map with the 3 personas), and **CopaMigo** (the routing-and-handoff flow). NOT today, but do this BEFORE submitting any product-design applications, since "I know Figma" without artifacts will not pass a design screen.
> - Use this portfolio work as evidence in the FEP.
>
> 🌟 **PORTFOLIO NORTH STAR (where this is going, look back in ~1 year):** Nothing is built for this yet and it is not a today task, but this is the target the portfolio is moving toward. The standard to hire against: PROVE you build and ship, do not just describe building.
> - **What Anthropic and Instructure-tier targets look for:** proof you build and ship, not descriptions of building. For Anthropic specifically: a live thing they can click, a two or three sentence "problem → what I made → what I learned," and a responsible/thoughtful tone. A 60-second video or a clean screenshot beats three paragraphs every time. For Instructure and edtech: the actual product UI, real users, and one honest outcome line. The common thread is *what is it, who's it for, can I try it, did it work*, answered visually and fast.
> - **The one-year version of this portfolio:** here are all my finished projects; here is a short video presentation about every single one; here is the whitepaper; here is the case study. Each project: live link + a 60-second video walkthrough + the problem/made/learned line + an honest outcome. Curated to the strongest work, image-first, fast to skim.
>
> 🏆 **FEP SHOWCASES = AVC 248 and AVC 100 (this week, see `notes/render/AVC248_RENDER_MASTER_PLAN.md`).** Both must be in the FEP and on the main portfolio index (`index.html`). **AVC 248** = the AI/PLE capstone (Render + student career agents). **AVC 100** = the retention redesign: it is the program's foundation course everyone in digital media takes and historically the lowest-success one; redesign it with student support + connection to retain students and MARKET the programs (an easy-win final project they are proud of, intros to full-time faculty and directors, where to get help, one 3-minute student-success video per module, "software is not that hard" message). AVC 183 (graphic-design-history project) and the UX course (in progress, not yet approved) are secondary showcases.
> - [ ] **THIS WEEK, before the FEP claims it done: SUBMIT the Animation + DMA stackable microcredential certificate requests.** The FEP should not say "done" until these are actually filed. Do it this week.
> - [ ] **THIS WEEK: SEND Rough Cut** <!--ROUGHCUT-THISWEEK--> the newsletter is a freshly completed, shipped deliverable and FEP evidence (Service to the Community + the AI-built distribution spreadsheet under New Skills). Send it before the FEP goes out.
>
> - [ ] **FEP Governance section, reframe official vs service (tomorrow).** Clearly distinguish the OFFICIAL, contract-required committees, which are **eCourses and OER**, from SERVICE / additional / extra work. Say plainly that Michelle contributed to BOTH of her official committees (these are part of the faculty contract). Label the rest, the ARC district committee, Basic Needs, the Faculty AI Community of Practice, the AI Advisory proposal, QM/OSCQR review, PARC, the curriculum/UX-course work, and Rough Cut, as **service or extra work**, not as "official committees."
> - [ ] **Decide whether to link a portfolio in the FEP (tomorrow).** If yes, link the CURATED portfolio site (`singletrackmom.github.io`), NOT the raw GitHub repo, so reviewers see the polished projects (Render, CopaMigo, Cultivate, the courses) and not internal files (TASKS.md, the FEP, the job-search and family-agent pages). The job-search / family material is not featured on the public portfolio index, so it stays out of view.
> 📎 **FEP EVIDENCE LIBRARY (locations, so nothing is lost).**
> - **DMA high-school-audience brochure (summer build):** working Google Doc https://docs.google.com/document/d/1earN3VzOF2kbnIgrd6mTnOjSRqxanogKJLNRAfcMukQ/edit . Collaborating with **Jeannie, Casey, Stephanie** on the text. This is FEP evidence (Program Development + Service to feeder schools).
> - **AVC 248 SP2026 student final portfolios (link the BEST on the FEP; full list kept here).** On the FEP now (curated picks, swap freely): Barsalou, Vera, Magee, Tukey, + Gutierrez Moreno (ASU transfer). Full list:
>   - Safia Al-Akoum, illustration/graphic design + animation backgrounds: https://www.youtube.com/watch?v=P9hgxrE9mAM
>   - Alexis Barsalou, animation + game (6 min): https://www.youtube.com/watch?v=dy0sGCGCPLk
>   - Lilyana Vera, animation/illustration/characters/concept art: https://www.youtube.com/watch?v=ccUepV19qG8
>   - Remini Kinman, social-media graphics, behavioral brands/gamers: https://www.youtube.com/watch?v=O7y0VB2T4sY
>   - McKaylyn Poppen, organized by software, no animation but good: https://www.youtube.com/watch?v=OTA8KGA1gzo
>   - Gigi Magee, branding/design: https://www.youtube.com/watch?v=2IqlYgSj85Y
>   - Janna Munoz, animation character design: https://youtu.be/GOZXBkqIZqc
>   - Michalea Freeman, graphic design: https://youtu.be/i-MVJchESwQ
>   - Jimena Gutierrez Moreno, sculpture, transferred to ASU: https://www.youtube.com/watch?v=8lkXwTjqyHQ
>   - Jasmin Verdugo Romero, 2d/3d animation, illustration, characters, VFX: https://youtu.be/N_ZNicCc7kM
>   - Beau Tukey, graphic designer + 3D modeler: https://www.youtube.com/watch?v=JfsxXLIgLVs
>   - Colette Donner, graphic + character design: https://www.youtube.com/watch?v=8b8VhmUv3g8
> - [ ] **UX course: follow up on the approval process** (what exactly is needed to push it through curriculum committee). Until approved, keep FEP language as "in progress."
> - [ ] Record one 3-minute student-success video per AVC 100 module (faculty/director intros, where to get help, the easy-win project).
>
> 🚀 **AVC 248 + RENDER = AI-POWERED CAPSTONE / PLE (big new build, full detail in `notes/render/AVC248_RENDER_MASTER_PLAN.md`).** Turning AVC 248 into a personal learning environment: an AI-literacy unit up front (Anthropic Academy model), Render all semester, and a capstone **Module 9** where every student builds their own portable career agent `.md` (works in any AI tool, even ChatGPT). DONE: Module 9 built; course front-page AI sell; formal CIO pilot proposal `AVC248_Claude_Pilot_Proposal.docx`. NEXT: (1) send the pilot proposal to CIO **Jordan**, follow up on approval + budget + whether Maricopa can get **Claude for Education** (Sonal cares about privacy, by design NO student PII enters AI); (2) build the AI-literacy starter unit; (3) add a guided goals questionnaire + resume-polish help to Render; (4) rebalance the 15-week schedule, CUT the business-dining-etiquette item (it is in Canvas, not the repo; keep netiquette) and give agent-building ~2 weeks; (5) weekly slide decks; (6) after the Fall 2026 test, show the **NAU connectivism professor** and submit to an early-2027 AI/edtech CFP (EDUCAUSE closed; check OLC Innovate, ASU+GSV, Magna "AI in Education"). Access/cost: pool tokens via a pay-as-you-go **API key** for Render; student accounts via **Claude for Education** or reassignable **Team** seats, NOT 24 individual subscriptions.
>
> 🛠️ **FINISH BUILDING OUT RENDER (before the Fall pilot).** Wire up and SHOW the agents and the new features so the tool demos cleanly: the **Career Agent `.md` export** (currently template-based, decide whether to make it a live Claude call), the **guided goals builder**, the **three example personas (Maya / Riley / Nina)**, resume-tailoring help, and the reach-job anchor flowing through every module. Reconcile the two Render copies (`/render/` public vs `canvas/avc248/render/` course app) into one source of truth. **KEEP THE PRD UP TO DATE** with each feature, both `/render/prd.html` and the build-status comment block atop `render/index.html`.
>
> 🧭 **AI PROJECT PRIORITIES (what to build between grading, job apps, and committee work):**
> 1. **Render + CopaMigo to bulletproof by END OF SUMMER.** These are the two that have to actually work: Render for the Fall 2026 AVC 248 pilot, CopaMigo for the bot-replacement pitch with Genesis and Eric Pawelski. This is the top AI-build priority.
> 2. **Personal project agents already work (Wayfinder, the family agents).** Leave them running; just link them as working things, with optional short videos later. Do NOT keep iterating them (hands-off policy). They are portfolio evidence as-is.
> 3. **SSS UX study is long-term (could run for years).** Do a video about the UX study ONCE it is far enough along to show where the AI-tool opportunities are. Not now.
> - **Ordering against the real job:** teaching and grading come first; job applications on the Tue + Fri 3 to 5 PM block; AI-build time (Render/CopaMigo hardening) in focused summer blocks, not daily. No daily pressure.
>
> 👀 **LOOK AT EXAMPLE PORTFOLIOS (when there is time, tomorrow or later, not urgent):** browse the curated list at github.com/emmabostian/developer-portfolios (dozens of developer and developer-advocate portfolios) to see the build-and-ship, case-study, live-demo style to model: big hero, one image per project, a tight problem/built/outcome blurb, a live link. Claude offered to curate 4 standouts from that list (plus any Anthropic or Instructure people) with notes on what to steal from each, ask Claude to pull those when ready.
>
> 📋 **FEP near-term (June 20 notes):** FEP team so far: **Casey Farina = faculty peer**; third person still TBD (Michelle's choice from chair/admin/another faculty/staff developer/advisory/alumni, the chair signs as chair regardless, so the third person can be someone else). Genesis's last name is **Toole**. **SEND THE ROUGH CUT NEWSLETTER before submitting the FEP** so there is a freshly completed deliverable to point to; Rough Cut plus its AI-built distribution spreadsheet should be an FEP highlight. The FEP must center the REAL teaching job (AVC courses, course design, assessment, committees, the UX course going to the curriculum committee), with the AI prototypes as supporting evidence, not the main subject.
>
> 🔖 **WHERE WE LEFT OFF (June 19):** Michelle reset the weekend. She leaves for camping Sunday, so the whole weekend goes to the two things she CANNOT do from camp and is nearly finished with: the **League for Innovation fellowship** and the **EDUCAUSE cohort course** (both paid for, both barely started, EDUCAUSE due before Tue June 23). **AVC100 is number one every day** and **FEP first draft** are the two she CAN work from camp, so they continue but don't eat the weekend. At camp she wants ONLY AVC100 + FEP, no League/EDUCAUSE distraction. Off her plate: **van tires moved to Saturday, Kevin is taking it in.** **GAIL exam: do NOT treat Monday as a hard wall yet**, the June 22 date is only from Michelle's own notes citing the NAAIC confirmation email, not independently verified; confirm the real date from the voucher email in the gccaz inbox before scheduling around it.
>
> 🔖 **WHERE WE LEFT OFF (June 17):** Reprioritized. (1) **Declined the GCC Dean (Short-Term) role** after reading how the salary scale actually worked: she would have netted almost nothing, would report to a VP she does not want to work with, and would be required on campus 5 days a week. Application pulled, not submitting. (2) **Noodle PM application still not submitted, doing it TODAY** (top priority). (3) Top three today: **FEP (start, not begun yet; real deadline ~June 25 because it needs multiple sign-offs before the dean gets it by June 30), Noodle, laundry put away.** (4) Added a stack of personal/bills items (dental insurance fight over Jasper's wisdom teeth, health insurance on Devan's collections bill, the rest of the bill stack, household-expense recalc for August when Devan moves out). (5) Van: needs solar measurements (ladder problem to solve), a tire/alignment check before Sunday's camping trip, and a wash/wax/conditioner pass Fri–Sat. (6) House must be clean (windows, bathrooms) before the renter moves in by July 1. (7) Long list: start AVC181 + AVC248 for fall now, do not wait. (8) Booked rest: **two full weeks of nothing at end of July.** See the TODAY block below.

> 🔖 **WHERE WE LEFT OFF (June 15 night):** Big session with Claude. (1) Job search: rebuilt and VERIFIED the dashboard against companies' own job boards (most old listings were stale; 11 confirmed live), and rewired the daily search to sweep many official ATS boards, verify every posting is live, drop technical/engineering PM roles, and write a static no-JavaScript dashboard. (2) GCC Dean (Short-Term) application: built a full CV and cover letter, DUE Tue June 16 (no location shown so they don't see she is out of state, no em dashes, supervisory and faculty-evaluation work featured, the $100K grant line removed). (3) Noodle PM application queued for tomorrow. (4) Camping: started a Grand Mesa 5-day itinerary (research parked in `Documents/Claude/Camping/`). (5) Reorganized everything off the Desktop into `Documents/Claude/` (JobSearch, Applications, Camping) and updated all task paths. (6) A one-time 7:00 AM task "morning-coffee-run" will greet Michelle and run the job search plus morning priorities when she next signs on. See the ordered TOMORROW MORNING block below.

> 🔖 **WHERE WE LEFT OFF (June 13–14 night):** Big website pass on the SSS work. Built the
> `airc-sss/` section: hub + four initiative pages (1 Map & baseline, 2 UX Study, 3 Why students
> don't persist, 4 Recommendations & pilots), all sharing `airc-sss/sss.css`. Built the executive
> deck `airc-sss/The_Persistence_Imperative.pptx` and the web version `airc-sss/faculty-briefing.html`
> (linked from the homepage). Did a full stealth sweep (removed all job-search / EdTech-PM-transition
> / sabbatical content; sabbatical.html and edtech-day.html deleted). Standardized page widths to
> 1080px and added a "← Home" eyebrow to every page. Ran a typographic sweep (curly quotes, no em
> dashes, no straight/inch/foot marks), this is now a hard rule in CLAUDE.md. **Next up:** unify the
> heading/type system across older sections (Cultivate, Render, CopaMigo, Canvas) so they match the
> SSS pages, see the "Website" task below. Everything was committed-ready; confirm it's pushed.


> ⭐ **RESUMING THE AIRC SSS UX STUDY? Read `airc-sss/WORKING-STATE.md` FIRST.** Every deliverable (plan, study kit, dashboard, live Jotform form), the scope, decisions, and open items live there. Public dashboard: `airc-sss/index.html`. Live tester form: https://form.jotform.com/261635441630048

This file is the source of truth and Claude reads it first every session. The old May
launch-week content has been folded in and re-dated. Yosemite (past) removed. Nothing here
is assumed "done" unless it says so, adjust as needed.

## ⚙️ START HERE: run the agents first, then this file is the map

**FIRST QUESTION EVERY MORNING: did the agents run (was the computer on at ~6 AM)?** The five daily agents + daily-focus are scheduled for ~6 AM, but Michelle turns her computer OFF overnight, so if the machine was off/asleep they DID NOT RUN. If they didn't run, run them live before anything else, then come back here for priorities.

**Where the agents live:** all are scheduled tasks at `Documents/Claude/Scheduled/<name>/SKILL.md`. To run one live, read its SKILL.md and execute it. The five daily job/career agents:
- **Michelle (job search)**, `daily-job-search` → tracker + dashboard `Documents/Claude/JobSearch/Michelle_job_dashboard.html` and phone view `jobs/` in this repo
- **Kevin**, `kevin-daily-job-search` → drafts an email to Kevin (Berg Berg Photography)
- **Devan**, `devan-daily-job-search` → drafts an email to Devan (seasonal/part-time near Golden, CO)
- **Jillian**, `jillian-find-your-flow` → publishes a new volume to `flow/` in this repo
- **Jasper**, `jasper-soar` → publishes the aerospace dashboard to `soar/` in this repo
- Plus `daily-focus` → rebuilds `daily-focus.md` from THIS file.

**Where everything else lives:** all project work is in the GitHub folder (this repo, `singletrackmom.github.io`). The agents and their SKILL.md files, plus JobSearch / Applications / Camping, live under `Documents/Claude/`. This TASKS.md is the map that points to all of it.

**Order each morning:** (1) run the agents above if the computer was off when they were scheduled, (2) read this TASKS.md + daily-focus.md for priorities, (3) work the priorities.

## How Michelle works (to-do list, NOT calendar blocking)

This file IS the to-do list and it's the home for all work. Michelle reorders priorities
herself and chunks big items across days. Claude keeps the list current.

**The calendar is ONLY for real meetings**, things with other people and fixed times.
Claude does NOT block out work time on the calendar anymore. Don't add work blocks; add
items here instead.

When Claude IS asked to schedule an actual meeting:

- **Location / time zones:** Michelle is in Colorado (Mountain time). Campus is Arizona
  time, which in summer is ONE HOUR BEHIND her (AZ doesn't observe DST). Watch this when
  scheduling anything tied to campus or AZ people.
- **Summer campus hours:** 7:00 AM–6:00 PM Mon–Thu (Arizona time). Nobody is on campus
  Friday. On-campus requirement is 2 days / 12 hrs; she usually does 3 days / 18 hrs but can
  bunch them Tue–Thu and be gone Friday through Monday (good for weekend van trips).
- Workout 8:00–9:30 every morning. Nothing work-related starts before 9:30. Yoga mornings
  (often run to ~10:30–10:45) push the work start later still.
- Morning is peak deep-work time, protect the first long block for the hardest task.
- Check the **shechelleb@gmail.com** calendar, it overlays all the others
  (micag04441@gccaz.edu work, michelle.blomberg@gmail, bergbergphotography). Do NOT
  double-book against any of them.
- EXCEPTION: bergbergphotography events CAN be overlapped, UNLESS it's a wedding or a
  wedding show, those are mandatory, treat as hard blocks.
- Moving/changing any meeting that has other attendees notifies all of them, get explicit
  OK first.
- Colors: red = joint with Kevin, blue = Claude work blocks.

---

## ⭐ Current priorities (June 13 brain dump)

### ▶ TODAY (Fri June 19) + weekend before camping

**⭐ PRIORITY ORDER THIS WEEKEND (June 19, Michelle's reset). She leaves for camping Sunday, so the weekend goes to what can't travel:**
1. **League for Innovation fellowship, catch up / finish.** Near the end, paid for, barely touched. Cannot do from camp. (League account: mblomberf, league.org.)
2. **EDUCAUSE cohort course, finish the whole thing.** Almost done, paid for, due before Tue June 23 while camping. Cannot do from camp.
3. **AVC100, number one, every day.** Post lesson, grade, keep current. CAN work from camp.
4. **FEP, first draft.** Open `fep/fep-2026.md`, get a first pass down. CAN work from camp.
- **At camp: ONLY AVC100 + FEP. No League / EDUCAUSE there, finish those before Sunday.**
- **Van tires + alignment → Saturday, Kevin is taking it in.** Off Michelle's plate.
- **GAIL exam → verify the real deadline first.** June 22 is only from Michelle's notes (citing the NAAIC confirmation email), not independently confirmed. Find the voucher email (Fast Lane / na_operations@fastlane.net or Google Skills / noreply@skills.google) in the gccaz inbox and read the actual date before treating Monday as a wall. Not a weekend item.

**Added June 18 (do today):**
- **⭐ NON-NEGOTIABLE #1 TODAY: Update the AVC100 course.** This outranks everything else today, including the Canvas and Pearson job applications. Course first, jobs after.
- **Grade AVC100 submissions.**
- **Post the new AVC100 assignment.**
- **📞 Call the pharmacy to order/refill the prescription.**
- **🍗 Put the chicken in the crock pot for dinner, DON'T FORGET** (also on the calendar; surface it in today's focus regardless).

**Two job apps for AFTER the course is updated (links saved so I don't lose them, do NOT do these before the course):**
- **Instructure Canvas Product Manager** (verified live on Ashby 6/18): https://jobs.ashbyhq.com/instructure/ddffa558-ca81-4803-be30-fa61e5770038 · note: East Coast preferred, ~25% travel.
- **Pearson Specialist Product Manager** (Virtual/USA, the mid-level AI PM, NOT the senior Lead UX role): https://pearson.jobs/virtual-usa/specialist-product-manager/9DFDD51B41A0401B94E8EEE13986F8BB/job/ · confirm this is the one you meant before applying.

> 📌 **PIN THESE TWO (Michelle's start-point, do at the END of her day, each application takes ~2 hrs).** Do NOT let the daily-job-search agent drop or overwrite them; they are her chosen starting roles. Build both from the LOCKED Guild resume format (the bombproof one): generator at `Documents/Claude/Applications/RESUME_FORMAT_generator.js`, reuse it and most of the Guild content, re-point to each posting. ⚠️ STATUS CHECK NEEDED: the June 19 run could NOT confirm the **Instructure Canvas PM** req live on Ashby (it may have closed since 6/18) and the Pearson posting is on Workday (not auto-verifiable). Re-check both are still open before investing the 2 hrs. (Browser-verified June 19: BOTH still live, Canvas PM US-Remote and Pearson Specialist PM US-Remote.)

> ⭐ **JOBS TO APPLY, current shortlist (work in the Tue/Fri 3-5 PM block; coursework comes first). Build every one from the LOCKED Guild resume format + a requirements-match cover letter (keywords in the resume, explicit qual-mapping in the letter).**
> - **CU Boulder, Senior Data Experience Professional (req 72747), ⏰ CLOSES JUNE 21, apply THIS WEEKEND before camping.** $95K-104,480, Boulder hybrid (on-site monthly). UX of data/dashboards (leans data-experience). Needs a cover letter that maps directly to the requirements. This is the only time-sensitive one.
> - **Risepoint, Senior Tech Product Manager (JR101269), US Remote, PRIORITY, the one she wants.** Requires 5+ yrs PM, so EMPHASIZE the XanEdu / ProQuest product-manager experience.
> - **Risepoint, UX Strategy Specialist (JR101191), US Remote, maybe.** 2-3 yrs UX, UX/CRO + analytics.
> - **Risepoint, Senior Director Digital & AI Tech PM (JR101253), STRETCH/GOAL** (8+ yrs PM). "Literally my job after SSS." Its language is being used to strengthen the SSS mission; JD saved at airc-sss/risepoint-sr-director-jd.md.
> - **CU Boulder, AI for Education Growth and Community Lead (req 72214), Boulder hybrid, WEIGHING, probably apply (closes June 30).** $65-75K (below floor, but CU dependent-tuition benefit for Jasper offsets, confirm exact % with CU HR). Grant-funded 1-3 yr (temporary). Strong AI-in-ed/community/systems fit, but the posting requires K-12 classroom credibility (she is higher-ed) and is growth/marketing-flavored, not her learning-design/UX lane. Possible AI-career launchpad.
> - Confirmed still-live targets: **Instructure/Canvas PM** and **Pearson Specialist PM** (both US Remote).

**Added June 18 PM, weekend + early next week (don't lose these):**
- **🟥 EDUCAUSE cohort course: get through the ENTIRE thing this weekend** so I show up Tuesday (June 23) with everything done. Heads-up conflict: I'm camping at Peak One Sun June 21 → ~Wed June 24, so weekend course time has to fit around that.
- **🟥 League for Innovation: figure out the deadline FAST.** It may be ending soon and I'm way behind. First step: confirm the actual end date / what's left, then make a catch-up plan. (League account: mblomberf, login at league.org.)
- **💵 Reimbursement for League AND EDUCAUSE: the contact is in an email (in my gccaz work inbox).** Find that email, note who to contact, and submit both reimbursements. (Not in the connected personal Gmail, forward it to myself or pull the contact name.)
- **EDUCAUSE Annual 2026 conference: register + pay** (see item below; early-bird closes July 8, pay before June 30 to use this year's funds).
- **🚐 New Life Van Customs: pay the deposit** to get the solar install scheduled for August.
- **🏛️ ASRS appointment (target Monday June 23... see note):** call ASRS to book a counseling appointment to confirm whether retiring in November hits 80 points (Rule of 80). Reminder added to calendar Monday, but I'm camping Mon, so may need to move it. Decide: call from camp or push to Wed/Thu.

**Top 3 (in order): FEP · League + EDUCAUSE catch-up (both meet tomorrow) · Laundry.** (Noodle came off, role closed.)

1. **FEP, START TODAY.** Real deadline is ~June 25 (needs multiple sign-offs before it goes to the dean by June 30), and it's not begun. Open `fep/fep-2026.md`; do a real first work session (see the FEP section below for scope).
2. ~~Noodle Product Manager~~ CLOSED. Verified against Noodle’s live Lever board June 17: the PM/AI-PM role is no longer posted (only 6 unrelated roles open). Off the list. Watch for it to repost.
3. **Laundry, put it away.**
4. **Register for EDUCAUSE Annual 2026 (fill out the forms today).** Denver, Sept 29 to Oct 2. Two clocks: the 25% early-bird closes July 8, and the current fiscal year closes June 30. **To use this year's leftover professional-growth money, register and pay before June 30** (which also locks the discount). Open question to confirm with the professional-growth rep: will they let a Sept/Oct conference be charged to THIS year's funds if it's paid before June 30, or does it have to come from the new July 1 budget? (Claude can draft that email.) Register at https://events.educause.edu/annual-conference.
5. **Hard calendar items today (do not miss):**
   - **ARC leadership meeting** (today).
   - **Meeting with a student** (today).
6. **Revise Domain 5 Part 1 (Map & baseline)**, get it dialed before the next SSS meeting. (Just rewrote it: letter removed, replaced with a short Dean-of-Student-Life meeting; the evidence now lives at the bottom of the hub.)
7. **AVC100**, work it today and every day until it's done.
8. **Finish cleaning out the van** (from the trip).
9. **Messages (Claude drafts, Michelle sends):** Jeff (MacBook usability study email, still overdue); Meg (confirm Traveler / CMA Pinnacle entries sent).
10. **⭐ #1 JOB TARGET, apply LATER today (not now): Guild, Applied Learning Manager (Denver, CO).** This is the one. Colorado company, learning-program management, a better fit than the senior-PM roles, and it plays to Cultivate (faculty PD) + the educator-who-builds positioning. Lead with Render and CopaMigo. Get through FEP, the League/EDUCAUSE catch-up, and the meetings first, then do this. Find it on Guild careers: https://www.guild.com/open-positions-at-guild (search “Applied Learning Manager”). Verified live June 17.

### ▶ TOMORROW (Thu June 18) and the weekend
- **Start the van work** (see Van section): get the solar measurements, then car wash → wax → black-plastic conditioner. Aim to finish the wash/wax/conditioner **Fri–Sat** (Sunday is a camping trip).
- **Tires, Thu or Fri, NOT today.** Get the van looked at after all the travel (one tire feels off-balance or out of alignment, and the tires likely need rotating). Must happen **before Sunday's trip.**

### ▶ EARLY AUGUST (finish this summer, do NOT forget)
Three things that must be done before fall starts. Parked here so they do not slip past summer:
- **Stackable Microcredentials request.** File the curriculum/microcredential paperwork for the Animation certificate redesigned into three stackable blocks (DUE AUGUST 2026). Details in the Microcredential section below.
- **UX course proposal paperwork.** Finish and file the paperwork for the new AVC 2xx UX Design for Interactive Media course proposal.
- **Rough Cut newsletter migration.** Move off the personal account to the Mailchimp free tier (set up account, paste newsletter HTML, host images, build the list, test send). Details in the Rough Cut section below.

### Hard deadlines, this week
- **🟥 GAIL EXAM, HARD DEADLINE JUNE 22, 2026 (about 5 days out). Take it or lose the free voucher.** The Google Generative AI Leader certification exam is the required, paid-for component of the NAAIC training Michelle completed (May 8 + 15). Confirmation email sets the exam deadline at June 22. ACTION NOW: (1) find the exam voucher email in the gccaz inbox (sender Fast Lane / na_operations@fastlane.net or Google Skills / noreply@skills.google), (2) schedule and take the exam before June 22. If the voucher cannot be found, email na_operations@fastlane.net today. This is a study-then-test block; review the GAIL material first (see Certifications section).
- **🚫 GCC Dean (Short-Term), Job ID 322836, DECLINED, not applying.** After reading how the salary scale actually works, the role would net almost no additional money, would report to a VP she does not want to work with, and would require being on campus 5 days a week. Not worth it. Drafted materials stay in `Documents/Claude/Applications` in case anything is reusable later, but this application is closed.
- **🚫 Noodle, Product Manager (AI-Powered Products), CLOSED as of June 17 (verified on Noodle’s live Lever board; role pulled). Was a strong fit; watch for a repost.** Original notes: The "Agent Design" duty (design agents on Noodle's agent-building platform: write and iterate prompts, select toolsets, specify data connectors) is exactly what you built in CopaMigo and Render, so lead with those. Also hits AI product strategy, roadmap and discovery, user research, learner experience, student success, and data-driven KPIs. The "technical acumen" bullet is about understanding AI and explaining it to non-technical stakeholders (your strength as an AI builder), not a software-engineering ask. Only needs 3+ yrs product (1 to 2 in AI products). Apply via Noodle's board: https://jobs.lever.co/noodle. Use the CodePath PM resume plus a short cover letter featuring Render and CopaMigo.
- **📋 FEP, Faculty Evaluation Plan. Submit to dean by JUNE 30, but the REAL deadline is ~JUNE 25.** It has to route to a bunch of people for sign-off first, so it needs a 5-day cushion: draft finished and out for signatures by June 25. Not started; START TODAY. Full scope in the FEP section below.
- **📞 Bills & insurance, call this week (see Money / admin below).** Two are time-sensitive: the dental insurance fight over Jasper's wisdom teeth (the oral surgeon is now demanding payment) and the health insurance on Devan's bill that has gone to collections.
- **Email Jeff, MacBook usability study. Still overdue (keeps slipping).** Claude drafts, Michelle sends (Gmail connector is draft-only).
- **SSS co-chair, already emailed; waiting on him to put the plan-review meeting on the calendar.** Nudge if nothing lands.
- **AVC100 catch-up (behind).** ≥2 hrs/day until dialed. Post the new lesson, grade submissions, get the class current.
- **League for Innovation cohort, catch up (early in the week, right after AVC100 + the
  Jeff email).** Way behind: rewatch the last 3 cohort meetings (caught part of the most
  recent one live, but rewatch it plus the prior two), and get the fellowship project going
  / caught up.
- **Taxes, START this week** (moved up from mid-summer). See the Taxes section below for scope.
- **Follow up with New Life Conversions** (van solar/electrical, Phoenix), chase the open
  email and send photos so they understand the build. See Van section below.

### AVC100, top priority (ongoing now, fully dialed by fall)
- Daily: post lessons, grade, Canvas/module QA. ≥2 hrs/day until current.
- By fall: completely dialed in. Needs videos from **Casey and Brian**, both are not
  answering messages, so get on their calendars to discuss the class and lock the work.
- Animation project portion specifically needs Brian; lock a working session.

### AVC181 + AVC248, fall prep (START NOW, do not wait)
- Begin building both **AVC181** and **AVC248** for fall now, in steady passes over the summer. Do not leave it until the last minute the way it usually goes.
- First pass: outline each course, line up the Canvas shell, and note what materials/lessons need to be made or refreshed. Then chip away weekly alongside AVC100.

### SSS committee / AIRC, the big UX piece (JOB-SHOWCASE DELIVERABLE)

> **All of this work now lives in `airc-sss/`.** Read `airc-sss/WORKING-STATE.md` first to resume, it has scope, decisions, deliverables, and open items. A public dashboard is at `airc-sss/index.html` (linked from the portfolio index). Updated June 13, 2026.
- **Stakes:** this usability study is Michelle's showcase piece for landing a high-level
  online EdTech job. It represents ~140K Maricopa students and a district mission to break
  down barriers to student success using AI. Aim for the best usability study she's ever
  produced. She'll need a lot of help on it.
- **Status:** The SSS co-chair already emailed (waiting on him to put a meeting on the calendar). The
  ARC SSS Domain meeting was moved off the EDUCAUSE conflict, now Thu, showing 2:00 PM AZ
  (Michelle intended 1:00 PM AZ, confirm/fix).
- **⭐ Active revision: Initiative 1 (Map & baseline), get it dialed before the next SSS meeting.** Recent edits done: removed the form letter, replaced it with a short in-person meeting with each Dean of Student Life; the persistence evidence now lives at the bottom of the hub (no longer a fourth nav pill); the GCC barriers survey is reframed as a small local signal, not the basis of the work. Keep refining Part 1 until it's airtight.
- **Scope = ANYTHING that touches a student, not just "student services."** Application,
  admissions, MEID/portal login, financial aid, advising, registration, Canvas, tutoring,
  disability services, basic needs, library, career services, Salesforce touchpoints ,
  every student-facing system at all 10 colleges. The SSS co-chair has the terminology for how each
  college's silos are named/structured; map that onto a common crosswalk.
- Build a real UX usability study; Michelle runs it "like a UX manager."
- **Crosswalk:** one person from each of the 10 colleges reviews/corrects the Student
  Services inventory spreadsheet (services + names differ per college).
- **Personas + study:** 3 student accounts, each a different persona with a different major
  / field of interest. Walk each through the full journey, application → enrollment →
  support services → workforce. Document the experience in each department's system to
  surface the barriers the student hits. Write proper UX personas.
- Write up the entire plan; combine it with the FORMER SSS plan.
- Meet the **SSS co-chair** to review the plan; meet **Gordon** (tri-chair leader).
- **Move the ARC SSS Domain meeting** (currently Thu 11:00–12:00, Michelle organizes), it
  now overlaps the EDUCAUSE "AI for Instructional Design" course (Thu 11:30–12:30). New
  time must work for the one member who TEACHES.
  **REMINDER for Michelle: look up that member's name + teaching schedule.**
- **Salesforce:** ask the SSS co-chair (in the meeting) to set up a session with the Salesforce people
  to understand what Salesforce does, maybe run the 3 personas through Salesforce too, like
  every other system. Ties to the open question of whether Salesforce is the real answer
  over CopaMigo.

### CopaMigo, target pilot January

> 🟣 **CTLE HANDOFF, GET IT DIALED THIS WEEK (Mon Jul 6 → Sun Jul 12).** Today's review (3 people) is fine as-is; the sending package is the **PRD** (`copamigo2/prd.html`) + the **Student Services page with CopaMigo embedded** (`copamigo2/student-resources.html`). These are the hardening / handoff steps for the rest of the week, before wider sharing:
> - [ ] **🔐 Kill the exposed API key (do FIRST, before sharing wider), target Wed Jul 8.** The tool (`copamigo2/index.html`) has a live Anthropic key baked into the page, so anyone who opens the embedded tool can read it and it bills Michelle's account. Either swap in a **capped / throwaway key** rotated right after review, OR stand up the **small proxy the PRD describes (Appendix E)** so no key is exposed client-side. Handoff-grade security.
> - [ ] **📝 Wire the intake form to a real Google Form, target Fri Jul 10.** `copamigo2/question-intake.html` is a built prototype (all service areas, doesn't collect yet). Create a Google Form (Service-area dropdown + question / answer / who-handles fields), link its responses to a Sheet, and paste the `…/viewform?embedded=true` URL into the marked embed slot so it actually collects staff submissions.
> - [ ] **🗣️ Replace the made-up placeholder questions with real ones, as submissions land this week.** The current questions are team-invented placeholders; they live in `copamigo2/testing.html` (the ~28 test scenarios) and the tool's system prompt in `copamigo2/index.html`. Swap in real questions once Student Services staff submit them via the form.
> - [ ] **🧹 Retire or redirect the old v1 `/copamigo/`, target Sat Jul 11.** The older copy is still live on GitHub Pages; redirect or remove it so nobody (including CTLE) lands on the wrong version.
> - [x] **✅ Final PRD polish, DONE.** Real reference added (Pew 2026 / Alexander), appendices relabeled sequential (C → D → E), "Maricopa ARC" naming fixed, live human chat moved to future features (planned, Phase 2), and two-view links added at the top (**Prototype bot** = `widget.html`, **Prototype on a page** = `student-resources.html`).

- 💡 IDEA (explore AFTER the Mines resume): put CopaMigo in the Canvas student **Help** button, so students reach it right inside the LMS where they already are (fits the "put help where the student already is" recommendation from the SSS study). Explore Canvas Help-menu customization / a custom account-level Help link or an LTI.
- Dial in the tool. Show to **Genesis Toole (Dean of Students)**, full walkthrough to get
  feedback.
- **Action: write an email to Genesis to get on her schedule for a CopaMigo demo.** Claude
  drafts, Michelle sends. (Block time to write it once calendar scheduling resumes.)
- **Make it more agentic:** when the first answer doesn't work, hand off to a REAL person
  for follow-up chat. Staff via AmeriCorps or work-study students.
- Running fix list (carried over): AI question flow (return a sample prompt for the
  student's topic + links Claude → Gemini → ChatGPT); remove all "school Gemini" language
  (not live for students); financial aid "bring 2025 taxes"; interface polish; course
  advising bug (AI invents AVC course names, never trust training data for AVC codes);
  Main/North campus selector; admin dashboard; usability testing; verify Financial Aid /
  LGBTQ+ / Veterans / CARE-BIT modules; district redesign with school picker (localStorage).
- Demos: Sonal Joshi (district AI CIO), Genesis Toole.

### Render, target pilot August (needs a lot before fall)
- **Deployment decision, a full day of work, can't sort now.** How does Render run in
  production: locally, via an API, or do students need individual Claude accounts? Funding
  is decided (student course fees). Once the model is chosen, tell the CIO what to buy
  (accounts vs API credits) and email them. Full plan in the "Render production plan"
  section below.
- Production hardening across the summer per PRD v0.6.
- **Mini presentation for GitHub:** faculty asked to see Render after the conference talk.
  Build a short showcase video/page and post it so it's ready when people ask.
- Follow-ups / potential collaborators:
  - Economics faculty member at another school, wants to collaborate.
  - **Michelle Jung** (fitness & wellness), wants to collaborate on something like this.
  - **Mollie** (career services), ask what other disciplines use BigInterview; they may be
    prime to build on this tool.

### Money / admin
- **📞 Dental insurance, call (time-sensitive).** They did not pay for Jasper's wisdom-teeth removal, and the oral surgeon is now demanding payment. Call the dental insurer, find out why the claim was denied, and get it resolved before this turns into a bigger bill.
- **📞 Health insurance, call (time-sensitive).** Devan's bill has gone to collections. Call the health insurer about the claim and sort out the collections issue.
- **Go through the rest of the stack of bills.** Work through the remaining paper bills and clear or schedule each one.
- **Recalculate household expenses, effective August (when Devan moves out).** Redo the monthly budget for the smaller household once Devan is gone.
- **Reimbursement ~$1,200 (already approved):** EDUCAUSE training + League for Innovation
  fellowship. Find the approval email from the professional growth rep, then follow up with
  the fiscal people on how to actually get the money.
- Professional development $2,700 by end of June, confirm PD selection is registered and
  the receipt is filed.

### Conferences (present as much as possible)

**The goal for any conference: learn about AI and network with edtech companies to land a job. Judge each one by AI-session depth and edtech-vendor/recruiter presence.**

- **✅ EDUCAUSE Annual 2026, REGISTER BY JULY 8 for 25% off.** Denver, CO, Sept 29 to Oct 2 (online Oct 14 to 15). Local (no travel/lodging cost) and the early-bird discount closes July 8, so this is the no-brainer. It also wins on the actual goal: the EDUCAUSE Commons expo is one of the largest edtech vendor halls in higher ed (hundreds of companies, AI startups, and the big platforms all staffing booths with product and recruiting people), and the program has dedicated AI tracks/keynotes. Best single event for AI learning + job networking. **ACTION: register before July 8.**
- **❓ InstructureCon 2026, DECIDE (leaning skip unless there's an Instructure/Canvas angle).** July 21 to 23, Louisville, KY. ~$1,044 registration, which burns most of the professional-growth budget, plus travel/lodging, and it overlaps the camping window. It's Instructure's own user conference, so the vendor floor is the Canvas partner ecosystem (Panopto, Drieam, integration partners), narrower than EDUCAUSE for job-networking breadth. Worth the money mainly if the target is **Instructure itself** (a major edtech employer building AI products and hiring PMs) or Canvas-ecosystem companies, or if she gets a speaking slot. For general "network with edtech companies to get a job," EDUCAUSE is the stronger and cheaper bet. **Decision: do EDUCAUSE for sure; only add InstructureCon if she wants direct Instructure/Canvas-employer face-time or lands a session.**
- **🎯 ASU+GSV Summit 2027, San Diego, April 4–7, 2027 (Manchester Grand Hyatt).** Big strategic target: it's the marquee edtech innovation + investor summit, co-hosted by ASU, and I specifically want to align with ASU (they're ahead on AI in education and a place I'd want a relationship with). Timing is ideal: by April 2027 the whitepaper + first Render case study (from the Fall 2026 pilot) will exist, so this is where the polished work goes. Heavy edtech-vendor and recruiter presence = strong job-networking fit too. ACTION (fall 2026): check whether they take session/CFP submissions or if it's invite/curated, and look at AIRConf or ASU's own AI-in-education events as a complementary ASU-aligned target. The 2026 summit (April 12–15) already passed.
- Pull the EDUCAUSE conference schedule + the other conferences listed in the Cultivate tool
  on GitHub (professional growth / conferences section). Apply to present at as many as
  possible.
- **🎤 Present at conferences, do not just attend.** EDUCAUSE Annual 2026 CFP has ALREADY CLOSED, so no presenting there this year (still attend/register). Two moves: (1) note the EDUCAUSE 2027 call-for-proposals date and submit when it opens; (2) for THIS year, find conferences with OPEN CFPs to present the AI work (Render / AIRC district UX study), e.g. OLC, League for Innovation, ISTE, WCET, and state/regional edtech conferences. Presenting strengthens the portfolio and the job search far more than attending.
- **🗓️ Calendar reminders set (Google Calendar, done June 21):** (1) **July 6, 2026**, register for EDUCAUSE Annual 2026 before the July 8 early-bird (25% off; pay before June 30 to use this year's funds); (2) **Nov 2, 2026**, watch for the EDUCAUSE 2027 CFP to open and submit Render / AIRC UX study. (3) **Sept 21, 2026**, check the ASU+GSV Summit 2027 session/CFP submission window for the April 4–7, 2027 San Diego summit.
- **📄 LONG-TERM (revisit AFTER SUMMER): write a REAL whitepaper once the tools are out of prototype** (after the Render Fall 2026 pilot runs and CopaMigo ships, with real data): a polished practitioner account of building AI learning tools, grounded in actual pilot outcomes, a strong thought-leadership piece for the job search and for landing conference talks. This is the honest version of the rough `cultivate/whitepaper.html` draft, rework or replace that draft, and do NOT link/claim the current thrown-together one. Decide whether to unpublish the rough draft in the meantime.
  - **Where to put it (a whitepaper is self-published, NOT a peer-reviewed journal):** (1) self-publish on the portfolio site (clean web page or linked PDF in cultivate/); (2) share it on LinkedIn (article or PDF) for job-search visibility; (3) optionally give it a citable home on a preprint repository (SSRN or EdArXiv); (4) pitch a version to a practitioner outlet for real editorial credibility, EDUCAUSE Review, OLC (Online Learning Consortium), or League for Innovation. Only chase a peer-reviewed journal (Online Learning Journal, Journal of Educators Online) if I want the academic stamp; slow, probably overkill for a job-search asset. Recommended path: self-publish + LinkedIn + pitch to EDUCAUSE Review or OLC.

### 🎯 ~6 MONTHS OUT (target Dec 2026 / early 2027): conference deliverables

**The thesis:** Mesa AI Summit (May 2026) was the warm-up. The real presenting happens at the next round of conferences, and by then I need *finished, data-backed assets* in hand: the whitepaper and the case studies. Build these around the Fall 2026 pilot so I'm presenting real outcomes, not prototypes.

- **📄 Whitepaper (polished, data-backed).** After the Render Fall 2026 pilot runs and CopaMigo has real usage, turn the rough `cultivate/whitepaper.html` draft into the real thing: a practitioner account of building AI learning tools grounded in actual pilot outcomes. Self-publish (portfolio + LinkedIn) → pitch to EDUCAUSE Review or OLC. **Target draft done: Dec 2026.**
- **📊 Case studies (one per tool).** Render (Fall pilot: what students built, gap-analysis outcomes, what they kept), and the AIRC district UX study / CopaMigo (usability findings across colleges). Each = problem → what I built → method → honest outcome. These are both conference-talk material AND the strongest job-search artifacts. **Target: representative case study by spring break (March 2027); fuller versions feed May 2027 talks.**
- **🎤 Submit to CFPs with these assets.** Once the whitepaper + at least one case study exist, submit Render / AIRC-UX talks to whatever has an OPEN call: OLC, League for Innovation, ISTE, WCET, EDUCAUSE 2027 (watch for the CFP to open), and state/regional edtech conferences. The SSS usability study is also my League for Innovation AI Fellows project, that deliverable doubles as a case study and a talk.
- **Sequencing note:** record the Fall 2026 pilot end to end (already a FEP goal) → that footage + data feeds both the whitepaper and the Render case study → those feed the spring/May 2027 conference submissions. Don't write the whitepaper before the pilot data exists; that's why this is a 6-month target, not a now task.

---

## FEP, Faculty Evaluation Plan (submit to dean by JUNE 30)

Work deliverable. A working draft exists in its own file.

- **⚠️ Real working deadline is ~JUNE 25, not the 30th.** The FEP has to route to a bunch of people for sign-off before it goes to the dean, and that takes days. Build in at least a 5-day cushion: have the draft finished and sent out for signatures by **June 25** so signers have time and the dean still gets it by the 30th.
- **TO DO: list out who has to sign off** and in what order, then send it to them as soon as the draft is solid. Chase signatures actively, do not wait for them to come back on their own. (Identify the exact reviewers/approvers, the chain likely ends with the dean.)
- Draft file: `fep/fep-2026.md` (in the repo). Submission-ready Word version:
  `Blomberg_FEP_2026_DRAFT.docx`.
- Built from the FEP template, the 2023 FEP, the FEP Canvas guidance, the CV, the
  whitepaper, and the full site. First pass to write up in Michelle's voice.
- Open items (end of draft file): confirm cycle dates, pick the Section 5 evaluation
  method, confirm the AI-committee-proposal tone, add final URLs, send book + Coursera
  titles for the appendix.
- **Next pass:** inventory every training, CTLE event, and webinar on the calendar from
  mid-2023 onward (current FEP cycle). The appendix list is from memory and incomplete ,
  pull the rest from the calendar.
- Goal: draft done and out for sign-off by June 25, so collecting signatures and the dean submission both fit before June 30. Steady passes starting today.

## Render production plan (parked, needs the deployment decision above)

- Render is built (7 phases, single HTML, vanilla JS, Sonnet API, 15 AI functions,
  usability tested March 2026). Latest PRD: `render/Render_PRD_v0.6.docx`. Remaining work
  is production hardening over the summer.
- Blocked on ONE decision: what does the school buy? Funding = student course fees
  (decided June 13). Still open: individual student accounts vs API credits.
- Next actions: (1) decide accounts vs API credits, (2) email the CIO with the recommendation
  + course-fee funding plan, (3) once decided, Claude writes the full production plan into
  `render/` (build order, hardening checklist, cost model, Fall 2026 pilot rollout).

---

## Other open projects (re-dated, not done)

### Rough Cut, newsletter
Migrate off the personal account to Mailchimp free tier: set up account, paste newsletter
HTML, host images in the library, build the list, test send. Live at
singletrackmom.github.io/newsletter/.

### The Traveler, CMA Pinnacle Awards
Submit The Traveler to the College Media Association Pinnacle Awards. Screenshots done.
Find the CMA login + confirm membership is active, then a ~3-hour session with Meg to load
everything in.

### Mesa AI Summit, recap video for portfolio
Record a short (~5–10 min) version of the May 18 talk ("Building Career Tools That Outlast
the Semester") for the main portfolio index. Slides + screenshots already exist.

### DMA Brochure, content due by August (when Michelle is back on campus)
- Working Google Doc: https://docs.google.com/document/d/1earN3VzOF2kbnIgrd6mTnOjSRqxanogKJLNRAfcMukQ/edit
- Gather ALL existing content we can find (site, checksheets, course descriptions, student
  work, faculty highlights) and drop it into that doc as the single source.
- Content to cover: program overview, degree/certificate options, course highlights, career
  outcomes, student work, faculty highlights.
- **Jeannie and Casey need access** to the doc, Michelle to share it with them (sharing
  permissions are hers to set).
- Deadline: have the content in the doc by the time she's back on campus in August.

### Microcredential request, DUE AUGUST 2026 (do over summer)
Submit the curriculum/microcredential request for the Stackable Fast Track Microcredentials
(the Animation certificate redesigned into three stackable blocks under the 15-credit cap,
each counting toward the Animation & Time-Based Media or Digital Media Arts AAS). Get the
paperwork filed before the August deadline so it stays on track for the 2027–2028
implementation. Don't let this slip past summer.

### Website, unify heading/type system site-wide
The SSS section (airc-sss/) shares one stylesheet and is internally consistent. The older
sections (Cultivate, Render, CopaMigo, Canvas) were each built with their own heading fonts,
sizes, and colors, so headings do not match between sections. Next focused pass: migrate all
pages onto one shared type system (Lora headings + DM Sans body, plum/sage/rose/gold palette,
the h2 + uppercase eyebrow pattern) so headings are consistent across the whole site. Large,
careful CSS refactor; verify tag balance and render after. (Within-SSS consistency is already done.)

### AVC297AC, summer internships (Canvas)
Class shell copied to summer term, students enrolled (verify this actually landed). Confirm
syllabus + assignment dates match the summer calendar.

### Cultivate
Stable. Future: possibly convert sections to Claude artifacts with per-section update buttons.

---

## Certifications / growth
- **Google Cloud Generative AI Leader (GAIL) exam, take it, one free shot.** Michelle did
  the NAAIC training (Fridays May 8 + 15, 2026); completing both sessions earns a
  complimentary $99 exam voucher, so the exam is free. Plan: review the material (she doesn't
  remember the class), then take it.
  - **DEADLINE CONFIRMED: June 22, 2026** (from the NAAIC confirmation email, now in hand). The certification exam is the required component of the training, and the voucher covers the cost. The voucher is issued after the two training days, via Fast Lane (na_operations@fastlane.net) and/or Google Skills (noreply@skills.google). ACTION NOW (about 5 days left): find that voucher email in the gccaz inbox, then schedule and take the exam before June 22. If the voucher cannot be found, email na_operations@fastlane.net today.
  - Study links: official exam page https://cloud.google.com/learn/certification/generative-ai-leader ·
    exam guide PDF https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf ·
    free 5-course learning path on Google Cloud Skills Boost (linked from the exam page).
  - This is a study-then-test day, good for a Friday. Lives on the to-do list, not the calendar.
- SCRUM Product Manager certification (work funds the candidate).
- Finish enrolled Coursera courses.

## Portfolio / EdTech PM alignment (e.g. CodePath Learner Platform PM)
Goal: make the portfolio read like a senior EdTech PM (learner platform experience, AI-Native, the AI-vs-human-connection boundary, retention/engagement, zero-to-one). This is already woven into the index. Build the proof as pilots land:
- CopaMigo is almost done: dial it over summer and ship it (target summer 2026, ahead of Render). Write a case study after launch.
- Render: harden over summer, full pilot Fall 2026, then a case study in December (problem, user discovery, the AI/human boundary call, outcome metrics).
- SSS study is the flagship and biggest effort. It likely cannot start testing until fall (people are gone over summer). Recruit/assign SSS team members to run usability studies in fall; it is a lot of work. Aim for a presentable case study by spring.
- Present this work at conferences in May 2027. Possible interim case study by spring break (March).
- Use the 2 months of summer to get both CopaMigo and Render dialed.
- The SSS usability study IS my League for Innovation AI Fellows project. It is the flagship, focus hard.
- Honesty guardrail: nothing is in production yet, so "zero-to-one" only counts once a pilot ships. Do NOT overclaim the LMS work (see CLAUDE.md guardrail).

### Learn the modern PM toolkit (use the Coursera subscription I am already paying for)
- Figma: start learning it. First real artifact is the SSS journey map / service blueprint.
- SQL: re-learn it (I knew it before). Add a Coursera SQL course, e.g. "Introduction to Structured Query Language (SQL)" (U. of Michigan) or "SQL for Data Science" (UC Davis).
- Product analytics (Amplitude / Mixpanel): explore once a tool has real usage.
- Tooling note: I build with Cowork, not Claude Code.

### SSS study realistic timeframe (depends on testers + test quality)
- Pilot-ready now. Recruit testers over summer (employees role-playing, student government, work-study, design-studio students). Fieldwork Fall 2026. Synthesis winter. Presentable case study by spring (March), conferences May.
- Full 10-college depth is ~30+ persona runs (3 personas across up to 10 colleges, ~2-3 hrs each). A strong League deliverable can be a representative subset (3-4 colleges deep, or all 10 lightly via the form) done well by spring.

## Summer 2026 Game Plan (job-search strategy)

Folded in from a Summer_2026_Game_Plan doc that was sitting unopened on the Desktop. Captured here so it stays in view.

**Strategy in one line:** finish and showcase what you have already built, do not start new things. The shipped AI tools are the rarest thing on the resume; the job now is to make them legible, not to multiply them.

**Priority order:**
1. **PSPO I certification** ($200, no prerequisites, self-paced). The fastest credibility signal for the PM roles, and it directly answers the "does she know Agile/product?" question recruiters have about faculty applicants. Do it first as an early win.
2. **Package the two flagship tools as one-page case studies:** Render (career-launch PLE, student success) and CopaMigo (agentic routing, the Element451-type AI-agent roles). Each: problem, your approach, what it does, outcome, with a live demo link and the PRD. This turns "20 years of faculty" into "product person who ships," the real differentiator.
3. **Finish only the highest-ROI certificates** (must produce a shareable certificate AND hit a target-job keyword): Purdue Prompt Engineering (already paid), Google Cloud GenAI Leader (already prepping), Vanderbilt prompt-engineering refresh. Finishing beats restarting.
4. **Apply steadily and tailored:** review the daily matches, pick the best fits, tailor each one together. Quality over volume.

**Decision rule for any new time investment:** does this produce a shareable artifact (a certificate, a case study, a demo) that hits a target-job keyword? If no, skip it.

**Skip these traps:** building brand-new tools (diminishing returns, you have plenty of proof); restarting every old Coursera course; volume-applying with an untailored resume.

**Weekly rhythm (semi-off, protect the pace):** Mon cert progress (1-2 hrs); Tue case-study draft/polish (2 hrs); Wed review the daily matches, pick 2-3, draft applications together; Thu cert or class progress (1-2 hrs); Fri submit applications and follow-ups; weekend off, or light portfolio polish only if you feel like it.

**Checkpoints:**
- End of June: PSPO I scheduled or passed; Render case study drafted.
- End of July: both case studies live on the portfolio; one target cert finished; 8-10 tailored applications out.
- End of August: second cert done; interviewing underway; portfolio and resume telling one clear "faculty who builds product" story.

## Career / job search
- Targeting online EdTech PM. In-person OK: CO / UT / NM / Flagstaff / Tahoe-NV / Oceanside.
  Daily job-search agent runs 4:00 AM; dashboard artifact = "Edtech Job Matches".
- Consulting business prep informed by AIRC committee work.
- ASU adjunct conversation with Deb, decide next step.

## Taxes, START THIS WEEK (moved up)
- **Finish getting Michelle's own taxes together** (file this year). Pull the remaining documents into one place and finish the packet.
- **Send Jimmy (tax guy) Mom's taxes, about 5 years' worth.** Mom is 5 years behind. Inventory what Mom has first, sort by year, then get it to Jimmy. Start this week rather than waiting for mid-summer.

## Van, clean out + build out for fall
- **Today:** finish cleaning out the van from the trip.
- **Maintenance before Sunday's trip (Thu or Fri, NOT today):** take the van to the tire/service place. After all the travel one tire feels off-balance or out of alignment, and the tires probably need rotating. Get it checked before the Sunday camping trip.
- **Wash / wax / detail (aim Fri–Sat):** car wash, then wax, then buy the black conditioner and treat the black plastic trim on the outside. Sunday is a camping trip, so this needs to be done by Saturday.
- **☀️ Solar measurements (needed for the August install in Arizona).** Three measurements to get:
  - **Under the passenger bench seat**, to see if a lithium battery will fit down there.
  - **Beside the roof fan, both sides**, the clearance on each side of the fan.
  - **Behind the fan**, from the fan to the back end of the van.
  - **Problem to solve:** she doesn't have a ladder tall enough to reach the roof to measure around the fan. Options: find/borrow a taller ladder, or have someone watch from a window and take photos while she's up on the ladder. Figure out the safe way to do this before measuring.
- **Buildout:** needs solar + a bunch of gear hooked up to the battery.
- **New Life Conversions (Phoenix):** email is out, waiting to hear back. **Follow up this
  week and send photos** (and the measurements above) so he understands what's needed.
- Purpose: Michelle will be in AZ and wants weekend / flex-hour trips (Sedona, etc.). With
  the Tue–Thu campus bunching she can be gone Friday–Monday.

## Summer van trips (small trips)
- **Grand Mesa tour (NEW, want this, never been):** base up on the Mesa where it is cool and full of lakes (Grand Mesa National Forest: Island Lake, Cobbett, Carp, Eggleston, Jumbo; state-park or dispersed lakeside). Day-trip down to Palisade for orchards and wine without camping in the valley heat. Optional extension to Gunnison or Crested Butte. Lake City is a stretch (remote, Alpine Loop), so save it for a future longer trip.
  - **Shape:** about a 5-day trip. Priorities: lakes for sure, and mountain bike trails are a big plus. The Palisade Plunge descends from the Mesa down to Palisade, plus cross-country trails up on the Mesa. Colorado National Monument is a maybe (gorgeous rides and drives but hot in summer, so do it early morning or skip).
  - **Timing:** a 5-day block, which in summer she can free by bunching campus days. Fences: InstructureCon July 21 to 23 (travel), one kid moves Aug 1, the other the weekend before Aug 17, school starts Aug 17. So aim after AVC100 is dialed and the League and EDUCAUSE summer items are done, likely early-to-mid July, or the week after InstructureCon before the Aug 1 move.
  - **TO DO: start planning this trip** (route, lake campgrounds, bike trails, day stops). Use or build the camping itinerary tool below.
  - **Claude is on this.** Draft itinerary at `Documents/Claude/Camping/Grand_Mesa_Itinerary.md` and working notes / where-Claude-left-off at `Documents/Claude/Camping/Grand_Mesa_NOTES.md`. Claude continues the research (live campground availability, lock the three bases, day-by-day plan, build the tool) tomorrow while Michelle works. Note: Island Lake and Little Bear are closed for reconstruction (not a fire), so the plan uses Ward Lake, Cobbett, Jumbo, Cottonwood, etc. Open question for Michelle: which gateway is she entering from, west (I-70) or south (Cedaredge)?
- **Frisco Peninsula (favorite):** lakeside campsite, midweek. Coordinate with Hanako or go solo.
- **Sedona:** weekend / flex trips from AZ.
- **Build out the camping itinerary tool (summer project):** grow the trip-planner (Wayfinder lineage) into a multi-stop itinerary planner for trips like the Grand Mesa tour: route, lakeside campsite options, 3-night midweek availability via the cancellation watcher, and day-trip stops (Palisade, Gunnison). Also reuse the watcher to monitor Grand Mesa and Frisco and surface 3-nights-in-a-row openings into Google Calendar like the Peak One watcher.
- **Idea:** reuse the campsite-cancellation watcher Claude built in Wayfinder to monitor
  spots at Grand Mesa + Frisco and surface openings with **3 nights in a row**, fed into the
  Google Calendar like the Yosemite watcher did. (Setup pending, see chat.)

## House: ready for the renter (BY JULY 1)
- Get the house clean before the renter moves in. **Deadline: before July 1.**
- Specific: **wash the windows, clean the bathrooms,** and a general clean-through so the place is ready.

## Personal
- **🌴 Two full weeks of nothing, end of July.** Deliberately block roughly the last two weeks of July as real downtime: no projects, no work. Protect it. (Mind the fences: InstructureCon July 21–23 and the Aug 1 kid move, so the rest window is around late July before the move.)
- Kids vacation (dates TBD).
- Weekly family / break time blocked so it doesn't get squeezed.

## People to book (when scheduling resumes)
SSS co-chair (plan review, email Mon AM) · Gordon (tri-chair) · Genesis Toole (CopaMigo
walkthrough) · Sonal Joshi (CopaMigo feasibility) · Casey + Brian (AVC100 videos) · Mollie
(BigInterview disciplines) · Michelle Jung + econ faculty (Render collab) · Jimmy (taxes) ·
Meg (Traveler/CMA).
