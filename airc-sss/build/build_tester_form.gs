/**
 * ARC Domain 5 (Student Support and Success) — Student Journey Tester Form
 * Auto-generated from Maricopa_Scenario_Bank.xlsx (the 91 human-assigned scenarios).
 *
 * WHAT IT DOES
 *   Builds a Google Form + linked Sheet. A committee tester opens it, picks their
 *   college, and gets one of THAT college's real scenarios from the bank: a persona
 *   and one task, keyed to a Scenario ID (Sxxx). They run it with their own student
 *   login, log what happened, and submit. About 15 minutes. Every submission is one
 *   task and lands in the Sheet, keyed back to the Scenario Bank by Scenario ID.
 *
 * THE SPLIT
 *   Anything with NO login (finding public pages, reading policy) = the AI runs it
 *   (the 90 AI scenarios). Anything a real student login can reach = committee members
 *   run it (these 91 Human scenarios). This form is the human half.
 *
 * HOW TO RUN (about 2 minutes)
 *   1. script.google.com, sign in with the account you want the form on (personal is
 *      fine for the test; later run the same script on your work account, or make a copy).
 *   2. New project, delete the sample, paste ALL of this, Save.
 *   3. Run  buildTesterForm , Review permissions, Allow.
 *   4. View > Logs prints: FORM TO FILL OUT, FORM TO EDIT, RESPONSES SHEET.
 *   No student PII. Personas are test profiles. Initials only.
 */

var PERSONA_LIBRARY = "https://singletrackmom.github.io/airc-sss/persona-library.html";
var RUN_GUIDE = "https://singletrackmom.github.io/airc-sss/run-sheet.html";

// Campus -> that campus's human scenarios (label = Scenario ID · Persona · Task).
var SCENARIOS = {
  "Glendale (GCC)": [
    "S001 \u00b7 P01 Marisol Reyes \u00b7 Apply to the college as a brand-new student.",
    "S003 \u00b7 P01 Marisol Reyes \u00b7 Apply for financial aid (FAFSA) for the first time.",
    "S005 \u00b7 P01 Marisol Reyes \u00b7 Find out when aid disburses and when your refund lands.",
    "S007 \u00b7 P01 Marisol Reyes \u00b7 Figure out that Canvas is the LMS and that classes live there.",
    "S017 \u00b7 P03 Alex Nguyen \u00b7 Choose or change your major / Field of Interest.",
    "S019 \u00b7 P03 Alex Nguyen \u00b7 Find counseling / mental-health support and confirm it is confidential.",
    "S021 \u00b7 P03 Alex Nguyen \u00b7 Self-enroll in your first classes.",
    "S023 \u00b7 P03 Alex Nguyen \u00b7 Reach your instructor when something goes wrong.",
    "S095 \u00b7 P17 DeShawn Allen \u00b7 Understand how dropping affects your financial aid.",
    "S097 \u00b7 P17 DeShawn Allen \u00b7 Self-enroll in your first classes.",
    "S163 \u00b7 P32 Leila Hassan \u00b7 Find a club, community, or identity program that fits you.",
    "S165 \u00b7 P32 Leila Hassan \u00b7 Self-enroll in your first classes."
  ],
  "Chandler-Gilbert (CGCC)": [
    "S043 \u00b7 P07 Jasmine Williams \u00b7 Find housing, childcare, or basic-needs referrals.",
    "S045 \u00b7 P07 Jasmine Williams \u00b7 Drop a class and know the refund and withdrawal deadline.",
    "S047 \u00b7 P07 Jasmine Williams \u00b7 Find out when aid disburses and when your refund lands.",
    "S081 \u00b7 P14 Priya Patel \u00b7 Build a transfer plan to a university with no wasted credits.",
    "S083 \u00b7 P14 Priya Patel \u00b7 Self-enroll in your first classes.",
    "S137 \u00b7 P26 Hannah Berg \u00b7 Figure out that Canvas is the LMS and that classes live there.",
    "S139 \u00b7 P26 Hannah Berg \u00b7 Self-enroll in your first classes.",
    "S151 \u00b7 P29 Ethan Park \u00b7 Figure out that Canvas is the LMS and that classes live there.",
    "S153 \u00b7 P29 Ethan Park \u00b7 Self-enroll in your first classes.",
    "S179 \u00b7 P36 Yuki Tanaka \u00b7 Keep F-1 visa status valid while registering and paying.",
    "S181 \u00b7 P36 Yuki Tanaka \u00b7 Self-enroll in your first classes."
  ],
  "Estrella Mountain (EMCC)": [
    "S031 \u00b7 P05 Hassan Abdi \u00b7 Get your MEID and first login without coming to campus.",
    "S033 \u00b7 P05 Hassan Abdi \u00b7 Self-enroll in your first classes.",
    "S035 \u00b7 P05 Hassan Abdi \u00b7 Use campus tech: print a form, get on wi-fi, use a lab.",
    "S103 \u00b7 P19 Caleb Smith \u00b7 Complete new-student orientation / FYE.",
    "S105 \u00b7 P19 Caleb Smith \u00b7 Get your MEID and first login without coming to campus.",
    "S107 \u00b7 P19 Caleb Smith \u00b7 Use campus tech: print a form, get on wi-fi, use a lab.",
    "S167 \u00b7 P33 Cody Martin \u00b7 Complete new-student orientation / FYE.",
    "S169 \u00b7 P33 Cody Martin \u00b7 Use campus tech: print a form, get on wi-fi, use a lab."
  ],
  "GateWay": [
    "S049 \u00b7 P08 Kevin Nguyen \u00b7 Log in to student email and find official messages.",
    "S051 \u00b7 P08 Kevin Nguyen \u00b7 Get a student ID card.",
    "S119 \u00b7 P22 Nicole Tran \u00b7 Set up a payment plan or pay a bill.",
    "S121 \u00b7 P22 Nicole Tran \u00b7 Find and use tutoring (in person or online).",
    "S123 \u00b7 P22 Nicole Tran \u00b7 Log in to student email and find official messages.",
    "S145 \u00b7 P28 Maria Gonzalez \u00b7 Enter through Adult Ed / GED / ESL and find the next step into credit classes.",
    "S147 \u00b7 P28 Maria Gonzalez \u00b7 Find housing, childcare, or basic-needs referrals.",
    "S149 \u00b7 P28 Maria Gonzalez \u00b7 Self-enroll in your first classes."
  ],
  "Mesa (MCC)": [
    "S037 \u00b7 P06 Robert Kessler \u00b7 Find out your residency classification and what it means for tuition.",
    "S039 \u00b7 P06 Robert Kessler \u00b7 Order transcripts.",
    "S041 \u00b7 P06 Robert Kessler \u00b7 Use campus tech: print a form, get on wi-fi, use a lab.",
    "S109 \u00b7 P20 Brittany Hale \u00b7 Find out when aid disburses and when your refund lands.",
    "S111 \u00b7 P20 Brittany Hale \u00b7 Drop a class and know the refund and withdrawal deadline.",
    "S159 \u00b7 P31 Tyrone Davis \u00b7 Log in to student email and find official messages.",
    "S161 \u00b7 P31 Tyrone Davis \u00b7 Self-enroll in your first classes."
  ],
  "Paradise Valley (PVCC)": [
    "S059 \u00b7 P10 Tyler Brooks \u00b7 Self-enroll in your first classes.",
    "S061 \u00b7 P10 Tyler Brooks \u00b7 Figure out that Canvas is the LMS and that classes live there.",
    "S063 \u00b7 P10 Tyler Brooks \u00b7 Use campus tech: print a form, get on wi-fi, use a lab.",
    "S085 \u00b7 P15 Frank DiMarco \u00b7 Get your MEID and first login without coming to campus.",
    "S087 \u00b7 P15 Frank DiMarco \u00b7 Self-enroll in your first classes.",
    "S089 \u00b7 P15 Frank DiMarco \u00b7 Use campus tech: print a form, get on wi-fi, use a lab.",
    "S125 \u00b7 P23 Jordan Lee \u00b7 Find a club, community, or identity program that fits you.",
    "S127 \u00b7 P23 Jordan Lee \u00b7 Book an advising appointment."
  ],
  "Phoenix College": [
    "S025 \u00b7 P04 Ana Lucia Torres \u00b7 Apply for financial aid (FAFSA) for the first time.",
    "S027 \u00b7 P04 Ana Lucia Torres \u00b7 Find out your residency classification and what it means for tuition.",
    "S029 \u00b7 P04 Ana Lucia Torres \u00b7 Self-enroll in your first classes.",
    "S091 \u00b7 P16 Sofia Ramirez \u00b7 Apply for financial aid (FAFSA) for the first time.",
    "S093 \u00b7 P16 Sofia Ramirez \u00b7 Self-enroll in your first classes.",
    "S133 \u00b7 P25 Gabriel Mendez \u00b7 Find food / a food pantry on campus.",
    "S135 \u00b7 P25 Gabriel Mendez \u00b7 Set up a payment plan or pay a bill."
  ],
  "Rio Salado": [
    "S099 \u00b7 P18 Grace Okafor \u00b7 Confirm consortium aid covers a class at the second college.",
    "S101 \u00b7 P18 Grace Okafor \u00b7 Get prior or transfer credits evaluated.",
    "S141 \u00b7 P27 Victor Nguyen \u00b7 Take one needed class at a second college (consortium).",
    "S143 \u00b7 P27 Victor Nguyen \u00b7 Confirm the swirl credit and residency carry back home."
  ],
  "Scottsdale (SCC)": [
    "S009 \u00b7 P02 Darnell Carter \u00b7 Get prior or transfer credits evaluated.",
    "S011 \u00b7 P02 Darnell Carter \u00b7 Certify VA / veterans education benefits.",
    "S013 \u00b7 P02 Darnell Carter \u00b7 Drop a class and know the refund and withdrawal deadline.",
    "S015 \u00b7 P02 Darnell Carter \u00b7 Log in to student email and find official messages.",
    "S053 \u00b7 P09 Linda Yazzie \u00b7 Find a club, community, or identity program that fits you.",
    "S055 \u00b7 P09 Linda Yazzie \u00b7 Book an advising appointment.",
    "S057 \u00b7 P09 Linda Yazzie \u00b7 Use campus tech: print a form, get on wi-fi, use a lab.",
    "S071 \u00b7 P12 Mei Chen \u00b7 Set up a payment plan or pay a bill.",
    "S073 \u00b7 P12 Mei Chen \u00b7 Self-enroll in your first classes.",
    "S113 \u00b7 P21 Omar Haddad \u00b7 Set up Disability Resources (DRS) accommodations.",
    "S115 \u00b7 P21 Omar Haddad \u00b7 Find counseling / mental-health support and confirm it is confidential.",
    "S117 \u00b7 P21 Omar Haddad \u00b7 Book an advising appointment.",
    "S171 \u00b7 P34 Samantha Wright \u00b7 Order transcripts.",
    "S173 \u00b7 P34 Samantha Wright \u00b7 Find a club, community, or identity program that fits you."
  ],
  "South Mountain (SMCC)": [
    "S065 \u00b7 P11 Destiny Carter \u00b7 Find housing, childcare, or basic-needs referrals.",
    "S067 \u00b7 P11 Destiny Carter \u00b7 Find food / a food pantry on campus.",
    "S069 \u00b7 P11 Destiny Carter \u00b7 Book an advising appointment.",
    "S075 \u00b7 P13 Marcus Johnson \u00b7 Apply to the college as a brand-new student.",
    "S077 \u00b7 P13 Marcus Johnson \u00b7 Choose or change your major / Field of Interest.",
    "S079 \u00b7 P13 Marcus Johnson \u00b7 Find career services and an internship.",
    "S129 \u00b7 P24 Aaliyah Robinson \u00b7 Apply for financial aid (FAFSA) for the first time.",
    "S131 \u00b7 P24 Aaliyah Robinson \u00b7 Self-enroll in your first classes.",
    "S155 \u00b7 P30 Rosa Jimenez \u00b7 Self-enroll in your first classes.",
    "S157 \u00b7 P30 Rosa Jimenez \u00b7 Get a student ID card.",
    "S175 \u00b7 P35 Andre Thompson \u00b7 Book an advising appointment.",
    "S177 \u00b7 P35 Andre Thompson \u00b7 Self-enroll in your first classes."
  ],
};


function buildTesterForm() {
  var form = FormApp.create('ARC Domain 5 — Student Journey Tester');
  form.setDescription(
    'Walk one piece of a student\'s journey and tell us where it got hard. Pick your college '
    + 'and the form gives you a scenario: a persona (who you are) and one task. Stay in character, '
    + 'use your own student login, and start like a new, confused student would: problems, not '
    + 'destinations (never go straight to the office you already know). About 15 minutes. '
    + 'No student data: personas are test profiles, initials only.');
  form.setCollectEmail(false);
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(true);
  form.setProgressBar(false);

  form.addTextItem().setTitle('Your initials').setHelpText('Initials only. No full names or student data.').setRequired(true);

  var campusItem = form.addMultipleChoiceItem()
      .setTitle('Which college are you testing at this session?')
      .setHelpText('The next page gives you a scenario for that college.')
      .setRequired(true);

  // Build one page per campus, each with that campus's scenario dropdown.
  var campusNames = Object.keys(SCENARIOS);
  var pages = {};
  for (var i = 0; i < campusNames.length; i++) {
    var name = campusNames[i];
    var pb = form.addPageBreakItem()
      .setTitle(name + ' · your scenario this session')
      .setHelpText(
        'Take the next scenario on the list that is not already marked done on the tracker '
        + '(or the one your rep assigned you). Each one names your persona (Sxxx · P## Name) and '
        + 'your one task. Read your persona first: ' + PERSONA_LIBRARY + '  ·  Run guide: ' + RUN_GUIDE);
    form.addListItem()
      .setTitle('Your scenario (pick the one you are running)')
      .setHelpText('Format: Scenario ID · Persona · Task. This is who you are and your one job this session.')
      .setChoiceValues(SCENARIOS[name])
      .setRequired(true);
    pages[name] = pb;
  }

  // Shared "what happened" page that every campus funnels into.
  var logPage = form.addPageBreakItem()
      .setTitle('What happened on this task')
      .setHelpText('One submission = one scenario. Record what the student ACTUALLY did, not where they were supposed to go.');

  form.addMultipleChoiceItem().setTitle('Did you finish it?')
      .setChoiceValues(['Completed','Completed, but it was hard','Could not complete','Service not offered here (that is a finding)'])
      .setRequired(true);
  form.addMultipleChoiceItem().setTitle('Severity')
      .setChoiceValues(['1 — Minor (slight friction, figured it out fast)','2 — Moderate (confusion, extra steps or a wrong turn)','3 — Major (needed a human, or nearly gave up)','4 — Blocking (could not complete, a real student would likely quit)'])
      .setRequired(true);
  form.addParagraphTextItem().setTitle('How you tried').setHelpText('Where you started (search terms, first page) and the path you took.').setRequired(true);
  form.addParagraphTextItem().setTitle('Where you got stuck or confused');
  form.addTextItem().setTitle('Words or labels that tripped you up').setHelpText('Jargon or menu names that did not make sense.');
  form.addTextItem().setTitle('Did you need a human? If so, who or which office?');
  form.addTextItem().setTitle('About how long did it take? (minutes)');
  form.addParagraphTextItem().setTitle('One idea: where could AI or a clearer signpost have helped?').setHelpText('This is how a barrier becomes a pilot. It should make staff work easier, not replace it.');
  form.addTextItem().setTitle('Screenshot link (optional)').setHelpText('Paste a link to a screenshot of a dead end or confusing page, if you have one.');

  // Wire branching: campus choice -> that campus's page; each campus page -> shared log page.
  var choices = [];
  for (var j = 0; j < campusNames.length; j++) choices.push(campusItem.createChoice(campusNames[j], pages[campusNames[j]]));
  campusItem.setChoices(choices);
  for (var k = 0; k < campusNames.length; k++) pages[campusNames[k]].setGoToPage(logPage);

  var ss = SpreadsheetApp.create('Student Journey Tester — responses (live)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  Logger.log('==================================================');
  Logger.log('FORM TO FILL OUT (share with committee): ' + form.getPublishedUrl());
  Logger.log('FORM TO EDIT: ' + form.getEditUrl());
  Logger.log('RESPONSES SHEET (your study data): ' + ss.getUrl());
  Logger.log('==================================================');
}
