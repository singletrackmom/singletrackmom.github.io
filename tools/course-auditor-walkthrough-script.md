# Dial Your Course · walkthrough script

**Goal.** Show, in about three minutes, that the tool reads a real Canvas export, computes every finding, and hands the course back changed. A viewer should finish knowing it works and knowing what it refuses to do.

**Audience.** Hiring committees (Mines OLED), instructional designers, the CTLE, and colleagues being asked to break it. Educated, not technical. No jargon that needs a footnote.

**Process.** Screen recording, real course (AVC100), no slides, no talking-head intro. One take per section, cut together. Voice over a live screen.

---

## Before you record

- Open the tool at `/tools/course-auditor.html`, fresh reload, nothing loaded.
- Have the AVC100 `.imscc` on the desktop, visible, so the drop is real on camera.
- Set credits to 1 and outside hours to 26.5 before you start talking about them.
- Close every other tab. Hide the bookmarks bar.
- Record at 1280 x 720 or larger. Zoom the browser to 125 percent so text is readable on a phone.

---

## 0:00 · Cold open, no preamble

*(Screen: the empty tool. Cursor drags the .imscc file onto the drop zone. It loads.)*

> This is a Canvas course. Not a demo course, my course, exported this morning. I am going to drop it into a tool I built and let it tell me what is wrong with it.

*(Findings appear.)*

> Nineteen checks just ran against it. Everything you are about to see was computed from that file. Nothing here is a template and nothing here is a guess.

**Why this opening.** No logo, no "hi, I'm Michelle." The first eight seconds prove the thing works. Everything else is elaboration.

---

## 0:20 · The problem, in one breath

*(Screen: scroll the findings list slowly.)*

> Online course review is done by reading. One person opens the course, reads it top to bottom, and forms an impression. It takes hours, it is inconsistent between reviewers, and the parts that are actually countable never get counted. Those are the parts this checks.

---

## 0:35 · Seat time · the HLC finding

*(Screen: open the workload card. Show 30.8 hours against the 26.5-hour allowance.)*

> A one-credit course carries forty hours of student work. Thirteen and a half of those happen in class. The other twenty-six and a half happen outside it, and in an online course there is no classroom to observe, so the course package is the only evidence those hours exist.

> The Higher Learning Commission has flagged seat time in online courses at my institution. This is the finding that answers it. The tool reads every assignment, estimates the work, and tells me my course is running at a hundred and sixteen percent of what the credit allows.

> I can correct every one of these numbers. It is an estimate and it says so.

**Do not say** "no other tool does this." Do not editorialize about HLC.

---

## 1:05 · Outcomes and alignment · the bigger accreditation story

*(Screen: the competency map. Fourteen outcomes, the coverage figure.)*

> This is the part accreditors actually ask about. HLC's Criterion 3.E is assessment of student learning: can you show that what you claim to teach is evidenced by something you grade.

> The tool reads the course's outcomes, reads every rubric, and reports how many of those outcomes are actually collected somewhere. It reports the real number. When my coverage was low, it told me it was low.

*(Screen: the declared-exception radio buttons.)*

> Not every gap is a mistake. Some of my assignments carry no outcome on purpose, because they are formative. So the tool lets me say so, and say why. That turns an omission into an argument I can defend in a review, instead of a red flag I have to explain.

---

## 1:40 · The AI-resistance audit · the part people remember

*(Screen: the airesist card. Nine strong, five adequate, two exposed.)*

> This one asks a question I could not find a tool for: could a student pass this assignment without doing it.

> It does not look at the assignment title. It reads the rubric criteria, because the rubric is where evidence is actually collected. It looks for seven signals: did the student capture something physical, is there a record of process, was critique given and answered, is a decision defended, is the content local and specific.

> My nine project steps come back strong. Two items come back exposed. And the point I want to make is that the authenticity of the task is not what protects it. A model will happily write a portfolio case study or a reflective essay. What resists substitution is the record of making.

---

## 2:10 · Accessibility, and what it will not do

*(Screen: the a11y card, then the coverage table.)*

> Ten structural checks: alternative text, headings that are actually headings and not bold paragraphs, link text that says where it goes, table headers.

> And then this table, which is the part I care about most. It says plainly what this tool does not check. It does not open your PDFs. It does not verify that your captions are correct, only that they exist. For those, it tells you exactly where to go in Canvas.

> A check that cannot be computed is never reported as a pass. That rule is the whole tool.

---

## 2:30 · Approve, export, and the list only Canvas can do

*(Screen: Step 4. Show a typo edit, click into the text field, change the suggested wording.)*

> Every change is proposed, not applied. And where it suggests wording, I can edit the wording. It is my course.

*(Screen: click export. The file downloads.)*

> That writes the approved fixes and the time budget for each module back into the package, and hands me a file I import into a sandbox.

*(Screen: Step 5 appears, six items.)*

> And then this. Six things a course package physically cannot carry, because they are account-level objects only Canvas holds. Attaching an institutional outcome to a rubric is one of them. So it becomes a checklist with the exact click path, and it stays ticked when I come back.

---

## 2:50 · Close

> It uses no AI. It was built with AI, and it runs on rules, which is why it cannot invent a finding. There is a version two in the interface, greyed out, that shows the four things a model could add. Those need a sanctioned endpoint the college controls, and that is a conversation I am trying to start.

> It is a prototype. It is in testing across Digital Media Arts. If you want to try to break it, the link is below and I would like to hear what you find.

*(End. No outro card. Cut hard.)*

---

## Rules for the recording

- Say the number, then show the number. Never the reverse.
- Do not apologize for the prototype status. State it once, at the end, plainly.
- No claims about other products. Not one.
- If a check throws or misfires on camera, keep it and say so. It is a prototype and honesty is the pitch.
- Target 3:00. Hard cap 3:30. If it runs over, cut the accessibility section, not the AI-resistance one.
- This is the longest video in the portfolio, and only because it has a live demo. Every other project gets 2:00 to 2:30. See WALKTHROUGH-PLAN.md.

---

## Reusable outline for the other project walkthroughs

Every walkthrough uses the same five beats. Only the content changes.

1. **Cold open.** Do the thing on camera in the first ten seconds. No introduction.
2. **The problem**, in two sentences, with no throat-clearing.
3. **Two features**, the ones that would make a skeptic sit up. Not five features. Two.
4. **The limits.** What it will not do, and what it refuses to guess. This is what makes the rest credible.
5. **Status and the ask.** What it actually is right now, and what you want from the viewer.
