/**
 * AVC 100 · WEEK ONE PRETEST · Google Form builder
 *
 * RUN THIS IN WEEK 1 OF FALL 2026. It is the baseline half of a real pre/post design.
 * The end-of-course survey (build_avc100_survey.gs) is the post half, and its items
 * are worded to match these exactly so the two can be compared item by item.
 *
 * WHY IT MATTERS: this summer I had to use a RETROSPECTIVE pre/post, asking students at
 * the end to recall how they felt at the start. That is a legitimate method, but it is
 * recall, not measurement. With a real week-one baseline I can make a much stronger claim.
 *
 * WHAT IT MEASURES: this course is 1 credit. The goal is NOT proficiency. The goal is that
 * a student opens the software, makes a small real thing, stops being afraid of it, and
 * wants to keep going. So the items measure INTIMIDATION and INTENT TO CONTINUE, not skill.
 *
 * ANONYMITY vs. MATCHING, read this before you run it:
 *   Matched pre/post data (linking each student's week-1 answer to their week-8 answer)
 *   is far stronger than comparing two group averages. To get it WITHOUT collecting names,
 *   use a self-generated code: ask for the same non-identifying code on both surveys.
 *   The code below (mother's-initial + birth-day + first pet) is a standard research
 *   technique. It matches reliably and identifies nobody.
 *
 * HOW TO RUN IT:
 *  1. Sign in with your GCC account (this collects student responses)
 *  2. script.google.com → New project → paste this in → Save
 *  3. Dropdown says buildAVC100Week1Pretest → Run → allow permissions
 *  4. Execution log prints the edit link and the student link
 */

function buildAVC100Week1Pretest() {

  var form = FormApp.create('AVC 100 · Week One Check-In');

  form.setDescription(
    'This is ANONYMOUS and it is not graded. There are no right answers and nothing here ' +
    'affects your grade.\n\n' +
    'I ask this in week one and again at the end, so I can see what actually changed for ' +
    'you across the class. It tells me what to fix.\n\n' +
    'This is not a test of what you know. Please answer honestly, including "I have never ' +
    'opened this."\n\nAbout 2 minutes.'
  );

  form.setCollectEmail(false);
  form.setProgressBar(true);
  form.setConfirmationMessage('Thank you. See you at the end of the course.');

  // ── the matching code: links pre to post, identifies nobody ──
  form.addTextItem()
      .setTitle('Your private code')
      .setHelpText(
        'So I can compare your week-one answers to your end-of-course answers WITHOUT knowing who you are.\n\n' +
        'Make it like this, all lowercase, no spaces:\n' +
        '  the first letter of your mother\'s first name\n' +
        '  + the DAY of the month you were born (2 digits)\n' +
        '  + the first 3 letters of your first pet\'s name\n\n' +
        'Example: m07cat\n\n' +
        'Write it down. You will enter the SAME code on the survey at the end of the course. ' +
        'I cannot work out who you are from it.'
      )
      .setRequired(true);

  // ── the software: intimidation, not skill ──
  form.addPageBreakItem()
      .setTitle('The software')
      .setHelpText('1 = strongly disagree, 5 = strongly agree. Be honest. Most people in this class have never opened these.');

  form.addGridItem()
      .setTitle('How much do you agree, right now, in week one?')
      .setRows([
        'Opening Illustrator, Photoshop, and After Effects feels intimidating.',
        'I have made something real in each of these programs.',
        'I could make a simple piece on my own, without step-by-step instructions.',
        'I want to take another class that uses this software.'
      ])
      .setColumns(['1', '2', '3', '4', '5'])
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('Before this class, how much had you used design software of any kind?')
      .setChoiceValues([
        'Never opened any of it',
        'Opened it once or twice, never made anything',
        'Made a few things, mostly following a tutorial',
        'I use it fairly regularly',
        'I am comfortable with it'
      ])
      .setRequired(true);

  // ── support and belonging: same items as the exit survey ──
  form.addPageBreakItem()
      .setTitle('Getting help')
      .setHelpText('1 = strongly disagree, 5 = strongly agree');

  form.addGridItem()
      .setTitle('How much do you agree, right now?')
      .setRows([
        'I know where to go if I need help at GCC, academic or personal.',
        'If I was struggling, I believe someone at this college would help me.',
        'I feel connected to other people in this class.'
      ])
      .setColumns(['1', '2', '3', '4', '5'])
      .setRequired(true);

  // ── context ──
  form.addPageBreakItem()
      .setTitle('A little about you');

  form.addMultipleChoiceItem()
      .setTitle('Is this your first fully online college course?')
      .setChoiceValues(['Yes', 'No'])
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('Is this your first semester at GCC?')
      .setChoiceValues(['Yes', 'No'])
      .setRequired(true);

  form.addParagraphTextItem()
      .setTitle('What are you hoping to get out of this class?')
      .setHelpText('Optional. One line is fine.')
      .setRequired(false);

  form.addParagraphTextItem()
      .setTitle('Is there anything you are worried about going into this class?')
      .setHelpText('Optional. This is the one I read most carefully.')
      .setRequired(false);

  Logger.log('DONE.');
  Logger.log('EDIT the form:         ' + form.getEditUrl());
  Logger.log('SEND this to students: ' + form.getPublishedUrl());
  Logger.log('');
  Logger.log('REMINDER: add the same "your private code" question to the END-OF-COURSE survey,');
  Logger.log('with the same instructions, so the two can be matched.');
}
