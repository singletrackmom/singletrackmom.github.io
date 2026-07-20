---
name: assessment-library-refresh
description: Build-time refresh of the Dial Your Course reference library (tools/reference/*.md), the grounding corpus behind the tool's authentic-assessment, UDL, and RSI suggestions. Use when Michelle asks to update, refresh, or check for newer sources in the assessment reference library, or on a schedule. Pulls candidate scholarship from open, keyless indexes (OpenAlex, ERIC), Michelle vets it, and the vetted claim plus citation goes into the versioned files. Never touches the running tool; the base library stays the trust path.
---

# Assessment library refresh

**Goal:** keep the reference library current so the tool's grounded suggestions never go stale, while keeping the vetted base library as the only thing the running tool trusts. This is a build-time curation loop, never a runtime call.

**Audience:** the tool maintainer (Michelle). Faculty are served indirectly, through better-grounded suggestions.

**Process:** retrieve candidates, vet by hand, update the versioned files. The running tool at `course-dialer/index.html` reads only the base library and makes no live scholarly calls.

## Why the base library stays put
The tool's trust path is deterministic retrieval: a finding type selects a vetted block from `tools/reference/*.md`. A model, when used at all, writes only the last-mile sentence against material it did not invent. Live scholarly calls in that path would add latency, rate limits, and unvetted text. So this refresh runs at build time, and nothing enters the advice until a human vets it.

## The files this maintains
`AUTHENTIC_ASSESSMENT.md`, `ALTERNATE_ASSESSMENTS.md`, `UDL_3.md`, `RSI.md`, `ID_MODELS.md`, `OSCQR_QM_CROSSWALK.md`, `BLOOMS.md`, `SEAT_HOURS.md`. Read `tools/reference/README.md` first; it holds the architecture and the index list.

## The loop
1. **Query the open, keyless indexes** for each topic (authentic assessment under generative AI, two-lane assessment, UDL 3.0, RSI):
   - OpenAlex: `https://api.openalex.org/works?search=<query>&sort=publication_date:desc&per-page=10&mailto=michelleblomberg@gmail.com`
   - ERIC: `https://api.ies.ed.gov/eric/?search=<query>&format=json`
   - (Also available: Semantic Scholar, CORE, Crossref. No personal API key, ever.)
2. **Draft candidate summaries.** For each new work, a one-line claim, the citation, and which file it would strengthen. This is the only AI step, and it produces candidates, not committed advice.
3. **Vet by hand.** Michelle confirms each claim is real, current, and defensible before it enters a file. Reject vendor marketing and anything unverifiable.
4. **Write the vetted claim plus citation into the file,** in the existing format. Keep the tone: argue validity, not pedagogy; hand over a replacement, never just a criticism.
5. **Version it.** Every change is a git commit so the advice is auditable. Note the refresh date in the file and in the tool's Library tab status line.
6. **Do not edit the running tool's inline base library** except deliberately, when a vetted change should ship to faculty. The tool's Library tab can fetch OpenAlex candidates for review, but those are never auto-added; this skill is how they get vetted in.

## Rules
- No personal API key, no student data, no PII. Keyless open indexes only.
- Public repo: keep internal accreditation detail out of these files (see the note in `SEAT_HOURS.md`).
- No em dashes. Curly quotes and apostrophes. Cite every claim.
