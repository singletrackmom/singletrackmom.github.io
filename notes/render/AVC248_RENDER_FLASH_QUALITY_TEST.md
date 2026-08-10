# Gemini Flash quality test for Render (10-minute check)

**Purpose:** confirm Google Gemini Flash gives good enough resume coaching and fit-report feedback before proposing it to OIT and the department chair. If Flash passes, both request documents (`AVC248_RENDER_OIT_PILOT_REQUEST.md` and `AVC248_RENDER_CHAIR_FUNDING_REQUEST.md`) are ready to send.

**You are not paying.** Google AI Studio is free to test, no card. The free tier can learn from what you type, so use the fake resume below, never a real student's.

**Which model:** at the top of AI Studio there is a model dropdown that shows the exact model name. Pick the newest plain **Flash** (not Flash-Lite, not Pro). Whatever name sits in that box is the model you are testing.

---

## Steps

1. Go to aistudio.google.com and sign in with a personal Google account.
2. Click through any terms prompt. You land on a chat-style screen.
3. Open the model dropdown (top of the screen) and choose Gemini Flash.
4. Find the "System instructions" field and paste the System Instructions block below.
5. Paste the Sample Input block into the main chat box.
6. Press Run. Read the result against the quality bar at the bottom.

---

## System instructions (paste into the System instructions field)

```
You are a career coach for entry-level community college students. A student will give you their resume and a job posting. Write a "Should I Apply?" fit report that is honest but encouraging. Never tell them they won't get in. Ground everything only in the job posting given, do not invent requirements. Structure it as: (1) a fit band, one of Reach, Possible, or Strong, no percentage; (2) a short list of the posting's key requirements, each marked met, partly met, or not yet, with one line of evidence from their resume; (3) a clear call: apply, apply with tweaks, or stretch and learn; (4) three concrete ways to make the application stronger; (5) if it's a reach, two or three job types better matched to them right now. Keep the tone warm and mentoring, like a coach who believes in them.
```

---

## Sample input (paste into the main chat box)

```
MY RESUME
Objective: Looking for an entry-level design or social media job.
Experience:
- Sales Associate, local clothing store, 2 years. Helped customers, ran the register, built the store's Instagram posts and grew followers.
- Barista, campus coffee shop, 1 year. Made drinks, trained two new hires.
Education: Working on an Associate of Applied Science in Digital Media Arts, Glendale Community College, expected 2027. Courses in graphic design, typography, and digital imaging.
Skills: Adobe Photoshop and Illustrator (class level), Instagram, Canva, teamwork, dependable.

THE JOB POSTING
Junior Social Media Coordinator. We need someone to plan and design posts for Instagram and TikTok, keep a content calendar, and use Adobe Creative Suite or Canva to make graphics. Requirements: 1+ year creating social content, basic graphic design skills, strong communication, ability to meet deadlines. Nice to have: experience growing a following, and short-form video editing.
```

---

## The quality bar (what a pass looks like)

It should read like a real coach, not a generic checklist. A pass:

- Notices the real strengths (the Instagram-growth experience, the design coursework, Adobe and Canva skills).
- Flags the honest gap (no short-form video editing yet).
- Lands on a sensible band (this example should read Possible or Strong).
- Gives three specific, doable ways to strengthen the application.
- Stays warm and hopeful, never harsh, never "you won't get in."

If it does that, Flash passes and the pilot can run on Flash. If it feels thin, shallow, or robotic, the next tier up (Gemini Pro) is the fallback, at higher cost. Note which it was and we adjust the documents if needed.
