# GCC Digital Arts Newsletter — Issue 01

This folder is the deployment-ready version of the newsletter. Upload the entire folder to GitHub Pages and it will render correctly.

## Files

```
newsletter/
├── index.html               ← The newsletter itself (open in browser)
├── README.md                ← This file
└── images/
    ├── steamworks-hero.jpg  ← STEAMworks VR cave rendering
    ├── stephanie-lucas.jpg  ← Faculty spotlight portrait
    └── gcc-logo.png         ← GCC logo for the footer
```

## How to deploy

1. Upload the entire `newsletter/` folder to the root of your `singletrackmom.github.io` repo
2. Commit and push
3. The newsletter will be live at: `https://singletrackmom.github.io/newsletter/`

## How to send as email

When you're ready to send through Mailchimp, Flodesk, or another email service:

1. Upload the `images/` folder contents to the email platform's image library (or host them on GitHub Pages and reference the full URLs)
2. Paste the HTML from `index.html` into the platform's "Custom HTML" or "Code your own" block
3. Find-and-replace `images/steamworks-hero.jpg` with the full hosted URL (and similar for the other two images)
4. Send a test to yourself first to check rendering

## Editing the newsletter

Most text is written to be updated each issue. Search `index.html` for `[SQUARE BRACKETS]` to find remaining placeholders (the hero image link, unsubscribe links, etc.).

When writing a new issue, the two feature stories (STEAMworks and Design Studio) should be swapped out for whatever is new. The Faculty Spotlight, Recent Awards, Programs at a glance, and Cost Comparison sections can stay roughly the same with periodic updates.
