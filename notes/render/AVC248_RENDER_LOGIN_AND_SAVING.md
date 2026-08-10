# Render Pilot: Login, Data, and Hosting Recommendation

**Prepared by:** Michelle Blomberg, Residential Faculty, Digital Media Arts, Glendale Community College
**Regarding:** How students sign in, where their work is stored, and where Render is hosted for the AVC248 pilot
**Date:** August 2026

---

## Recommendation at a glance

- **Identity: anonymous handle, no student identity stored.** Students sign in with a made-up handle and a PIN, never a name or email. The system can tell 44 accounts apart without knowing who anyone is.
- **Grading: through Canvas, never inside Render.** Render is the student's own workspace. It outputs what they need (resume, future plan, reflections on the jobs the agent finds) and they submit those to Canvas under their real Canvas login. The instructor never opens a student's Render.
- **Hosting: the page on district GitHub Pages, the backend on Supabase.** The static interface lives on a district-owned GitHub organization. The login, saved work, and AI key live in a district-owned Supabase backend. No personal accounts, no student data exposed.
- **Why this combination:** it keeps the strict no-PII posture, makes the tool genuinely the student's to keep after they leave the college, and gives OIT the simplest possible data story to approve.

The alternative, district Google sign-in, is documented at the end for completeness, along with the honest tradeoff.

---

## Goal, Audience, Process

**Goal.** Give each student a private, persistent career workspace they can return to on any machine, that stores no personal identity, and that remains theirs after graduation, while the instructor grades only the finished work submitted to Canvas.

**Audience.** AVC248 students, 24 to 44, working on a mix of personal and shared lab machines.

**Process.** A student signs in with an anonymous handle. Their saved work loads from a server, they keep working, and every change saves back. When they need AI help, the same backend holds the Gemini key and makes the call. When they finish a deliverable, they export it and submit it to Canvas, where the grade attaches to their real Canvas identity. The instructor never needs to enter the tool.

---

## The identity decision

### Recommended: anonymous handle sign-in

**How it works.** The student signs in with a handle and a PIN, for example "bluefox42," chosen or assigned, never their name or email. Their work is stored in a small database keyed to that handle. The resume content itself is already stripped of direct identifiers.

**Privacy posture.** Genuinely no personally identifiable information. The system stores "bluefox42's project" and cannot connect that handle to a real person. This fully honors Render's original promise and gives OIT a clean, short data-handling review: no identity is collected, so there is no identity to govern.

**Why it is the right call for this course, three reasons:**

1. **Grading does not require it.** Because students submit their finished deliverables to Canvas, the grade lives on the Canvas submission, not in Render. The tool never needs to know who anyone is, and the instructor never needs a name-to-handle crosswalk.
2. **It makes the tool outlast the semester.** This is the point of Render. An anonymous handle is not tied to the college, so the student keeps the tool and everything in it after they graduate or leave. A district-account login would be deprovisioned when they leave, taking their workspace with it, which defeats the entire purpose.
3. **Its one weakness is low-stakes here.** The usual downside of anonymity is that a forgotten handle cannot be recovered. But since grades live in Canvas, a lost handle costs a student only their personal workspace, not a grade. They start a fresh handle and continue. The risk that normally argues against anonymity is largely removed by this design.

**What gets built.** A Supabase project (database plus handle login), a sign-up and login screen in Render, and the Gemini key held in a Supabase edge function so it never reaches a student device.

---

## Where Render lives (hosting)

Render now has two parts, and they live in two places. This is normal for a tool with a login.

**The interface (the page): district GitHub Pages.** Render is a static site, so GitHub Pages hosts it well. It should live on a district-owned GitHub organization, not a personal account, so that district student traffic sits under district control and separate from any personal portfolio. If a district GitHub organization is not available, the fallback is a clean, separate project account, still not mixed in with personal work. The page holds no secrets, so public static hosting is appropriate and free.

**The backend (login, saved work, AI key): Supabase.** GitHub Pages only serves static files. It cannot run a database or hold a secret, so the login, the stored student work, and the Gemini key live in a Supabase backend, which can be owned by a district or department account. This is the only place any data or credential sits, and it is designed to hold no student identity.

**On district server space.** A dedicated district server is not needed for the pilot. GitHub Pages plus Supabase covers hosting, storage, login, and the AI key. District-hosted server space remains a later option if the district ever wants to self-host the backend instead of using Supabase, at which point the move is a migration, not a rebuild.

---

## What this means for the OIT request

This design produces the cleanest data-handling story available:

- No student identity is stored anywhere in the tool.
- No personal data is sent to the AI, which runs on the paid, protected Gemini tier that does not train on inputs.
- The only stored data is anonymous, keyed to a handle, on a district-owned backend.
- Grading happens entirely in Canvas, under the student's existing, already-governed Canvas identity.

There is, in short, no new pool of student data to protect, which is the shortest path to a yes.

---

## Alternative, for completeness: district Google sign-in

**How it works.** The student signs in with their Maricopa Google account. Work saves under their Google identity in a district-governed store, most directly a Google Sheet or Drive files written by Apps Script, which can also hold the Gemini key.

**Privacy posture.** Identified but protected. The system knows exactly who each student is. Everything sits inside the Maricopa Google tenant, covered by the district agreement, and the paid Gemini tier does not train on it. This is a legitimate posture, but it is not no-PII, and it should not be described as such.

**Why it is not the recommendation.** It is the smoothest login experience, and for a course that needed to see named progress inside the tool it would be the simpler choice. But this course does not need that, grading runs through Canvas, and the district login carries a real cost: when a student leaves the college, the account is deprovisioned and the student loses Render and everything in it. That directly undercuts the goal of a tool that outlasts the semester.

---

## Side by side

| | Recommended: Anonymous handle | Alternative: District Google |
|---|---|---|
| Login | Made-up handle plus PIN | Maricopa Google account |
| Identity held | None | The student is known |
| Privacy label | Truly no-PII | Identified but protected |
| Grading | Canvas submissions only | Canvas submissions only |
| Outlasts the semester | Yes, not tied to the college | No, lost when the account is deprovisioned |
| Lost access | Not recoverable, but low-stakes here | Easy, the account persists while enrolled |
| Backend | Supabase (district-owned) | Apps Script plus a Sheet |
| Where the AI key lives | Supabase edge function | Apps Script |
| Frontend hosting | District GitHub Pages | District GitHub Pages |

Both store work safely on a server, keep the Gemini key off student devices, and work on shared lab machines. Browser-only storage is not an option, since a cleared cache would lose a student's work.
