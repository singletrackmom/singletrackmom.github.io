# Van Power & Solar · Master Question Doc

**Goal:** Keep every solar and power decision in one place so nothing gets lost between me and my van converter (Tom at New Life Conversions), and so I can reliably run my gear and charge my devices without killing the battery, on a limited budget.

**Audience:** Me, plus Tom / New Life Conversions. The "Questions for Tom" section is meant to be handed to him directly.

**Process:** Capture the system, lock in decisions, list open questions, and check the math once I know real battery, solar, and Dometic numbers.

---

## Context / where things stand

- New Life Conversions (Tom Birk) is doing the electrical. They're cleaning up a mess from VanLife Customs, who installed a 1000W inverter I didn't want and were supposed to wire the Dometic straight to the battery but never did.
- The van is a 10-year-old, 135K-mile rig. This is a **stopgap** setup to make it functional until I can get a newer 4WD van. Budget is tight (teacher, 3 kids in college).
- I move the van every few days, so the alternator can help recharge while driving.

---

## The Quote · Estimate #612 ($6,696.13, sent Jun 17, valid 10 days so technically expired)

**What it covers**

- Fridge + Starlink DC work: hardwire Dometic to 12V, protected DC circuits, Starlink Mini setup with on/off switch, DC fuse block. Materials $432 + labor 10 hrs ($1,650) = ~$2,082.
- Solar: 2 rigid roof panels, brackets, roof entry gland, MC4 cabling, Victron SmartSolar MPPT controller, breakers. Materials $1,189 + labor 17 hrs ($2,805) = ~$3,994.
- Plus card/ACH fee and AZ tax. Deposit to start: 29% materials = $1,941.88.

**What it does NOT cover (the important gaps)**

- No battery. The damaged marine cell stays. Solar has nothing good to charge into.
- No DC-to-DC alternator charger.
- No laptop charging. Says explicitly "no labor spent on Goal Zero recharge point." After $6,696 I still can't charge the MacBook efficiently.

**Read:** ~65% of the quote is solar. Solar is fine for me (see below), but the keystone I actually need, a battery, isn't in it. Scope drifted from my original solar-first email. Need to re-quote with the gaps added.

---

## My real usage (this sizes everything)

- **Fridge (Dometic):** the only all-the-time load. Often I run only the cooler side, not the freezer. Runs less in cold weather. (I've been running it half-on partly because the battery dies so fast, that's the battery's fault, not the fridge.)
- **Everything else is intermittent and rarely simultaneous:** Maxxair fan, one laptop, phones, Starlink, only when I'm working/parked.
- **Heater (Webasto):** basically never a factor. ~4 nights a year in winter, never while other things run.
- **I move the van every few days,** so the alternator can recharge.

This is a light, fridge-dominant load, so a **modest battery** (likely ~100Ah / ~1,280Wh LiFePO4) is probably plenty. **I'm in Colorado most of the year (cooler), only in AZ heat for work trips**, so the fridge runs on the low end most of the time. Caveat: the CFX5 95DZ can be hungry if fully used (rated ~123Ah/day both zones moderate, up to ~205Ah/day in heat with the freezer on), but that's an occasional-AZ ceiling, not my normal. 100Ah works only if I baby it (one zone, cool weather). **But I bought this fridge to run it fully, including the freezer**, so I actually want the biggest battery that fits under the seat (~200Ah if it fits) plus enough solar. The under-seat space is the gating limit, need Tom to measure it. **Option if more won't fit under the seat: build a battery box under the bed** (removing the inverter frees space), which could allow 200Ah+ for real full-fridge use. If rooftop solar can't keep up, a tiltable/portable panel as a supplement is on the table.

---

## The guiding principle

1. **Spend on what transfers to the next van.** The LiFePO4 battery, a DC-to-DC alternator charger, and USB-C gear all move to the next rig, 100%. The roof panels + Victron controller are semi-transferable if they're rail-mounted with just a cable gland (confirm with Tom), the hardware moves but the reinstall labor doesn't. The battery is the safest spend.
2. **Roof solar is the base; portable is back on the table as a supplement.** Roof solar needs no storage and just works, so it's the base. But flat roof panels underperform (can't tilt, worst in low winter sun). Since I want to run the fridge fully, a tiltable/portable panel can out-produce the roof (aim at sun, park van in shade, better winter angle) and get around my limited roof space. Hassle is the tradeoff, and I only need it for the rare multi-day stationary stay (I usually move every ~2 nights, so the alternator handles most recharging). **Plan: have Tom wire in an external MC4 solar input now so the van can accept a fold-out panel later. Buy the panel only if/when needed.**
3. **Prefer DC, but don't obsess.** Avoiding the inverter saves ~15%. Battery capacity, solar, and enough ports matter more. Hardwired 12V-to-USB-C for the laptops; don't sweat inverter loss on phones.

Keep the 1000W inverter off unless something truly needs AC.

---

## Loads

**Already on the battery**

- Webasto diesel heater (low electrical draw, mostly at startup)
- Maxxair fan

**Being added / moved to DC**

- Dometic CFX5 95DZ cooler (94L dual-zone). Runs all the time. Was on the inverter (wrong), being wired straight to DC. Rough draw: ~20-35W average with the compressor cycling, more in AZ heat, so very roughly 400-700Wh/day when hot. **Confirm exact draw and model with Tom.**
- Starlink Mini. Was on the inverter. Pulls ~25-40W continuously, so ~600-950Wh/day if run all day. This is a big load, needs its own DC cord.

**Device charging**

- Up to 4 phones (~20W each), 1 iPad (~30W), MacBook Pro (~96W) and MacBook Air (~30-67W). Up to ~300W peak if all at once, rare and short. Daily energy is what matters (~230-350Wh/day of device charging).

---

## Equipment status

- **Marine cell battery.** ~2 years old, has sat uncharged for months at a time (likely sulfated / damaged). Drains in ~20-30 hours with no solar. Lead-acid, so only ~half its capacity is usable. **Planned replacement: LiFePO4 (lithium).**
- **Solar.** Not installed yet. Considering two 200W panels or flexible panels. Roof is tight (rooftop AC that only runs when driving, plus the Maxxair fan). **Confirm what actually fits and realistic yield with Tom.**
- **Goal Zero Yeti 400.** Failing. Battery weak, and now only the USB ports work (AC outlet dead), so it won't charge the MacBook Air anymore. Retire it or keep as an emergency USB charger only.
- **Ampeak 1000W inverter.** The one I didn't want. Makes AC from the battery, only useful for wall-plug gear. Keeping it as an occasional AC option. It has its own on/off button, so I'll just power it off when not in use (idle drain is only when it's on, ~150-300Wh/day). No added switch needed. Tradeoff: it sits where a battery box could go, so keeping it may cost battery capacity I want for the fridge. Decision rule: if I have to choose, battery capacity wins. Let Tom advise whether both fit.

---

## Decisions I've made

1. **Replace the marine battery with LiFePO4.** I likely need a new battery anyway, and lithium gives ~2x usable capacity, lasts longer, and transfers to my next van. Size modestly to fit the budget.
2. **Add a DC-to-DC alternator charger** so driving every few days meaningfully recharges the battery.
3. **Wire the Dometic and Starlink straight to DC**, off the inverter.
4. **Laptops charge from hardwired 12V-to-USB-C PD outlets** (100W), not the inverter. Need at least two 100W outlets plus a hub for phones/iPad.
5. **Keep solar modest** given the roof, sized to help cover daily loads and buffer with alternator charging.
6. **Retire the Yeti 400** as a daily tool. Backup only.
7. **Portable power bank/station is optional**, only for charging away from the van.

---

## Questions for Tom

**Dometic / loads**

- Exactly how much does my Dometic CFX draw (watts or amp-hours per day)? What model is it?
- With everything on DC (fridge + heater + fan + Starlink + device charging), what's my expected daily draw in watt-hours?

**Battery**

- What size LiFePO4 do you recommend for that daily load, keeping the budget tight?
- Given I move every few days, how much will a DC-to-DC alternator charger realistically put back per hour of driving?
- **Fit constraint:** the battery only fits under the seat, there's nowhere else. What are the current marine battery's dimensions, and can a LiFePO4 fit that same footprint? (Lithium is usually more compact per usable Wh, so it should fit and hold more.) How much usable capacity fits in that spot?
- Is lithium worth it on this van, or would you keep the marine battery and lean on solar + alternator? (I'm leaning lithium because it moves to my next van.)

**Laptop / device charging**

- I want **at least 4 USB ports** near my work spot, straight off the battery (not the inverter, not the Goal Zero): two 12V-to-USB-C rated a full 100W each for laptops, plus at least 2 more (USB-C/USB-A) for phones, iPad, Wahoo bike computer, lights, etc.

**Solar**

- How many panels actually fit around the AC unit and fan? Do flexible panels make sense here?
- What total wattage, and what will it realistically produce on a clear AZ day?
- Sized to cover the fridge plus other loads, or mainly to keep the fridge going and slow the overall drain?
- Snow load / Colorado winter: any concern with panels and roof penetrations long term? (You said sun degrades seals faster than cold, want that confirmed in writing.)

**Charging ports**

- Can you install at least **two hardwired 12V-to-USB-C PD outlets rated for a full 100W each** for the laptops? (Not the 18-30W car sockets.)
- Best way to add enough ports for up to 4 phones + iPad at once: more DC USB-C outlets, a DC-fed hub, or a multi-port charger?

**Inverter**

- Once the Dometic and Starlink are on DC, do I still need the 1000W inverter for anything?
- Can it go on a switch so it draws nothing when off?

---

## The math to check (fill in with Tom's numbers)

- LiFePO4 battery capacity: ______ Wh
- Daily solar input (clear AZ day): ______ Wh
- Alternator charge per hour of driving: ______ Wh
- Daily loads:
  - Dometic CFX5 95DZ: ~300-600Wh/day typical (CO, cooler, one zone); AZ heat with both zones would be ~1,478-2,468Wh but that's rare for me
  - Starlink Mini (all day): ~600-950Wh
  - Heater + fan: ______ Wh
  - Device charging: ~230-350Wh
- Net per day (solar + alternator in, minus loads out): ______ Wh → sustainable or slowly draining?

---

## Still to decide / buy

- [ ] Confirm LiFePO4 size and price with Tom; pay deposit once the math checks out.
- [ ] Confirm DC-to-DC alternator charger is in the plan.
- [ ] Confirm 2× 100W DC USB-C outlets + a plan for phones/iPad.
- [ ] Confirm what solar actually fits and its realistic yield.
- [ ] Decide on a portable USB-C unit for away-from-van (Anker C300X vs USB-C power bank), or skip for now.
- [ ] Retire or keep the Yeti 400 as backup.

---

## Fold-out panel · buy-later checklist (match these to Tom's specs)

When I eventually buy a portable/tiltable panel, it must match what Tom wired in:

- [ ] Connector: MC4 output (avoid proprietary Jackery/EcoFlow/Goal Zero plugs, or get an MC4 adapter)
- [ ] Open-circuit voltage (Voc) under the Victron MPPT's max PV voltage: ______ V (get from Tom)
- [ ] Wattage within the controller's max added capacity: ______ W (get from Tom)
- [ ] Know whether it plugs in alongside the roof panels or replaces them while in use: ______ (get from Tom)

---

*Living doc. Updated from the New Life Conversions email thread (Jun-Jul 2026).*
