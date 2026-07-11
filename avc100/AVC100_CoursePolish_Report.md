# AVC 100 · Dial Your Course Report

**Run date:** July 11, 2026 · **Profile:** 1 credit, loads at 2, lecture/lab (studio), online
**⚠️ Source caveat:** run against the **repo files**, not the sandbox Canvas course. Re-run once the `.imscc` export lands.

---

## 🔴 FINDING 1 · The course is 34% over its seat-hour budget

**This is the most important thing in this report.**

AVC100 is a **1-credit** course. The rule is `credits × 40`, so:

| | Hours |
|---|---|
| Total student hours | **40** |
| Direct instruction (my videos, lessons, content) | 13.5 |
| **Student work (them doing things)** | **26.5** |

The proposed fall structure requires **35.5 hours** of student work. **Nine hours over budget.**

And those estimates were **generous to the course.** I budgeted **3 hours for a complete Illustrator travel poster** made by someone who has never opened Illustrator. The realistic number is 5 to 6. That pushes the true total toward **45 hours, nearly double the budget.**

### The honest diagnosis

**AVC100 is a 3-credit course wearing a 1-credit shell.** Three Adobe applications, three complete design projects, a critique practice, and a published portfolio, in 40 total hours.

The 3-part restructure is pedagogically *correct* and it makes the overage *worse*, by about 4.5 hours.

This likely explains more about how the course feels than anything else in it. **Students are not struggling because they are underprepared. They are struggling because they are doing 3-credit work for 1 credit.**

And this course is about to be copied by other faculty, who will each quietly discover the same thing.

### Options

| Lever | Saves | What it costs |
|---|---|---|
| **Drop to two projects** (cut the poster) | ~7 hrs | Lose Illustrator entirely. Large. |
| **Critique 2 classmates instead of 4** | ~2 hrs | Weakens the thing the course exists for. Resist. |
| **Part 3 = written reflection, not rework** | ~3 hrs | Keeps the critique loop, loses the revision practice. |
| **Petition to make AVC100 a 2-credit course** | Fixes it properly | Curriculum committee. Slow. **The true answer.** |

**Recommendation:** the course is not badly designed, it is **mis-credited.** Pursue the credit change. In the meantime, "Part 3 = reflection, not rework" is the cheapest honest cut.

---

## 🔴 FINDING 2 · Lora will not render in Canvas

You asked for Lora, your design-system typeface. **It cannot work in Canvas.**

Lora is a Google Font, loaded with a `<link>` tag. **Canvas strips `<link>` tags when it sanitizes a page on save.** Your editor preview will look correct, and every student will see a fallback serif. This is the silent failure mode, and it is why the tool restricts you to five typefaces.

**Substitute: Georgia.** Warm, high x-height, readable serif. The closest thing to Lora that is installed on essentially every machine and will actually render.

If you ever want real Lora in Canvas, it requires an LTI that injects global CSS (DesignPLUS / CidiLabs). That is a district purchase, not a paste.

---

## ✅ FINDING 3 · Green palette, all pairs pass WCAG AA

Pulled straight from your own `shared.css`, so the course matches your design system.

| Role | Hex | |
|---|---|---|
| Header background | `#3a6348` | deep pine |
| Subheadings | `#4a7c59` | sage green |
| Links / accent | `#7a5a1f` | warm gold |
| Callout box | `#e4ede5` | pale sage |
| Rules / borders | `#c3d1c5` | |
| Body text | `#2e3a30` | near-black green |

**Contrast, all passing (4.5:1 minimum):**

| Pair | Ratio | |
|---|---|---|
| White on header green | **6.87:1** | ✅ |
| Subheading on white | **4.86:1** | ✅ |
| Body on white | **11.9:1** | ✅ |
| Links on white | **6.34:1** | ✅ |
| Body on callout box | **9.95:1** | ✅ |

Solid colors only. No gradients.

---

## 🟡 FINDING 4 · Objectives are not measurable

Checked against the banned-verb list. **This course is written at the wrong Bloom's level throughout.**

AVC100 is a 100-level intro course, so objectives should live in **Understand → Apply → Analyze.** Students should be *making* things, not *knowing about* them.

### Rewrites

| Assignment | Current (unmeasurable) | Rewritten (observable) | Level |
|---|---|---|---|
| **Color Palette** | "Students will understand color theory." | "Using Adobe Color, **construct** a five-color palette and **justify** each choice against the poster's mood." | Create / Evaluate |
| **Pen & Shape** | "Learn the pen tool." | "**Trace** a reference image using the Pen tool, **producing** closed paths with fewer than 12 anchor points." | Apply |
| **Poster Part 1** | "Plan your poster." | "**Sketch** four thumbnail compositions and **select** one, **explaining** the hierarchy choice that drove the decision." | Analyze / Evaluate |
| **Poster Part 2** | "Develop the poster." | "**Construct** an 18 × 24 vector poster **applying** a defined palette, limited type, and a clear focal hierarchy." | Create / Apply |
| **Poster Part 3** | "Finalize and export." | "**Revise** the poster in response to at least two specific peer critiques, **articulate** what changed and why, and **export** print-ready PDF and web JPG." | Evaluate / Create |
| **Cut It Out** | "Understand selections." | "**Isolate** three subjects from their backgrounds using Select Subject and **refine** the edges." | Apply |
| **Postcard Part 2** | "Build your postcard." | "**Composite** a destination photo, an isolated animal, and type into a layered 1200 × 1800 PSD, **maintaining** editable layers." | Create |
| **Animation Part 2** | "Build the animation." | "**Animate** two layers into frame using paired Position keyframes and **export** an H.264 MP4." | Apply |
| **Behance** | "Publish a portfolio." | "**Curate** three finished projects into a published Behance project and **compose** a description of tools used and decisions made." | Create / Evaluate |

### The trap, worth teaching

**"Understand" is a valid Bloom's *level* and an invalid objective *verb*.** The level names the cognition. The verb has to name the **observable evidence** of it. If you cannot observe it, you cannot assess it.

**Banned throughout:** understand, know, learn about, appreciate, be familiar with, be aware of, grasp, comprehend.

---

## 🟡 FINDING 5 · Missing content: Digital Media Foundations

The course teaches software and critique but never teaches **how digital media actually works.** Nothing on:

- **Raster vs. vector** and why it matters
- **Resolution** (72 vs 300 ppi, image size vs canvas size)
- **Why Illustrator vs. Photoshop vs. After Effects**
- **File formats** and which are native, lossy, or transparent
- **File naming conventions**
- **Folder structure and where files are actually saved**
- **Always keep your native file**

This is not a gap in a software course. Given what AVC100 is actually *for*, media literacy, terminology, and critique, **this is the curriculum.**

**Recommendation:** a short, required, ungraded **Foundations page per unit.** Scaffolded, never dumped. See `AVC100_Foundations.md`.

---

## 🟡 FINDING 6 · Three source files contradict each other

If faculty copy this course today, **they copy the contradictions.**

| File | Says |
|---|---|
| `AVC100_All_Projects_and_Exercises.md` | Animation build uses **a template** |
| `AVC100_SocialMediaAnimation_ForCanvas.md` | Animation build uses **no template** (current) |
| `AVC100_All_Video_Scripts.md` | "Build **from the template**" |
| `AVC100_Schedule.md` | Still lists the axed **Make It Move** |

**Blocked on the sandbox export.** Reconcile against the real course, then delete the losers.

---

## 🟡 FINDING 7 · Peer critique is timed backwards

Students post to Discord **two days before the deadline**, receive feedback, and then submit. **They have no time to act on it.** The feedback is decorative, and they know it.

**Fixed by the 3-part structure:** put the critique round *between* Part 2 and Part 3. Feedback lands after they have built something and before they finalize it, which is where critique belongs.

---

## Summary

| # | Finding | Severity |
|---|---|---|
| 1 | **34% over seat-hour budget. Course is mis-credited.** | 🔴 |
| 2 | Lora cannot render in Canvas. Use Georgia. | 🔴 |
| 3 | Green palette, all WCAG AA pairs pass | ✅ |
| 4 | Objectives unmeasurable throughout. Rewrites provided. | 🟡 |
| 5 | Digital Media Foundations content missing entirely | 🟡 |
| 6 | Three source files contradict each other | 🟡 |
| 7 | Peer critique timed so it cannot be acted on | 🟡 |

**Re-run this report against the sandbox `.imscc` before acting on anything structural.**
