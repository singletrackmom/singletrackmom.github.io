# AVC 183, Digital Graphic Design 1 · Course Notes

Rough planning notes. Not organized yet. Course still in development (migrating and adapting from AVC 181 Graphic Design I).

---

## Draft module idea: Brand guidelines as design tokens, applied across media (2 Aug 2026)

The insight worth teaching is not a specific tool. It is the **design-system / design-token mindset**: define the brand once (palette, type scale, spacing, logo usage), then apply those same tokens consistently everywhere. That concept is core graphic design, it spans print and web, and it is tool-durable. Tools churn; the systematic-brand-application concept does not. This is a strong "outlast the semester" lesson.

**Goal:** Students learn to express a set of brand guidelines as reusable tokens (color, type, spacing, logo rules) and apply them consistently across print, screen design, and web, understanding that each medium implements the same tokens its own way.

**Audience:** AVC 183 digital graphic design students (Digital Media Arts). Many will move between print and interactive work, so the through-line matters.

**Process / how it works:** Start from a brand guide the students build, turn it into a token set, then implement the same tokens in each medium and compare. Teach the concept first, the tools second.

### The same tokens, per medium

- **Print** applies brand tokens through Illustrator and InDesign: paragraph styles, character styles, object styles, and swatches.
- **Adobe CC Libraries** is the piece to flag for this course. It shares the same brand colors, type, and logos across every Adobe file, print and web. For graphic design students this is arguably the most directly relevant "brand tokens everywhere" tool, and they are already in the Adobe suite.
- **Figma** applies them through variables and shared styles.
- **Web** applies them through CSS custom properties (variables) or a Tailwind config.

### Where Tailwind fits (honest placement)

- Tailwind CSS is a **utility-first CSS framework**: a large library of ready-made classes (`p-4`, `text-lg`, `bg-white`) applied directly in the HTML, plus a config file that holds the brand tokens (colors, type, spacing) so the web build matches the brand guide.
- It is **one example on the web side** of the tokens lesson, not the headline. It is a front-end implementation tool, not a UX-design tool.
- **Free and open source** (MIT license). There is a paid add-on (Tailwind Plus) with pre-designed components, never required.
- **Pedagogy caution:** teach CSS fundamentals first (box model, specificity, flexbox, grid). Handing beginners Tailwind before they understand CSS trains them to paste utility classes without understanding styling. Introduce Tailwind as an intermediate piece, framed as the **design-to-development handoff**: how a design gets built by, and handed to, developers.

### Figma and Tailwind

- They do not connect natively. The bridge is the shared **design-token** idea: Figma variables (brand colors, type, spacing defined once) map to the same tokens in a Tailwind config.
- Plugins exist that try to export Figma tokens or frames into Tailwind classes, but the auto-generated code is rough. The durable link is the token concept, not a plugin.

### Open item / next step

- Run this module concept past the UX-practitioner advisory panel (same industry-validation loop used for the AVC 2xx UX course). If the panel and the AVC 183 competencies do not call for front-end frameworks, keep Tailwind out of the design course and teach the tokens concept with Adobe (styles, swatches, CC Libraries) and CSS variables instead. Do not add Tailwind just because it is popular.
- Decide whether this lives as one module or threads through the whole brand unit.

---

## Updated course objectives (draft, 2 Aug 2026)

The inherited objectives are artifact-based and dated (they literally say "design a letterhead" and "design a business card"). A modern beginning graphic design course should be **skill and competency based**, not tied to specific deliverables. Draft rewrite, students will be able to:

1. Apply the core design principles (hierarchy, contrast, alignment, proximity, repetition, balance, and white space) to build clear, intentional compositions.
2. Design with a grid, using grid systems to structure layout and create visual order.
3. Demonstrate typography fundamentals: letterform anatomy, type classification, type pairing, typographic hierarchy, and spacing (kerning, tracking, leading) for readable, expressive type.
4. Apply color theory (harmonies, contrast, and accessibility) to design work.
5. **Apply an existing brand system** from a real brand manual and design consistently within its rules (the "apply before you build" step).
6. **Build a simple brand identity** of their own (logo, palette, type system, and a short set of guidelines) and document it as a mini brand manual.
7. Source and use imagery legally, with copyright and Creative Commons literacy and correct attribution.
8. Use industry tools (Illustrator, InDesign, Photoshop) and prepare files correctly for screen and print.
9. Work through a real design process: brief, research, iteration, critique, and presentation.
10. Make accessibility-aware decisions (contrast, legibility) in their design work.

**Signature progression Michelle wants:** apply an existing brand first (hand students a finished brand manual, they design within it), then build their own brand. This teaches consistency and rationale before creative ownership. Good brand systems to apply are in the OER list below (NASA, USWDS, Mailchimp).

---

## OER to kickstart the course (verified live Aug 2026)

Curated open/free resources to build the course on, alongside the videos Michelle will make. License stated per item. "Free but all rights reserved" = free to assign by link, but NOT to copy or remix into our own materials. Only CC-licensed and public-domain items can be repackaged into a course pack.

### Design fundamentals
- **Graphic Design and Print Production Fundamentals**, BCcampus / Graphic Communications Open Textbook Collective. [opentextbc.ca/graphicdesign](https://opentextbc.ca/graphicdesign/) (also in the [Open Textbook Library](https://open.umn.edu/opentextbooks/textbooks/graphic-design-and-print-production-fundamentals)). **License: CC BY 4.0.** The anchor text: design elements and principles, composition, typography, color, with exercises and a glossary. Print-production chapters skew dated; the design/type/color fundamentals are standard and fully remixable.
- **Baseline, The Free Design Bootcamp**. [baselinehq.com](https://baselinehq.com/) (grids: [baselinehq.com/4-grid-systems.html](https://baselinehq.com/4-grid-systems.html)). **License: free but all rights reserved.** Modern self-paced modules on layout, grids, typography, and color. Link it, do not repackage.

### Typography
- **Butterick's Practical Typography**, Matthew Butterick. [practicaltypography.com](https://practicaltypography.com/). **License: free but all rights reserved.** The clearest reference on kerning/tracking/leading, type selection, hierarchy, readability. Current and maintained.
- **Kern Type (the kerning game)**, Method of Action. [type.method.ac](https://type.method.ac/). **License: free to use.** Hands-on kerning practice with scored feedback. Desktop only.
- **Shape Type (letterform game)**, Method of Action. [shape.method.ac](https://shape.method.ac/). **License: free to use.** Letterform anatomy and curve construction. Pairs with Kern Type.
- **Type Connection (typographic pairing game)**, Aura Seltzer. [typeconnection.com](https://www.typeconnection.com/). **License: free to use.** Teaches type pairing strategies. Interface is dated but pedagogically sound.
- **Thinking with Type (companion site)**, Ellen Lupton. [thinkingwithtype.com](https://thinkingwithtype.com/). **License: free but all rights reserved (the book is copyrighted, NOT OER).** Use the official free letter/text/grid explainers. Do not distribute pirated full-book PDFs.

### Grid and layout
- Covered by the two anchors: the composition/design-principles material in *Graphic Design and Print Production Fundamentals* (CC BY 4.0) plus Baseline's **Grid Systems** module ([baselinehq.com/4-grid-systems.html](https://baselinehq.com/4-grid-systems.html)). Classic Muller-Brockmann and "Making and Breaking the Grid" are NOT open-licensed, keep them as optional library reading.

### Branding and brand manuals to apply
- **NASA Graphics Standards Manual (1976, Danne & Blackburn)**. [full PDF](https://users.cs.jmu.edu/bernstdh/web/common/policies/NASA_StyleGuide_Nov06.pdf). **License: U.S. government work, effectively public domain** (the modern reissue book is copyrighted; the original manual is federal). A complete grid-and-logo system to apply as an exercise; "dated" on purpose, which makes it a great teaching artifact for consistency and rationale.
- **NASA Brand Center (current)**. [nasa.gov/nasa-brand-center](https://www.nasa.gov/nasa-brand-center/). **License: free to view.** Modern counterpart showing how a legacy identity is governed today.
- **Mailchimp Content Style Guide**. [styleguide.mailchimp.com](https://styleguide.mailchimp.com/) ([GitHub source](https://github.com/mailchimp/content-style-guide)). **License: CC BY-NC 4.0 (openly licensed).** The best open example of the voice/tone side of a brand system.
- **U.S. Web Design System (USWDS)**. [designsystem.digital.gov](https://designsystem.digital.gov/). **License: public domain (U.S. government / CC0-equivalent).** A complete, modern, openly-usable design system (color, type scale, components, accessibility). Excellent "apply an existing system" exercise and models WCAG practice. (Most universities also post brand guidelines publicly, search "[school] brand guidelines PDF" for a campus example.)

### Color
- **Adobe Color**. [color.adobe.com](https://color.adobe.com/). **License: free to use.** Interactive color wheel for harmonies and contrast/accessibility checks.
- Pair with the color chapters of *Graphic Design and Print Production Fundamentals* (CC BY 4.0) for the openly-licensed reading.

### Copyright and Creative Commons literacy
- **Creative Commons for Educators and Librarians**, Creative Commons + ALA. [certificates.creativecommons.org/cccertedu](https://certificates.creativecommons.org/cccertedu/). **License: CC BY.** Plain-language teaching material on copyright and the six CC licenses.
- **Openverse**, WordPress / Creative Commons. [openverse.org](https://openverse.org/). **License: tool is open; results are CC or public domain.** Search 800M+ openly-licensed images with one-click attribution. The practical companion to the CC lesson.

**Remix note:** only the CC BY / CC BY-NC / public-domain items (BCcampus textbook, Mailchimp, USWDS, NASA 1976 manual, CC Certificate content) can be copied and remixed into our own materials. The rest are free to assign by link only. Skip the pirated full-text PDFs of *Thinking with Type* and *Making and Breaking the Grid*, they are not open-licensed.

### Not yet done
- AVC 183 has NOT been run through the Course Dialer yet. Once the objectives above are settled, run it through to draft the module structure and assessments.
