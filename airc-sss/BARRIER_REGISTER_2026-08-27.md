# Barrier register, 27 August 2026

The aggregated result of the whole study to date. Everything logged in Part 1 and Part 2, merged into one ranked list, each barrier tied to whether AI can close it.

**Goal.** Give the Student Support and Success domain one ranked, decision-ready list of where students get lost, and say for each one whether AI can close it, so the domain brings forward only what it can actually deliver.

**Audience.** The ARC committee and the Domain 5 working group. People who run colleges and student-services offices, who did not read the run logs, and who will be asked to fund or staff what this recommends.

**Process.** Read every logged run across both parts, normalize each finding into one register row, collapse repeats, rank by candidate severity, then type each barrier by the domain's three AI routes or mark it not-AI-addressable and hand it off.

---

## How to read this

**Severity is the Nielsen 0 to 4 scale, assigned by the tester, pending human rating.** Nothing here is a confirmed district finding. Where a severity was revised, the register carries the revision, including the four revised **downward**.

**Two evidence tiers, kept apart.** `page-opened` means the tester opened the page in a browser and read it, and is quotable as a claim about content. `search-layer` means the tester recorded what a query returned, and is quotable as a claim about retrieval only. The two are not equal, and the study's four retractions all came from treating a search summary as page content.

**Repeats collapse.** A barrier found at nine colleges is one row with an instance count, not nine rows.

**Counts:** 5 at candidate 4, 17 at candidate 3, 12 at candidate 2 and below. These match the committee deck built from this file.

**Sources:** `PART1_FINDINGS_2026-07-27.md` (Layer 0 sweep, 11 persona runs, 3 end-to-end funnel walks) and `PART2_RUNS_2026-08-25.md` (13 page-opened runs, two search-layer batches, three ten-college comparisons, two completed crosswalk rows). All ten colleges touched. Public web only, no login, no student data, no contact with staff.

**AI route** uses the domain's own three, from `agents/README.md`: **build a tool**, **plug into a system already in use**, **department workflow or agent**, or **not AI-addressable** and routed to the owning office.

---

## The central finding, which sits above the register

**Retrieval matches vocabulary, not need.** Pages that contain the student's word rank on the student's query. Pages that contain only the service's name do not.

Three tasks were run at the same colleges with two phrasings each, the student's own words and the service's own words.

| Task, felt-need phrasing | Colleges where it works |
| --- | --- |
| “I ran out of food, I am hungry, need help eating” | **1 of 10.** Four return nothing. Two return a student literary magazine. |
| “I cannot pay my rent this month, I need money now” | **2 of 10.** Four return nothing. |
| “I have ADHD, what help can I get in class” | **2 of 10** name the condition in student-facing service content. |

The three successes explain the rule. Scottsdale's pantry ranks because its page says *“our hungry students.”* Chandler-Gilbert's ranks because the page says *“CGCC's food pantry is called the Coyote Cupboard.”* Estrella Mountain's disability content ranks because they publish a page titled **ADD/ADHD**. Each contains a word the student would actually type. That is the only thing they have in common.

Estrella Mountain's **Mariposa Literary Review** surfaced as a top result for three separate crisis queries: unsafe, hungry, and cannot pay rent. It ranks because it is the only place on that domain where anyone writes about being broke, frightened, and hungry in the first person. The services exist. The language of need exists. They are in different documents.

---

## Candidate severity 4

### 4.1 A student in an unsafe moment gets a compliance document

- **What happens.** She searches “something happened, I do not feel safe, report a concern, help.” Seven of nine colleges fail to return a service.
- **Evidence.** Works at **Mesa** (Reporting Concerns, with 911, College Police, EMPACT Crisis Line, 988, and a Victim Services number) and **South Mountain** (Office of Care and Conduct, with a plain FAQ answering *“Is my report confidential?”* and *“Can I submit a report for myself?”*, page-opened). Partial at **GateWay** and **Rio Salado**, where a Behavioral Intervention Team page exists but is framed as reporting someone else's concerning behavior. Poor at **Phoenix**, **Scottsdale** (four chemistry syllabus PDFs), **Glendale** (crime statistics, Annual Security Report, a 474-page PDF). Fails at **Chandler-Gilbert** and **Estrella Mountain** (a 110-page PDF, a catalog update, a senior-citizens class flyer, a literary magazine). Separately at **Paradise Valley**: two results, the Annual Security Report PDF and Alumni Success Stories.
- **Verification.** Search-layer, with the two working models page-opened.
- **AI route.** Plug into a system already in use. Route the felt-need phrasing to the service page and the published number on the chat surface every college site already carries.
- **Hard constraint.** An assistant never counsels, screens, or triages a student in crisis. It routes to a human, a service page, or a published number, immediately and every time. If that cannot be guaranteed, do not deploy on this path.
- **Handle with care.** Clery reports are legally required and the offices publishing them are doing their job. The failure is retrieval, not authorship, and saying so protects the relationships the fieldwork needs.

### 4.2 MEID is the silent gatekeeper of the whole journey

- **What happens.** Three personas walked the full enrollment funnel at three colleges. All three completed stages 1 through 7 on the public site and were stopped at the same place, Register for Classes, where the Student Center demands an MEID, a password, and Duo. No one enrolled.
- **Evidence.** Identical wall at **Glendale**, **Scottsdale**, and **Mesa**. Severity 4 at Glendale and Mesa, 2 at Scottsdale. The MEID is not created at the wall; it is created at stage 3 inside the admissions wizard, disguised as the yes-or-no question *“Do you have a Maricopa email / Student ID?”* A student meets MEID as an unexplained demand at stages 2, 3, 5, and 8. One enrollment attempt crosses gccaz.edu, maricopa.edu, admissions.maricopa.edu, and sso.maricopa.edu.
- **Verification.** Page-opened, three end-to-end walks.
- **AI route.** Build a tool, then plug it in. One plain answer served wherever the question is asked: “You get an MEID when you apply. It is your student ID and password for everything after this.” Stable, district-wide, and currently written nowhere the student is.
- **Scope honesty.** The login wall itself is not ours to move and should not be. What is ours is that the identifier the whole journey depends on is never explained.

### 4.3 Four gates stop a refugee student from applying

- **What happens.** A 22-year-old with a refugee background, English as a third language, and a relative interpreting the form is blocked at four points on a page that is otherwise warm and well written, and that states cost up front at $97 per credit hour.
- **Evidence, all page-opened at Estrella Mountain.** Identification: *“The application will not be processed until the ID is uploaded,”* no alternative path named. Prior transcripts: hand-delivered, emailed, and unofficial all refused, no alternative for foreign or unobtainable records. A 48-hour application expiry, and he needs a relative to interpret the form. All new students default to out-of-state tuition until documents are submitted, so the documentation gate is wired to the price. The page is offered in English and Spanish only, nothing in Arabic or Somali.
- **AI route.** **Mostly not AI-addressable.** The gates are policy and belong to Admissions and district IT. Routed there, not carried forward as a domain recommendation.
- **What is answerable.** Three questions with answers that exist somewhere in the district and are not on the page: whether an alternative documentation path exists, what to do when prior transcripts cannot be obtained, and a warning about the 48-hour expiry before a student starts.

### 4.4 The adult-education bridge is invisible

- **What happens.** A student who finished a GED and wants to start credit classes cannot find the path.
- **Evidence.** **South Mountain**: zero results, no Adult Education, GED, or ESL content indexed on the domain at all (severity 4). **Phoenix**: the GED-to-credit pathway exists and is announced in a **2021 news post** describing a partnership with Rio Salado, with no equivalent service page found (severity 3). A Spanish-language search for the same need at Phoenix returned no Spanish page.
- **Verification.** Search-layer, with the Phoenix news item page-opened.
- **AI route.** Plug into a system already in use. Surface the bridge as an answerable question rather than an archived announcement.
- **Split.** Moving the content to a service page belongs to each college's web team. Answering over it where it currently lives is what the domain can do now.

### 4.5 Disability services never name the condition, for the students least able to persist

- **What happens.** Five of six colleges have solid disability-services pages that never name the conditions students actually have. A student who knows “DRS” and “accommodations” finds the service everywhere. A student who only knows they have ADHD finds it at one college.
- **Evidence.** **Estrella Mountain** is best in district: a dedicated ADD/ADHD page plus Learning Disabilities, Assistive Technology, Disability 101, The Law, separate Current and Future Student paths, and an FAQ. **Paradise Valley** is strong on process, repeating *“complete our New Student Application”* identically across five pages. **Mesa** names ADHD only on the faculty referral page. **Chandler-Gilbert** names it only when listing external psychiatric providers. **Scottsdale** names it only in alumni success stories. **Glendale** fails: a library ebook guide written for paediatricians and psychiatrists.
- **Persona exposure, the largest in the study.** 22 of 50 personas carry a disability or neurodivergence. **15 of those are suspected, undiagnosed, or undisclosed**, meaning they do not know they would qualify and would never search the word “accommodations.”
- **Candidate severity.** 3, **rising to 4** for the undisclosed group.
- **AI route.** Build a tool, then plug it in. A condition-name to service mapping. Estrella Mountain has already proved the approach works.

---

## Candidate severity 3

| # | Barrier | Evidence and colleges | Tier | AI route |
| --- | --- | --- | --- | --- |
| 3.1 | The felt-need phrasing does not reach the page the jargon term reaches | **Glendale.** “What is my MEID and how do I get one” returns the MEID page first. “I applied, now how do I log in the first time, get my username” returns New Student Enrollment, Wireless Networks, HESI Testing, and Job Openings. Same page, same need, opposite results, on the district's most load-bearing credential. | search-layer | Build, then plug in |
| 3.2 | Disability content never names conditions | 8 of 10 colleges on the retrieval sweep. Where ADHD does appear: faculty referral pages, teacher-training syllabi, clinical ebooks, external provider lists, alumni marketing, news items. All written *about* these students, not *to* them. | search-layer | Build, then plug in |
| 3.3 | Spanish-language discovery fails independently of whether Spanish content exists | Four felt-need searches at two colleges reached nothing: Phoenix (GED bridge, apply as new student) and **GateWay, which runs a full Spanish hub explicitly covering food and housing insecurity**. Content exists, in Spanish, on the same site, and discovery fails anyway. | search-layer | Plug into a system already in use |
| 3.4 | Same function, unrecognizable local names | Food and basic needs across the district: GCC Cares, Bear Necessities, Patio Pick-Up, Coyote Cupboard, Gecko Grocery, Mesa Market, Artie's FIT Market, Puma Pantry, The Village. A student who knows the words “food pantry” will not search these. | page-opened + search-layer | Build, then plug in |
| 3.5 | An emergency fund is catalogued and reached as a fundraising asset | **South Mountain**, page-opened. Promises *“up to $500 within 48 hours”* in large type, states *“The Application Cycle is currently closed”* below the eligibility list, and excludes rent, which is the persona's actual need. Breadcrumb: Home / About / Foundation and Development. Of ten pages carrying the fund's name, most are Donations, Annual Reception, Giving to SMCC. Two sponsored private-loan results ran alongside. | page-opened | Plug in. Strongest single AI case in the set |
| 3.6 | Status at time of asking is not surfaced | Three funds, two colleges. South Mountain's emergency fund, Scottsdale's Maricopa Scholarships (*“now closed”*), and the scholarship portal. The most repeatable instance in the study. | page-opened | Plug in, needs a status feed |
| 3.7 | Live student processes documented only in archived news | **Rio Salado** consortium aid: the best explanation in the district sits on a `/news/2021/` page banner-stamped *“This article appears for archival purposes… may no longer be applicable,”* and the swirl decision turns on exactly those facts. **Phoenix** GED bridge, same shape. | page-opened | Plug in |
| 3.8 | A common returning-adult question is unanswerable on the site that answers it | **Mesa.** “Will my old college credits from 20 years ago still count” returns a news story about a 12-year-old, Enrollment Steps, and the Hall of Fame. The answer exists in the Nursing program FAQ: *“Maricopa Community Colleges accept all eligible courses regardless of the age of the course.”* | search-layer, answer page-opened | Plug in |
| 3.9 | The high-school fork makes a 17-year-old self-diagnose | **Chandler-Gilbert** surfaces Concurrent Enrollment, Dual Enrollment, ACE Dual Enrollment, and High School College Advisors. **GateWay** surfaces ACE described as a scholarship, Hoop of Learning, and Dual Enrollment. **ACE is a scholarship at one college and a dual-enrollment variant at another.** 3 of 50 personas. | search-layer | Build, then plug in |
| 3.10 | The only route to a human who helps pick classes is labeled with a word she does not know | **Glendale**, P22 Marisol Reyes, page-opened. *“I see nursing and I see Advisement, but nobody says they go together, and I don't know what advisement means. I don't want to click the wrong thing.”* Gave up. | page-opened | Build, then plug in |
| 3.11 | Cost and residency is the highest-anxiety stage and the most broken | All three funnel walks rated it 3. The residency page timed out and never loaded on two of three. None of the three ever got a plain price on the page meant to give it; the friendly $97 per credit lives on a marketing homepage, disconnected from the legal residency page that says you are out-of-state until you prove otherwise. | page-opened | Plug in, plus a web-team handoff |
| 3.12 | Placement forks into nine-plus exams with no program-to-test map | **GateWay**, P44. EdReady, ACCUPLACER, HESI, CELSA and more, with no “for a health program, here is the one test.” Remote testing offered only for HESI, so an online student is stranded. The `/testing` link timed out twice. | page-opened | Department workflow or agent |
| 3.13 | “Counseling” means two different things and the site does not say which | **Paradise Valley** buries crisis help under Academics, states counselors *“do not conduct therapy,”* and shows 988 as a bare link with no number. **Estrella Mountain** carries the same caveat plus three different crisis numbers. | page-opened | Plug in |
| 3.14 | The aid landing page opens in federal jargon and locks its content in images | **Mesa**, P48. Opens with OBBBA, SAI, proration. FAFSA-year and eligibility content are un-zoomable images on a phone. The “what if aid is not enough” answer (payment plan, Mesa Promise) is fragmented and never linked from the aid flow. | page-opened | Plug in, plus accessibility handoff |
| 3.15 | Tutoring answers are trapped inside course syllabus PDFs | **Scottsdale.** Every result is a syllabus PDF from `directory.scottsdalecc.edu/files/syllabi`. The content inside is good (24/7 Brainfuse, up to 6 free hours per semester, an in-person Math Center) but lives in individual syllabi rather than a service page. **South Mountain** returned nothing. | search-layer | Plug in |
| 3.16 | A publicly indexed staging environment is serving content to students | **Rio Salado.** A swirl-and-residency query returned the 2001-02 catalog and a 2019-20 catalog served from `www-stage.riosalado.edu`. A staging URL also appears in a Chandler-Gilbert international FAQ. | search-layer | **Not AI-addressable.** Route to the web teams |
| 3.17 | The admissions path splits into two routes the site never connects | **Estrella Mountain**, P50. The felt need splits into non-credit ESOL and credit enrollment, with “non-credit” and “CELSA” never explained. The first action link, admissions.maricopa.edu, timed out repeatedly on a phone. | page-opened | Build, then plug in |

---

## Candidate severity 2 and below

| # | Barrier | Where | Severity |
| --- | --- | --- | --- |
| 2.1 | The counseling FAQ answers the fear using the word *private*; the student searches *confidential*. The answer is one accordion click from a student who has decided the site does not address it. Employee-facing counseling pages rank in a student's own results. | Paradise Valley | 2 |
| 2.2 | For-profit and aggregator crowding at the top of the funnel. Maricopa surfaces, but never as a single front door, and always beside University of Phoenix, UTI, West-MEC, Research.com, Monster. A motivated person can miss the cheapest accredited option. | Layer 0, district-wide | 2 |
| 2.3 | No named School Certifying Official on the public site; the certifying function is a faceless office with no remote-submission path for an online-only veteran. “VSO” collides with the veteran's own meaning of the term. | Scottsdale | 2 |
| 2.4 | The service is named Learning Center, Learning Resources, or LRC, not the word “tutoring” that students search. Only the online path has clear steps; the in-person walk-in has no location or map. | South Mountain | 2 |
| 2.5 | International jargon (SEVIS, I-20, I-94) never explained, a step referencing a form with no link, and one FAQ link pointing to a staging URL. | Chandler-Gilbert | 2 |
| 2.6 | Transfer answers are almost entirely catalog PDFs, so a transfer-anxious student gets degree-requirement documents rather than a plan. | Chandler-Gilbert | 2 |
| 2.7 | The disability portal URL says GCCAZ on a PVCC page, which a cautious student reads as the wrong college. Jargon-first ordering: affiliation process, MEID, Section 504 before plain steps. “Testing accommodations” never says “extra time.” | Paradise Valley | 2 |
| 2.8 | The pantry is mascot-branded and sign-up requires an MEID email plus an external GivePulse form. | Scottsdale | 1 |
| 2.9 | Cost, length, location, and aid ineligibility are all stated, but the cost sits in a mid-page icon and the aid ineligibility in a footnote below a two-step lead-capture form. A student can form an impression of affordability before reaching the sentence that matters. | GateWay EMT | **1, revised down from 3** |
| 2.10 | The basic-needs landing page opens with a statistic (59 percent of students experience basic-needs insecurity) before saying how to get food. Hours and locations are one click down. *“GPA requirements vary based on funding”* is vague enough to read as “I probably do not qualify.” | Chandler-Gilbert | 1 |
| 2.11 | The college states ACH refunds at 3 to 5 business days; the district page says 3 to 4. Two levels of the same institution give different numbers. | South Mountain / district | 1 |
| 2.12 | *“Verification documents submitted by email will not be accepted”* sits alone without the accepted method next to it. A stated no with no adjacent instead-do-this. | Mesa | **1, revised down from 2** |

---

## Wins, recorded as first-class rows

Naming the colleges that solved something is the cheapest recommendation available, and it protects the relationship with the ones that have not.

- **Chandler-Gilbert, the self-translating sentence.** *“CGCC's food pantry is called the Coyote Cupboard.”* The plain word and the brand name in one sentence, so the plain-need search matches. **This is the pattern the whole study should point at.**
- **Estrella Mountain, disability organized by condition.** A dedicated ADD/ADHD page plus Learning Disabilities, Assistive Technology, Disability 101, The Law. Directly copyable, requires no renaming.
- **Mesa, the student's question as the heading.** *“Why was I selected for Verification?”* not “Verification Requirements.” Explains the federal reason plainly, notes roughly 30 percent of applicants are selected (which removes the “what did I do wrong” fear), and carries one short video per sub-step. For a persona who loses the thread in multi-step processes, close to correct design.
- **South Mountain, real numbers stated early.** Actual disbursement dates, ACH refunds in 3 to 5 business days, and *“All GPAs welcome, FAFSA is not required.”*
- **Chandler-Gilbert, transfer as a five-step list.** Credit evaluation is step three of five on a page named for what the student is doing, with a named form.
- **Phoenix and Scottsdale, on-site search that does the synonym work.** “Scholarships without a social security number” returns Dreamers/DACA Scholarship Resources first. “How many credits do I need to keep my visa” returns the F-1 status page first, without the student ever typing “F-1.”
- **District-wide, transcripts.** Mesa, Rio, and Scottsdale all route through Parchment, all state $5, all give a phone number. District consistency already works here.
- **Estrella Mountain, the multilingual welcome.** *“Get started here / Empieze Aqui / أبدأ هنا”* gave the refugee persona a moment of belonging.
- **Chandler-Gilbert, international admissions.** A clean numbered 1 to 6 flow, *“NO application fee,”* a concrete cost figure, and an explanation that the I-20 is mailed after acceptance.

---

## The recommendation this register produces

Not a content-writing project and not a renaming project. A **vocabulary-to-service map**, containing three things the evidence names directly:

1. **Felt-need phrases to service names.** “I'm hungry” resolves to Coyote Cupboard, Gecko Grocery, Mesa Market, Artie's FIT Market, Puma Pantry, The Village.
2. **Condition names to services.** ADHD, anxiety, dyslexia, autism all resolve to Disability Resources.
3. **Plain words to institutional terms.** Confidential to private. Log in to MEID. Rent to emergency assistance.

**Check what is already deployed before proposing any build.** Confirmed on every college site: **a language selector in the header** and **a chat widget in the corner**. Observed directly on GateWay, South Mountain, and Mesa, and consistent with the Chandler-Gilbert and GateWay Spanish hub instructions. Any recommendation starting “build a translation layer” or “add a chat” is proposing something already deployed. The question is what those surfaces are connected to.

**The pilot is nearly free.** Run the felt-need phrase list this study already collected against each college's own site search, and report the number back. One person, about a week, no procurement, no new content, no renaming, no rebuild.

---

## What this study is not claiming

**Four retractions, all in the same direction.** Every one came from reading a search summary instead of opening the page, and every one overstated the barrier.

1. GateWay's EMT page does state cost, length, location, and that it is not financial-aid eligible. Severity 3 to 1.
2. Mesa's verification page is not weak. It is one of the best pages in the study. Severity 2 to 1.
3. The claimed JavaScript render defect was the tester's own extraction failing, which **also removes the second instance reported in Part 1**.
4. One run inverted completely. The student fails on Google and succeeds on the college's own site search, using identical words.

**Stated limits.**

- The testers are AI personas, not students. This locates barriers for volunteer fieldwork; it does not replace it.
- Severity is tester-assigned and pending human rating.
- The ten-college tables are **one query phrasing per cell**. They demonstrate a mechanism. They are not a survey, and the counts should be presented as a demonstration rather than defended as measurements.
- Top-of-funnel search ran in a non-Arizona environment, so pure ranking observations there are flagged for an Arizona re-run. The GCC-versus-Glendale-California and GateWay-versus-Gateway-Kentucky name collisions are almost certainly localization artifacts and are **not scored**.
- Everything is public web. Nothing behind a login has been tested.

**Method changes this produced, for the run sheet before volunteers start.**

- **Test both search surfaces and name which one failed.** A finding logged as “the student could not find it” is incomplete until it says whether it was Google or the college's own search. Phoenix College's own search returns the affirming page first for a sensitive query where Google does not.
- **Click, never retype.** Three URLs transcribed from search-result breadcrumbs 404'd because the display drops path segments. A tester who retypes will log a broken link that is not broken.
- **Browser verification is not optional.** See the four retractions.
- **Add a per-college on-site search column to the crosswalk.** Search quality varies more between colleges than the naming does, and it is directly actionable.

---

## Open items

**Data integrity, fix before any of this is presented by persona ID.** Batch 2 of Part 2 carries persona IDs that do not match `agents/README.md`: Jordan Lee logged as P23 (P23 is Ana Lucia Torres; Jordan Lee is P07), Rosa Jimenez as P30 (P30 is Diego Morales; Rosa Jimenez is P27), Maria Gonzalez as P28 (P28 is Jose Herrera; Maria Gonzalez is P26), plus “P18 Grace Okafor” and “Alex Nguyen,” neither of whom is in the fifty. **The findings stand. The labels do not.** Report those by college and task until reconciled.

**Stale header.** `PART2_RUNS_2026-08-25.md` line 4 says “Runs logged: 7.” There are 13 scenario sections plus two further batches. The closing “not yet run” list is also stale; six of the eight it names do have write-ups above it.

**Actually not yet run, from the AI-assigned bank.** S048 Emiliano Vargas at GateWay, S118 Nicole Tran at GateWay.

**Recorded as inconclusive, not a finding.** A combined query bundling textbook affordability and payment plans returned zero at two colleges, but it bundled two distinct needs. The payment-plan half succeeded when tested alone. Re-run separately before logging.

**Next phase.** The journey behind the login: registration, aid status, holds, the portal, and the moment a student drops a class without knowing what it does to their aid. Needs authorization, a test-account path touching no real student data, and tri-chair sign-off on scope, the same way Part 1 was cleared.
