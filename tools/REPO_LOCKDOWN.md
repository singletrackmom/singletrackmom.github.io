# Repo lockdown

Why: the site repo is public, so the Dial Your Course build notes, reference library and v2 file can be read by anyone. Written 11 November 2026. Nothing has been changed yet.

## Part 1. Upgrade to GitHub Pro (Michelle, 5 minutes)

Do this first. If the repo goes private on the free plan, the site goes down.

1. Go to github.com and sign in as singletrackmom.
2. Click the profile photo, then Settings.
3. Open Billing and licensing.
4. Click Upgrade or Compare all plans, and pick Pro at $4 a month, billed monthly.
5. Skip anything labeled Copilot. That is a separate product.

## Part 2. Make the repo private (Michelle, with Claude walking through it)

1. Open the repo, then Settings, then scroll to the Danger Zone.
2. Change visibility to Private.
3. Check Settings, then Pages, still shows the site as published.
4. Load michelleblomberg.com and confirm it is live.

Do not delete the commit history. It is dated proof of when the work was done.

## Part 3. Move the sensitive files out of the site folder (Claude, Michelle approves first)

Pro hides the repo, not the website. Files left in the site folder can still be opened by direct link, so these move to a separate private repo:

- course-dialer: BUILD_TOMORROW.md, COMPETITIVE_SCAN.md, NEXT.md, TECH_ARCHITECTURE.md, V2_BUILD_NOTES.md, V2_FUNCTIONS_MAP.md, V2_RESEARCH_LANDSCAPE.md, walkthrough-script.md
- tools/reference: all files
- tools: course-auditor-v2.html, QUALITY_SYSTEM.md, NEXT_DIALER_ROUNDTRIP.md
- notes: agent-business-idea.md, league-capstone-dial-your-course.md

Stays public: the Dial Your Course overview page, the cover image and the version 1 tool.

Link check, done 11 November: no live page links to any of these files. Paths that need updating after the move: CLAUDE.md (QUALITY_SYSTEM), TASKS.md (course-dialer/NEXT.md), portfolio/PORTFOLIO.md, three pages under private/, and the course dialer and reference library skills that read tools/reference.

## Part 4. Check who looked (Michelle, 2 minutes)

In the repo, open Insights, then Traffic. It shows 14 days of views, clones and referring sites. No names.

## Limits

- Anyone who already cloned or forked the repo keeps their copy.
- Version 1 is a live web page, so its source can be viewed in a browser.
