# Module 0 · Getting Started (standard for every course)

> **Current standard, set 7 Nov 2026 (Michelle).** Module 0 is two videos (Meet Your Instructor, then the Course Walkthrough with its built-in Canvas Studio quiz), then the Technology Login Challenge, the AI Primer and the introductions discussion. Nothing else. No syllabus information in Module 0; course rules live in the syllabus (Syllabus+). Instructor notes sit at the TOP of every module in every course, collapsed, instructor only.
>
> **Module 0, in order, identical in every course:**
> 1. **Instructor notes** (collapsed), including the course’s competency map.
> 2. **Welcome** (the Start Here page in Canvas, published before the rest of the course so students can drop in time): course description, an expanded description the instructor writes, the course competencies, the computer requirement and Student Technology Request link, and (AI courses) that the course uses Gemini and why it is safe. Slots: `course_description`, `competencies`.
> 2b. **Objectives** (0.1 setup; 0.2 AI Primer in AI courses).
> 3. **Meet Your Instructor:** captioned video, 3 minutes at most, and a short bio.
> 4. **Course Walkthrough:** captioned Canvas Studio video, up to 15 minutes: Canvas navigation, all materials in Modules, the student support button (CopaMigo and student resources), then the entire syllabus. A Canvas Studio quiz is built into the video: it pauses at five questions answered on screen, and the fifth is always “Have you read the syllabus, and do you understand everything in it?” That is the whole syllabus quiz; there is no separate quiz.
> 5. **Technology Login Challenge** (10, Process Work): core accounts and a test recording. In AI courses the private under-18 question rides in this submission.
> 6. **AI Primer** (10, Process Work), AI courses.
> 7. **Introductions** (5, Exercises, discussion): Discord post by Wednesday noon, three comments by the Thursday deadline. AVC100 has no AI Primer; it ends with **Student Success** (the `student_success` slot).
>
> Slots used: `equipment`, `setup_extra`, `instructor_notes`, `competency_map`, `student_success` (AVC100). The Syllabus Quiz and the `quiz_extra` slot are gone. Links that used to point at Module 0 syllabus anchors now name the section “in the syllabus.” The words live in ONE file, `canvas/_shared/module0.html`; run `tools/course-build/build.py --all`. Never edit Module 0 on a course page. No course has a “Where You Stand” or AI-position discussion.

Student-facing rule: describe the workflow as simply how the course works. Never say something is new, now, changed, moved, revised or replaced; students never saw an earlier version.

Set 24 Oct 2026. Simplified from the live AVC183 and AVC248 Start Here modules (two quizzes and two Technology Login Challenges become one quiz and one setup assignment). Every course's Module 0 uses this pattern; only the software table changes per course.

No required textbooks: Near Z Degree program; use OER and free sources. (See `program-design/PROGRAM_NOTES.md`.)

One deadline (the first Thursday, noon). Seat hours per course stay as set in `tools/course-build/build.py`.

## Instructor notes (box at the top)
- Before the term: create the course channel on the Digital Media Discord and paste its invite link into the Technology Setup page and a Canvas announcement. Confirm the class is on the district Adobe Creative Cloud list.
- Week 1: welcome everyone in Discord, reply to each Introductions post, and message anyone with no post by Wednesday.
- Grade Technology Setup within 48 hours; anyone missing software gets a direct fix, not a deduction, on the first try.

## Objectives
- 0.1 Set up and verify every core course account, and record and share a short narrated test recording.
- 0.2 (AI courses) Write and revise a prompt in Gemini, and evaluate its answer critically.

## Items
| # | Item | Type | Points |
|---|---|---|---|
| 1 | Meet Your Instructor: video (3 minutes max) and bio | Page | none |
| 2 | Course Walkthrough: Canvas Studio video (up to 15 minutes) with a five-question embedded quiz | Page, Studio quiz | none in Canvas |
| 3 | Technology Login Challenge (core accounts, test recording) | Assignment, Process Work | 10 |
| 4 | AI Primer (AI courses) or Student Success (AVC100) | Assignment | 10 / 5 |
| 5 | Introductions | Discussion, Exercises | 5 |

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
- AVC294: Figma, Miro, plus the student's own field tools (Unity or Unreal, Blender, Audition or Reaper).
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
