# Dial Your Course: build order for the morning

**Goal:** get the roundtrip working so the walkthrough video can be recorded. Export a Canvas course, run it through the dialer, apply the style guide and seat time, re-import, and see it land.

**Audience:** the assistant, starting fresh. Michelle should be able to say "read BUILD_TOMORROW.md and start" and work begins immediately.

**Process:** four builds in dependency order. Do not reorder. Each has an explicit done-test.

**Written:** August 16, 2026, after reading the existing research.

---

## STOP. Read these three first. Do not re-derive anything.

1. **`course-dialer/V2_FUNCTIONS_MAP.md`** , already contains the **seat-time display convention** and the **export/writeback logistics**. The design decisions are made. Search it for "Seat-time display convention" and "Writeback / export logistics."
2. **`canvas/reference/CANVAS_OUTCOMES_EXPORT_BUG.md`** , the outcomes problem is already diagnosed. Likely a **stale `has_outcomes?` cache** that the CSV import never invalidates. Two discriminating tests are written and take five minutes each. They have never been run because they need Michelle's Canvas.
3. **`course-dialer/NEXT.md`** , standing context and prior decisions.

**Key facts already established, do not relitigate:**
- Read side works. The tool parses `.imscc` today.
- Content writeback is **mechanically feasible**: unzip the `.imscc`, edit module HTML, update the manifest, re-zip, re-import via Common Cartridge.
- Outcomes writeback is **open, not blocked**. Only one test was ever run. Treat as untested.
- v1 = **no AI, no API, no login, no server.** Client-side only. This is a hard architectural line tied to data sovereignty.
- Canvas imports a **whole package**, not pieces. The tool is the workspace; Canvas is a sync target.

---

## Build 1: resolve the version problem (30 min, do this first)

`course-dialer/` currently holds **two** live builds:
- `index.html` (318 KB) , what the site serves today. The older, simpler one.
- `v2.html` (327 KB) , the newer build Michelle set aside as "way too complicated."

**Tasks:**
1. Open both. Determine what v2 has that index does not, and what index does better.
2. **Ask Michelle which is the base.** Do not decide this alone. Her stated instinct is that v2 got too complicated, so the default assumption is index.html is the base and v2 is a parts donor.
3. Whichever loses, move it to `course-dialer/_archive/` so no reviewer stumbles into it. (The old `_to_delete/` folder is gone: its two pending skill drafts were already live in `.claude/skills/`, so they were removed on 28 Aug 2026.)
4. Remove `.DS_Store` and the six `.fuse_hidden*` files. They are junk and they are in the repo.

**Done test:** `michelleblomberg.com/course-dialer` serves exactly one tool, and no stale build is reachable by URL.

---

## Build 2: the syllabus upload slot (1 hour)

**The problem Michelle identified:** course objectives never reach the dialer because they live in Canvas's **Syllabus tool**, which is not content and does not export with the package. So alignment checking has nothing to align against.

**The fix, and it is the right product call:** do not require every faculty member to change how they write syllabi. Add an upload slot to the tool.

**Build:**
- A file input that accepts **PDF, DOCX, TXT, and pasted text**.
- Parse it for objectives. Look for the usual headings: "Course Objectives," "Learning Outcomes," "Course Learning Outcomes," "Upon completion," "Students will be able to."
- Extract each objective into the same structure builder mode uses for hand-typed objectives, so downstream alignment code needs no changes.
- Show what was found and let the user correct it before it commits. Never silently accept a bad parse.
- If nothing parses, fall back to manual entry with a clear message explaining why the export did not carry them.

**Also add, as a second path:** a short in-tool note telling the user they can attach the syllabus as a PDF file inside their Canvas course so it exports next time. Both paths, not one.

**Done test:** upload a real GCC syllabus PDF, see the objectives appear as editable items, and see the alignment check run against them.

---

## Build 3: the writeback engine (2 to 3 hours, this is the core)

**This is the thing that has never been built and it is what the video needs.**

The tool reads `.imscc` today. It does not write one. Build the write path.

**Mechanics, already validated as feasible in V2_FUNCTIONS_MAP.md:**
1. Unzip the `.imscc` in the browser (JSZip, client-side, no server).
2. Walk the module and page HTML files.
3. Inject the changes.
4. Update `imsmanifest.xml` if any files were added.
5. Re-zip and hand the user a downloadable `.imscc`.

**What gets injected, in priority order:**

**a) The time-on-task note, per assignment.** This is Michelle's explicit ask: real time stamps on each project, not just a total in the tool.

The convention is already specified in V2_FUNCTIONS_MAP.md and must be followed exactly:
- Bold label carrying the meaning in words, never italics alone. WCAG 1.3.1 and 1.4.1.
- Pattern: **Estimated time:** about 2 hours on this assignment.
- May sit in a muted box in the palette fill so it does not read as body content, but the label text carries the meaning.
- Register it in the style guide as a named component, "Time-on-task note," with fixed markup so every module renders identically.

**b) The style guide.** Apply the defined formatting so pages are consistent after re-import.

**c) Objectives**, if the outcomes tests pass. Otherwise write them as visible page content rather than Canvas outcome objects, and say so in the report.

**Guardrail:** the tool should refuse to write anything it cannot verify. That constraint is already the thing reviewers praised about this tool. Do not break it here.

**Done test:** export a real course, run it through, download the modified `.imscc`, and **re-import it into a sandbox Canvas course.** Confirm by eye that the time-on-task notes and the style guide are present.

---

## Build 4: run the two outcomes tests (5 minutes, needs Michelle at a Canvas login)

From `CANVAS_OUTCOMES_EXPORT_BUG.md`. These have been queued since July and never run.

- **Test 1, bust the cache:** Sandbox course → Settings → change anything → Save → export. Check whether outcomes now appear in the package.
- **Test 2, bind one outcome:** Take one assignment → Rubric → Find Outcome → attach → export. Check the package.

They discriminate cleanly. If Test 1 works, the fix is a documented workaround the tool can instruct users to do. If only Test 2 works, objectives must be rubric-bound to survive, which is also actionable guidance.

**Ask Michelle for the resulting `.imscc` files.** This is a five-minute task that has been blocking accuracy for a month.

---

## Then, and only then, record

Do not record before the roundtrip has been run manually at least once with no camera. The video must be a demonstration, not a discovery.

**Shot list:**
1. Export a real course from Canvas.
2. Drop it into the dialer.
3. Findings appear, each traced to its standard and location.
4. **It refuses to report something it cannot compute.** Say why out loud. A reviewer called this the best thing about the tool.
5. Upload the syllabus, objectives appear.
6. Apply fixes and the style guide.
7. Export the corrected package.
8. **Re-import into Canvas.**
9. Show the time-on-task notes on each assignment, the style guide applied, and the objectives present.

Steps 8 and 9 are the payoff. If something does not survive, **say so in the video.** The honest version is more credible than a staged one, and it is consistent with how the tool itself reports.

---

## Michelle's standing rules that apply to all of this

- Show proposed changes before editing files.
- No em dashes. Curly quotes only.
- Solid palette colors only, no gradients.
- Goal, Audience, Process on anything new.
- Never run git. She commits and pushes herself.
- Be honest about status. The tool is in testing, not production.
