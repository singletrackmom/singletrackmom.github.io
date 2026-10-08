/**
 * AI Opportunity Pipeline, intake backend.
 * One Sheet, one record per request. Requestor columns (A to O) fill from the web form.
 * Assessment columns (P onward) are filled by Michelle and the IT team.
 *
 * Setup: run setup() once. Then Deploy > New deployment > Web app
 * (Execute as: Me, Who has access: Anyone) and paste the /exec URL into the form page.
 */

var SHEET_NAME = 'Requests';
var NOTIFY = true; // email the sheet owner on every new request

// Requestor columns, in order. "key" matches the form field name.
var REQ_COLS = [
  ['ID', null], ['Submitted', null], ['Status', null],
  ['Name', 'name'], ['Email', 'email'], ['College', 'college'], ['Department', 'dept'],
  ['Goal', 'goal'], ['What is getting in the way', 'problem'],
  ['Who is served', 'audience'], ['People affected', 'reach'], ['Who approves', 'approver'],
  ['Success measure', 'measure'], ['Data involved', 'data'], ['Kind of help', 'kind']
];

// Assessment columns, filled by the team.
var ASSESS_COLS = [
  'Privacy gate', 'Security gate', 'Accessibility gate', 'Gates',
  'Impact', 'Confidence', 'Effort (person-weeks)', 'RICE score', 'Rank',
  'Disposition', 'Reason', 'Owner', 'Decision date', 'PRD link'
];

function col_(name) { // 1-based column index by header name
  var all = REQ_COLS.map(function (c) { return c[0]; }).concat(ASSESS_COLS);
  return all.indexOf(name) + 1;
}
function letter_(n) {
  var s = '';
  while (n > 0) { var m = (n - 1) % 26; s = String.fromCharCode(65 + m) + s; n = Math.floor((n - 1) / 26); }
  return s;
}

function setup() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);
  var headers = REQ_COLS.map(function (c) { return c[0]; }).concat(ASSESS_COLS);
  sh.getRange(1, 1, 1, headers.length).setValues([headers]).setFontWeight('bold').setWrap(true).setVerticalAlignment('top');
  sh.setFrozenRows(1);
  sh.setFrozenColumns(1);
  // Requestor block and assessment block get different solid header colors.
  sh.getRange(1, 1, 1, REQ_COLS.length).setBackground('#E8EEF4');
  sh.getRange(1, REQ_COLS.length + 1, 1, ASSESS_COLS.length).setBackground('#F4EBD6');

  var N = 1000;
  function dv(name, list) {
    var rule = SpreadsheetApp.newDataValidation().requireValueInList(list, true).setAllowInvalid(false).build();
    sh.getRange(2, col_(name), N, 1).setDataValidation(rule);
  }
  dv('Status', ['New', 'In discovery', 'Scored', 'Decided']);
  dv('Privacy gate', ['Pending', 'Pass', 'Fail']);
  dv('Security gate', ['Pending', 'Pass', 'Fail']);
  dv('Accessibility gate', ['Pending', 'Pass', 'Fail']);
  dv('Impact', ['3 · Massive', '2 · High', '1 · Medium', '0.5 · Low', '0.25 · Minimal']);
  dv('Confidence', ['100% · High', '80% · Medium', '50% · Low']);
  dv('Disposition', ['Pilot', 'More discovery', 'Use what already exists', 'Training or process change', 'Not an AI problem', 'Declined']);
  var effort = SpreadsheetApp.newDataValidation().requireNumberGreaterThan(0).setAllowInvalid(false)
    .setHelpText('Estimated effort in person-weeks, greater than 0.').build();
  sh.getRange(2, col_('Effort (person-weeks)'), N, 1).setDataValidation(effort);

  // Gate colors
  var gr = sh.getRange(2, col_('Gates'), N, 1);
  sh.setConditionalFormatRules([
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('FAIL').setBackground('#F4D6D6').setRanges([gr]).build(),
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('PASS').setBackground('#D8EBD8').setRanges([gr]).build()
  ]);
  sh.getRange(2, col_('Decision date'), N, 1).setNumberFormat('yyyy-mm-dd');
  sh.getRange(2, col_('Submitted'), N, 1).setNumberFormat('yyyy-mm-dd hh:mm');
  sh.getRange(2, col_('RICE score'), N, 1).setNumberFormat('0.0');
  sh.setColumnWidths(1, headers.length, 140);
  Logger.log('Setup done. Now deploy as a web app.');
}

function formulasFor_(r) {
  var P = letter_(col_('People affected'));
  var g1 = letter_(col_('Privacy gate')), g3 = letter_(col_('Accessibility gate')), G = letter_(col_('Gates'));
  var I = letter_(col_('Impact')), C = letter_(col_('Confidence')), E = letter_(col_('Effort (person-weeks)'));
  var S = letter_(col_('RICE score')), R = letter_(col_('Rank'));
  var gates = '=IF(COUNTIF(' + g1 + r + ':' + g3 + r + ',"Fail")>0,"FAIL",IF(COUNTIF(' + g1 + r + ':' + g3 + r + ',"Pass")=3,"PASS","PENDING"))';
  var rice = '=IF(AND(' + G + r + '="PASS",ISNUMBER(' + P + r + '),' + I + r + '<>"",' + C + r + '<>"",ISNUMBER(' + E + r + ')),' +
    P + r + '*VALUE(LEFT(' + I + r + ',FIND(" ",' + I + r + ')-1))*(VALUE(LEFT(' + C + r + ',FIND("%",' + C + r + ')-1))/100)/' + E + r + ',"")';
  var rank = '=IF(' + S + r + '="","",COUNTIF($' + S + '$2:$' + S + '$2000,">"&' + S + r + ')+1)';
  return { gates: gates, rice: rice, rank: rank };
}

function clean_(v) {
  v = String(v == null ? '' : v).trim().slice(0, 2000);
  return /^[=+\-@]/.test(v) ? "'" + v : v; // block formula injection
}

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    var p = e.parameter || {};
    if (p.website) return json_({ ok: true }); // honeypot
    var sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
    var r = sh.getLastRow() + 1;
    var row = REQ_COLS.map(function (c) {
      var k = c[1];
      if (!k) return '';
      var v = (e.parameters && e.parameters[k]) ? e.parameters[k].join(', ') : '';
      if (k === 'reach') {
        var n = parseFloat(v); return isNaN(n) ? '' : n;
      }
      return clean_(v);
    });
    row[0] = 'AIP-' + ('000' + (r - 1)).slice(-3);
    row[1] = new Date();
    row[2] = 'New';
    sh.getRange(r, 1, 1, row.length).setValues([row]);
    var f = formulasFor_(r);
    sh.getRange(r, col_('Gates')).setFormula(f.gates);
    sh.getRange(r, col_('RICE score')).setFormula(f.rice);
    sh.getRange(r, col_('Rank')).setFormula(f.rank);
    sh.getRange(r, col_('Privacy gate'), 1, 3).setValues([['Pending', 'Pending', 'Pending']]);
    if (NOTIFY) {
      try {
        MailApp.sendEmail(Session.getEffectiveUser().getEmail(), 'New AI request ' + row[0] + ', ' + row[6],
          'From: ' + row[3] + ' (' + row[4] + ')\n' + row[5] + ', ' + row[6] +
          '\n\nGoal: ' + row[7] + '\n\nWhat is getting in the way: ' + row[8] +
          '\n\nWho is served: ' + row[9] + '\nPeople affected: ' + row[10] +
          '\nWho approves: ' + row[11] + '\nSuccess measure: ' + row[12] +
          '\nData involved: ' + row[13] + '\nKind of help: ' + row[14] +
          '\n\nOpen the Sheet to assess it: ' + SpreadsheetApp.getActiveSpreadsheet().getUrl());
      } catch (err) {}
    }
    return json_({ ok: true, id: row[0] });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
