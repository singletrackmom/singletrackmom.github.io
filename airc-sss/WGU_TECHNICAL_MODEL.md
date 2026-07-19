# WGU synthetic-validation technical model (from the Open edX 2026 presentation)

Captured 19 July 2026 from a screenshot of the WGU conference talk. This is the technical spine of the "synthetic course validation" the SSS journey paper already cites. Keep for the study AND the Dial Your Course tool (it maps to both).

## The slide: "Starting points for your institution" (three cards)

**Steps** (how you start)
- Define your population
- Pick a dimension
- Run on one course

**What you need** (inputs)
- Fine-tuned SLM (a Small Language Model fine-tuned on their data, not a giant general LLM)
- JSON output schema (a fixed, machine-readable output format)
- One course in your platform (one real course loaded in the LMS)

**What you get back** (outputs)
- Structured JSON of barriers
- Versioned cohort definition
- Pre-launch QA documentation

## What it means, plain
WGU models a student population as a synthetic cohort, picks ONE variable to test at a time, and runs it against ONE course to keep the first pass small. The engine is a fine-tuned Small Language Model constrained by a JSON output schema, so every run returns the same structured shape. Out comes a machine-readable list of barriers, a versioned definition of the cohort that produced it (so results are reproducible and trackable over time), and QA documentation you can act on BEFORE the course goes live. In short: a repeatable, structured, pre-launch barrier check driven by a small tuned model with strict JSON output.

## Are WE (SSS journey study) doing it the same way?
Mostly the same architecture, one real difference.

Same:
- Synthetic students modeled on a DEFINED population (our fixed set of 50 persona profiles = their "define your population").
- Start SMALL (our demo: one AI tester, two colleges, twelve walks = their "run on one course").
- One dimension/task at a time (our single-task-per-run rule = their "pick a dimension").
- STRUCTURED, inspectable output (our "structured, inspectable finding" ~ their "structured JSON of barriers").
- VERSIONED definitions (our versioned agent template + golden set ~ their "versioned cohort definition").
- QA discipline before trusting results (our validation gate + golden set + multiple runs ~ their "pre-launch QA documentation").

Different (the one to decide on):
- **Model:** WGU uses a FINE-TUNED SMALL LANGUAGE MODEL. Our paper currently uses prompt-scaffolded agents on a general model with a human validation gate, NOT a fine-tuned SLM. A fine-tuned SLM is cheaper to run, more consistent, and can run PRIVATELY / on-prem, which fits Michelle's data-sovereignty hard line (no student PII leaving district control). Tradeoff: fine-tuning needs training data and engineering we do not have yet.
- **Target:** WGU validates a COURSE (course-level barriers, pre-launch QA). Our SSS study validates the student SERVICES journey across 10 colleges. WGU's course-QA angle actually maps more to the **Dial Your Course** tool than to the services study. Note both.

## Open questions to answer later
1. Do we adopt an explicit JSON output schema for our synthetic-student findings (cheap, high value, makes results machine-readable and comparable)? Likely yes.
2. Do we move toward a fine-tuned SLM for privacy + consistency, or stay with prompt-scaffolded agents + validation gate for now? Depends on data + engineering capacity.
3. For the Dialer: WGU's "structured JSON of barriers + versioned definition + pre-launch QA doc" is close to what the Dialer already outputs. Worth aligning the Dialer's output contract to this shape.

## Source
Western Governors University, synthetic course validation, Open edX 2026 conference presentation (cited in `_paper-source.html`). This file is the technical detail behind that citation.
