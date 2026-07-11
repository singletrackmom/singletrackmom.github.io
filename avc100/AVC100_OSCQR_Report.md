# AVC 100 · OSCQR Review

**Scored against the real course export**, July 11, 2026. 38 HTML pages, 26 graded assignments, 5 modules, 15 rubrics.

Rubric: **OSCQR**, the SUNY Online Course Quality Review Rubric, 50 standards in 6 sections.
Licensed **CC BY 4.0**, developed by the State University of New York through SUNY Online. <https://oscqr.suny.edu>

**Goal:** Find what a real quality review would flag, before a real quality review does.

**Audience:** Me, and the faculty who will copy this course.

**Process:** Scan the export mechanically for what can be measured. Read for what cannot. Mark everything honestly, including the standards this course already passes.

---

## 🔴 THE FINDING THAT REVERSES TODAY'S WORK

### Standard 23, *"A sans-serif font with a standard size of at least 12 pt is used."*

**AVC100 currently PASSES this.** The course has **zero inline font declarations**, so every page inherits Canvas's default, Lato, a sans-serif. Clean.

**And the style guide I built today would BREAK it.**

I recommended **Georgia** as a substitute for your Lora. Georgia is a **serif**. So is Lora. Applying that style guide would take a standard this course currently passes and fail it, across all 38 pages, in one click.

**The fix:** the Dial Your Course default must be **sans-serif**. Of the five Canvas-safe typefaces:

| Typeface | OSCQR 23 |
|---|---|
| Georgia | ✗ serif |
| Palatino | ✗ serif |
| **Verdana** | ✓ **sans-serif, widest, most legible at small sizes** |
| **Trebuchet** | ✓ sans-serif, friendlier |
| **Helvetica / Arial** | ✓ sans-serif, neutral |

**Recommendation: Verdana.** It is the standard accessibility sans-serif, installed everywhere, and survives Canvas. Trebuchet if Verdana feels too plain.

**This is exactly why running the rubric matters.** I was one click from making your course worse while believing I was improving it.

---

## 🔴 Standard 14, *"Course includes links to privacy policies for technology tools."*

**FAIL, and it is the most substantive gap in the course.**

AVC100 requires students to use **four third-party tools**: **Discord** (28 mentions), **Miro** (46 mentions), **Behance**, and **Adobe Creative Cloud**. Every one of them collects student data. **The course links to none of their privacy policies.**

This is not a paperwork nitpick. You are directing students to create accounts on commercial platforms as a condition of passing a course. **They are entitled to know what those companies do with their data**, and a quality reviewer will flag it immediately.

It also sits badly next to your own position on the ARC. You argue for data-sovereign design at the district level, and this course quietly routes every student through four vendors without disclosure.

**Fix:** one page in Getting Started. Four links. Twenty minutes of work, and it turns a liability into a teaching moment about digital citizenship.

---

## 🔴 Standard 9, *"Course objectives are clearly defined, measurable, and aligned."*

**FAIL.** Documented in full in `AVC100_Objectives_Rewrite.md`.

- **"You will be introduced to the principles of design"**, appears **3 times**. Passive, unobservable, ungradeable.
- **"Learn about," "learn," "demonstrate an understanding of"**, 5 more objectives.
- Six objectives have **no criterion**, so there is no way to tell if a student met them.

**And this is your most important content.** The design-principles scaffold is riding on the weakest objective in the course.

---

## 🔴 Standard 47, *"Opportunities for learners to review their performance and assess their own learning (self-tests with feedback)."*

**FAIL, and the mechanism is broken, not missing.**

You built two vocabulary quizzes for exactly this purpose. **Both are corrupted.** Every answer choice in the matching question shares the same ident, so Canvas cannot tell the four answers apart. See `AVC100_Reconciliation.md`.

The intent is right. The instrument is broken. **Rebuild as an HTML self-check** so it cannot corrupt again on a course copy.

---

## 🟡 Standard 46, *"Criteria for the assessment of a graded assignment are clearly articulated (rubrics)."*

**MOSTLY PASS, with real defects.** You have **15 rubrics**, which is genuinely strong. But:

- **Lesson and Exercise: After Effects**, rubric is **20 pts**, assignment is **10 pts**.
- **Animation, Step 2**, rubric is **14 pts**, assignment is **15 pts**.
- **Two orphan rubrics** ("Phase 3 Project + Critique," "Final revised project") from a course design that no longer exists.
- The Animation rubric grades **"assets imported and placed in the template."** *There is no template.*

---

## 🟡 Standard 35, *"A text equivalent for every non-text element is provided (alt tags, captions, transcripts)."*

**PARTIAL.** Images are clean: **2 images, both with alt text.** Zero missing.

But the course embeds **15 YouTube videos and 3 Canvas Studio items**, and **captions cannot be verified from the export**, it contains links, not video files.

- **Your own videos:** auto-caption in Studio, then **edit them**. Auto-captions run 70–90% accurate and fail hardest on technical vocabulary.
- **Someone else's YouTube video:** you cannot caption it and may not re-upload it. Ask the owner, find a captioned version, re-record it yourself, or use Amara (~$5/video).
- **A transcript does not satisfy this.** WCAG 1.2.2 requires captions.

---

## 🟡 Standard 33, *"Course materials include copyright and licensing status."*

**PARTIAL.** The course mentions **Pexels (6×) and Unsplash (2×)**, so you are already pointing students at properly licensed sources. Good instinct.

But it never **states the licensing status** or teaches *why* those sources are safe. Students are told where to get images, not why it matters. **One paragraph turns a instruction into a competency**, and it is the same media-literacy thread as the "Reputable Sources" Student Success item.

---

## 🟡 Standard 2, *"Module-level overviews make content, activities, due dates, and assessments predictable."*

**PARTIAL.** Modules exist and are clean, but **no module states how long it takes.** This is precisely what the Dial Your Course workload sliders produce.

---

## ✅ WHAT THE COURSE ALREADY PASSES

Do not fix these. They are working.

| Std | Standard | Result |
|---|---|---|
| **37** | Hyperlink text is descriptive | ✅ **Zero "click here" links.** Rare. |
| **36** | Images have text equivalents | ✅ 2 images, both with alt text |
| **21** | Text formatted with headings | ✅ Clean hierarchy: 50 H2, 108 H3, 23 H4 |
| **22** | No flashing or blinking text | ✅ None |
| **23** | Sans-serif, 12pt+ | ✅ **Currently passing** (see the warning above) |
| **24–26** | Tables used properly | ✅ **Zero tables.** Nothing to fail. |
| **34** | Text content in accessible format | ✅ **Zero PDFs.** Everything is HTML. |
| **11–12** | Tech skills stated and scaffolded | ✅ Technology Orientation assignment |
| **6** | Learner success resources | ✅ **Five Student Success items**, one per module |
| **30** | Higher-order thinking | ✅ Critique, analysis, revision |
| **31** | Authentic activities | ✅ Real design projects, published portfolio |
| **41–43** | Class community, learner-to-learner | ✅ **Discord (28), critique (30), Miro (46).** This is the strongest part of the course. |
| **32** | OER / free materials | ✅ Pexels, Unsplash |

**Note on 34:** you have **zero PDFs**. The entire PDF-remediation problem we spent time on today **does not apply to this course.** It is already clean.

---

## Correction: my earlier report was partly fiction

The sample findings I put in Dial Your Course claimed *"6 PDFs need remediation"* and *"3 images missing alt text."* **Both were invented placeholder numbers, and both are wrong.** The real course has **zero PDFs** and **zero images missing alt text.**

I have to fix that in the tool. **A course-quality tool that reports fake failures is worse than no tool**, and I built one for a few hours.

---

## Summary

| Priority | Standard | Issue |
|---|---|---|
| 🔴 | **23** | The style guide I built would **break** a standard you currently pass. Switch to **Verdana**. |
| 🔴 | **14** | **No privacy policy links** for Discord, Miro, Behance, or Adobe. Most substantive gap. |
| 🔴 | **9** | Objectives unmeasurable throughout |
| 🔴 | **47** | Self-check quizzes are **corrupted** |
| 🟡 | **46** | Two rubric/assignment point mismatches, two orphan rubrics, one grades a template that does not exist |
| 🟡 | **35** | 18 videos, captions unverified |
| 🟡 | **33** | Image licensing used but never explained |
| 🟡 | **2** | No time estimates in module overviews |

**The course is in better shape than the repo files suggested.** The mechanical accessibility is clean, the interaction design is genuinely strong, and the rubrics exist and are mostly good. **The failures are concentrated in objectives, the broken quizzes, and disclosure, not in the teaching.**

---

*OSCQR is made available under CC BY 4.0 by the State University of New York through SUNY Online. This report applies the rubric; it is not affiliated with or endorsed by SUNY.*
