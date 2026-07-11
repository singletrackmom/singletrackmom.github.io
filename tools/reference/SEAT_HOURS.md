# GCC Seat Hours · Source of Truth for Course Polish

**Goal:** Give Course Polish a correct, citable seat-hour model so it never invents an hour budget.

**Audience:** Me, and anyone maintaining the Course Polish tool.

**Process:** This table is transcribed from the department reference doc (`GCC_Seat_Hours_Syllabus_Language.docx`, in this folder). Course Polish reads from it as a **lookup table**, not a derived formula. When another department differs, add a profile, do not change the rule.

---

## Why this matters

The approved seat-hours language is **required and must appear verbatim** in every syllabus, in the workload / student-expectations section (in Syllabus+, the field is **"Instructional Contact Hours & Out-of-Class Student Work"**). Paraphrasing does not satisfy it.

That is why Course Polish treats missing or altered seat-hours language as a **high-severity** finding, not a nitpick.

**Live source, always link this rather than copying it:** [Required Syllabus Language on Seat Hours and Direct Instruction](https://docs.google.com/document/d/1i3Tw0cbMaWB5JDBqbCL0SGbuEHAYXhv1DBGQsVcpeFA/edit)

---

## The rule

> **Total student hours = credits × 40. Always.**

**Load hours do not change the total.** They change the **split** between direct instruction, in-class studio time, and outside work. A 3-credit course is 120 hours whether it loads at 3, 4, 5, or 6.

This is the thing that is easy to get backwards, and I did get it backwards on the first pass.

## The table

| Credits | Load | Activity type | Example | Total | Direct | In-class studio | Outside |
|---|---|---|---|---|---|---|---|
| 3 | 3 | Lecture | ARH, HUM | 120 | 40 | — | 80 |
| 3 | 6 | Lec+Lab (studio) | **AVC183, AVC248**, ART111, ART161, AVC184 | 120 | 40 | 40 (in person) | 40 (in person) |
| 3 | 6 | Lec+Lab (studio), **online** | **AVC183, AVC248** | 120 | 40 (min) | folded into outside | 80 |
| 1 | 2 | Lec+Lab (studio) | **AVC100** | 40 | 13.5 | — | 26.5 |
| 3 | 5 | Lec+Lab | FMP151 | 120 | 33.5 | 33.5 | 53 |
| 3 | 4 | Lec+Lab | FMP211 | 120 | 26.5 | 26.5 | 67 |
| 3 | 0 | Lab / Special Projects | FMP, AVC298AC | 120 | 4 (min) | — | remainder, independent research or creative work |
| 3 | 0 | Internship | AVC297AC | 120 | 2 to 4 brief engagements (20 to 30 min each) | — | remainder |
| 3 (LEC) + 0 (Lab) | 2 (LEC) + 3 (Lab) | LEC and Lab separated | FMP108 | 120 | 27 | 40 lab | remainder |

## My courses

- **AVC100** · 1 credit, loads at 2 · **40 total hours** (13.5 direct + 26.5 outside)
- **AVC183** · 3 credits, loads at 6 · **120 total hours**
- **AVC248** · 3 credits, loads at 6 · **120 total hours**

## ⚠️ Discrepancy to resolve

`canvas/avc248/competencies.html` currently says AVC248 is *"120 student hours across 15 weeks, about 8 hours per week... roughly 40 hours are direct instruction and about 80 hours are studio production."*

**That matches the approved online 3-credit studio language exactly.** Good. No change needed. Leaving this note so nobody "fixes" it later.

## Notes for whoever maintains this

- **Other departments may use different splits.** Add a profile to the `SEAT` table in `course-auditor.html`. Do not change `credits × 40`, that part is federal.
- The approved language differs between **in-person** and **online** for the 3/6 studio row. Online folds the in-class studio hours into the outside-work total and adds the **RSI (regular and substantive interaction)** paragraph. The RSI language is itself a compliance requirement for online courses. Do not drop it.
- Always check the **CCTA website** for a course's official credits, load hours, periods, and activity type before trusting anything here.

**Source:** GCC Art & Humanities Department, *Faculty Reference: Required Syllabus Language on Seat Hours and Direct Instruction.*

**Always link, never copy:** <https://docs.google.com/document/d/1i3Tw0cbMaWB5JDBqbCL0SGbuEHAYXhv1DBGQsVcpeFA/edit>

The department can revise this document at any time. Both tools link to it live so they never serve stale wording. If you find a local copy of the .docx anywhere in this repo, delete it.

> **Note:** this repo is public (`singletrackmom.github.io`). Keep internal accreditation detail out of these files.
