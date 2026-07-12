# AVC 100 · Fall Build Sheet

**Goal:** Build the fall sandbox so it is genuinely ready, then export it and run Dial Your Course against it as a real test.

**Audience:** Me.

**Process:** Fix by hand only what a tool cannot fix. Leave everything a tool *should* catch, so the test means something. Build, export, run, compare against this sheet.

---

## The discipline for this build

> **Do not hand-fix the things the tool is supposed to find.**

If you pre-polish the course, the tool reports a clean bill of health and **you learn nothing about whether it works.** The point of running it on a real course is to find out whether it finds what is there.

| Fix by hand | Leave for the tool |
|---|---|
| Structure, dates, points, rubrics | **Colour and typeface** — the style guide writes Pine |
| Assignment groups + turn weighting **ON** | **Alt text** on any image you add |
| Learning outcomes in Canvas Outcomes | **Heading structure** |
| Video placeholders and scripts | **Privacy-policy links** (OSCQR 14) |
| Delete the orphan rubrics and stale dates | **Workload / seat-hour totals** |
| Rebuild the two vocabulary quizzes | **PII scan of course Files** |
| | **Alignment matrix** — it should build itself once Outcomes exist |

**Then check the report against this sheet.** Anything on the right that it *misses* is a bug in the tool. Anything on the left it *reports* means I did not finish the build.

---

## 1 · Videos · placeholders and scripts

**Six videos. Three are essential; three are nice.** Put the placeholder in now so the page structure is right, then record into it.

### Where each one goes

| # | Video | Lives in | Length | Priority |
|---|---|---|---|---|
| **1** | **Welcome to AVC 100** | Getting Started module, top | 2–3 min | **Essential** — instructor presence (OSCQR 40) rests entirely on this |
| **2** | **Illustrator: the Pen tool** | Lesson and Exercise: Illustrator | 6–8 min | **Essential** |
| **3** | **Photoshop: selecting a subject** | Lesson and Exercise: Photoshop | 6–8 min | **Essential** |
| **4** | **After Effects: two keyframes** | Lesson and Exercise: After Effects | 5–7 min | **Essential** — script already written |
| **5** | **How critique works here** | Getting Started, after Technology Orientation | 3–4 min | Nice |
| **6** | **Photographing your thumbnails** | Poster · Step 1: Sketch | 2 min | Nice — but it directly serves the new capture criterion, and it is 2 minutes |

### The placeholder to paste into each page

Inline styles only, so Canvas does not strip it. **Pine palette values, so it matches what the tool will write.**

```html
<div style="border:2px dashed #c0d5cb;background-color:#e3efe9;border-radius:6px;padding:18px 22px;margin:20px 0;font-family:Verdana,Geneva,sans-serif;">
  <p style="margin:0 0 6px;font-weight:bold;color:#1f4d3a;font-size:16px;">🎥 Video: [TITLE]</p>
  <p style="margin:0 0 10px;color:#22332c;font-size:15px;line-height:1.65;">
    <strong>Coming soon.</strong> This walkthrough covers [WHAT IT COVERS]. Until it is posted,
    work from the written steps below — they cover the same ground.
  </p>
  <p style="margin:0;color:#2f6b52;font-size:14px;">
    <a href="[SCRIPT LINK]" style="color:#2f6b52;">Script and step-by-step instructions &rarr;</a>
  </p>
</div>
```

**The placeholder is not an apology. It is a fallback.** A student who arrives before the video exists still has the written steps, which means the page works either way. **Never ship a placeholder that offers nothing.**

### Where the scripts live

**Create a module at the top called `Instructor Notes`, and unpublish it.**

- **Unpublished modules do not appear to students** and travel with the course copy, so every faculty member who copies this course gets the scripts too.
- Put each video script on its own page inside it.
- Link each page from its video placeholder.

> **One caution.** An unpublished module is invisible to students, **but course Files is not.** If you upload a script as a file rather than a Canvas page, and Files is published, a student can browse to it. **Use Canvas pages, not file uploads.**

**Already written:** the After Effects script (two Position keyframes, Easy Ease, comp setup) — from the terminology pass against Adobe's own documentation.

**Still to write:** Welcome, Pen tool, Selection, Critique, Thumbnails.

---

## 2 · Learning Outcomes · do this before you export

**This is the one that makes or breaks the tool test.**

Your syllabus lives in **Simple Syllabus**, which is a separate application. **Canvas has no outcomes for this course**, so the alignment matrix cannot build itself — and alignment is the tool's headline claim.

1. **Canvas → Outcomes.** *(Not in the nav? Settings → Navigation → drag Outcomes up → Save.)*
2. **+ Group** × 5, one per MCCCD competency:
   - `1 · Operate a computer`
   - `2 · Create digital art and design projects using the computer`
   - `3 · Use tools available in the software package`
   - `4 · Use various input and output devices`
   - `5 · Prepare images for print and presentation`
3. **Inside each group, + Outcome** for the module-level objectives that roll up to it. **Use your twelve Bloom's objectives, not the district text.** You grade yours; theirs get satisfied as a consequence.
4. **Bind each to a rubric criterion:** assignment → Rubric → Edit → **Find Outcome** → Import.

**Click "Find" first.** It pulls account-level outcomes. **If Maricopa has ever loaded the board-approved competencies into Canvas, they are already there** and you import them in thirty seconds instead of typing anything.

**When this is done, the tool builds the alignment matrix with no typing, on this export and every future one.**

---

## 3 · Assignment groups · the ten-second fix that matters most

1. Create two groups: **Projects** and **Exercises and Reflection**.
2. **Assignments → three-dot menu, top right → Assignment Group Weight.**
3. ✅ **Weight final grade based on assignment groups.**
4. **Projects 55% · Exercises and Reflection 45%.**

> **Your current course has weighted groups (50/50) and weighting switched OFF.** Canvas is ignoring them and grading raw points. **The syllabus says one thing and the gradebook does another**, and a student finds the gap while calculating what they need on a final.

Also create a third group, **Student Success**, or keep those six inside Exercises and Reflection — but **name the group either way**, so the co-curricular intent is visible in the gradebook rather than inferred.

---

## 4 · Structure

**Five modules, unchanged. Nine project steps, not seven.**

| Module | Contains |
|---|---|
| **Instructor Notes** *(unpublished)* | Video scripts |
| **Getting Started** | Syllabus & Course Intro · Introduce yourself · Technology Orientation · Welcome video · Critique video |
| **Student Success** | 6 items × 3 pts, checkmark-graded, **including Digital Media Programs at GCC** |
| **Graphic Design Poster** *(Illustrator)* | Colour Palette Exercise · Lesson · **Sketch → Build → Refine** |
| **Photographic Postcard** *(Photoshop)* | Lesson · **Sketch → Build → Refine** |
| **Social Media Animation** *(After Effects)* | Lesson · **Sketch → Build → Refine** |
| **Launch It** | Behance Portfolio · Course Reflection |

**Every project step is 15. Behance is 10. Exercises are 10.**

---

## 5 · Delete these

| | Why |
|---|---|
| **Rubric: "Phase 3 Project + Critique"** | References "Phases," a structure the course no longer uses. Attached to nothing. |
| **Rubric: "Final revised project"** | Grades "Phase 1 PDF / Phase 2 JPG / Phase 3 MP4." No such assignment exists. |
| **Assignment: "Getting Help with Coursework or Technology"** | Duplicate of "Where to get help," in no module, worth 5 while its siblings are 3, **and carrying a stale due date of July 13, 2026.** Merge the content in, delete the assignment. |
| **The matching question in both vocabulary quizzes** | Corrupted at the QTI level — every answer choice shares one `ident`. **It will corrupt again on every course copy.** |

**Rebuild both quizzes as multiple choice only.** The MC questions exported cleanly; only matching is broken. The six imaging questions are already correct.

---

## 6 · Fix these by hand

| | |
|---|---|
| **"Introduce yourself"** | Hardcoded *"Sunday May…"* / *"Friday May…"* in the body text. **Remove.** The Canvas due date already says when it is due, and hardcoded dates break on every copy. |
| **After Effects exercise rubric** | 20 points on a 10-point assignment. Rebuild at 10. |
| **Animation rubric** | Grades "assets imported and placed in the template." **The template exists** — `AVC100_Travel_Animation_Template.aet`, in course Files inside a zip. Confirm the assignment actually links students to it. |
| **All 9 project rubrics** | Rebuild at 15, with the new capture and output criteria. |

---

## 7 · Leave these alone · they are the test

**Do not fix these before you export. They are what you are testing.**

- ❌ **No privacy-policy links** for Discord, Miro, Behance, Adobe, YouTube. *(OSCQR 14 — the tool should flag five tools.)*
- ❌ **No Pine palette applied.** Pages inherit Canvas defaults. *(The style guide should write Pine into every page.)*
- ❌ **Captions unverified** on 2 embedded and 6 linked videos. *(The tool should count 8 videos and correctly exclude the 25 YouTube channel links, which are not videos.)*
- ❌ **Workload over budget.** ~31 hours against a 26.5-hour outside-work allowance. *(The tool should report ~118%.)*
- ❌ **Single submission format** on most assessments. *(The UDL check should flag Principle 3.)*

---

## 8 · Then: export and run it

**Canvas → Settings → Export Course Content → Course.**

Drop the `.imscc` into Dial Your Course and check the report against Section 7.

### What a working tool should report

| Check | Expected |
|---|---|
| **Parse** | ~35 pages · 29 assignments · outcomes **> 0** · rubrics ≈ 12 · groups 2–3 · quizzes 2 · modules 6–7 |
| **Alignment** | Matrix builds. Every competency evidenced. **No "no outcomes defined" error** — that is the sign the Outcomes work landed. |
| **Grade weighting** | **Passes.** No "weighting is switched off" finding. |
| **OSCQR 14** | **Fails** — five third-party tools, no privacy links |
| **OSCQR 23** | Passes — no inline fonts |
| **OSCQR 35** | 8 videos to caption · 2 embedded, 6 linked, **25 channel links excluded** |
| **Seat hours** | ~118% of budget |
| **UDL P3** | Most items single-format |
| **PII scan** | Clean |
| **Style guide** | Writes Pine into every page; download the restyled `.imscc` |

### The two failure modes to watch for

1. **It reports AVC100's old numbers.** Then something is still hardcoded and I have work to do.
2. **It reports a problem you fixed.** Then a check is stale.

**Preview before you import anything, and import into a sandbox, never a live section.**
