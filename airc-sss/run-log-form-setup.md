# Wiring the Log button to a Google Form (auto-fills the scenario)

The tester tool (`run.html`) hands each person one scenario. When they finish, the
Log button should open a Google Form that already knows which scenario they ran, so
nobody has to type a scenario number. This note walks through building that form and
pasting one prefilled link into `run.html`.

You do this once. After that every tester just clicks Log and the form arrives
pre-stamped with the scenario ID, persona, campus, task, tester type, and mode.

## What you are setting up

`run.html` has this near the top of its script:

```
const LOG_FORM_PREFILL = "";
```

You will paste a Google Forms prefilled link between those quotes. That link carries
six placeholder tokens that `run.html` swaps out for the real values before it opens
the form:

- `__SID__` becomes the scenario id (for example S001)
- `__PID__` becomes the persona id (for example P01)
- `__CAMPUS__` becomes the campus (for example GCC)
- `__TASK__` becomes the task text
- `__TESTER__` becomes Human or AI
- `__MODE__` becomes Online or In person

There is also a `const LOG_FORM_URL = "";` right below it. Leave it blank. It is only
a fallback for a plain form link with no auto-fill, and it is used only if
`LOG_FORM_PREFILL` is empty.

## Step 1, build the form

You can build it by hand or run the script in Step 4. Either way the form needs these
questions, in this order:

1. Scenario ID, short answer
2. Persona, short answer
3. Campus, short answer
4. Task, short answer (or paragraph)
5. Tester type, multiple choice: Human, AI
6. Mode, multiple choice: Online, In person
7. Completed, multiple choice: Yes, Partial, No
8. Severity, linear scale 0 to 4
9. Time on task, short answer
10. What happened, paragraph
11. Suggested fix, paragraph

Questions 1 through 6 are the ones the tool fills in automatically. Questions 7
through 11 are what the tester writes after the run.

## Step 2, get the prefilled link

1. Open your form in the editor.
2. Click the three-dot menu at the top right and choose &ldquo;Get pre-filled link.&rdquo;
3. The form opens in fill-in mode. In the answer boxes, type the literal tokens, exactly
   as written, into the matching questions:
   - Scenario ID: `__SID__`
   - Persona: `__PID__`
   - Campus: `__CAMPUS__`
   - Task: `__TASK__`
   - Tester type: `__TESTER__`
   - Mode: `__MODE__`
   Leave Completed, Severity, Time on task, What happened, and Suggested fix empty. The
   tester answers those.
4. Note: Tester type and Mode are multiple choice, so a prefilled link normally only
   accepts one of the real options. Enter the token anyway if the form allows a custom
   entry, or, if it will not take the token, change those two questions to short answer
   just long enough to grab the link, then switch them back. The tool sends &ldquo;Human&rdquo; or
   &ldquo;AI&rdquo; and &ldquo;Online&rdquo; or &ldquo;In person,&rdquo; which match the options.
5. Click &ldquo;Get link&rdquo; at the bottom, then &ldquo;Copy link.&rdquo;

You now have a URL that looks something like:

```
https://docs.google.com/forms/d/e/FORM_ID/viewform?usp=pp_url&entry.111=__SID__&entry.222=__PID__&entry.333=__CAMPUS__&entry.444=__TASK__&entry.555=__TESTER__&entry.666=__MODE__
```

The tokens must survive in the copied link. If Google encoded them (for example
`__SID__` shows up as `%5F%5FSID%5F%5F`), change the encoded pieces back to the plain
tokens by hand before pasting.

## Step 3, paste it into run.html

Open `run.html`, find `const LOG_FORM_PREFILL = "";`, and paste your link between the
quotes:

```
const LOG_FORM_PREFILL = "https://docs.google.com/forms/d/e/FORM_ID/viewform?usp=pp_url&entry.111=__SID__&entry.222=__PID__&entry.333=__CAMPUS__&entry.444=__TASK__&entry.555=__TESTER__&entry.666=__MODE__";
```

Save. That is it. Now when a tester clicks Log, the tool replaces each token with that
scenario&rsquo;s real values and opens the form in a new tab, already filled in. If the
constant is left blank, the Log button stays in a &ldquo;Log form link pending&rdquo; state and
explains what to do when clicked.

## Step 4, ready-to-paste Apps Script that builds the form

If you would rather not build the form by hand, open script.google.com, make a new
project, paste this in, and run `buildBarrierLogForm`. It prints the edit URL and the
published (viewform) URL in the execution log. Use the edit URL to do the &ldquo;Get
pre-filled link&rdquo; step above.

```javascript
function buildBarrierLogForm() {
  var form = FormApp.create('District Barriers Study, Barrier Log');
  form.setDescription(
    'One entry per scenario run. The first six fields auto-fill from the tester tool. ' +
    'Fill in Completed, Severity, Time on task, What happened, and Suggested fix after your run. ' +
    'Never enter real student data.'
  );
  form.setCollectEmail(false);

  form.addTextItem().setTitle('Scenario ID').setRequired(true);
  form.addTextItem().setTitle('Persona');
  form.addTextItem().setTitle('Campus');
  form.addTextItem().setTitle('Task');

  form.addMultipleChoiceItem()
    .setTitle('Tester type')
    .setChoiceValues(['Human', 'AI']);

  form.addMultipleChoiceItem()
    .setTitle('Mode')
    .setChoiceValues(['Online', 'In person']);

  form.addMultipleChoiceItem()
    .setTitle('Completed')
    .setChoiceValues(['Yes', 'Partial', 'No'])
    .setRequired(true);

  form.addScaleItem()
    .setTitle('Severity')
    .setBounds(0, 4)
    .setLabels('No barrier', 'Blocks the task')
    .setRequired(true);

  form.addTextItem().setTitle('Time on task (for example, 12 minutes)');

  form.addParagraphTextItem()
    .setTitle('What happened')
    .setHelpText('What you expected, what you found, where you got stuck.')
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('Suggested fix');

  Logger.log('Edit URL: ' + form.getEditUrl());
  Logger.log('Published URL: ' + form.getPublishedUrl());
}
```

After the script runs, open the edit URL, do Step 2 to get the prefilled link with the
tokens, then paste it into `LOG_FORM_PREFILL` per Step 3.
