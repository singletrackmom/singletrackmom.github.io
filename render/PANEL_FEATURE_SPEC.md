# Render: the Hiring Panel feature

**Goal:** after a student has a resume, a cover letter, and a dialed portfolio, Render assembles a simulated hiring panel for the exact job they are applying to, scores their application against that panel's rubric, and tells them in plain language what to change before they will get an interview.

**Audience:** a student who has never had a professional job and does not know what a hiring panel is. Assume zero prior knowledge. Nothing is obvious to them.

**Process:** build five TABS inside Render's panel section. Not pages, not one long scroll. Michelle demos this by clicking tab to tab, saying "here is what we are looking at," then clicking the next one. Each tab must be clear standing alone, with nobody narrating it.

**Status:** specified, not built. The PRD already references a panel (13 mentions) and the tool has an `INTERVIEW PREP PANEL` function, but the scored report does not exist.

---

## The real reason this feature exists

The feedback is the surface. The point underneath is that **the student is operating an agent panel, and that is the training wheels for building their own.**

By the time they finish, they have seen a panel assembled from a job posting, watched four agents with different lenses score the same thing, seen the scores reconciled, and watched a plan come out the other side. That is the pattern for every multi-agent system they will ever build. They learn it by using one that matters to them, not by reading about orchestration.

**Say this out loud on the last tab.** Do not leave it implicit. A student who finishes should be able to answer "what is an agent panel and why would you build one," because they just used one on their own resume.

---

## Tab rules, non-negotiable

- **Five tabs.** One idea per tab.
- **Each tab fits on one screen** at demo resolution. If it scrolls, it is too long.
- **Each tab is self-explaining.** A stranger clicking through with no narration should understand it. Michelle should be able to stop talking and it still lands.
- **Concise output.** A number, a short table, a few sentences. Not paragraphs of analysis.
- **The tab labels are plain English**, not jargon. "Meet your panel," not "Evaluation configuration."

---

## The model to copy

Michelle ran this on her own EAB application on 16 Aug 2026 and it worked. Four independent reviewers, each with a different lens, each scoring the same rubric without seeing each other's scores, then a synthesis. It produced a number (40%), a routing decision (Analyst not Senior), and a ranked change list. The reusable version is saved at `~/Documents/Claude/JobSearch/_AGENTS/eab-hiring-panel.md`. **Read that file before building.** It is the working prototype of this feature.

---

## TAB 1: Meet your panel

Written for someone who has never interviewed. Explain the concept before the content.

- **What a hiring panel is.** Plain language. "When you apply, your application does not go to one person. It goes to a few people who each care about something different. They score you, then decide together whether to spend an hour talking to you. Most applications never get that hour."
- **Who is on YOUR panel**, generated from the actual job description. Typically four:
  - the **hiring manager** who owns the job and will be your boss
  - a **senior person in your craft** who judges whether your work is good enough
  - a **recruiter** who checks boxes fast and rejects most applications in seconds
  - a **teammate or customer-facing person** who judges whether you would be useful to them
- For each: their job title, what they personally care about, what makes them say no, and one line on what they will look at first.
- **The rubric they score against**, pulled from the job posting's own requirements, weighted. Show the weights.
- **What the scores mean.** 5 exceptional, 4 advance, 3 only if the pool is thin, 2 decline, 1 disqualifying.

## TAB 2: Your score

- **Composite number** and what it predicts, stated plainly. "This means you probably will not get a call yet, and here is why."
- **Score per criterion**, with the reviewer's actual reasoning quoted.
- **Three things that are working.** Quote the student's own words back to them so they know what to protect.
- **Three to five gaps**, each quoting the exact text that caused it. Never a vague impression.
- **The single highest-leverage change**, named as one action.

## TAB 3: Your fix list

Ranked highest leverage first. Three columns:

| What to change | Where | Why it matters |

Grouped into **Resume**, **Cover letter**, and **Portfolio**. Every item is a specific action, not advice. "Add the words UX and visual design to your skills section" beats "strengthen your skills section."

Also include a short **do not change** list, so a nervous student does not rewrite something that is already working.

## TAB 4: Interview practice

Only unlocks after the fix list is addressed, so a student does not practice for an interview they will not get.

- **Question bank generated from the job description**, not generic. Sorted: likely, possible, and the hard one they are hoping you do not ask.
- **At least 10 practice questions with a real spoken voice.**
- After each answer, feedback on structure (did they give a situation, a task, an action, a result) rather than on personality.

## TAB 5: You just built an agent panel

The payoff tab, and the one that makes this a teaching tool instead of a feedback tool.

- **Name what just happened**, in plain language. "Four different reviewers looked at your application. Each one cared about something different. They scored the same rubric separately, then their scores were combined. That is called an agent panel, and you just ran one."
- **Show the pattern as a simple diagram:** a job posting goes in, roles get assigned, each agent scores independently, results reconcile, a plan comes out.
- **Why independence matters.** If the agents talk first, they agree too easily and you learn nothing. Separate scores surface real disagreement.
- **Where else this works.** Critiquing a portfolio piece, checking a client proposal, reviewing a design against accessibility rules. Same shape, different lens.
- **One next step:** the student writes the four roles they would use for a panel on something they care about. Not code. Just who is in the room and what each one is looking for. That is the whole skill.

---

## The ElevenLabs constraint, read this before building the voice

Michelle has an ElevenLabs subscription. There is a real architectural conflict to solve first.

**Render is client-side with no backend and no login, and stores no student PII.** That is a deliberate, load-bearing decision tied to the data-sovereignty line. An ElevenLabs API key cannot be embedded in a client-side page, because anyone can view source and steal it, and the bill is Michelle's.

Three options, in order of preference:

1. **Pre-generate the audio.** Render the 10 practice questions to MP3 once with ElevenLabs, commit the files, and play them back. No key in the browser, no per-use cost, works offline. **Loses:** questions cannot be tailored per job. Fix by pre-generating a bank of common questions per job family and using option 3 for the tailored ones.
2. **Browser speech synthesis** (`window.speechSynthesis`). Free, no key, works everywhere, tailored to any question. **Loses:** the voice is robotic. Acceptable for a v1 and better than nothing.
3. **A proxy the district hosts** that holds the key server-side. Correct long-term, but it is a backend, which is the thing Render deliberately does not have. Only worth it if the district sponsors the tool.

**Recommendation: ship option 2 now, add option 1 for the top questions.** Do not put the key in the page under any circumstance.

---

## Sample pages to build

Michelle asked for a worked example so students see what good looks like. Build a fake but realistic student:

- a Digital Media Arts student applying to a real, plausible junior design job
- their actual job description
- their actual cover letter, with realistic first-attempt weaknesses
- their actual resume, same
- then all four output pages above, fully written, scoring that application honestly

**The sample must show a student who does NOT pass on the first try.** Every tab of the sample must be demo-ready, because this is what Michelle clicks through when showing the tool.

**The sample must show a student who does NOT pass on the first try.** A sample where the fake student aces it teaches nothing and sets a false expectation. Show a 2.8, show the gaps, show the fix list, then optionally show the same application after the fixes.

---

## What to add to the PRD

The PRD references a panel but not the scored report. Add to section 7:

- the five-tab output structure and the rule that each tab is self-explaining
- the panel-composition logic (roles derived from the job posting)
- the rubric-weighting logic (criteria pulled from the posting's own requirements)
- the gate: interview practice unlocks after the fix list
- the voice architecture decision and why the key never touches the client
