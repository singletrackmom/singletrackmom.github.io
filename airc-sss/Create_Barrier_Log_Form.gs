/**
 * Maricopa Student Journey UX Study — Barrier Log
 * One-click builder for the Google Form + linked response Sheet.
 *
 * HOW TO USE (about 2 minutes):
 *   1. Go to script.google.com and sign in with the account you want the form on
 *      (your personal Gmail OR your gccaz account — either works).
 *   2. New project → delete the sample code → paste ALL of this in → Save.
 *   3. Click Run ▶ on  createBarrierLogForm  → Review permissions → Allow.
 *   4. Open the Execution log (or View ▶ Logs). It prints three links:
 *        • FORM TO FILL OUT  → share this with one rep per college
 *        • FORM TO EDIT      → tweak wording if you want
 *        • RESPONSES SHEET   → your live Barrier Log data
 *   5. Testers log ONE task per submission, then click "Submit another response".
 */
function createBarrierLogForm() {
  var form = FormApp.create('Maricopa Student Journey UX Study — Barrier Log');
  form.setDescription(
    'Log ONE task per submission. Stay in character as the persona. '
    + 'Record what they ACTUALLY did, not where they "should" go. '
    + 'No student PII — initials only. Click "Submit another response" for the next task.');
  form.setCollectEmail(false);
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(true);
  form.setProgressBar(false);

  // ---------- SECTION 1: About this run (top of the form) ----------
  form.addSectionHeaderItem()
      .setTitle('About this run')
      .setHelpText('Fill these in after you log in as the persona, before you start the task.');

  form.addListItem()
      .setTitle('College')
      .setHelpText('Where this task is happening. For a swirl task (S1–S4), choose the SECOND college.')
      .setChoiceValues(['CGCC','EMCC','GateWay','GCC','MCC','PVCC','Phoenix College','Rio Salado','SCC','SMCC'])
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('Persona')
      .setChoiceValues([
        'A — Marisol (first-gen, workforce/nursing)',
        'B — Darnell (returning adult, business transfer; swirls)',
        'C — Alex (recent grad, exploring/digital media; swirls)'])
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('Program path for this run')
      .setChoiceValues(['Degree-seeking','Exploratory / undecided','Certificate / workforce'])
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('Advising approach')
      .setChoiceValues(['Self-advising (tried alone first)','Sought advising'])
      .setRequired(true);

  form.addTextItem()
      .setTitle('Tester initials')
      .setHelpText('Initials only — no full names or student data.');

  // ---------- SECTION 2: What happened on this task ----------
  form.addPageBreakItem()
      .setTitle('What happened on this task')
      .setHelpText('One submission = one task.');

  var tasks = [
    '1 — Apply & choose your major/program [All]',
    '2 — Find money to pay for it [All]',
    '3 — Residency / what you’ll be charged [All]',
    '4 — Get enrolled in the right classes (self-advise or ask?) [All]',
    '4a — Required new-student / FYE step [Degree/Explore]',
    '4b — Get into the certificate course sequence [Cert]',
    '4c — Try to self-register first [Self-advise]',
    '5 — Sort out math/English placement [All]',
    '6 — Pay the bill or set a payment plan [All]',
    '7 — Login, student email & ID [All]',
    '8 — First-day logistics, parking, getting around [All]',
    '7b — Campus tech: printing, wi-fi, lab/computer access, password reset [All]',
    '9 — Canvas: find classes, syllabus, first due date [All]',
    '10 — Canvas: submit work + quiz, check grade [All]',
    '11 — Canvas: message your instructor [All]',
    '12 — Canvas: fix a missing/dropped class [All]',
    '13 — Get textbooks/materials affordably [All]',
    '14 — Struggling in math — do something [All]',
    '15 — Out of money for food/rent [All]',
    '16 — Mental health slipping — find support [All]',
    '17 — Need disability accommodations [All]',
    '18 — Something unsafe/wrong — get help [All]',
    '19 — Drop/withdraw without wrecking aid [All]',
    '20 — Find a club/team/activity [All]',
    '21 — Find a campus job / work-study [All]',
    '22a — Plan transfer to a university and/or career [Degree/Explore]',
    '22b — Path to a job/licensure/next credential [Cert]',
    '23 — Find an internship/practicum [All]',
    '24 — Apply to graduate / complete certificate [All]',
    '25 — Send your transcript to a university/employer [All]',
    '26 — Save your email, files & coursework before account closes [All]',
    'S1 — Enroll at a 2nd Maricopa college for a needed course [Swirl B/C]',
    'S2 — Make financial aid cover the 2nd-college class (consortium) [Swirl B/C]',
    'S3 — Make the 2nd-college course count back home [Swirl B/C]',
    'S4 — Get help at the 2nd college’s unfamiliar systems [Swirl B/C]'
  ];
  form.addListItem().setTitle('Task').setChoiceValues(tasks).setRequired(true);

  form.addTextItem().setTitle('First search terms the persona used');
  form.addTextItem().setTitle('Where did they go FIRST?');
  form.addParagraphTextItem().setTitle('Path taken (offices, pages, clicks)');
  form.addTextItem().setTitle('Number of dead ends / wrong turns');
  form.addMultipleChoiceItem().setTitle('Did they need a human?').setChoiceValues(['No','Yes']);
  form.addTextItem().setTitle('If yes — who / what office? (leave blank if no)');
  form.addTextItem().setTitle('Where did they finally land? (local office/tool name)');
  form.addMultipleChoiceItem().setTitle('Did this service exist at THIS college?')
      .setChoiceValues(['Yes','No — not offered here (finding)','Not sure']);
  form.addTextItem().setTitle('Time to complete (minutes)');
  form.addMultipleChoiceItem().setTitle('Severity')
      .setChoiceValues(['1 — Minor','2 — Moderate','3 — Major (needed a human / nearly quit)','4 — Blocking (could not complete)'])
      .setRequired(true);
  form.addParagraphTextItem().setTitle('Barrier description — what went wrong');
  form.addParagraphTextItem().setTitle('AI opportunity idea (optional)');
  form.addMultipleChoiceItem().setTitle('Bilingual gap? (especially Persona A)')
      .setChoiceValues(['N/A','Spanish-language help was findable','Spanish-language help was missing']);
  form.addTextItem().setTitle('Screenshot link (optional)');

  // ---------- Link a response spreadsheet ----------
  var ss = SpreadsheetApp.create('Barrier Log (live) — Student Journey UX Study');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  Logger.log('==============================================');
  Logger.log('FORM TO FILL OUT (share with reps): ' + form.getPublishedUrl());
  Logger.log('FORM TO EDIT: ' + form.getEditUrl());
  Logger.log('RESPONSES SHEET (your Barrier Log): ' + ss.getUrl());
  Logger.log('==============================================');
}
