# DMA Jobs Discord agent (dma-jobs-daily) - AUTHORITATIVE INSTRUCTIONS

**This repo file is the source of truth for how the agent runs.** It lives in the repo on purpose so Michelle and Claude can both edit it freely. The scheduled task in the protected folder (`~/Documents/Claude/Scheduled/dma-jobs-daily/SKILL.md`) should hold only two things: the secret webhook URL, and one line pointing here ("read discord/DMA_JOBS_AGENT.md in singletrackmom.github.io and follow it"). Never edit rules in the protected folder; edit them here.

**Goal:** every day, surface real digital-media jobs a current DMA student or recent grad can actually land, and post them to the DMA Discord #jobs board as the "Digital Media Jobs" bot.
**Audience:** GCC DMA students and recent grads (some have professional work already, some are building their first portfolio).
**Process:** dedupe, search, hard-filter by the experience cap, then post via webhook. Details below.

## Schedule (bulletproof)
Runs DAILY. It is scheduled in the morning, but Michelle's computer is often off overnight, so if the morning run was missed, run it as soon as she signs on / as soon as Claude starts, same catch-up rule as the family agents. This one is daily (not twice-weekly like her own job search) because it serves all her students.

## STEP 1 - Dedupe
Read `discord/posted-jobs.json`. Never repost anything already logged there.

## STEP 2 - Search
Find entry-level / early-career digital media jobs: motion graphics, graphic design, video/editing, animation, UI/UX, web design, illustration, game design. Software sweep counts as relevant: Photoshop, Illustrator, InDesign, After Effects, Premiere, Figma, Cinema4D, Blender, Unity. Prefer Arizona (Phoenix metro) and remote; national remote is fine.

## STEP 3 - Hard filter (THE experience cap - updated 19 July 2026)
Cap on required experience = **4 years minus the experience the job's REQUIRED schooling already represents**, because a student's ~4 years of college counts as real experience (they build portfolio work while enrolled).

- Requires only **high school diploma / GED** (no degree): accept up to **4 years** required/preferred experience.
- Requires or accepts an **associate / "some college" / community college**: accept up to **2 years**.
- **Bachelor's degree REQUIRED**: reject. (Bachelor's "preferred" is fine.)
- **Internship / entry-level**: always accept.

Reject if required experience exceeds the cap for its education level (e.g. HS + 5 years, or associate + 3 years), or if the role is not digital-media relevant.

Say **"portfolio,"** never "student portfolio." Many of these students have real professional work; a portfolio requirement (student or professional) is fine.

A role that passes but is titled "senior" or is a clear stretch may be labeled **"(stretch role)"** so students read it as aspirational.

## STEP 4 - Post as the bot (verified working method)
1. Get the webhook URL from the protected SKILL.md (read-only; it is a SECRET, never commit it to this public repo).
2. With claude-in-chrome, navigate a tab to a plain non-Discord, no-CSP page. `example.com` works. Do NOT use singletrackmom.github.io (its CSP blocks the fetch) and NOT discord.com (Origin rejected, error 50067).
3. Run javascript_tool:
   `fetch(WEBHOOK_URL, {method:"POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify({username:"Digital Media Jobs", embeds:[ ...up to 3... ]})})`
   HTTP **204 = success**. (The webhook token ends in a capital letter O, not a zero.)
4. Embed shape (match exactly): title = "Role, Company (City, ST)" or "(Remote)"; url = direct apply link; description = a bold lead-in then 1-2 factual sentences (no commentary); color = 8020096; footer = {"text":"Digital Media Jobs"}.
5. After a real 204, append the job to `discord/posted-jobs.json`.

## Do NOT
- Do NOT type a job into Discord as Michelle (it posts under her name, wrong).
- Do NOT hardcode the webhook URL anywhere in this public repo.

## RUNBOOK - if anything breaks tomorrow, read THIS first (do not improvise for hours)

**Hard rule: if a step fails twice, STOP and tell Michelle exactly what failed, which fix below you tried, and what you need. Do NOT take over her screen and do NOT burn more than a few minutes. She has explicitly said she will not sit through a long fight again.**

Pre-flight self-check (do these before posting):
1. Confirm `discord/.webhook.local` exists and is one line starting with `https://discord.com/api/webhooks/`. That is the URL. Do NOT open the protected `~/Documents/Claude/Scheduled/` folder, do NOT use computer-use / screen control to get it. It lives in the repo now.
2. Confirm `discord/posted-jobs.json` loads (for dedupe).

Known failure -> known fix:
- **Cloud says "Failed to fetch" / connection refused / 403 posting to Discord.** This is expected: Anthropic's cloud is FIREWALLED off Discord. NEVER try to curl/fetch the webhook from the cloud container or from bash. The post can ONLY go out through Michelle's browser via claude-in-chrome. If claude-in-chrome is not connected, tell her that is the blocker, do not flail.
- **Browser fetch fails with "Failed to fetch" from her Chrome.** The tab origin is wrong. Navigate the tab to `example.com` first. Do NOT run the fetch from singletrackmom.github.io (its CSP blocks it) and NOT from discord.com (Discord rejects Origin discord.com, error 50067).
- **HTTP 401 / 50027 invalid token.** The webhook URL is mis-read. The token ends in a capital letter **O**, not a zero. Re-copy from `discord/.webhook.local`, do not retype by hand.
- **It posted under Michelle's name instead of the bot.** You typed into Discord instead of using the webhook. NEVER type a job into Discord. Always POST the webhook with `username:"Digital Media Jobs"`.
- **You are tempted to edit the agent rules and the file "won't save."** That is the OLD protected `SKILL.md` in `~/Documents/Claude/Scheduled/`. macOS blocks all writes there from a cloud session. Do NOT try. Edit THIS repo file instead (it is the source of truth); the protected file only holds a pointer + the secret URL.

Success signal: the webhook POST returns **HTTP 204**. Only then append the job(s) to `discord/posted-jobs.json`.

## Related files
- Filter detail: `discord/JOB_RULES.md`
- Posting playbook + gotchas: `discord/POSTING.md`
- Approved-but-unposted queue: `discord/queue.json`
- Dedupe log: `discord/posted-jobs.json`
