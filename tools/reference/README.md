# Dial Your Course, reference library

This folder is the grounding corpus for the tool's v2 suggestions. The point: when the tool proposes an alternate assessment, a UDL fix, an RSI statement, or reads findings through an instructional-design lens, the recommendation is pulled from vetted material here, not invented by a model. This is what keeps a trust-critical tool from giving plausible-but-wrong advice.

## How it works (the architecture)

- **Runtime = deterministic retrieval.** A finding type selects a reference block from these files. The model, when used at all, writes only the last-mile sentence against material it did not invent. No live scholarly calls at run time (no latency, no rate limits, no unvetted text in a trust path).
- **Build time = curation.** These files are authored and refreshed at build time. A build-time pass queries the open, keyless scholarly indexes below, Michelle vets what comes back, and the vetted claim + citation goes into the file. NotebookLM is a fine workbench for this authoring; it is not the tool's engine.
- **Versioned.** Everything here lives in git so a change to the advice is auditable.

## Free scholarly indexes for build-time refresh (no personal API key)

- OpenAlex, 250M+ works, fully open, no key. https://openalex.org · https://docs.openalex.org
- ERIC, education-specific, free API. https://eric.ed.gov/?api
- Semantic Scholar Graph API, ~200M papers, no key for basic use. https://www.semanticscholar.org/product/api
- CORE, 300M+ open-access full texts, free key. https://core.ac.uk/services/api
- Crossref REST API, metadata/DOIs, free. https://www.crossref.org/documentation/retrieve-metadata/rest-api/

## Files

- `AUTHENTIC_ASSESSMENT.md` and `ALTERNATE_ASSESSMENTS.md`, the AI-resilient substitution menu.
- `UDL_3.md`, CAST UDL 3.0 principles as checkable recommendations.
- `RSI.md`, Regular and Substantive Interaction: the regulation and documentable practices.
- `ID_MODELS.md`, instructional-design model lenses (Backward Design, ADDIE, SAM, Merrill, Dick & Carey, Gagne, connectivism).
- `BLOOMS.md`, the verb bank for measurable objectives.
- `SEAT_HOURS.md`, the credit-hour / workload math.
- `OSCQR_QM_CROSSWALK.md`, where the tool is strong vs. weak against the full rubrics (to build).
