# Saving Claude tokens: repo and session notes

From a conversation on Sat 24 Oct 2026, prompted by a colleague’s advice to break AVC150 into its own repo.

## What actually costs tokens

- **Claude does not load the whole repo.** It only sees the files it opens or searches. Having 3,000+ files in one repo is not by itself the cost.
- **The startup read.** Every session starts by reading CLAUDE.md (about 33 KB) and TASKS.md (about 27 KB). That’s roughly 15,000 tokens before any work starts, and most of it is about other projects.
- **Site-wide searches.** Name scrubs, link checks and “find everywhere” searches touch every project.
- **Long sessions (the biggest cost).** One marathon session covering six projects keeps all of it in context until it runs out of room and has to be summarized. One topic per session saves the most.

## Fix 1: split the startup files (free, no git changes)

- Keep the root CLAUDE.md short: the site rules that apply everywhere (design lint, preflight, never run git, no faculty names, no deleting).
- Move course rules into `canvas/CLAUDE.md` and each project’s detail into its own folder’s CLAUDE.md. Claude reads a folder’s CLAUDE.md when it works there.
- Keep TASKS.md to the locked order, this week, and deadlines. Move each project’s backlog into that project’s folder (for example `canvas/avc150/TASKS.md`).

## Fix 2: one topic per session (free, starting now)

- Open with the topic: “AVC150 today,” “GCC Cares today.”
- Start a new session when switching projects, instead of continuing a long one.

## Fix 3: break a course into its own repo (before AVC150 runs)

A colleague’s method: make a new empty repo, give Claude the URL, and Claude breaks the course out and populates it.

1. On GitHub, create an empty repo (for example `avc150`). Send Claude the URL.
2. Claude copies the course files into a new folder on the Mac, with a short course-only CLAUDE.md and copies of `tools/design-lint.py` and `tools/preflight.py`.
3. Clone it and publish with GitHub Desktop (Claude never runs git).
4. Claude leaves a redirect at the old address so shared links keep working.

**Know before you do it:**
- A repo named `avc150` publishes at michelleblomberg.com/avc150/, not /canvas/avc150/. The redirect covers the old link.
- It lets you add collaborators (colleagues, ASU) without giving them access to the job search, TASKS.md or family pages. That’s the bigger reason to do it.
- Split only courses that get collaborators. Moving all six courses mid-semester is a lot of churn for a small saving.
- Do it after Version 6 (the faculty review feedback) is merged, so you’re not moving a course that’s still changing.

**Option: let Claude create the repo.** A colleague pointed out that Claude can create repos itself if the GitHub CLI (`gh`) is installed and signed in. That would end the standing “Claude never runs git” rule, so decide that on purpose first. Without it, creating the empty repo on github.com takes about 30 seconds (New repository, name it, Create), and Claude does the rest.
