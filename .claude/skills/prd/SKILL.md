---
name: prd
description: Build or update a Product Requirements Document (PRD) for one of Michelle Blomberg's tools or projects (Render, CopaMigo, Dial Your Course, Wayfinder, and similar). Use whenever she asks to create, write, update, or "dial in" a PRD or product requirements page. Produces a consistent HTML page on the site design system, never a Word or Excel file.
---

# PRD

**Goal:** every PRD comes out with identical structure and formatting from the first draft, so headings, sections, and styling never drift between tools.
**Audience:** Michelle plus anyone she shares the tool with (district leadership, pilot partners, hiring managers).
**Process:** clone the design system, fill the locked section skeleton, keep Goal/Audience/Process visible, ship as an HTML page.

## Format (locked)
- It is an HTML page on the site design system, never `.docx` or `.xlsx`. Build and link `.html`.
- Start from the page-builder skill's design system (same fonts, palette, 1000px column, header, footer, nav). Easiest path: clone an existing clean PRD, `render/prd.html` (green accent) or `course-dialer/prd.html`, and swap the content.
- `h1` = product name. Eyebrow directly under it: "Product requirements". `h2` = numbered top sections. `h3` = subsections.
- Accent color convention: Render's PRD is green, Cultivate's is plum. Pick ONE solid palette accent per PRD, never a gradient.
- No em dashes. Curly quotes and apostrophes only. Body text left-aligned, never justified. Solid palette colors only.

## The locked section skeleton (use these, in this order)
1. **Summary** - what it is, one paragraph.
2. **Goal** - specific, not vague. (This carries the "Goal" of Goal/Audience/Process.)
3. **Users and context** - exactly who it serves and the situation they are in. (Carries "Audience.")
4. **How it works** - the real mechanics, subsectioned. (Carries "Process.")
5. **Data, privacy, and governance** - data storage, FERPA, no-PII line, any pipeline.
6. **Build and portability** - stack, running on district infrastructure, model portability, key handling.
7. **Pilot and testing** - how the pilot runs, step by step.
8. **Definition of success** - what moves it from pilot to production.
9. **Rollout** - phasing, and what is explicitly out of scope.
10. **Open questions and risks** - honest unknowns.
11. **Roadmap** - what comes next.
- End with a short **Key references** block if sources are cited.
- Insert extra numbered sections only when a tool needs them (e.g. Dial Your Course adds a "Version 2" section). Keep the numbering continuous and the rest of the skeleton intact.

## Content rules
- Goal, Audience (Users), and Process (How it works) must all be present and clearly labeled. Never ship a PRD missing any of the three.
- Be honest about status: label prototypes as prototypes, in-testing as in-testing. Nothing is in production. No unverifiable numbers.
- No student PII / no data that trains a model. Data-sovereign by design. No personal API keys in shipped tools (use a server-side proxy).
