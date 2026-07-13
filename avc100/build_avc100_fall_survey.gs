/**
 * AVC 100 · FALL 2026 End-of-Course Survey · Google Form builder
 *
 * WHAT THIS DOES: builds the whole survey as a Google Form in one click.
 * Almost everything is a 1 to 5 scale. Fifteen questions, about 4 minutes for a student.
 *
 * HOW TO RUN IT (2 minutes):
 *  1. Sign in to Google with your GCC ACCOUNT (not personal, this collects student responses)
 *  2. Go to script.google.com → New project
 *  3. Delete the code in the box, paste ALL of this in
 *  4. Click Save
 *  5. Make sure the dropdown at the top says: buildAVC100FallSurvey
 *  6. Click Run. Allow permissions the first time (your script, your form, your account).
 *  7. Open "Execution log" at the bottom. It prints two links:
 *     one to EDIT the form, one to SEND to students.
 */

// ── THE CREDIT-HOUR CONTRACT ──────────────────────────────────────────────
// Taken from the seat-time lookup in course-dialer/workload.html, profile '1-2-studio':
//
//   AVC 100 · 1 credit · loads at 2 · studio · ONLINE
//   TOTAL student hours .... 40   (the rule is credits x 40, always;
//                                  load hours change the SPLIT, not the total)
//     direct instruction ... 13.5
//     studio ...............  0
//     outside work ......... 26.5
//
//   40 hours ÷ 7.5 weeks = 5.3 hours per week
//
// This is the promise the course makes. The survey asks whether it was true.
var TOTAL_HOURS = 40;
var WEEKS = 7.5;
var HOURS_PER_WEEK = Math.round((TOTAL_HOURS / WEEKS) * 10) / 10;   // 5.3

function buildAVC100FallSurvey() {

  var form = FormApp.create('AVC 100 · End-of-Course Survey (Fall 2026)');

  form.setDescription(
    'This survey is ANONYMOUS. I cannot see who submitted it, and it does not affect your grade.\n\n' +
    'I rebuilt this course to make it less lonely and to make it obvious where to get help. ' +
    'I need to know whether that worked, so I can fix what did not. Please be honest, ' +
    'including about what fell flat.\n\n' +
    'About 4 minutes. Everything is a 1 to 5 rating.'
  );

  form.setCollectEmail(false);
  form.setProgressBar(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage('Thank you. This actually changes what I build next.');

  // Only list supports that ACTUALLY EXISTED in this section. Do not ask about
  // anything you did not build; a student rating a thing that was not there is noise.
  // FALL 2026: add the After Effects demo videos and the Getting Help / CopaMigo video.
  var SUPPORTS = [
    'The student-services videos in the modules',
    'The Getting Help video (how to find support at GCC)',
    'The Discord community',
    'The way the course was broken into modules',
    'The software demo videos (Illustrator, Photoshop, After Effects)',
    'Instructor feedback on your projects',
    'Critique from classmates',
    'The course schedule and due dates',
    'Knowing where to find tech support',
    'The three-phase postcard project'
  ];

  // ── the matching code: links this to the week-one pretest, identifies nobody ──
  form.addTextItem()
      .setTitle('Your private code')
      .setHelpText(
        'The same code you made in week one, so I can see what changed for YOU without knowing who you are.\n\n' +
        'It was: first letter of your mother\'s first name + the DAY of the month you were born (2 digits) + ' +
        'the first 3 letters of your first pet\'s name. All lowercase.\n\nExample: m07cat\n\n' +
        'If you cannot remember it, just write "forgot" and answer the rest anyway.'
      )
      .setRequired(true);

  // ─────────────────────────────────────────────
  // 1 · ONE CLICK, BIG PAYOFF
  // ─────────────────────────────────────────────
  form.addMultipleChoiceItem()
      .setTitle('Is this your first fully online college course?')
      .setChoiceValues(['Yes', 'No'])
      .setRequired(true);

  // ─────────────────────────────────────────────
  // 2 · WHAT CHANGED  (retrospective pre/post)
  // ─────────────────────────────────────────────
  // NOTE ON WHAT THIS MEASURES:
  // AVC 100 is a 1-credit intro. The goal is NOT proficiency. The goal is that a student
  // opens the software, makes a small real thing, stops being afraid of it, and wants to
  // keep going. So measure demystification and intent to continue, not skill.
  // NO retrospective recall this time. You have a real week-one baseline from the pretest,
  // matched by the private code. These items are worded IDENTICALLY to the pretest so the
  // two can be compared line by line, per student.
  form.addPageBreakItem()
      .setTitle('What changed for you')
      .setHelpText('You answered these same questions in week one. This is not a test of how good you are, it is about what changed.');

  form.addGridItem()
      .setTitle('Now, TODAY. How much do you agree? (1 = strongly disagree, 5 = strongly agree)')
      .setRows([
        'Opening these programs still feels intimidating.',
        'I have made something real in each of these programs.',
        'I could make a simple piece again on my own, without step-by-step instructions.',
        'I want to take another class that uses this software.',
        'I know where to go for help at GCC.'
      ])
      .setColumns(['1', '2', '3', '4', '5'])
      .setRequired(true);

  // ─────────────────────────────────────────────
  // 3 · DID THE SUPPORTS HELP
  // ─────────────────────────────────────────────
  form.addPageBreakItem()
      .setTitle('Did these help you?')
      .setHelpText('1 = not helpful at all, 5 = extremely helpful. "Did not use it" is a real and useful answer, please use it if it is true.');

  form.addGridItem()
      .setTitle('How helpful was each one?')
      .setRows(SUPPORTS)
      .setColumns(['Did not use it', '1', '2', '3', '4', '5'])
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('Which ONE of those would you have been fine without?')
      .setHelpText('Be honest. This is how I find out what to cut.')
      .setChoiceValues(SUPPORTS.concat(['None, I used all of them']))
      .setRequired(true);

  // The student-services videos are the core theory of this redesign: put the door to help
  // INSIDE the course, so a student in trouble does not have to go looking for it.
  // These two questions are how I find out whether that door was ever actually used.
  form.addMultipleChoiceItem()
      .setTitle('Because of something in this course, did you ever actually contact a service at GCC, or go to an office, for help?')
      .setHelpText('For example: the Cares office / basic needs, counseling, advising, financial aid, tutoring, tech support, disability resources, veterans services.')
      .setChoiceValues(['Yes', 'No', 'I looked into it but did not go'])
      .setRequired(true);

  form.addParagraphTextItem()
      .setTitle('If yes, or if you looked into it: which service, and was it useful?')
      .setHelpText('Optional, and please do not include anything about your situation you would rather keep private. I only need to know whether the door worked.')
      .setRequired(false);

  // ─────────────────────────────────────────────
  // 4 · SUPPORT AND BELONGING
  // ─────────────────────────────────────────────
  form.addPageBreakItem()
      .setTitle('Support and belonging')
      .setHelpText('1 = strongly disagree, 5 = strongly agree');

  form.addGridItem()
      .setTitle('How much do you agree?')
      .setRows([
        'I felt connected to other people in this class.',
        'I knew where to go if I needed help, academic or personal.',
        'If I was struggling, I believed someone at this college would help me.',
        'I am proud of the work I made in this class.',
        'I learned things I will actually use.'
      ])
      .setColumns(['1', '2', '3', '4', '5'])
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('At some point, did you seriously consider dropping this class?')
      .setChoiceValues(['Yes', 'No'])
      .setRequired(true);

  form.addParagraphTextItem()
      .setTitle('If yes: what made you stay, or what almost made you leave?')
      .setHelpText('Optional, and the most useful thing you could tell me.')
      .setRequired(false);

  // ─────────────────────────────────────────────
  // 5 · DIFFICULTY AND WORKLOAD  (bipolar 1-5, 3 = just right)
  // ─────────────────────────────────────────────
  form.addPageBreakItem()
      .setTitle('Difficulty and workload')
      .setHelpText('For these two, 3 means "about right." Lower means too little, higher means too much.');

  form.addScaleItem()
      .setTitle('The DIFFICULTY of this course was:')
      .setBounds(1, 5)
      .setLabels('Much too easy', 'Much too hard')
      .setRequired(true);

  form.addScaleItem()
      .setTitle('The AMOUNT OF WORK in this course was:')
      .setBounds(1, 5)
      .setLabels('Much too light', 'Much too heavy')
      .setRequired(true);

  form.addScaleItem()
      .setTitle('How often did you feel overwhelmed in this course?')
      .setBounds(1, 5)
      .setLabels('Never', 'Almost always')
      .setRequired(true);

  // ── SEAT TIME ──
  // The credit-hour contract. A 1-credit course carries a fixed number of student
  // hours. Verify EXPECTED_HOURS against the official course record before you send this.
  form.addPageBreakItem()
      .setTitle('Time')
      .setHelpText(
        'This one matters a lot to me.\n\n' +
        'This is a 1-credit course. A 1-credit course is designed to take about ' + TOTAL_HOURS +
        ' hours of your time in total, and ours ran over ' + WEEKS + ' weeks. That works out to roughly ' +
        HOURS_PER_WEEK + ' hours per week, including watching, reading, and making the projects.\n\n' +
        'That is the promise the course makes. I need to know whether it was true.'
      );

  form.addScaleItem()
      .setTitle('You were expected to spend about ' + HOURS_PER_WEEK + ' hours per week on this course, for ' + WEEKS + ' weeks (about ' + TOTAL_HOURS + ' hours in total). Was that about right?')
      .setBounds(1, 5)
      .setLabels('It took much LESS time than that', 'It took much MORE time than that')
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle('Roughly how many hours per week did you actually spend on this course?')
      .setHelpText('Your best honest guess. Include watching, reading, and making the projects.')
      .setChoiceValues([
        'Less than 2 hours',
        '2 to 4 hours',
        '4 to 6 hours',
        '6 to 8 hours',
        '8 to 10 hours',
        'More than 10 hours'
      ])
      .setRequired(true);

  form.addParagraphTextItem()
      .setTitle('If it took much more or much less time than expected, which parts of the course drove that?')
      .setHelpText('Optional. Naming the specific assignments helps me fix it.')
      .setRequired(false);

  // ─────────────────────────────────────────────
  // 6 · INSTRUCTOR  (one question, on purpose)
  // ─────────────────────────────────────────────
  form.addPageBreakItem()
      .setTitle('Your instructor');

  form.addGridItem()
      .setTitle('How much do you agree?')
      .setRows([
        'My instructor gave clear instructions and useful feedback, and responded when I needed help.',
        'I felt my instructor cared about my wellbeing and my success.'
      ])
      .setColumns(['1', '2', '3', '4', '5'])
      .setRequired(true);

  // ─────────────────────────────────────────────
  // 7 · IN YOUR OWN WORDS
  // ─────────────────────────────────────────────
  form.addPageBreakItem()
      .setTitle('In your own words')
      .setHelpText('These are the answers I read most carefully.');

  form.addParagraphTextItem()
      .setTitle('What helped you the most, and why?')
      .setRequired(false);

  form.addParagraphTextItem()
      .setTitle('What got in your way, confused you, or wasted your time?')
      .setRequired(false);

  // The open door. A student who was carried by this course needs a place to say so, in
  // her own words, on her own terms, with only what she chooses to share. This is the
  // ONLY ethical way that story ever gets told: she tells it, anonymously, or it is not told.
  form.addParagraphTextItem()
      .setTitle('Did anything in this course help you with something bigger than the class itself? If so, and if you are willing, tell me about it.')
      .setHelpText(
        'Completely optional, and completely anonymous.\n\n' +
        'Share only what you want to share. You do not owe me any details about your life, ' +
        'and I would rather you left out anything private.\n\n' +
        'I ask because I built the support pieces of this course on a theory: that if the door to ' +
        'help is inside the class, someone who needs it will find it. If that happened for you, ' +
        'even in a small way, I want to know, because it tells me to keep building this way for ' +
        'the next student.'
      )
      .setRequired(false);

  form.addParagraphTextItem()
      .setTitle('Anything else you want to tell me?')
      .setRequired(false);

  Logger.log('DONE.');
  Logger.log('EDIT the form:          ' + form.getEditUrl());
  Logger.log('SEND this to students:  ' + form.getPublishedUrl());
  Logger.log('');
  Logger.log('Match this to the week-one pretest on the "private code" column.');
}
