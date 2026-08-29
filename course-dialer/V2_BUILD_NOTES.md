# Dial Your Course, v2 rebuild notes

Built overnight, 20 July 2026. This is the pick-up-here file for the rebuilt tool.

## What happened
`course-dialer/index.html` was rebuilt into the v2 shell you scoped in `V2_FUNCTIONS_MAP.md`, `prd.html` section 7, and `TECH_ARCHITECTURE.md`. The build is **additive**: the v1 audit engine (parser, all 19 deterministic checks, the workload model, the Canvas-safe restyler, and the export round-trip) is preserved intact. Everything new wraps around it.

- Your working v1 tool was backed up first to `course-dialer/index.pre-v2-rebuild.20260720-0249.bak.html`. If anything here is wrong, that file is the known-good v1.
- Style follows the **current tool look** (crimson `#C8102E`, Open Sans), not the plum portfolio, per your note. The locked site header/footer chrome (DM Sans) stays, per the design system.
- One line was added to the engine so the shell can read the parsed course (`window.__DIAL.getCourse`, `buildLive`). Nothing else in the engine changed.

## What is real and working (v1 core, no AI)
- **Cover launcher** with two doors (Build / Audit) and a section dashboard: per-section on/off toggles and status chips. Toggling a section syncs to the audit engine's check cards.
- **Build a course** (new): input-first (objectives, credits, modality, level, seat-hour profile, palette), then an outline-first gate. Generates modules sized to the outside-work budget (credits x 40, split by load and modality), each with a Bloom-checked objective (flags banned verbs), a discipline-aware grounded assessment, an activity, an RSI touchpoint (online), a UDL option, and a time-on-task note. Reorder, rename, add, delete. Exports Canvas-safe inline HTML per module and an experimental starter `.imscc`.
- **Audit a course**: the full v1 tool, unchanged. Drop a Canvas export, run the checks, approve fixes, export a dialed package.
- **Preview**: reads the course you are building, or the parsed package, in-tool without Canvas.
- **Action plan**: rolls up every flagged finding from the last audit into one prioritized checklist with fix-effort ratings, notes, and done checkboxes (the OSCQR action-plan pattern). Persists across sessions.
- **Library (RAG)**: the vetted base corpus baked in (replacement ladder, two-lane model, survive checklist, UDL, RSI), with deterministic retrieval by finding type and discipline, each suggestion carrying its sources. A "Fetch candidate sources (OpenAlex)" button pulls newer works for vetting only, never auto-added. Base library is the trust path.
- **Save / resume**: autosaves to this browser, and downloads a `.dialer` project file you can reopen or back up.
- **Settings**: institution profile, accreditation model, rubric set, competency-source link, and the AI paste-bridge panel (no key, nothing sent from the page).

## What is honestly stubbed (and why)
- **Live AI features** stay as the **paste-bridge** and locked "opt-in via bridge" rows. A credential cannot live in a static page; this is your data-sovereignty line, not a shortcut. The bridge composes a prompt from your objectives/modules for the sanctioned model.
- **Synthetic-student usability test (section E)** is not in this browser build. Running many agent sessions needs offline compute, as your own `TECH_ARCHITECTURE.md` says. It is a separate batch job, not a tab.
- **Starter `.imscc` export** is labeled experimental: import to a **sandbox** course first, then promote. It writes web-content module pages plus a manifest; it has not been round-trip tested in Canvas yet.
- **Course-level assessment (B6)** is present as a dashboard section and a build note, not yet a full guided form. It needs co-development with the campus assessment coordinator, per your July 19 note.
- **Institution settings** persist locally but are not yet wired to change every check's behavior; the ILO catalog lives at `canvas/reference/GCC_ILOs.md`.

## New skills added
- the `research-first` skill - at the start of any new build, asks whether to scan existing tools first (the thing you keep forgetting).
- the `assessment-library-refresh` skill - the build-time RAG updater that keeps `tools/reference/*.md` current from OpenAlex/ERIC, human-vetted, while the base library stays the trust path.

## To verify next (quick)
1. Open the rebuilt `index.html` and click through: Cover, Build (generate an outline), Audit (drop the AVC100 export), Preview, Action plan, Library, Settings.
2. Run the two outcomes-export tests still queued in the old `NEXT.md` (they decide how much the builder must lean on hand-entered objectives).
3. Test the experimental starter `.imscc` import into a sandbox course before trusting it.
4. Flag anything the audit reports that you know is false (the standing rule).
