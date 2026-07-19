# Dial Your Course, competitive landscape scan

Run July 19, 2026. Fanned out across the Canvas LTI ecosystem, native LMS roadmaps, AI-native startups, and conference/academic work, then fact-checked the claims. This builds on V2_RESEARCH_LANDSCAPE.md; it does not repeat the accessibility/rubric neighbors already logged there (Ally, UDOIT, YuJa, DesignPLUS, OSCQR, QM, OLC, Coursetune, Simple Syllabus).

## Bottom line
Your open lane is real, but it is narrower than "nobody does both," so state it precisely.

Almost every tool sits in one of two camps: AI builders that generate a course but do no compliance audit, or auditors that review a course but do not build. The one exception is CourseAgent, which does both build and a light "six-layer audit." But its audit checks generic quality (coherence, inclusive language, basic accessibility) of courses it generated itself. It does not import an existing course, and it names no real framework, no WCAG level, no Quality Matters, no OSCQR, no credit-hour, no RSI. So the honest differentiation is not "we do both." It is this specific bundle that no one else has: audit an existing, imported course, against real compliance frameworks, LMS-agnostic, data-sovereign, and free.

## Who does what

| Tool | Camp | What it does | Audit / Build / Both | LMS | Cost | AI | Link |
|---|---|---|---|---|---|---|---|
| CourseAgent | Both (shallow audit) | Authors courses from docs/URLs; "six-layer audit" of its own output (coherence, inclusive language, accessibility), no named framework, no import | Both | Agnostic (SCORM export) | Paid (trial) | Yes | courseagent.ai/features-ai-authoring |
| OLC Course Review Assistant GPT | Audit | Ingests full unzipped LMS exports (Canvas, D2L, Moodle, Blackboard), scores vs the OLC Scorecard's 50 objectives, acts as a peer coach. OLC framework only; needs ChatGPT | Audit | Agnostic (via export) | Free-ish (needs ChatGPT) | Yes | onlinelearningconsortium.org/olc-insights/2025/06/course-review-assistant-gpt |
| CourseMagic | Build | AI course builder "for any LMS," aligns activities to outcomes, exports Common Cartridge (.imscc) | Build | Agnostic | Paid | Yes | coursemagic.ai |
| EduGears AI | Build | Breaks a syllabus into structured lessons + quizzes/slides; 22-tool LTI content platform | Build | Agnostic (LTI) | Paid | Yes | lti.edugears.ai |
| Coursebox AI | Build | Generates a full course from a prompt/document; own LMS, AI grading, rubric gen | Build | Own LMS + export | Paid | Yes | coursebox.ai |
| Instructure IgniteAI | Build components | Rubric Generator from outcomes; experimental "LLM-Enabled Assignment" for authentic assessment; content gen | Build (components) | Canvas-locked | Paid (Canvas) | Yes | prnewswire.com IgniteAI release |
| Intelligent Insights | Neither | Canvas analytics/reporting, not course design | n/a | Canvas-locked | Paid | Yes | instructure.com Intelligent Insights |
| Blackboard AI Design Assistant | Build | Generates structure, prompts, rubrics, test questions; accessibility handled separately by Ally | Build | Blackboard-locked | Paid | Yes | help.anthology.com AI Design Assistant |
| D2L Lumi | Build + partial align | Generates materials/quizzes; automated Bloom's tagging + outcome alignment | Build (+align) | Brightspace-locked | Paid | Yes | d2l.com/lumi |
| Cidi Labs DesignPLUS | Design | Canvas-only design toolset (LTI + Canvas API) | Build/design | Canvas-locked | Paid | Partial | cidilabs.com |
| ASU Learning Objectives Consultant | Build (narrow) | Drafts measurable objectives from inputs; explicitly does NOT validate curriculum or institutional standards | Build (slice) | Agnostic | Free (ASU) | Yes | ai.asu.edu learning-objectives-consultant |

## Where you are genuinely differentiated
No competitor bundles all of these, and that is the real story:
- Audits an EXISTING, imported course (CourseAgent only audits its own output; the builders do not audit at all).
- Against real, named frameworks together: WCAG 2.1 AA, Quality Matters, OSCQR, OLC, credit-hour/seat-time, RSI, and authentic/AI-resistant assessment. OLC's GPT is the only serious auditor and it covers only the OLC scorecard.
- LMS-agnostic AND data-sovereign (no student data, no personal API keys). The strongest incumbents (IgniteAI, Lumi, DesignPLUS, Ally) are all locked to one LMS.
- Free.

## Gaps worth considering (features competitors ship that you do not, yet)
- A shipped AI rubric generator tied to outcomes (IgniteAI, Coursebox, Blackboard, CourseAgent all have one).
- An embedded/interactive authentic-assessment mechanism, not just design guidance (Canvas's experimental LLM-Enabled Assignment).
- Quiz / question-bank generation during the build step (EduGears, Coursebox, Lumi, Blackboard).
- Automated Bloom's Taxonomy tagging (Lumi).
None of these are required to hold your lane; they are the obvious "table stakes" additions if you want the build side to feel as complete as the incumbents.

## Look at these first
1. CourseAgent (courseagent.ai) - the only other tool that claims both. Confirm firsthand how shallow its audit really is; it both validates your lane and is your nearest threat.
2. OLC Course Review Assistant GPT - the closest thing to your audit half. Try it on a real export; it is the bar your audit has to clear and beat on framework breadth.
3. CourseMagic (coursemagic.ai) - closest LMS-agnostic builder with the same Common Cartridge posture as you.
4. Instructure IgniteAI - the incumbent whose roadmap most overlaps your assessment/alignment features and could commoditize them. Watch it.
5. Coursebox (coursebox.ai) - the leading AI-native builder startup.

## Honest caveats
- Most capability claims come from vendor marketing, not independent benchmarks. Treat features as "advertised," not proven.
- The conference-presentation angle (EDUCAUSE, OLC, QM Connect, DT&L, WCET) did NOT surface solid verified findings, so pre-product academic work is a real coverage gap. Two academic sources did appear and are worth a look: an Ohio State "AI-Resistant Assessment Creation Tool" and a QM handout, "Using Generative AI to Ensure Course Objective Alignment." So people ARE presenting alignment/assessment tooling at QM, even if nothing productized matches you.
- On your hunch that nobody is doing synthetic-student course testing: this scan did not find anyone doing it, which supports you, but the conference angle was thin, so treat "nobody does synthetic students" as plausible and still unconfirmed. That is the one angle worth a dedicated follow-up.
- Fast-moving space. IgniteAI's rubric generator is Dec 2025; Canvas's authentic-assessment feature is experimental. Re-check the incumbents before any big claim in a talk.

## Sources
- courseagent.ai/features-ai-authoring
- onlinelearningconsortium.org/olc-insights/2025/06/course-review-assistant-gpt
- coursemagic.ai/integration/canvas
- lti.edugears.ai
- coursebox.ai
- prnewswire.com IgniteAI release (Dec 2025)
- instructure.com Intelligent Insights press release
- help.anthology.com Blackboard AI Design Assistant
- d2l.com/lumi
- cidilabs.com
- ai.asu.edu learning-objectives-consultant
- Ohio State AI-Resistant Assessment Creation Tool; QM "Using Generative AI to Ensure Course Objective Alignment" handout

---

## Correction (July 19): OLC and OSCQR are one family
The original scan implied OLC's auditor covers "only the OLC scorecard, not OSCQR." That is wrong. OSCQR is now stewarded by OLC and branded as part of the OLC Quality Scorecard Suite ("OLC Quality Scorecard Suite: OSCQR Course Design Review"). SUNY created it; OLC maintains it. So OSCQR and the OLC scorecard are the same family, not separate camps.

That makes OLC the most consolidated player on the AUDIT side, with two things, not one:
- The OSCQR review dashboard (oscqr.suny.edu): a MANUAL tool. A human reviewer scores all ~50 standards by hand and it generates an action plan. It does not scan the course automatically.
- The OLC Course Review Assistant GPT: a single-framework chatbot inside ChatGPT.

Differentiation still holds, and this sharpens how to say it. Do NOT claim "nobody audits against OSCQR" (OLC does). DO claim: automated instead of manual, many frameworks instead of one (WCAG technical scan + QM + OSCQR/OLC + credit-hour + RSI + authentic assessment), LMS-agnostic, data-sovereign (not inside ChatGPT), and audit + build in one place. Neither OLC tool does a technical WCAG scan, checks seat-time/credit-hour, or builds.

Strategic note: OLC is on the IP plan's "connectors, not buyers" list. So OLC is simultaneously the closest audit competitor AND a potential stage/partner. Presenting at OLC or aligning the tool to the OSCQR rubric they champion could be distribution, not rivalry. Same IP caution as any partner applies: protect the vision (ownership confirmed, NDA, disclosure timing) before showing the whole roadmap.

Sources: OLC Quality Scorecard Suite OSCQR PDF (s29068.pcdn.co/wp-content/uploads/qss-online-course-quality-review-rubric-oscqr.pdf); oscqr.suny.edu; onlinelearningconsortium.org/quality/scorecards/course-review
