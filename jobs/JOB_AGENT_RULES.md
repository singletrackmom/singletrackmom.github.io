# Job search rules

These are the only rules for Michelle’s job search. One scheduled task, “Job search,” reads this file every run. Nothing else holds targeting rules. To change a rule, change it here, once. Rewritten 7 Nov 2026 from a 521-line file that contradicted itself.

**Goal:** one page, every morning, of every open role worth Michelle’s time, rated honestly, best first.
**Audience:** Michelle, reading jobs/index.html on her phone.
**Process:** the daily task reads this file and TARGET_COMPANIES.md, searches every source in the tier order in section 7, verifies each lead on the employer’s own posting, rates it, edits jobs/index.html, and emails her a short summary.

## 1. What goes on the page

A role in her lanes (section 3), rated strictly against the posting’s stated minimum qualifications (section 5), at 2 stars or more, with no dealbreaker (section 4).

- AI is not required. A posting that mentions AI or innovation can earn more stars (section 5). Search “innovation” everywhere; it often means AI.
- Education is not required. It raises rank. A role outside education gets the OUTSIDE ED tag.
- Pay has no floor for Colorado and remote roles. Relocation roles need $80,000 or more (section 2). Always show the band, or “pay not posted.”

## 2. Where

- **Colorado:** any arrangement, on site, hybrid or remote. Denver, Boulder, Golden and short drives first.
- **US remote** that allows Colorado. Check the application form’s state question.
- **Relocation zone, on site, only at a strong 4 or 5 stars AND posted pay of $80,000 or more** (no posted pay means it stays off): Washington, Oregon, Ann Arbor (Michigan), California within about an hour of Lake Tahoe or San Diego, New Mexico, Flagstaff (NAU, Coconino CC), Colorado mountain towns (Durango, Glenwood Springs, Carbondale, Salida, Gunnison, Steamboat, Grand Junction) and Utah. She is more likely to move to the first places on that list than to Salt Lake City.
- **Google for Education (higher ed) and Gemini for Education, any US location:** she would move for it (Michelle, 7 Nov 2026). Search Google Careers every run for “higher education,” “Gemini for Education,” “Google for Education,” “Gemini adoption,” “education,” “learning technology,” “learning experience,” “AI transformation” and “program manager learning,” US locations. Higher-ed and Gemini for Education roles follow this Google rule; every other Google role follows the normal geography and star rules. Every match she clears the minimums for goes on the board at 2 stars or more, with no pay floor and no star floor. Each one sits at the very top of the page with a “GOOGLE · apply today” flag, and “GOOGLE JOB” leads the email subject the same day it’s found. Leave off pure sales roles (titles with Sales Representative or Account Executive) and anything with heavy travel; keep Solutions Engineer, adoption, learning and program roles.
- **Arizona:** remote roles only, plus on-site roles at the Maricopa district.
- Nowhere else on site: no other part of California, no East Coast, no other states.

## 3. Lanes, ranked

1. AI enablement, AI adoption, AI innovation, AI program or solutions manager, digital transformation, innovation manager or director. Solutions engineer, solutions architect, implementation and forward-deployed roles at edtech and AI companies count here too, as long as they pass the dealbreakers (no required coding, no sales quota, under about 25 percent travel).
2. Faculty development and teaching-center roles.
3. Instructional design, learning experience design, academic and learning technology, online learning. Corporate learning design counts here too (building courses, simulations and media for a company’s employees): in, as long as the job is building it, not delivering it (Michelle, 7 Nov 2026: “building corporate training would be fine if they pay me”).
4. UX research, service design and product discovery.
5. Product operations and edtech product roles.
6. Edtech implementation, onboarding and customer success, individual contributor.

## 4. Dealbreakers, the complete list

Cut the role, whatever else is true, if it has any of these:

- Required coding, Python or SQL (listed as preferred is fine).
- A developer or software engineering role (writing production code is the job).
- Selling it herself or a quota. Pre-sales is fine: demos, pilots, proofs of concept and technical answers while a customer decides (Michelle, 8 Nov 2026).
- Contract, fixed-term, temporary or grant-limited.
- About 25 percent travel or more.
- Managing more than about 5 people, or managing managers.
- A trainer title, or delivering training as the whole job.
- K-12 required.
- A degree she does not hold, such as a PhD or a CS degree.
- A stated minimum of recent product management years.

## 5. Stars, the only scale

Rate against the stated minimum qualifications. Be strict. Judge her experience only from her CV at `~/Documents/Claude/JobSearch/cv.html` (private, outside the repo; in device_bash `$HOME/mnt/JobSearch/cv.html`), her one source of truth; read it every run, and never assume a gap without searching it. **No CV, no ratings:** if that file cannot be opened, do not rate or add any card, never fall back to another copy (anything in `_to_delete/` is stale), and lead the email subject with “CV NOT READ”.

- ★★★★★ She clears every minimum and most preferred qualifications, it is lane 1, Colorado or remote, no real gap.
- ★★★★ She clears every minimum, with one soft gap (a preferred skill).
- ★★★ She clears the minimums on paper, with a real hole (wrong industry, low pay).
- ★★ A stretch on experience: a hard years gate she does not meet.
- ★ Does not fit. One line in the run notes, no card.

**Dream-job match.** A higher-ed or edtech AI enablement role modeled on the Mines AI Solutions Manager (AI intake, prototyping, requirements, adoption and rollout; titles like AI Solutions Manager, AI Enablement Lead, AI Solutions Lead, AI Acceleration), or Google’s Gemini Adoption Solutions Engineer or Solutions Engineer, Higher Education, in Colorado, remote, or any US location for Google, where she clears the minimums, is automatically 5 stars and leads the email subject as “DREAM JOB” (Michelle, 8 Nov 2026).
**AI boost.** A posting that mentions AI or innovation can go to 5 stars. One that mentions neither tops out at 4 stars.
**Faculty development floor.** A Colorado faculty development or teaching-center role where she clears the minimums is at least 4 stars, AI or not.
**5 stars is an emergency:** top of the page with a “5 stars, don’t pass this up” flag, and “5-STAR JOB” leads the email subject.

## 6. Order on the page

LOCAL (Colorado) section first, then REMOTE & ONLINE, then RELOCATION, ON SITE (the `dream` section). Inside each section: stars, then lane, then AI. Rank badges run #1 to #N straight down the page. Each section header shows its count. Renumber every run.

## 7. Sources

Work in this order. Tiers 1 and 2 run every day, no exceptions. If time runs short, cut from tier 3, never from tiers 1 or 2.

**Tier 1, scripted, every run.** Every scripted board in TARGET_COMPANIES.md through its public feed (Ashby, Greenhouse, Lever, Workday, SmartRecruiters, Workable), including the Colorado Workday schools (Mines, MSU Denver, CSU, Colorado Mesa, Fort Lewis, Western, Adams, Aims, Colorado Mountain College), CCCS, and every job alert email since the last run (LinkedIn, HigherEdJobs, Built In, Google Careers and others; some arrive forwarded from her second Gmail). Google Careers alerts (her saved searches for “higher education,” “Google for Education” and “Gemini for Education”) come from Google Careers to her main Gmail; open every job in them on Google’s own posting and rate it under the Google rule in section 2.

**Tier 2, Chrome, every run, before anything else in Chrome.** The “Priority Chrome, every run” list in TARGET_COMPANIES.md: CU Boulder, CU Taleo (Denver, Anschutz, UCCS, System), University of Denver, HigherEdJobs, the EDUCAUSE Career Center, signed-in LinkedIn (Denver 35 miles and US remote, since the last run), Built In Colorado and AcademicCareers.com. Read every page of results, not just page one, and record the count read for each.

**Tier 3, Chrome, rotating.** The three rotation groups in TARGET_COMPANIES.md (A: edtech and vendor boards; B: nonprofits, associations and the no-board companies; C: relocation-zone universities). Run the group for today: day of the month 1, 4, 7 … is A; 2, 5, 8 … is B; 3, 6, 9 … is C (that is, (day − 1) mod 3: 0 = A, 1 = B, 2 = C). Every source gets read at least every three days. If a group was skipped, it runs first the next day.

**Script first, even for “Chrome” boards.** The device_bash shell on Michelle’s Mac reaches boards the cloud sandbox cannot (11 Nov 2026). Before opening a board in Chrome, try the script route listed beside it in TARGET_COMPANIES.md: CU Boulder, CU Taleo and DU pages; ADP boards through `https://workforcenow.adp.com/mascsr/default/careercenter/public/events/staffing/v1/job-requisitions?cid=<cid>&ccId=19000101_000001&lang=en_US`; Jibe boards (Ellucian, McGraw Hill) through `/api/jobs`; Ashby, Greenhouse, Lever, Workable and Pinpoint through their JSON feeds. Chrome is for what a script cannot read.

**Nothing is skipped silently.** Every tier 2 source and every source in today’s rotation group either gets a count in the run notes or goes on a “Skipped today” line with the reason (would not load, login, CAPTCHA, ran out of time). **A partial read is a skip:** “24 of 88” goes on the Skipped line too, with the count read.

**Named targets, every run, by name.** Instructure, Google, BoodleBox, Element451, Playlab, D2L, Bevel, Alchemy, EDUCAUSE, Mines, CU (all campuses), DU and MSU Denver each get their own line in the run notes and the email: “read · <n> open · <n> in lane”, or “NOT READ” with the reason. Every in-lane role at a named target is rated in writing (added, or left off with the reason), never passed over silently.

**Time goes to finding jobs.** Do not re-check every card every day. Once a week (Mondays), prune the board: re-open each card’s posting and remove the closed ones. On other days, re-check only cards that close within 7 days. Tier 2 sources are read in full before any pruning.

**Search terms:** AI Solutions Manager, AI Enablement Lead, AI Solutions Lead, AI Acceleration, Gemini Adoption Solutions Engineer, AI, artificial intelligence, innovation, AI enablement, AI adoption, digital transformation, faculty development, educational developer, teaching and learning, instructional design, learning experience, learning designer, academic technology, online learning, UX research, service design, product operations, implementation, customer success.

**CU (any campus).** CU’s dependent tuition benefit matters to her (“anything for CU entry,” 10 Nov 2026). A CU role she clears the minimums for goes on the board at 2 stars or more with no pay floor.

## 8. Never list

- Anything on the Google Sheet “Applied jobs (Claude reads this)” (file id 1Giv6HSPmQuNcTR-wWqhkQ4in4MzG9pRFzP71HGd9kyc) or its “Not applied” tab. Read both every run.
- Anything with a folder in the Drive folder “Job Applications (Claude drafts)” (folder id 1tp7P_E0c2hwBNlRN0sZVb1GEAl_lWZHV).
- A role she has an application-received email for (add it to the sheet if missing).
- A role she took off the page herself. When she takes one off, add it to the Not applied tab.

## 9. Links

Every Apply link is the deep link to that one posting on the employer’s own careers page or ATS, opened and seen live today. Never a job board, a search page, a bare careers page or an aggregator. A Workday or iCIMS page that comes back empty to a script is not dead; open it in Chrome.

## 10. Cards

Every card is `<details class="card local|remote|dream">`. Keep the existing markup and CSS.

Every card carries `id="r<rank>"` matching its rank badge (#29 is `id="r29"`). After sorting and renumbering, rewrite every card’s id to match its new rank, so the email’s jump links land on the right card.

Visible line, in this order: the stars (`<span class="stars" aria-label="Four out of five stars">&#9733;&#9733;&#9733;&#9733;&#9734;</span>`, always five glyphs), then a badge only for NEW <D MON>, CLOSES <D MON>, OUTSIDE ED or STRETCH (2 stars), then the title in `<h3 class="jt">`, then one `<span class="sub">` line: employer in bold, location, pay, closing date. Every card shows the closing or application-deadline date whenever the posting gives one (“Closes 22 Nov”), or “no close date posted.” Add a CLOSES badge when it is within 7 days.

Inside, in this order:
1. Two to four short bullets on what the job is.
2. **Strong:** the skills and requirements from the posting that match, in the posting’s own words, as a short comma-separated list.
3. **Light:** the requirements she may not meet, worded as the posting words them, or “Nothing material.”
4. The Apply link, alone in `.foot`.

Nothing on a card describes Michelle: no projects, titles, years, “your” or “you have.” About 120 words inside the card at most.

## 11. The page

- Edit jobs/index.html surgically. Never rewrite or wipe it.
- Remove a card only when the posting is verified closed, she applied, or she took it off. Never remove a YOUR PICK card unless it closed, and never change stars she set herself.
- Insert a card inside its section, never after it. After every edit: no repeated titles, and card count equals rank-badge count.
- Nothing between the header and the first card.
- One dated line per run in the run-notes block at the bottom: what was searched, added, removed, left off and why (one line each for 1-star roles), and anything that couldn’t be read.
- Run python3 tools/preflight.py. It must pass.
- Never run git. Michelle commits and pushes.

## 12. The email

One email to Michelle’s personal Gmail (the address is in the task prompt, never in this public file) per run. **Always send `htmlBody` built from the template below.** A plain-text-only email is a failed run. `body` is only a three-line fallback: the counts, “Open the full board: michelleblomberg.com/jobs/”, and the subject’s warnings.

Subject: “Job search · <Weekday D Month> · <n> new”, or “· no changes”, or “5-STAR JOB · <Employer> · Job search · <Weekday D Month>”, or “GOOGLE JOB · <Title> · Job search · <Weekday D Month>” (a Google job wins the subject over a 5-star one). “CV NOT READ” leads any subject when the CV could not be opened. When any tier 2 source or named target was skipped or only partly read, end the subject with “· <n> sources not read”.

**Links:** every link is an `<a>` with words (the job title, “Open the full board,” “View the thread”). Never paste a bare URL anywhere in the email. Never a google.com/url redirect; link the real posting URL.

**Hierarchy, top to bottom:** the number of new jobs, big. Then the board button. Then new jobs, best stars first, each title bold and linked. Then closing soon, removed, needs your reply. Then targets. Then the small gray footer. Leave out any section with nothing in it, except Targets.

**Template.** Fill the {…} slots. Repeat a job block per job. Inline styles only, Arial, the site palette (plum #7a5080, sage #456546, ink #26221f, muted #6d635f, lines #e5ddd1), no gradients, no images.

```html
<div style="font-family:Arial,sans-serif;color:#26221f;max-width:600px;margin:0 auto;font-size:15px;line-height:1.45">
  <p style="margin:0;font-size:40px;font-weight:bold;color:#7a5080;line-height:1">{n} new</p>
  <p style="margin:4px 0 18px;color:#6d635f">{n} removed · {n} on the board</p>
  <p style="margin:0 0 24px"><a href="https://michelleblomberg.com/jobs/" style="background:#7a5080;color:#fff;padding:10px 18px;text-decoration:none;font-weight:bold;display:inline-block">Open the full board</a></p>

  <h2 style="font-size:18px;margin:0 0 10px;color:#7a5080;border-bottom:2px solid #e5ddd1;padding-bottom:4px">New today</h2>
  <!-- one block per new job, best stars first -->
  <div style="margin:0 0 14px">
    <div style="color:#7a5080;font-size:16px">{★★★★☆} <span style="color:#6d635f;font-size:13px">#{rank}</span></div>
    <a href="{real posting URL}" style="font-weight:bold;font-size:16px;color:#26221f">{Title}</a>
    <div style="color:#6d635f;font-size:14px">{Employer} · {location} · {pay} · {Closes D Mon or no close date posted}</div>
    <div style="font-size:14px">{one line on what the job is} <a href="https://michelleblomberg.com/jobs/#r{rank}" style="color:#456546">See card</a></div>
  </div>

  <h2 style="font-size:18px;margin:20px 0 10px;color:#7a5080;border-bottom:2px solid #e5ddd1;padding-bottom:4px">Closing within 7 days</h2>
  <p style="margin:0 0 6px"><b><a href="https://michelleblomberg.com/jobs/#r{rank}" style="color:#26221f">{Title}</a></b> · {Employer} · closes {D Mon}</p>

  <h2 style="font-size:18px;margin:20px 0 10px;color:#7a5080;border-bottom:2px solid #e5ddd1;padding-bottom:4px">Needs your reply</h2>
  <p style="margin:0 0 6px"><b>{Employer}</b>: {what they want} · <a href="{thread link}" style="color:#456546">View the thread</a></p>

  <h2 style="font-size:18px;margin:20px 0 10px;color:#7a5080;border-bottom:2px solid #e5ddd1;padding-bottom:4px">Removed</h2>
  <p style="margin:0 0 6px;color:#6d635f">{Employer} · {Title} ({filled, closed or applied})</p>

  <h2 style="font-size:18px;margin:20px 0 10px;color:#7a5080;border-bottom:2px solid #e5ddd1;padding-bottom:4px">Targets</h2>
  <p style="margin:0 0 4px"><b>{Target}</b> · read · {n} open · {n} in lane</p>
  <p style="margin:0 0 4px;color:#7a5080"><b>{Target} · NOT READ</b> ({reason})</p>

  <p style="margin:24px 0 0;font-size:12px;color:#6d635f">Push jobs/ in GitHub Desktop to publish today’s changes.<br>Skipped today: {list, or nothing}.<br>{Problems: … only if something broke}</p>
</div>
```

Rank numbers in the email must match the page after the run’s final renumbering.

## Writing

No em dashes, no exclamation points, curly quotes (as HTML entities on the page), never “genuinely” or “straightforward.” Never say she led an LMS migration.
