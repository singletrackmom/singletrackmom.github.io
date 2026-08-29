# Synthetic student agents (50 instantiated personas)

This folder holds the 50 synthetic-student agents for the Student Journey Gap Analysis (Student Support and Success domain, AI Resource Center). They are the bottom tier of a three-tier, 52-agent system: these 50 personas, one orchestrator that assigns persona plus task plus college, and one research aggregator (`../research-aggregator-agent.md`) that merges every logged run into the barrier register. Each file is one persona from the library, fully instantiated as a runnable system prompt: who the student is, what they know and do not know, their device, life constraints, and emotional state, followed by the same hard rules and findings schema every run returns.

These were generated from two sources in the parent folder:

- `synthetic-student-agent.md`, the reusable template (the role, the `{{fields}}`, the hard rules, and the findings schema).
- `_personas-50.html`, the persona library (ID, name, age, profile, home college, language for all 50).

## Status, updated 29 August 2026

Every file here is an instrument, not a result: a persona file is a prompt, and a run log is the outcome. **Public-web fieldwork has run.** Phase 1a (27 July 2026) and Phase 1b (25 August 2026) together produced roughly 58 logged runs across all ten colleges, using 22 of these 50 personas. Results live in `PHASE1A_RUNS_2026-07-27.md`, `PHASE1B_RUNS_2026-08-25.md`, and the merged `BARRIER_REGISTER_2026-08-27.md`, never in this folder.

Still not run: anything behind a login. That phase needs authorization, a test-account path touching no real student data, and sign-off on scope.

**Known data-integrity item.** Batch 2 of Phase 1b carries persona IDs that do not match the roster below: Jordan Lee logged as P23 (he is P07), Rosa Jimenez as P30 (she is P27), Maria Gonzalez as P28 (she is P26), plus a "P18 Grace Okafor" and an "Alex Nguyen" who are not in the fifty. The findings stand; the labels do not. Report those runs by college and task until the IDs are reconciled.

## How the orchestrator uses these

For a single run, the orchestrator picks three things and combines them:

1. A persona file from this folder (for example `P22_Marisol-Reyes.md`), which supplies the in-character system prompt.
2. A task (for example, “find out what classes to take for nursing” or “find emergency food help”), which replaces the swappable default goal in the file.
3. A target college site to attempt it on (a persona can be run against their home college or, for the crosswalk, another college in the district).

The persona then attempts the task on that college’s public site, in character, thinking aloud, and returns the fixed findings schema. Running the same task across colleges and personas is what produces the comparable set of candidate barriers the study analyzes. A human validates severity and reality before any finding counts.

## STANDING GUARDRAILS. Read before writing any finding.

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

---

## The orchestrator’s lens: gaps we can close with AI

The persona agents stay naive on purpose. They report honestly where a student like them struggles, and they never pre-judge whether a problem is fixable. That is what keeps their findings real. The goal-keeping happens one level up, at the orchestrator, when it collects and synthesizes what the personas return. The orchestrator holds the domain’s actual goal in view the whole time: we are looking for gaps AI can genuinely help close, not a catalog of everything imperfect.

When synthesizing findings, the orchestrator:

1. Tags each candidate barrier by how AI could close it, if it can, using the domain’s three ways: **build a tool**, **plug a tool into a system already in use**, or **create a department workflow (an agent)** that takes routine, repetitive tasks off staff. A barrier that fits none of the three is marked not-AI-addressable and routed to the office that owns it, rather than carried forward as one of our recommendations.
2. Prioritizes the AI-addressable barriers by reach (how many students the fix would help) when shaping the recommendations. The rest are documented and handed off, not solved here.
3. Notes service-coverage gaps, where a college lacks a service a peer college offers. Standing up a new service is not ours to do, but the orchestrator flags it, because the usage baseline and later usage can make the case for that college to add it.
4. Keeps the payoff in view: every AI direction is about lifting routine work off staff so their time goes to the students who need a person, never about replacing anyone.

This keeps the study both honest and useful. Every logged barrier stays real, and what the domain brings forward as its own recommendations is only what AI can actually close.

## The 50 files

| ID | Name | Home college | File |
| --- | --- | --- | --- |
| P01 | Robert Kessler | MCC; swirls to SCC | `P01_Robert-Kessler.md` |
| P02 | Tyler Brooks | PVCC | `P02_Tyler-Brooks.md` |
| P03 | Destiny Carter | SMCC | `P03_Destiny-Carter.md` |
| P04 | Frank DiMarco | PVCC | `P04_Frank-DiMarco.md` |
| P05 | Caleb Smith | EMCC | `P05_Caleb-Smith.md` |
| P06 | Brittany Hale | MCC | `P06_Brittany-Hale.md` |
| P07 | Jordan Lee | PVCC | `P07_Jordan-Lee.md` |
| P08 | Brooke Hanson | CGCC | `P08_Brooke-Hanson.md` |
| P09 | Cody Martin | EMCC | `P09_Cody-Martin.md` |
| P10 | Samantha Wright | SCC | `P10_Samantha-Wright.md` |
| P11 | Leila Hassan | GCC | `P11_Leila-Hassan.md` |
| P12 | Megan O’Brien | GateWay | `P12_Megan-OBrien.md` |
| P13 | Dylan Foster | MCC | `P13_Dylan-Foster.md` |
| P14 | Travis Coleman | SCC | `P14_Travis-Coleman.md` |
| P15 | Hunter Bishop | CGCC; ACE | `P15_Hunter-Bishop.md` |
| P16 | Rachel Dunn | GCC | `P16_Rachel-Dunn.md` |
| P17 | Ashley Bennett | CGCC; swirls to MCC | `P17_Ashley-Bennett.md` |
| P18 | Kaylee Morrison | SMCC | `P18_Kaylee-Morrison.md` |
| P19 | Gregory Pierce | PVCC | `P19_Gregory-Pierce.md` |
| P20 | Amber Sullivan | MCC | `P20_Amber-Sullivan.md` |
| P21 | Nathan Reed | EMCC | `P21_Nathan-Reed.md` |
| P22 | Marisol Reyes | GCC; swirls to EMCC | `P22_Marisol-Reyes.md` |
| P23 | Ana Lucia Torres | Phoenix; Rio for one online class | `P23_Ana-Lucia-Torres.md` |
| P24 | Sofia Ramirez | Phoenix | `P24_Sofia-Ramirez.md` |
| P25 | Gabriel Mendez | Phoenix | `P25_Gabriel-Mendez.md` |
| P26 | Maria Gonzalez | GateWay | `P26_Maria-Gonzalez.md` |
| P27 | Rosa Jimenez | SMCC | `P27_Rosa-Jimenez.md` |
| P28 | Jose Herrera | GCC | `P28_Jose-Herrera.md` |
| P29 | Valeria Castillo | GateWay | `P29_Valeria-Castillo.md` |
| P30 | Diego Morales | SMCC | `P30_Diego-Morales.md` |
| P31 | Lucia Fernandez | Phoenix | `P31_Lucia-Fernandez.md` |
| P32 | Carlos Vega | EMCC | `P32_Carlos-Vega.md` |
| P33 | Isabella Ruiz | CGCC | `P33_Isabella-Ruiz.md` |
| P34 | Miguel Santos | GCC | `P34_Miguel-Santos.md` |
| P35 | Camila Delgado | CGCC; swirls to MCC | `P35_Camila-Delgado.md` |
| P36 | Fernando Rios | Rio + GCC (swirl) | `P36_Fernando-Rios.md` |
| P37 | Alejandra Nunez | GateWay | `P37_Alejandra-Nunez.md` |
| P38 | Emiliano Vargas | Phoenix; ACE | `P38_Emiliano-Vargas.md` |
| P39 | Guadalupe Flores | SMCC | `P39_Guadalupe-Flores.md` |
| P40 | Ricardo Mendoza | MCC | `P40_Ricardo-Mendoza.md` |
| P41 | Jasmine Williams | CGCC | `P41_Jasmine-Williams.md` |
| P42 | Darnell Carter | SCC; swirls to Rio | `P42_Darnell-Carter.md` |
| P43 | Andre Thompson | SMCC | `P43_Andre-Thompson.md` |
| P44 | Nicole Tran | GateWay | `P44_Nicole-Tran.md` |
| P45 | Yuki Tanaka | CGCC | `P45_Yuki-Tanaka.md` |
| P46 | Linda Yazzie | SCC | `P46_Linda-Yazzie.md` |
| P47 | Jaylen Brooks-Ramirez | GCC | `P47_Jaylen-Brooks-Ramirez.md` |
| P48 | Kiana Alofa | MCC | `P48_Kiana-Alofa.md` |
| P49 | Mei Chen | SCC | `P49_Mei-Chen.md` |
| P50 | Hassan Abdi | EMCC | `P50_Hassan-Abdi.md` |
