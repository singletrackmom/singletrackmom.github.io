# AI Indicator

**Goal:** show students at a glance whether AI is allowed in a module or assignment, using one consistent red, yellow, green indicator across every course.
**Audience:** GCC Digital Media Arts students first; then any Maricopa faculty who want a ready-made, accessible indicator.
**Process:** research what exists (done 13 Nov 2026), decide the scale and where it sits, build it into my course build system, then offer a copy-paste version for other faculty.

Status: idea. Nothing built.

## The idea (Michelle, 13 Nov 2026)

A slider-style indicator, red to yellow to green, showing whether students can use AI for a module. It would sit in the module’s divider (the Canvas text header) or at the top of the module. The instructor sets it. If Canvas cannot host it, a snippet of HTML pasted into the top of each module page.

## What Canvas allows

| Option | Works? | Notes |
| --- | --- | --- |
| HTML in a module text header | No | Canvas text headers are plain text. HTML typed there shows as code. |
| Emoji or Unicode in a text header | Yes | 🔴 🟡 🟢 paste in fine. Cheapest version: a text header like “🟢 AI allowed: Gemini for research and feedback.” Needs words, not color alone, for accessibility. |
| HTML snippet in a Canvas page (HTML view) | Yes | Inline styles work. No JavaScript, so no live slider: the instructor picks the version with the right level already set. |
| LTI app or Canvas theme script | Only with district admin | An LTI tool or a custom theme script needs Maricopa admin approval and install. Not a faculty-level option. Park unless the ARC wants a district-wide version. |
| My course build system | Yes | Courses are generated from `canvas/<course>/course.html` by `tools/course-build/build.py`. One `data-ai` value per module or assignment could render the indicator everywhere, and `package.py` carries it into the Canvas package. No hand pasting. |

## What already exists

- **AI traffic light models** are common. Warwick’s IATL labels every assessment red, amber or green; College of Staten Island and Edutopia publish the same three-level model.
- **The AI Assessment Scale (AIAS)** by Perkins, Furze, Roe and MacVaugh: a five-level scale from no AI to full AI. University of Stirling embedded it in every Canvas module from Autumn 2025 and prompts staff to pick a level for each assessment. Ontario Tech adapted it with an icon per level placed in the assignment header (CC BY-NC-SA).
- **The 2024 AIAS revision moved away from traffic-light colors** to a neutral palette, because red and green imply some levels are bad and others good. Worth deciding before building.
- **Google Classroom** has an extension (Traffic Lite) that adds a color AI-policy widget to assignments. Nothing equivalent found for Canvas.

Nothing found that is a ready-made Canvas indicator faculty can drop into modules. The gap is real but small: the frameworks exist, the Canvas packaging does not.

## Ways it could work, simplest first

1. **Emoji text header.** A text header at the top of each module or above each assignment: “🟢 AI allowed: Gemini for research and feedback.” Five minutes per course, works today, no admin needed. Limit: plain text only, no styling.
2. **Pasted HTML block.** A styled block (icon, level word, one sentence on what is allowed) pasted into the top of a module page or assignment in HTML view. Three or five versions, one per level, kept in a snippet file. Limit: no live slider; changing a level means re-pasting.
3. **Built into my courses.** A `data-ai` value on each module or assignment in `course.html`; `build.py` renders the indicator and `package.py` carries it into Canvas. One edit changes it everywhere. Best fit for my own courses.
4. **Snippet generator for other faculty.** A small page on my site: pick the level, add one sentence, click Copy, paste into Canvas. Shares the idea across the district without anyone installing anything. Pairs well with a pitch to other digital media faculty.
5. **District version.** An LTI tool or Canvas theme script that adds the indicator to every course, set by the instructor. Needs district IT and the ARC. Only worth raising once versions 1 to 4 show students use it.

## Questions to settle, most important first

1. **Module or assignment?** My courses already state AI use per assignment (“AI comes in small pieces, each tied to one task”). Stirling, Warwick and Ontario Tech all set the level per assessment, not per module. A module can mix red and green assignments.
2. **Three colors or the AIAS levels?** Traffic light is simpler for students; AIAS is the research-backed standard and avoids the “red is bad” read.
3. **Accessibility.** Color can never carry the meaning alone (WCAG 2.1 AA): every level needs a word label and an icon or shape. Red-green is the most common color-blindness pair.
4. **Does it replace text that already exists?** Each assignment page already has an AI use section. The indicator should standardize that section, not add a second one.

## Sources

- Canvas Community, text headers do not accept HTML; Unicode works: https://community.canvaslms.com/t5/Archived-Questions/ARCHIVED-Colours-in-TEXT-HEADERS/m-p/156093
- Warwick IATL AI Traffic Light System: https://warwick.ac.uk/fac/cross_fac/iatl/sharingpractice/repository/trafficlight/
- College of Staten Island AI Use Policy, Traffic Light Model: https://www.csi.cuny.edu/sites/default/files/2026-04/College_of_Staten_Island_AI_Use%20Policy_Traffic_Light_Model.pdf
- Edutopia, A Stoplight Model for Guiding Student AI Usage: https://www.edutopia.org/article/creating-ai-usage-guidelines-students/
- University of Stirling, AI Assessment Scale in Canvas: https://learnteach.stir.ac.uk/?p=1416
- Ontario Tech, AI in Assessment Scale: https://tlc.ontariotechu.ca/nexthub/artificial-intelligence/ai-scale/
- Perkins, Roe and Furze (2024), The AI Assessment Scale Revisited: https://arxiv.org/abs/2412.09029v1
