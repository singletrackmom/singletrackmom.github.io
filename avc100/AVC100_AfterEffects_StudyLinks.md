# After Effects · Study Links (AVC100 Social Media Animation)

**Goal:** Get me (Michelle) up to speed fast enough to teach the AVC100 social media story project: a vertical 1080 × 1920 animated post where a student slides their own image and text into frame over a video background.

**Audience:** Just me, tonight. A designer who knows Illustrator and Photoshop cold but is new to After Effects.

**Process:** Watch in order. Start with the one core skill (text/image sliding in over a background), then the template question, then the eagle/animal fly-across only if I keep that piece. Sizing is settled: every comp is 1080 × 1920, 30 fps, vertical.

---

## The one thing the whole project rests on

The "slide in" is two Position keyframes: the layer starts just off the edge of the frame, and ends where it should sit. That single technique works the same for text, an image, or an animal. Teach it once, reuse it everywhere.

Keys students will touch: **P** for Position, **S** for Scale, **T** for the Text tool, **spacebar** to preview, **N** to trim the work area before export.

---

## 1. Core skill: text and image animating over a video background

- Create Animated Instagram Stories in After Effects (no plugins): https://www.youtube.com/watch?v=GR54SI_hG_w

This is the closest match to the project. Beginner, vertical story format, no paid add-ons.

## 2. If I decide to build a drop-in template

- How to Create an Instagram Story Template in After Effects (Envato Tuts+): https://www.classcentral.com/course/youtube-how-to-create-an-instagram-story-template-in-after-effects-136448

About 49 minutes. The only one that actually teaches building a reusable template (placeholder layers, pre-comps) rather than a one-off animation. Only needed if I keep the template approach.

## 3. The eagle / animal flying across the scene

- Flying Bird Animation for Beginners (no plugins): https://www.youtube.com/watch?v=sOVBYlLx4Cs
- Animate a Bird in 5 Minutes: https://www.youtube.com/watch?v=jFf4jHKZ-Tg

Bring in the animal as a transparent PNG (or a clip with alpha), then set two Position keyframes so it crosses the frame. Skip this section entirely if the animal doesn't need to enter the composition.

## 4. Adobe's own reference (when I want the official version)

- Animating text (Adobe Help): https://helpx.adobe.com/after-effects/using/animating-text.html

---

## Quick build recipe (from scratch, no template)

1. Composition › New Composition. 1080 wide, 1920 tall, 30 fps, 10 seconds. Name it.
2. File › Import › File. Bring in the video. Drag it to the timeline. Press **S** to scale it up until it fills the tall frame (some cropping is normal).
3. Text tool (**T**), click in the frame, type. Or import an image and drop it above the video.
4. Select the layer, press **P** for Position. At frame 0, click the stopwatch and drag the layer just off one edge. Move to about 1 second, drag it to its resting spot. Two keyframes: it slides in.
5. Press **N** to trim the work area. Composition › Add to Adobe Media Encoder Queue › H.264 › export MP4.
