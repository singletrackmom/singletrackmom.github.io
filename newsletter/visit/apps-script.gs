/**
 * Glendale Community College Digital Arts
 * Visit Request Form → Email + Spreadsheet
 *
 * This script does two things when the visit form is submitted:
 *   1. Emails dmarts@gccaz.edu with the form details
 *   2. Appends a row to a Google Sheet
 *
 * Setup instructions are in README.md in the newsletter folder.
 */

// ──────────────────────────────────────────────────────────────────
// CONFIGURATION — edit these values
// ──────────────────────────────────────────────────────────────────

var NOTIFY_EMAIL = "dmarts@gccaz.edu";

// Leave this empty string "" if you're not using a spreadsheet yet.
// To enable spreadsheet logging, create a Google Sheet, copy its ID from
// the URL (the long string between /d/ and /edit), and paste it here.
var SPREADSHEET_ID = "";

var SHEET_NAME = "Visit Requests";

// ──────────────────────────────────────────────────────────────────
// DO NOT EDIT BELOW THIS LINE (unless you know what you're doing)
// ──────────────────────────────────────────────────────────────────

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);

    // 1. Send email notification
    sendNotificationEmail(data);

    // 2. Write to spreadsheet (only if configured)
    if (SPREADSHEET_ID && SPREADSHEET_ID.length > 0) {
      writeToSpreadsheet(data);
    }

    return ContentService
      .createTextOutput(JSON.stringify({ status: "ok" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    // Log the error for debugging
    console.error("Form submission error:", err);
    return ContentService
      .createTextOutput(JSON.stringify({ status: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function sendNotificationEmail(data) {
  var subject = "New Visit Request from " + (data.name || "someone");

  var body = "You have a new visit request for Digital Arts at GCC.\n\n";
  body += "───────────────────────────────\n";
  body += "Name: " + (data.name || "") + "\n";
  body += "Email: " + (data.email || "") + "\n";
  body += "Role: " + (data.role || "") + "\n";

  if (data.school) {
    body += "School / organization: " + data.school + "\n";
  }

  body += "\n";
  body += "Programs of interest: " + (data.programs || "(none specified)") + "\n";
  body += "Group size: " + (data.group_size || "(not specified)") + "\n";
  body += "Availability: " + (data.availability || "") + "\n";

  if (data.notes) {
    body += "\nNotes:\n" + data.notes + "\n";
  }

  body += "───────────────────────────────\n";
  body += "Submitted: " + (data.submitted_at || new Date().toISOString()) + "\n";

  MailApp.sendEmail({
    to: NOTIFY_EMAIL,
    replyTo: data.email || NOTIFY_EMAIL,
    subject: subject,
    body: body
  });
}

function writeToSpreadsheet(data) {
  var ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  var sheet = ss.getSheetByName(SHEET_NAME);

  // Create the sheet if it doesn't exist
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow([
      "Submitted",
      "Name",
      "Email",
      "Role",
      "School",
      "Programs",
      "Group Size",
      "Availability",
      "Notes"
    ]);
    sheet.getRange("A1:I1").setFontWeight("bold");
    sheet.setFrozenRows(1);
  }

  sheet.appendRow([
    data.submitted_at || new Date().toISOString(),
    data.name || "",
    data.email || "",
    data.role || "",
    data.school || "",
    data.programs || "",
    data.group_size || "",
    data.availability || "",
    data.notes || ""
  ]);
}

// Optional: test the script manually from the Apps Script editor.
// Click "Run" with this function selected to verify email delivery works.
function testEmail() {
  sendNotificationEmail({
    name: "Test User",
    email: "test@example.com",
    role: "High school teacher or counselor",
    school: "Test High School",
    programs: "Digital Media Arts, Photography",
    group_size: "15",
    availability: "Wednesday morning, Friday afternoon",
    notes: "This is a test submission.",
    submitted_at: new Date().toISOString()
  });
  Logger.log("Test email sent to " + NOTIFY_EMAIL);
}
