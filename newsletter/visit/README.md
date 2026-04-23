# Visit form — setup

The form in `index.html` submits to a Google Apps Script that:
1. Emails `dmarts@gccaz.edu` with the submission
2. Appends a row to your Google Sheet
3. Returns the user to `/newsletter/` after 3 seconds

## One-time setup

1. **Create a Google Sheet** to collect submissions. From its URL, copy the ID:
   `https://docs.google.com/spreadsheets/d/{THIS_PART}/edit`

2. **Open [script.google.com](https://script.google.com)** → New project.
   Paste `apps-script.gs` into `Code.gs`.

3. **Paste your Sheet ID** into `SPREADSHEET_ID` near the top of `Code.gs`.
   (Leave `""` if you only want email and no spreadsheet.)

4. **Deploy** → New deployment → Web app
   - Execute as: **Me**
   - Who has access: **Anyone**
   - Click Deploy. Authorize when prompted.
   - Copy the **Web App URL** it gives you.

5. **Paste that URL** into `visit/index.html`, replacing
   `PASTE_YOUR_APPS_SCRIPT_URL_HERE` (near the top of the `<script>` block).

6. **Test it**: fill out the form on the live page. You should:
   - Get an email at dmarts@gccaz.edu
   - See a new row in the Sheet
   - Be redirected back to `/newsletter/` after a few seconds

## Demo mode

If `ENDPOINT_URL` is still `PASTE_YOUR_APPS_SCRIPT_URL_HERE`, the form shows a
"demo mode" message and logs the payload to the browser console. This lets you
test the UI without the backend wired up.

## Changing the redirect target

In `visit/index.html`, edit `RETURN_URL` and `REDIRECT_DELAY_MS` at the top of
the script block.
