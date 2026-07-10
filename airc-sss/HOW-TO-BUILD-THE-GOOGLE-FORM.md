# Build the Google Form (replaces the Jotform) — 2 minutes, no Terminal

The builder script is in this same folder: **`Create_Barrier_Log_Form.gs`**
It creates the Google Form AND a linked responses spreadsheet, collects no PII (initials only), and includes every task.

## Steps
1. Go to **script.google.com**, signed into the Google account you want the form on (your **personal Gmail** is simplest, since your other form lives there).
2. Click **New project** (top left).
3. It shows sample code (`function myFunction()...`). Select all of it and **delete** it.
4. Open **`Create_Barrier_Log_Form.gs`** (in this folder), select all, copy, and paste it into the empty editor.
5. Click the **save** icon (floppy disk).
6. At the top, make sure the function dropdown says **createBarrierLogForm**, then click **Run (▶)**.
7. First time only, a permissions popup: **Review permissions** → pick your account → you'll see **"Google hasn't verified this app"** (normal for your own script) → **Advanced** → **Go to [project] (unsafe)** → **Allow**. It's your own code, it's safe.
8. Look at the **Execution log** at the bottom. It prints three links:
   - **Form to fill out** (the one you share with reps)
   - Form to edit
   - Responses sheet (your live Barrier Log)
9. **Copy the "Form to fill out" link and paste it to Claude.** Claude will swap it in for the Jotform on the test-plan page and the agenda, and retire the Jotform everywhere.

## What's still pointing at the old Jotform (to update once the Google Form exists)
- `airc-sss/test-plan.html` (the button + URL near the bottom)
- The meeting agenda / running-minutes doc
- `airc-sss/WORKING-STATE.md` note about the live form
