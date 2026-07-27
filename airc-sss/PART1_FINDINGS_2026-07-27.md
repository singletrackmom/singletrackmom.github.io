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
