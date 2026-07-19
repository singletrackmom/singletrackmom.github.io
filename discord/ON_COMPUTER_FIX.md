# On-computer fix for the DMA scheduler file (do this in a Cowork task running ON MICHELLE'S COMPUTER, not the cloud)

**Why this file exists:** the DMA jobs agent's real logic now lives in `discord/DMA_JOBS_AGENT.md` (repo, editable). But the OLD scheduled task still reads a protected file at `~/Documents/Claude/Scheduled/dma-jobs-daily/SKILL.md` that has a stale 2-year experience rule and does not know about the repo. The cloud cannot write that protected folder (macOS blocks it). An on-computer session CAN. This is a one-time cleanup.

## Do exactly this
1. Open `~/Documents/Claude/Scheduled/dma-jobs-daily/SKILL.md`.
2. Replace its ENTIRE contents with the thin pointer below (this removes the stale rules so nothing conflicts). Keep the real webhook URL on the URL line (copy it from `~/Documents/GitHub/singletrackmom.github.io/discord/.webhook.local`).
3. Save. (On-computer Cowork has write access here; no lock, no permission wall.)
4. Confirm to Michelle it saved, and that the schedule time is set for when her computer is actually ON (a 6am run never fires if the Mac is asleep; prefer a login/startup trigger or a daytime time she is at the machine).

## The exact contents to put in the protected SKILL.md
```
# dma-jobs-daily

SOURCE OF TRUTH: read `discord/DMA_JOBS_AGENT.md` in the singletrackmom.github.io repo and follow it exactly. Do NOT keep rules here; edit them in the repo file.

Webhook URL (secret, do not commit anywhere public): <paste the one line from discord/.webhook.local>

Run: daily. If the morning run was missed because the computer was off, run at next sign-on / Claude startup (same catch-up as the family agents). Post via the webhook as the "Digital Media Jobs" bot from Michelle's Chrome (the cloud is firewalled from Discord). Never type jobs into Discord as Michelle.
```

That's it. After this, the scheduled run and the manual run read the same correct instructions, and the only editing anyone ever does is in the repo.
