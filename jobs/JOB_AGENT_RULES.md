# Job Agent Rules (authoritative)

This file is the source of truth for Michelle's personal job-search agent. The protected
`Documents/Claude/Scheduled/daily-job-search/SKILL.md` should point here and read this every run.
Edit the targeting here, in the repo, not in the protected skill.

Last tightened: **August 29, 2026** (collapsed card format locked, no preamble, run notes trimmed, schedule moved to Tuesday and Friday).
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
- Higher-ed technology companies: Instructure/Canvas, Element451, D2L/Brightspace, Anthology,
  Watermark, Coursera, 2U/edX, and similar. High-paying and remote preferred here.
- Colorado / Denver-metro edtech and AI companies (always scan, local is a bonus): MagicSchool AI
  (Denver, AI for educators, remote-first, strong fit), Guild (Denver, workforce education, keep
  scanning even though she applied to one role), Pluralsight (Utah HQ but remote and CO-friendly,
  AI learning content). Each run, also sweep Built In Colorado for any Denver/Boulder edtech or AI
  company hiring in her lanes and add the fits.
- Small/mid AI-forward edtech companies (Element451-type, always scan their own boards): Element451,
  EdSights, Stellic, ReUp, uConnect, WriteSea, Prentus, Big Interview, Packback, Coursedog, Turnitin,
  Halda (Utah), Pathify (Denver). These hire implementation, customer-education, CS, and ID roles that
  value a teacher-who-builds. Do NOT chase (acquired/absorbed/dead): Ocelot and Ivy.ai (now Gravyty),
  Mainstay (Lemnis), Symplicity (Volaris), Forage (EAB), Sana (Workday), AllHere (defunct).
- Industry-crossover-into-higher-ed roles are welcome (a company serving colleges, or a learning
  team inside a larger org that maps to her strengths).
- Primary edtech job boards for discovery (verify every hit on the employer's own board): edtechjobs.io
  (timestamps postings and marks "Position Filled," best for freshness) and Built In Colorado.
K-12-only roles are out. This is a higher-ed search.

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
