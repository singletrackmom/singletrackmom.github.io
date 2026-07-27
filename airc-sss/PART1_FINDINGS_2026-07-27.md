# Part 1 findings log, first batch, 27 July 2026

**Part 1 = no-login tasks only** (getting-in-the-door search + public service findability). Public web, no account, already cleared by the tri-chairs. This is the first real logged batch, run to check the instrument and watch for saturation. Severity uses the Nielsen 0 to 4 scale (0 none, 1 cosmetic, 2 minor, 3 major, 4 catastrophic).

## Layer 0, getting in the door (search from a felt need)

Personas searched the way a real person would, from a motivation, not a college name.

- **"6 month certificate programs that pay well near Phoenix"** (laid-off, wants fast income). Maricopa surfaces, but underneath aggregator and for-profit results (Research.com, University of Phoenix, Monster). Scottsdale CC and "Maricopa Community Colleges" appear, but no single district front door for "fast job training near me." Severity 2.
- **"how to become a nurse in Phoenix affordable"** (career goal, cost-driven). Maricopa nursing (Phoenix College, Paradise Valley) surfaces well, but below ranking aggregators and next to ASU Online and for-profits. Severity 1 to 2.
- **"welding training Glendale AZ"** (trade goal, local). GCC's welding page ranks, but competes head-to-head with UTI, West-MEC, and Arizona Automotive Institute (for-profit and MEC) on the same first page. A student cannot tell the cheap accredited option from the expensive one. Severity 2.
- **"affordable online college Phoenix working parent"** (flexible/online need). Rio Salado surfaces as the Maricopa answer, but under University of Phoenix and Franklin. Severity 2.

**Layer 0 theme:** Maricopa shows up, but never as a clear single front door, and always beside for-profit and aggregator noise. A motivated person can miss the cheapest accredited option entirely. This is the getting-in-the-door leak, and it is invisible if the study starts at "Apply."

## Flagged for localized re-test: name-collision in search (NOT scored)

Important caveat: these searches ran in a generic, non-localized US search environment (no Arizona location, no login), so the two results below are almost certainly a test-condition artifact, not a barrier a local student hits. Real Google localizes by the searcher's location, so a prospective student in Phoenix would most likely get the Arizona college prioritized. These are set aside, not scored, and should be re-run from an Arizona location before any conclusion.

- **GCC vs Glendale, California.** A generic search for "Glendale Community College" surfaced glendale.edu (California) at or above gccaz.edu. Likely a localization artifact.
- **GateWay vs Gateway, Kentucky.** A generic search surfaced Gateway (Kentucky) above the Phoenix GateWay. Likely a localization artifact.

Takeaway: this is a known reality (the district will not rename a college), so it is a small disambiguation caveat, not a headline finding. The real lesson is methodological: search-findability runs must be executed from the student's actual location, which is a refinement for the persona agents.

## Cross-college naming chaos (the crosswalk barrier, shown live)

Same function, unrecognizable local names. A student who knows the words "food pantry" will not search these:
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

The headline themes (name-collision findability, cross-college naming chaos, for-profit crowding at the top of funnel) repeated across colleges within the first handful of runs, which is the diminishing-returns signal Nielsen describes. The instrument is producing concrete, decision-ready records. Next: widen persona variety on the same tasks to confirm identity-specific barriers, and extend the public-service sweep across the remaining colleges.

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

7. **Cross-college naming chaos, reconfirmed.** Same function, unrecognizable local names (food pantry brands, counseling meanings), plus a real cross-college trust snag: PVCC's disability portal URL says GCCAZ, which a cautious student reads as the wrong college.

## Wins recorded (the study credits what works)

Fair findings require logging the good, and there is real good: SCC's plainly titled "Food and Housing Resources" page ranked and did the work, and even lists a tribal (Salt River Pima Maricopa) food bank; EMCC's multilingual "Get started here / Empieze Aqui / أبدأ هنا" welcome gave the refugee student a moment of belonging; CGCC's international admissions page uses a clean numbered 1 to 6 flow, states "NO application fee," gives a concrete cost figure, and explains the I-20 is mailed after acceptance; MCC defines grants, scholarships, and work study in one plain line each; GateWay's EdReady is a real at-home placement option (just buried). These are the models to copy, not exceptions to explain away.

## Methodological notes for the write-up

- **Portal timeouts are a finding, not noise.** Two heavy external portals failed to load on a phone during real runs. Whether or not they are up every minute, the pattern (funnel the lowest-bandwidth users into the heaviest external pages) is a genuine access risk to record and re-test.
- **Localization caveat still applies** to any search-from-need step (runs used a generic, non-Arizona search environment). The findability signal here is about site labeling and page structure once the student arrives, which localization does not change; pure search-ranking observations stay flagged for an Arizona-located re-run.
- **This batch supports widening, not deepening.** Because the defect classes are repeating, the next useful move is breadth: run the same task set at the remaining colleges (GateWay, GCC, Phoenix, Rio not yet covered on several of these services) to confirm the crosswalk pattern holds district-wide, then hand the confirmed themes to the domain as the Part 1 result set.

**Total logged Part 1 runs to date: 11 persona-agent runs + the Layer 0 findability sweep + the live crosswalk checks.** Still preliminary and human-validation-pending; nothing is presented as a completed district finding. The instrument works and the themes are converging.
