# Glendale Community College Digital Arts Newsletter — Issue 01

## How to deploy to GitHub Pages

1. Upload the entire `newsletter/` folder to the root of your `singletrackmom.github.io` repo
2. Commit and push
3. The newsletter will be live at `https://singletrackmom.github.io/newsletter/`

## Folder structure

```
newsletter/
├── index.html
├── README.md
└── images/
    ├── steamworks-hero.jpg
    ├── stephanie-phoenix.jpg
    ├── gcc-logo.png
    ├── sticker-goggles.png
    ├── sticker-trophy.png
    ├── sticker-clapperboard.png
    ├── sticker-sparkle.png
    └── sticker-money.png
```

## How to send as email

When sending through Mailchimp, Flodesk, or any email platform:

1. Upload the contents of `images/` to the email platform's image library, or host them on GitHub Pages and reference full URLs (e.g. `https://singletrackmom.github.io/newsletter/images/steamworks-hero.jpg`)
2. Paste the HTML from `index.html` into the platform's "Custom HTML" or "Code your own" block
3. Find-and-replace `images/steamworks-hero.jpg` with the full hosted URL, and do the same for all other images
4. Send a test to yourself first to check rendering

## Editing

Text placeholders to fill in before sending:
- `[TOUR URL]` — replace with Schedule-a-Visit form link
- `[REQUEST INFO URL]` — replace with Ask-a-Question form link
- `[ISSUE 01 · Spring 2026]` — issue label
- `[PREVIEW TEXT]` — the preview snippet shown in inbox
- `[UNSUBSCRIBE]` `[PREFERENCES]` `[WEBSITE]` — add these after choosing an email platform (Mailchimp etc. insert them automatically)

## Typography

- Headings: Libre Baskerville (Google Font) with fallbacks to Baskerville, Baskerville Old Face, Hoefler Text, Garamond, Georgia
- Body: Inter (Google Font) with fallbacks to system UI fonts (Segoe UI, Helvetica Neue, Helvetica, Arial)

Both Google Fonts load from `fonts.googleapis.com` when available. If a recipient's email client blocks Google Fonts (e.g., Outlook desktop), the fallback fonts render reliably.
