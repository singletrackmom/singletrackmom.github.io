// Student Journey Gap Analysis, ARC committee deck, 27 Aug 2026
// Built by the research-aggregator role from PART1_FINDINGS_2026-07-27.md and PART2_RUNS_2026-08-25.md
// Palette is the study palette from airc-sss/sss.css. Solid colors only, no gradients.

const pptxgen = require("pptxgenjs");

const INK = "3A2E3F";
const PAPER = "FAF7F2";
const WHITE = "FFFFFF";
const STONE = "E2D8CE";
const MUTED = "8A7E7A";
const PLUM = "7A5080";
const PLUM_PALE = "EDE4F2";
const SAGE = "6B8F6E";
const SAGE_PALE = "E4EDE5";
const ROSE = "C4929E";
const ROSE_PALE = "F5E8EB";
const GOLD = "B8956A";
const GOLD_PALE = "FDF6EE";

const HEAD = "Cambria";
const BODY = "Calibri";

const W = 13.333;
const H = 7.5;
const M = 0.62;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "Michelle Blomberg";
pres.title = "Student Journey Gap Analysis, AI Opportunities";

function darkSlide() {
  const s = pres.addSlide();
  s.background = { color: INK };
  return s;
}
function lightSlide() {
  const s = pres.addSlide();
  s.background = { color: PAPER };
  return s;
}

// Standard content-slide header. Returns the y where content may begin.
function header(s, kicker, title, kickerColor) {
  s.addText(kicker.toUpperCase(), {
    x: M, y: 0.42, w: W - M * 2, h: 0.26,
    isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 11, bold: true, charSpacing: 1.6,
    color: kickerColor || PLUM,
  });
  s.addText(title, {
    x: M, y: 0.72, w: W - M * 2, h: 0.72,
    isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 30, bold: true, color: INK,
  });
  return 1.55;
}

function footer(s, text) {
  s.addText(text, {
    x: M, y: H - 0.52, w: W - M * 2, h: 0.28,
    isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 10, italic: true, color: MUTED,
  });
}

function card(s, opts) {
  s.addShape(pres.ShapeType.roundRect, {
    x: opts.x, y: opts.y, w: opts.w, h: opts.h,
    rectRadius: 0.06,
    fill: { color: opts.fill || WHITE },
    line: { color: opts.line || STONE, width: 0.75 },
  });
}

// Severity chip
function chip(s, x, y, label, color, w) {
  const cwid = w || 1.42;
  s.addShape(pres.ShapeType.roundRect, {
    x: x + (1.42 - cwid), y: y, w: cwid, h: 0.34, rectRadius: 0.1,
    fill: { color: color }, line: { color: color, width: 0.5 },
  });
  s.addText(label, {
    x: x + (1.42 - cwid), y: y, w: cwid, h: 0.34,
    isTextBox: true, margin: 0, align: "center", valign: "middle",
    fontFace: BODY, fontSize: 10.5, bold: true, color: WHITE,
  });
}

const tableBase = {
  fontFace: BODY, fontSize: 11.5, color: INK,
  border: [
    { type: "none" },
    { type: "none" },
    { pt: 0.75, color: STONE },
    { type: "none" },
  ],
  autoPage: false,
};
function headRow(cells) {
  return cells.map((c) => ({
    text: c,
    options: {
      bold: true, color: WHITE, fill: { color: INK },
      fontSize: 11, fontFace: BODY,
    },
  }));
}

/* ---------------------------------------------------------------- 1. Title */
{
  const s = darkSlide();
  s.addText("STUDENT SUPPORT AND SUCCESS  ·  DOMAIN 5  ·  27 AUGUST 2026", {
    x: M, y: 1.5, w: W - M * 2, h: 0.3,
    isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 12, bold: true, charSpacing: 1.8, color: ROSE,
  });
  s.addText("Where students get lost,\nand what AI can actually fix", {
    x: M, y: 1.95, w: 10.4, h: 1.9,
    isTextBox: true, margin: 0, lineSpacing: 46,
    fontFace: HEAD, fontSize: 40, bold: true, color: PAPER,
  });
  s.addText(
    "Student Journey Gap Analysis. Findings to date from synthetic-persona usability runs across all ten Maricopa colleges, ranked by severity, each tied to a service that already exists.",
    {
      x: M, y: 4.1, w: 9.4, h: 0.9,
      isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 15, color: STONE, lineSpacing: 22,
    }
  );
  s.addShape(pres.ShapeType.line, {
    x: M, y: 5.35, w: 3.2, h: 0,
    line: { color: PLUM, width: 2.25 },
  });
  s.addText("Michelle Blomberg  ·  Co-chair, Student Support and Success", {
    x: M, y: 5.6, w: 8, h: 0.3,
    isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 13, color: PAPER,
  });
  s.addText("Preliminary. Severity is tester-assigned and pending human rating.", {
    x: M, y: 5.95, w: 8, h: 0.3,
    isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 11.5, italic: true, color: STONE,
  });
  s.addNotes(
    "Frame in one line: we sent fifty synthetic students at the public websites of all ten colleges and recorded where they got stuck. Everything here is public-web only, no login, no student data. Say the word candidate out loud on severity before anyone asks."
  );
}

/* -------------------------------------------------------- 2. What this is */
{
  const s = lightSlide();
  const y = header(s, "Method", "What you are looking at, and what it is worth");

  const cols = [
    {
      t: "The corpus",
      c: [
        "Part 1, July: a top-of-funnel search sweep, 11 persona runs, and 3 end-to-end enrollment walks.",
        "Part 2, August: 13 detailed public-tier runs, two search-layer batches, three ten-college comparisons, two completed crosswalk rows.",
        "All ten colleges touched. Public web only. No login, no student data, no contact with staff.",
      ],
      fill: WHITE,
    },
    {
      t: "Two evidence tiers, kept apart",
      c: [
        "Page-opened. The tester opened the page and read it. Quotable as a claim about content.",
        "Search-layer. What a query returned. Quotable as a claim about retrieval only.",
        "The ten-college tables are retrieval evidence. They say what students find, not what pages contain.",
      ],
      fill: WHITE,
    },
    {
      t: "What the numbers are not",
      c: [
        "Severity is the Nielsen 0 to 4 scale, assigned by the tester, pending human rating. Nothing here is a confirmed district finding.",
        "The testers are AI personas, not students. This is instrument work that tells volunteer fieldwork where to look.",
        "Four first-pass claims were retracted on inspection. All four had overstated the barrier.",
      ],
      fill: GOLD_PALE,
    },
  ];

  const cw = 3.86;
  cols.forEach((col, i) => {
    const x = M + i * (cw + 0.36);
    card(s, { x: x, y: y, w: cw, h: 4.55, fill: col.fill });
    s.addText(col.t, {
      x: x + 0.28, y: y + 0.28, w: cw - 0.56, h: 0.6,
      isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 15.5, bold: true, color: INK,
    });
    s.addText(
      col.c.map((t, j) => ({
        text: t,
        options: { bullet: true, breakLine: j !== col.c.length - 1, paraSpaceAfter: 9 },
      })),
      {
        x: x + 0.28, y: y + 0.95, w: cw - 0.56, h: 3.4,
        isTextBox: true, margin: 0, valign: "top",
        fontFace: BODY, fontSize: 11.5, color: INK, lineSpacing: 15.5,
      }
    );
  });
  footer(s, "Sources: PART1_FINDINGS_2026-07-27.md, PART2_RUNS_2026-08-25.md");
  s.addNotes(
    "Lead with the limits. This buys you credibility for the next eighteen slides. The retraction line is the strongest thing on this slide, say it plainly: we found four of our own claims were wrong, we checked them in a browser, and every error had made the college look worse than it was."
  );
}

/* -------------------------------------------- 3. The finding, big and dark */
{
  const s = darkSlide();
  s.addText("THE CENTRAL FINDING", {
    x: M, y: 1.35, w: W - M * 2, h: 0.3,
    isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 12, bold: true, charSpacing: 1.8, color: ROSE,
  });
  s.addText("Retrieval matches vocabulary,\nnot need.", {
    x: M, y: 1.8, w: 11.6, h: 1.7,
    isTextBox: true, margin: 0, lineSpacing: 50,
    fontFace: HEAD, fontSize: 44, bold: true, color: PAPER,
  });
  s.addText(
    "Pages that contain the student’s word rank on the student’s query. Pages that contain only the service’s name do not.",
    {
      x: M, y: 3.75, w: 10.6, h: 0.8,
      isTextBox: true, margin: 0, lineSpacing: 26,
      fontFace: BODY, fontSize: 18, color: STONE,
    }
  );
  s.addText(
    "A student who already knows the institution’s words finds the service everywhere. A student who only knows what is wrong finds it almost nowhere. That second student is this study’s equity population.",
    {
      x: M, y: 4.85, w: 10.6, h: 0.9,
      isTextBox: true, margin: 0, lineSpacing: 22,
      fontFace: BODY, fontSize: 14.5, color: PAPER,
    }
  );
  s.addNotes(
    "This is the whole deck in two sentences. Everything after this is evidence for it or a fix built on it. Pause here."
  );
}

/* ------------------------------------------------ 4. Food, ten colleges */
{
  const s = lightSlide();
  const y = header(s, "Evidence 1 of 3", "“I ran out of food, I am hungry, need help eating”");

  s.addText("1", {
    x: M, y: y + 0.05, w: 1.5, h: 1.0,
    isTextBox: true, margin: 0, align: "center",
    fontFace: HEAD, fontSize: 62, bold: true, color: PLUM,
  });
  s.addText("of ten colleges\nreturns its food program", {
    x: M, y: y + 1.05, w: 1.9, h: 0.7,
    isTextBox: true, margin: 0, align: "center",
    fontFace: BODY, fontSize: 12, color: INK, lineSpacing: 15,
  });
  s.addText("Every one of these ten colleges runs a food program. Search the service’s own words instead (“free food for students”) and the pantries surface immediately.", {
    x: M, y: y + 1.95, w: 2.5, h: 1.6,
    isTextBox: true, margin: 0, valign: "top",
    fontFace: BODY, fontSize: 11.5, color: INK, lineSpacing: 15,
  });

  const rows = [
    headRow(["College", "What the college’s own search returned"]),
    [{ text: "Scottsdale", options: { bold: true, color: SAGE } }, { text: "Artie’s FIT Market, result 1. Works, because the page says “our hungry students.”", options: { color: SAGE } }],
    ["Chandler-Gilbert", "Zero results"],
    ["Phoenix", "Zero results"],
    ["Paradise Valley", "Zero results"],
    ["South Mountain", "Zero results"],
    ["Glendale", "One result: The Traveler, the student literary magazine"],
    ["Estrella Mountain", "Two results, both the Mariposa Literary Review"],
    ["GateWay", "One result: the Early College High School wellness policy"],
    ["Mesa", "One result: a 2018 Empty Bowls fundraiser press release"],
    ["Rio Salado", "Wellness blog posts on mindful eating and portion control"],
  ];
  s.addTable(rows, {
    x: M + 2.85, y: y, w: W - M * 2 - 2.85,
    colW: [2.4, 7.05],
    rowH: 0.325,
    ...tableBase,
  });
  footer(s, "Search-layer evidence: what the query returned. Two colleges answer a hunger query with a student literary magazine.");
  s.addNotes(
    "The literary-magazine result is the one people remember. It ranks because it is the only place on that domain where anyone writes about being hungry in the first person. The services exist. The language of need exists. They are in different documents."
  );
}

/* ---------------------------------------- 5. Emergency aid, ten colleges */
{
  const s = lightSlide();
  const y = header(s, "Evidence 2 of 3", "“I cannot pay my rent this month, I need money now”");

  s.addText("2", {
    x: M, y: y + 0.05, w: 1.5, h: 1.0,
    isTextBox: true, margin: 0, align: "center",
    fontFace: HEAD, fontSize: 62, bold: true, color: PLUM,
  });
  s.addText("of ten colleges\nreturns emergency help", {
    x: M, y: y + 1.05, w: 1.9, h: 0.7,
    isTextBox: true, margin: 0, align: "center",
    fontFace: BODY, fontSize: 12, color: INK, lineSpacing: 15,
  });
  card(s, { x: M, y: y + 1.95, w: 2.5, h: 1.75, fill: PLUM_PALE, line: PLUM });
  s.addText("Mesa’s page contains the word “rent.” The query contains the word “rent.” It still returns nothing, because the rest of the sentence does not match.", {
    x: M + 0.2, y: y + 2.12, w: 2.1, h: 1.45,
    isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 11.5, color: INK, lineSpacing: 15,
  });

  const rows = [
    headRow(["College", "What the college’s own search returned"]),
    [{ text: "South Mountain", options: { bold: true, color: SAGE } }, { text: "Verna McClain Emergency Fund. Works, because the page says “apply now.”", options: { color: SAGE } }],
    [{ text: "Glendale", options: { bold: true, color: SAGE } }, { text: "Housing and Shelter, result 1, with real numbers. The emergency fund itself never surfaces.", options: { color: SAGE } }],
    ["Chandler-Gilbert", "A 2020 news post, plus a page about what rent costs, written for international students"],
    ["Mesa", "Zero results"],
    ["Phoenix", "Zero results"],
    ["GateWay", "Zero results"],
    ["Scottsdale", "Zero results"],
    ["Paradise Valley", "An athletics conference handbook about paying annual dues, and a catalog PDF"],
    ["Estrella Mountain", "The Mariposa Literary Review again"],
    ["Rio Salado", "A financial self-care blog, the 2001-02 catalog, and an OER lesson using rent as a metaphor for interest"],
  ];
  s.addTable(rows, {
    x: M + 2.85, y: y, w: W - M * 2 - 2.85,
    colW: [2.4, 7.05],
    rowH: 0.325,
    ...tableBase,
  });
  footer(s, "Both successes work for the same reason: the page happens to contain the student’s word.");
  s.addNotes(
    "Glendale is worth naming out loud since it is your college. It works, but for an accidental reason, and the actual emergency fund still does not surface."
  );
}

/* --------------------------------------------- 6. ADHD, ten colleges */
{
  const s = lightSlide();
  const y = header(s, "Evidence 3 of 3", "“I have ADHD, what help can I get in class”");

  const rows = [
    headRow(["College", "What came back", "Names the condition?"]),
    [{ text: "Estrella Mountain", options: { bold: true, color: SAGE } }, { text: "A dedicated ADD/ADHD page, plus Learning Disabilities, Assistive Technology, Disability 101, The Law", options: { color: SAGE } }, { text: "Yes", options: { bold: true, color: SAGE } }],
    [{ text: "GateWay", options: { bold: true, color: SAGE } }, { text: "Neurodiversity SUCCESS and Sensory-Friendly Rooms, naming ADHD, autism, sensory processing", options: { color: SAGE } }, { text: "Yes", options: { bold: true, color: SAGE } }],
    ["Phoenix", "DRS page and Accommodations Requirements, with useful lead times", "No"],
    ["Paradise Valley", "Accommodations page and a student success story", "No"],
    ["Mesa", "ADHD named only on the faculty referral page", "Only to faculty"],
    ["Chandler-Gilbert", "ADHD named only when listing external psychiatric providers", "Only to refer out"],
    ["Scottsdale", "ADHD named only in alumni success stories", "Only in marketing"],
    ["South Mountain", "A news story about students who designed an ADHD app", "Only as news"],
    ["Glendale", "A library ebook for paediatricians and psychiatrists", "Only to clinicians"],
    ["Rio Salado", "Teacher-training syllabi: “strategies to use with students that have ADHD”", "Only to future teachers"],
  ];
  s.addTable(rows, {
    x: M, y: y, w: W - M * 2,
    colW: [2.1, 7.35, 2.64],
    rowH: 0.325,
    ...tableBase,
  });

  card(s, { x: M, y: y + 3.85, w: W - M * 2, h: 1.0, fill: PLUM_PALE, line: PLUM });
  s.addText(
    [
      { text: "Look at where ADHD does appear.  ", options: { bold: true } },
      { text: "Faculty referral pages. Teacher-training syllabi. Clinical ebooks. External provider lists. Alumni marketing. News items. Every one of those is written about students with ADHD rather than to them. The institutions have plenty of language for this condition. Almost none of it is addressed to the person who has it." },
    ],
    {
      x: M + 0.28, y: y + 4.0, w: W - M * 2 - 0.56, h: 0.75,
      isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 12.5, color: INK, lineSpacing: 16.5,
    }
  );
  footer(s, "22 of the 50 personas carry a disability or neurodivergence. 15 of those are suspected, undiagnosed, or undisclosed.");
  s.addNotes(
    "This is the clearest equity case in the study. The fifteen undisclosed students do not yet know they would qualify, so they would never search the word accommodations. They search the word they have."
  );
}

/* ------------------------------------------------------ 7. The mechanism */
{
  const s = lightSlide();
  const y = header(s, "Why", "The three successes explain every failure");

  const items = [
    { c: "Scottsdale, food", d: "Artie’s FIT Market ranked first because its page says “our hungry students.”" },
    { c: "Chandler-Gilbert, food", d: "Ranked because the page says “CGCC’s food pantry is called the Coyote Cupboard.”" },
    { c: "Estrella Mountain, disability", d: "Ranked because they publish a page titled ADD/ADHD." },
  ];
  const cw = 3.86;
  items.forEach((it, i) => {
    const x = M + i * (cw + 0.36);
    card(s, { x: x, y: y, w: cw, h: 1.75, fill: SAGE_PALE, line: SAGE });
    s.addText(it.c, {
      x: x + 0.26, y: y + 0.22, w: cw - 0.52, h: 0.34,
      isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 11, bold: true, charSpacing: 1.2, color: INK,
    });
    s.addText(it.d, {
      x: x + 0.26, y: y + 0.62, w: cw - 0.52, h: 1.0,
      isTextBox: true, margin: 0, valign: "top",
      fontFace: BODY, fontSize: 13, color: INK, lineSpacing: 17,
    });
  });

  s.addText("Each one contains a word the student would actually type. That is the only thing they have in common.", {
    x: M, y: y + 1.95, w: W - M * 2, h: 0.34,
    isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 13.5, italic: true, color: INK,
  });

  card(s, { x: M, y: y + 2.45, w: W - M * 2, h: 2.05, fill: WHITE });
  s.addText("The same rule explains the rest of the study", {
    x: M + 0.32, y: y + 2.65, w: W - M * 2 - 0.64, h: 0.34,
    isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 16, bold: true, color: INK,
  });
  const pairs = [
    "The MEID page answers “MEID” but not “how do I log in the first time.”",
    "Disability pages say “accommodations” but never “ADHD.”",
    "The counseling FAQ says “kept private.” The student searches “confidential.”",
    "Pantries say “Coyote Cupboard” and “Gecko Grocery” but never “hungry.”",
  ];
  s.addText(
    pairs.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i !== pairs.length - 1, paraSpaceAfter: 7 } })),
    {
      x: M + 0.32, y: y + 3.08, w: W - M * 2 - 0.64, h: 1.35,
      isTextBox: true, margin: 0, valign: "top",
      fontFace: BODY, fontSize: 13, color: INK, lineSpacing: 17,
    }
  );
  s.addNotes(
    "The point to land: nobody has to rename anything. Chandler-Gilbert solved it by writing one extra sentence that translates its own mascot name. That is the cheapest fix in the study."
  );
}

/* --------------------------------------------------- 8. Register overview */
{
  const s = lightSlide();
  const y = header(s, "The register", "Everything found so far, ranked");

  const bands = [
    { n: "5", lab: "candidate 4", sub: "Catastrophic. A student in a serious moment is stopped.", col: PLUM, pale: PLUM_PALE },
    { n: "17", lab: "candidate 3", sub: "Major. The service exists and the student does not reach it.", col: GOLD, pale: GOLD_PALE },
    { n: "12", lab: "candidate 2 and below", sub: "Minor and cosmetic. Logged, not prioritized.", col: MUTED, pale: WHITE },
  ];
  const cw = 3.86;
  bands.forEach((b, i) => {
    const x = M + i * (cw + 0.36);
    card(s, { x: x, y: y, w: cw, h: 2.15, fill: b.pale, line: b.col });
    s.addText(b.n, {
      x: x + 0.26, y: y + 0.22, w: cw - 0.52, h: 0.95,
      isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 54, bold: true, color: b.col,
    });
    s.addText(b.lab, {
      x: x + 0.26, y: y + 1.15, w: cw - 0.52, h: 0.32,
      isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 13, bold: true, color: INK,
    });
    s.addText(b.sub, {
      x: x + 0.26, y: y + 1.5, w: cw - 0.52, h: 0.55,
      isTextBox: true, margin: 0, valign: "top",
      fontFace: BODY, fontSize: 11.5, color: MUTED, lineSpacing: 15,
    });
  });

  card(s, { x: M, y: y + 2.4, w: W - M * 2, h: 2.1, fill: WHITE });
  s.addText("How to read this register", {
    x: M + 0.32, y: y + 2.6, w: W - M * 2 - 0.64, h: 0.32,
    isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 16, bold: true, color: INK,
  });
  const notes = [
    "A barrier found at nine colleges is one row, not nine. Repeats collapse and carry an instance count.",
    "Severity is the tester’s candidate rating. Where it was revised, the register carries the revision, including the four revised down.",
    "Barriers that are policy, staffing, or web-team work are marked not-AI-addressable and routed to the office that owns them. They are not carried forward as this domain’s recommendations.",
  ];
  s.addText(
    notes.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i !== notes.length - 1, paraSpaceAfter: 8 } })),
    {
      x: M + 0.32, y: y + 3.0, w: W - M * 2 - 0.64, h: 1.4,
      isTextBox: true, margin: 0, valign: "top",
      fontFace: BODY, fontSize: 12.5, color: INK, lineSpacing: 16.5,
    }
  );
  footer(s, "Grouping by the research aggregator. Individual run records remain in the Part 1 and Part 2 logs.");
  s.addNotes(
    "If someone challenges the counts, the honest answer is that the grouping is a judgment call and the raw runs are all in the logs. Do not defend the exact number, defend the ranking."
  );
}

/* ---------------------------------------- 9-13. The candidate 4 barriers */
function barrierSlide(o) {
  const s = lightSlide();
  const y = header(s, o.kicker, o.title, o.sevColor);

  chip(s, W - M - 1.42, 0.46, o.sevLabel, o.sevColor, o.sevWidth);

  const CH = 4.95; // card height, both columns

  // Left: what happens to the student
  card(s, { x: M, y: y, w: 6.05, h: CH, fill: WHITE });
  s.addText("WHAT HAPPENS TO THE STUDENT", {
    x: M + 0.3, y: y + 0.24, w: 5.45, h: 0.26,
    isTextBox: true, margin: 0, valign: "top",
    fontFace: BODY, fontSize: 10, bold: true, charSpacing: 1.4, color: o.sevColor,
  });
  s.addText(o.what, {
    x: M + 0.3, y: y + 0.58, w: 5.45, h: 1.32,
    isTextBox: true, margin: 0, valign: "top",
    fontFace: HEAD, fontSize: 14.5, color: INK, lineSpacing: 19,
  });
  s.addText("EVIDENCE", {
    x: M + 0.3, y: y + 2.0, w: 5.45, h: 0.26,
    isTextBox: true, margin: 0, valign: "top",
    fontFace: BODY, fontSize: 10, bold: true, charSpacing: 1.4, color: MUTED,
  });
  s.addText(
    o.evidence.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i !== o.evidence.length - 1, paraSpaceAfter: 7 } })),
    {
      x: M + 0.3, y: y + 2.32, w: 5.45, h: CH - 2.6,
      isTextBox: true, margin: 0, valign: "top",
      fontFace: BODY, fontSize: o.evidence.length > 4 ? 10.5 : 11.5, color: INK,
      lineSpacing: o.evidence.length > 4 ? 14 : 15.5,
    }
  );

  // Right: the intervention
  const rx = M + 6.45;
  const rw = W - M * 2 - 6.45;
  card(s, { x: rx, y: y, w: rw, h: CH, fill: o.fixPale, line: o.fixLine });
  s.addText("WHAT AI CAN DO ABOUT IT", {
    x: rx + 0.3, y: y + 0.24, w: rw - 0.6, h: 0.26,
    isTextBox: true, margin: 0, valign: "top",
    fontFace: BODY, fontSize: 10, bold: true, charSpacing: 1.4, color: o.fixLine,
  });
  s.addText(o.fixType, {
    x: rx + 0.3, y: y + 0.56, w: rw - 0.6, h: 0.32,
    isTextBox: true, margin: 0, valign: "top",
    fontFace: BODY, fontSize: 12.5, bold: true, color: o.fixLine,
  });
  s.addText(o.fix, {
    x: rx + 0.3, y: y + 0.96, w: rw - 0.6, h: 1.62,
    isTextBox: true, margin: 0, valign: "top",
    fontFace: BODY, fontSize: 12.5, color: INK, lineSpacing: 17,
  });
  if (o.guard) {
    s.addShape(pres.ShapeType.roundRect, {
      x: rx + 0.3, y: y + 2.7, w: rw - 0.6, h: 1.95, rectRadius: 0.06,
      fill: { color: WHITE }, line: { color: o.fixLine, width: 0.75 },
    });
    s.addText(
      [
        { text: o.guardLabel + "  ", options: { bold: true, color: o.fixLine } },
        { text: o.guard },
      ],
      {
        x: rx + 0.48, y: y + 2.88, w: rw - 0.96, h: 1.6,
        isTextBox: true, margin: 0, valign: "top",
        fontFace: BODY, fontSize: 11.5, color: INK, lineSpacing: 15.5,
      }
    );
  }
  if (o.footer) footer(s, o.footer);
  if (o.notes) s.addNotes(o.notes);
  return s;
}

barrierSlide({
  kicker: "Highest severity  ·  1 of 5",
  title: "A student in an unsafe moment gets a compliance PDF",
  sevLabel: "CANDIDATE 4",
  sevColor: PLUM,
  what: "She searches “something happened, I do not feel safe, report a concern, help.” Seven of nine colleges fail to return a service. Five return police pages, Clery compliance documents, catalogs, handbooks, or course syllabi.",
  evidence: [
    "Paradise Valley returns two results: the Annual Security Report PDF, and Alumni Success Stories. No CARE team, no report form, no crisis line.",
    "Glendale returns crime statistics, the Annual Security Report, and a 474-page PDF.",
    "Chandler-Gilbert and Estrella Mountain fail outright: a 110-page PDF, a catalog update, a senior-citizens class flyer, a literary magazine.",
    "Mesa and South Mountain work. South Mountain’s Office of Care and Conduct answers “Is my report confidential?” in plain words.",
  ],
  fixType: "PLUG INTO A SYSTEM ALREADY IN USE",
  fix: "Route the felt-need phrasing to the service page and the published number, on the chat surface every college site already carries. Mesa and South Mountain have already written the content. The failure is retrieval, not authorship.",
  guardLabel: "Safety rule, non-negotiable.",
  guard: "An assistant never counsels, screens, or triages a student in crisis. It routes to a human, a service page, or a published number, immediately and every time. If we cannot guarantee that, we do not deploy on this path.",
  fixPale: PLUM_PALE,
  fixLine: PLUM,
  footer: "Clery reports are legally required and the offices publishing them are doing their job. The failure is that a frightened student reaches them instead of the service.",
  notes:
    "Say the safety rule out loud before anyone asks it. This is the slide where the committee decides whether you have thought about risk. Also protect the Clery offices explicitly, you need their cooperation for fieldwork.",
});

barrierSlide({
  kicker: "Highest severity  ·  2 of 5",
  title: "MEID is the silent gatekeeper of the whole journey",
  sevLabel: "CANDIDATE 4",
  sevColor: PLUM,
  what: "Three personas walked the full enrollment funnel at three colleges. All three completed stages 1 through 7 on the public site and were stopped at exactly the same place: Register for Classes, where the Student Center demands an MEID, a password, and Duo. No one enrolled.",
  evidence: [
    "The wall is identical at Glendale, Scottsdale, and Mesa. That is the real Part 1 and Part 2 boundary, observed rather than assumed.",
    "The MEID is not created at the wall. It is created much earlier, inside the application wizard, disguised as the yes-or-no question “Do you have a Maricopa email or Student ID?”",
    "A student meets MEID as an unexplained demand at four separate stages before anything defines it.",
    "One enrollment attempt crosses four different domains, each with a different look.",
  ],
  fixType: "BUILD A TOOL, THEN PLUG IT IN",
  fix: "One plain answer, served wherever the question is asked: “You get an MEID when you apply. It is your student ID and password for everything after this.” The fact is stable, district-wide, and currently written nowhere the student is.",
  guardLabel: "Scope honesty.",
  guard: "The login wall itself is not ours to move and should not be. What is ours is that the identifier the entire journey depends on is never explained. That part is answerable today.",
  fixPale: GOLD_PALE,
  fixLine: GOLD,
  footer: "Severity 4 at Glendale and Mesa, 2 at Scottsdale, on the register stage of three end-to-end funnel walks.",
  notes:
    "Do not let this become a request to change single sign-on. The ask is one sentence of plain language, served at four moments. Cheap, district-wide, and it unblocks the whole path.",
});

barrierSlide({
  kicker: "Highest severity  ·  3 of 5",
  title: "The adult-education bridge is invisible at two colleges",
  sevLabel: "CANDIDATE 4",
  sevColor: PLUM,
  what: "A student who finished a GED and wants to start credit classes cannot find the path. At South Mountain the search returns nothing at all. At Phoenix the pathway exists, and it lives in a 2021 news post.",
  evidence: [
    "South Mountain: zero results. No Adult Education, GED, or ESL content indexed on the domain at all.",
    "Phoenix: the GED-to-credit pathway is announced in a 2021 news item describing a partnership with Rio Salado. A pathway that exists only as a news item is not findable by anyone who was not reading the news in 2021.",
    "A Spanish-language search for the same need at Phoenix returned no Spanish page at all.",
    "This is the same population at both colleges: low English literacy, working, first-generation.",
  ],
  fixType: "PLUG INTO A SYSTEM ALREADY IN USE",
  fix: "Surface the bridge as an answerable question rather than an archived announcement. The content exists and is decent. It is catalogued as news instead of as a service.",
  guardLabel: "Split the work honestly.",
  guard: "Moving that content onto a service page belongs to each college’s web team, not to this domain. Answering the question over the content wherever it currently lives is what we can do now, without waiting for anyone.",
  fixPale: GOLD_PALE,
  fixLine: GOLD,
  footer: "Two colleges, same task, same population, both unreachable.",
  notes:
    "The pattern behind this one repeats: live student processes documented only in archived news. Rio Salado’s consortium-aid page is the second confirmed instance, and it carries a banner saying it may no longer apply.",
});

barrierSlide({
  kicker: "Highest severity  ·  4 of 5",
  title: "Disability services never say the word the student has",
  sevLabel: "CANDIDATE 3 TO 4",
  sevWidth: 1.72,
  sevColor: PLUM,
  what: "Five of six colleges have solid disability-services pages that never name the conditions students actually have. A student who knows the words “DRS” and “accommodations” finds the service everywhere. A student who only knows they have ADHD finds it at one college.",
  evidence: [
    "22 of the 50 personas carry a disability or neurodivergence. 15 of those are suspected, undiagnosed, or undisclosed.",
    "Those 15 do not know they would qualify, so they would never search the word “accommodations.” They search the word they have.",
    "At Glendale the query returns a library ebook written for paediatricians and psychiatrists.",
    "Estrella Mountain organizes disability content by condition. It is the working model, inside the district, requiring no renaming.",
  ],
  fixType: "BUILD A TOOL, THEN PLUG IT IN",
  fix: "A condition-name to service mapping. ADHD, anxiety, dyslexia, autism, all resolving to Disability Resources. Estrella Mountain has already proved the approach works by writing the condition names onto a page.",
  guardLabel: "Largest reach in the study.",
  guard: "This barrier has the biggest persona exposure of anything found, and it lands hardest on the students least likely to persist through a failed search.",
  fixPale: GOLD_PALE,
  fixLine: GOLD,
  footer: "Severity rises to 4 for the undisclosed group specifically. Tested at six colleges on the crosswalk row, ten on the retrieval sweep.",
  notes:
    "If you only get one build funded this year, argue for this one. Biggest reach, clearest equity case, and a working model already exists at Estrella Mountain to copy.",
});

barrierSlide({
  kicker: "Highest severity  ·  5 of 5",
  title: "Four gates stop a refugee student from applying",
  sevLabel: "CANDIDATE 4",
  sevColor: PLUM,
  what: "A 22-year-old with a refugee background, English as a third language, and a relative interpreting the form for him is blocked at four separate points on a page that is otherwise warm and well written.",
  evidence: [
    "Identification: “The application will not be processed until the ID is uploaded.” No alternative path is named.",
    "Prior transcripts: hand-delivered, emailed, and unofficial transcripts all refused. No alternative for foreign or unobtainable records.",
    "A 48-hour expiry: start the application more than 48 hours ago and you begin again. He needs a relative to interpret it.",
    "Cost: new students default to out-of-state tuition until documents are submitted. The documentation gate is wired to the price he pays.",
    "The page is offered in English and Spanish. Nothing in Arabic or Somali.",
  ],
  fixType: "MOSTLY NOT AI-ADDRESSABLE",
  fix: "The gates are policy and belong to Admissions and district IT. We do not carry them forward as our recommendation, and we hand them to the office that owns them.",
  guardLabel: "What is answerable.",
  guard: "Three questions with answers that exist somewhere in the district and are not on the page: whether an alternative documentation path exists, what to do when prior transcripts cannot be obtained, and a warning about the 48-hour expiry before a student starts.",
  fixPale: ROSE_PALE,
  fixLine: ROSE,
  footer: "Included precisely because most of it is not ours. Naming what AI cannot fix is what makes the rest of the list credible.",
  notes:
    "This slide is deliberate. It shows the committee that we are not proposing AI for everything. It also lands a real handoff to Admissions, in the room, with evidence.",
});

/* ------------------------------------------- 14. The candidate 3 clusters */
{
  const s = lightSlide();
  const y = header(s, "Candidate 3  ·  major", "The rest, grouped by what would fix them", GOLD);

  const groups = [
    {
      t: "Vocabulary gaps",
      col: GOLD,
      pale: GOLD_PALE,
      items: [
        "“How do I log in the first time” does not return the MEID page. The jargon term does.",
        "“Confidential” does not return the counseling FAQ. It says “kept private.”",
        "Tutoring answers are trapped inside individual course syllabus PDFs.",
        "Transfer-credit age: the answer exists in one program’s nursing FAQ and nowhere a returning adult would look.",
      ],
    },
    {
      t: "State and staleness",
      col: PLUM,
      pale: PLUM_PALE,
      items: [
        "“Apply now, $500 within 48 hours” sits above “the application cycle is currently closed.” Three funds, two colleges.",
        "The best explanation of consortium aid in the district carries a banner saying it may no longer apply.",
        "Live processes documented only in archived news, now at two colleges.",
        "A publicly indexed staging subdomain is serving catalogs to students.",
      ],
    },
    {
      t: "Language and forks",
      col: SAGE,
      pale: SAGE_PALE,
      items: [
        "Four Spanish-language felt-need searches at two colleges reached nothing, including at a college publishing a full Spanish hub on that exact need.",
        "A 17-year-old must self-diagnose among four differently named programs. ACE is a scholarship at one college and a dual-enrollment variant at another.",
        "Nine-plus placement exams with no “for this program, here is your test.”",
        "“Counseling” means academic advising at some colleges and mental health at others.",
      ],
    },
  ];

  const cw = 3.86;
  groups.forEach((g, i) => {
    const x = M + i * (cw + 0.36);
    card(s, { x: x, y: y, w: cw, h: 4.5, fill: g.pale, line: g.col });
    s.addText(g.t, {
      x: x + 0.28, y: y + 0.26, w: cw - 0.56, h: 0.4,
      isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 17, bold: true, color: g.col,
    });
    s.addText(
      g.items.map((t, j) => ({ text: t, options: { bullet: true, breakLine: j !== g.items.length - 1, paraSpaceAfter: 10 } })),
      {
        x: x + 0.28, y: y + 0.78, w: cw - 0.56, h: 3.5,
        isTextBox: true, margin: 0, valign: "top",
        fontFace: BODY, fontSize: 11.5, color: INK, lineSpacing: 15.5,
      }
    );
  });
  footer(s, "All three clusters resolve to the same intervention. None requires renaming a service or rebuilding a site.");
  s.addNotes(
    "Do not read this slide aloud. Let them scan it. Your line is: seventeen major barriers, three shapes, one fix."
  );
}

/* ------------------------------------------ 15. Already deployed, critical */
{
  const s = darkSlide();
  s.addText("BEFORE ANYONE PROPOSES A BUILD", {
    x: M, y: 0.75, w: W - M * 2, h: 0.3,
    isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 12, bold: true, charSpacing: 1.8, color: ROSE,
  });
  s.addText("Two things already sit on every\ncollege site in the district", {
    x: M, y: 1.15, w: 11.4, h: 1.3,
    isTextBox: true, margin: 0, lineSpacing: 40,
    fontFace: HEAD, fontSize: 33, bold: true, color: PAPER,
  });

  const two = [
    { t: "A language selector", d: "In the header of every college site. The Spanish hubs tell students to use it: find the globe menu, choose Español, and the page translates." },
    { t: "A chat widget", d: "In the corner of every college site. A student-facing conversational surface is already deployed and already staffed or automated." },
  ];
  two.forEach((it, i) => {
    const x = M + i * 6.15;
    s.addShape(pres.ShapeType.roundRect, {
      x: x, y: 2.75, w: 5.75, h: 1.6, rectRadius: 0.06,
      fill: { color: PAPER }, line: { color: PAPER, width: 0.5 },
    });
    s.addText(it.t, {
      x: x + 0.32, y: 2.95, w: 5.1, h: 0.38,
      isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 19, bold: true, color: INK,
    });
    s.addText(it.d, {
      x: x + 0.32, y: 3.38, w: 5.1, h: 0.85,
      isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 12.5, color: INK, lineSpacing: 16,
    });
  });

  s.addText(
    [
      { text: "So the question is not whether to build a chat or a translation layer. ", options: { bold: true, color: PAPER } },
      { text: "Both exist. The question is what those surfaces are connected to, and whether a student ever reaches them. Any recommendation that starts with “build a translation layer” is proposing something the district already deployed, and it will be corrected in this room.", options: { color: STONE } },
    ],
    {
      x: M, y: 4.7, w: 11.9, h: 1.1,
      isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 15, lineSpacing: 22,
    }
  );
  s.addText("Observed directly on GateWay, South Mountain, and Mesa, and consistent with the Chandler-Gilbert and GateWay Spanish hub instructions.", {
    x: M, y: 6.05, w: 11.9, h: 0.5,
    isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 11, italic: true, color: STONE,
  });
  s.addNotes(
    "This slide saves you from the most likely objection, which is that someone already bought a chatbot. Yes. That is the point. We are proposing what to connect it to."
  );
}

/* ---------------------------------------------------- 16. The recommendation */
{
  const s = lightSlide();
  const y = header(s, "The recommendation", "A vocabulary-to-service map, and one place to plug it in");

  card(s, { x: M, y: y, w: 5.35, h: 4.35, fill: WHITE });
  s.addText("What it contains", {
    x: M + 0.3, y: y + 0.26, w: 4.75, h: 0.36,
    isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 17, bold: true, color: INK,
  });
  const contains = [
    "Felt-need phrases to service names. “I’m hungry” resolves to Coyote Cupboard, Gecko Grocery, Mesa Market, Artie’s FIT Market, Puma Pantry, The Village.",
    "Condition names to services. ADHD, anxiety, dyslexia, autism all resolve to Disability Resources.",
    "Plain words to institutional terms. Confidential to private. Log in to MEID. Rent to emergency assistance.",
  ];
  s.addText(
    contains.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i !== contains.length - 1, paraSpaceAfter: 11 } })),
    {
      x: M + 0.3, y: y + 0.75, w: 4.75, h: 3.4,
      isTextBox: true, margin: 0, valign: "top",
      fontFace: BODY, fontSize: 12.5, color: INK, lineSpacing: 17,
    }
  );

  const steps = [
    { n: "1", t: "Build the map", d: "The felt-need phrases are already collected. This study produced them as a by-product of every run.", col: GOLD },
    { n: "2", t: "Test it for free", d: "Run those phrases against each college’s own site search. No new content, no renaming, no rebuild. This is the pilot, and it costs a person a week.", col: PLUM },
    { n: "3", t: "Plug it into the surface that exists", d: "Connect the map to the chat widget already on every college site, with crisis paths routed to humans and published numbers.", col: SAGE },
  ];
  const sx = M + 5.75;
  const sw = W - M * 2 - 5.75;
  steps.forEach((st, i) => {
    const yy = y + i * 1.56;
    card(s, { x: sx, y: yy, w: sw, h: 1.24, fill: WHITE });
    s.addShape(pres.ShapeType.roundRect, {
      x: sx + 0.28, y: yy + 0.3, w: 0.62, h: 0.62, rectRadius: 0.31,
      fill: { color: st.col }, line: { color: st.col, width: 0.5 },
    });
    s.addText(st.n, {
      x: sx + 0.28, y: yy + 0.3, w: 0.62, h: 0.62,
      isTextBox: true, margin: 0, align: "center", valign: "middle",
      fontFace: HEAD, fontSize: 20, bold: true, color: WHITE,
    });
    s.addText(st.t, {
      x: sx + 1.08, y: yy + 0.22, w: sw - 1.4, h: 0.34,
      isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 16, bold: true, color: INK,
    });
    s.addText(st.d, {
      x: sx + 1.08, y: yy + 0.56, w: sw - 1.4, h: 0.62,
      isTextBox: true, margin: 0, valign: "top",
      fontFace: BODY, fontSize: 11.5, color: INK, lineSpacing: 15,
    });
  });
  footer(s, "Nothing gets renamed. No page gets rebuilt. Three colleges already solved a piece of this by accident, simply by writing a student’s word onto a page.");
  s.addNotes(
    "Step two is the ask. It is nearly free, it is measurable, and it produces a number you can bring back to this committee: how many of our own students’ words find our own services."
  );
}

/* ----------------------------------------------- 17. Working models, wins */
{
  const s = lightSlide();
  const y = header(s, "Credit where it is due", "Working models already inside the district", SAGE);

  const wins = [
    { c: "Chandler-Gilbert", t: "The self-translating sentence", d: "“CGCC’s food pantry is called the Coyote Cupboard.” The plain word and the brand name in one sentence, so the plain-need search matches." },
    { c: "Estrella Mountain", t: "Disability by condition", d: "A dedicated ADD/ADHD page, plus Learning Disabilities, Assistive Technology, Disability 101. Organized the way students search." },
    { c: "Mesa", t: "The student’s question as the heading", d: "“Why was I selected for Verification?” Not “Verification Requirements.” One short video per sub-step, and the reassurance that 30 percent are selected." },
    { c: "South Mountain", t: "Real numbers, stated early", d: "Actual disbursement dates, ACH refunds in 3 to 5 business days, and “All GPAs welcome, FAFSA is not required.”" },
    { c: "Phoenix and Scottsdale", t: "On-site search that does the synonym work", d: "“Scholarships without a social security number” returns the Dreamers and DACA page first. “How many credits to keep my visa” returns the F-1 page first." },
    { c: "District-wide", t: "Transcripts, done consistently", d: "All colleges route through Parchment, all state $5, all give a phone number. District consistency already works here." },
  ];

  const cw = 3.86;
  const ch = 2.1;
  wins.forEach((wn, i) => {
    const col = i % 3;
    const row = Math.floor(i / 3);
    const x = M + col * (cw + 0.36);
    const yy = y + row * (ch + 0.3);
    card(s, { x: x, y: yy, w: cw, h: ch, fill: SAGE_PALE, line: SAGE });
    s.addText(wn.c.toUpperCase(), {
      x: x + 0.26, y: yy + 0.2, w: cw - 0.52, h: 0.26,
      isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 9.5, bold: true, charSpacing: 1.2, color: SAGE,
    });
    s.addText(wn.t, {
      x: x + 0.26, y: yy + 0.48, w: cw - 0.52, h: 0.6,
      isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 14.5, bold: true, color: INK, lineSpacing: 18,
    });
    s.addText(wn.d, {
      x: x + 0.26, y: yy + 1.06, w: cw - 0.52, h: 0.92,
      isTextBox: true, margin: 0, valign: "top",
      fontFace: BODY, fontSize: 11, color: INK, lineSpacing: 14.5,
    });
  });
  s.addNotes(
    "Naming the colleges that solved something protects the relationship with the ones that have not. Every one of these is a copyable pattern, not a compliment."
  );
}

/* ------------------------------------------------- 18. What we are not claiming */
{
  const s = lightSlide();
  const y = header(s, "Honesty", "What this study is not claiming", ROSE);

  card(s, { x: M, y: y, w: 6.05, h: 4.3, fill: ROSE_PALE, line: ROSE });
  s.addText("Four claims we retracted", {
    x: M + 0.3, y: y + 0.26, w: 5.45, h: 0.38,
    isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 17, bold: true, color: INK,
  });
  s.addText("All four came from reading a search summary instead of opening the page. All four had overstated the barrier.", {
    x: M + 0.3, y: y + 0.72, w: 5.45, h: 0.55,
    isTextBox: true, margin: 0, valign: "top",
    fontFace: BODY, fontSize: 12, italic: true, color: INK, lineSpacing: 16,
  });
  const retractions = [
    "GateWay’s EMT page does state its cost, length, location, and that it is not financial-aid eligible. Severity revised from 3 down to 1.",
    "Mesa’s verification page is not weak. It is one of the best pages in the study.",
    "The claimed JavaScript render defect was our own extraction failing, which also removes the second instance we reported in Part 1.",
    "One run inverted completely: the student fails on Google and succeeds on the college’s own search, using identical words.",
  ];
  s.addText(
    retractions.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i !== retractions.length - 1, paraSpaceAfter: 9 } })),
    {
      x: M + 0.3, y: y + 1.35, w: 5.45, h: 2.75,
      isTextBox: true, margin: 0, valign: "top",
      fontFace: BODY, fontSize: 12, color: INK, lineSpacing: 16,
    }
  );

  const rx = M + 6.45;
  const rw = W - M * 2 - 6.45;
  card(s, { x: rx, y: y, w: rw, h: 4.3, fill: WHITE });
  s.addText("Limits we are stating up front", {
    x: rx + 0.3, y: y + 0.26, w: rw - 0.6, h: 0.38,
    isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 17, bold: true, color: INK,
  });
  const limits = [
    "The testers are AI personas, not students. This locates barriers for volunteer fieldwork. It does not replace it.",
    "Severity is tester-assigned and pending human rating. Nothing here is a confirmed district finding.",
    "The ten-college tables are one query phrasing per cell. They demonstrate a mechanism. They are not a survey.",
    "Top-of-funnel search runs used a non-Arizona search environment. Ranking observations there are flagged for an Arizona re-run.",
    "Everything is public web. Nothing behind a login has been tested yet.",
  ];
  s.addText(
    limits.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i !== limits.length - 1, paraSpaceAfter: 9 } })),
    {
      x: rx + 0.3, y: y + 0.78, w: rw - 0.6, h: 3.3,
      isTextBox: true, margin: 0, valign: "top",
      fontFace: BODY, fontSize: 12, color: INK, lineSpacing: 16,
    }
  );
  s.addNotes(
    "Volunteer this slide, do not wait to be asked. A study that names its own errors is much harder to dismiss than one that does not."
  );
}

/* ----------------------------------------------------------- 19. Next phase */
{
  const s = lightSlide();
  const y = header(s, "Next", "What the logged-in phase opens up");

  card(s, { x: M, y: y, w: W - M * 2, h: 1.15, fill: PLUM_PALE, line: PLUM });
  s.addText(
    [
      { text: "Everything in this deck stops at the same door. ", options: { bold: true } },
      { text: "Three funnel walks at three colleges all ended at Register for Classes, blocked by a login the student does not have. Every barrier we have found so far is one a student hits before we have any relationship with them at all." },
    ],
    {
      x: M + 0.32, y: y + 0.24, w: W - M * 2 - 0.64, h: 0.75,
      isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 13.5, color: INK, lineSpacing: 18,
    }
  );

  const next = [
    { t: "What we test next", d: "The journey behind the login: registration, aid status, holds, the portal, and the moment a student drops a class without knowing what it does to their aid." },
    { t: "What we need to do it", d: "Authorization for logged-in testing, a test-account path that touches no real student data, and the tri-chairs’ sign-off on scope, the same way Part 1 was cleared." },
    { t: "What we would bring back", d: "The same register, extended past the wall, plus a measured baseline: how many of our students’ own words reach our own services today." },
  ];
  const cw = 3.86;
  next.forEach((n, i) => {
    const x = M + i * (cw + 0.36);
    const yy = y + 1.45;
    card(s, { x: x, y: yy, w: cw, h: 2.85, fill: WHITE });
    s.addText(n.t, {
      x: x + 0.28, y: yy + 0.26, w: cw - 0.56, h: 0.6,
      isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 16, bold: true, color: INK, lineSpacing: 20,
    });
    s.addText(n.d, {
      x: x + 0.28, y: yy + 0.92, w: cw - 0.56, h: 1.75,
      isTextBox: true, margin: 0, valign: "top",
      fontFace: BODY, fontSize: 12.5, color: INK, lineSpacing: 17,
    });
  });
  s.addNotes(
    "Be specific about the ask: authorization, a test-account path, tri-chair sign-off on scope. Do not leave with a vague yes."
  );
}

/* ------------------------------------------------------------- 20. The ask */
{
  const s = darkSlide();
  s.addText("WHAT I AM ASKING FOR TODAY", {
    x: M, y: 0.95, w: W - M * 2, h: 0.3,
    isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 12, bold: true, charSpacing: 1.8, color: ROSE,
  });
  s.addText("Three decisions", {
    x: M, y: 1.35, w: 10, h: 0.85,
    isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 38, bold: true, color: PAPER,
  });

  const asks = [
    { n: "1", t: "Approve the free pilot", d: "Run the felt-need phrase list against each college’s own site search and report the number back to this committee. One person, about a week, no procurement." },
    { n: "2", t: "Name an owner for the map", d: "The vocabulary-to-service map is a district asset, not a college project. It needs a home before it becomes ten inconsistent spreadsheets." },
    { n: "3", t: "Authorize the logged-in phase", d: "Scope sign-off from the tri-chairs, and a test-account path that touches no real student data." },
  ];
  asks.forEach((a, i) => {
    const yy = 2.5 + i * 1.35;
    s.addShape(pres.ShapeType.roundRect, {
      x: M, y: yy, w: 0.7, h: 0.7, rectRadius: 0.35,
      fill: { color: PLUM }, line: { color: PLUM, width: 0.5 },
    });
    s.addText(a.n, {
      x: M, y: yy, w: 0.7, h: 0.7,
      isTextBox: true, margin: 0, align: "center", valign: "middle",
      fontFace: HEAD, fontSize: 22, bold: true, color: PAPER,
    });
    s.addText(a.t, {
      x: M + 0.95, y: yy - 0.02, w: 11.1, h: 0.4,
      isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 20, bold: true, color: PAPER,
    });
    s.addText(a.d, {
      x: M + 0.95, y: yy + 0.4, w: 11.1, h: 0.62,
      isTextBox: true, margin: 0,
      fontFace: BODY, fontSize: 13, color: STONE, lineSpacing: 17,
    });
  });

  s.addText("Nothing gets renamed. No site gets rebuilt. Every fix runs over content that already exists.", {
    x: M, y: 6.55, w: 11.9, h: 0.4,
    isTextBox: true, margin: 0,
    fontFace: BODY, fontSize: 14, italic: true, color: ROSE,
  });
  s.addNotes(
    "Close on the last line. It is the reason this is fundable and the reason no office in the room has to defend itself."
  );
}

const OUT = "/sessions/nice-optimistic-hawking/mnt/singletrackmom.github.io/airc-sss/export/out/Student_Journey_AI_Opportunities_2026-08-27.pptx";
pres.writeFile({ fileName: OUT }).then(() => console.log("WROTE " + OUT));
