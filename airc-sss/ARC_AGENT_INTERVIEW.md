# ARC newsletter interview: agents

Prep for the district AI Resource Center interview on how I use agents.

**Goal:** teach faculty and staff across ten colleges what an agent actually is, using
work they can look at, so the ones who are curious have somewhere to start.
**Audience:** Maricopa faculty and staff who have used a chatbot and have not built
anything. Most have never heard "agent" used precisely. A few build.
**Process:** teach the ladder (prompt, skill, agent, orchestrator), show one real
example at each rung, and land on the two lessons that are actually mine: the craft
is in the constraint, and deciding where the automation stops is the design decision.

---

## The one-sentence answer

A skill is a single focused job: something in, a useful result out, one step.
An agent is a role: it is given a persona and constraints, it takes several steps on
its own, and it decides what to do next. An orchestrator is an agent whose job is
running other agents.

That definition is already published on the Render skills tab, so it stays consistent.

---

## The ladder (teach this, it is the whole talk)

Most faculty are on rung one and do not know there are four.

| Rung | What it is | My example |
|---|---|---|
| 1. Prompt | You ask, it answers, one turn. Nothing is saved. | What everyone is already doing |
| 2. Skill | A saved, reusable prompt that does one job well. Same job, new input, every time. | Resume tailoring in Render; my page-builder and PRD skills |
| 3. Agent | A role with constraints that takes multiple steps on its own, uses tools, and decides the next move. | A synthetic student browsing a college website |
| 4. Orchestrator | An agent that runs other agents and sequences the work. | The one agent conducting the other fifty |

The jump that matters is rung two to rung three. A skill waits for you. An agent goes.

---

## The inventory

### Agents

**The student-journey study. Fifty persona agents and one orchestrator.**
The flagship, and the thing to lead with. Each of fifty personas is its own agent, a
whole student rather than a trait or a lens. Each agent browses the live college
website itself with no special access and no login, because a prospective student has
neither. It narrates in the first person so the reasoning is visible. It returns a
structured finding: outcome, path taken, where it broke, a quote, a candidate
severity, device notes, every one traceable to a page. The orchestrator sequences the
journey and routes the runs.
Status: agents and orchestrator built, Part 1 underway. Ten colleges, roughly 140,000
students.

**Render. Four agents on top of about nineteen skills.**
The teaching case, because students build and keep them. Career counselor (knows the
whole picture, names the single next move), job search agent (built from the student's
own goals, verifies every posting is still live on the employer's site), hiring
committee (four reviewers score separately, hand back a ranked fix list), interview
panel (the same four interview the student and coach every answer). At the end of the
course every agent and skill is exported as a labeled prompt file with a plain-English
readme, so the student pastes them into their own Claude, Gemini, or ChatGPT and keeps
using them. The interface does not have to survive; the agents do.
Status: usability tested, pilot Fall 2026.

**The DMA jobs agent.** Runs daily on its own. Dedupes against everything already
posted, searches broadly, hard-filters by an experience cap so nothing out of reach
gets through, posts to the student Discord as its own bot. This is the cleanest
example of "works on its own over time" and the easiest for staff to picture.
Status: live, running daily.

**Dial Your Course, library refresh.** A build-time agent that pulls new scholarship
from open indexes (OpenAlex, ERIC) for human vetting, then updates the grounded corpus
the tool ships with. Good illustration that an agent can maintain a resource rather
than answer a question.
Status: built.

**Synthetic-user usability agents.** The same persona method turned on my own builds,
so an assessment gets walked through by agents before a learner ever sees it.

### Skills

Seven working skills behind the portfolio and courses: assessment-library-refresh,
build-a-course, page-builder, prd, research-first, resume-and-cover-letter,
website-style-guide. Plus roughly nineteen student-facing skills in Render (resume
tailoring, cover letter, match check, skills-gap, learning resources, training plan,
portfolio ideas and review, elevator pitch, LinkedIn, networking messages, interview
questions and feedback, thank-you notes, salary research, weekly schedule, freelance
strategy and contract coach, search diagnosis).

Worth saying out loud: most of what looks like AI work is skills, not agents. That is
not a lesser thing. Skills are where almost everyone should start.

### Not agents, do not call them agents

CopaMigo is a routing model over verified content, not an agent army. It is a good
tool and the honest description is better than an inflated one, especially in a room
where someone will check.

---

## The two points that are actually mine

Everything above is inventory. These are the ideas, and they are what makes it worth
interviewing me rather than reading a vendor page.

**1. The craft is in the constraint.**
The instinct is that the hard part is making the AI capable. It is the opposite. An AI
is too capable by default: it breezes through a form a real student abandons, because
it reads faster, knows more vocabulary, and never gets discouraged. Every persona
agent is held down to what that student would plausibly know, with that student's
device, patience, and reading speed. Take the constraint away and the study returns
the average student, and the average student is exactly the one who never has trouble.
The limiting is the design work.

**2. Deciding where the automation stops is the design decision, not the model choice.**
Severity rating stays human. The research is clear that models are least reliable
exactly there, so every finding is a candidate until a person confirms it. The agent
finds; it does not decide. For this audience that is also the governance answer: the
whole system collects no student data and no PII, which is the same line the district
already drew when it declined a vendor AI add-on over data collection.

---

## Likely questions

**"Do I need to code to do this?"** No. Every agent above is written in plain English:
who you are, what you know, what you may not do, what to hand back. That is the actual
skill, and it is a writing skill. Faculty already write rubrics and assignment
constraints, which is the same muscle.

**"How is this different from just using ChatGPT?"** ChatGPT waits for you. An agent
has a standing job, constraints, and somewhere to put the result. The DMA jobs agent is
the easiest picture: nobody opens it, it just posts jobs every morning.

**"Isn't this replacing staff?"** No, and I would not build it if it were. The study
exists to take routine repetitive work off advisors, the easy factual questions and the
"we will get back to you in a few days" booking email, so their time goes to the
individual problems and the human connection. The domain members are advisors and
financial-aid staff. The study is built to make their jobs easier, and they helped
shape it.

**"Where do I start?"** Write one skill, not an agent. Take a thing you do every week,
write down exactly how you do it including what good looks like, and save it. Use it
five times and fix it each time. That is a skill, and it is most of the value.

---

## Guardrails for this interview

- **ARC is the AI Resource Center, a center, not a committee.** I co-chair the Student
  Support and Success domain, Domain 5. I do not lead the ARC.
- **Refer to people by title, never by name**, in anything published.
- **Nothing is in production.** Render is in pilot, CopaMigo is a prototype in testing,
  the study is underway. Early adopter, not finished. Say so plainly; being the person
  doing it first is the story, and inflating it is the only way to lose the room.
- **Do not mention my own job search.** The family agents stay out too; if the pattern
  is useful, describe it generically as scheduled agents that publish to a page.
- **Ask to review the writeup before it runs**, specifically for the Domain 5 wording
  and anything that implies production.

---

## After it runs

Ask permission to link it, then link it rather than reproducing the text. Add a short
recognition section to the site, which does not exist yet. A district publication
saying the agent work is worth interviewing is the first thing on the portfolio that
someone other than me vouched for.
