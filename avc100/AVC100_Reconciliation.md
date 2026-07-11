# AVC 100 · Reconciliation Report

**Run against the real courses**, July 11, 2026.
Sources: `gc-blomberg-avc100-sandbox-export.imscc` and `gc-2026-summr1-avc100-10017-export.imscc`

**Goal:** Establish one source of truth before rebuilding the sandbox for fall.

**Audience:** Me, and the faculty who will copy this course.

**Process:** Sandbox = dates and module layout. Summer = rubrics, points, content. Everything below is what the real courses actually contain, not what the repo files claimed.

---

## 🔴 1. I FOUND THE CORRUPTED QUIZ

Both vocabulary quizzes are broken, and the bug is precise.

**Every answer choice in the matching question shares the same ident.** All 16 response labels are `ident="1"` in one quiz and `ident="2"` in the other. Canvas cannot tell the four answers apart, and all four correct-answer mappings point at the same ident.

```
LEFT 1: Balance      → choice 1
LEFT 2: Alignment    → choice 1
LEFT 3: White Space  → choice 1
LEFT 4: Repetition   → choice 1
```

Four prompts, four "correct answers," all pointing at the same thing. **The matching question is unanswerable.** That is exactly the behavior you described, and it will corrupt again on the next course copy, because it is a QTI export defect, not a content mistake.

### And there is a second bug nobody noticed

**"Imaging and Animation Vocabulary Check" contains DESIGN terms.** Its matching question asks students to match *Balance, Alignment, White Space, Repetition*, those are the design principles from the *other* quiz. The imaging and animation vocabulary is not in it at all. **It is a duplicate of the Design quiz's matching question.**

The six multiple-choice questions in that quiz *are* correct (resolution, PSD, keyframe, selection, compositing, scale). Only the matching question is wrong.

### Recommendation

**Do not repair these. Rebuild them, and not as Canvas quizzes.**

A quiz that corrupts once will corrupt again on the next copy, and this course is about to be copied by several faculty. **A broken quiz that propagates to five sections is worse than no quiz.** Build the vocabulary check as an HTML self-check page instead: no QTI, no corruption, ungraded, unlimited retries, travels with the course forever.

---

## 🔴 2. The Animation rubric still requires a template that does not exist

**"Animation step 2" rubric, criterion 1:** *"Postcard assets imported and placed in the template"*, 3 pts.

There is no template. **Students are being graded on using a thing you do not provide.**

---

## 🔴 3. Two rubrics do not match their assignment's points

| Assignment | Assignment pts | Rubric pts |
|---|---|---|
| **Lesson and Exercise: After Effects** | **10** | **20** ✗ |
| **Social Media Animation, Step 2: Build** | **15** | **14** ✗ |

The After Effects one is a factor of two. The rubric grades out of 20 (opacity keyframes, position keyframes, scale keyframes, Easy Ease, comp size) on an assignment worth 10.

**Also note what that rubric expects:** fade with *opacity* keyframes, slide with *position* keyframes, scale with *scale* keyframes, plus *Easy Ease*. That is a far bigger exercise than the "two Position keyframes" we designed today. **The rubric and the plan disagree about what this exercise is.**

---

## 🔴 4. Two orphan rubrics from a course design that no longer exists

| Rubric | Points | Problem |
|---|---|---|
| **Phase 3 Project + Critique** | 15 (summer) / 30 (sandbox) | References "Phases," a structure the course no longer uses. Also mentions an **OBS video posted to Discord**, which is nowhere in the current course. |
| **Final revised project** | 30 | Grades "Phase 1 PDF / Phase 2 JPG / Phase 3 MP4 with revisions." No such assignment exists. |

These are leftovers. They are not attached to anything in the module list. **Delete them, or a faculty member copying the course will find them and wonder what they missed.**

Worth noting: *"Final revised project"* is a **30-point revision assignment across all three projects.** That is the Part 3 idea you reinvented today, from an earlier version of the course. You already had it and dropped it.

---

## 🟡 5. Student Success, six items, not five, and the grading is inconsistent

| Item | Points | Grading |
|---|---|---|
| Online Learning Tips | 3 | ✗ **points** (should be checkmark) |
| Where to get help | 3 | ✓ checkmark |
| GCC Cares | 3 | ✓ checkmark |
| Advising | 3 | ✗ **points** |
| Reputable Tutorial/Learning Sources | 3 | ✓ checkmark |
| **Getting Help with Coursework or Technology** | **5** | ✗ **points** |

**The sixth one is a duplicate.** "Where to get help" and "Getting Help with Coursework or Technology" are two different assignments covering the same ground. The second is **not in any module**, it is orphaned in the course, worth 5 points instead of 3.

**Fix:** delete the orphan, set all five to **3 points, checkmark grading.**

---

## 🟡 6. Summer drifted. The sandbox is the more consistent course.

You told me summer wins on grading. **On grading type, that is backwards.** Four items were switched from checkmark to points during the term:

| Item | Sandbox | Summer |
|---|---|---|
| Student Success: Online Learning Tips | checkmark | **points** |
| Student Success: Advising | checkmark | **points** |
| Student Success: Getting Help | checkmark | **points** |
| Syllabus and Course Introduction | checkmark, 3 pts | **points, 5 pts** |
| Technology Orientation | checkmark, 5 pts | **points, 10 pts** |
| Digital Media Programs at GCC | 5 pts | 3 pts |

**Summer wins on rubrics and content. The sandbox wins on grading type.** Confirm which you actually want.

---

## ✅ 7. Good news: almost no hardcoded dates

Only **one** assignment has a date baked into its body text: **"Introduce yourself"** ("Sunday May…", "Friday May…").

That is far better than expected. Fix that one and the course copies cleanly.

---

## 📋 8. What the course actually is

**Five modules**, not eight:

1. **Getting Started**
2. **Graphic Design Poster (Illustrator)**
3. **Photographic Postcard (Photoshop)**
4. **Social Media Animation (After Effects)**
5. **Launch It: Develop your Portfolio**

**Total: 208 points across 26 graded items.**

**The exercises are actually named:** Color Palette Exercise · Lesson and Exercise: Illustrator · Lesson and Exercise: Photoshop · Lesson and Exercise: After Effects.

**There is no "Cut It Out" and no "Make It Move."** Those exist only in the repo markdown files, which are a *different, older* design. **The repo files were never the course.** Every recommendation I made from them needs re-checking against this.

**Poster has 3 steps. Postcard and Animation have 2.** Confirms the restructure.

**Critique is currently 4 classmates** in every rubric (one orphan rubric says 2). Changing to 2 means editing 8 rubrics.

**Sandbox-only items:** "Syllabus and Course Introduction" assignment, and both vocabulary quizzes.

---

## Decisions needed

1. **Quizzes:** rebuild as HTML self-checks, or repair the QTI and risk it corrupting again?
2. **Grading type:** sandbox (checkmark) or summer (points) for the Student Success items?
3. **The orphan "Getting Help" assignment:** delete?
4. **Orphan rubrics** (Phase 3, Final revised project): delete?
5. **After Effects exercise:** the rubric wants opacity + position + scale keyframes + Easy Ease, out of 20. The plan we made today is two Position keyframes, out of 10. **Which is the real exercise?**
