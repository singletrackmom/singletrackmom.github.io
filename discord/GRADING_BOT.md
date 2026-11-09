# Discord process-work grading

Status: idea, not decided. Revisit over winter break. Nothing changes in current courses this semester.

## The problem

Students post process work in Discord, then screenshot the same work into Canvas so it can be graded. Michelle comments in Discord and grades in Canvas, so every post gets handled two or three times. Students don’t all use their real names in Discord, so Canvas is the only place she can tell who is who. Comments end up sporadic and grading falls weeks behind.

## The idea

- Students post process work in Discord only. No screenshots.
- Michelle comments in Discord on deadline days (or daily), time-boxed to about 20 minutes, newest posts first.
- Students submit only the final design in Canvas.
- At the end of each project, the channel is exported, process posts are tallied per student, and one process grade is drafted with a short rationale. Michelle reviews and enters the grade.

## How it would work

1. **Export.** DiscordChatExporter pulls the project channel to a CSV (and, if the images need judging, downloads the images too, since Discord image links expire). Run it with a bot account, never a personal Discord login.
2. **Who is who.** A server-nickname rule (nickname matches the Canvas name) plus a one-time roster map of Discord user ID to Canvas name. The ID never changes, so one pass covers the semester.
3. **Tally and draft.** Ideally a Gemini Gem with the rubric and process checklist in its instructions, reading the CSV, the roster map and the finals. Claude can do the tally as a fallback.
4. **Storage.** CSV, images and roster map live on the Maricopa Google account, never the personal one.

## Options found (9 Nov 2026)

| Option | Fit | Notes |
| --- | --- | --- |
| DiscordChatExporter (free, open source) | Best | Exports server channels to CSV, JSON, HTML or TXT with attachments. Export per project, no server needed. |
| Zapier “Log new Discord channel messages to Google Sheets” | Good, no-code | Live sheet as posts land. Costs past the free tier, and a third company touches student work, so it needs a district check. |
| Custom nightly bot (GitHub Actions to Google Sheet) | Only if the above fall short | Own bot account with read-history permission. The DMA jobs bot likely posts by webhook, which can’t read. |
| Chrome extension exporters | Skip | Small unknown developers reading the whole Discord session. |
| Classroom bots (cold-call, attendance, polls) | Skip | Built for attendance and participation, not process work. |
| discord2sheet | Skip | Only logs messages students send with a command. |

## Open decisions

- **Gemini or Claude for the tally.** Test first: export one channel, build the Gem, compare its tally to a hand count.
- **Grading weights.** The `course-build-standard` skill sets Process Work at 10 points per step. One process grade per project changes that standard; decide before any course build uses it.
- **Canvas visibility.** Whether students see per-step complete or incomplete marks in Canvas during the project, or only the final process grade.
- **District rules.** Check whether bots are allowed in course Discord servers.
- **Which course pilots it** in Spring 2027.

## Before any switch

- Tell students in the syllabus: process work lives in Discord, the final goes in Canvas, no screenshots.
- Start with a new project, never one already in progress.

## References

- DiscordChatExporter: https://github.com/Tyrrrz/DiscordChatExporter
- Zapier, Discord and Google Sheets integrations: https://zapier.com/apps/discord/integrations/google-sheets/61742/send-discord-channel-messages-from-new-or-updated-rows-on-google-sheets-spreadsheets
- discord2sheet-bot: https://github.com/hugonun/discord2sheet-bot
- Cold call bot that grades participation from Discord: https://gitea.communitydata.science/collective/coldcallbot/compare/master..foote_spring_2021
- Extension permission review example (Discord Chats Exporter): https://extscope.org/extension/gcickoimlignpaimgekhajcbogfmbpnc
- Setting up a Discord bot with the message content permission (tutorial): https://dev.to/fuderrpham03/build-a-python-bot-to-automate-your-expense-tracking-with-discord-and-google-sheets-53ck
