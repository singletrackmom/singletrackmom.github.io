/**
 * Glendale Community College Digital Arts
 * Connect Form → Email Notification + Google Spreadsheet
 *
 * Handles four contact types:
 *   - campus_tour   : Studio tour on scheduled date
 *   - virtual_tour  : Live video walkthrough
 *   - outreach      : Faculty visits their location
 *   - more_info     : General question / request for info
 *
 * Setup:
 *   1. Open script.google.com → New project → paste this file
 *   2. Create a Google Sheet. Copy its ID from the URL
 *      (the long string between /d/ and /edit) and paste below.
 *   3. Deploy → New deployment → Web app
 *      - Execute as: Me
 *      - Who has access: Anyone
 *   4. Copy the Web App URL and paste it into visit/index.html
 *      where it says PASTE_YOUR_APPS_SCRIPT_URL_HERE.
 *   5. Run testEmail() once to verify email delivery works.
 *      (You'll need to authorize the script on first run.)
 */

// ── CONFIGURATION ───────────────────────────────────────────────
var NOTIFY_EMAIL   = "dmarts@gccaz.edu";

// Paste your Google Sheet ID here (leave "" to skip spreadsheet logging)
var SPREADSHEET_ID = "1vVGuh0xW2cUvxPmR4uMha4ODwrqT8Eg_KVE19-eOZdY";

// Name of the tab inside the sheet
var SHEET_NAME = "Connect Requests";
// ────────────────────────────────────────────────────────────────


function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    sendNotificationEmail(data);
    if (SPREADSHEET_ID && SPREADSHEET_ID.length > 0) {
      writeToSpreadsheet(data);
    }
    return ContentService
      .createTextOutput(JSON.stringify({ status: "ok" }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    console.error("Form error:", err);
    return ContentService
      .createTextOutput(JSON.stringify({ status: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}


function sendNotificationEmail(data) {
  var typeLabels = {
    "campus_tour":  "Campus Tour Request",
    "outreach":     "Outreach Presentation Request",
    "more_info":    "Information Request"
  };

  var typeLabel = typeLabels[data.connect_type] || "Contact Request";
  var subject = typeLabel + " — " + (data.name || "someone");

  var body = "New " + typeLabel.toLowerCase() + " via the Digital Arts newsletter.\n\n";
  body += "──────────────────────────────\n";
  body += "Name:  " + (data.name  || "") + "\n";
  body += "Email: " + (data.email || "") + "\n";
  if (data.role)       body += "Role:  " + data.role + "\n";
  if (data.group_size) body += "Group size: " + data.group_size + "\n";

  body += "\n";

  // Type-specific details
  if (data.connect_type === "campus_tour") {
    body += "Type: Campus tour\n";
    body += "Requested date: " + (data.tour_date || "(not specified)") + "\n";
  }

  if (data.connect_type === "outreach") {
    body += "Type: Outreach presentation\n";
    body += "Location: " + (data.outreach_location || "(not specified)") + "\n";
    body += "Timing: " + (data.outreach_timing || "(not specified)") + "\n";
  }

  if (data.connect_type === "more_info") {
    body += "Type: Information request\n";
    body += "Question:\n" + (data.info_question || "(none)") + "\n";
  }

  if (data.notes) {
    body += "\nAdditional notes:\n" + data.notes + "\n";
  }

  body += "\n──────────────────────────────\n";
  body += "Submitted: " + (data.submitted_at || new Date().toISOString()) + "\n";

  MailApp.sendEmail({
    to: NOTIFY_EMAIL,
    replyTo: data.email || NOTIFY_EMAIL,
    subject: subject,
    body: body
  });
}


function writeToSpreadsheet(data) {
  var ss    = SpreadsheetApp.openById(SPREADSHEET_ID);
  var sheet = ss.getSheetByName(SHEET_NAME);

  // Create sheet with headers if it doesn't exist yet
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow([
      "Submitted",
      "Type",
      "Name",
      "Email",
      "Role",
      "Group Size",
      "Tour Date",
      "Outreach Location",
      "Outreach Timing",
      "Info Question",
      "Notes"
    ]);
    sheet.getRange("A1:L1").setFontWeight("bold");
    sheet.setFrozenRows(1);
  }

  sheet.appendRow([
    data.submitted_at            || new Date().toISOString(),
    data.connect_type            || "",
    data.name                    || "",
    data.email                   || "",
    data.role                    || "",
    data.group_size              || "",
    data.tour_date               || "",
    data.outreach_location       || "",
    data.outreach_timing         || "",
    data.info_question           || "",
    data.notes                   || ""
  ]);
}


// ── TEST FUNCTIONS (run from the Apps Script editor to verify) ──

function testCampusTour() {
  sendNotificationEmail({
    connect_type: "campus_tour",
    name: "Maria Gonzalez",
    email: "mgonzalez@glendaleunion.edu",
    role: "High school teacher or counselor",
    group_size: "22",
    tour_date: "October 14, 2026",
    notes: "We're a graphic design class. Interested in seeing the DMA lab especially.",
    submitted_at: new Date().toISOString()
  });
  Logger.log("Test campus tour email sent to " + NOTIFY_EMAIL);
}

function testOutreach() {
  sendNotificationEmail({
    connect_type: "outreach",
    name: "Jennifer Reyes",
    email: "jreyes@highschool.edu",
    role: "High school teacher or counselor",
    group_size: "30",
    outreach_location: "Deer Valley High School, Phoenix AZ",
    outreach_timing: "Any Thursday in February",
    submitted_at: new Date().toISOString()
  });
  Logger.log("Test outreach email sent to " + NOTIFY_EMAIL);
}

function testInfoRequest() {
  sendNotificationEmail({
    connect_type: "more_info",
    name: "Alex Kim",
    email: "alexk@gmail.com",
    role: "Parent or guardian",
    info_question: "Does the animation program have a transfer agreement with ASU? And what software do students use?",
    submitted_at: new Date().toISOString()
  });
  Logger.log("Test info-request email sent to " + NOTIFY_EMAIL);
}
