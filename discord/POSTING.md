# DMA Jobs Discord - the real posting method (verified working 2026-07-19)

## How the bot posts (THIS is the working way)
Jobs appear as the "Digital Media Jobs" bot by POSTing a Discord webhook from the browser. The daily `dma-jobs-daily` agent does exactly this; Claude can do it too, live, using the Claude-in-Chrome tools.

Steps:
1. Get the webhook URL + embed format from the agent's SKILL.md at `~/Documents/Claude/Scheduled/dma-jobs-daily/SKILL.md`. That folder is protected (a cloud session cannot mount it); open it read-only via Finder/Quick Look with computer-use if you need it. The webhook URL is a SECRET - never write it into this public repo.
2. With claude-in-chrome, navigate a tab to a plain, no-CSP, non-Discord page. `example.com` works. Do NOT use singletrackmom.github.io (its Content-Security-Policy blocks the fetch -> "Failed to fetch"), and NOT discord.com (Discord rejects webhook posts whose Origin is discord.com, error 50067).
3. Run javascript_tool: `fetch(WEBHOOK_URL, {method:"POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify({username:"Digital Media Jobs", embeds:[ ...up to 3... ]})})`. HTTP 204 = success.
4. Embed shape (match exactly): title = "Role, Company (City, ST)" or "(Remote)"; url = direct apply link; description = a bold lead-in then 1-2 factual sentences, no commentary/category; color = 8020096; footer = {"text":"Digital Media Jobs"}.

Gotchas that wasted time before: the github.io origin fails on CSP; the discord.com origin fails with 50067; and the webhook token ends in a capital letter O, not a zero (easy to misread off a screenshot).

## Do NOT
- Do not type a job into Discord as Michelle (posts under her name, wrong).
- Do not hardcode the webhook URL in this repo.

## Filter + files
- Rules: `discord/JOB_RULES.md` (and the agent's own SKILL.md).
- Approved-but-unposted: `discord/queue.json`. Dedupe log: `discord/posted-jobs.json` (append only after a real 204).

## What it is
An AGENT (`dma-jobs-daily`, scheduled, runs on Michelle's Mac) defined by a SKILL.md. Both.
