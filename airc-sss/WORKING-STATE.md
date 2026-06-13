# AIRC Domain 5 (Student Support & Success) — WORKING STATE

**Last updated: June 13, 2026.** Future Claude: read this first to resume the AIRC SSS committee work. Everything below reflects decisions made with Michelle on June 13. Deliverable files live in this same `airc-sss/` folder.

## What this is
Michelle co-chairs ARC **Domain 5 — Student Support & Success** (with another co-chair). We are building an AI-grounded **student-journey usability study** that finds barriers across all 10 Maricopa colleges and turns them into prioritized, human-in-the-loop AI recommendations. It doubles as Michelle's UX job-showcase piece.

## DOMAIN SCOPE — stay in our lane (from the ARC Domain Groups Overview)
**In scope (ours):** AI for the student journey application → graduation — advising, counseling, financial aid, enrollment, registration; retention/persistence/completion; student well-being, personal development, engagement **outside the classroom**; making student-facing services accessible, responsive, equitable.
**Out of scope (NOT ours):** anything about **classroom instruction, curriculum, pedagogy, or faculty tools & training** → that's **Domain 2 (Teaching & Learning)**; governance/security/policy → **Domain 1**; employee training / operational workflows / **Institutional Research (IR)** → **Domain 3**; credentials/badges → **Domain 4**.

### Cross-domain working groups we JOIN (we don't own these)
- **Domain 2 (Teaching & Learning):** student AI-literacy in courses, and **course-design barriers** we surface — e.g., a Canvas course-barrier review aligned to **OSCQR** + required syllabus elements. We contribute the student-barrier lens; they own it. *(This was wrongly listed as our flagship earlier — corrected.)*
- **Domain 3 (Operational Efficiency & Employee Training, incl. IR):** dropout/retention data (Institutional Research, Domain 3), staff workflow/training.
- **Domain 1 (Strategy, Security & Governance):** the Salesforce student-data-collection concern / data governance.

### The four other domains + chairs
1. Strategy, Security & Governance — CIO (PC) + faculty (CGCC)
2. Teaching & Learning — VPAA + faculty (EMCC), faculty (CGCC)
3. Operational Efficiency & Employee Training — Sr. Assoc. VP of IR (SCC), faculty (SMCC)
4. AI Credentials — dean (CGCC), faculty (MCC)
5. Student Support & Success — Michelle Blomberg (GCC) + co-chair (SMCC) ← us

## ARC framework every domain follows
Four responsibilities: (01) identify priorities, (02) build a roadmap, (03) stakeholder engagement, (04) decide how work gets done — Path A (group does it), Path B (form a working group), or another path (e.g., student project). **Michelle wants real WORKING GROUPS with deliverables, not meetings that produce nothing.**

## Our plan = 4 prioritized initiatives (P1–P4)
- **P1 Map the landscape** — tool inventory + service crosswalk (local name per function at each college). First pass done (40+ functions × 10 colleges). *Translate, don't standardize — each college keeps its own names/programs; we never ask them to align.*
- **P2 Student Journey UX Study** — 3 personas live the full journey at all 10 colleges; **problems, not destinations** (we never say "go to advising"; the persona figures it out); capture barriers + severity. Includes **swirling** (occasional, most students never; a needed class is full or not offered in person, so they take that ONE class at another campus that semester. Application still required, but residency now carries over after a recent fix; consortium aid; credit back home) and a **graduation offboarding** task (save email/Drive/coursework before the account closes).
- **Known real barriers (from the co-chair, verify in fieldwork):** many students are never advised and have NO advisor shown in their SIS. GCC may have fixed this via the Field of Interest (FOI) system, but it is NOT district-wide. The residency-re-proof barrier for swirling students was recently removed.
- **P3 Usage & workflow baseline** — how many of ~140,000 students use each service; how depts think students find them vs. how they really do; dept-manager survey. (Dropout/IR data = cross-domain w/ Domain 3.)
- **P4 AI recommendations & pilots** — turn barriers into prioritized, human-in-the-loop AI pilots, built with staff + students; "I am AI" buy-in campaign. **AI-only scope guardrail:** service-process ideas get routed to the right body; classroom/faculty ideas go to Domain 2.

## Real data backing the study (say this in presentations/interviews)
1. Primary research across all 10 colleges' websites (the crosswalk).
2. **GCC Faculty Senate Student Frustrations Survey** — 83 barriers, avg ~4.5/5 frustration AND impact. Top theme: campus tech (printing, wi-fi, login/DUO, lab access). Cross-walked into the tasks.
3. **Rio Salado Student Senate notes (Mar 2026)** — student voice on AI in the classroom (mostly Domain 2 territory), plus a useful hook: students need civic-duty/volunteer hours → the Student AI Group can offer them.

## The 3 personas (BEING DEEPLY DEVELOPED — see Personas doc)
Map to district "Test Student 1/2/3" accounts if that's what we're given.
- **Marisol Reyes (Test Student 1)** — first-gen, 19, pre-Nursing/CTE, works, phone-first, Spanish at home, Pell-dependent. Swirls.
- **Darnell Carter (Test Student 2)** — 34, veteran, Business AA → ASU transfer, full-time job + kids, self-advises, impatient. Swirls.
- **Alex Nguyen (Test Student 3)** — 18, exploring/digital-media, digitally fluent but institutionally naive, ADHD/anxiety, needs DRS, wants belonging.
Personas need **validation with real students** (design-studio students; Student AI Group via student government).

## Deliverables built (in this folder)
- `AIRC_Domain5_Student_Support_Success_Plan.docx` — the domain plan (ARC-aligned, 4 initiatives, roadmap, stakeholder, execution, to-do, real-data section).
- `Maricopa_Student_Journey_Study_Kit.xlsx` — 10 tabs: Read Me, Personas, Scenario Roadmap (branching by program path; swirl tasks; campus-tech task), How to Run It, Service Crosswalk (answer key, 10 colleges), District Tools, Barrier Log, AI Opportunity Map, Roadmap & To-Do, Survey (real data).
- `Student_Journey_Persona_Profiles.docx` — the deep personas (this is the priority deliverable; being built).
- `SSS_Domain_Meeting_Agenda_June18.docx` — DRAFT agenda, **ON HOLD** pending the final working-group list + persona/scope fixes.
- `Create_Barrier_Log_Form.gs` and `student-journey-study.html` and `Student_Journey_Form_Blueprint.docx` — three ways to stand up the tester form.

## Key decisions / preferences
- No personal names attributed in the documents (ideas stand alone).
- Translate-don't-standardize; AI-only scope; human contact is the metric; no PII (test accounts, initials only).
- Personas: highly developed, named, with quirks; map to Test Student #.
- Working groups (Path B) with deliverables, including people who join OTHER domains' groups.

## OPEN ITEMS / next steps
- **Personas:** deeply develop (done this session) → then validate with real students.
- **Form:** DONE. Jotform connected (michelle.blomberg@gmail.com) and the live tester questionnaire is built: **https://form.jotform.com/261635441630048**. The dashboard and the portfolio index link to it ("Live Questionnaire"). Pull responses later via the Jotform `list_submissions`/`analyze_submissions` tools and drop into the workbook Barrier Log. (A `.gs` Google-Form builder and an in-browser HTML version also exist as alternatives.)
- **Work Google Drive (micag04441@gccaz.edu):** NOT connected; Maricopa IT admin likely must approve Claude as a trusted app. Only her **personal** Gmail Drive is connected. Once work Drive connects, place the plan (Google Doc) + workbook (Google Sheet) there.
- **Subcommittees/working groups:** Michelle is finalizing the authoritative list. Do NOT make us own Domain 2/3 items; set up cross-domain participation. Rebuild the agenda after that.
- **Meeting:** Thu (confirm 1:00 vs 2:00 PM AZ + the member who teaches Thursday).
