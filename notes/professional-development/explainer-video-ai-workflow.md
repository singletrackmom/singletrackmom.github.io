# Explainer video with AI: script to graphics to two voices (2026)

A practical, affordable path from a finished script to a cartoonish, consistent explainer video with two good AI voices. Built for a designer who wants the AI pieces spelled out.

## Workflow shape
Script → scene breakdown → illustrations → two voice tracks → assembly. Do it in that order. Images and voices can be produced in parallel once the script is broken down, then combined in one editor.

## 1. Script prep (do this before touching any AI tool)
Break the script into beats (one idea = one visual; a 3-minute explainer is 12 to 20 beats). Build a simple shot list, one row per beat:
- Beat number, Voice (A or B, mark every line), Narration text (exact words), Visual description, On-screen text (short), Duration estimate (~150 words/min).

Decide the two-voice logic up front and stay consistent: e.g., Voice A is the guide, Voice B is the curious student. Color-code A and B in the doc so you can see the rhythm. Rebalance if one voice carries almost everything.

Write each visual description like a brief to an illustrator who has never seen your show: subject and action, setting, mood, and a fixed style reminder. Keep recurring character descriptions identical word-for-word across scenes. That repetition is the trick.

## 2. Graphics (consistent cartoon)
Tools worth using in 2026:
- **Ideogram (Character + Style)** — top pick. Upload a reference image to lock a character's face, clothing, and art style across generations; best at text-in-image. Free tier plus a cheap paid plan (~$8-20/mo).
- **Midjourney V7 (Omni Reference, `--oref`, `--ow`)** — most polished cartoon look; subscription ~$10/mo; weaker at text-in-image.
- **A storybook tool (e.g., ToonyStory)** — built to hold one character across many panels; good if the general tools drift.

Pick one and commit. Prompting for consistency:
- Write a one-paragraph **style bible** and paste it into every prompt (flat vector cartoon, thick outlines, cel-shaded, 5-color palette with **exact hex codes**, minimal backgrounds).
- **Lock the palette by naming hex codes**, not "warm colors."
- **Anchor recurring characters with a reference image** (Ideogram Character / Midjourney `--oref`), not just words.
- Generate a **character sheet first** (neutral pose + a few expressions) as your reference and consistency check.
- Keep aspect ratio 16:9 and framing consistent.
- **Text in images:** either use Ideogram, or generate art with no text and add labels later in the editor (usually better, keeps text crisp and editable).
- **Diagrams/charts:** build in Canva/Figma/PowerPoint in your palette, export PNG. Do not fight an image generator for a clean flowchart.

Script-to-storyboard / animation (optional): Google Flow (Storyboard Studio, Veo), mStudio (script to animatic to final), Runway Gen-4.5, Google Veo 3.1 for motion. Recommendation for a first explainer: use consistent stills + light motion in the editor, not full AI animation. Save Veo/Runway for one or two hero shots.

## 3. Voices (two natural narrators)
Tools:
- **ElevenLabs** — quality leader for expressive English; easiest to audition two contrasting voices. Free tier ~10 min (testing only); $5 Starter adds commercial rights (~30 min); $22 Creator ~100k characters.
- **Google Cloud TTS (Chirp 3 HD)** — nearly as good, far cheaper (first 1M characters/month free). A little setup through Google Cloud.
- **Murf** — friendly all-in-one studio with pacing/emphasis and per-word timing; ~$20-30/mo.

Pick two that work together: contrast the timbre (not just gender), match register to roles, avoid two voices with the same pace/pitch, and audition them on the same two-line exchange.

Make them human, not robotic:
- **Feed one beat at a time**, not the whole script.
- Use pacing/emphasis controls: ElevenLabs stability/style sliders; Google/Murf accept SSML (`<break time="400ms"/>`, `<emphasis>`, rate/pitch). A few pauses are the biggest fix.
- Punctuate for breath; regenerate freely; export each voice as its own file named by scene (`S04_VoiceA.wav`).

## 4. Assembly
Editor: **CapCut (free)** is the practical pick (timeline, auto-captions, keyframes). DaVinci Resolve (free) for more control; Descript to edit by transcript.
1. Drop voice clips on the timeline in script order (A and B on separate tracks).
2. Place each illustration above its narration and stretch to match that line's length.
3. Add subtle motion (Ken Burns slow zoom/pan via two keyframes) so stills feel alive.
4. Add on-screen text/labels here in your palette fonts (not baked into images).
5. Add captions (auto, then proofread) — accessibility requirement.
6. Balance audio (consistent voice levels; optional music bed ~ -20 dB under voice; short fades).
7. Export 1080p, 16:9, MP4.

## Fastest path (the stack)
- Script prep: a spreadsheet. Free.
- Illustrations: **Ideogram** paid, Character lock + hex-locked style bible. ~$8-20.
- Voices: **ElevenLabs Starter** ($5) for two voices with commercial rights, generated line by line; or **Google Chirp 3 HD** (effectively free at this volume).
- Diagrams/labels: **Canva/Figma**. Free.
- Assembly: **CapCut**, free, with Ken Burns motion + auto-captions.

Rough total for one video: **~$15-25**, less on free tiers. Cancel monthly subs after the project if you are not making more.

**Two make-or-break moves:** lock your character with a reference image (not just words), and generate voices one beat at a time with deliberate pauses.
