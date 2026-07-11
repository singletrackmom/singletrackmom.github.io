/**
 * SYLLABUS CHECKER · Google Apps Script
 * Glendale Community College · Art & Humanities
 *
 * GOAL:     Read a submitted syllabus, compare it against the approved language,
 *           and email the instructor a report of what is missing. READ ONLY.
 *           This script never edits anyone's syllabus.
 *
 * AUDIENCE: Whoever maintains the syllabus submission Google Form.
 *
 * PROCESS:  Bind to the Form → on submit, read the syllabus + the live approved
 *           language Doc → compare → email a report.
 *
 * WHY APPS SCRIPT: it runs inside Google Workspace as an authorized user, so
 * there is no OAuth app, no client secret, no server, and no CORS. It reads the
 * approved-language Doc LIVE on every run, so when the department revises the
 * wording the checker is instantly current. Nothing to keep in sync.
 *
 * WHY NO AI (for now): "does the approved statement appear verbatim" is a string
 * comparison. An LLM would be strictly worse here, because it might judge a
 * paraphrase as a match. On an accreditation item, deterministic beats clever.
 *
 * ─────────────────────────────────────────────────────────────────────────────
 * SETUP
 *   1. Open the syllabus submission Google Form → ⋮ → Script editor.
 *   2. Paste this file in.
 *   3. Set APPROVED_DOC_ID below (already filled in).
 *   4. Confirm FORM_FIELDS matches your actual question titles.
 *   5. Triggers (clock icon) → Add Trigger → onFormSubmit → From form → On form submit.
 *   6. Run onFormSubmit once manually to grant permissions.
 * ─────────────────────────────────────────────────────────────────────────────
 */

// The department reference doc. The authority. Read live, never copied.
var APPROVED_DOC_ID = '1i3Tw0cbMaWB5JDBqbCL0SGbuEHAYXhv1DBGQsVcpeFA';

// Your Form's question titles. Update these if you reword a question.
var FORM_FIELDS = {
  name:     'Instructor Name',
  email:    'Email',
  course:   'Major Class & Number',
  combined: 'Is this for a combined/associated section?',
  minor:    'Minor/Associated Class(es) & Number(s) (if applicable)',
  start:    'Class Start Date',
  upload:   'Upload a PDF or Doc of your syllabus here.',
  ssUrl:    'Simple Syllabus/Syllabus+ Option: Enter the "Syllabus PDF URL" provided here'
};

/**
 * WHO GETS WHAT
 *   Instructor → an email report of what is missing. They need to act.
 *   The department admin → the response Sheet, with status columns written back by this
 *                 script. They need to MONITOR, not read 40 emails. One tab,
 *                 sortable, shows who is compliant and who is not.
 *
 * OWNERSHIP: install this on the WORK account that owns the Form (the same
 * account the Form already submits to). Then it is the department's tool, it
 * keeps running if any one person leaves, and the department controls it.
 */
var ADMIN_EMAIL = '';        // optional weekly digest to the department admin. Leave blank for none.
var STATUS_COLUMNS = ['Check status', 'Missing items', 'File type', 'Checked on'];

/* ══════════════════════════════════════════════════════════════════════════
   SEAT-HOUR PROFILES
   Total student hours = CREDITS x 40. Always. Load hours do NOT change the
   total; they change the split. Confirm credits/load/activity type on CCTA.
   ══════════════════════════════════════════════════════════════════════════ */
var PROFILES = {
  'AVC100': { label: '1 credit, loads at 2, lecture/lab (studio)', match: 'For this 1 credit lecture/lab (studio)' },
  'AVC183': { label: '3 credits, loads at 6, studio',              match: 'credit online studio course' },
  'AVC248': { label: '3 credits, loads at 6, studio',              match: 'credit online studio course' },
  'ART111': { label: '3 credits, loads at 6, studio',              match: 'credit studio course' },
  'ART161': { label: '3 credits, loads at 6, studio',              match: 'credit studio course' },
  'AVC184': { label: '3 credits, loads at 6, studio',              match: 'credit studio course' }
};

// A distinctive phrase from the RSI paragraph. Present = RSI is there.
var RSI_FINGERPRINT = 'regular and substantive interaction';

/* ══════════════════════════════════════════════════════════════════════════
   MAIN
   ══════════════════════════════════════════════════════════════════════════ */
function onFormSubmit(e) {
  var r = readResponse(e);
  if (!r.email) { Logger.log('No email on submission; nothing to send.'); return; }

  var approved = fetchApprovedStatements_();   // live, from the Doc
  var syllabus = extractSyllabusText_(r);      // {text, format, reliable, note}

  var findings = [];

  // If we could not read the file, say so plainly rather than guessing.
  if (syllabus.text === null) {
    findings.push({
      level: 'blocked',
      title: 'Could not read your syllabus',
      body: syllabus.note + ' Nothing was checked. Resubmit as a Google Doc or Word file and the report will run.'
    });
    sendReport_(r, findings, syllabus);
    return;
  }

  var hay = normalize_(syllabus.text);

  // ── CHECK 1 · approved seat-hours statement, verbatim ──────────────────
  var hit = null;
  for (var i = 0; i < approved.length; i++) {
    if (hay.indexOf(normalize_(approved[i])) !== -1) { hit = approved[i]; break; }
  }
  if (hit) {
    findings.push({ level: 'pass', title: 'Approved seat-hours statement found', body: 'Present and verbatim.' });
  } else {
    var guess = guessProfile_(r.course);
    findings.push({
      level: 'missing',
      title: 'Approved seat-hours statement not found',
      body: 'The required seat-hours language does not appear in your syllabus, or it has been reworded. It must appear <b>exactly as approved</b>, in the workload section (in Syllabus+, "Instructional Contact Hours &amp; Out-of-Class Student Work").'
            + (guess ? '<br><br>Based on <b>' + r.course + '</b> (' + guess.label + '), you likely need the statement for that profile.' : '')
            + '<br><br>Copy the correct wording from the reference sheet: ' + docLink_()
    });
  }

  // ── CHECK 2 · RSI, online and hybrid only ──────────────────────────────
  // Only assert this when we know the modality. The Form does not ask, so we
  // infer from the approved statement found. If we cannot tell, we say so
  // instead of failing someone incorrectly.
  var rsiPresent = hay.indexOf(normalize_(RSI_FINGERPRINT)) !== -1;
  var looksOnline = hay.indexOf('online') !== -1;
  if (rsiPresent) {
    findings.push({ level: 'pass', title: 'RSI statement found', body: 'Regular and Substantive Interaction language is present.' });
  } else if (looksOnline) {
    findings.push({
      level: 'missing',
      title: 'RSI statement not found',
      body: 'This looks like an online or hybrid course, which requires a Regular and Substantive Interaction statement. '
          + 'It is <b>already built into the approved online seat-hours statement</b>, so pasting that one block covers both. ' + docLink_()
    });
  } else {
    findings.push({
      level: 'info',
      title: 'RSI not checked',
      body: 'Could not determine whether this course is online or hybrid. If it is, an RSI statement is required. ' + docLink_()
    });
  }

  // ── CHECK 3 · form hygiene (free, catches real errors) ─────────────────
  if (r.combined === 'Yes' && !r.minor) {
    findings.push({
      level: 'missing',
      title: 'Combined section with no associated classes listed',
      body: 'You marked this as a combined or associated section but did not list the associated class numbers. Combined syllabi must name every class, including class numbers.'
    });
  }
  if (r.course && !/^[A-Za-z]{2,4}\d{3}[A-Za-z]{0,2}-\d{4,6}$/.test(r.course.trim())) {
    findings.push({
      level: 'info',
      title: 'Class number format looks off',
      body: 'Expected PREFIX###-##### (for example AVC248-12345). You entered: ' + r.course
    });
  }
  var due = fridayOfFirstWeek_(r.start);
  if (due && new Date() > due) {
    findings.push({
      level: 'info',
      title: 'Past the submission deadline',
      body: 'Your class started ' + fmtDate_(r.start) + ', so this syllabus was due Friday, ' + fmtDate_(due) + '.'
    });
  }

  sendReport_(r, findings, syllabus);
  writeStatusForAdmin_(e, findings, syllabus);
}

/* ══════════════════════════════════════════════════════════════════════════
   ADMIN DASHBOARD
   The Form already writes every submission to a response Sheet. We append
   status columns to that same row. The admin opens one tab and sorts by status.
   They do not get 40 emails. This is the difference between monitoring and
   drowning.
   ══════════════════════════════════════════════════════════════════════════ */
function writeStatusForAdmin_(e, findings, syllabus) {
  if (!e || !e.range) return;                       // only runs on a Sheet-linked Form
  var sheet = e.range.getSheet();
  var row = e.range.getRow();

  var missing = findings.filter(function(f){ return f.level === 'missing' || f.level === 'blocked'; });
  var status = missing.length === 0 ? 'COMPLETE'
             : (findings.some(function(f){return f.level==='blocked';}) ? 'UNREADABLE' : 'MISSING ITEMS');

  var head = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
  var startCol = head.indexOf(STATUS_COLUMNS[0]) + 1;

  // First run: add the status headers once.
  if (startCol === 0) {
    startCol = sheet.getLastColumn() + 1;
    sheet.getRange(1, startCol, 1, STATUS_COLUMNS.length)
         .setValues([STATUS_COLUMNS]).setFontWeight('bold');
  }

  sheet.getRange(row, startCol, 1, 4).setValues([[
    status,
    missing.map(function(f){ return f.title; }).join(' · ') || '—',
    syllabus.format + (syllabus.reliable ? '' : ' (unreliable)'),
    new Date()
  ]]);

  // Solid color, no gradient. Red = act, green = done, grey = cannot read.
  var color = status === 'COMPLETE' ? '#e7f1e8'
            : (status === 'UNREADABLE' ? '#eceded' : '#fdeaea');
  sheet.getRange(row, startCol).setBackground(color).setFontWeight('bold');
}

/* ══════════════════════════════════════════════════════════════════════════
   OPTIONAL · weekly digest to the admin
   Set ADMIN_EMAIL and add a weekly time-based trigger for this function.
   ══════════════════════════════════════════════════════════════════════════ */
function weeklyDigest() {
  if (!ADMIN_EMAIL) return;
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  var data = sheet.getDataRange().getValues();
  var head = data[0];
  var sCol = head.indexOf(STATUS_COLUMNS[0]);
  var cCol = head.indexOf(FORM_FIELDS.course);
  var nCol = head.indexOf(FORM_FIELDS.name);
  if (sCol < 0) return;

  var open = data.slice(1).filter(function(r){ return r[sCol] && r[sCol] !== 'COMPLETE'; });
  var rows = open.map(function(r){
    return '<tr><td style="padding:6px 10px;border:1px solid #e2e2e2;">' + (r[nCol]||'') + '</td>'
         + '<td style="padding:6px 10px;border:1px solid #e2e2e2;">' + (r[cCol]||'') + '</td>'
         + '<td style="padding:6px 10px;border:1px solid #e2e2e2;">' + r[sCol] + '</td></tr>';
  }).join('');

  MailApp.sendEmail({
    to: ADMIN_EMAIL,
    subject: 'Syllabus check: ' + open.length + ' still outstanding',
    htmlBody: '<div style="font-family:Georgia,serif;color:#212121;">'
      + '<p>' + open.length + ' syllab' + (open.length===1?'us':'i') + ' still need attention.</p>'
      + (open.length ? '<table style="border-collapse:collapse;font-size:14px;">'
          + '<tr style="background:#C8102E;color:#fff;"><th style="padding:6px 10px;text-align:left;">Instructor</th>'
          + '<th style="padding:6px 10px;text-align:left;">Course</th><th style="padding:6px 10px;text-align:left;">Status</th></tr>'
          + rows + '</table>' : '<p>Everything is clear.</p>')
      + '<p style="font-size:12px;color:#5c5c5c;margin-top:14px;">Full detail is in the response sheet.</p></div>'
  });
}

/* ══════════════════════════════════════════════════════════════════════════
   READ THE APPROVED LANGUAGE, LIVE
   Every paragraph starting "For this N credit..." is an approved statement.
   Read on every run, so a department edit takes effect immediately.
   ══════════════════════════════════════════════════════════════════════════ */
function fetchApprovedStatements_() {
  var body = DocumentApp.openById(APPROVED_DOC_ID).getBody().getText();
  var out = [];
  var paras = body.split('\n');
  for (var i = 0; i < paras.length; i++) {
    var p = paras[i].trim();
    if (/^For this .* credit/i.test(p) && p.length > 80) out.push(p);
  }
  if (!out.length) throw new Error('No approved statements found in the reference doc. Has its format changed?');
  return out;
}

/* ══════════════════════════════════════════════════════════════════════════
   EXTRACT THE SYLLABUS TEXT
   Google Doc  → native, reliable.
   Word .docx  → convert via Drive, reliable.
   PDF         → convert via Drive, NOT reliable for a verbatim check.
   ══════════════════════════════════════════════════════════════════════════ */
function extractSyllabusText_(r) {
  if (!r.fileId) {
    return { text: null, format: 'none', reliable: false,
             note: r.ssUrl
               ? 'You submitted a Syllabus+ PDF URL rather than a file. This checker cannot read that link yet.'
               : 'No syllabus file was attached.' };
  }

  var file = DriveApp.getFileById(r.fileId);
  var mime = file.getMimeType();

  // Google Doc: read directly.
  if (mime === MimeType.GOOGLE_DOCS) {
    return { text: DocumentApp.openById(r.fileId).getBody().getText(),
             format: 'Google Doc', reliable: true, note: '' };
  }

  // Word or PDF: ask Drive to convert to a Doc, read it, then throw the copy away.
  var temp = null;
  try {
    temp = Drive.Files.copy({ title: 'tmp-check-' + Date.now() }, r.fileId, { convert: true });
    var text = DocumentApp.openById(temp.id).getBody().getText();
    var isPdf = (mime === MimeType.PDF);
    return {
      text: text,
      format: isPdf ? 'PDF' : 'Word',
      reliable: !isPdf,
      note: isPdf
        ? 'PDF text extraction is imperfect. A "verbatim" check against extracted PDF text can produce false failures. If this report flags language you know is present, resubmit as a Google Doc or Word file.'
        : ''
    };
  } catch (err) {
    return { text: null, format: mime, reliable: false,
             note: 'Could not convert this file to readable text (' + err.message + ').' };
  } finally {
    if (temp && temp.id) { try { DriveApp.getFileById(temp.id).setTrashed(true); } catch (e2) {} }
  }
}

/* ══════════════════════════════════════════════════════════════════════════
   HELPERS
   ══════════════════════════════════════════════════════════════════════════ */

// Normalize so formatting noise does not cause a false failure.
// Curly quotes, non-breaking spaces, and collapsed whitespace all get flattened.
// This is the difference between a check that works and one people hate.
function normalize_(s) {
  return String(s)
    .replace(/[‘’‛′]/g, "'")
    .replace(/[“”‟″]/g, '"')
    .replace(/[–—]/g, '-')
    .replace(/ /g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .toLowerCase();
}

function readResponse(e) {
  var out = { name:'', email:'', course:'', combined:'', minor:'', start:null, fileId:null, ssUrl:'' };
  if (!e || !e.response) return out;
  out.email = e.response.getRespondentEmail() || '';

  e.response.getItemResponses().forEach(function(ir) {
    var t = ir.getItem().getTitle();
    var v = ir.getResponse();
    if (t === FORM_FIELDS.name)     out.name = v;
    if (t === FORM_FIELDS.course)   out.course = v;
    if (t === FORM_FIELDS.combined) out.combined = v;
    if (t === FORM_FIELDS.minor)    out.minor = v;
    if (t === FORM_FIELDS.ssUrl)    out.ssUrl = v;
    if (t === FORM_FIELDS.start && v) out.start = new Date(v);
    if (t === FORM_FIELDS.upload && v && v.length) out.fileId = v[0];  // file uploads come back as an array of IDs
  });
  return out;
}

function guessProfile_(course) {
  if (!course) return null;
  var prefix = String(course).toUpperCase().split('-')[0].trim();
  return PROFILES[prefix] || null;
}

function fridayOfFirstWeek_(start) {
  if (!start) return null;
  var d = new Date(start);
  var f = new Date(d);
  f.setDate(d.getDate() + ((5 - d.getDay() + 7) % 7));
  return f;
}

function fmtDate_(d) {
  return d ? Utilities.formatDate(new Date(d), Session.getScriptTimeZone(), 'MMMM d, yyyy') : '';
}

function docLink_() {
  return '<a href="https://docs.google.com/document/d/' + APPROVED_DOC_ID + '/edit">Approved seat-hours language</a>';
}

/* ══════════════════════════════════════════════════════════════════════════
   THE REPORT
   ══════════════════════════════════════════════════════════════════════════ */
function sendReport_(r, findings, syllabus) {
  var missing = findings.filter(function(f){ return f.level === 'missing' || f.level === 'blocked'; });
  var ok = missing.length === 0;

  var head = ok ? '#2e7d32' : '#C8102E';
  var title = ok ? 'Thank you for submitting' : 'Almost there, a few items to add';

  var rows = findings.map(function(f) {
    var dot = f.level === 'pass' ? '#2e7d32'
            : (f.level === 'info' ? '#5c5c5c' : '#C8102E');
    return '<div style="border:1px solid #e2e2e2;border-left:5px solid ' + dot + ';border-radius:8px;padding:12px 14px;margin-bottom:8px;background:#fff;">'
         + '<div style="font-weight:700;font-size:14px;color:#212121;margin-bottom:4px;">' + f.title + '</div>'
         + '<div style="font-size:13px;color:#5c5c5c;line-height:1.6;">' + f.body + '</div>'
         + '</div>';
  }).join('');

  var caveat = '';
  if (syllabus.note) {
    caveat = '<div style="background:#eceded;border-left:5px solid #C8102E;border-radius:0 6px 6px 0;padding:12px 14px;margin-bottom:14px;font-size:13px;line-height:1.6;color:#212121;">'
           + '<b>About your file (' + syllabus.format + '):</b> ' + syllabus.note + '</div>';
  }

  var html =
    '<div style="font-family:Georgia,serif;color:#212121;font-size:15px;line-height:1.65;max-width:720px;">'
  + '<div style="background:' + head + ';color:#fff;padding:16px 20px;border-radius:6px;margin-bottom:16px;">'
  + '<div style="font-size:20px;font-weight:700;">' + title + '</div>'
  + '<div style="font-size:13px;margin-top:4px;">' + (r.course || 'your course') + '</div></div>'
  + caveat
  + '<p style="font-size:14px;">Hi ' + (r.name || 'there') + ',</p>'
  + '<p style="font-size:14px;">' + (ok
      ? 'Your syllabus has the approved language it needs. Nothing else is required.'
      : 'Your syllabus is close. Please add the items marked in red, then resubmit.') + '</p>'
  + rows
  + '<p style="font-size:12px;color:#5c5c5c;margin-top:16px;border-top:1px solid #e2e2e2;padding-top:12px;">'
  + 'This is an automated report. It only reads your syllabus, it never changes it. '
  + 'Approved wording is read live from the ' + docLink_() + ', so it is always current. '
  + 'If something here looks wrong, reply and tell me.</p></div>';

  // Instructor only. The admin watches the Sheet, not an inbox.
  MailApp.sendEmail({
    to: r.email,
    subject: (ok ? 'Syllabus received: ' : 'Syllabus needs a few items: ') + (r.course || ''),
    htmlBody: html
  });
}
