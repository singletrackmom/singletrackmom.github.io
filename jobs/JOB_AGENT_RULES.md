# Job Agent Rules (authoritative)

This file is the source of truth for Michelle's personal job-search agent. The protected
`Documents/Claude/Scheduled/daily-job-search/SKILL.md` should point here and read this every run.
Edit the targeting here, in the repo, not in the protected skill.

Last tightened: July 25, 2026.

## Goal
Surface only roles Michelle can realistically land and actually wants, in higher education and
higher-ed-adjacent lanes, ranked honestly by fit to her resume. No aggregator noise, no padding
to hit a number, no dead links.

## Audience
Michelle Blomberg. Her real lanes: learning-experience / instructional design, UX and service
design, faculty enablement / academic innovation, AI-in-education, and EdTech product. Her degree
that carries the requirement is the M.Ed. in educational technology (the BFA is her design and UX
foundation). She has NO formal PM title history, so lead with shipped work, not a PM bar.

## Process (the rules)

### 1. Stars measure fit to HER, not role prestige
If the first or primary requirement is something Michelle does not have, the role caps at 2 stars,
goes in a clearly labeled "stretch" section, and never appears in the apply-now list. Disqualifiers
that cap the score:
- Years of software development / engineering experience
- 5+ years of formal product-management experience
- A degree or credential she does not hold (PhD, CS degree, etc.)
- Heavy quantitative / data-science / SQL-first roles
- Enterprise-SaaS senior/staff UX-research bar

A five-star role is one where she meets the core requirements and the work maps to her real
strengths. This rule exists because a Google role was once tagged five stars while its first
requirement was years of development experience she does not have. Do not do that again.

### 2. Higher ed is the anchor, every run
Always search, by name, every run:
- University of Colorado Boulder and Colorado School of Mines (always).
- All Colorado universities and Denver-metro community colleges: CU Denver, MSU Denver, University
  of Denver, Community College of Denver, Arapahoe CC, Red Rocks CC, Front Range CC, Colorado State
  (CSU). Other Colorado universities stay in, flagged as likely lower pay (but still above floor).
- Higher-ed technology companies: Instructure/Canvas, Element451, D2L/Brightspace, Anthology,
  Watermark, Coursera, 2U/edX, and similar. High-paying and remote preferred here.
- Colorado / Denver-metro edtech and AI companies (always scan, local is a bonus): MagicSchool AI
  (Denver, AI for educators, remote-first, strong fit), Guild (Denver, workforce education, keep
  scanning even though she applied to one role), Pluralsight (Utah HQ but remote and CO-friendly,
  AI learning content). Each run, also sweep Built In Colorado for any Denver/Boulder edtech or AI
  company hiring in her lanes and add the fits.
- Industry-crossover-into-higher-ed roles are welcome (a company serving colleges, or a learning
  team inside a larger org that maps to her strengths).
- Primary edtech job boards for discovery (verify every hit on the employer's own board): edtechjobs.io
  (timestamps postings and marks "Position Filled," best for freshness) and Built In Colorado.
K-12-only roles are out. This is a higher-ed search.

### 3. Core titles (the bulk of apply-now when they fit her resume)
Learning experience designer, instructional designer, learning designer, curriculum designer /
manager, faculty development / academic innovation, AI enablement / adoption / trainer (education),
UX designer / researcher, service designer. When a title like these fits her CV, rank it high.

### 4. Drop the off-lane roles
Do not surface: background-check companies (e.g. Checkr), home-services marketplaces (e.g. Angi),
generic dev-heavy product roles, or heavy quant product-analyst roles. Demote/remove CodePath,
Michelle reviewed those and they were not real fits.

### 5. Verified specific links only
Every Apply link must open the exact, live job posting, verified the day of the run. An expired
posting or a generic `/careers` landing page does not count as verified and cannot go in the
apply-now list. If only a generic page can be found, mark the role unverified and keep it out of
the four- and five-star tiers. Instructure is on its own board / Ashby, not Lever; verify JS-rendered
boards by opening the link.

### 6. Geography
- Remote preferred.
- Colorado local and hybrid are great (Denver / Boulder / Golden).
- Relocation zone OK: Utah, New Mexico, Flagstaff, Western Slope (Carbondale/Roaring Fork,
  Durango/Cortez/Mancos, Grand Junction/Fruita).
- NO San Francisco / California relocation. Michelle confirmed she will not move there, even for a
  dream AI-lab role. Do not surface California-onsite roles as real options.
- NYC and the entire East Coast: never, even for a dream job.

### 7. Salary
$80K hard floor. Flag any band that dips below it. Target $100K realistic, $150K aspirational.

### 8. Google / Anthropic and other dream-tier
Reach only, and only if the role is remote or Denver/Boulder local. Never SF-onsite. Keep them in a
small labeled reach section, not the apply-now list.

## Output
Cumulative dashboard rebuilt to `Documents/Claude/JobSearch/Michelle_job_dashboard.html` and the
phone view at `jobs/index.html` (noindex, unlinked). Keep still-live prior matches, flag NEW vs
carried-over, sort by honest fit. Do not resurface roles Michelle has already applied to. Solid
palette colors only, no gradients; no em dashes; curly quotes.
