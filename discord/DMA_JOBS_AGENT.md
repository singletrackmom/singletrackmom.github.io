# DMA Jobs Discord agent (dma-jobs-daily), AUTHORITATIVE INSTRUCTIONS

**This repo file is the ONE source of truth for how the agent runs: filter rules, sourcing, posting method, runbook, and the scheduler fix.** It lives in the repo on purpose so Michelle and Claude can both edit it freely. (`JOB_RULES.md`, `POSTING.md`, and `ON_COMPUTER_FIX.md` were folded into this file on 28 Aug 2026 and deleted. One file for this agent.)

The scheduled task in the protected folder (`~/Documents/Claude/Scheduled/dma-jobs-daily/SKILL.md`) should hold only two things: the secret webhook URL, and one line pointing here ("read `discord/DMA_JOBS_AGENT.md` in singletrackmom.github.io and follow it"). Never edit rules in the protected folder; edit them here.

**Goal:** every day, surface real digital-media jobs a current DMA student or recent grad can actually land, and post them to the DMA Discord #jobs board as the "Digital Media Jobs" bot.
**Audience:** GCC DMA students and recent grads (some have professional work already, some are building their first portfolio).
**Process:** dedupe, search, hard-filter on level and pay realism plus the experience cap, then post via webhook from Michelle's browser. Details below.

## Schedule (bulletproof)
Runs DAILY. It is scheduled in the morning, but Michelle's computer is often off overnight, so if the morning run was missed, run it as soon as she signs on / as soon as Claude starts, same catch-up rule as the family agents. This one is daily (not twice-weekly like her own job search) because it serves all her students.

## STEP 1, Dedupe
Read `discord/posted-jobs.json`. Never repost anything already logged there. `discord/queue.json` is the approved-but-unposted queue.

---

# STEP 2, THE FILTER

**Updated 2026-08-27. Read the LEVEL AND PAY REALISM section first, it overrides anything below it that conflicts.**

## LEVEL AND PAY REALISM (added 27 Aug 2026 after two bad posts)

These are community college students, most of them still enrolled. Post work they can actually get.

- **Internships and part-time work are the TARGET, not the fallback.** These students are enrolled and most of them are working already. **At least two of any three posts should be an internship or part-time.** A run that posts three full-time salaried roles has missed, even if all three pass every other filter.
- **NO STRETCH ROLES.** The old "(stretch role)" label is **retired**. Do not use it, and do not post anything that would need it.
- **Experience: zero to one year. Reject two or more**, required or preferred. If a posting does not state a number, it must read unmistakably as entry level or the answer is no.
- **Reject any title containing** senior, lead, principal, manager, director, head of, or specialist II and up.
- **PAY CEILING: do not consider a role advertising $55,000 or more.** Tightened 4 Sept 2026, from $75,000, at Michelle's direction. Her words: a $60,000 posting is a real full-time professional job and these students are not going to get it. A title that says junior attached to a salary that says otherwise means the title is lying.
- **Believable range:** roughly $16 to $24 an hour, or roughly $33,000 to $48,000 a year. Internships may be hourly, part-time, unpaid-for-credit, or seasonal.
- **When in doubt, aim lower.** A part-time $18/hour design assistant post that three students apply to is worth more than a polished full-time role none of them will get. The failure mode of this agent has always been aiming too high.

**Why this section exists.** On 27 Aug 2026 the agent posted a "Junior Editor" at $100,000 to $125,000 and a 3+ year designer role labeled a stretch. Both cleared the experience-cap rule below, because that rule only tests years against schooling and has no test for seniority or pay. Both were pulled (removed via webhook PATCH the same day; do not repost either). The cap rule alone is not sufficient; this section is the missing filter.

## The experience / education cap (original rules, 19 July 2026)

Canonical statement of who these jobs are for. The agent surfaces jobs a current DMA student or recent grad can realistically land, counting their schooling as real experience (students build portfolio work while enrolled).

Cap on the experience a job may require = **4 years minus the experience the job's REQUIRED schooling already represents.**

- Requires only **high school diploma / GED** (no degree): accept up to **4 years** of required or preferred experience.
- Requires or accepts an **associate degree / "some college" / community college**: accept up to **2 years** of required or preferred experience.
- **Bachelor's degree REQUIRED**: reject. (Bachelor's "preferred" is fine.)
- **Internship or entry-level**: always accept.

Reasoning: a student's roughly 4 years of college counts toward the experience bar, so a high-school-only job asking for a few years of experience is still reachable. An associate-level job already credits about 2 of those years, so it should ask for no more than about 2 additional.

Reject if required experience exceeds the cap for its education level (for example HS + 5 years, or associate + 3 years), or if the role is not digital-media relevant.

> ⚠️ **SUPERSEDED 4 SEPTEMBER 2026. Kept for the reasoning, not for the numbers.**
>
> This section's sliding cap is what let full-time professional roles through: it permits up to 4 years of experience for a job that asks only for a high school diploma, which describes a great many real, full-time, competitive jobs. **The LEVEL AND PAY REALISM section above wins outright.** Zero to one year, under $55,000, internships and part-time preferred over full-time. Where the two disagree, this one loses. Do not average them.

## Scope
Entry-level / early-career digital media: motion graphics, graphic design, video and editing, animation, UI/UX, web design, illustration, game design. Plus a software sweep: Photoshop, Illustrator, InDesign, After Effects, Premiere, Figma, Cinema4D, Blender, Unity. Prefer Arizona (Phoenix metro) and remote; national remote is fine.

## Language
Say **"portfolio,"** never "student portfolio." Many of these students have real professional work; a portfolio requirement (student or professional) is fine.

---

# STEP 3, WHERE TO SOURCE

Corporate ATS boards alone (Ashby, Greenhouse, Lever, Workable) skew toward the wrong end of the market and are what produced the bad posts on 27 Aug 2026. Search creative-industry and local sources FIRST. Look EVERYWHERE, not just one or two boards.

1. **Local Phoenix metro, highest value.** AIGA Arizona, Valley agencies and studios, sports organizations, ASU and the Maricopa colleges, school districts, hospital systems, credit unions, resorts and hospitality groups, Valley-headquartered retail and restaurant chains, print and sign shops, local news and media. AZ sports orgs on TeamworkOnline (Arizona Cardinals, Phoenix Suns / Mercury / Player 15 Group, Arizona Diamondbacks), plus the ASU and Grand Canyon University job boards.
2. **Creative boards:** AIGA Design Jobs, Behance JobList, Dribbble Jobs, Coroflot, Authentic Jobs, We Work Remotely (design), ArtStation (game and animation), Creativepool.
3. **Video and motion:** ProductionHUB, Mandy, Stage 32, Free The Work. (Motion Hatch is also worth a look.)
4. **Games and animation:** Hitmarker, ArtStation Jobs.
5. **Creative staffing:** Aquent, 24 Seven Talent, Robert Half Creative, Onward Search, Profiles.
6. **ATS boards (reliable, verifiable, deep-linkable):** Greenhouse, Lever, Ashby. Easiest to confirm live and link straight to the real apply page, but see the warning above about the level skew.
7. **Sports beyond AZ:** TeamworkOnline nationally (lots of entry-level and internship motion, design, and video roles), good for portfolio-building even if out of state.
8. **LinkedIn, Indeed, ZipRecruiter, Glassdoor, Monster:** discovery ONLY, never the published link.

**Known dead or useless as of 27 Aug 2026:** Krop (portfolio builder only now), Working Not Working /jobs (404), Communication Arts design jobs (404), Motionographer board (gone), Creative Circle (rebranded to Everforth, old URLs 404). Aquent and Vitamin T list no Arizona roles at all. ArtStation and Coroflot return zero for Arizona. Behance JobList is mostly anonymous freelance gigs with no employer to verify against.

## ALWAYS POST THE DIRECT COMPANY LINK (hard rule, Michelle, Aug 2026)
The published apply link must ALWAYS go to the company's OWN website or application page, never a third-party job-search site. Michelle's reason: third-party sites make students create accounts and then spam them endlessly. So when you find a role on any board (a creative board, an aggregator, anywhere), trace it back to the employer's own careers page and post THAT link.

Example done right: We Work Remotely listed LooseGrip's Junior Designer behind a WWR signup wall, but LooseGrip's own site (loosegrip.net/join-our-team/junior-designer) had a direct application form, so we posted the company link, not the WWR one.

If you genuinely cannot find a direct company apply page (only a gated third-party link exists), treat it as a **lead**, not a post. Some creative boards gate the apply link behind a free account (We Work Remotely, Dribbble); same rule applies.

**Exception:** sports orgs' TeamworkOnline pages are OK. TeamworkOnline is the employer's actual applicant-tracking system, like Greenhouse or Workday, not a spammy aggregator.

**Aggregators = LEADS ONLY, never the published link.** Indeed, LinkedIn, ZipRecruiter, Glassdoor, and Monster: listings go stale, many are reposts or staffing-agency posts, and you cannot reliably deep-link the real apply page. Use them only to discover a role, then find and verify the posting on the company's OWN board before posting. **Dice** is IT / software-developer focused and mostly off-target for DMA creatives; only check it for the occasional UI/UX or game-programming role.

---

# STEP 4, POST AS THE BOT (verified working method)

Jobs appear as the "Digital Media Jobs" bot by POSTing a Discord webhook **from the browser**. The scheduled agent does exactly this; Claude can do it too, live, using the claude-in-chrome tools.

1. **Get the webhook URL from `discord/.webhook.local`.** It is one line starting with `https://discord.com/api/webhooks/`. That file is git-ignored and the URL is a SECRET, never commit it to this public repo and never paste it into a chat. Do NOT open the protected `~/Documents/Claude/Scheduled/` folder and do NOT use computer-use / screen control to get it. It lives in the repo now.
2. **The post must go out through Michelle's browser.** Anthropic's cloud is FIREWALLED off Discord, so a curl or fetch from the cloud container or from bash will always fail. Use claude-in-chrome.
3. **Navigate a tab to a plain, no-CSP, non-Discord page.** `example.com` works. Do NOT use singletrackmom.github.io (its Content-Security-Policy blocks the fetch, "Failed to fetch") and NOT discord.com (Discord rejects webhook posts whose Origin is discord.com, error 50067).
4. **Run javascript_tool:**
   ```js
   fetch(WEBHOOK_URL + "?wait=true", {
     method: "POST",
     headers: {"Content-Type": "application/json"},
     body: JSON.stringify({username: "Digital Media Jobs", embeds: [ /* up to 3 */ ]})
   }).then(r => r.json())
   ```
   **Use `?wait=true`** so Discord returns the created message object. **Capture the message `id`** and save it with the job in `discord/posted-jobs.json`, because that id is the only way to edit or remove a post later when a role closes:
   ```js
   fetch(WEBHOOK_URL + "/messages/" + MESSAGE_ID, {
     method: "PATCH",
     headers: {"Content-Type": "application/json"},
     body: JSON.stringify({embeds: [ /* the remaining jobs */ ]})
   })
   ```
   **HTTP 204 (plain POST) or 200 (with `?wait=true`) means success.** The webhook token ends in a capital letter **O**, not a zero (easy to misread off a screenshot).
5. **Embed shape (match exactly):**
   - `title` = "Role, Company (City, ST)" or "(Remote)"
   - `url` = the direct company apply link
   - `description` = a bold lead-in then 1 to 2 factual sentences, no commentary and no category label
   - `color` = 8020096
   - **NO footer.** The bot already posts as "Digital Media Jobs," so a "Digital Media Jobs" footer is redundant (Michelle, Aug 2026). Leave the footer field off entirely.
6. **After a real 204 or 200, append the job (with its message id) to `discord/posted-jobs.json`.**

## Do NOT
- Do NOT type a job into Discord as Michelle. It posts under her name, which is wrong.
- Do NOT hardcode the webhook URL anywhere in this public repo.

---

# RUNBOOK, if anything breaks, read THIS first (do not improvise for hours)

**Hard rule: if a step fails twice, STOP and tell Michelle exactly what failed, which fix below you tried, and what you need. Do NOT take over her screen and do NOT burn more than a few minutes. She has explicitly said she will not sit through a long fight again.**

Pre-flight self-check (do these before posting):
1. Confirm `discord/.webhook.local` exists and is one line starting with `https://discord.com/api/webhooks/`.
2. Confirm `discord/posted-jobs.json` loads (for dedupe).

Known failure, known fix:

- **Cloud says "Failed to fetch" / connection refused / 403 posting to Discord.** Expected: Anthropic's cloud is firewalled off Discord. NEVER try to curl or fetch the webhook from the cloud container or from bash. The post can ONLY go out through Michelle's browser via claude-in-chrome. If claude-in-chrome is not connected, tell her that is the blocker, do not flail.
- **Browser fetch fails with "Failed to fetch" from her Chrome.** The tab origin is wrong. Navigate the tab to `example.com` first. Do NOT run the fetch from singletrackmom.github.io (CSP blocks it) and NOT from discord.com (Origin rejected, error 50067).
- **HTTP 401 / 50027 invalid token.** The webhook URL is mis-read. The token ends in a capital letter **O**, not a zero. Re-copy from `discord/.webhook.local`, do not retype by hand.
- **It posted under Michelle's name instead of the bot.** You typed into Discord instead of using the webhook. NEVER type a job into Discord. Always POST the webhook with `username:"Digital Media Jobs"`.
- **A posted role turns out to be bad or closed.** PATCH the message using the saved message id (see STEP 4). That is how the 27 Aug bad posts were pulled.
- **You are tempted to edit the agent rules and the file "won't save."** That is the OLD protected `SKILL.md` in `~/Documents/Claude/Scheduled/`. macOS blocks all writes there from a cloud session. Do NOT try. Edit THIS repo file instead (it is the source of truth); the protected file only holds a pointer plus the secret URL.

Success signal: the webhook POST returns HTTP 204 (or 200 with `?wait=true`). Only then append the job(s) to `discord/posted-jobs.json`.

---

# ON-COMPUTER FIX for the scheduler file (one-time cleanup)

**Do this in a Cowork task running ON MICHELLE'S COMPUTER, not the cloud.**

**Why:** the agent's real logic now lives in this repo file. But the OLD scheduled task may still read a protected file at `~/Documents/Claude/Scheduled/dma-jobs-daily/SKILL.md` that has a stale 2-year experience rule and does not know about the repo. The cloud cannot write that protected folder (macOS blocks it). An on-computer session CAN.

1. Open `~/Documents/Claude/Scheduled/dma-jobs-daily/SKILL.md`.
2. Replace its ENTIRE contents with the thin pointer below (this removes the stale rules so nothing conflicts). Keep the real webhook URL on the URL line, copied from `~/Documents/GitHub/singletrackmom.github.io/discord/.webhook.local`.
3. Save. (On-computer Cowork has write access here; no lock, no permission wall.)
4. Confirm to Michelle it saved, and that the schedule time is set for when her computer is actually ON (a 6am run never fires if the Mac is asleep; prefer a login/startup trigger or a daytime time she is at the machine).

The exact contents to put in the protected SKILL.md:

```
# dma-jobs-daily

SOURCE OF TRUTH: read `discord/DMA_JOBS_AGENT.md` in the singletrackmom.github.io repo and follow it exactly. Do NOT keep rules here; edit them in the repo file.

Webhook URL (secret, do not commit anywhere public): <paste the one line from discord/.webhook.local>

Run: daily. If the morning run was missed because the computer was off, run at next sign-on / Claude startup (same catch-up as the family agents). Post via the webhook as the "Digital Media Jobs" bot from Michelle's Chrome (the cloud is firewalled from Discord). Never type jobs into Discord as Michelle.
```

After this, the scheduled run and the manual run read the same correct instructions, and the only editing anyone ever does is in the repo.

---

## What this is
An AGENT (`dma-jobs-daily`, scheduled, runs on Michelle's Mac) defined by a SKILL.md that points at this file. Both an agent and a skill.

## Related files
- Webhook URL (secret, git-ignored): `discord/.webhook.local`
- Approved-but-unposted queue: `discord/queue.json`
- Dedupe log (append only after a real 204/200): `discord/posted-jobs.json`
- Public case-study page: `discord/overview.html`
