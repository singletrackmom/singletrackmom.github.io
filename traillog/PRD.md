# TrailLog · Product Requirements Document

*Working name. Easy to change. The service record that follows your bike.*

> **How to use this file:** This is the single source of truth for the app. If you are building with Claude, start a new Project, paste this whole document into the project knowledge (or just open this file in the chat), and tell Claude “read the PRD, this is what we’re building.” Claude will then understand the product, the users, and the rules without you re-explaining every time.

---

## 1. The one-line pitch

A Carfax for high-end mountain bikes. Every service, at any shop, gets logged against the specific bike, so the maintenance history follows the bike for its whole life (and especially when it gets sold).

## 2. The problem

People buy expensive mountain bikes ($5K to $15K) and do not maintain them on schedule. Suspension forks and rear shocks need service by ride hours, drivetrains and tires wear by miles, and brakes and sealant need attention on a calendar. Most riders track none of this. Bike shops say it constantly: great bikes come in neglected because nobody told the owner what was due or when.

Riders who do not wrench on their own bikes have no easy way to know:
- What service is due, and when, based on how much they actually ride.
- What was done last time, and where.
- Their suspension tune settings (fork and shock setup codes).

## 3. Who it is for

**Primary user: the bike owner who does NOT do their own maintenance.** They own a nice bike, ride regularly, and rely on shops. They want to be told when something is due and to keep a clean history. This is the marketable audience.

**Secondary user: the bike shop.** Shops add verified service entries. This is the trust layer (the “Carfax” part) and the partnership/business angle. A rider can use any shop, but most have two or three regular shops.

## 4. Why it beats Carfax

Carfax is fed by reported events. TrailLog is fed continuously: the **owner** keeps it current every time any service happens, at any shop, and shops can verify entries. So the record is richer and more trustworthy than a vehicle history report, and it raises resale value because a buyer can see the full, verified service history.

## 5. Core features (v1, what the prototype shows)

1. **Pick a bike first.** On open, the rider sees their garage and selects a bike. Each bike has its own profile because forks, shocks, tires, and wear all differ per bike. (Real example: Element, Hayduke, Rail, each tracked separately.)

2. **Mileage from Strava.** Most riders already track miles and ride time in Strava, per bike (Strava “Your Gear” shows miles per bike). TrailLog reads that.
   - **Important nuance:** do NOT use a flat all-time average. Riding is seasonal (more in summer, less in winter). Use a **recent trailing average (about 4 weeks)** to project when service comes due, so the reminders match how the person is riding right now.

3. **Service schedule per bike, by the right unit.**
   - Suspension (fork lowers, fork full, rear shock) is tracked by **ride hours** (miles converted to hours).
   - Drivetrain (chain, brake pads on e-bikes) is tracked by **miles**.
   - Brake bleed, sealant, motor service, bearings are tracked by **calendar months**.
   - Intervals vary by bike make and use (an e-bike wears chains and pads faster than an XC bike).

4. **“When is my next service due?”** Given recent weekly riding, project a date for each item and surface the soonest one. Show a clear status: OK, soon, overdue.

5. **Permanent service history (the Carfax record).** A timeline of every service, with the shop name and a “verified by shop” badge versus “self-logged.” Stays with the bike.

6. **Suspension tune codes.** Every fork and shock has a setup code on a sticker (e.g. RockShox Trailhead QR, Fox serial). Store the code plus the baseline settings (air pressure, rebound clicks, compression clicks, volume spacers/tokens) so the rider never loses their tune and a shop can reproduce it.

7. **Reminders.** Notify the rider when something is coming due, based on their riding pace.

8. **Log any service yourself.** Many owners do a lot of their own work. The rider can record any service on any bike: what was done, the date, whether they did it or a shop did, optional cost, and notes. Logging a tracked item resets that item’s clock.

9. **Receipt photos (the proof layer).** When a shop does the work, the rider snaps a photo of the receipt and attaches it to the entry. This is what makes the history credible and not just self-reported, so it holds up at resale the way Carfax receipts do. Entries show as “Receipt on file,” “Verified by shop,” or “Self-logged, no receipt.”

## 6. Out of scope for v1 (later)

- Real Strava OAuth login and live mileage sync (v1 uses simulated sample data).
- Real accounts and a database so data persists across devices.
- Shop-side dashboard for shops to log and verify directly (v1 lets the rider attach a receipt photo, but the shop does not yet confirm it inside the app).
- Booking a service appointment in-app.
- Push notifications to a phone.

## 6a. Competitive landscape (researched June 2026)

Honest read: the four pieces of this concept all exist somewhere, but no single product combines them for the high-end MTB owner. Be ready to answer “how is this different from SAGLY plus Frame-Book?”

- **SAGLY** (iOS, free + paid tiers, actively updated 2026) is the closest. It does fork/shock setup storage, Strava-synced maintenance reminders, and a change history. It does NOT do shop or receipt verification, and the record does not transfer to a new owner. This is the one to study hardest.
- **ProBikeGarage** (iOS/Android/web, ~$3/mo) is the strongest general maintenance tracker: Strava sync, service intervals, component lifecycle, and receipt/photo attachments (self-uploaded, unverified). No suspension tune fields, no resale transfer.
- **Frame-Book** and **VELOWALLET** chase the “bike passport / service history that follows the bike on resale” angle, including workshop-linked entries and owner-to-owner handoff. Both are general cycling, not MTB, and neither stores suspension tunes.
- **Strava My Gear** (free) tracks per-bike and per-component mileage. It is the data source, not a full competitor.
- Suspension-only apps (FullSquish, ShockPro, etc.) store tunes well but do nothing else.
- Theft registries (**Bike Index**, **Project 529 Garage**) are adjacent. They own bike identity and theft recovery, not service history. More likely partners than competitors.

**The defensible wedge:** MTB-specific, with shop-verified or receipt-backed service records that also store suspension tunes, and that transfer to the next owner to raise resale value. That exact bundle is currently unowned. The moat is thin (SAGLY could add verification; a passport startup could add tunes), and the hard part is bike-shop adoption for verification, which is the same chicken-and-egg problem Frame-Book faces. The realistic v1 value, even before any shop network, is a clean personal record plus receipt photos that make resale honest.

## 7. How the math works (so Claude builds it right)

- **Ride hours** = total miles ÷ average speed. Use about **8.5 mph** for mountain biking (includes climbing). If Strava ride-time is available later, use that directly instead of estimating.
- **Recent weekly pace** = average miles per week over the **last 4 weeks** (not all-time).
- For an **hours-based** item: hours used = current bike hours − hours at last service; weeks until due = (interval − hours used) ÷ (weekly miles ÷ 8.5).
- For a **miles-based** item: miles used = current miles − miles at last service; weeks until due = (interval − miles used) ÷ weekly miles.
- For a **calendar** item: due date = last service date + interval months.
- **Status:** OK under 80 percent of interval, “soon” at 80 to 100 percent, “overdue” over 100 percent.

### Reasonable starting intervals (confirm with a shop before shipping)

| Item | Interval | Tracked by |
|---|---|---|
| Fork lower-leg service | 50 hours | ride hours |
| Fork full service | 200 hours | ride hours |
| Rear shock air-can service | 50 hours | ride hours |
| Chain wear check / replace | 500 to 1000 miles | miles |
| Brake pads (e-bike) | ~400 miles | miles |
| Brake bleed | 12 months | calendar |
| Tubeless sealant refresh | 2 to 3 months | calendar |
| Pivot bearing inspection | 12 months | calendar |
| E-bike motor service | 12 months | calendar |

## 8. Data model (plain English)

A **rider** has many **bikes**. Each **bike** has:
- Identity: name, make/model, year, use type, total miles, recent weekly miles.
- A **fork** and optionally a **rear shock**, each with: model, setup code, and baseline settings (pressure, rebound, compression, tokens).
- A list of **components**, each with: name, interval, unit (hours / miles / months), last-service date, and the miles or hours reading at last service.
- A **history** list of service events, each with: title, date, shop, verified (true/false), and a note.

## 9. Design rules

- Mobile-first, single column, dark theme (riders use it on a phone, often outdoors). The prototype mirrors the look riders already know from Strava.
- **Solid colors only. Never use gradients.** Pick one accent (orange in the prototype) plus green / amber / red for OK / soon / overdue status.
- **No em dashes anywhere.** Use commas, periods, parentheses, or a middot.
- **Use proper curly quotes (“ ” ‘ ’), never straight quotes or prime marks.**
- Keep it scannable. The rider should understand “what is due” in a few seconds.

## 10. Tech approach (beginner-friendly)

- **v1 prototype:** one self-contained HTML file. HTML, CSS, and plain JavaScript in a single file, with the sample data written into the code. No build step, no server, no accounts. You can open it by double-clicking the file, or paste it into Claude as an Artifact and publish a share link.
- **Data for the demo is in memory.** It resets every reload on purpose, so the prototype runs the same as a local file, a published Claude artifact, or on a website later.
- **Hosting (when you are ready to share a real link):**
  - Easiest now: build it as a Claude **Artifact** and click **Publish**. Anyone can open the link, no GitHub needed. (Caveat: artifacts cannot save data between reloads, which is why v1 data is sample data.)
  - Free permanent web address later: a **GitHub Pages** site (free GitHub account, drop in `index.html`, turn on Pages). This also lets data persist with `localStorage`.
- **Next step after v1:** add real Strava login (Strava API, requires registering the app with Strava and a small backend to hold the keys), then real accounts and a database so each rider’s data is saved.

## 11. Build order (suggested for a first app)

1. Get the prototype running and play with it. Understand each screen.
2. Change the sample bikes to your own real bikes and numbers.
3. Adjust the service intervals after talking to a shop.
4. Add a screen to add a new bike from inside the app.
5. Publish it as an artifact and show two or three shop owners. Write down what they say.
6. Only then decide whether to invest in real Strava sync, accounts, and a database.

## 12. Open questions to resolve with shops and riders

- Are the suspension intervals right for the bikes you care about? Shops will tell you fast.
- How do you make a receipt photo trustworthy enough to matter at resale? Photo only, or shop confirms it in-app later?
- What is the real business model: rider subscription, shop partnership/subscription, or shop-branded (shops “own” it and give it to customers)?
- Is the resale-value angle (verified history raises what a used bike sells for) worth leading the marketing with?
- Given SAGLY and Frame-Book already exist, is the MTB + verification + resale + tune bundle a big enough wedge, or is the better play to integrate with a theft registry (Bike Index, Project 529) for bike identity?
