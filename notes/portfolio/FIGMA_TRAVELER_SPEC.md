# Figma build spec, The Traveler interactive

Written 17 Aug 2026, during the EAB Product Experience Designer application.
When Michelle says &ldquo;the Figma project,&rdquo; this is the file.

---

## Goal

Produce one public Figma file that proves visual craft, component thinking, and
prototyping ability, because that is the single gap standing between this
application and a clean advance. Both simulated reviewers on the EAB hiring panel
independently said the same thing: Figma is claimed in the packet and never shown,
and one real file flips their scores without further discussion.

## Audience

The EAB portfolio review, which happens after the phone screen. Specifically a
Principal Product Designer acting as a craft gate. Secondarily every future
design application, since this file fills the same hole everywhere.

## Process

Take the existing Traveler print brand, which already lives on a Miro board, and
derive a digital system from it: named styles, a component library with variants,
six screens, and a click-through prototype. Roughly four to five focused hours.

---

## Why The Traveler, and not CopaMigo

The posting says: *&ldquo;Build and maintain reusable prototype assets utilizing
EAB&rsquo;s design system, component libraries, and modern prototyping platforms.&rdquo;*

Read literally, the job is: **someone hands you a design language you did not
create, and you build assets inside it.** The Traveler rehearses exactly that task
with real source material. Designing CopaMigo in Figma would be working inside a
system Michelle already owns, which does not test the same skill, and the
portfolio already documents CopaMigo six different ways.

Three more reasons:

1. **It fixes the weakest score.** Visual design came in at 2.5, the lowest on the
   rubric. The whole portfolio is utilitarian tool UI in one plum-and-sage palette.
   The Traveler is art-directed editorial work.
2. **It carries third-party validation.** Pinnacle Award for College Literary
   Magazine (2015, 2016, 2025) and AIGA Best of Phoenix selections (2017 to 2022).
   Visual craft is the one thing that cannot be asserted into existence.
3. **It was already wanted.** An interactive Traveler has been on the list. This
   is not throwaway work.

### The authorship line, say it exactly this way

Michelle is the **design faculty advisor** and has been since 2011, Volumes 44 to 58.
She coaches the student design team through branding theme, design and typography,
print production, and launch. She has nothing to do with the editorial side or the
art competition.

So the framing is:

> The print brand is student work produced under my art direction across fifteen
> volumes. What I built here is the digital system derived from it: the component
> library, the responsive behaviour, and the interactive prototype.

Deriving a system from someone else&rsquo;s design language **is** the job description.
The authorship question is the story, not a risk.

---

## The build

### Page 1, Cover

Title, one line on what the file is, the role statement above, the source
(Volume NN print brand, Miro board), and the date.

### Page 2, Foundations

Pull real values off the Miro board. Do not invent any of these.

**Color styles**, named with slashes so they group into folders:

| Style name | Source |
|---|---|
| `ink` | body text colour from the volume palette |
| `paper` | background stock colour |
| `accent/primary` | the volume&rsquo;s lead accent |
| `accent/secondary` | the supporting accent |
| `rule` | hairline and divider colour |

**Text styles**, using the magazine&rsquo;s real typefaces:

`Display` · `Title` · `Byline` · `Body` · `Pull quote` · `Caption` · `Folio`

Add one short note per group saying **why**: why this face for body copy, why this
measure, why this leading. That annotation is what separates a designer from
someone who moved swatches around.

### Page 3, Components

This is the page that scores. Build each, then `Cmd+Option+K`.

| Component | Property and variants | Why it matters |
|---|---|---|
| **Piece card** | `type` = poem / prose / art | Three variants of one component is the highest-value object in the file |
| **Pull quote** | `align` = left / center | Type hierarchy thinking |
| **Figure** | `size` = inset / full-bleed | Editorial layout judgment |
| **Contributor card** | `state` = compact / expanded | Reusable pattern |
| **Masthead** | `mode` = issue / archive | Navigation treated as a component |

Lay them out in a tidy grid with a `Label` heading over each group. This page alone
is what a design-systems reviewer opens first.

### Page 4, Screens

Press **F**, draw frames at **390 × 844**. Six frames, a real literary magazine
information architecture:

1. **Issue landing.** Cover art, volume number, one line of invitation.
2. **Contents.** Piece cards, all three variants visible together.
3. **A poem.** The hard one, and the one to spend care on. Line breaks in poetry
   carry meaning, and responsive layout destroys them. Solving that on a 390px
   screen is a genuine craft demonstration.
4. **A prose piece.** With a pull quote and an inset figure.
5. **An artwork.** Full-bleed with caption, image-forward treatment.
6. **Contributors.** The card in both states.

Use components for everything. If you catch yourself drawing a card by hand, stop
and place the component instead.

### Page 5, Print to screen

Two frames side by side: a print spread from the Miro board, and the screen
translation. One sentence under each naming what had to change and why. This is the
before-and-after page, and reviewers weight it heavily because it proves
translation judgment rather than a first draft that happened to look fine.

### Prototype

Prototype tab. Wire 1 → 2 → 3 → 4 → 5 → 6, add a back arrow on each frame, set
**Device: iPhone 14**, press play and click all the way through. If it plays, done.

### Share

Share → **Anyone with the link** → **can view**. Copy the link. It goes in the
resume header and in the cover letter&rsquo;s prototype bullet. Ask Claude to rebuild
the application PDF afterward.

---

## What to be able to say about it

- &ldquo;Every colour and type value is a named style, so a change propagates.&rdquo;
- &ldquo;The piece card is one component with three variants, not three cards.&rdquo;
- &ldquo;The brand is student work I art-directed. The system derived from it is mine,
  and that is the same thing you would ask me to do inside EAB&rsquo;s library.&rdquo;
- &ldquo;The poem screen is where I started, because line breaks carry meaning and
  responsive layout destroys them.&rdquo;

## What would make it worse

Twenty screens at seventy percent. A craft gate grades this as design work, not as
proof you opened the app. Six careful frames and a real component page beat a big
messy file every time. Do not build it the night before, and do not hold the
application waiting for it.
