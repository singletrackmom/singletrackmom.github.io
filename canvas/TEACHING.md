# Teaching, cross-course working notes

- [ ] **Instructor AI statement for Spring 2027:** add “Instructor Use of AI” to the syllabus and the short version to resume and cover letter pages. Decide on the opt-out line first. Drafts: `drafts/INSTRUCTOR_AI_STATEMENT.md`.
- [ ] **Syllabus quiz rebuild (Module 0, every course):** write a stronger quiz on the grading format: noon deadlines, each class’s due days, the 24-hour grace window with 10% off, the hard close. Not urgent.
- [ ] Export the “Grids are your Friends” Prezi before Prezi shuts down.
- [ ] Internships: reply to the internship contact with host-company requirements; email the student without an internship.
- [ ] **ON HOLD until January (no syllabus changes mid-semester): rebuild syllabi for the next round of classes.** Drop Syllabus+ (not required) and put each syllabus in the Canvas Syllabus page so it exports with the course. Start from `drafts/syllabi/NOTES.md`: the four Syllabus+ copies (AVC183, AVC248, AVC182 → AVC283, AVC100) are in `drafts/syllabi/source/`, with the comparison, broken links, laptop pools by course and the no-Chromebook / checkout / hotspot / basic needs section every syllabus needs. Also paste in what left Module 0 (`drafts/SYLLABUS_REVIEW.md` Appendix, `drafts/MODULE0_REMOVED_SLOTS.md`) and decide the open questions in NOTES.md.
- [ ] STEAMworks tools training, scheduled.
- Waiting on Michelle: simulations license, CC BY or CC BY-NC-SA?


**PINNED, Sun 25 Oct (idea from the hike, don’t lose it):** add STEAMworks options (NFC/RFID objects, laser cutting, AR, VR, drone photography) to AVC150, 183, 190, 248, 283 and 2xx, so STEAMworks and the dean see the equipment money in the courses. Notes and suggestions: `drafts/STEAMWORKS_OPTIONS.md`. Options added to all six course drafts (25 Oct). AVC294: its Canvas file numbers modules one higher than the course page (drift from the restructure); rebuild from the course page before import. Still to confirm with STEAMworks: which AR tool, and whether the tags are phone-readable NFC. Note: another session moved the courses to a shared build (`tools/course-build/`), and AVC283 is now 123.5 hours (it was 120 last night); check before committing. When the FAA Part 107 certificate comes through, add it to the CV. STEAMworks grant is awarded and already on the CV; add it to the remaining resume lanes (details at the end of that doc).

**Restructured Sun 11 Oct 2026, at Michelle’s request: “i keep adding and adding and never doing.”**

## Moved from CLAUDE.md, 8 Nov 2026

## Course builds, the locked standard (set 24 Oct 2026)

Every course build or revision follows the `course-build-standard` skill: two noon deadlines a week (Discord post at noon the day before, deadline at noon, 24-hour late window at 10% off, hard close at noon the day after), a purple `#7a5080` title box on every page of public builds (switch to GCC red `#CB3338` only when Michelle says a build is going into GCC Canvas), then Objectives, then Overview, the same module rhythm everywhere (Overview, Watch, Read, Practice, Assessment, Critique, Due), competencies called out per Quality Matters Standard 2 (tagged module objectives, one "measures" line per assignment, full map in Start Here), Process Work at 10 points per step and the final at 30 in Projects. AVC150 is the reference build for structure. Course titles: AVC183 Graphic Design; AVC283 Graphic Design 2; AVC190 Introduction to Web Design and UX; AVC294 UX Design for Interactive Media. The data science course (built for Mines) stays blue and is exempt. Terms and dates (set 24 Oct 2026): AVC100 runs spring, summer and fall; AVC183, AVC190 and AVC248 run spring and fall; AVC150 and AVC283 spring only; AVC294 fall only. Date every build for Spring 2027 (semester begins Sat 16 Jan 2027; closed MLK Mon 18 Jan, Presidents’ Day Mon 15 Feb, spring break 15 to 21 Mar; last day of classes Sun 9 May; finals 10 to 14 May, per the MCCCD 2026 to 2027 academic calendar) and/or Fall 2027 (semester begins Sat 21 Aug 2027; closed Labor Day, Veterans Day, Thanksgiving; verify exact days against the 2027 to 2028 calendar).

## Discord process-work grading (idea, decide over break; added 9 Nov 2026)

Status: idea, not decided. Revisit over winter break. Nothing changes in current courses this semester.

### The problem

Students post process work in Discord, then screenshot the same work into Canvas so it can be graded. Michelle comments in Discord and grades in Canvas, so every post gets handled two or three times. Students don’t all use their real names in Discord, so Canvas is the only place she can tell who is who. Comments end up sporadic and grading falls weeks behind.

### The idea

- Students post process work in Discord only. No screenshots.
- Michelle comments in Discord on deadline days (or daily), time-boxed to about 20 minutes, newest posts first.
- Students submit only the final design in Canvas.
- At the end of each project, the channel is exported, process posts are tallied per student, and one process grade is drafted with a short rationale. Michelle reviews and enters the grade.

### How it would work

1. **Export.** DiscordChatExporter pulls the project channel to a CSV (and, if the images need judging, downloads the images too, since Discord image links expire). Run it with a bot account, never a personal Discord login.
2. **Who is who.** A server-nickname rule (nickname matches the Canvas name) plus a one-time roster map of Discord user ID to Canvas name. The ID never changes, so one pass covers the semester.
3. **Tally and draft.** Ideally a Gemini Gem with the rubric and process checklist in its instructions, reading the CSV, the roster map and the finals. Claude can do the tally as a fallback.
4. **Storage.** CSV, images and roster map live on the Maricopa Google account, never the personal one.

### Options found (9 Nov 2026)

| Option | Fit | Notes |
| --- | --- | --- |
| DiscordChatExporter (free, open source) | Best | Exports server channels to CSV, JSON, HTML or TXT with attachments. Export per project, no server needed. |
| Zapier “Log new Discord channel messages to Google Sheets” | Good, no-code | Live sheet as posts land. Costs past the free tier, and a third company touches student work, so it needs a district check. |
| Custom nightly bot (GitHub Actions to Google Sheet) | Only if the above fall short | Own bot account with read-history permission. The DMA jobs bot likely posts by webhook, which can’t read. |
| Chrome extension exporters | Skip | Small unknown developers reading the whole Discord session. |
| Classroom bots (cold-call, attendance, polls) | Skip | Built for attendance and participation, not process work. |
| discord2sheet | Skip | Only logs messages students send with a command. |

### Open decisions

- **Gemini or Claude for the tally.** Test first: export one channel, build the Gem, compare its tally to a hand count.
- **Grading weights.** The `course-build-standard` skill sets Process Work at 10 points per step. One process grade per project changes that standard; decide before any course build uses it.
- **Canvas visibility.** Whether students see per-step complete or incomplete marks in Canvas during the project, or only the final process grade.
- **District rules.** Check whether bots are allowed in course Discord servers.
- **Which course pilots it** in Spring 2027.

### Before any switch

- Tell students in the syllabus: process work lives in Discord, the final goes in Canvas, no screenshots.
- Start with a new project, never one already in progress.

### References

- DiscordChatExporter: https://github.com/Tyrrrz/DiscordChatExporter
- Zapier, Discord and Google Sheets integrations: https://zapier.com/apps/discord/integrations/google-sheets/61742/send-discord-channel-messages-from-new-or-updated-rows-on-google-sheets-spreadsheets
- discord2sheet-bot: https://github.com/hugonun/discord2sheet-bot
- Cold call bot that grades participation from Discord: https://gitea.communitydata.science/collective/coldcallbot/compare/master..foote_spring_2021
- Extension permission review example (Discord Chats Exporter): https://extscope.org/extension/gcickoimlignpaimgekhajcbogfmbpnc
- Setting up a Discord bot with the message content permission (tutorial): https://dev.to/fuderrpham03/build-a-python-bot-to-automate-your-expense-tracking-with-discord-and-google-sheets-53ck

## Gemini skills replace Gems (added 10 Nov 2026)

Google is replacing Gems with skills. Personal-account Gems go read-only on 17 Nov 2026. Skills don’t sync between Workspace and personal Gemini. Affects AVC183 Design History (Gems are one of the student options) and AVC248 (career agents).

- [ ] Test skills on a student account (18+ and under-18): create one, use it inside a regular chat, and stack two together.
- [ ] Check whether existing course Gems migrated, and whether their knowledge files came with them.
- [ ] Rebuild one example as a skill (for example, the Design History research helper) to demonstrate for students.
- [ ] Record a short demo for students: what a skill is, how to make one, how to use it in a chat.
- [ ] Update course pages that say “Gem” to say “skill” (AVC183 Design History options, AVC248 agent steps).
- [ ] Show students how to keep their skill instructions in a Doc they own, so they can rebuild the skill on personal Gemini after graduation.
