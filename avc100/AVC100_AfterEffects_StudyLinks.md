# After Effects · Study Links (AVC100 Social Media Animation)

**Goal:** Get me (Michelle) up to speed fast enough to record the AVC100 Social Media Animation build video. The assignment is now: import the postcard PSD as a Composition, slide the animal and the type into frame with two Position keyframes each, export an MP4. No template, no from-scratch comp, no animating the animal itself.

**Audience:** Just me. A designer who knows Illustrator and Photoshop cold and is new to After Effects.

**Process:** Watch fundamentals in the current version of the software, not Instagram-story tutorials. The story-template genre teaches masks, shape reveals, and trim paths, which is three times harder than what I am teaching and none of it is in my rubric. Learn the one skill, record my own screencast, and my video becomes the up-to-date one.

---

## The one thing the whole project rests on

The slide-in is **two Position keyframes**: the layer starts just off the edge of the frame and ends where it should sit. Same technique for the animal and for the type. Teach it once, reuse it.

This has not changed in over a decade. Any tutorial, any year, describes it the same way: select the layer, press **P**, click the stopwatch, drag off-frame, move the playhead, drag to its resting spot.

Keys I will use on camera: **P** Position · **S** Scale · **spacebar** preview · **N** end of work area.

---

## 1. Fundamentals, current version (watch these)

- **Learn Adobe After Effects in 1 Hour, Complete Beginner Course 2026:** https://www.youtube.com/watch?v=DWcGNub-yqk
  The main one. Current UI. I only need the first stretch: compositions, layers, keyframes, and export. Roughly 20 minutes of it covers everything my assignment goes near.

- **Learn After Effects in 10 Minutes, Beginner Tutorial:** https://www.youtube.com/watch?v=2nGwjjXJx8E
  Fast orientation if I want the panel tour before the longer one.

- **Adobe Learn, After Effects:** https://www.adobe.com/learn/after-effects
  Adobe's own. Always matches the shipping version, so zero risk of stale UI.

## 2. The single skill, written out

- **School of Motion, How to Set Keyframes:** https://www.schoolofmotion.com/blog/how-to-set-keyframes-after-effects
- **Animating text (Adobe Help):** https://helpx.adobe.com/after-effects/using/animating-text.html

## 3. Export, and the thing my script currently gets wrong

- **Exporting H.264 from the After Effects Render Queue (Adobe):** https://helpx.adobe.com/after-effects/using/exporting-h264-from-the-after-effects-render-queue.html

My assignment still routes students through **Adobe Media Encoder**. After Effects can now render H.264 (MP4) straight from its own Render Queue: **File › Export › Add to Render Queue**, then in **Output Module** set **Format: H.264**. One app instead of two, and it removes the biggest beginner failure point ("Media Encoder opened and I don't know what this is"). Adobe warns direct H.264 render is slow on heavy projects. Mine is a five-second vertical animation, so that warning does not apply.

**Decide before I record:** whichever way I demo is the way it gets baked into the video.

---

## Build recipe (matches the current assignment)

1. **File › Import › File.** Choose the postcard PSD. Set **Import As: Composition.** Layers come in separated.
2. **Double-click the comp** in the Project panel. It opens already vertical at the postcard's size.
3. **Animal:** select the layer, press **P**. Playhead at start, click the **stopwatch**, drag the animal off the edge it comes in from. Move ahead about 1 second, drag it to its resting spot. Two keyframes. It slides in.
4. **Type:** same four moves, entering from the other side, matching the storyboard.
5. **Spacebar** to preview. **N** to set the end of the work area.
6. **Export** to MP4 (Render Queue › Output Module › H.264, or Media Encoder, pending the decision above). Set the Output File location so the file is findable.

---

## Open issues on the assignment itself

- **No duration is specified anywhere.** Not in the assignment text, not in either rubric. Import-as-Composition inherits the PSD's default comp length, so students will export inconsistent lengths with dead air. Add a line: "your finished animation should be about 5 seconds." Then the **N** trim has a target.
- **Two versions of this assignment exist in the repo.** `AVC100_SocialMediaAnimation_ForCanvas.md` is current (no template). `AVC100_All_Projects_and_Exercises.md` still has the old template version. Copying from the wrong file re-posts the template assignment by accident.
- **"Make It Move"** was cut from the assignments but still appears in `AVC100_All_Video_Scripts.md` and `AVC100_Schedule.md` (Tue Jul 7).
- **No Behance video** exists. The portfolio assignment is due Tue Jul 14 and has no script.

## What I deliberately cut

The old Instagram-story template tutorials and the "build a reusable template" course are gone. There is no template in this assignment anymore, and the story-template genre teaches effects my students will never touch. If I bring a template back for a warm-up exercise later, that is a separate search.
