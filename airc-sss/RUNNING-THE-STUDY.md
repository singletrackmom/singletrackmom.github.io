# District Barriers Study, How We Are Running It

**Goal:** Map where students hit barriers across all ten Maricopa colleges, one persona and one task at a time, and turn each barrier into a human-in-the-loop AI pilot. Give every volunteer a fifteen-minute, one-click job with zero prep.

**Audience:** Michelle (co-chair), the Student Support and Success domain members who volunteer as testers, and anyone she hands the tool to.

**Process:** One tester, one college, one task. The tester opens a single web page, is handed a student persona and one thing that student needs, works it on the real college website from that student&rsquo;s point of view, and logs what broke. No login, no prep, no hunting through documents.

---

## The one link testers use

**https://singletrackmom.github.io/airc-sss/run.html**

That page does everything:
- Tester picks their college once (their login only reaches one college&rsquo;s systems, so they only get that campus&rsquo;s tasks).
- It auto-assigns one scenario: who you are, what&rsquo;s true for you, and the one thing you are trying to do.
- It gives the fifteen-minute rules.
- &ldquo;Log your result&rdquo; opens the Google form. &ldquo;Give me a different one&rdquo; hands them another.

No accounts, no app, no data collected on the page itself. Runs are recorded against a Scenario ID and initials only, never a student record.

## The exact message to send every team member

Copy and paste this, fill in the name:

> Subject: 15 minutes to help the barriers study
>
> Hi [name],
>
> Here is your part of the Student Support and Success barriers study. About fifteen minutes, one sitting, no prep.
>
> 1. Open this link: https://singletrackmom.github.io/airc-sss/run.html
> 2. Pick your college, the one whose systems you can actually log into.
> 3. You will get one student (a persona) and one task. Become that student and try to do the task on our real college website, out loud, without looking up where to go. A real student is not told where to go either.
> 4. The moment you hit a wall, a dead end, a confusing name, a form that will not submit, that is the finding. Note it.
> 5. Stop at fifteen minutes even if you did not finish. Not finishing is a real result.
> 6. Click &ldquo;Log your result&rdquo; and fill in the short form. Done.
>
> Want to do another? Click &ldquo;Give me a different one.&rdquo; Every run helps us map where students get stuck. Thank you.

## Where results go

The &ldquo;Log your result&rdquo; button opens a **Google Form**, and every response lands in a Google Sheet Michelle owns. The form fields: Scenario ID, initials, campus, did you complete it, what happened / the barrier, severity (Nielsen 0 to 4), time taken, and any suggested fix.

**Separate by college:** every response carries the Campus field, so in the linked Sheet you filter or pivot by campus to see each college on its own. The tool also only ever hands a tester scenarios for the campus they chose, so coverage is tracked per college from both ends.

## Status and the one open task

- **The tester page is built and live-ready** at `airc-sss/run.html`, 169 runnable scenarios across all ten colleges, 36 personas.
- **OPEN: the Google Form.** Michelle creates it once (forms.new, add the fields above, Send &rarr; link &rarr; copy), sends the link to Claude, and Claude pastes it into the `LOG_FORM_URL` line near the bottom of `run.html`. Until then the Log button says &ldquo;link pending.&rdquo;
- **Optional next:** pre-fill the form with the Scenario ID, persona, and campus so testers only log the result. Needs one &ldquo;Get pre-filled link&rdquo; sample from the created form.

## Guardrails (unchanged)

**Translate, do not standardize. The service names are not the defect.**
Every college names its own services, and those names are campus identity. GCC Cares, Bear Necessities, Patio Pick-Up, Coyote Cupboard, Gecko Grocery, Mesa Market, Artie&rsquo;s FIT Market, Puma Pantry, The Village: each is that college&rsquo;s own, students who know them use them, and **no college is ever asked to rename anything.** A recommendation that requires a rename or a site rebuild is out of scope and gets marked as such.

**State every barrier as what happens to the student.** The defect is that a stated need does not reach the service that would meet it. The service exists. The search does not find it. If a finding reads as *&ldquo;these colleges call it different things,&rdquo;* it is not finished, it is an inventory observation. Write the student into it or do not log it.

**Problems, not destinations.** A tester is never told where to go. They start from the felt need and have to find it.

**No student data, ever.** Initials and a Scenario ID only. No PII enters any system at any point.

**Severity is tester-assigned and pending human rating.** Never promote a candidate severity, never average severities into a new number, never quietly drop the word candidate.

**Keep the evidence tiers apart.** `page-opened` is quotable as a claim about content. `search-layer` is quotable as a claim about retrieval only. Four claims collapsed in round 1b from blurring these, and all four had overstated the barrier.

**Credit what works, by name.** A working model inside the district is the cheapest recommendation available, and naming the colleges that solved something protects the relationships the fieldwork depends on.

**Compliance material is not a villain.** When a felt-need query returns a Clery report, the failure is retrieval, not authorship. Say so.

**Never put an assistant between a student and a crisis.** For safety, crisis and mental-health paths the only acceptable AI role is routing to a human, a service page, or a published number. It does not counsel, screen, or triage.


**Human contact is the metric.** Nothing is presented as a completed run until a real run exists.
