---
name: resume-and-cover-letter
description: Build or tailor Michelle Blomberg's resume and cover letter for a specific job. Use whenever she asks to create, update, tailor, or "dial in" a resume or cover letter for a role, company, or job posting. Produces a 3 to 4 page docx plus PDF resume and a business-letter cover letter with a requirements-match block.
---

# Resume and cover letter

**Goal:** produce a tailored, ATS-friendly resume (3 to 4 pages) and a matching cover letter for one specific job, drawn down from the master CV and consistent with every locked formatting rule.
**Audience:** Michelle, applying to a specific posting. The reader is a human screener plus an ATS keyword scan.
**Process:** research the CV and the job, copy the frozen generator, swap only content, build docx then PDF, verify page breaks, save to the company folder.

## Always do first (research before formatting)
1. Read the master CV `cultivate/cv.html`. It is the single source of truth for background, metrics, presentations, certs, and service. Fetch it, never ask Michelle to upload it.
2. Look at the last few relevant apps in `~/Documents/Claude/JobSearch/<Company>_Application/` (or ones she points to) to see the current dialed style. The **Per Scholas and WGU builds (June 2026) are the preferred reference**, not the Anthropic one.
3. Read the job description. List every minimum qualification. These drive the cover letter map and the resume keywords.

## Build method (do NOT re-engineer the layout)
- Copy the frozen generator `~/Documents/Claude/Applications/RESUME_MASTER_BOMBPROOF.js`. Swap ONLY the content. Never touch layout, spacing, date logic, or colors.
- `npm install docx`, then `node`. Convert to PDF with the docx skill's soffice script. Verify page breaks with `pdftotext -layout` (and a pdftoppm PNG for a quick visual).
- Finals go in `~/Documents/Claude/JobSearch/<Company>_Application/`: `Blomberg_Resume_<Company>.docx`+`.pdf`, `Blomberg_CoverLetter_<Company>.docx`+`.pdf`, and that build's `.js`. Keep build junk (chk*.png, *.tmp, locks, node_modules) OUT.
- Full locked detail lives in `~/Documents/Claude/JobSearch/BULLETPROOF_FORMAT_SPEC.md`. Read it if anything here is ambiguous.

## Resume rules (locked, every time)
- Open with a short narrative Professional Summary (4 to 5 lines, executive tone, Michelle's mission language). Tailor the substance but do NOT name the posting or say "this role." No skills-list or "Areas of Expertise" opener.
- ONE entry format across ALL sections: **Title** (bold, the only bold text), comma, Organization (regular weight), date alone in its own right-aligned column. Pattern: **Title**, Organization [tab] Date.
- Date-on-top-line rule: the date always sits on the top line at the right margin and never drops to a second line. If Title + Org is too long, break between title and org, keep the bold title and date together on top, move the org to its own line below. Only the org moves.
- Dates right-aligned in one consistent column. Ranges use "to" (2011 to Present). Never in parentheses, never mid-line. Two ranges: ascending, the "Present" range on the right.
- Separators inside a line are commas, never middots or pipes. City, state on an italic line under the title unless it fits without wrapping the date. No period after the state.
- Technical Skills is a bulleted list at the very BOTTOM, each bullet a bold category label before the colon, categories aligned to the target job. Only skills Michelle actually uses. Split genuinely different categories (data/analytics separate from accessibility).
- Full 3 pages (up to 4). Calibri. Name centered at top, contact line beneath: Golden, Colorado, email, michelleblomberg.com (the real domain, NOT github.io, never invent URLs). No em dashes. Curly quotes and apostrophes.
- Every page BEGINS with a title (name header, job title, or section heading), never an orphan bullet or lone heading. Keep-with-next on headings and titles. Keep the Certifications block whole. A small gap at a page bottom is fine.
- Write accomplishments in Michelle's own words. Never lift phrasing from the job description (reads AI-written). Show the skills through concrete results, not abstract skill statements.
- Be honest about status: prototypes are prototypes, in-testing is in-testing, nothing is production. No numbers she cannot verify (say "improved" without a figure if unsure).
- Leave out dated/irrelevant certs (e.g. the 2014 Quality Matters cert). The current QM/OSCQR lead-reviewer service role stays.

## Cover letter rules (locked, every time)
- Formal block business letter. Header CENTERED to match the resume (centered name, centered contact line, spaces between items, no middots). NO rule or border under the header.
- Body order, one blank line between blocks, zero blank lines inside the address block: (1) date; (2) recipient address as FOUR tight lines (office/org name, parent institution, street address, "City, ST ZIP"), no "Human Resources"/"Attn"/dept line, look up the real address; (3) "Dear Hiring Committee:" with a colon; (4) "RE: [exact job title]" with the title in bold; (5) body; (6) "Sincerely," then name.
- Requirements-match block ("How I meet what you are looking for"): one bold lead-in per minimum qualification, answered in Michelle's OWN words (never the JD's phrasing). A screener checks every box in seconds. Companion step: make sure the real keywords for each requirement ALSO appear naturally in the resume (Technical Skills + bullets), because the ATS scans the resume.
- Do NOT open with "I have been watching for a role like this" or any eager/informal hook (she finds it desperate). Open with the single strongest, most relevant qualification stated as fact and evidence. Never write "I am the perfect candidate." Never mention proximity to the employer's city.
- Avoid "genuinely" and "straightforward." No em dashes. Curly quotes.

## Accuracy guardrails (hard, do not violate)
- She led the campus LMS team and contributed to the RFP that led to Canvas adoption. She did NOT lead or run the Blackboard-to-Canvas migration and was not on the migration team. Never write "led the migration" or "scaled a platform to 250K users."
- She co-chairs the Student Support and Success DOMAIN of the ARC (AI Resource Center), not the whole ARC.
- Her bachelor's is a BFA in Visual Communications, NOT in education. Never say "my degrees are in education." Let the M.Ed. carry the degree requirement; frame the BFA as her UX and design foundation.
- AVC course codes: confirm DMA vs Animation before using any.
