# Fixing the stuck "Relaunch to update" on the Claude desktop app (Mac)

**Your situation:** you shut down every night, open in the morning, and Claude never actually updates even though the "Relaunch to update" banner keeps showing. This is a **known bug**, not something you're doing wrong. It's documented in Anthropic's own issue tracker.

## What's happening
On macOS, clicking "Relaunch to update" often closes the app but does not install the update or relaunch, so the same "update available" banner comes back every time. The root cause is background processes holding file locks during the update, so the update can't finish.

## The reliable fix (do this, it works)
**Reinstall over the top from the website:**
1. Fully **quit Claude**: with Claude focused, press **Cmd+Q** (closing the window is not enough).
2. Make sure nothing is still running: open **Activity Monitor** (Applications, Utilities), search **claude** and **cowork**, and quit any leftover processes.
3. Go to **claude.ai/download** and download the latest Mac app.
4. Open the downloaded file and **drag Claude into Applications, replacing the old one** when it asks.
5. Open Claude. It will now be on the current version, and the nagging banner should be gone.

## Quicker thing to try first (sometimes enough)
1. **Cmd+Q** to fully quit (not just close the window).
2. Wait ~10 seconds.
3. Reopen. Sometimes a true full quit lets the pending update install on its own. If the banner is still there, do the reinstall above.

## Why "shut down the computer" doesn't do it
Shutting down or just closing the window can leave a Claude/cowork helper process running in the background, which holds the file lock that blocks the update. Only a real Quit (Cmd+Q) or the reinstall clears it.

## Session best practices (how to run Cowork so it stays fast and never "forgets")

**End your session and start fresh each day** (or whenever it starts feeling slow). A long session piles the whole conversation into memory, which makes it slow and, once it gets too big, makes it compact/summarize itself and lose detail, that is the "forgetting." A fresh session is fast and full. **Do NOT keep one session open forever; that guarantees the slowdown.** Your memory now lives in the files (TASKS.md, CLAUDE.md, the project docs), so restarting loses nothing.

**Login routine, every morning:**
1. **Connect the repo folder** (`singletrackmom.github.io`) first. Until it is connected, Claude cannot see any files and will seem lost.
2. If doing job-search or LinkedIn work, also connect the **JobSearch folder** (`~/Documents/Claude/JobSearch/`).
3. Say **"read CLAUDE.md and TASKS.md"**, or a keyword like **"open the dial your course plan."** If it acts lost, tell it to read those two files, that means it skipped the step.

## Sources (Anthropic issue tracker)
- macOS app update relaunch fails, manual reinstall required: https://github.com/anthropics/claude-code/issues/50582
- App stuck on "Relaunch to apply" after every restart: https://github.com/anthropics/claude-code/issues/49699
- "Relaunch to update" applies immediately with no confirmation: https://github.com/anthropics/claude-code/issues/61582
