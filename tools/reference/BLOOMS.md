# Bloom's Taxonomy · Reference for Dial Your Course

**Goal:** Give Dial Your Course real data for the objectives check, so it can flag unmeasurable verbs and suggest observable replacements at the right cognitive level, without needing an AI model.

**Audience:** Me, and anyone maintaining Dial Your Course.

**Process:** Two lists do most of the work. A **banned-verb list** (unmeasurable) and a **verb bank by level** (observable). Both are string matching. Only a full contextual rewrite needs a model.

---

## Which Bloom's

**Revised Bloom's Taxonomy** (Anderson & Krathwohl, 2001). Six levels, verbs not nouns, `Create` at the top rather than `Evaluate`. This is the version accreditors and curriculum committees expect.

## The rule

> **If you cannot observe it, you cannot assess it.**

"Understand," "know," and "appreciate" describe what happens inside a student's head. Nobody can see inside a student's head, so nobody can grade it. Every unmeasurable objective is a promise you cannot keep and cannot verify.

Note the trap: **"Understand" is a valid Bloom's LEVEL and an invalid objective VERB.** The level describes the cognition. The verb has to describe the observable evidence of it. This confuses people constantly and it is worth saying out loud in the tool.

## Banned verbs (flag these)

Unmeasurable. There is no assignment that proves a student did them.

`understand` · `know` · `learn` · `learn about` · `appreciate` · `be aware of` · `be familiar with` · `become acquainted with` · `gain knowledge of` · `be exposed to` · `grasp` · `comprehend` · `realize` · `internalize` · `value` · `have a working knowledge of` · `study` · `cover` · `explore` (when it means "we will talk about it")

## Verb bank, by level

| Level | What the student does | Observable verbs |
|---|---|---|
| **1 · Remember** | Recalls facts | define, list, recall, identify, name, label, recognize, state, match, select, locate |
| **2 · Understand** | Explains ideas | describe, explain, summarize, paraphrase, classify, compare, contrast, interpret, illustrate, give an example of |
| **3 · Apply** | Uses it in a new situation | apply, demonstrate, execute, implement, use, produce, solve, operate, calculate, modify, build |
| **4 · Analyze** | Breaks it apart, sees relationships | analyze, differentiate, deconstruct, organize, examine, categorize, diagnose, distinguish, attribute |
| **5 · Evaluate** | Judges against criteria | evaluate, critique, judge, justify, defend, appraise, assess, argue, select (with rationale), prioritize |
| **6 · Create** | Makes something new | create, design, construct, develop, formulate, compose, generate, produce (original), plan, author |

## Structure of a measurable objective

> **[Condition] the student will [observable verb] [object] [criterion].**

- **Condition** (optional): "Given a client brief..." "Using Adobe Illustrator..."
- **Verb**: from the bank above. Exactly one. Two verbs means two objectives.
- **Object**: the actual thing.
- **Criterion** (optional but strong): "...to WCAG AA contrast standards." "...in under five seconds."

**Weak:** Students will understand color theory.
**Strong:** Using Adobe Color, the student will **construct** a five-color palette and **apply** it consistently across a poster, postcard, and animation. *(Two verbs, so arguably two objectives. Good problem to have.)*

## Level-appropriateness (the check nobody runs)

Bloom's level should **match the course level**, and a program should escalate across it.

- A **100-level intro** course sitting entirely at *Remember* and *Understand* is under-ambitious. Students should be making things.
- A **capstone** sitting at *Remember* is a real problem, and it is the kind of thing a curriculum reviewer notices immediately.
- **AVC248 is a capstone.** Its objectives should live in *Apply, Analyze, Evaluate, Create*. If any of them say "understand," that is a finding.

## Alignment

An objective is not just measurable, it has to **map to an official Maricopa course competency.** A beautifully written objective that serves no competency is scope creep, and a competency with no objective serving it is a gap. Dial Your Course should check both directions.

---

## What Dial Your Course can do with this, and where the line is

**Deterministic, no AI:**

- Flag any banned verb.
- Flag an objective with **no verb from the bank** at all.
- Flag **two or more verbs** in one objective (should be split).
- Suggest replacement verbs **at the appropriate level**.
- Flag **level mismatch** against the course level.
- Flag objectives that map to **no competency**, and competencies with **no objective**.

**Needs a model:**

- Rewriting "understand color theory" into a full, contextual, measurable objective.

**The honest framing:** the tool can tell you *exactly what is wrong* and *what family of verb to reach for* without any AI at all. The last mile, writing the sentence for you, is the only part that needs a model, and a human should be writing that sentence anyway.

**Source:** Anderson, L. W. & Krathwohl, D. R. (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives.*
