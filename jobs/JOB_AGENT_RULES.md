# Job Agent Rules (authoritative)

This file is the source of truth for Michelle's personal job-search agent. The protected
`Documents/Claude/Scheduled/daily-job-search/SKILL.md` should point here and read this every run.
Edit the targeting here, in the repo, not in the protected skill.

Last tightened: **September 17, 2026** (target company list rebuilt and verified, tiered 1/2/3; Anthology/Encoura/Ellucian split recorded; do-not-chase rule corrected to point at acquirers).
Prior: **September 16, 2026** (added Alchemy / Nectar Inc as a target company).
Prior: **August 29, 2026** (collapsed card format locked, no preamble, run notes trimmed, schedule moved to Tuesday and Friday).
Prior: **August 28, 2026** (CV is rule zero, new star rubric, Anthropic removed, card format added).
Prior: August 12, 2026 (added "innovation" titles, all-Colorado + mountain-town reach, Flagstaff/NAU/Coconino).

> ## ⛔ RULE ZERO: READ THE CV BEFORE ANYTHING ELSE
>
> **Open `cultivate/cv.html` in this repo and read it.** It is the single source of truth for job history, titles, dates, and accomplishments. Do not work from a summary, including this file or `CLAUDE.md`. Do not assert a gap in her experience without searching the CV for it first. When briefing a subagent, **paste the relevant CV text into the brief**, because a subagent cannot reliably fetch the public URL.
>
> **This file previously said she has &ldquo;NO formal PM title history.&rdquo; That was false and it caused real damage.** The CV shows **Product Manager, Higher Education, ProQuest/XanEdu, 1999 to 2002** and **Director of Instructional Technology, GCC Innovation Center, 2004 to 2011**, seven years leading platforms and the teams behind them. On 28 Aug 2026 that one sentence produced a page of wrong star ratings, a community-college Academic Dean scored 2 stars when she exceeds both the minimum and the preferred bar, and 22 roles removed on a false premise.
>
> **Three files have claimed authority over this agent:** this one, the scheduled `Documents/Claude/Scheduled/daily-job-search/SKILL.md`, and the job-search section of `CLAUDE.md`. **This file wins.** The SKILL.md is readable with the Read tool even though its folder cannot be mounted, so read it for the source list, but where the two disagree, follow this file.

## Goal
Surface only roles Michelle can realistically land and actually wants, in higher education and
higher-ed-adjacent lanes, ranked honestly by fit to her resume. No aggregator noise, no padding
to hit a number, no dead links.

## Audience
Michelle Blomberg. Her real lanes: learning-experience / instructional design, UX and service
design, faculty enablement / academic innovation, AI-in-education, and EdTech product. Her degree
that carries the requirement is the M.Ed. in educational technology (the BFA is her design and UX
foundation).

Her own words on positioning: **&ldquo;I can&rsquo;t rely on just my faculty position to get me into these jobs because they want someone actually doing this work as their job. Rely on my committee assignments and extra projects.&rdquo;** So lead with the ARC domain co-chair role and the ten-college study, the GCC Cares Hub brand identity she leads, the intranet redesign committee, the 45-faculty online transition, the QM/OSCQR reviewer work, and the past Director and PM roles. Not &ldquo;she teaches.&rdquo;

## Process (the rules)

### 1. The star rubric (set by Michelle, 28 Aug 2026)

Five-star scale. **Rate against the STATED MINIMUM QUALIFICATIONS in the posting, not against the seniority the title implies, and not against titles she has not held.**

- **5 stars.** The work is AI, learning experience design, instructional design, UX research or service design, faculty development, or AI enablement, AND she meets the minimum qualifications.
- **4 stars.** She meets the minimums, or is close, OR the work is squarely in one of those lanes.
- **Below 4 stars: it does not go on the page at all.** If it is not a real match, do not surface it. There is no stretch section and no reach section any more.

Be generous where the evidence supports it. **If there is no honest gap, write &ldquo;You clear the minimums&rdquo; rather than inventing a weakness.** The recurring failure has been marking her down for not holding a title when she has done the work, or when the CV shows she held the title already.

### 🔢 RANKING. Set 19 September 2026. The page is ORDERED, not just filtered.

**Every card carries a rank badge, `<span class="tag rank">#N</span>`, as the first child of its
`.srow`. Numbering runs 1..N straight through BOTH sections, Colorado first. Renumber the whole
page on every run. A card without a badge is a bug.**

**Tier 1, Colorado. Always #1 and down, whatever the lane.** Her reasoning, in her words: a
Colorado role competes against one state, a US-remote role competes against fifty, so in-state is
materially easier to land. Inside the Colorado tier, order by:

1. **Hybrid or partly remote** beats full on-site. She asked for this specifically. State the
   in-office days on the card every time.
2. **AI-forward** work beats non-AI.
3. Strength of fit against the stated minimums.
4. Band, last. She has accepted that the Colorado tier pays less than the remote tier.

**Tier 2, remote. AI-forward first.** Inside it: AI or AI-enablement work, then fit, then band.
Travel-heavy roles sink regardless of band, and roughly 25 percent or more is a cut, not a sink.

**Do not renumber to hide a removal.** If she takes a card off, renumber cleanly and say which
numbers moved, because she refers to these roles by number in conversation.

**Section headers carry the count** in `<span class="gcount">`. Update both every run.

**Known trap, hit on 19 September.** When adding a card, insert it INSIDE its
`<section class="group local">` or `<section class="group remote">`. Appending after the last
`</details>` in the file puts it outside the section, and the next reorder silently DUPLICATES it.
After any edit, assert: no repeated `class="jt"` title, and card count equals rank-badge count.

### Work shape, set 19 September 2026, RELAXED same day. Read the relaxation, not the first draft.

**Claude filtered far too hard on the first pass and Michelle pulled it back. Her words:
&ldquo;this rule is making me nervous, I don't think we want to cut that hard, we are not picky at
this point in time.&rdquo; When in doubt, LEAVE THE CARD ON THE PAGE.**

- **The only hard title cut is a literal trainer title.** Trainer, Training Specialist. That is it.
- **Instructional design, learning experience design and UX specialist all STAY on the table.** They
  are core lanes, not edge cases, whatever the employer type.
- **AI-forward is a preference, not a filter.** Rank AI-adjacent work higher. Do not remove a role
  for lacking AI.
- **What she actually does not want** is a job that is eight hours a day standing up delivering
  corporate trainings, or whose whole output is building them. That is a RANKING signal and a
  note on the card, not a reason to drop the role.
- **Presenting should be part of the job.** She wants some of it. Briefing leadership, running a
  discovery workshop, demoing a solution: all wanted.

**Travel and location, set 19 September 2026.**

- **OUT: travel-heavy roles.** Anything advertising roughly 25 percent travel or more, and
  consulting roles that travel to client sites for a living. Her words: &ldquo;probably not a
  traveling position so much, more just remote is what I'm looking for.&rdquo;
- **Remote is the preference**, not merely acceptable. Weight genuinely remote roles above hybrid,
  and hybrid above on site, when fit is otherwise equal.
- **COLORADO IS NEVER FILTERED. This overrides the work-shape rules above.** Her reasoning, 19
  Sept: a Colorado role competes against one state, a US-remote role competes against fifty, so the
  in-state ones are materially easier to land. **Keep every Colorado role on the page regardless of
  lane, shape or commute**, including on-site. State the commute plainly on the card and let her
  weigh it. The work-shape filters apply to remote and out-of-state roles only.
- **What she is actually fleeing is travel, not commuting.** She has been doing heavy travel and
  wants out. A 35-minute drive to Englewood is fine. Fifty percent travel is not.

These still remove a role outright, regardless of lane:
- A stated minimum of 5+ years of *recent, formal* product management, or a director/VP role gated on more supervisory years than the CV shows.
- Years of software development or engineering experience as a primary requirement.
- A degree or credential she does not hold (PhD, CS degree).
- Heavy quantitative, data-science, BI, dashboard, or SQL-first roles. She is not a data person.
- Below the $80K floor (exceptions in Section 7).
- Already applied, interviewed for, or rejected. Check every row of the tracker first.

### 2. Higher ed is the anchor, every run
Always search, by name, every run:
- EVERY Colorado university, statewide, not just Denver-metro (scan each one's careers board every run):
  University of Colorado (Boulder, Denver, Colorado Springs/UCCS, and Anschutz), Colorado School of
  Mines, Colorado State University (Fort Collins, CSU Global, CSU Pueblo), Metropolitan State University
  of Denver (MSU Denver), University of Denver, Colorado Mesa
  University (Grand Junction), Fort Lewis College (Durango), Western Colorado University (Gunnison),
  Colorado College (Colorado Springs), Adams State (Alamosa), and any other CO public or private
  non-Christian institution. SKIP Christian schools (Regis, Colorado Christian) and, per Michelle
  (Aug 12), University of Northern Colorado / UNC Greeley. Everything else statewide is IN. Non-flagship and
  mountain/rural universities stay IN, flagged as likely lower pay but still above floor; Michelle will
  relocate for these (see Geography).
- EVERY Colorado community college, statewide (scan the Colorado Community College System / CCCS Workday
  board plus any standalone boards every run): all 13 CCCS colleges, Arapahoe CC, Community College of
  Aurora, Community College of Denver, Front Range CC, Red Rocks CC, Pikes Peak State College, Pueblo CC,
  Colorado Northwestern CC, Lamar CC, Morgan CC, Northeastern Junior College, Otero College, Trinidad
  State; plus Aims Community College (Greeley) and, importantly, Colorado Mountain College (all campuses:
  Glenwood Springs, Aspen, Carbondale, Steamboat, Leadville, Salida/Buena Vista, Breckenridge, Vail,
  Rifle, Edwards, Spring Valley). Target instructional design, learning/academic technology, faculty
  development, academic innovation, and student-success roles. Mountain-town CC roles are wanted, not
  demoted, Michelle will move for the right one.
- FLAGSTAFF, ARIZONA (scan every run, in-person there is acceptable): Northern Arizona University (NAU,
  nau.edu/human-resources jobs board) and Coconino Community College (coconino.edu). Flagstaff is inside
  Michelle's relocation zone. Target the same lanes: instructional design, e-learning / academic
  technology, faculty development, academic/AI innovation, student success, UX. This is the ONE Arizona
  exception besides genuinely-remote Maricopa roles.
- KEYWORDS to run against every college board and every company board (not just "instructional design"):
  innovation, "innovation manager", "innovation director", "director of innovation", "dean of innovation",
  "academic innovation", "digital innovation", AI strategy, AI innovation, emerging technology, change
  management, AI enablement, AI adoption, AI literacy, AI trainer, digital transformation, learning
  technology, academic technology, educational technology, learning experience, faculty development,
  student success, service design, UX. Michelle's strongest lanes are AI strategy / innovation / change
  management / enablement, so weight those at least as heavily as instructional design. Run the word
  "innovation" as its own explicit search against every board every run (Innovation Manager / Director /
  Dean, Director of Academic or Digital Innovation), Michelle specifically wants these surfaced.
- Maricopa County Community College District, Arizona (scan jobs.erp.maricopa.edu every run) but
  REMOTE / work-from-anywhere ONLY. Michelle works at GCC now and will NOT commute to or live in
  Arizona, and Maricopa "hybrid" means in-Valley, so surface only genuinely remote District Office,
  OIT, academic-technology, teaching-and-learning, AI/innovation, or Rio Salado (online college)
  roles. Drop every in-person Phoenix-metro posting.
### 2c. TARGET COMPANIES. Rebuilt and verified 17 September 2026.

> ⚠️ **The sector consolidated hard in 2025 and 2026. Searching old names returns dead listings.**
> **Anthology no longer exists.** Chapter 11 in late 2025; emerged March 2026 as **Blackboard** (teaching
> and learning only, Oaktree/Nexus owned). Its SIS and ERP went to **Ellucian**. Its CRM and student
> success went to **Encoura**. **Ocelot and Ivy.ai** are now one product, “Ivy & Ocelot,” inside
> **Gravyty**. **Coursera merged with Udemy** (May 2026, layoffs followed). **Symplicity** went to
> **Volaris** (Feb 2026). **Sana** went to **Workday**. **Udacity** is inside **Accenture LearnVantage**.
> Search the acquirer, never the corpse.

**TIER 1. Scan every run, and treat as apply-and-network targets.**

- **Instructure (Canvas)** · KKR-owned, healthy, dominant LMS. **Salt Lake City, Utah**, strongly remote.
  Hires Instructional Designer, Learning Experience Designer, adoption and faculty-enablement roles by name.
- **Western Governors University** · **Salt Lake City, Utah.** The largest employer of instructional and
  learning experience designers in US higher ed. Competency-based, heavy internal AI work, remote-friendly.
- **ASU / EdPlus** · Tempe, AZ. The national center of gravity for learning design, learning engineering
  and academic innovation. She already has an ASU adjunct conversation open.
- **Southern New Hampshire University** · huge remote learning-design org; hires LXD nationwide remote
  despite the NH address.
- **Alchemy / Nectar Inc** · alchemy.works, North Charleston SC, all roles remote. Curie is an AI course
  design system, a close cousin to her Course Dialer work. **Had an open full-time remote Learning Designer
  role as of 17 Sept.** Services/agency model, so confirm the full-time role clears the $80K floor and skip
  the contract postings. Board: `https://insource-services-group.breezy.hr/`
- **Element451** · independent, $175M from PSG, 250+ institutions including community colleges. **New York**,
  remote roles. **Careers page posts nothing; resumes go to jobs@element451.com.** This one is networked into,
  not applied to. She has a meeting at EDUCAUSE.
- **Encoura** · **NEW, and the biggest omission.** Austin, TX. Bought RNL and Anthology’s entire student
  success and lifecycle portfolio in Feb 2026. This is where the student-success software jobs physically went.
- **D2L (Brightspace)** · public, independent, US remote. One of the few LMS vendors that employs
  instructional designers as core revenue staff: Instructional Designer, Learning Architect, Curriculum Developer.
- **McGraw Hill** · independent, went public July 2025. Columbus, OH, remote-friendly. Hires LXD and digital
  product roles in a non-coastal footprint.
- **Pearson** · independent, healthy, pushing AI upskilling hard. Distributed/remote US higher-ed operation.
- **Cengage** · KKR-backed, remote-first culture, weighing a 2026 IPO. Pre-IPO usually means active hiring.
- **Adobe** · large **Lehi, Utah** campus, which makes it viable without California. Education program,
  customer education and design-advocacy roles suit her design background.
- **EdSights** · $80M raise Sept 2025, 250+ universities, remote-friendly. AI retention chatbot.
  **Conversation designer is a real entry point for a non-engineer who has built agents.**
- **InScribe** · **NEW. DENVER, COLORADO.** AI plus peer-community platform that routes students to answers
  and support. This is CopaMigo’s exact category, in her city. 2026 wins include CSU Global.
- **EdVisorly** · **NEW.** $13.3M Series A July 2026. AI platform for the community-college-to-university
  transfer problem. Explicitly built around community colleges. Remote.
- **Cadmus** · **NEW.** Assessment platform built for authentic, AI-resilient assessment rather than
  detection. Her exact intellectual lane. Australian-origin, **verify US hiring before investing time.**
- **Riipen** · **NEW.** Embeds real employer projects into curriculum at scale. Sits where her experiential
  learning and career readiness work overlap. Community colleges are a core segment.
- **uConnect** · remote-first, “work from anywhere.” Virtual career center platform. Low opening volume,
  excellent fit and geography.

**TIER 2. Scan every run, apply when the posting is genuinely remote or in-zone.**

- **Salesforce (Education Cloud)** · **has a Denver office**, which puts it in zone. Maricopa is implementing
  Education Cloud, so she has live domain context most candidates lack. **Industry Advisor - Education** and
  customer success roles hire higher-ed insiders and value domain over platform certification; Solution
  Engineer roles do want platform skill. Worth the swing on the higher-ed angle.
- **Gravyty (Ivy & Ocelot)** · the acquirer of Ocelot and Ivy.ai. Community colleges are an explicit market.
  Hires CS, implementation, PM, and conversation design. Remote roles posted regularly.
- **EAB** (holds **Forage**) · one of the larger lane-relevant employers. DC-based but posts US-remote.
  **Filter hard for remote**, no East Coast relocation.
- **Ellucian** · Reston VA, genuinely remote-friendly, post-acquisition integration hiring. PM, UX, customer
  enablement. Administrative systems, so little true instructional design.
- **Blackboard** (formerly Anthology) · debt-free and refocused on teaching and learning, which is her subject
  matter. Just shed a third of the company and leadership is unsettled. Higher risk.
- **Transfr** · **NEW.** VR career exploration and vocational training sold to community colleges and workforce
  boards. Hires Instructional Designer and Curriculum Developer. **Directly relevant to the XR lab work.**
  Last funding was 2023, so check runway.
- **Modern Campus** · continuing ed and workforce registration, which is her market. Toronto HQ, distributed US.
- **Coursedog** · “remote-first in perpetuity,” curriculum and catalog operations, acquiring (ClassRanked 2026).
- **Stellic** · degree planning and advising UX. Expanding in 2026 (Indiana system-wide, Cornell). Seattle, small.
- **Pathify** · campus experience platform, $25M raised, acquired Navengage. Careers page 404s; go via LinkedIn.
- **Workday (Student)** · 2026 Gartner MQ Leader for higher ed SIS. Pays well above floor, genuinely distributed.
  Roles skew enterprise implementation.
- **Turnitin** · Advance-owned, remote-heavy despite Oakland HQ. **Philosophical flag: a detection-first company
  is an awkward home for an authentic-assessment person**, and the CEO has publicly forecast AI-driven headcount cuts.
- **Lemnis** (holds **Mainstay**) · public charity, nonprofit, mission-aligned nudging and coaching.
  Comp may press the $80K floor.
- **Handshake** · repositioned around Handshake AI (training data), ARR past $1B. Real open product design roles.
  SF HQ, **confirm US-remote on any posting.**
- **Guild** · Denver, in zone, lane-relevant. **But: two large layoffs, Macy’s partnership ended, and an RTO
  push began Jan 2026.** Employer-benefits side rather than institutional higher ed.
- **Coursera (+ Udemy)** · remote-first and hires her titles, but mid-merger with active layoffs. Revisit once
  integration settles.
- **Watermark** · faculty workflow, accreditation and assessment, Austin, remote-friendly. **Main Capital
  announced intent to acquire 16 Sept 2026.** Hiring usually freezes during a pending PE deal; time for Q1 2027.
- **Macmillan Learning**, **Kaltura**, **Panopto**, **Articulate** (fully remote but corporate L&D), **Civitas
  Learning** (analytics-heavy), **Risepoint**, **ETS**, **College Board**, **ibl.ai**, **Top Hat**.
- Smaller, verify comp clears the floor: **WriteSea** (Tulsa OK), **Prentus**, **Big Interview**, **Packback**
  (no 2026 news either way, mild flag), **Halda** (bootstrapped, only sales roles open), **ReUp Education**
  (remote-first, but coaching/ops rather than design), **Interstride**, **Quinncia**, **Steppingblocks**.
- Each run, sweep **Built In Colorado** for any Denver/Boulder edtech or AI company hiring in her lanes.

**TIER 3. DO NOT APPLY. Dead, absorbed, or wrong lane.**

Do not search these brands’ own boards. Where an acquirer is named, **search the acquirer instead.**

- **AllHere** · DEAD. Chapter 7 bankruptcy after the LAUSD chatbot collapse. Remove entirely.
- **Ocelot**, **Ivy.ai** · gone as companies. One product inside **Gravyty** (Tier 2). Three old entries, one employer.
- **Mainstay** · now **Lemnis** (Tier 2).
- **Symplicity** · now **Volaris/Constellation**. Perpetual-hold owner that runs for margin, not headcount growth.
- **Forage** · now inside **EAB** (Tier 2).
- **Sana** · now inside **Workday**, as enterprise HR learning, not higher ed.
- **Udacity** · inside **Accenture LearnVantage**. Target LearnVantage if the tech-upskilling lane appeals.
- **2U / edX** · two restructurings in two years, contracting OPM market, regulatory pressure. Wrong place to spend a search.
- **Anthology** · the name is retired. See Blackboard, Ellucian and Encoura above.
- **Pluralsight** · lender-owned after the 2024 restructuring; corporate tech skilling, not higher ed. Utah fallback only.
- **MagicSchool AI** · Colorado and well funded, but **K-12 first**, which fails the higher-ed filter. Note it if that filter ever relaxes.
- **Technolutions (Slate)** · New Haven CT, in-office, engineering-heavy, almost no design roles. Fails lane and geography.
- **Figma** · healthy and public, but San Francisco-centered with no education design org. Fails the no-California rule.
- **Lightcast** · labor-market data. Analytics lane she has excluded.
- **Oracle (Student Cloud)** · struggling sub-product, no appetite for learning-design roles.
- **Barnes & Noble Education**, **Follett** · campus retail, losing or winning contracts respectively, but no design function either way.
- **Wiley** · healthy, but it sold its OPM to Risepoint and exited higher-ed services. Now research publishing and AI licensing.
- **Jenzabar** · Boston-centric, administrative systems, lean and privately held.
- **iSpring**, **Miro**, **Pangram Labs**, **GPTZero**, **VictoryXR** · wrong lane, wrong market, or too little signal.

> ⚠️ **Name collision, do not confuse these.** **Alchemy / Nectar Inc** (alchemy.works, North Charleston SC,
> course design services) and **Nectir** (nectir.io, AI infrastructure for schools, $12.5M March 2026) are
> different companies. Both are worth pursuing. Nectir is fully US-remote but had no lane-fit role posted
> as of 17 Sept; watch it.

> **Ownership note.** Private equity dominates this sector: KKR owns Instructure and backs Cengage; Vista owns
> EAB and co-owns Ellucian with Blackstone; Oaktree and Nexus own Blackboard; Providence backs Modern Campus;
> Volaris owns Symplicity; Main Capital is buying Watermark. Real salaries, recurring cost-cutting cycles.
> The genuinely independent employers in her lane are Pearson, McGraw Hill, D2L, Adobe, Workday, Macmillan,
> Kaltura, Docebo, and the universities themselves.

- Industry-crossover-into-higher-ed roles are welcome (a company serving colleges, or a learning
  team inside a larger org that maps to her strengths).
- Primary edtech job boards for discovery (verify every hit on the employer's own board): edtechjobs.io
  (timestamps postings and marks "Position Filled," best for freshness) and Built In Colorado.
K-12-only roles are out. This is a higher-ed search.

### 2a. THE BOARD URLS. Verified 1 September 2026. Use these, do not search for them.

**Most Colorado institutions moved to Workday on 5 January 2026.** The old links are dead and some of the colleges still link to them from their own HR pages, which is how a run wastes twenty minutes.

> ⚠️ **A Workday or iCIMS board returns an EMPTY BODY to a plain fetcher**, because the listings are JavaScript-rendered. An empty response is NOT evidence the board is dead. Open these in the browser, or hit the Workday JSON endpoint. Calling a live board dead has already cost one run.

| Institution | Board URL | Req ID in the deep link? |
| --- | --- | --- |
| **MSU Denver** (top priority) | `https://msudenver.wd1.myworkdayjobs.com/MSUDenver` | yes, `JR######` |
| **CSU Fort Collins** | `https://csusystem.wd12.myworkdayjobs.com/fortcollins_careers` | yes, `R2026######` |
| **CSU Pueblo** | `https://csusystem.wd12.myworkdayjobs.com/pueblo_careers` | yes, `R2026######` |
| **CSU System office** | no separate board, its roles post onto Fort Collins | |
| **CSU Global** | staff `https://staff-csuglobal.icims.com/` &middot; faculty `https://faculty-csuglobal.icims.com/` | yes, numeric |
| **CCCS**, all 13 colleges | staff `https://hr.cccs.edu/jobs/search/search-page-apt` &middot; faculty `/search-page-faculty` &middot; instructors `/search-page-instructors` | no, slug only |
| **CU** Denver, Anschutz, UCCS, System | `https://cu.taleo.net/careersection/2/jobsearch.ftl?lang=en` | yes, `?job=#####` |
| **CU Boulder**, separate board | `https://jobs.colorado.edu/jobs` | yes, numeric |
| **Colorado School of Mines** | `https://mines.wd1.myworkdayjobs.com/Mines_Careers` | yes, `JR######` |
| **University of Denver** | `https://jobs.du.edu/` | yes, numeric |
| **Colorado Mountain College** | `https://wd5.myworkdaysite.com/recruiting/coloradomtn/ColoradoMountainCollege` | yes, `JR######` |
| **Aims** | `https://aims.wd1.myworkdayjobs.com/Jobs` | yes, `R####` |
| **Colorado Mesa** | `https://coloradomesa.wd501.myworkdayjobs.com/CMUCareers` | yes, `JR######` |
| **Fort Lewis** | `https://fortlewiscollege.wd1.myworkdayjobs.com/FLC` | yes, `JR####` |
| **Western Colorado** | `https://western.wd1.myworkdayjobs.com/WESTERN` | yes, `R###` |
| **Colorado College** | `https://jobs.coloradocollege.edu/jobs/search` | no, slug only |
| **Adams State** | `https://adams.wd1.myworkdayjobs.com/ASU` | yes, `R###` |
| **NAU** Flagstaff | `https://careers.nau.edu/jobs/search` | no, slug only |
| **Coconino CC** | `https://www.schooljobs.com/careers/coconinocc` | yes, numeric |

**Dead, do not use again:** `jobs.colostate.edu`, `careers.csupueblo.edu`, `jobs.mines.edu` (redirects), `coloradomtn.edu/employment`, `aims.edu/about/employment`, `csusystem.edu/careers`, `in.nau.edu/human-resources/careers`.

**Maricopa: `jobs.maricopa.edu` is the WRONG HOST and is unreachable.** The live host is `jobs.erp.maricopa.edu`, PeopleSoft tenant `MCPAHPRD`, `SiteId=1000`. The reliable way in is Maricopa&rsquo;s own server-rendered listing pages, which are not blocked and embed the full job JSON: `https://www.maricopa.edu/about/careers/full-time-staff`, plus `/faculty`, `/adjunct-faculty`, `/part-time`. Paginate with `?page=2`.

### 3. Core titles (the bulk of apply-now when they fit her resume)
Learning experience designer, instructional designer, learning designer, curriculum designer /
manager, faculty development / academic innovation, AI enablement / adoption / trainer (education),
UX designer / researcher, service designer, and INNOVATION titles (Innovation Manager, Innovation
Director / Director of Innovation, Dean of Innovation, Director of Academic or Digital Innovation).
When a title like these fits her CV, rank it high.

ADDED Aug 8, 2026 (title-shift reframe): the market renamed "UX Designer" to "Product Designer,"
which carries a higher pay band, so ALSO search these consolidated / higher-value titles every run
and rank them high when they fit:
- Product Designer; Product Designer (Education / EdTech / Learning); Senior Product Designer
- LX Designer; Learning Product Manager; Product Manager (Learning / Education / Student Success)
- Student Experience Designer; Student Journey Designer; Content Designer; Design Strategist
- Solutions / Forward-Deployed / Developer-Advocate / Developer-Education roles at AI + edtech cos
  (her "build-with-people" favorite lane)
Honest caveat for ranking: "Product Designer" roles at tech companies often want a shipped-at-scale
portfolio and an industry product/design title she does not yet have, so a bare "Senior/Staff Product
Designer" at a big tech co is usually a 3-star reach, not a bullseye. Rank HIGHEST the product/LX
titles that sit in education, student success, or AI-enablement, where her Render / CopaMigo / ARC
student-journey work is real, ownership-level evidence.

### 4. Drop the off-lane roles
Do not surface: background-check companies (e.g. Checkr), home-services marketplaces (e.g. Angi),
generic dev-heavy product roles, or heavy quant product-analyst roles. Demote/remove CodePath,
Michelle reviewed those and they were not real fits.

### 5. Verified specific links only (open the company's own page every run)
Every Apply link must open the EXACT, live job posting on the EMPLOYER'S OWN careers page, verified
the day of the run by actually fetching that page and seeing the title + location live. This is
non-negotiable, Michelle hates clicking through to a blank or dead page.
- BANNED as apply links: a bare ATS board landing page (e.g. `nrel.wd5.myworkdayjobs.com/NREL` with
  no req), a search-results page, a generic `/careers` page, or ANY aggregator (Indeed, LinkedIn,
  ZipRecruiter, Glassdoor, edtechjobs.io). Those are for DISCOVERY only, never the final link.
- The link must be the deep link to the specific req (the URL that contains the job/req ID). If the
  employer's ATS will not expose a stable deep link, do NOT list it as an apply link, find the real
  req URL or drop the role. Do not hand Michelle a board and tell her to "search the ID."
- If a company only posts to Workday, check whether it also has a human-readable careers page (e.g.
  `careers.<company>.gov` / `.com`) that deep-links into the req, and use that.
- A role whose only available link is generic or unverifiable stays OUT of the four- and five-star
  tiers and out of the apply-now list. Instructure is on its own board / Ashby, not Lever; verify
  JS-rendered boards by opening the link.
- NREL note (Aug 2026): NREL rebranded to "National Laboratory of the Rockies"; its board is now
  `nrel.wd5.myworkdayjobs.com/NLR`. As of this update it had NO instructional-design / L&OD / learning
  reqs open (only ML/research/postdoc). Re-verify before ever re-adding an NREL card.

### 6. Geography
- Remote preferred.
- Colorado local and hybrid are great (Denver / Boulder / Golden).
- Relocation zone OK (Michelle will move for the right role): any Colorado mountain town, explicitly
  including Durango, Glenwood Springs / Roaring Fork Valley, Carbondale, Salida, Gunnison, Steamboat,
  Grand Junction/Fruita, Cortez/Mancos; plus Utah, New Mexico, and Flagstaff, Arizona.
- NO San Francisco / California relocation. Michelle confirmed she will not move there, even for a
  dream AI-lab role. Do not surface California-onsite roles as real options.
- NYC and the entire East Coast: never, even for a dream job.

### 7. Salary
$80K hard floor. Flag any band that dips below it. Target $100K realistic, $150K aspirational.

### 8. Anthropic is OFF. Permanently.
**Never surface an Anthropic role.** Michelle&rsquo;s call, 28 Aug 2026, in her words: she loves them and is not going to get hired there with her skills, so stop pointing her at them. Other dream-tier employers (Google, OpenAI, Microsoft) only if remote or Denver/Boulder local, and only if they clear 4 stars on the rubric above. Never SF-onsite, see Section 6.

## Output

Cumulative dashboard rebuilt to `Documents/Claude/JobSearch/Michelle_job_dashboard.html` and the
phone view at `jobs/index.html` (noindex, unlinked). Keep still-live prior matches, flag NEW vs
carried-over, sort by honest fit. Do not resurface roles Michelle has already applied to. Solid
palette colors only, no gradients; no em dashes; curly quotes.

### The page is never wiped
Read the current `jobs/index.html` in full first and edit it **surgically**. Never wholesale-rewrite it and never replace it with the desktop dashboard&rsquo;s contents; the two curations are allowed to differ. Never remove a role unless Michelle says it is a bad match or the posting is verified closed on the employer&rsquo;s own board. **This was broken twice on 28 Aug 2026 by agents that rebuilt the page instead of editing it, losing the star glyphs and the card layout. Do not do it again.**

### Star markup, exactly this
```html
<span class="stars" aria-label="Four out of five stars">&#9733;&#9733;&#9733;&#9733;&#9734;</span>
```
Filled `&#9733;`, empty `&#9734;`, always five glyphs, aria-label spelling the number in words. **The stars are the first element in the summary row, top left, 18px.** Never render a rating as the words &ldquo;4 stars.&rdquo;

### Card format, LOCKED 29 Aug 2026. Every card collapses.

Michelle scans this page on her phone. **The whole page must be scannable in one pass without opening a single card.** Every card is a `<details class="card local|remote">`. The CSS is already in `jobs/index.html`; do not rewrite the style block.

**Visible in the `<summary class="cardtop">`, in this order, and nothing else:**

1. **The stars.** Top left, 18px, the locked markup above. The most important element on the card.
2. **A badge, only when one truly applies.** `NEW 29 Aug` for a role found in this run, `CLOSES 6 SEPT` for a real deadline. **No editorial badges ever.** Nothing like &ldquo;strongest match of the sweep,&rdquo; &ldquo;re-rated Aug 27,&rdquo; or &ldquo;you exceed every stated qualification.&rdquo;
3. **The title**, as `<h3 class="jt">`.
4. **One `<span class="sub">` line:** company in `<b>`, then location or remote, then pay, then the requisition number, middot separated.

**Collapsed inside `<div class="body">`, in this order:**

5. **What the job is.** Two to four short bullets on the actual work. Do not describe Michelle here, and do not keep naming Render and CopaMigo.
6. **`Strong:`** the specific stated minimums she clears and the credential that clears each one. Point at the CV, not at &ldquo;she teaches.&rdquo;
7. **`Light:`** the specific real gaps against the stated minimums. If there are none, write **&ldquo;Nothing material, you clear every stated minimum&rdquo;** rather than inventing a weakness.
8. **`Lead with:`** in the `.foot`, beside the Apply button. One CV credential.

**The headings are exactly `Strong:` and `Light:`.** Not &ldquo;Where you are strong.&rdquo;

**Keep the body short.** Her words, 29 Aug: &ldquo;these are like a book.&rdquo; Aim for about 120 words inside the collapse, hard stop at 150. If a card runs long, cut it. Never add a fifth block.

### No preamble. Ever.

**Nothing goes between `</header>` and the first card.** No summary paragraph, no &ldquo;what changed overnight,&rdquo; no explanation of the rating method, no note about which cards are new. Her words, 29 Aug: **this is redundant with our chat conversation.** Say it in the chat reply, or put it in the collapsed run-notes block at the bottom.

### The run-notes block at the bottom

One `<details class="log">` after the last card. Keep only what stops a future run from repeating work: what was looked at and left off and why, roles under the salary floor, roles out of lane, roles already in flight, roles verified closed, roles worth re-checking, and the standing framing and accuracy note. **Never write a narrative of what this run fixed.** No &ldquo;ratings raised as a result,&rdquo; no &ldquo;the card copy was rewritten,&rdquo; no &ldquo;every card now shows both halves.&rdquo; Michelle already had that conversation.

### Housekeeping
Never run git. Save the files and stop; Michelle reviews changes in GitHub Desktop and pushes herself. Run `python3 tools/design-lint.py` from the repo root before declaring done, and fix anything CRITICAL.

### 9. Verified closed or already applied. Never resurface these.

Checked against `~/Documents/Claude/JobSearch/Michelle_job_tracker.xlsx` on 1 September 2026, after a run put four bad cards on the page.

- **Blackbaud, Senior Program Manager, AI Literacy and Enablement (R0014526).** VERIFIED CLOSED 29 Aug and again 1 Sept: &ldquo;this job is no longer accepting applications.&rdquo; It has now been added to the page and removed twice. Do not add it a third time.
- **Blackbaud, AI Adoption Specialist (R0014520).** Verified closed 29 Aug.
- **Code for America, Emerging Tech and AI Governance and Enablement Lead (job 8001846). APPLIED 2 August 2026.**
- **AnswerRocket, AI Adoption and Enablement Consultant. APPLIED 2 August 2026.**
- **Colorado School of Mines, AI Solutions Manager (JR109535). APPLIED 18 September 2026**, on the closing day. Tracker row 153. Phone screen expected late September into October. Prep hub at `/minesai`. **Do not resurface.** Note: `mines/` in the repo is a DIFFERENT Mines role, Online Learning Experience Designer for Mines Online, and Michelle was **not selected** for that one (19 Sept 2026). Do not resurface that either.
- **Pluralsight, Solutions Portfolio Lead, Learning.** Reviewed and deprioritised as a reach. The newer *Principal* Solutions Portfolio Lead, AI (R0014425) is a different requisition and is fair to surface, but say that she looked at this family before.

> ⚠️ **CROSS-CHECK THE TRACKER BEFORE ADDING ANY CARD.** Not the page, the tracker. The page only shows what is currently listed; the tracker holds what she has applied to and what has been verified closed. On 1 Sept 2026 a run skipped this check and put two already-applied roles and one twice-removed closed role on the page.
>
> ⚠️ **A JOB PAGE THAT LOADS IS NOT AN OPEN JOB.** Fetch the posting and search the body for &ldquo;no longer accepting applications,&rdquo; &ldquo;this job is closed,&rdquo; and &ldquo;position filled.&rdquo; A subagent reported the closed Blackbaud role as live with full requirement text, because it read a cached rendering rather than the page state.

