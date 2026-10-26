# Module 0 · Getting Started (standard for every course)

> **Slimmed 25 Oct 2026 (Michelle).** Module 0 is “clean and clear and not cluttered up with a bunch of rules and syllabus stuff.” Students download software, meet the instructor, read the syllabus and take the syllabus quiz, then complete the AI Primer, and Module 0 is done. Course rules (deadlines and late work, critique, accessibility of student work, grading, competencies, college policies, support services, AI use) live in the syllabus, not in Module 0. The text that came out of Module 0 is preserved as proposed syllabus wording in `drafts/SYLLABUS_REVIEW.md`; the full earlier master is in `drafts/MODULE0_FULL_VERSION.md`.
>
> **Module 0, in order, identical in every course (AVC100 has no AI part):**
> 1. **Welcome** (the Start Here page in Canvas): a few sentences on how the course is organized, the course introduction slot, and where the syllabus is.
> 2. **Meet Your Instructor:** the introduction video and how to make contact (Canvas Inbox for private questions, the course channel on the Digital Media Discord for course questions). Reply times live in the syllabus.
> 3. **Technology Setup:** the equipment slot, then the Technology Setup assignment (core accounts, software, the computer-loan request link).
> 4. **Syllabus:** read the syllabus, then the Syllabus and Course Overview Quiz. Every quiz question is answered in the syllabus. The short list of syllabus topics carries the `#deadlines`, `#critique` and `#accessibility` anchors that later assignments link to.
> 5. **AI Primer** (AI courses only): a two-line pointer to the syllabus AI section and Google’s sources (anchor `#ai`), then the AI Primer assignment, unchanged.
>
> Course slots still used: `course_intro`, `instructor_extra`, `equipment`, `setup_extra`, `quiz_extra`, `course_sections` (course-specific pages later modules link to, such as AVC150 Consent and Privacy, AVC248 Recordings), `ai_extra` (AVC283 AI-Use Log Template), `instructor_notes`, and `competency_map`, which now sits inside the hidden Instructor notes. Slots dropped from Module 0: `how_extra`, `critique_extra`, `support_extra`, `course_description`, `materials_extra`, `grading`, `competencies`, `ai_course_rules`, `read_extra`; their text is in the appendix of `drafts/SYLLABUS_REVIEW.md` for each course’s syllabus.

> **Built, not copied (25 Oct 2026).** The exact student text for Module 0, AI in This Course, Technology Setup, the AI Primer and the Syllabus Quiz lives in ONE file, `canvas/_shared/module0.html`, and `tools/course-build/build.py --all` puts it into every course page. Edit that file, never a course page. This markdown holds the reasons and rules; the master holds the words. No course has a "Where You Stand" or AI-position discussion (Michelle, 25 Oct 2026). AVC100 gets Module 0 without the AI parts.


Student-facing rule: describe the workflow as simply how the course works. Never say something is new, now, changed, moved, revised or replaced; students never saw an earlier version.

Set 24 Oct 2026. Simplified from the live AVC183 and AVC248 Start Here modules (two quizzes and two Technology Login Challenges become one quiz and one setup assignment). Every course's Module 0 uses this pattern; only the software table changes per course.

No required textbooks: Near Z Degree program; use OER and free sources. (See `program-design/PROGRAM_NOTES.md`.)

One deadline (the first Thursday, noon). Seat hours per course stay as set in `tools/course-build/build.py`.

## Instructor notes (box at the top)
- Before the term: create the course channel on the Digital Media Discord and paste its invite link into the Technology Setup page and a Canvas announcement. Confirm the class is on the district Adobe Creative Cloud list.
- Week 1: welcome everyone in Discord, reply to each introduction, and message anyone with no Discord intro by Wednesday.
- Grade Technology Setup within 48 hours; anyone missing software gets a direct fix, not a deduction, on the first try.

## Objectives
- 0.1 Set up and verify every core course account, and record and share a short narrated test recording.
- 0.2 (AI courses) Write and revise a prompt in Gemini, and evaluate its answer critically.

## Items
| # | Item | Type | Points |
|---|---|---|---|
| 1 | Start Here: welcome, meet the instructor | Page | none |
| 2 | Technology Setup (core accounts, test recording, Discord introduction) | Assignment, Process Work | 10 |
| 3 | Syllabus and Course Overview Quiz (every answer is in the syllabus) | Quiz, Exercises | 5 |
| 4 | AI in This Course: two-line pointer to the syllabus AI section (AI courses) | Page | none |
| 5 | AI Primer (AI courses) | Assignment, Process Work | 10 |

Student-facing pages never show planning codes (S1, D4, PW18); use plain item titles and ‘Grading (N points)’.

## Technology Setup (the one setup assignment)
Two rules (revised 24 Oct 2026): the same core accounts in every course, set up in week 1; course-specific apps set up just in time, in the module where they are first used (each of those modules has a short setup step). Students are graded on the outcome, not on one brand of tool.

Core accounts, every course, week 1:
| Tool | What it is for | How to get it |
|---|---|---|
| Canvas | Assignments and grades | Log in with MEID |
| Maricopa Google account | Gmail, Drive, Docs, YouTube (unlisted videos), Gemini | Log in with MEID@maricopa.edu |
| Gemini | Research, writing and feedback; never visual design | gemini.google.com with the Maricopa account (never a personal account) |
| Google Sites | Where you publish web pages and interactive work in every course | sites.google.com with the Maricopa account; nothing to install |
| Adobe Creative Cloud | The district license for every design app | adobe.com, sign in with the Maricopa email; install apps when a module first needs them |
| Discord | Daily questions, critique, class community | Join the course channel: https://discord.gg/EXAMPLE-COURSE (placeholder) and download from discord.com/download |
| A way to record and share | Showing and explaining your work all term | Your choice; see below |

Recording, by field (one line per student type, so nobody guesses):
| If you are | Use this to record | What you share |
|---|---|---|
| A visual design, animation, web or game student | OBS Studio (obsproject.com, free); Meet, Zoom, QuickTime or Snipping Tool also work | A short screen video with your voice |
| A sound design student | Your audio tool: Audition, Reaper or Audacity (a phone voice memo works too) | A short audio clip with a one-line written description; add OBS only when a project needs you to show a screen |
| A screen-reader user | Whatever recorder you already use with your screen reader | A short audio or video clip; tell the instructor if nothing works so an equivalent is set up |

Recording, your choice of tool. The outcome is the same for everyone: a short recording of you explaining something on your screen or in your project, shared as an unlisted link. Default recommendation is OBS Studio (obsproject.com, free). Equal options: a Google Meet or Zoom recording, QuickTime (Mac) or the Windows Snipping Tool screen recorder, or for audio-first and sound design work an audio recording from Audition, Reaper, Audacity or a phone voice memo with a short written or spoken description. Screen-reader users: OBS can be hard to operate with a screen reader; use whichever recorder you already use with yours, and tell the instructor if none works so an equivalent is set up. No one loses points for which tool they use.

Discord rules: questions go in the course channel, not DMs; set the server nickname to the name you want to be called; add a profile photo or avatar; screen names are allowed; add alt text to every image you post and a transcript or caption to every audio or video post.

Submit (a Google Doc, Google Slides page or Miro board, whichever works with your tools):
1. Proof each core account works (screenshots, or a short written confirmation for screen-reader users).
2. A link to a 10-second test recording (video or audio) with your voice and something from your work, shared unlisted.
3. Your Discord introduction (name and pronunciation, program, one thing to learn, two examples of past work with alt text or a description) and three comments on classmates' introductions.

Rubric, 10 points: core accounts 4, test recording 3, Discord introduction 2, three comments 1.

Instructor notes addition: in week 1, privately ask each student what tools and assistive technology they use, contact Disability Resources and Services for any accommodation, and approve an equivalent recorder for anyone who needs one.

## Course-specific apps (set up in the module where first used, not in Module 0)
- AVC100: Photoshop, Illustrator, After Effects (Creative Cloud).
- AVC150: Premiere Pro and Audition (Creative Cloud), Adobe Express, Gemini Notebook.
- AVC183: Illustrator, InDesign, Photoshop (Creative Cloud), Miro, Figma.
- AVC190: Figma (education plan), Illustrator and Photoshop, Google Sites, WAVE; optional VS Code for the code option.
- AVC2xx: Figma, Miro, plus the student's own field tools (Unity or Unreal, Blender, Audition or Reaper).
- AVC248: Adobe Portfolio or Behance, LinkedIn, Google Sites, Gemini.
- AVC283: Illustrator, InDesign, Photoshop, Acrobat (Creative Cloud), Gemini Notebook.

## Accessibility of student work (every course, every assignment)
Set 24 Oct 2026. Required on every submission and every Discord post; stated in the syllabus and on each assignment that produces media (not in Module 0, from 25 Oct 2026).
- Video: accurate captions. Start with automatic captions (YouTube Studio, Premiere Pro Speech to Text, Google Vids or Meet), then read every line and fix names, terms and timing by hand. Automatic captions alone are not enough.
- Audio: a transcript (auto-transcribe, then correct by hand) and, for sound pieces, a short text description of the important non-speech sounds.
- Images: alt text on every meaningful image (one or two sentences on what matters, not "image of"); decorative images marked decorative.
- Documents and slides: real headings, readable contrast, and alt text; PDFs exported with tags.
- Web pages (Google Sites): headings in order, descriptive link text, alt text, captions on embedded video, checked with WAVE or a screen reader.
- Grading: each media assignment rubric includes captions or transcript and alt text (about 10 percent of the points).
- Instructor: every instructor video is captioned and corrected the same way; every course page passes the course accessibility check.

## Deadline rhythm (stated in the syllabus and in Module 0 Instructor notes in every course)
- Everything is due at noon, Arizona time. Never midnight.
- Late work: accepted for 24 hours after the deadline at 10% off. Nothing is accepted after noon the day after.
- Critique: every project step and project (Process Work and Projects) is posted to the class Discord by noon the day before it is due, and students leave three critique comments by the due time. Exercises, readings, quizzes and reflections have no Discord step; they follow the noon due time and the late rule only.
- Each assignment page shows only what applies to it: projects show all three times (Discord the day before, due, hard close); other items show the due time and hard close.

25 Oct 2026: three critique comments everywhere, including on Discord introductions (Michelle). Final projects are due Thursday of finals week.
