# Dial Your Course · Technical architecture

How the whole thing actually works, spelled out so the back end is visible. v1 first (no AI, the full stack), then the v2 AI layer added on top. Written 19 July 2026.

## Design principles (these drive every choice below)
1. **Browser-first, no server for v1.** Everything runs client-side, in the user's browser. No backend to host, no database to secure.
2. **No course data leaves the machine.** Fits the data-sovereignty line. The course is read, edited, previewed, and exported all locally.
3. **No login for v1.** Save/resume is a file the user owns, not an account. (Revisit only if collaboration is ever needed.)
4. **AI is opt-in, never required.** v1 is fully useful with zero AI and zero API key.
5. **One source of truth: the course JSON.** Every module reads and writes the same in-memory course object.

---

## v1 architecture (no AI)

### 1. Platform and hosting
- A static web app: HTML + CSS + vanilla JavaScript. No build step required, no framework needed. (A light library like Preact/Alpine is optional if the UI grows, not required.)
- Hosted free on GitHub Pages (the existing `singletrackmom.github.io`), or any static host. Nothing server-side.
- Runs entirely in the browser tab. Closing the tab loses nothing that has been saved to a project file (see State).

### 2. The course data model (the core)
- A single JSON object is the whole course: metadata, modules, pages, assignments, objectives, due dates, seat-time estimates, per-module check results, and per-module status (not started / in progress / passed / has reds).
- Every module, the preview, and the export all read and write this one object. Nothing else is the source of truth.
- This is what makes "work in pieces, save as you go" possible: state is just this object, serialized.

### 3. Ingestion (reading a course in) - LMS-independent
- **Canvas .imscc (Common Cartridge):** it is a ZIP. Unzip in-browser with **JSZip**, parse `imsmanifest.xml` and the module HTML/XML with the browser's built-in **DOMParser**, map into the course JSON.
- **Word (.docx):** parse client-side with **mammoth.js** into HTML, then into the JSON.
- **Google Doc / plain syllabus:** exported file uploaded, or text pasted/embedded, parsed into the JSON.
- All parsing happens in the browser. no upload to any server.

### 4. The modules (each its own tool, all deterministic)
Each module is a JS function that takes the course JSON and returns findings and/or edits. No AI in v1.
- **Syllabus checker:** rule-based checks against the required-elements list from Institution Settings.
- **Seat-time / seat-hours:** compute estimated time per assignment with the workload formula (already built), inject the "Time-on-task note" component.
- **Dates:** compute or shift due dates; produce a dates change-list.
- **Objectives / alignment:** map tasks to objectives entered by hand in builder mode (see the outcomes note).
- **Accessibility:** parse the module HTML and flag WCAG issues deterministically (missing alt text, heading order, link text, color-contrast values).
- **OSCQR + learning-science / ID checks:** checklist evaluation against the OSCQR rubric and the grounding corpus.
- **Course-level assessment (B6) and RSI (B7):** guided forms that write structured entries into the JSON.

### 5. State, save, and resume
- The project state is the course JSON plus per-module status.
- **Durable save = download a project file** (`.json` or a named `.dialer` file) the user keeps. **Resume = reopen that file** (file picker), the tool loads the JSON. Portable, no server, user owns it.
- **Convenience autosave = browser IndexedDB** (or localStorage for small state) so a reopened tab restores the last session on the same machine. The downloadable file is the real backup. (This is a real hosted tool, so browser storage is available, unlike a sandboxed preview.)

### 6. Preview (v1, no AI)
- Render the course JSON, or just one section, as readable HTML in the tab. This is the "read it without uploading to Canvas" feature. Pure rendering, targeted to whatever section you ask for.

### 7. Export (the "give me the final file" button, available anywhere)
- Rebuild a valid **.imscc** from the course JSON: generate module HTML, write `imsmanifest.xml`, zip with **JSZip**, trigger a browser download. The user imports it into Canvas.
- Also export a readable **HTML** or **PDF** and a **Word** file for non-Canvas use.
- Because the tool holds the whole course, it can always emit a complete package even if only one module was touched. you export a snapshot, never hand-assembled pieces.
- **Change classifier:** the tool tags each change as "apply directly in Canvas" (due dates, via Canvas's bulk date tool) vs "needs a package re-import" (structural: pages, order, alignment), so the user only re-imports when structural changes justify it.

### 8. Institution settings / CTLE layer
- A separate settings JSON (syllabus rules, accreditation model, OSCQR set, institutional learning outcomes, competency-source link). Modules read it.
- Created once by a CTLE overseer and shared as a settings file, so faculty inherit the right rules without entering them.

### 9. Reference / research repository (v1 = static)
- The grounding corpus already in `tools/reference/` (OSCQR, authentic assessment, Bloom's, seat-hours, RSI, UDL, ID models) is bundled as static data and shown on demand ("give me more on improving my assessments"). No AI needed to display it.

### v1 libraries (all client-side, no server)
- **JSZip** (unzip/zip .imscc), **mammoth.js** (.docx), built-in **DOMParser** (XML/HTML), the browser **download API** / FileSaver (save files), **IndexedDB** (autosave). That is the whole dependency list. No backend, no framework mandatory.

### v1 data flow, in one line
Upload a course file → parse to course JSON in-browser → run modules on the JSON → preview/read in-tab → save the JSON as a file whenever → export a full .imscc when ready → import to a sandbox Canvas course → promote to live.

---

## v2 AI enhancements (layered on top, opt-in)

v2 changes nothing structural. it reveals a deeper layer inside the same modules once an AI connection is present.

### AI connection (the one real architecture question)
Putting an API key in browser JavaScript exposes it publicly (this is exactly the CopaMigo key-exposure bug). So AI cannot just call a model from the browser with a shared key. Two safe options:
- **Paste-bridge (pilot, zero backend):** the tool builds the prompt, the user pastes it into the sanctioned district model, pastes the result back. No key anywhere, no data sent by the tool, no backend. Slower but fully data-sovereign.
- **Thin key-only proxy (to scale):** a tiny serverless function holds the district key and forwards requests. It stores NO course data, it only relays. This is the smallest possible backend, added only for AI convenience, and only with district blessing. Never Michelle's personal key.

### Per-module AI features (each module's "with the AI plug-in" layer)
- Syllabus: draft the required narrative from the course.
- Authentic-assessment alignment: evaluate the reds and yellows and suggest redesigns, grounded by retrieval from the research repository.
- Course-level assessment: draft the competency narrative, suggest survey questions aligned to objectives, summarize returned survey data into "what to improve."
- RSI: evaluate the described approach and suggest specifics.
- Objectives: suggest objective phrasings (still authored by the faculty member).

### Research-repository updater agent (offline, not in the browser)
- A build-time agent/skill that periodically pulls new scholarship from open indexes (OpenAlex, ERIC) for human vetting, then updates the static corpus the tool ships. Runs offline, on a schedule. never in the user's tab.

### Student-agent usability test (v2, the one piece that needs real compute)
- Demographic-trained synthetic students run the course and report where a real student would struggle (modeled on WGU and the `airc-sss/` study). Running many agent sessions is beyond a browser tab, so this is a separate offline/batch job the user opts into, not client-side. Honest: this is the only part that needs compute outside the browser.

---

## Honest constraints and open decisions
1. **AI key security forces a choice:** paste-bridge (no backend) or a tiny key-only proxy (minimal backend, no data storage). v1 sidesteps this entirely by needing no AI.
2. **The synthetic-student test needs offline compute.** Everything else is browser-only.
3. **Outcomes writeback is untested, not broken.** Only one Canvas test was run. Next step: create outcomes in the builder, export, and test whether builder-created outcomes import to Canvas correctly (NEXT.md task #1). Until then, alignment uses hand-entered objectives.
4. **Save is file-based by default.** IndexedDB autosave is per-browser; the portable backup is the downloadable project file. No account, no server, on purpose.
5. **Lovable / a backend app is deferred.** A React+backend build (e.g. Lovable) would add server-stored data and lock-in against the data-sovereignty line. Only revisit if logins/collaboration become a real requirement.
