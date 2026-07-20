---
name: research-first
description: Use at the very start of ANY new build project for Michelle Blomberg, before writing code or designing, whenever she asks to build, create, make, prototype, or start a new tool, app, product, agent, feature, or project (not editing an existing page). After she describes the idea, ask whether to research existing tools that already solve the problem before building. Michelle forgets to do this and there may already be tools out there.
---

# Research first

**Goal:** never build something new before checking whether it already exists. A competitive scan sharpens the idea, finds the real gap, and sometimes saves the whole build. Michelle forgets this step, so the tool remembers it for her.

**Audience:** Michelle, at the moment she floats a new build idea.

**Process:** the moment a new build project starts, and before any code, design, or file creation, do this in order.

## 1. Reflect the idea back in one line
Confirm what she is building and the problem it solves, in a single sentence, so the scan is aimed correctly.

## 2. Ask, do not assume
Use the AskUserQuestion tool (not plain text) to ask whether to run a competitive scan first. Offer clear options, for example:
- "Yes, scan existing tools first (recommended)" - fan out across the relevant ecosystem, name the closest tools, and report where her idea is genuinely differentiated before we build.
- "Quick check only" - a fast look at the two or three most obvious existing tools, then build.
- "Skip it, I already know the landscape" - go straight to building.

If the session is unattended (scheduled or she has gone offline), default to running the scan and state that assumption.

## 3. If she says yes, run a real scan
- Fan out with WebSearch / WebFetch across the actual ecosystem for the problem (direct competitors, adjacent tools, native platform features, startups, and any academic or conference work).
- Fact-check claims; treat vendor marketing as "advertised," not proven.
- Report: who does what, where her idea is genuinely differentiated (state it precisely, never "nobody does this" unless verified), and the table-stakes features competitors ship that she does not.
- Save the scan as a dated markdown file in the project folder (for example `COMPETITIVE_SCAN.md`), so it is reusable and versioned.

## 4. Then build
Fold the scan into the design: lead with the real differentiation, and note the gaps worth closing. Hand off to the page-builder or prd skill as needed.

## Voice and rules
- Push back before cheerleading. If a competitor already does this well, say so plainly.
- No em dashes. Curly quotes and apostrophes. Honest status (prototype, in testing), never imply production.
- Goal, Audience, Process on anything built, clearly labeled.
