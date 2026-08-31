# ☀️ START HERE, MORNING OF 31 AUGUST 2026

**A fresh session with no memory of last night should read this whole block before touching anything.** It is the running order. Everything below the divider marked REFERENCE is background, not instructions.

Last night ended with **preflight green**, 5,818 links resolving, and v2 structurally finished. What is left is one safety job, three page conversions, and a short list of corrections.

---

## 🚨 JOB ONE. Do this before any portfolio work.

**`airc-sss/` is publicly serving material that should not be public.** Verified by opening the files, not assumed. `.nojekyll` sits in the repo root, which disables Jekyll, so GitHub Pages serves every `.md`, `.docx`, `.xlsx` and `.pptx` at its literal path. Both front pages link the folder, so it is crawled.

**Claude cannot fix this.** The shell only reaches the repo, and these files have to move *outside* it. This is Michelle at the keyboard, in Finder and GitHub Desktop.

### The move list, in priority order

Move to `~/Documents/Claude/ARC/`, then commit the deletions in GitHub Desktop.

**Tier 1, the ones that matter most:**

| File | Why |
| --- | --- |
| `risepoint-sr-director-jd.md` | A saved job description sitting inside district committee work, saying the SSS mission &ldquo;says it better&rdquo; and listing phrases to pull into the project outcome |
| `WORKING-STATE.md` | Says the study &ldquo;doubles as Michelle&rsquo;s UX job-portfolio piece.&rdquo; Also carries her GCC work email, her personal Gmail, a named district administrator, the live form URL, and committee positioning |
| `BARRIER_REGISTER_2026-08-27.md` | Ten named colleges rated on their failures, 34 severity-scored findings. Mesa 14 mentions, Chandler-Gilbert 12, GateWay 11, Scottsdale 11, Estrella 10, South Mountain 9, Glendale 7. Also names a district staging host as a defect before the web team was told |
| `PHASE1A_RUNS_2026-07-27.md`, `PHASE1B_RUNS_2026-08-25.md` | Raw run logs, college-attributed |

**Tier 2, same pass:** `SSS_Working_Group_Charter_DRAFT.docx` &middot; `SSS_Domain_Meeting_Agenda_June18.docx` &middot; `AIRC_Domain5_Student_Support_Success_Plan.docx` &middot; `Student_Journey_Form_Blueprint.docx` &middot; `The_Persistence_Imperative.pptx` &middot; `Maricopa_Scenario_Bank.xlsx` &middot; `Maricopa_Student_Journey_Study_Kit.xlsx` &middot; `meeting-agenda-2026-07-09.md` &middot; `_CHANGES-2026-07-27.private.html` &middot; `ARC_AGENT_INTERVIEW.md` &middot; `agents/` (51 files) &middot; `synthetic-student-agent.md` &middot; `research-aggregator-agent.md` &middot; `build/tester_data.json` &middot; `build/scenarios.json` &middot; `export/` &middot; `Create_Barrier_Log_Form.gs` &middot; `HOW-TO-BUILD-THE-GOOGLE-FORM.md` &middot; `run-log-form-setup.md` &middot; `WGU_TECHNICAL_MODEL.md` &middot; `RUNNING-THE-STUDY.md`

**Keep public:** the HTML case-study pages, the cover and journey graphics, `sss.css`. Those are hers and they are the portfolio.

### Three more things while in there

1. **Check GitHub Desktop history for `airc-sss/_paper-source.private.html`.** It holds a staff contact roster. It is gitignored now, and **gitignore is not retroactive**, so it only helps if the file was never committed. It is not in the working tree, which is consistent with either answer.
2. **Close or gate the Jotform.** It is linked from `run-sheet.html` and open to anyone, which lets a stranger poison the dataset.
3. **`ethics.html` and `airc-sss/index.html` both say findings &ldquo;stay unpublished until the domain confirms them.&rdquo;** That is currently false, on the same server. Once the files move it becomes true again. This is the reason the move is urgent rather than tidy.

**Genuinely fine, so do not spend worry here:** no FERPA exposure, no student PII, no real participants, no IRB needed for anything run so far. The 20 files in `export/` are build tooling, not transcripts. All 51 files in `agents/` are prompts, not results. Every persona name is fabricated. Naming the district is fine.

---

## JOB TWO. The three big projects have no v2 page.

Michelle approved converting all three. **Read this before starting, because &ldquo;just copy it straight over&rdquo; will not work.**

| Project | Pages | With inline `style=` | With `<style>` blocks |
| --- | --- | --- | --- |
| `airc-sss/` (Student Journey) | 14 | 13 | 7 |
| `render/` | 14 | 14 | 13 |
| `copamigo/` | 13 | 13 | 12 |

**`tools/v2-lint.py` blocks every one of those**, and it blocks on purpose: no `<style>` block, no `style=` attribute, must link `/v2/assets/v2.css` and nothing else, two-link nav, locked footer, `noindex`, one `h1`, `main#main`, skip link, eyebrow under the h1. So this is conversion, not copying, at roughly 41 pages.

**Suggested order, and check it with Michelle first:**

1. **Render.** Biggest portfolio payoff, and the v2 tab structure is already decided in this file: Overview, Live tool, The course, Product requirements. `learning-design/avc248.html` becomes the course tab or it is orphaned on promotion. Decide what happens to `render/hiring-panel.html` and `render/interview-panel.html`, which are linked from nowhere.
2. **CopaMigo.** Standard Overview, Live tool, Product requirements.
3. **Student Journey.** Do this one last and do not rush it. It needs its own decisions, below.

**Nothing is broken while this waits.** The v2 cards point at the v1 pages, those pages work, and v1 is never deleted, so the links keep working after promotion too. What is missing is v2 chrome, which is cosmetic. **Job one is not cosmetic.**

### The Student Journey needs more than a conversion

Michelle: &ldquo;copy it straight over as it is and we can prune it later,&rdquo; but also &ldquo;I want to call out the synthetic students and ethics, I do not want to get in trouble.&rdquo; Those pull in opposite directions, so: **convert it as it stands, then do the ethics and anonymization pass before it is linked from anywhere public.**

Currently nine tabs, three of which overlap. Recommended six:

| Tab | What goes on it |
| --- | --- |
| Overview | Goal, Audience, Process. Absorbs the current Scope page |
| Method | Persona construction, the one persona plus one college plus one task model, saturation, the findings schema |
| Synthetic students | The 52-agent architecture and the literature, including where it fails. The differentiator, and what an employer will ask about |
| **Ethics and limits** | **Sits before Findings, never after.** A reader who meets the caveats first reads the findings as careful. Full drafted language is in the audit block below |
| Findings | Does not exist yet and is the tab a hiring manager wants. **College A through J**, mechanism level, led by &ldquo;retrieval matches vocabulary, not need,&rdquo; carrying the four retractions as a strength |
| Roadmap | Absorbs Approach and Build teams |

**Drop Progress as a public tab.** Its one strong item, the channel assumption named as the largest threat to validity, moves into Ethics and limits.

**Anonymization is not optional.** Colleges are A through J for failures **and for wins**, because naming the winners makes the losers identifiable by subtraction. Local service names each identify their campus instantly, including the Coyote Cupboard example, which is the best one in the corpus and the most identifying. Never publish the staging hostname. Never publish the persona-to-home-college roster.

**Required under every statistics block:** &ldquo;Counts are AI agent runs. No human participant has taken part in this study.&rdquo;

### The format question Michelle wants to think about

She asked whether the Journey should use the screenshot format. **It has better material than screenshots:** `progress.html` shows the study correcting itself in public, and `demographics.png` is a real chart nothing in v2 uses. A study is evidenced by its instruments and its corrections, not by pictures of pages. Worth arguing about with her rather than deciding alone.

---

## JOB THREE. Corrections and open items on v2.

- [ ] **Syllabus Checker still owes a captured run.** It is the only tool page without a real artifact. Run one of her own syllabi through `/syllabus-checker/` and build `syllabus-checker/report-sample.html` modelled on `course-dialer/report-sample.html`. About an hour, and it is the highest-value gap left.
- [ ] **`v2/build/index.html` is now unlinked** after the dead-end &ldquo;Live tool&rdquo; tab was removed. Michelle deletes it in Finder or leaves it. Claude does not delete files.
- [ ] **The `og:image` is still a stand-in.** Every v2 page points at `course-dialer/cover.png`. Needs a real 1200x630 PNG. Affects how a shared link looks, nothing else. Shippable without it.
- [ ] **A screenshot of `sample-agent/`** once it is pushed. It currently uses an SVG cover built on the agent&rsquo;s own palette, which is fine but a real capture is better.
- [ ] **Vet the four research candidates** quarantined at the bottom of `tools/reference/AUTHENTIC_ASSESSMENT.md`.
- [ ] Still open from before: split `TASKS.md` into live list and FEP evidence, move the zone map into `CLAUDE.md`, build the morning brain-dump skill.

---

## PROMOTION DAY, when she says go

Not yet. When she does:

1. Strip `noindex` from every v2 page.
2. Move `v2/` up to the repo root.
3. Strip the `/v2/` prefix from every href.
4. Leave a redirect stub at `course-dialer/` pointing to `dial/`. **`cultivate/cv.html` links `course-dialer/overview.html` and that CV is in 25 sent applications.**
5. **Never delete v1.** Thirty-five top-level directories are live GitHub Pages URLs, on her resume and in things already sent.
6. In `tools/design-lint.py`, delete v1&rsquo;s leniency rather than loosening anything in `v2-lint.py`.

---

## STATE OF PLAY, what was finished 30 August

**Fixed, verified, preflight green:**

- **The askbar was dead.** v2 copied the hero widget markup but not its script, so `abSubmit` was undefined and the first interactive element on the page threw a ReferenceError, on a page headlined &ldquo;I build AI tools.&rdquo; Now `v2/assets/askbar.js`, external so it cannot be lost in a copy again. Its 25K answer bank was checked against every guardrail in `CLAUDE.md` and is clean.
- **A fabricated claim was removed from `about.html`, v1 and v2.** It said the data showed a vocabulary quiz was not discriminating, so it was replaced with an applied task and re-checked the next term. **None of that happened.** What the files actually say is that AVC 100 has two vocabulary quizzes, they are the only AI-vulnerable assessments in the course, they were corrupted at the QTI level, nobody noticed for a term, and the plan is to rebuild them as multiple choice. **That true version is a better story and Michelle should decide whether to write it.**
- **Seat Time said &ldquo;specified but not built.&rdquo; It is built.** `course-dialer/workload.html` runs against AVC 100 with seven course profiles. Status corrected and the missing live-tool link added.
- **The round trip was documented nowhere.** Dial does not just report: it writes approved changes back into the package and repackages the cartridge for reimport, entirely in the browser tab, and it refuses to write a package it did not read. Now on the front page, the overview, the tool landing page, and the Quality page.
- Campground was &ldquo;not built yet&rdquo; on the front page and &ldquo;built and used&rdquo; on its own pages. It ran daily for a month across a Yosemite trip. Corrected everywhere, along with the 8am versus 10:16 and one-versus-seven contradictions.
- Six tool pages had Goal/Audience/Process prose and no artifact. Prose moved up to the overviews; each page now carries a real artifact: the 28-finding scoreboard, twelve palette swatches, the seven workload profiles, five built simulations, the OER licence record, the syllabus standards table.
- Dial overview is now 996 words, Build 767, both next to `render/overview.html` at 911, and both carry Goal, Audience, Process, Tools, Outcomes, Status, an evidence group, and the PRDs.
- Eleven smaller text errors: &ldquo;Tool 5 of 6&rdquo; against a suite that no longer exists, both Build tools parented to Dial, a missing sibling tab, one SVG with two alt texts, an alt claiming 50 tasks when the CV says 46, stale section names, &ldquo;entirely from OER,&rdquo; &ldquo;Strava mileage&rdquo; when Strava is simulated, the lowest-success superlative, five uses of &ldquo;prototype,&rdquo; and the PRD tab that renamed itself when clicked.
- Status now appears on all eight Dial, Build, Render and CopaMigo cards.

**Still true and unchanged:** run `python3 tools/preflight.py` and paste the output before calling anything done. Never run git. Never give Michelle Terminal instructions.

---
---

# Portfolio, the plan

**The entire website is the portfolio.** Everything linked from `index.html` is part of it.
This is the one planning file for all of it. Do not split it into per-project markdowns.

**Structure of this file:** the active plan first, reference material below it.

**Pruned 30 Aug 2026.** Roughly 1,300 lines were cut: the Mines portfolio audit and gap-fill
plan (that role was turned down), the EAB pre-send checklist (those fixes shipped 17 Aug and
`tools/preflight.py` now does that job), the July 4 site map and portfolio index (stale, and
the linter covers it), the July learning-design gap plan, the Home vs Work redundancy note,
and an old homepage summary draft. Nothing below is dead.

---
# PORTFOLIO v2, design notes captured 30 Aug 2026

**Goal.** Get her read as a **builder**, not as faculty, within the first line of the page.

**The real problem, in her words 30 Aug:** *&ldquo;the agents said I&rsquo;m not getting these jobs, my job title is faculty, not builder, so I have to show myself as a builder first and foremost.&rdquo;* And: *&ldquo;I send people to this site and they get overwhelmed and don&rsquo;t know what they&rsquo;re looking at, so they click around and never dig deep unless I send them to a specific project.&rdquo;*

**Those are one problem, not two.** The overwhelm is the symptom. The mis-categorization is the disease. A front page that is a pile of projects still makes the reader *infer* &ldquo;builder&rdquo; from the evidence, and a reader who already has &ldquo;faculty&rdquo; in their head will not do that work. **The page has to assert it in the first line and then prove it.**

**The priority stack, set by her 30 Aug:**

1. **AI. First priority, not negotiable.**
2. **Higher education, as the DOMAIN, not as the identity.** She knows this sector cold, which is an asset to an EdTech company. It is not who she is on this page.
3. **The work outside teaching classes.** Teaching is the job everyone already assumes. The portfolio exists to show what she built on top of it.

**The line that inverts the read:** she builds AI tools, and her domain happens to be higher education. Not: she is a professor who also builds things. Same facts, opposite conclusion.

**What this rules out.** Do not open with a title, a college, or a course list. Do not let &ldquo;Residential Faculty&rdquo; be the first noun on the page. It belongs on About and on the resume, where the context helps.

**What this demands.** Every project entry leads with a builder verb and a shipped object, and carries evidence that real people used it. Usability tested with students in March 2026. 100+ verified URLs. A ten-college study. A prototype that went to pilot. Those are builder artifacts. &ldquo;Taught,&rdquo; &ldquo;advised,&rdquo; and &ldquo;coordinated&rdquo; are not, however true they are.

**Audience.** Two readers, in priority order. **(1)** A screening agent or recruiter at a large EdTech company hiring an AI builder or prototyper. **(2)** A college hiring committee for a learning-experience-design role. Reader 1 is the target. Reader 2 is the fallback and must not be allowed to blur reader 1.

**Process.** Build the new portfolio alongside the current one in an unpublished directory. Switch over when it is finished. Never move or rename a directory that already has a live URL.

---

## The decision made 30 Aug: build alongside, do not rework in place

35 top-level directories are live GitHub Pages URLs, some of them on her resume and in things she has already sent. The current site keeps running and stays untouched. v2 gets built in its own directory, out of the nav, and goes live as one switch.

**The site-wide nav and footer consistency pass is PARKED until this decision resolves.** Findings are already recorded (82 pages with a redundant Home link in the nav, 84 in the footer, 11 with a nonstandard footer, one course page missing its Courses link, and a linter regex that silently skips 153 pages). If v2 replaces those pages, most of that work evaporates. Fix it in the v2 template instead, once.

---

## What the two readers actually do

Reader 1, the screening agent, is pattern matching in well under a minute for: **did this person ship AI things, what were they, and is there evidence they worked.** It is not reading prose. What defeats it is a landing page that requires reading to work out what she does.

Reader 2, the college committee, wants pedagogy, evidence of student impact, and institutional credibility.

**The current front page shows 29 cards at once.** That is a directory, not a portfolio. It hands both readers the sorting problem instead of solving it.

---

## The main disagreement, worth arguing about

Her proposed categories are **Course assessment and building / Student success / Job search and workforce / Agents / Experiential learning**.

That is an org chart of her own domains. It is how she thinks about her work, and it is not how either reader thinks. A hiring reader does not care about her taxonomy, and "Agents" as a category is a technology label, not a thing anyone is looking for.

**Recommended instead: a short flat set of named products, under one thesis line.** Five to seven items, each with a name, one line on what it does and who it is for, and an honest status. A screener scans names and one-liners, then clicks the one that matches the job description. Categories earn their place only past roughly eight items, and then three at most.

If categories stay, organize by **the problem solved**, not by her internal grouping. "Tools that cut the work of designing a course." "Tools that get students to the help they need." That is language the reader already has.

---

## The single biggest point: Dial Your Course is ONE card, not six

Her architecture insight is good product thinking and it should be built. **But it is a product decision, not a portfolio decision.**

Six front-page entries reading "Dial part 1" through "Dial part 6" does the opposite of what she wants. "Dial part 4" is a filename, not a name. Six cards for one product makes it look like she had one idea and split it six ways, and it buries the actual achievement, which is that she designed a **suite where each tool stands alone or chains into the next.**

**One card. "Dial Your Course, a six-tool suite for course design."** The six tools are listed inside the case study, each with a real name. Names, not part numbers:

- **Syllabus Builder**
- **Standards Check**, OSCQR, Bloom's, RSI, and the strategies course
- **Style Guide**, the palette and Canvas-safe HTML generator, already built and in daily use
- **Seat Time Meter**
- **Authentic Assessment**, described by her as the big one and the most valuable, not yet built out
- **OER Finder**, locate open materials for thin modules, with export to an OER repository

---

## The product architecture she described, captured for the PRD

Not a portfolio question, but do not lose it.

- Upload an entire course and run all six tools, **or** run any one tool standalone.
- Chaining: either check every tool at the start, or finish one and be offered the next.
- **Cadence differs by tool.** Syllabus, seat time, style and standards are start-of-semester, run once. **Authentic Assessment is the one she would return to weekly**, taking the module she is about to teach and asking what would improve it. Design for that difference rather than treating all six the same.
- Bloom's verbs probably belong inside Authentic Assessment rather than as their own step.
- **Open question:** the same framework could build a course from scratch, not only assess an existing one. That is likely a different product shape, not a seventh tool. Decide before building.

---

## AI or learning experience design: commit, then add a lens

She said it plainly: **"really I want this to be an AI portfolio, I just threw in learning experience for that one job."** So commit to that, and stop hedging on the landing page.

**Do not build two front doors.** Two landing pages means two things to maintain, they drift, and a reader who finds the wrong one gets the wrong impression. Worse, hedging reads as not knowing what you are.

**One landing page with an AI thesis, and a secondary path for reader 2.** The same projects carry a learning-design framing that a filter or a single "For learning design roles" link surfaces. Same evidence, two readings, half the maintenance. Render is an AI tool AND a piece of learning experience design. It does not need to live twice.

---

## Where the non-AI work goes

Internships, The Traveler, the Design Studio, the GCC Cares Hub, and STEAMworks are her deepest and longest credential, and the awards are real.

**They do not belong on the landing page as a peer to the AI work.** A section captioned "this section is not AI" on an AI portfolio actively dilutes the thesis, and it is the first thing a screening agent will use to mis-sort her.

Put them below the fold as **Teaching and program leadership**, or on the About page. They are what makes her credible to reader 2 and they are what proves she has shipped things that outlasted her, but they are not the headline.

---

## Depth over breadth, and status honesty

Everything she has built is a prototype or in testing. **A grid of twelve prototypes reads as a person who does not finish things.** Three or four projects presented with real depth (the problem, the process, what testing showed, the honest status) beat twelve thin cards for both readers.

Suggested flagships: **Render**, **CopaMigo**, **Dial Your Course**, and the **ARC student journey study** as the research credential.

Everything else becomes a compact "also built" list. That list still does useful work, it shows she builds constantly, but it does not have to compete for attention.

---

## Push back on including these at all

The **family job agents** (Kevin, Devan, Jasper, Jillian) and the **campground search tool** are not EdTech and not AI-for-education. On a portfolio aimed at reader 1 they dilute. They do show range and a real building habit, so one honest line in the "also built" list is right. A category called "Agents" that mixes Wayfinder with a campground finder is not.

---

## Open questions for Michelle

1. Is Dial Your Course one product or six, **commercially**? The answer settles the portfolio question too.
2. Which three projects are the flagships? Recommendation above, needs her confirmation.
3. Does Wayfinder belong in the professional set, or in "also built"?
4. Does the campground tool get pulled out as its own tool, and if so, is it on this site at all?
5. What is the one-sentence thesis at the top of the landing page? Everything else follows from it, and nobody but her can write it.


---

## The front page has ONE job: routing

Her own evidence: *&ldquo;they never dig deep unless I send them to a specific project.&rdquo;* The deep pages work. The front page does not. So stop asking it to showcase and make it route.

Three to five doors. Each one obviously different from the others. Each leading to a case study that stands alone, because the pattern that already works is her sending someone a direct link. Design for that instead of against it: every project page should read correctly as the first page someone sees, with no dependency on the landing page for context.

29 cards is not a portfolio. It is a directory, and it hands the reader the sorting problem she is trying to solve for them.

---

## Student success is the right cluster, and for a better reason than she thinks

She asked whether anything else can be linked to student success. It can, and it is worth doing, but not because it fills a category.

**&ldquo;Student success&rdquo; is the product category EdTech companies actually sell.** EAB, Civitas, Element451, Anthology and the rest organize their entire businesses around that phrase. Naming that cluster in their language means reader 1 recognizes the shape of her work immediately, without translation.

What belongs in it: **CopaMigo** (routing students to campus services), the **ARC student journey study** (the research underneath it), **Render** (career services is student success), the **AVC100 redesign** (a student success module inside every course module, tied to institutional learning outcomes), and the **GCC Cares Hub** identity work on basic needs.

That is a genuine, coherent body of work in exactly the vocabulary the target employer uses. It may be the strongest single cluster she has.

---

## The highest-value action is not the portfolio. It is getting CopaMigo to pilot.

Every project she has is a prototype. The one thing her positioning lacks is **something real people used in production**, and that is the precise gap a screener reads as &ldquo;faculty who tinkers&rdquo; rather than &ldquo;builder.&rdquo;

A CopaMigo pilot answers that in a way no page layout can. **The Maricopa AI CIO has already asked to see it.** That is the lever, and it is already in her hand.

**Questions to settle before pushing for it:**

- What does &ldquo;pilot&rdquo; mean concretely: how many students, over what period, at which college, and who owns it operationally?
- What does she need to have said yes before it can start, and who says it?
- What gets measured? Even a small number that can be stated publicly changes the portfolio entry from &ldquo;prototype&rdquo; to evidence.
- The data-governance answer is already her strongest card. No student data, no PII. The district declined a vendor AI add-on specifically over student data collection, which makes a data-sovereign campus-built tool the easy yes.

**Sequencing note.** A portfolio rebuilt now says &ldquo;prototype&rdquo; five times. The same portfolio rebuilt after a pilot starts says &ldquo;in pilot at a 10-college district.&rdquo; If both cannot happen at once, the pilot is worth more.


---

## Structure, video, and sequencing. Decided 30 Aug 2026.

### Read by the two target readers

| | EdTech screener, AI builder role | College committee, LXD and leadership |
| --- | --- | --- |
| Watches video? | **No.** Skims, decides in under a minute. | **Yes.** It is the strongest asset for this reader. |
| What lands | A six-tool suite. A national fellowship capstone. Two tools in live pilot with real students. | League Fellow. ARC domain co-chair. A ten-college study. A tool the district CIO asked to see. |
| What loses them | Having to sit through CopaMigo to reach Render. | Prototypes with no evidence anyone used them. |

They diverge only on video. They agree on everything else.

### Video: four, not twelve, and NOT one per section

**Section-level videos serve her narrative, not the viewer&rsquo;s task.** A section video covering CopaMigo and the journey study bundles a tool with a research study. Grouping the family job agents at the end &ldquo;because they all started from the same idea&rdquo; is her logic, not a viewer need.

- **One front-page video, 2 to 3 minutes: her demoing Dial Your Course.** This is the builder proof. A person demoing software they built cannot be mistaken for faculty who only teaches, and the thumbnail alone does that work.
- **One embedded in each flagship overview page:** Render, CopaMigo, ARC study. For the reader who already clicked and wants depth.
- **Nothing for the &ldquo;also built&rdquo; items.**

Four videos is less work than section videos done properly, and it serves both readers instead of splitting the difference.

### Layout: do not redesign the grid

The problem is quantity, not the visual system. Keep the existing card design. Change what is on the page and how much of it shows at once.

- One section visible at a time, the current card style retained.
- A large feature slot (the video) with smaller project cards beside it.
- **Land on Dial Your Course.** Correct for both readers, it is the most complete and most product-shaped work.

**Three sentences per section is not too much, IF they are claims and not descriptions.** The test: could a reader skip every card in the section and still know what the section proves? If yes, the summary earns its place. If it only introduces, cut it.

### CORRECTION to the earlier note on teaching and leadership

The earlier note said put teaching and program leadership below the fold. **That is right for &ldquo;builder&rdquo; and wrong for &ldquo;leader,&rdquo;** which she added to the brief on 30 Aug.

**Resolution: not a section, a credential strip near the top.** Four lines, no more.

- League for Innovation Fellow, capstone publishing nationally
- ARC Student Support and Success domain co-chair
- Founded the GCC AI community of practice
- DMA Program Director, 2011 to 2022

Third-party validation is the most direct counter to &ldquo;faculty, not builder,&rdquo; and the current site buries all of it by filing it as teaching. **The League capstone in particular belongs on the front page.** National publication is external validation she already has and does not show.

### SEQUENCING. The most important decision here.

Her own words, 30 Aug: *&ldquo;everything else is half assed right now.&rdquo;* She is right, and the fall load is the reason.

Fall 2026 commitments: two class pilots (CopaMigo and Render, across the current class and the late-start class beginning end of September), the League for Innovation capstone which must be bulletproof and has to publish nationally, a portfolio rebuild, an active job search, the FEP due 30 June, four courses, and an ARC domain co-chairship.

**The portfolio is the item that waits.** The pilots and the capstone *generate the content the portfolio needs.* Building it now means writing &ldquo;prototype&rdquo; five times and then rebuilding it in January.

- **Fall:** pilots and capstone.
- **Winter break:** portfolio v2, with &ldquo;piloted across two classes&rdquo; and &ldquo;published nationally through League for Innovation&rdquo; in it.

### The pilot plan, captured 30 Aug

If Claude or Gemini access lands within a week, she can run **CopaMigo and Render simultaneously across two classes**: the currently running section and the late-start section beginning end of September. Two tools, two cohorts, one semester. That is the single highest-value thing on this list, because it is the only thing that converts every &ldquo;prototype&rdquo; label into evidence.

**Still to settle:** what gets measured, what she can state publicly afterward, and the consent language, which has to be in front of students at the start of the semester and not in December.

---

## Dial Your Course walkthrough, script. Drafted 30 Aug 2026.

**Goal.** Show a viewer that a real course goes in and real fixes come back, and that Michelle built the thing doing it.

**Audience.** Someone who already clicked into the Course Design and Quality section. Not a cold visitor. The cold visitor gets the &ldquo;how I work with agents&rdquo; interview on the front page instead.

**Process.** Do NOT give six tools thirty seconds each. Six equal segments is a product manual and nobody finishes it. Open on the problem, run **one real course** end to end, go deep on two tools, name the rest as they fire. **Six to seven minutes.** Three was never going to hold this.

### The structural point that has to land

**Four of the six tools contain no AI.** They are rule-based checks against a published standard. Only Authentic Assessment and OER Finder use a model. Say this out loud, early. It is a credibility asset with two different audiences: a district that is cautious about AI hears &ldquo;this is mostly deterministic checking,&rdquo; and an EdTech employer hears someone who knows when not to reach for a model. Burying it wastes it.

**OSCQR has to be named in the first ninety seconds.** It is the standard her college uses and for anyone in the field it is the credential of the whole tool. **Say in the same breath that the tool is not hard-wired to it.** Point it at whichever rubric an institution uses. That is what makes it a product rather than one college’s internal script.

### The script

**0:00 to 0:45, the problem.** Every online course has to clear a quality bar. At her college that standard is OSCQR, plus seat time, accessibility, and regular substantive interaction. Do not say the whole district uses it. A faculty member checks it by hand against a rubric they have probably never read, or does not check it at all. On camera: the actual OSCQR rubric. Say the number of items out loud.

**0:45 to 1:15, what this is.** Six tools. A Canvas export goes in, what to fix comes back. Run one tool or chain all six. **State the AI line here.** Four are rule-based. Two use a model. Say why that was the right call.

**1:15 to 2:45, tool in depth, Standards Check.** Upload a real course export. Watch it run against OSCQR. Show a real finding on a real module, not a demo file. Show a fix being made. **This is the segment that proves the tool works, so give it the time.**

**2:45 to 4:15, tool in depth, Authentic Assessment.** The one that matters most and is the least finished, so be honest about state on camera. Take a module with a take-home essay and show what comes back. This is where the model earns its place, and where the pitch is: the goal is converting a colleague who has always assigned papers and multiple-choice tests.

**4:15 to 5:30, the other four, fast.** Syllabus Builder, Style Guide, Seat Time Meter, and the Open Educational Resources finder. Fifteen to twenty seconds each, named as they fire in the chain, not explained. The chain running is the point, not each tool.

**5:30 to 6:15, what comes out.** The report. What a faculty member does Monday morning with it. Name honestly what is built and what is not.

**6:15 to 6:45, close.** One line on where it goes: League for Innovation capstone, publishing nationally. No credential recital, the work carries it.

### Production notes

- Screen recording with voice over, not a talking head. The tool is the subject.
- Use a real course, hers, with a real finding. A clean demo file reads as a mockup.
- Cut a **60 to 90 second version for LinkedIn** from the Standards Check segment. Same shoot.
- Never say &ldquo;AI-powered&rdquo; about the whole suite. It is four-sixths not.


---
---

# REFERENCE, not the plan

Raw material for pages that have not been built yet. Kept because it would be expensive to
reconstruct, not because it is active work.

## ⛔ HARD RULE: NO DATES ON THE PORTFOLIO. NONE.

**Not career dates, not project years, not "recently," not "seven years ago."** Every year was
stripped from this site on purpose, for age-discrimination reasons, and that includes the
studio work. Do not re-litigate this.

**The consequence, and accept it:** every piece has to stand undated. There is no "be kind, it
is old." If the work is good it stays; if it is not, it comes off. That is the cleaner standard.

(The old history, the reusable learning objects and the 3D computer build, is INTERVIEW
material, spoken, undated. It never goes on the site.)

---

## What we found tonight, and why it matters

Michelle has been running a **design studio** with real campus clients for over a decade,
and running **faculty-SME builds with students** for over two. It is the most complete
evidence in the portfolio that she can take something from nothing to a shipped artifact
with a measurable outcome, and almost none of it is on the site.

**This is not the AI story. It is the reason the AI story is believable.** The AI tools are
prototypes with pending evidence. The studio is a finished arc with national awards. One
makes the other credible.

**Placement: it stays under Experiential learning. It does NOT move to the front.** The
homepage stays AI tools, the ARC study, and the authentic-assessment thesis. Nobody should
land on the site and think "community college art professor." But when someone asks
"have you actually run anything to completion," this is the page.

---

## The evidence log (everything discovered, so it does not evaporate)

### The studio model
- Every project runs with a **student Project Manager** who writes the **design brief**,
  owns the **timeline**, and keeps the project moving. The same model runs The Traveler.
- Projects run in **Basecamp, Slack, Miro, and Discord**. Real tooling, not a class folder.
- Briefs include: client, goal, approach, client-needs list, team roster with roles,
  and a **timeline with client proof cycles, approval gates, and deliberate buffer**.
- The studio grew **out of a course**. The course did real client work, the work made the
  case, and it earned a grant. It now **pays students**. (NEED: the grant start date.)

### Client list (the campus is the client base)
| Client | Deliverable | Have? |
|---|---|---|
| Open Educational Resources Committee | Silent animated explainer, web + Gaucho TV | ✅ video live, Miro board (NEEDS REDACTION) |
| The Traveler, 60th Anniversary Edition | Print literary magazine, full design system | ✅ Miro board + PDF (NEEDS REDACTION) |
| Healthcare Technology Systems | Program promo video | Link: `FSYG0sOkd1w` |
| STEAM program | Motion bumper | Link: `zXuNyr9B4uU` |
| Fitness and Wellness | Mobile app, cross-disciplinary build | Link: `eYzRaS1Vjsk` |
| International Education Center | Onboarding booklet + presentation | ✅ brief .docx + .pptx |
| Aquatics | 90-foot mural | ✅ Instagram, need a clean photo |
| Science Olympiad | Apparel, multiple years | NEED PHOTO |
| Odyssey of the Mind | Apparel | NEED PHOTO |
| Astronomy Festival | Commemorative pin | **NEED PHOTO. Pin is in her desk at work. Ask Kevin to shoot it.** |
| The Library | Illustrated Harry Potter map, Halloween | NEED FILE |
| Theatre and Dance | Play and show posters | NEED FILES |
| ~~Digital Media Arts~~ | ~~Program promo~~ | **OUT. She flinched at it. 7 years old.** |

### The Traveler, 60th Anniversary Edition (the flagship)
The one project with a complete arc AND a measured outcome.

- **Concept:** each chapter is a decade of GCC, rendered in that decade's design language.
  A running timeline across the front and back covers.
- **Design system:** consistent grid (3 columns), body type held constant, an icon library
  built in Illustrator, and **GCC Red (#CB3338) pulled from the official college web style
  guide**, held constant across every decade's palette.
- **Ownership:** each decade assigned to a named student designer.
- **Primary research:** the students wrote their own **alumni questionnaire** (favorite class,
  cost of coffee, how you got to campus, what you wore).
- **Archival research:** the college librarian, the GCC library archive, the **Arizona Memory
  Project**, the college Flickr.
- **Sourced facts:** decade facts cited to the Bureau of Labor Statistics, the US Department
  of Energy, the National Center for Education Statistics.
- **Executive stakeholder:** *"1/27 · Be prepared to present concept to the GCC President."*
  *"3/4 · Book goes to President for final approval."*
- **Real production:** printer quotes, purchase order requested from the district office,
  book delivered to campus offices.
- **PM instinct, from a student:** *"This is subject to change, I have padded the deadline a little."*
- **OUTCOME: three Pinnacle Awards, College Media Association.** National.

### The OER promo (the best process artifact)
- **Team roles:** Advisor, Project Manager, Video Assembly, Characters, Animator.
- **Stakeholders:** OER Committee chair, former chair, and the college marketing director.
- **Goal (their words):** educate students and faculty on OER, where to find those classes in
  Find a Class, and the fact that they save students money.
- **Deliverables:** 30-second animated video for **Gaucho TV** (student union and library),
  Instagram Reels, GCC news page.
- **THE CONSTRAINT that makes it a design problem: Gaucho TV screens have no sound.** It had
  to be understood by someone walking past, audio off, not planning to pay attention.
- **Pre-production bible:** hand-drawn storyboards, character design sheets, **animation
  rigging notes** (limbs to duplicate and rig, eyes with pupils separate from whites, a set
  of rotatable mouths), scene-by-scene event sequence, mood board, **scene-by-scene audio plan**.
- **Typography rationale: Roboto, because the GCC web style guide specifies it.** They linked
  the Maricopa brand guide to prove it. Then explored five display faces for the headline.
- **The fact, from their own script:** *"Open Maricopa, formerly Maricopa Millions, has saved
  students over $36 million in textbook costs from 2013 to 2023."*

### The deep history (goes in her MOUTH, not on the site)
As **Director of Instructional Technology**, she ran student interns building **reusable
learning objects** with a **business and information technology faculty member as the
subject-matter expert**, meeting weekly, producing interactive objects faculty dropped into
Blackboard. **One was a 3D model of a computer that an online student had to assemble.**

**That is the simulation-as-assessment thesis, built before the tooling existed.** An online
student who cannot touch the hardware, performing the task in a browser, where the artifact
IS the evidence. Same structure as the Mines engineering simulation. Same faculty-SME model.

**DO NOT PUT A YEAR ON THIS, ANYWHERE ON THE SITE.** Every date was stripped from the site on
purpose, for age-discrimination reasons. This is interview material, spoken, undated:

> *"Because I built one. An online student assembling a computer from a 3D model, with a
> faculty SME supplying the content. The idea was right and the tooling wasn't. It is now."*

---

## ⛔ REDACTION LIST, do this BEFORE any export is published

**The Miro boards contain other people's private information. This is the hard stop.**

1. **OER board, stakeholder block: THREE COLLEAGUES' FULL NAMES AND WORK EMAIL ADDRESSES.**
   Delete entirely. Replace with titles only: "OER Committee chair, former chair, and the
   college marketing director."
2. **Team rosters: roles only.** Advisor, Project Manager, Video Assembly, Characters,
   Animator. The roles are the interesting part. Strip the names.
3. **Traveler board: decade assignments name five students in full.** Strip.
4. **Dot-voting legends** name students. Strip or crop.
5. **Collaborator avatars and comment bubbles** show student faces. Turn off cursors and
   avatars before exporting, or crop.
6. **Internal Google Drive links.** Remove.

The redacted board loses **nothing** that makes it impressive. Every role, timeline, goal,
storyboard, rigging note, color rationale, and audio plan survives.

---

## THE TO-DO LIST

### Before Wednesday: NOTHING. Site is frozen.
Mines closes Wednesday. Tommy is Wednesday at 3:00 PM. Do not touch the live site.
(The one edit already made: the OER video is embedded on `murals/overview.html` under
"Selected client work," with the $36M figure correctly attributed to Open Maricopa. That is
done, it is safe, and it is finished.)

### Thursday, phase 1 · Redact and export (1 hour)
- [ ] Redact both Miro boards per the list above
- [ ] Export **full board as JPG** (~2000px, quality 85). It is a texture, not a document.
- [ ] Export **detail crops as PNG** (readable): storyboard, character rigging, event
      sequence, color and type
- [ ] Save to `/assets/studio/`

### Thursday, phase 2 · Rebuild the page (2 hours)
- [ ] **Rename the page.** "Murals and client projects" undersells it. It is a **studio**.
- [ ] Restructure to Goal / Audience / Process (the site rule), then **Selected client work**
- [ ] **Lead with The Traveler 60th.** It is the only complete arc with a national outcome.
- [ ] OER promo second (best process artifact, live video, strongest constraint)
- [ ] Then Healthcare Technology, STEAM, Fitness app (dated, framed as the course that
      preceded the studio)
- [ ] **The method section is the point:** student PM, written brief, client proof cycle,
      approval gate, delivery. Show the International brief as the artifact.
- [ ] Keep the **mural photo as the card thumbnail on `work.html`.** It is still the strongest
      image on the site and it earns the click.

### Thursday, phase 3 · The flythrough video (this IS the After Effects video, task #9)
- [ ] Camera move through the redacted Traveler board. Pull back for scale, drop into the
      storyboards, the icon library, the timeline.
- [ ] Doubles as the process reel, the portfolio piece, and the AE teaching artifact. One file,
      three jobs.

### Whenever · Photo shot list
- [ ] **Astronomy pin** (Kevin, macro, one clean hero shot). It is in her desk at work.
- [ ] Science Olympiad and Odyssey of the Mind shirts (flat lay, or find the original art)
- [ ] Harry Potter library map (does the file still exist? ask the library)
- [ ] Theatre and dance posters (originals are almost certainly in a class folder)
- [ ] Fitness app screens (stills pulled from the video will do)
- [ ] A clean photo of the 90-foot mural (currently only on Instagram)

### Open questions for Michelle
- [ ] **When did the Design Studio grant start?** This is the hinge date. Everything before it
      is "a course doing real client work." Everything after is "a funded studio that pays
      students." Two different sentences.
- [ ] Roughly what years does the client work span, and which course produced it?
- [ ] Are there more briefs in Basecamp and Slack? **Two or three across different years beats
      twenty.** It shows the method held, not that one class got lucky.

---

## The line that changes the pitch

She has been saying **"I have no formal PM experience"** for months. Tonight, three separate
things contradicted it:

1. She has run client projects with a **written brief, a project manager, a timeline, client
   approval gates, and a handoff since at least 2014.**
2. She ran them in **Basecamp, Slack, and Miro**, which are on half the UX and product job
   descriptions she has been told she is not qualified for.
3. She **built the structure that teaches students to manage projects**, and then got out of
   the way.

And it maps cleanly onto what she is studying for the **CSPO**:
- **She is the Product Owner.** She owns what gets built, in what order, and whether it
  delivered value.
- **The student PM is the delivery role.** Runs the process, holds the timeline, clears
  blockers.
- **The campus office is the stakeholder.**

**She has been running a Scrum-shaped studio for twelve years without the vocabulary.** The
CSPO is not her learning something new. It is her getting the words for something she already
does.

Precision matters here: **this is not the same as being a product manager at a software
company, and she must not claim it is.** But "I have no PM experience" is false, and she has
been saying it to herself for months.

---

## From `portfolio/STUDIO_ASSETS.md`

# Design Studio, asset register

**The one place every studio link lives.** Nothing else is organized, so this file is the
source of truth. Add to it the moment you find something. Do not let links live in chat.

**HARD RULE: no dates anywhere on the portfolio.** Not career dates, not project years.
Every piece stands undated. See `STUDIO_PLAN.md`.

---

## VIDEOS (YouTube)

| Project | Client | Link | On the page? | Notes |
|---|---|---|---|---|
| **OER / Open Maricopa explainer** | OER Committee | `https://www.youtube.com/watch?v=u-uAOc10H8c` | ✅ **embedded** | Silent by design, built for sound-off Gaucho TV. Miro board exists (NEEDS REDACTION). |
| **A day in the life** | DMA recruitment | `https://www.youtube.com/watch?v=nOkNWzAYu6o` | ✅ **embedded** | Live action + hand-drawn animation. Narrated, subtitles burned in by hand. Michelle: "the best project in there." |
| **Healthcare Technology Systems promo** | HCT program | `https://youtu.be/FSYG0sOkd1w` | ❌ not yet | Need: what's in it, what makes it good. |
| **STEAM bumper** | STEAM program | `https://www.youtube.com/watch?v=zXuNyr9B4uU` | ❌ not yet | Bumper, different deliverable type. Good for showing range. |
| **Fitness and Wellness app** | Fitness + Wellness / personal training | `https://www.youtube.com/watch?v=eYzRaS1Vjsk` | ❌ not yet | **Cross-disciplinary.** Personal-training students were the SMEs and demoed correct form on camera; DMA students built the interface. Output: a custom exercise program for a real client. **This is the faculty-SME partnership model, long before AI.** Lead with the MODEL, not the UI. |

**How to get the script off a video with burned-in subtitles:** download the MP4 (YouTube
Studio → Content → three dots → Download), drop it in the folder, and Claude can pull one
frame per second and read the subtitles off the images. No speech-to-text needed. Claude
cannot watch video or hear audio, and cannot fetch YouTube.

---

## MIRO BOARDS

| Board | Link | Status |
|---|---|---|
| **Traveler 2025 brainstorming** (60th Anniversary Edition) | `https://miro.com/app/board/uXjVKoz8fC0=/` | ⛔ **REDACT BEFORE EXPORT.** PDF exported, not yet placed. |
| **OER video promo** | `https://miro.com/app/board/uXjVIFSgrQo=/` | ⛔ **REDACT BEFORE EXPORT.** |

**⛔ REDACTION, before a single frame is captured:**
1. **OER board: THREE COLLEAGUES' FULL NAMES AND WORK EMAIL ADDRESSES** in the stakeholder
   block. Delete. Replace with titles: "OER Committee chair, former chair, and the college
   marketing director."
2. Team rosters → **roles only** (Advisor, Project Manager, Video Assembly, Characters, Animator).
3. Traveler board → the five decade assignments name students in full. Strip.
4. Dot-voting legends name students. Strip or crop.
5. Collaborator avatars and comment bubbles show student faces. Turn off before export.
6. Internal Google Drive links. Remove.

**Never link a Miro board from the portfolio.** They are behind auth and set to noindex, so a
hiring manager gets a login wall. Export to image and host it here.

**Export recipe:** full board as **JPG** (~2000px, it is a texture, nobody reads it) plus 4 to 6
**PNG** section crops that are actually readable. Save to `/assets/studio/`.

---

## DOCUMENTS AND ARTIFACTS

| Item | Where | Notes |
|---|---|---|
| **International Info Design brief** | uploaded `.docx` | **The proof the studio has a method.** Student-written: client, named project manager, team roster with roles, goal, approach, client-needs list, and TWO parallel timelines with client proof cycles, an approval gate at Student Life, and a deliberate week of buffer. |
| **International Student presentation** | uploaded `.pptx`, 27 slides | Onboarding for students whose failure modes are losing visa status or heatstroke. **Soccer field as the unifying metaphor**, because the audience shares no language. ⛔ **DO NOT PUBLISH THE SLIDES.** One slide instructs international students on washing their clothes. It will read as condescending. Describe the project, show the metaphor, not that slide. |
| **Pool mural** | `https://www.instagram.com/p/CWmHpjgsoxo/` | 90 feet. Still the strongest image on the site. **Keep as the `work.html` card thumbnail.** Need a clean photo, not an Instagram link. |

---

## NEEDS A PHOTO (the shot list)

- [ ] **Astronomy Festival commemorative pin.** It is in her desk at work. **Ask Kevin to shoot
      it** (macro, clean surface). It is the one item on this list that is a *product*, and it is
      the one somebody kept.
- [ ] Science Olympiad shirts (multiple years)
- [ ] Odyssey of the Mind shirts
- [ ] Harry Potter map, made for the library at Halloween. Does the file survive? Ask the library.
- [ ] Theatre and dance posters. Originals are almost certainly in a class folder.
- [ ] Fitness app screens (stills pulled from the video will do)
- [ ] A clean photo of the 90-foot mural

---

## 🎬 THE DOCUMENTARY (in progress, add when done)

**A student team in the Design Studio is producing a documentary about the making of The
Traveler.** ⚠️ **It is BY the studio, not about Michelle by an outside crew.** Do not write it
the other way. That would be an overclaim.

- [ ] Add it to `traveler/overview.html` when it is finished.
- [ ] Get the link, and the client (is the Traveler team the client, or is this self-directed?).
- **Why it is good:** it is another client brief, and the subject is the studio's own flagship.
  Students documenting the making of an award-winning publication is the method eating its own
  tail in the best way.

---

## 🔨 TOMORROW: FLESH OUT THE STUDIO PAGE (`/studio/overview.html`)

**The folder is now `/studio/`, not `/murals/`.** A few murals do not compete with the rest of
the work, and the URL was reading `michelleblomberg.com/murals/` on a page titled The Design
Studio.

**1. HERO = the redacted Miro board.** Not the mural.
The hero has to say what the page is about before anyone reads a word. The mural says *we paint
walls.* **A Miro board says: this is a studio with a process.** That is the argument of the
whole page. Illegibility is fine, even good: at hero size it reads as *texture*, as the sheer
density of thinking, and that IS the message. Readable crops go inside each project.
**The mural photo stays as the card thumbnail on `work.html`.** It earns the click. Different
jobs, no competition.

**2. GOAL / AUDIENCE / PROCESS are about the STUDIO, not the projects.**
Michelle got here herself: *"I guess I'm describing how students are working on stuff."* Exactly.
- **Goal** → what the studio is *for*: students leave with real client work, real references, and
  a portfolio piece, because **the assessment IS the professional task.** A client is waiting.
  You cannot fake it and you cannot paste it. **This is authentic assessment, and it has been
  running for a decade.** Link to `authentic-assessment/`.
- **Audience** → the students first, the campus clients second. That order is the tell that this
  is pedagogy and not a design firm.
- **Process** → the method: written brief, student project manager, client proof cycle, approval
  gate, handoff. Tracked in Basecamp, Slack, Miro, Discord.

**3. Each project gets a BIGGER description**, but NOT its own Goal/Audience/Process block.
Eleven redundant heading sets would bury the argument. Each project carries its client, its
deliverable, its constraint, and what made it hard.

**4. Two zones.**
- **Featured, with depth (3 max):** the OER explainer, the Fitness and Wellness app
  (cross-disciplinary, personal-training students as SMEs), and A Day in the Life.
  (**The Traveler gets its OWN page**, see the split below.)
- **More client work:** the `workgrid` component (already built, already on the page), small 16:9
  frames, one caption each. Healthcare Technology and the STEAM bumper are in. The mural, pin,
  shirts, map, and posters join once photographed.

---

## PAGE SPLIT (decided July 13)

**Do not put the Traveler Miro board on the Design Studio page.** The two pages have two jobs.

- **`traveler/overview.html`** → the **flagship case study.** Deep. The design system, the alumni
  questionnaire, the archival research, the presentation to the college president, the print
  purchase order, delivery, **three Pinnacle Awards**, the Traveler Miro board, and eventually
  the documentary. It is the only project in the whole portfolio with a complete arc AND a
  national outcome. Treat it that way.
- **`murals/overview.html` (The Design Studio)** → the **method page.** The point is not the
  individual project goals, it is **how the work runs**: the written brief, the student project
  manager, the client proof cycle, the approval gate, the handoff. Evidence: the **OER** and
  **Healthcare** Miro boards, the International brief, and the client-work grid.

**And the deeper argument for the Studio page:** this is **authentic assessment**, and it has
been running for a decade. The assessment IS the professional task. A real client is waiting,
the student has to defend the work, and no model can produce it for them. Link the page
directly to `authentic-assessment/` as its oldest evidence.

---

## STILL TO FIND / DECIDE

- [ ] **More project briefs** in Basecamp and Slack. **Two or three across different years beats
      twenty.** It shows the method held, not that one class got lucky.
- [ ] **When did the Design Studio grant start?** The hinge. Before it: a course doing real
      client work. After it: a funded studio that pays students. (Needed for the narrative, NOT
      for a date on the page.)
- [ ] Which course produced this work?
- [ ] Presentation for International Students Orientation, is there a file?

---

## From `portfolio/FIGMA_TRAVELER_SPEC.md`

# Figma build spec, The Traveler interactive

Written 17 Aug 2026, during the EAB Product Experience Designer application.
When Michelle says &ldquo;the Figma project,&rdquo; this is the file.

---

## Goal

Produce one public Figma file that proves visual craft, component thinking, and
prototyping ability, because that is the single gap standing between this
application and a clean advance. Both simulated reviewers on the EAB hiring panel
independently said the same thing: Figma is claimed in the packet and never shown,
and one real file flips their scores without further discussion.

## Audience

The EAB portfolio review, which happens after the phone screen. Specifically a
Principal Product Designer acting as a craft gate. Secondarily every future
design application, since this file fills the same hole everywhere.

## Process

Take the existing Traveler print brand, which already lives on a Miro board, and
derive a digital system from it: named styles, a component library with variants,
six screens, and a click-through prototype. Roughly four to five focused hours.

---

## Why The Traveler, and not CopaMigo

The posting says: *&ldquo;Build and maintain reusable prototype assets utilizing
EAB&rsquo;s design system, component libraries, and modern prototyping platforms.&rdquo;*

Read literally, the job is: **someone hands you a design language you did not
create, and you build assets inside it.** The Traveler rehearses exactly that task
with real source material. Designing CopaMigo in Figma would be working inside a
system Michelle already owns, which does not test the same skill, and the
portfolio already documents CopaMigo six different ways.

Three more reasons:

1. **It fixes the weakest score.** Visual design came in at 2.5, the lowest on the
   rubric. The whole portfolio is utilitarian tool UI in one plum-and-sage palette.
   The Traveler is art-directed editorial work.
2. **It carries third-party validation.** Pinnacle Award for College Literary
   Magazine (2015, 2016, 2025) and AIGA Best of Phoenix selections (2017 to 2022).
   Visual craft is the one thing that cannot be asserted into existence.
3. **It was already wanted.** An interactive Traveler has been on the list. This
   is not throwaway work.

### The authorship line, say it exactly this way

Michelle is the **design faculty advisor** and has been since 2011, Volumes 44 to 58.
She coaches the student design team through branding theme, design and typography,
print production, and launch. She has nothing to do with the editorial side or the
art competition.

So the framing is:

> The print brand is student work produced under my art direction across fifteen
> volumes. What I built here is the digital system derived from it: the component
> library, the responsive behaviour, and the interactive prototype.

Deriving a system from someone else&rsquo;s design language **is** the job description.
The authorship question is the story, not a risk.

---

## The build

### Page 1, Cover

Title, one line on what the file is, the role statement above, the source
(Volume NN print brand, Miro board), and the date.

### Page 2, Foundations

Pull real values off the Miro board. Do not invent any of these.

**Color styles**, named with slashes so they group into folders:

| Style name | Source |
|---|---|
| `ink` | body text colour from the volume palette |
| `paper` | background stock colour |
| `accent/primary` | the volume&rsquo;s lead accent |
| `accent/secondary` | the supporting accent |
| `rule` | hairline and divider colour |

**Text styles**, using the magazine&rsquo;s real typefaces:

`Display` · `Title` · `Byline` · `Body` · `Pull quote` · `Caption` · `Folio`

Add one short note per group saying **why**: why this face for body copy, why this
measure, why this leading. That annotation is what separates a designer from
someone who moved swatches around.

### Page 3, Components

This is the page that scores. Build each, then `Cmd+Option+K`.

| Component | Property and variants | Why it matters |
|---|---|---|
| **Piece card** | `type` = poem / prose / art | Three variants of one component is the highest-value object in the file |
| **Pull quote** | `align` = left / center | Type hierarchy thinking |
| **Figure** | `size` = inset / full-bleed | Editorial layout judgment |
| **Contributor card** | `state` = compact / expanded | Reusable pattern |
| **Masthead** | `mode` = issue / archive | Navigation treated as a component |

Lay them out in a tidy grid with a `Label` heading over each group. This page alone
is what a design-systems reviewer opens first.

### Page 4, Screens

Press **F**, draw frames at **390 × 844**. Six frames, a real literary magazine
information architecture:

1. **Issue landing.** Cover art, volume number, one line of invitation.
2. **Contents.** Piece cards, all three variants visible together.
3. **A poem.** The hard one, and the one to spend care on. Line breaks in poetry
   carry meaning, and responsive layout destroys them. Solving that on a 390px
   screen is a genuine craft demonstration.
4. **A prose piece.** With a pull quote and an inset figure.
5. **An artwork.** Full-bleed with caption, image-forward treatment.
6. **Contributors.** The card in both states.

Use components for everything. If you catch yourself drawing a card by hand, stop
and place the component instead.

### Page 5, Print to screen

Two frames side by side: a print spread from the Miro board, and the screen
translation. One sentence under each naming what had to change and why. This is the
before-and-after page, and reviewers weight it heavily because it proves
translation judgment rather than a first draft that happened to look fine.

### Prototype

Prototype tab. Wire 1 → 2 → 3 → 4 → 5 → 6, add a back arrow on each frame, set
**Device: iPhone 14**, press play and click all the way through. If it plays, done.

### Share

Share → **Anyone with the link** → **can view**. Copy the link. It goes in the
resume header and in the cover letter&rsquo;s prototype bullet. Ask Claude to rebuild
the application PDF afterward.

---

## What to be able to say about it

- &ldquo;Every colour and type value is a named style, so a change propagates.&rdquo;
- &ldquo;The piece card is one component with three variants, not three cards.&rdquo;
- &ldquo;The brand is student work I art-directed. The system derived from it is mine,
  and that is the same thing you would ask me to do inside EAB&rsquo;s library.&rdquo;
- &ldquo;The poem screen is where I started, because line breaks carry meaning and
  responsive layout destroys them.&rdquo;

## What would make it worse

Twenty screens at seventy percent. A craft gate grades this as design work, not as
proof you opened the app. Six careful frames and a real component page beat a big
messy file every time. Do not build it the night before, and do not hold the
application waiting for it.

---

---


---

## Wayfinder, what belongs inside it. Decided 30 Aug 2026.

**Wayfinder is one project with tabs, not several cards.** Its v2 page gets:

| Tab | File today |
| --- | --- |
| Overview | `wayfinder/overview.html` |
| Live tool | `wayfinder/index.html` |
| Trip and Campground Builder | `wayfinder/builder.html` |
| Packing list | `wayfinder/frisco-packing.html` |
| Product requirements | `wayfinder/prd.html` |

**The Campground Finder stays a separate project**, because finding a site and running a trip are different problems and joining them makes both tools worse. The handoff is one direction: after a booking is confirmed by hand, the dates pass to Wayfinder.

**Not going on the portfolio:**

- **`lunch/`**, a CU Boulder food guide built for Jasper in August 2026, sorted by walking distance from Williams Village. A good thing to have made. It demonstrates nothing about building.
- **`traillog/`**, a bike service record with a 12KB PRD written in July and untouched since. **This one is a judgement call and is worth revisiting.** A tool with a real PRD behind it is stronger evidence than most of what is already on the page, and it is currently linked from nowhere at all.


---

## Render and AVC 248 are one thing. Decided 30 Aug 2026.

They were two cards on the front page, **Render** as a tool and **Design Self Promotion** as a course. Michelle&rsquo;s call: *&ldquo;this should actually probably be combined into render, it&rsquo;s not really 2 things it&rsquo;s one thing.&rdquo;* She is right. The course IS the tool being built, across a semester, by the students who will keep it.

**The front page now has one Render card**, subtitled &ldquo;capstone course and career tool.&rdquo;

**On the v2 Render rebuild**, the course becomes a tab rather than a card:

| Tab | Page today |
| --- | --- |
| Overview | `render/overview.html` |
| Live tool | `render/index.html` |
| The course | `learning-design/avc248.html` |
| Product requirements | `render/prd.html` |

`learning-design/avc248.html` is currently reachable from nowhere on the v2 front page, so it needs that tab or it is orphaned on promotion.

**Also on that page:** `render/hiring-panel.html` and `render/interview-panel.html` exist and are linked from nowhere either. Worth deciding whether they are tabs, part of the live tool, or dropped.

---

# 🔍 V2 AUDIT, 30 Aug 2026

Three parallel audits: text accuracy, structure and evidence, and ethics on the Student Journey study. Everything below is verified against the files, not asserted.

## Already fixed, no decision needed

- **The askbar was dead.** `v2/index.html` copied the hero widget markup but not its script, so `abSubmit` and `abAsk` were undefined and the first interactive element on the page threw a ReferenceError. On a page headlined "I build AI tools." The script is now `v2/assets/askbar.js`, external so it cannot be lost in a copy again. Its 25K answer bank was checked against every guardrail in `CLAUDE.md` and is clean.
- Build's two tools still read "Tool 5 of 6" and "Tool 6 of 6" against a suite that no longer exists. Now 1 of 2 and 2 of 2.
- Both Build tool pages had "Dial Your Course" as their parent tab. Corrected.
- `v2/dial/index.html` was missing the sibling tab every other Dial page carries.
- The same SVG carried two different alt texts on one page.
- The Student Journey alt text claimed "50 tasks." The CV says a 46-task taxonomy, and the image contains no tasks at all. Rewritten to describe the actual picture.
- The file header comment and four `aria-label`s still named sections that were renamed.
- "Built entirely from open educational resources" overstated it. The source page says OER plus original simulations she built.
- "Strava mileage" implied a live integration. TrailLog's own status says Strava is simulated.
- "Highest-enrollment, lowest-success course" softened to match what the CV and `avc100/overview.html` both actually say.
- Five uses of "prototype" in TrailLog, which v2 status language bans.

## Needs a decision

1. **Seat Time says "specified but not built." `course-dialer/workload.html` is the built tool**, with seven course profiles and real AVC 100 estimates. Either the page is stale or the two were never connected.
2. **Campground is simultaneously "not built yet" on the front page and "built and used" on its own overview and PRD.** Also "8am daily" on the card versus a 10:16 timestamp in the screenshot, and "one campground" versus seven in the sample run.
3. **Build overview says "in build," OER Finder says "specified, not built," Build index says "not built yet."** Three statuses for the same two tools.
4. **No status at all** on the Dial cards, the Build cards, Render, or CopaMigo, while their neighbours carry "live and adopted" and "paused." A reader infers everything is running.
5. **The PRD tab renames itself when you click it**, "PRD" on tool pages, "Product requirements" on the PRD pages.
6. **Two claims on `about.html` have no supporting file:** the vocabulary-quiz replacement result, and "several courses." The simulated client agent in graphic design is confirmed, the rest is not.
7. **Alex Rivera's development plan cites postings that do not say what it claims.** "Named in 3 of 4 saved postings" when one mentions Cinema 4D; expressions and colour grading are named in no posting at all.
8. **The front page says Michelle built each career agent "for one specific person, then handed it over."** Alex is fictional and Render has not finished a pilot, so that sentence should not cover the Alex card.

## The overviews

All four are 325 to 376 words, so length is already consistent. Two real problems: **`dial` is missing Process AND Status**, and **all four are missing Tools and Outcomes**. All four are about 40% the length of `render/overview.html` (911 words), which is the site's own model for a full case study.

**No series overview has a "what this produced" group.** The one that exists is on `v2/index.html` at site level, holding ten unlike things in one row.

Recommended targets, because a single number would force padding on two pages: **dial 850 to 950** (it absorbs four tool pages), **build 650 to 750** (absorbs two), **campground and traillog 500 to 600** (nothing to absorb). What a reader perceives as consistency is the same six headings in the same order plus an evidence group, not a word count.

## Evidence she owns and is not showing

The tool pages are 115 to 177 words each with almost no artifact. Every one has a real source already in the repo:

| Tool page | Artifact that exists | Path |
| --- | --- | --- |
| Quality Check | Full audit of a real Canvas package, 28 findings, 7,452 words | `course-dialer/report-sample.html` |
| Seat Time | Live workload calculator, 7 profiles, real AVC 100 data | `course-dialer/workload.html` |
| Style Guide | 12 palettes with live contrast, plus the real course styled with it | `course-dialer/styleguide.html`, `canvas/avc248/avc248-canvas.png` |
| Authentic Assessment | Five built AI-resistant simulations | `authentic-assessment/*.html` |
| OER Finder | A real licence-verified submission record | `data-science-course/OER_SUBMISSION.md` |
| Syllabus Checker | **Nothing.** Needs one captured run, about an hour | build `syllabus-checker/report-sample.html` |

Two more real AVC 100 outputs nothing links to: `course-dialer/todo-sample.html` (6 actions with exact Canvas click paths) and `course-dialer/ilo-test.html` (6 of 58 institutional outcomes evidenced).

**The three strongest, in order:** the 28-finding audit inline on the dial overview; the **44% to 60% completion rise** in `avc100/overview.html` with its chart at `avc100/prepost-chart.png`, currently three clicks deep on a v1 page; and `synthetic-smes/panel-review.html`, the method catching its own errors, which is better evidence than the method producing a course.

**Revised courses have no home in v2 at all.** `canvas/avc248/` alone is a rebuilt 9-module course, roughly 40,000 words across 100+ files.

## Render, CopaMigo and the Student Journey have no v2 page

Three of her four largest projects hold six words of card subtitle each. `render/overview.html` is simultaneously the model the v2 overviews are copying and a page that was never brought into v2.

---

# ⚠️ STUDENT JOURNEY, THE EXPOSURE. READ THIS FIRST, 30 Aug 2026

**`airc-sss/` is already public.** `.nojekyll` is in the repo root, which disables Jekyll, so GitHub Pages serves **every** file at its literal path: markdown, `.docx`, `.xlsx`, `.pptx`, `.json`. The repo itself is public on github.com with full file browsing. `airc-sss/` is linked from both front pages, so it is crawled.

This is not a risk to design around. It is live now. Verified, not assumed.

## What is exposed

| What | Where | Why it matters |
| --- | --- | --- |
| **Ten named colleges rated on their failures.** 34 severity-scored findings. Chandler-Gilbert 12 mentions, Mesa 14, GateWay 11, Scottsdale 11, Estrella 10, South Mountain 9, Glendale 7, Paradise Valley 5, Rio Salado 4, Phoenix College 1 | `BARRIER_REGISTER_2026-08-27.md` | The exact relationship damage the buy-in guardrail exists to prevent |
| **A saved job description tied to district committee work**, saying the SSS mission "says it better" and listing phrases to pull into the project outcome | `risepoint-sr-director-jd.md` | A colleague reads this as district service steered by a job hunt. The worst single item |
| **"Doubles as Michelle's UX job-portfolio piece"**, in writing | `WORKING-STATE.md` | Same problem, stated plainly |
| **Her GCC work email, her personal Gmail, and a named district administrator** | `WORKING-STATE.md` | PII, hers and someone else's |
| **A named district staging host** disclosed as a defect, not yet routed to the web team | `BARRIER_REGISTER` item 3.16 | An IT security office reacts badly to this on a personal site |
| **Unapproved draft district governance**, charter marked "Draft Proposal" with a blank approval date, meeting agendas, the domain plan at v0.3 | 4 `.docx`, 2 `.xlsx`, 1 `.pptx` | Publishing draft governance of a public institution without tri-chair sign-off |
| **Procurement-sensitive material**, a subcommittee tasked to find out what an un-purchased vendor bot does | `SSS_Domain_Meeting_Agenda_June18.docx` | Not hers to make public |
| **A live open data-collection form** anyone can submit to | `run-sheet.html`, `WORKING-STATE.md` | Poisons the dataset |

**And the one that compounds all of it:** `ethics.html` and `airc-sss/index.html` both state that findings "stay unpublished until the domain confirms them." They are published, on the same server. Being caught in a false ethics claim is worse than the original disclosure.

## Genuinely fine, so it does not get padded with worry

- **No FERPA exposure. No student PII. No real participants.** Nothing run to date involves people.
- **No IRB needed for what has run.** AI agents on public pages are not human subjects.
- **The 20 files in `airc-sss/export/` are build tooling, not transcripts.** The 51 files in `agents/` are prompts, not results. Every persona name is fabricated.
- **The "no one is replaced" framing on the public HTML pages is already right.** Do not rewrite what works.
- **Naming the district is fine.** She is a district employee and the district is public. Hiding it would read as coy.

## Move out of the repo, in priority order

Michelle moves these to `~/Documents/Claude/`, then commits the deletions in GitHub Desktop. **Claude cannot do this**, the shell only reaches the repo.

**Today:** `risepoint-sr-director-jd.md` · `WORKING-STATE.md` · `BARRIER_REGISTER_2026-08-27.md` · `PHASE1A_RUNS_2026-07-27.md` · `PHASE1B_RUNS_2026-08-25.md`

**Same pass:** `SSS_Working_Group_Charter_DRAFT.docx` · `SSS_Domain_Meeting_Agenda_June18.docx` · `AIRC_Domain5_Student_Support_Success_Plan.docx` · `Student_Journey_Form_Blueprint.docx` · `The_Persistence_Imperative.pptx` · both `.xlsx` · `meeting-agenda-2026-07-09.md` · `_CHANGES-2026-07-27.private.html` · `ARC_AGENT_INTERVIEW.md` · `agents/` (51 files) · `synthetic-student-agent.md` · `research-aggregator-agent.md` · `build/tester_data.json` · `build/scenarios.json` · `export/` · `Create_Barrier_Log_Form.gs` · `HOW-TO-BUILD-THE-GOOGLE-FORM.md` · `run-log-form-setup.md` · `WGU_TECHNICAL_MODEL.md` · `RUNNING-THE-STUDY.md`

**Keep public:** the HTML case-study pages, the cover and journey graphics, `sss.css`. Those are hers and they are the portfolio.

**Removing a file stops it being served. It does not remove it from the public commit history.** Whether that matters depends on whether anyone looks, and it is a judgement call, not an emergency. `_paper-source.private.html` holds a staff contact roster and is gitignored now, but gitignore is not retroactive: **check in GitHub Desktop whether it was ever committed.**

## Anonymize as College A through J

Failures always. **Wins too**, because naming the colleges that got it right makes the others identifiable by subtraction. Local service names each identify their campus instantly and must not be published, including the Coyote Cupboard example, which is the best one in the corpus and the most identifying. The literary-magazine finding keeps all its insight as "one college's student literary magazine ranked for three separate crisis queries." Never publish the staging hostname, anonymized or not. Never publish the persona-to-home-college roster.

## Tab set, six not nine

The current nine overlap. Scope is one screen, Approach and Roadmap both describe how a gap becomes a pilot, Progress is an internal process log with high risk and low employer value.

| Tab | What goes on it |
| --- | --- |
| Overview | Goal, Audience, Process. Absorbs Scope. |
| Method | Persona construction, the one persona plus one college plus one task model, saturation, the findings schema. |
| Synthetic students | The 52-agent architecture and the literature, including where it fails. The differentiator, and what an employer will ask about. |
| Ethics and limits | The drafted section. **Sits before Findings, not after.** A reader who meets the caveats first reads the findings as careful. |
| Findings | Does not exist yet and is the tab a hiring manager wants. Anonymized, stated at the mechanism level, led by "retrieval matches vocabulary, not need," carrying the four retractions as a strength. Publishes only what the domain has cleared. |
| Roadmap | Absorbs Approach and Build teams. |

**Drop Progress as a public tab.** Its one strong item, the channel assumption named as the largest threat to validity, moves into Ethics and limits.

**Required under every statistics block:** "Counts are AI agent runs. No human participant has taken part in this study."

The full drafted ethics language is in the audit transcript. It covers: what the testers are, what synthetic agents can and cannot establish, bounds on the findings, corrections carried in the record, human subjects and consent, data handled, permission and ownership, colleges not named, staff and the purpose of the work, and crisis paths.

---

# 💬 FRONT-PAGE POSITIONING LINE, captured 31 Aug 2026

Michelle found wording on someone else's portfolio that captures the thing v2 is missing on the front page: the site is not a list of deliverables, it is an argument about how she thinks.

**The source wording, which is SOMEONE ELSE'S and must not ship as written:**

> "For me, the portfolio isn't just a showcase of what I can build. It's a look at how I think, design, experiment, and turn challenges into structured experiences."

**Why it is saved here and not pasted onto the page.** It is another designer's sentence, and it is in another designer's voice. Lifting it would be a lift, and the cadence ("showcase," "turn challenges into structured experiences") is softer and more marketing-toned than the register in `CLAUDE.md`. What to keep is the *move*, not the words: name the thesis of the site before the work, and make the thesis about method rather than output.

**The move, stated plainly:** open the front page by telling the reader what they are about to watch her do, then let the projects be evidence for it.

**Where it goes:** the front-page thesis line on `v2/index.html`, and probably an echo in the opening of `v2/about.html`. This is the same slot as the open question already logged in the design notes, the one flagged as "the thesis line is the one only she can write."

**What is actually hers to say, drawn from the through-lines in `CLAUDE.md`.** Raw material for that line, not finished copy:

- Tools that outlast the semester.
- No PII, minimum data. First names, localStorage, anonymized aggregates.
- Data-informed iteration. Usability test, pilot, revise.
- AI as scaffolding, not replacement. Humans still decide.
- Connectivism and PLEs as the theoretical floor.
- Honest status. Prototypes are labeled prototypes.

**Open question for her:** the honest version of this line is probably closer to "I build small, data-light tools, test them on real students, and publish what did not work" than to "how I think, design, experiment." Hers has evidence in it. The source line does not. Decide which register the front page opens in before writing it.
