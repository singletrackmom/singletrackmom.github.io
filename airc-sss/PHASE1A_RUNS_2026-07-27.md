# Part 1 findings log, first batch, 27 July 2026

**Part 1 = no-login tasks only** (getting-in-the-door search + public service findability). Public web, no account, already cleared by the tri-chairs. This is the first real logged batch, run to check the instrument and watch for saturation. Severity uses the Nielsen 0 to 4 scale (0 none, 1 cosmetic, 2 minor, 3 major, 4 catastrophic).

## Layer 0, getting in the door (search from a felt need)

Personas searched the way a real person would, from a motivation, not a college name.

- **"6 month certificate programs that pay well near Phoenix"** (laid-off, wants fast income). Maricopa surfaces, but underneath aggregator and for-profit results (Research.com, University of Phoenix, Monster). Scottsdale CC and "Maricopa Community Colleges" appear, but no single district front door for "fast job training near me." Severity 2.
- **"how to become a nurse in Phoenix affordable"** (career goal, cost-driven). Maricopa nursing (Phoenix College, Paradise Valley) surfaces well, but below ranking aggregators and next to ASU Online and for-profits. Severity 1 to 2.
- **"welding training near Phoenix"** (trade goal, local). The district's welding program is at GateWay (the trades-focused campus), and it ranks, but competes head-to-head with UTI, West-MEC, and Arizona Automotive Institute (for-profit and MEC) on the same first page. A student cannot tell the cheap accredited option from the expensive one, and would not know which Maricopa college even offers the trade. Severity 2. (Trade example only; the finding is the for-profit crowding and the missing single front door, not the specific program.)
- **"affordable online college Phoenix working parent"** (flexible/online need). Rio Salado surfaces as the Maricopa answer, but under University of Phoenix and Franklin. Severity 2.

**Layer 0 theme:** Maricopa shows up, but never as a clear single front door, and always beside for-profit and aggregator noise. A motivated person can miss the cheapest accredited option entirely. This is the getting-in-the-door leak, and it is invisible if the study starts at "Apply."

## Flagged for localized re-test: name-collision in search (NOT scored)

Important caveat: these searches ran in a generic, non-localized US search environment (no Arizona location, no login), so the two results below are almost certainly a test-condition artifact, not a barrier a local student hits. Real Google localizes by the searcher's location, so a prospective student in Phoenix would most likely get the Arizona college prioritized. These are set aside, not scored, and should be re-run from an Arizona location before any conclusion.

- **GCC vs Glendale, California.** A generic search for "Glendale Community College" surfaced glendale.edu (California) at or above gccaz.edu. Likely a localization artifact.
- **GateWay vs Gateway, Kentucky.** A generic search surfaced Gateway (Kentucky) above the Phoenix GateWay. Likely a localization artifact.

Takeaway: this is a known reality (the district will not rename a college), so it is a small disambiguation caveat, not a headline finding. The real lesson is methodological: search-findability runs must be executed from the student's actual location, which is a refinement for the persona agents.

## A felt-need search does not reach the service (the crosswalk barrier, shown live)

The service exists at every college under the name that college chose, and those names are not the issue. The issue is that a student searching "food pantry" or "I am hungry" does not reach any of them, because the pages carry the service name and not the student's words:
- **GCC:** "GCC Cares" (Center for Assistance, Resources, and Educational Success), food under "Basic Needs."
- **Phoenix College:** "Bear Necessities," "Patio Pick-Up," "Resource Room," plus a "Food Pantry."
- Severity 3. This is the translate-don't-standardize crosswalk problem, demonstrated on the first two colleges checked.

## Part 1 / Part 2 split, shown live

- **MCC Disability Resources.** The DRS *information* is findable on the public site (Part 1), but *registering* requires "DRS Connect" and an MCC student email login (Part 2). Clean example of where the login wall falls. Severity 2 for the login-gated step.

## What works (record the wins too)

- **Rio Salado tutoring.** Clear path at riosalado.edu/student-resources/tutoring, 24/7 BrainFuse and an Online Writing Lab. The online-first college does findability well. Severity 0 to 1. Relevant to the online-learner emphasis.
- **EMCC counseling** is findable, but carries a caveat ("counseling faculty do not provide therapeutic counseling") and three different crisis numbers. A student in crisis faces number soup. Severity 2.

## First real persona-agent run (P22 Marisol Reyes vs live GCC site)

This is the instrument used as intended: the P22 agent definition loaded as the system prompt, assigned one task and her home college, walking gccaz.edu in character, returning the built findings schema.

- **persona_id / name:** P22, Marisol Reyes (19, GCC, phone-first, Spanish-first, first-gen, never advised, does not know the word "advisement")
- **college:** GCC (home)
- **task:** Talk to someone who can tell you what classes to take for nursing (T14, find advising, from a felt need)
- **outcome:** gave up
- **path_taken:** homepage → "Degrees & Certificates" hoping to find nursing → sees "Fields of Interest" and "Programs of Study" (does not know those terms) → backs out → "Become A Student" → sees "Advisement" and "Gaucho New Student Advisement" but does not know "advisement" means help picking classes → hesitates → tries the "What Type of Student Are You?" cards → generic students page, still no clear "talk to a person about nursing classes."
- **where_it_broke:** the only route to a human who helps pick classes is labeled "Advisement," a word she does not know, and nothing bridges "nursing" to "advisor."
- **quote:** "I see nursing and I see Advisement, but nobody says they go together, and I don't know what advisement means. I don't want to click the wrong thing."
- **suspected_barrier:** staff-language label ("Advisement") blocks a first-gen student; no felt-need path from "what do I take for nursing" to a person.
- **severity_candidate:** 3 (major). Human rater confirms.
- **device_note:** the mega-menu toggles are heavy on a phone, many submenus to open.
- **effort:** several dead-end menu opens, quits from anxiety about clicking the wrong thing.
- **notes:** plain-language wins exist ($97/credit, the "What Type of Student Are You?" cards). The gap is specifically the advising label and the nursing-to-advisor bridge.

## Saturation note

The headline themes (name-collision findability, felt-need searches not reaching the service, for-profit crowding at the top of funnel) repeated across colleges within the first handful of runs, which is the diminishing-returns signal Nielsen describes. The instrument is producing concrete, decision-ready records. Next: widen persona variety on the same tasks to confirm identity-specific barriers, and extend the public-service sweep across the remaining colleges.

---

# Part 1 findings log, second batch, 27 July 2026

Ten more persona-agent runs, each one persona + one no-login task + one college, walking the live public site in character and returning the findings schema. This batch deliberately widened both the persona variety (veteran, refugee/ESL, Native student, disability, health-careers, international/F-1, first-gen, dual-enrollment high schooler) and the service coverage (veterans, apply/English, food, disability, placement, mental health, financial aid, tutoring, dual enrollment, international admissions), across seven colleges not yet deeply sampled (SCC, EMCC, PVCC, GateWay, MCC, SMCC, CGCC). Severity is the Nielsen 0 to 4 candidate; a human rater confirms before it counts.

## The ten runs

| Run | Persona | College | Task | Outcome | Sev | Core barrier (candidate) |
| --- | --- | --- | --- | --- | --- | --- |
| P42 Darnell Carter | veteran, online | SCC | Use GI Bill, find who certifies enrollment to the VA | partial | 2 | No named School Certifying Official on the public site; certifying function is a faceless "office"; no remote-submission path for an online-only veteran; "VSO" abbreviation collides with the veteran's own meaning (a person, not an office) |
| P50 Hassan Abdi | refugee, ESL, phone | EMCC | Apply as a new student and find English help | partial | 3 | The felt need splits into two admissions paths (non-credit ESOL vs credit enrollment) that the site never connects; "non-credit" and "CELSA" never explained; the first action link (admissions.maricopa.edu) timed out repeatedly on a phone |
| P46 Linda Yazzie | Native, cost-driven | SCC | Find emergency food / a food pantry | found | 1 | The pantry is mascot-branded ("Artie's FIT Market"), which does not read as "food pantry" to someone searching literally; sign-up needs an MEID email and an external GivePulse form |
| P07 Jordan Lee | disability | PVCC | Find disability accommodations and how to set up | found (friction) | 3 | Jargon-first, process-last: leads with "affiliation process," MEID, Section 504 instead of plain steps; "testing accommodations" never says "extra time"; login wall at the DRS Connect portal; the portal URL says GCCAZ on a PVCC page |
| P44 Nicole Tran | health careers, online | GateWay | Find first steps + whether a placement test is needed | partial | 3 | Nine-plus exams listed (EdReady, ACCUPLACER, HESI, CELSA...) with no "for a health program, here is the one test"; the answer differs by program; remote testing offered only for HESI, so an online student is stranded; /testing link timed out twice |
| P19 Gregory Pierce | overwhelmed | PVCC | Find mental-health counseling, reach it now | partial | 3 | "Counseling" at the college means academic/career counseling; the services page states counselors "do not conduct therapy"; crisis help is buried under Academics; 988 shown only as a bare link, no number |
| P48 Kiana Alofa | affordability, phone | MCC | Find financial aid, the first step, help if aid is thin | partial | 3 | Landing page opens with federal jargon (OBBBA, SAI, proration); the FAFSA-year and eligibility content are un-zoomable images on a phone; the "what if aid is not enough" answer (payment plan, Mesa Promise) is fragmented and never linked from the aid flow |
| P03 Destiny Carter | struggling, in-person | SMCC | Find free math tutoring | found (friction) | 2 | Service named "Learning Center / Learning Resources / LRC," not the word "tutoring" that students search; leads with a video and acronym-heavy hours; only the online path has clear steps, the in-person walk-in has no location or map |
| P15 Hunter Bishop | high schooler | CGCC | Find how a high schooler enrolls, and if it is free | partial | 3 | Five programs thrown at once (Dual, Concurrent, ACE, Hoop of Learning, HS Advisors) with no "which one is you"; sign-up buried three levels deep and gated by jargon (MEID, Duo, Accuplacer, FERPA); "ACE" is a keyword trap (a closed need-based scholarship); the word "free" never appears |
| P49 Mei Chen | international, F-1 | CGCC | Find how to apply and what documents (I-20) are needed | found | 2 | US immigration jargon (SEVIS, I-20, I-94) never explained; Step 4 references a "form" with no link; one FAQ link points to a www-stage staging URL |

Outcome spread: 3 found, 5 partial, 2 found-with-friction, 0 flat failures. Severity spread: one 1, two 2s, one 2 (friction), six 3s. Nothing hit 4, though two access failures (the EMCC portal timeout and the GateWay dead testing link on an online student) are 3s that tip toward 4 for a low-patience, phone-only, or fully-online user.

## Cross-cutting themes (saturation is holding)

The same handful of barrier types now repeat across nine more runs, seven more colleges, and eight new services. This is the diminishing-returns pattern Nielsen describes: new runs keep confirming the same defect classes rather than surfacing new ones.

1. **Staff language beats student language (the naming barrier).** The single most repeated defect. Students search their felt need ("food pantry," "tutoring," "talk to someone," "extra time on tests") and the site answers in institutional labels ("Artie's FIT Market," "Learning Center / LRC," "counseling" meaning academic advising, "affiliation process," "VSO"). This is the same defect the first batch found at GCC ("Advisement") and Phoenix ("Bear Necessities"), now confirmed at SCC, PVCC, SMCC. It is the translate-don't-standardize crosswalk problem, shown live on real pages.

2. **Jargon walls with no glossary.** Nearly every run hit undefined terms a newcomer cannot decode: MEID, SEVIS, I-20, I-94, FAFSA/SAI/OBBBA, ACCUPLACER, cut score, non-credit, CELSA, Section 504, disbursement. The information exists but is written for people who already understand the system.

3. **No "which one is me" triage when a service forks.** When a need maps to several options, the site lists all of them and makes the anxious newcomer self-diagnose: five high-school programs at CGCC, nine placement exams at GateWay, academic vs mental-health counseling at PVCC, non-credit vs credit admission at EMCC. A one-question decision aid would resolve most of these.

4. **Online and phone-first students are stranded by in-person framing and heavy portals.** Veterans routed to an appointment-only office (SCC), placement described as a campus walk-in (GateWay), aid content locked in un-zoomable images (MCC), and two external portals that timed out on a phone (admissions.maricopa.edu, gatewaycc.edu/testing). For the online-first learner this study emphasizes, this is a recurring access barrier, not a cosmetic one.

5. **The Part 1 / Part 2 login wall is cleanly located.** Findability is public; the wall falls at exactly the same place every time, the DRS Connect portal (PVCC), the financial-aid award status / Student Center (MCC), the ESOL/admissions portal (EMCC). This confirms the three-part scope split is real and observable, not theoretical.

6. **Crisis and mental-health clarity is weak.** Beyond the first batch's EMCC "number soup," PVCC buries crisis help under Academics, states counselors do not do therapy, and shows 988 only as a bare link. This is the highest-stakes version of theme 1 and worth flagging to the domain on its own.

7. **Felt-need searches still not reaching the service, reconfirmed.** The services exist under their own local names, and a plain-language search reaches neither the food pantries nor the right meaning of counseling, plus a real cross-college trust snag: PVCC's disability portal URL says GCCAZ, which a cautious student reads as the wrong college.

## Wins recorded (the study credits what works)

Fair findings require logging the good, and there is real good: SCC's plainly titled "Food and Housing Resources" page ranked and did the work, and even lists a tribal (Salt River Pima Maricopa) food bank; EMCC's multilingual "Get started here / Empieze Aqui / أبدأ هنا" welcome gave the refugee student a moment of belonging; CGCC's international admissions page uses a clean numbered 1 to 6 flow, states "NO application fee," gives a concrete cost figure, and explains the I-20 is mailed after acceptance; MCC defines grants, scholarships, and work study in one plain line each; GateWay's EdReady is a real at-home placement option (just buried). These are the models to copy, not exceptions to explain away.

## Methodological notes for the write-up

- **Portal timeouts are a finding, not noise.** Two heavy external portals failed to load on a phone during real runs. Whether or not they are up every minute, the pattern (funnel the lowest-bandwidth users into the heaviest external pages) is a genuine access risk to record and re-test.
- **Localization caveat still applies** to any search-from-need step (runs used a generic, non-Arizona search environment). The findability signal here is about site labeling and page structure once the student arrives, which localization does not change; pure search-ranking observations stay flagged for an Arizona-located re-run.
- **This batch supports widening, not deepening.** Because the defect classes are repeating, the next useful move is breadth: run the same task set at the remaining colleges (GateWay, GCC, Phoenix, Rio not yet covered on several of these services) to confirm the crosswalk pattern holds district-wide, then hand the confirmed themes to the domain as the Part 1 result set.

**Total logged Part 1 runs to date: 11 persona-agent runs + the Layer 0 findability sweep + the live crosswalk checks.** Still preliminary and human-validation-pending; nothing is presented as a completed district finding. The instrument works and the themes are converging.

---

# Part 1 findings log, third batch, 27 July 2026, the enrollment funnel walked end to end

The first two batches sampled one service at a time. This batch does what the study is really for: take a persona from zero and walk the whole front-of-funnel in order, finding the college, apply, residency and cost, placement, financial aid, next steps, register, and keep going down the funnel until a login the student does not have blocks the run. Three personas walked the full funnel at three different colleges. The point of the walk is to locate exactly where Part 1 (public) ends and Part 2 (account required) begins, and to see what the student endures on the way down.

Runs: **P22 Marisol Reyes (GCC)**, **P42 Darnell Carter (SCC)**, **P48 Kiana Alofa (MCC)**.

## The headline: all three hit the same wall at the same place

Every walk completed Stages 1 through 7 on the public site and was stopped at **Stage 8, Register for Classes**, when the Student Center (redirect.maricopa.edu/student-center) redirected to the Maricopa single sign-on and demanded an **MEID + password + Duo two-factor** the student does not have. That is the Part 1 / Part 2 boundary, observed identically at three colleges: **the public journey runs all the way to the classroom door, and stops the instant a student tries to actually register.** No one enrolled.

A subtlety worth reporting: the account (the MEID) is not created at the wall. It is created much earlier, at **Stage 3, the admissions application wizard (admissions.maricopa.edu)**, where the very first screen asks "Do you have a Maricopa email / Student ID?" That is where "create your account" actually happens, but it is disguised as a yes/no eligibility question and never labeled as account creation. So a student meets the MEID as a barrier three separate times (application, placement via EdReady, registration) before anything explains what it is.

## Per-stage severity across the three walks

| Stage | GCC (P22) | SCC (P42) | MCC (P48) | Recurring defect |
| --- | --- | --- | --- | --- |
| 1. Find the college | 1 | 0 | 0 | Felt-need search lands fine; homepage buries the single next action under many competing CTAs |
| 2. How to apply | 3 | 2 | 2 | Undefined jargon at step one (MEID, Student Center, Duo, residency, placement); "write down your MEID" with no definition |
| 3. Start the application | 2 | 1 | 2 | Account/MEID creation disguised as an eligibility question; multiple new IDs introduced at once |
| 4. Residency and cost | 3 (4, page timed out) | 3 (residency page timed out) | 3 | "Out-of-state until you prove otherwise," statutes and Prop 308, no plain dollar figure; the residency page itself failed to load |
| 5. Placement | 3 | 2 | 2 | Too many test acronyms; the real relief (GPA 2.6+ may skip the test) is buried; at-home EdReady is gated by the MEID |
| 6. Financial aid | 2 | 3 | 2 | Account sprawl (MEID + Duo + Maricopa email + StudentAid.gov); alarming "aid not available / OBBBA" banners; veteran GI Bill siloed from the main aid page |
| 7. Next steps / advising | 2 | 2 | 2 | The friendliest human help (advising to pick classes) is gated behind "already admitted," positioned after the confusing account gate; hand-off pages that forward instead of answering |
| 8. Register | 4 (wall) | 2 (wall) | 4 (wall) | Student Center login wall, MEID + Duo; the true Part 1/Part 2 boundary |

## What the funnel walk adds beyond the single-service runs

1. **The wall is located and it is consistent.** Registration (Stage 8, Student Center) is where public findability ends, at all three colleges. This is the clean, defensible scope line for the study: Part 1 is everything above it, Part 2 begins here.

2. **MEID is the silent gatekeeper of the whole funnel.** The single most damaging defect is not any one page, it is that the identifier the entire journey depends on is never explained and its creation is hidden inside an eligibility question. A first-gen or newcomer student collects the word "MEID" as an unexplained demand at Stage 2, Stage 3, Stage 5, and Stage 8. One plain callout ("You will get an MEID when you apply. It is your student ID and password for everything after this.") would unblock the whole path.

3. **Cost and residency is the highest-anxiety stage, and it is the most broken.** Every walk rated it a 3, the residency page timed out and never loaded on two of the three, and none of the three ever got a plain price on the page that is supposed to give it (the friendly "$97/credit" lives only on a marketing homepage, disconnected from the scary legal residency page that says you are out-of-state until you prove otherwise).

4. **The order is backwards.** The most reassuring, human step, an advisor who will "help you pick your first-semester classes" and "walk you through logging in," sits at Stage 7, gated behind "already admitted," which is exactly after the confusing account gate where anxious students quit. The site puts its warmest content behind its coldest gate.

5. **System sprawl compounds the confusion.** A single enrollment attempt crosses gccaz.edu, maricopa.edu, admissions.maricopa.edu, and sso.maricopa.edu, each with a different look, so a low-confidence student loses track of "which site am I even on."

6. **Whole-person needs never surface in the funnel.** The working-parent walk (P48) never once saw childcare or family support anywhere in the get-started path; it would have to be hunted separately. The veteran walk (P42) had to find Veterans Services on its own because cost, residency, and the main aid page never routed a vet there.

## Wins recorded

"It is free to apply and everyone is accepted" (reassuring at the top of the funnel); a Spanish enrollment guide; the Maricopa Promise $600 scholarship; at-home non-proctored EdReady placement and an online orientation for online students; genuinely clear numbered enrollment-step pages at MCC and SCC; Enrollment Navigators / Saturday enrollment hours; and GCC's Gaucho New Student Advisement page, which speaks in plain language directly to the fear of picking the wrong classes. These are the models to copy.

## Status

Three end-to-end funnel walks, three colleges, one identical wall at registration. Preliminary and human-validation-pending, as with every batch; the value here is that the Part 1 boundary is now observed and located, not assumed, and the front-of-funnel defect pattern (unexplained MEID, broken and jargon-heavy residency/cost, backwards ordering of human help) reproduces across colleges. Next widening: run the same funnel at the remaining colleges (PVCC, CGCC, GateWay, SMCC, EMCC, Phoenix, Rio, GateWay) to confirm the wall and the MEID-gatekeeper pattern hold district-wide.
