# Family job-search agents

Michelle runs a small set of scheduled agents for her family. Each one researches jobs or opportunities for one person and publishes a page in this repo that the person just refreshes.

## Where the runnable instructions live

Each agent's actual runnable instructions live at `~/Documents/Claude/Scheduled/<name>/SKILL.md`.

- **That folder cannot be mounted** into a session's Linux workspace, so `bash` cannot see it.
- **The files CAN be opened directly with the Read tool by full path**, for example `/Users/michelleblomberg/Documents/Claude/Scheduled/kevin-daily-job-search/SKILL.md`. Do that instead of using computer-use or Finder.
- Writes to that folder are blocked from a cloud session (macOS protects it). To change an agent's rules from the cloud, put the rules in the repo and leave a pointer in the protected SKILL.md, the way the DMA jobs agent does (`discord/DMA_JOBS_AGENT.md`).
- **All scheduled tasks are currently DISABLED** (verified 28 Aug 2026: every task in the scheduler shows `enabled: false`). Nothing fires on its own right now. Runs happen manually.

To run one: read its SKILL.md and execute it.

## Cadence and the catch-up rule

- **The family agents run WEEKLY, not daily** (changed 19 July 2026). The scheduler cron is set to Sunday mornings for all four (Kevin 6:07, Devan 6:04, Jasper 6:03, Jillian 6:09). Do not run one that already ran in the last 7 days.
- They are scheduled in the morning, but Michelle turns her computer off overnight, so a due run often misses the cron and needs a manual run when she signs on. **If a run was missed because the computer was off, Claude runs it when she signs on. It is not her job.**
- Each agent **keeps ALL still-live leads week to week**: re-verify them, drop only the ones that have actually closed. Not everyone applies every run.

## HANDS-OFF POLICY (19 June 2026)

**Michelle should NOT spend her time running or iterating the family agents.** She wasted hours doing that. They run automatically and publish to their pages; if a run was missed, Claude handles it.

Family members can iterate their own page in their OWN Claude. Kevin's Focus page has ready-to-paste prompts at the bottom for exactly this.

---

## Who publishes where

| Person | Agent | Publishes to |
|---|---|---|
| Kevin (husband) | `kevin-daily-job-search` | `focus/` (published at singletrackmom.github.io/focus/) |
| Jillian | `jillian-find-your-flow` | `flow/` (the apply-today board is `flow/jobs.html`) |
| Devan | `devan-daily-job-search` | `summerwork/` |
| Jasper | `jasper-soar` | `soar/` |

There is also `devan-travel-dashboard-weekly`, a weekly refresh of Devan's Europe travel and work-abroad dashboard.

---

## Kevin, `focus/`

The page was renamed from `/kevin/` to **`/focus/`**, titled "Focus," with a photography theme: a camera-lens SVG in the hero and subtle bike accents. **No email anymore.** He just refreshes https://singletrackmom.github.io/focus/.

We run Berg Berg Photography (bergbergphotography.com), wedding photojournalism. Kevin is lead; Michelle assists selectively.

### His fit (hard)
Staged **PRODUCT / parts / frame / website** shots and **ARCHITECTURAL building photography** (he is an architecture expert). **NOT** influencer or content-creator work. He applied to Revel's content-creator role, but building a following is not his thing. He is a professional event photographer, not the phone-clip content-creator type.

### Bike-brand memory (hard)
Four bike brands sit about a mile from the house: **Revel, Commencal, Spot, Yeti**. Keep close watch on all four as photography outreach targets.

- **ALCHEMY BIKES IS OUT OF BUSINESS (June 2026). Never suggest it.**
- Watch for a possible Italian brand relocating to Golden (unconfirmed; confirm before listing).

Bike-brand outreach copy should offer, on top of staged product / parts / frame and building photography:
- a follow-up shop ride out to **Apex** (the local trail) to stage action shots
- **professional event photography**: races, team and sponsored-rider days, launches (all four brands have sponsored riders)

### HARD PAY FLOOR
**Kevin will not work for under $20/hour, no matter what.** Never surface sub-$20 or low per-gig work. The mortgage / field-inspection gig at roughly $5 to $15 per inspection is OUT and was removed.

Be realistic on too-good-to-be-true gigs. Mortgage and field inspection (for example FAR) is a real industry, but pay is modest and per-inspection and work is inconsistent. Keep them if they clear the floor, label them honestly as fill-in income, and include the safety rule: **never pay upfront, never cash-and-wire.**

### Growth strategy for slow wedding years (a standing "growth ideas" section on the Focus page)
- **Colorado-destination portrait business** for visiting families and couples, beyond Denver / Golden / Boulder into Rocky Mountain National Park and Estes Park, Grand Lake, Winter Park, and Frisco / Breckenridge / Dillon.
- **Get found:** one web page per destination (ranks on Google AND feeds AI search for queries like "Colorado portraits while on vacation"), a complete Google Business Profile with reviews, and Pinterest boards.
- **Ads:** Meta (Instagram/Facebook) ads into Texas (Dallas, Houston, Austin) and other feeder markets (OK, KS, NE, AZ, Chicago), plus Google Search ads for high-intent queries.
- **Airbnb Photography Service:** apply to host one. Airbnb relaunched Experiences and Services in 2025 and photography is a category, so it is a stay-then-session hookup. **NOT set up yet, real to-do.**
- **Adobe Stock:** monetize his 20-year Colorado archive. We know someone who does Adobe Stock, warm intro available.
- **Lodging and venue referral partnerships** in the mountain towns (the offline version of the Airbnb hookup).
- **Pivot existing wedding contacts** toward elopements and destination family sessions.

---

## Jillian, `flow/`

### CURRENT STATUS (this changes what the agent does)
**Jillian is now enrolled in a medical assistant program** (Red Rocks Community College, the CAAHEP-accredited program that leads to the AAMA **CMA**, the strongest medical assistant credential, rather than the more common CCMA).

Because of that:
- **Runs surface office and medical jobs only.** Front desk, patient registrar, med spa and clinic support, and similar work that fits alongside school and points at medical assisting.
- **Stop proposing new career paths.** The career-deep-dive letters are paused. Existing locked letters and the archive are left untouched. The weekly run refreshes the apply-today board (`flow/jobs.html`) only.

### Standing rules (still apply, and apply to any career content if it ever resumes)
- Every career edition MUST include a **"How to get qualified" box** with real, accredited, **verified links**, framed as a small first step.
- **Prefer the least-school path and LOCAL Colorado community-college programs.** If a 4-year degree is the only route, use a community-college transfer / 2+2 path. She is ADHD and school-averse and cost-smart, not chasing the hardest school.
- **Check what employers actually require.** Never send her after something unattainable.
- **Framing (hard): Jillian pulled back when she felt Michelle was deciding her life for her.** Always present paths neutrally as HER choice, coming from Flow, not from Mom. Low pressure. The next step is small, and it is hers.

### Path notes on file (background, do not re-litigate)
- **PTA path** = Arapahoe Community College (AAS). She has already attended the Arapahoe CC info session and toured Pima Medical Institute (Denver, roughly 18-month associate, more money but Michelle would help pay). She has NOT applied. Prereqs can be taken at Red Rocks CC, the closest to the house.
- **Personal trainer path** = one NCCA-accredited cert (NASM or ACE), the local Community College of Denver NASM program, or Life Time Academy. Note some Life Time trainer roles prefer a degree, so start entry-level.
- **Lanes she had asked about** before enrolling: the many ways to use criminal justice, and how to become a paralegal (certificate or associate, not law school).

---

## Devan, `summerwork/`

`devan-daily-job-search`, weekly (Sundays). Seasonal, part-time, temp, freelance jobs and gigs near Golden, CO. Drafts an email straight to Devan.

Companion agent: `devan-travel-dashboard-weekly`, a weekly refresh of his Europe travel and work-abroad dashboard.

---

## Jasper, `soar/`

`jasper-soar`, weekly (Sundays). An aerospace stay-current dashboard plus a small gig board: space news, launches, CU Boulder ways-in, Summer 2027 internship watch, and gigs. Published at singletrackmom.github.io/soar/.

---

## Related, NOT a family agent

### Michelle's own job search, `daily-job-search` to `jobs/`
Her own search is separate. Per her instruction it is **twice weekly (Tuesday and Friday)**, with a recurring 3:00 to 5:00 PM Mountain block on the shechelleb calendar for reviewing and applying; mornings are reserved for the League bootcamp and EDUCAUSE coursework. Apply only to strong fits, no daily pressure. (Note: the scheduler entry itself still carries a daily 6am cron, currently disabled. Worth reconciling.)

On the dashboard, flag what is **NEW vs carried-over** so she does not miss new ones; she has already looked up the old ones.

> **THE `jobs/index.html` PAGE IS NEVER WIPED (hard rule, added 4 Aug 2026 after a session clobbered it).** Published at singletrackmom.github.io/jobs/ (noindex, unlinked, stealth). It is her curated, cumulative list and it is hers.
>
> - **ONLY add new verified-live roles and update existing ones IN PLACE.** Never wholesale-rewrite the page, and never replace it with the contents of another file. The desktop copy `~/Documents/Claude/JobSearch/Michelle_job_dashboard.html` is a SEPARATE curation; the two are allowed to differ, so do NOT overwrite one with the other.
> - **NEVER remove a role** unless she explicitly says it is a bad match, OR the posting is verified closed on the employer's own board. Not on a hunch, not to "clean up."
> - **Before editing, READ the current `jobs/index.html`** (or fetch the live page) first, so you are editing the real current content, not a stale or wrong copy.
> - **Cross-check every role against her applied list** in `~/Documents/Claude/JobSearch/Michelle_job_tracker.xlsx` so you never surface something she already applied to, interviewed for, or was rejected from. When in doubt, ask.
> - Make surgical edits and preserve the existing design. If you cannot recover the real page, ask her before rebuilding. Do not guess.

### DMA Discord jobs agent, `dma-jobs-daily`
Serves her DMA students, not family, and runs DAILY. Same missed-run catch-up rule as the family agents. All of its instructions live in `discord/DMA_JOBS_AGENT.md`.
