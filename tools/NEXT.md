# Where we left off · 11 July 2026, late

**Goal:** Pick up tomorrow without re-deriving anything.

**Audience:** Me, in the morning.

**Process:** Do these in order. The first three are quick. The Mines application comes first regardless.

---

## 0 · Mines OLED application

**Closes 15 July.** Three days. Do it before anything here.

Then Michelle is finishing her After Effects tutorial.

---

## 1 · The Canvas outcomes question · FIRST THING, two tests, five minutes

Full write-up: **`canvas/reference/CANVAS_OUTCOMES_EXPORT_BUG.md`**. Read it before touching this.

Short version: **we were both wrong.** The Canvas source says a full course export *should* include unaligned outcomes. The likely cause is a **stale `has_outcomes?` cache** that the CSV import never invalidates, because it writes the outcomes but never touches the Course row.

**Test 1 · bust the cache.** Sandbox → Settings → change anything → Save → export.
**Test 2 · bind one outcome.** Color Palette Exercise → Rubric → Find Outcome → export.

They discriminate cleanly. Ask Michelle for the resulting `.imscc`.

**Then:** draft the CTLE email (task #14). She has standing to ask; she co-chairs Domain 5 of the ARC.

---

## 2 · Nav on every subpage · task #15

Top of the page, not the bottom. **Home · ← Back to [the tool this page belongs to].**

The `.prdnav` component already exists and is on all 8 PRDs plus the report sample. Copy it to the tool pages themselves and the other subpages. **Remove any existing bottom backlink** so nothing ends up with two.

Skip `avc100/pages/*.html` — those get pasted into Canvas.

---

## 3 · Assessment section, and call out the videos · task #16

Her words: *"we put it in the usability section but i don't see anything called out, you should at least call out the videos."*

`oscqr-assess` currently sits in band 2, **"Can a student use it?"**, which is the usability band. Rubric coverage is not a usability question.

**Proposal to confirm with her:** a fourth band, **Assessment**, holding `oscqr-assess`, `authentic`, and `airesist`. And surface the video finding properly — it should **name** the videos, not just count them. It already distinguishes embedded Studio from linked YouTube from channel links; show the list.

Change both the tool (`.chk` cards + `grouphd` labels in `course-auditor.html`) **and** the report generator's `BANDS` array.

---

## 4 · Then the open threads

- **AVC183 Computer Graphic Arts 1** (task #12) · write objectives, build the outcomes CSV, run the course through the tool. This is the second-discipline test the PRD calls for. **Ask her to flag anything the report says that she knows is false.**
- **Swap the hand-bound outcomes** (task #13) for a real export once #1 resolves. The published report currently uses bindings I made by hand. Every one is defensible, nothing is invented, but they are not what Canvas holds.
- **AVC248 walkthrough-video portfolio rework** (task #3), still open from earlier.

---

## State of the tool tonight

`tools/course-auditor.html` · **18 checks, all compute, none throw.** Cards and checks match with no orphans. Export round-trip verified: file count preserved, all XML byte-identical, output ASCII, no `<style>` block, package reimports.

**AVC100 report** (`tools/course-auditor-report-sample.html`): 28 findings · **2 fix · 10 review · 16 pass.**

- Workload **30.8 h, 116 % of the 26.5-hour outside-work allowance.** Warn, not high. The tool now asks for the outside-work hours rather than deriving them from a load formula.
- AI-resistance audit: **9 strong · 5 adequate · 2 exposed · 11 formative.** All nine Project steps come back strong.
- Competency map: **14 of 14 evidenced.**
- The two remaining reds are hers and both are quick: **no privacy policy linked** for Discord, Miro, Behance, Adobe, YouTube (**she already wrote the page**, `avc100/pages/tools-and-privacy.html`, it is simply not in the course), and the **Course Reflection** (10 pts, prose response to a general prompt).

**Style guide:** five typefaces, all sans-serif. Georgia and Palatino removed.

---

## Rules that keep getting broken. Read these.

- **Read the rubric criteria, not the assignment titles.** I have made this mistake four separate times and she has corrected me every time.
- **Never fabricate a binding or a finding.** I did it once in the sample report and had to walk it back in front of her.
- **A check that cannot compute does not fire.** No unearned pass, ever.
- **Low-stakes formative work is not a measurement instrument** and must never be flagged as a failed one.
- **AVC course codes: ask DMA vs Animation. Never guess.** AVC183 = Computer Graphic Arts 1, confirmed.
- **No em dashes. Curly quotes. One body size. Bold only for short lead-in phrases, never a whole sentence.**
- **Professional register.** No anecdotal clutter, no snark, no "nobody uses it."
- **Show proposed changes before editing her files.**
