# Glendale Community College Digital Arts Newsletter — Issue 01

## How to deploy to GitHub Pages

1. Upload the entire `newsletter/` folder to the root of your `singletrackmom.github.io` repo
2. Commit and push
3. The newsletter will be live at `https://singletrackmom.github.io/newsletter/`
4. The visit request form will be live at `https://singletrackmom.github.io/newsletter/visit/`

## Folder structure

```
newsletter/
├── index.html              ← the newsletter
├── README.md
├── images/                 ← newsletter images
│   ├── steamworks-hero.jpg
│   ├── stephanie-phoenix.jpg
│   ├── gcc-logo.png
│   └── sticker-*.png       (6 hand-drawn stickers)
└── visit/
    ├── index.html          ← the visit request form
    └── apps-script.gs      ← Google Apps Script for handling submissions
```

## Setting up the visit form

The form at `/newsletter/visit/` sends submissions to `dmarts@gccaz.edu` using a free Google Apps Script. It also optionally writes every submission to a Google Sheet. Setup takes about 10 minutes.

### Step 1 — Create the Apps Script

1. Go to [script.google.com](https://script.google.com) and sign in with a Google account (whichever account runs the script is the account that will send the email)
2. Click **New project**
3. Delete the placeholder code in `Code.gs`
4. Open `visit/apps-script.gs` from this folder, copy all of it, paste into the Apps Script editor
5. At the top of the script, verify `NOTIFY_EMAIL` is set to `dmarts@gccaz.edu`
6. Leave `SPREADSHEET_ID` empty for now — we'll fill this in later if/when you want spreadsheet logging
7. Click the disk icon to save. Name the project "GCC Digital Arts Visit Form" or similar

### Step 2 — Deploy the Apps Script as a Web App

1. In the Apps Script editor, click **Deploy → New deployment**
2. Click the gear icon next to "Select type" and choose **Web app**
3. Fill in:
   - Description: "Visit form submissions"
   - Execute as: **Me**
   - Who has access: **Anyone** (required — this lets the form submit without asking users to sign in)
4. Click **Deploy**
5. Google will ask you to authorize the script. Click through the permissions (it needs access to send email from your account)
6. After deploying, Google gives you a **Web app URL** — it looks like `https://script.google.com/macros/s/XXXXXX.../exec`
7. **Copy that URL**

### Step 3 — Wire the URL into the form

1. Open `visit/index.html` in a text editor
2. Find this line near the bottom (inside the `<script>` tag):
   ```
   var ENDPOINT_URL = "PASTE_YOUR_APPS_SCRIPT_URL_HERE";
   ```
3. Replace `PASTE_YOUR_APPS_SCRIPT_URL_HERE` with the Web app URL you copied
4. Save, commit, push

### Step 4 — Test it

1. Go to `https://singletrackmom.github.io/newsletter/visit/`
2. Fill out the form and submit
3. Within a minute you should receive an email at `dmarts@gccaz.edu` with the submission details
4. If nothing arrives, check spam, then check the Apps Script editor's **Executions** tab for errors

### Step 5 (later) — Add spreadsheet logging

Once you're getting submissions, it's easy to also save them to a spreadsheet:

1. Create a new Google Sheet at [sheets.google.com](https://sheets.google.com)
2. Copy the ID from the URL — the long string between `/d/` and `/edit`. Example URL: `https://docs.google.com/spreadsheets/d/1AbCDeFgHiJkLmNoP/edit` → ID is `1AbCDeFgHiJkLmNoP`
3. In the Apps Script editor, paste that ID into `SPREADSHEET_ID`
4. Save the script. That's it — new submissions will now be logged to the sheet AND emailed. The script creates the headers automatically on first write.

## Editing the form

To change the questions, edit `visit/index.html` directly:
- Find the `<form>` tag
- Add or remove `<div class="field">` blocks as needed
- Match the existing structure for consistent styling

If you add or rename fields, also update the `apps-script.gs` to handle the new data. In `sendNotificationEmail()` and `writeToSpreadsheet()`, add the new field names.

## Editing the newsletter

Text placeholders in the newsletter to fill in before sending by email:

- `[REQUEST INFO URL]` — the "Ask a Question" secondary CTA (next to Schedule a Visit)
- `[ISSUE 01 · Spring 2026]` — the issue label in the header
- `[PREVIEW TEXT]` — the inbox preview snippet
- `[UNSUBSCRIBE]` `[PREFERENCES]` `[WEBSITE]` — these are inserted automatically by most email platforms (Mailchimp, Flodesk, etc.)

The "Schedule a Visit" button already points to `/newsletter/visit/` on your GitHub Pages site.

## How to send as email

When sending through Mailchimp, Flodesk, or any email platform:

1. Upload the contents of `images/` to the email platform's image library, or host them on GitHub Pages and reference the full URLs (e.g. `https://singletrackmom.github.io/newsletter/images/steamworks-hero.jpg`)
2. Paste the HTML from `index.html` into the platform's "Custom HTML" or "Code your own" block
3. Find-and-replace `images/steamworks-hero.jpg` with the full hosted URL, and do the same for all other images
4. Send a test to yourself first to verify rendering

## Typography

- Headings: Libre Baskerville (Google Font) with fallbacks to Baskerville, Baskerville Old Face, Hoefler Text, Garamond, Georgia
- Body: Inter (Google Font) with fallbacks to system UI fonts (Segoe UI, Helvetica Neue, Helvetica, Arial)

Both fonts load from `fonts.googleapis.com` when available. If an email client blocks Google Fonts (Outlook desktop commonly does), the fallback fonts render reliably.
