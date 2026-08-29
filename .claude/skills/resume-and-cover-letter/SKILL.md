---
name: resume-and-cover-letter
description: Build or tailor Michelle Blomberg's resume and cover letter for a specific job. Use whenever she asks to create, update, tailor, or "dial in" a resume or cover letter for a role, company, or job posting. Produces a 3 to 4 page docx plus PDF resume and a business-letter cover letter with a requirements-match block. Holds every locked formatting rule, the frozen generator, the accuracy guardrails, and where the final files live.
---

# Resume and cover letter

> **Companion spec:** `~/Documents/Claude/JobSearch/BULLETPROOF_FORMAT_SPEC.md` holds the full locked detail, including the generator spacing rules. Read it if anything here is ambiguous.
>
> **Read `cultivate/cv.html` FIRST, every time. It is the single source of truth for job history, titles, dates, and accomplishments.** Open the actual file in this repo and read it before writing any resume, cover letter, job-fit rating, star rating, or agent brief.

**Goal:** produce a tailored, ATS-friendly resume (a full 3 pages, up to 4) and a matching cover letter for one specific job, drawn down from the master CV and consistent with every locked formatting rule.
**Audience:** Michelle, applying to a specific posting. The reader is a human screener plus an ATS keyword scan.
**Process:** research the CV and the job, copy the frozen generator, swap only content, build docx then PDF, verify page breaks, save to the company folder.

## Always do first (research before formatting)

1. **Read the master CV `cultivate/cv.html`.** It is the exhaustive master, the big-kahuna file, and every resume and cover letter is drawn DOWN from it and tailored to the job. It is the single source of truth for background, metrics, presentations, certs, and service. Fetch it, never ask Michelle to upload it.
   - **Never work from a summary in CLAUDE.md or from memory.** That file is a briefing, not the record. The CV is the record.
   - **Never assert a gap in Michelle's experience without checking the CV first.** If a posting asks for something, search the CV for it before calling it a miss.
   - **When writing a brief for a subagent, quote the CV into the brief.** Do not paraphrase her background from memory. A subagent cannot fetch the public URL reliably, so paste the relevant CV text in.
   - New projects, real metrics, presentations, certs, and service get added to the CV FIRST, then narrowed for each application. Other resume files are tailored per-company subsets, not masters. If a newer version ever surfaces, reconcile it back into the CV.
   - **Why this rule exists (28 Aug 2026):** an entire rebuild of `jobs/index.html` was rated against the invented claims that she has "no formal Product Manager title, ever" and "no director-level supervisory management." Both are flatly contradicted by the CV: **Product Manager, Higher Education, ProQuest/XanEdu, 1999 to 2002**, and **Director of Instructional Technology, GCC Innovation Center, 2004 to 2011**, seven years leading platforms and the teams behind them. Twenty-two roles were removed and dozens mis-rated on a false premise. Also missed in the same pass: she leads the GCC Cares Hub brand identity, helped plan the campus XR lab with the dean, sat on the GCC intranet redesign committee 2023 to 2024 as a UX practitioner, and led the emergency transition of 45+ faculty to online teaching.
   - Her own words: "I can't rely on just my faculty position to get me into these jobs because they want someone actually doing this work as their job. Rely on my committee assignments and extra projects."
2. **Look at the last few relevant apps** in `~/Documents/Claude/JobSearch/<Company>_Application/` (or ones she points to) to see the current dialed style. The **Per Scholas and WGU builds (June 2026) are the preferred reference**, not the Anthropic one. They nail the requirements-match cover letter (a labeled block mapping every minimum qualification, answered in her own words) plus matching keyword coverage in the resume. Model new applications on those.
3. **Read the job description. List every minimum qualification.** These drive the cover letter map and the resume keywords.

## Build method (do NOT re-engineer the layout)

- **Copy the frozen generator `~/Documents/Claude/Applications/RESUME_MASTER_BOMBPROOF.js`** (mirrored at `RESUME_FORMAT_generator.js`). Swap ONLY the content inside the calls. Keep every helper (`head`, `entry` / `entK` / `entKB`, `ent`, `sub`, `b`, `skill`) and all the spacing and margin values exactly. Never touch layout, spacing, date logic, or colors. Do NOT rebuild or relitigate them.
- **What the frozen template already encodes** (hard-won, do not re-engineer): a 2-cell borderless table per entry; an ADAPTIVE per-entry date column (the date cell is sized to its own date, with the right edge flush at the content margin, so ALL dates align in one column and never wrap to a second line); long titles wrap with the date staying top-right; ALL text black, NO grey anywhere; even section and entry spacing; most-recent-first in every section; Calibri; presentations use org-on-its-own-second-line (no comma on the title line) when the title is long.
- `npm install docx`, then `node`. Convert to PDF with the docx skill's soffice script. Verify page breaks with `pdftotext -layout`, and do a quick visual with `pdftoppm` to PNG to confirm.
- **The Anthropic build (19 June 2026) is the reference OUTPUT for formatting.** The Per Scholas and WGU builds are the preferred reference for CONTENT and for the requirements-match approach.

## Where the final files live (canonical, set 29 June 2026)

Every final resume and cover letter goes in ONE home, `~/Documents/Claude/JobSearch/`, in a per-company subfolder named `<Company>_Application/` (for example `JobSearch/Playlab_Application/`). Each subfolder holds:

- `Blomberg_Resume_<Company>.docx` and `.pdf`
- `Blomberg_CoverLetter_<Company>.docx` and `.pdf`
- that build's generator `.js`

Do NOT scatter final applications into `~/Documents/Claude/Applications/` anymore. Keep build junk (chk*.png, *.tmp, lock files, node_modules) OUT of the final subfolder. The reusable master template `RESUME_MASTER_BOMBPROOF.js` is a tool, not an application, and stays in `~/Documents/Claude/Applications/`. Existing apps (CodePath, Per Scholas, WGU, Anthropic, Guild, GCC Dean, Playlab) were consolidated into JobSearch on 29 June 2026.

## Resume rules (locked, every time)

### Content
- Open with a short, tailored **narrative Professional Summary** (about 4 to 5 lines, executive tone, drawn from Michelle's own mission language). Tailor it in substance, but do NOT name the specific posting or say "this role"; it should not look written for one job. **No skills-list or "Areas of Expertise" block.** What she dislikes is the generic skills-summary opener, not a narrative summary.
- **Every job entry must be thorough** and must demonstrate the relevant skills through concrete accomplishments, not abstract skill statements. The skills a section is meant to show should be visible in the bullets themselves.
- **Pull real depth from the CV:** relevant trainings, presentations, awards, and service. The resume should be a full, robust 3 pages (up to 4).
- **Never lift phrasing from the job description** into the resume. It reads as AI-written. Write accomplishments in Michelle's own words. (Keyword coverage is a different thing from lifted phrasing, see the requirements-match technique below.)
- **Be honest about status:** label tools still in progress as prototypes or "in testing," never imply production. Do not use numbers Michelle cannot verify (no invented percentages or counts); if unsure, say "improved" without a figure.
- **Leave out dated or irrelevant certifications** (for example the 2014 Quality Matters certificate). The current Quality Matters / OSCQR lead-reviewer service role is fine to keep.

### The one entry format (all sections)
ONE entry format across ALL sections (experience, projects, education, certifications, presentations, awards, service):

**Title**, Organization [right tab] Date

- The TITLE comes first and is **the only bold text**, then a comma, then the organization in regular weight, and the date sits alone in its own right-aligned column.
- **Only the title, role, or credential name is bold. Organizations are never bold, anywhere, including education and certifications.**
- **DATE-ON-TOP-LINE RULE (hard, 23 June 2026):** the date ALWAYS sits on the TOP line at the right margin and NEVER drops to a second line. When the title plus organization is too long to fit beside the date on one line, break it between the TITLE and the ORGANIZATION: keep the bold title and the date together on the top line, and move the organization down to its own line below. Only the organization moves, never the date.
- Dates are ALWAYS right-aligned in one consistent column, on every entry. Never in parentheses, never inside the body of a line. Ranges are written with the word "to" and spaces (for example, 2011 to Present).
- When an entry has two date ranges, list them in ascending order with the range ending in "Present" on the RIGHT (for example, 2010 to 2016, 2025 to Present).
- **Separators inside a line are commas.** Never middots, pipes, or bullet characters in the middle of a line.
- City and state for a job go on an italic line directly under the title, unless they fit on the title line without pushing the date to wrap. **No period after the state.**
- Experience entries: the Title, Organization line, then an **italic line for any prior title and the location**, then accomplishment bullets that show the skills through concrete results.
- Education and Certifications: same Title, Organization format, organization not bold, **no bullets**.

### Bullets
- **NEVER A LONE BULLET. EVER.** (Hard rule, 16 Aug 2026.) A bullet list exists to separate several distinct items. If an entry has only ONE supporting line, that line is a PARAGRAPH, not a bullet. If it is a long paragraph, it is a paragraph. Bullets are for short, parallel, genuinely separate points, never for a single block of prose wearing a bullet. Either write more real bullets or drop the bullet entirely. This is enforced in the generator: a single indented line under an entry renders as an indented paragraph, and only runs of two or more render as bullets.

### Sections
- **ONE product section, not two.** Do not split builds into a "selected" section plus an "additional builds" section. That reads as padding. Everything goes under a single `PRODUCT & PROTOTYPE WORK` heading, strongest first.
- **Technical Skills** is a bulleted list at the very BOTTOM. Each bullet leads with a bold category label before the colon, and the categories align to the specific job's required skills, not a generic or arbitrary list. Only list skills Michelle actually uses; remove anything she does not recognize. Split genuinely different categories (for example, Data and analytics separate from Accessibility).

### Page and type
- Full 3 pages. **Calibri.** Name centered at the top, contact line beneath it: **Golden, Colorado, email, phone number, michelleblomberg.com** (the real domain, NOT the github.io address). Never invent URLs (no github.com/singletrackmom).
- **The phone number STAYS on both the resume and the cover letter** (Michelle's call, 17 Aug 2026). Do not strip it "to match the spec."
- No em dashes anywhere. Curly quotes and apostrophes.
- Headings and entry titles use **keep-with-next** so a heading or job title never strands alone at the bottom of a page; it breaks to the next page instead.
- **Page breaks:** every page must BEGIN with a title (the name header, a job title, or a section heading), never an orphaned bullet or a lone heading. A small gap at the bottom of a page is fine and is preferred over an awkward break; force a page break before a role if needed, and keep the Certifications block whole. Tighten spacing (margins and paragraph spacing) to hold three pages.

## Cover letter rules (locked, every time)

### Format
- **Formal block business letter.** The header is **CENTERED** to match the resume (centered name, centered contact line). The contact line separates items with spaces, no middots.
- **NO rule, line, or border under the header** (name and contact line only, nothing underneath). Same for the resume header.
- Body order, with **exactly one blank line** between blocks and **zero blank lines inside the recipient address block**:
  1. **Date.**
  2. **Recipient address block, FOUR tight lines**, no blank lines between them and **no "Human Resources" / "Attn" / department line**: organization or office name (the real one, for example "Mines Online"), then the parent institution, then the street address, then "City, ST ZIP". Look up the real address.
  3. **Salutation:** "Dear Hiring Committee:" with a **COLON**.
  4. **Subject line:** "RE: [exact job title]" with the title in **bold**.
  5. **Body paragraphs.**
  6. "Sincerely," then the name.
- Exactly one blank line after the date and one blank line before the salutation.

### The requirements-match technique (use on EVERY cover letter, this is what beats the AI/ATS screen, Michelle loves it)
Include a clearly-labeled mapping block (for example, "How I meet what you are looking for") that addresses **EVERY minimum qualification** in the job description: one bold lead-in per requirement, answered in Michelle's OWN words (never lift the JD's phrasing, that reads AI-written). A human screener can then check every box in seconds.

**CRITICAL companion step:** the ATS usually scans the RESUME, not the letter. So for each requirement, make sure the real keywords (the exact skill names and terms the posting uses, wherever genuinely true) ALSO appear naturally in the resume (Technical Skills and bullets). Cover letter = explicit human-readable mapping; resume = keyword coverage; the two reinforce each other on every requirement. The Anthropic CSM build (19 June 2026) is the reference example.

### Openings (banned and required)
- **NEVER open with any version of "I have been watching for a role like this,"** or any eager or informal hook. Michelle finds it lame and desperate.
- **NEVER open by telling the organization why it exists or explaining its mission back to it.** She can already tell why they exist; that is not the job of the opening.
- **DO open** with the single most important, most relevant qualification that establishes she is the ideal candidate, stated as fact and evidence, without ever writing "I am the perfect candidate." The first sentence leads with the most important thing SHE brings and how it overlaps what they need, not with a description of the employer.
- **Never mention proximity to the employer's city.** The address already shows location.
- A mission tie-in, if any, belongs later and should be framed as **her own conviction**, never as a statement of what the organization's mission is.
- Avoid "genuinely," "straightforward," casual asides, and overly formal phrasing. No em dashes. Curly quotes.

## Accuracy guardrails (hard, do not violate)

- **LMS work.** She led the campus LMS team in the Blackboard era, co-chaired the district eLearning Advisory Group (which represented the roughly 250,000-user, 10-college system), and contributed to the RFP that led to Canvas adoption. She did **NOT** lead, own, or run the Blackboard-to-Canvas migration, and was **NOT** on the migration team. Never write "led the migration," "scaled a platform to 250K users," or anything implying she personally migrated or ran a 250K-user platform.
- **ARC.** She co-chairs the **Student Support and Success DOMAIN** (Domain 5) of the ARC (the Maricopa district AI Resource Center), not the whole ARC. It is a CENTER, never a "committee," and it is ARC, not AIRC.
- **The Design Studio.** She STARTED the cross-disciplinary design studio as a course and TAUGHT and LED it as her course (that run of leading the design is a real, strong credential, use it in past tense). **On the CV and resumes, END the studio dates at 2023, and say it "lives on as a grant-funded, paid studio led by other faculty."** Do NOT date it 2024, 2025, 2026, or "to Present," and do NOT say she leads, runs, relaunched, or currently advises it. (Background truth, reference only: she taught it roughly 2011 to 2024; it became a grant-funded paid studio in Fall 2025 led by another faculty member with her as an occasional project-basis advisor.)
- **The Traveler.** She is the **DESIGN faculty advisor only, since 2011 (Volumes 44 to 58)**. She coaches the student DESIGN team through the production cycle: branding theme, design and typography, print production, and launch. She has NOTHING to do with the editorial side (no submission review, no editorial selection, no editing) or the art contest and competition judging; students do the editing and a community judge selects the competition winners. The award is the **College Media Association Pinnacle Award for College Literary Magazine (2015, 2016, 2025)**, NEVER "Literary Magazine of the Year." Also a repeat AIGA Best of Phoenix Design Show selection (2017 to 2022).
- **Degrees.** Her bachelor's is a **BFA in Visual Communications, NOT in education.** Never say "my degrees are in education." Let the **M.Ed.** in educational technology (NAU, on connectivism and personal learning environments) carry the degree requirement, and frame the BFA as her user-experience and design foundation.
- **AVC course codes.** AI hallucinates these constantly, never trust training data. Confirm DMA vs Animation first and use only checksheet-verified courses. AVC183 is Digital Graphic Arts I; AVC283 is Digital Graphic Arts II. The historical course taught this cycle (for example in the FEP) is AVC181 Graphic Design I.
- **Program Director.** DMA Program Director 2011 to 2022, now faculty only.
