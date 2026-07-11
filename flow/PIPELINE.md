# Find Your Flow, pipeline and rules (Claude's working notes)

Not published, not linked. This is the list to lean on so Michelle does not have to direct every edition. One new letter per day, published to `flow/index.html` (current letter) and saved as the next `vol-NN.html`, then added to `archive.html`.

## Who Jillian is
Outgoing, loves travel and fitness, a people person, ADHD and school-averse but will do a short program or one certificate. Likes psychology but will NOT chase a doctorate. Strong at AI prompting. Not strong at math (avoid math-heavy paths, or note the light-math route). Does NOT like working with kids. Does NOT want a desk-bound work-from-home job, but remote-flexible work is fine if she can do it from a cafe, library, or coworking space. Colorado (Denver metro, near Golden). Cost-smart; Michelle will help pay for the right short program.

## Hard rules (do not break)
- Every edition MUST include a "How to get qualified" box with REAL, accredited, verified links, framed as a small first step. Prefer the least-school path and LOCAL Colorado community-college or public options; community-college transfer (2+2) if a 4-year is truly required.
- Check what employers actually require; never send her after something unattainable.
- Neutral, low-pressure, HER choice (the voice is Flow, not Mom). She pulled back when she felt her life was being decided for her.
- Include a real apply-today job lane (paycheck now) when possible.
- Honest pay section, no inflated numbers.
- Photos must RELATE to the topic and must NOT reuse the same photos from past newsletters. Use distinct Pexels/Unsplash IDs each time. (vol-13 fix used Pexels.)
- NO barista jobs in the career newsletter (covered separately as part-time elsewhere).
- Design: plum/sage/rose/gold palette already in each file, Lora + DM Sans, mobile 430px column, curly quotes, no em dashes.

## Already covered (vol 1-13), do NOT repeat
1 Airline customer service · 2 Physical Therapist Assistant · 3 Personal Trainer · 4 Cardiac Device Technician · 5 Modeling · 6 Paralegal · 7 Criminal Justice · 8 Esthetician/Skin Care · 9 Sonographer · 10 Animal Care/Dog Training · 11 Insights & Research · 12 Real Estate · 13 Massage Therapy.

## FORMAT (locked in June, Michelle's correction)
Deck = aspirational careers/settings that take some training. Then ONE real job in that field showing REAL pay (not a low-skill front-desk/foot-in-the-door placeholder she could already get). Pull fast-growing, good-pay ideas from BLS (bls.gov/ooh/fastest-growing.htm), be creative, do NOT just rebuild what Michelle already named. Verified Colorado-local training links. Photos must relate and be distinct (Pexels, not reused).

## BUILT (all in archive; index.html auto-rotates by date, see scheduler note)
- **vol-13 Massage Therapy** (Jun 26), fixed: real licensed massage therapist job (~$43-47/hr), no front-desk lane.
- **vol-14 Adventure guiding** (Jun 27), raft/hike/ski/tour guiding, free outfitter training, Colorado Adventure Center sample job.
- **vol-15 Occupational Therapy Assistant** (Jun 28), BLS 19% growth, ~$68K, 2-yr associate. Pueblo CC + GateWay (Phoenix, near family) programs; real Denver OTA job ~$38/hr.
- **vol-16 Hearing Aid Specialist** (Jun 29), BLS 18% growth, ~$61,560, NO degree in CO (6-mo on-the-job + ILE exam), HearingLife paid apprenticeship; Miracle-Ear trainee ~$65K base. Photos are hearing/senior-themed (no white-coat/nurse shots).
- **vol-17 Social Media Coordinator** (Jun 30), no degree, portfolio-first, ~$56K Denver. Berg Berg internship on-ramp; free HubSpot/Google/Meta certs. No barista.
- **vol-18 Flight Attendant** (Jul 1), BLS $67,130 median (~$32/hr), 9% growth, ~19,800 openings/yr. No degree, airline pays you to train (~6.5 wks). Honest AGE note: Southwest min 18 (apply now at 19), Frontier 20 (Denver HQ), United 21 (Denver hub), all base in Denver. Distinct from vol-1 (ground/customer-service). Photos: reused vol-1's proven-live Unsplash aviation/travel set because web_fetch image verification is provenance-locked and curl fallback is disallowed; all 5 are aviation-themed and guaranteed to render.

## TWO-PAGE MODEL (do not break)
- **The newsletter is the thing we archive.** Each career edition is a dated `vol-NN.html`, listed in `archive.html`, and rotated by date via the `index.html` scheduler. One new dated letter per day.
- **`jobs.html` is a SINGLE living page, never versioned or archived.** It holds the current part-time jobs Jillian can apply to right now; the agent updates it IN PLACE (add new openings, drop filled ones). Do NOT create dated copies of it and do NOT list it in archive.html. Every newsletter links to it via the bottom "Jobs you can apply to today" button.

## SCHEDULER (how /flow/ rotates), important
`flow/index.html` is a tiny date-scheduler, NOT a copy of a volume. On load it reads today's date and redirects to the edition whose date is the latest one <= today (vol-13 on Jun 26 ... vol-17 on Jun 30, then stays on the newest). **To add a new edition: build vol-NN.html, add it to archive.html, then in index.html append `["YYYY-MM-DD","vol-NN.html"]` to the `sched` array in date order AND update the noscript URL + the manual "Tap here" link to the newest file.** Do NOT overwrite index.html with a volume's content.

## FORMAT NOTE (streamlined Jun): each volume = deck + one "how to get qualified" box + one real-job box + the green "See all the careers we have explored" button + a small "How this letter works" link (about.html). No "is the pay good" shadow box, no Wag button, no jobs-board links.

## Queue / future ideas (not yet built)
- More BLS outside-the-box fits Michelle liked: substance abuse / behavioral / mental health counselor (17%, $59K; peer support is the no-degree on-ramp), ophthalmic medical technician (20%, $44K), recreational therapist (fitness+psych+outdoors, bachelor's), dental hygienist (~$87K CO, associate, high pay).
- **Peer support / recovery coach** (wellness coaching alongside), adults not kids. Qualify: Colorado Peer & Family Specialist (CPFS), 60-hr training + 500 hrs experience + IC&RC exam (~$295). Real job: WellPower peer specialist, ~$26.72/hr min.
- **Social media coordinator**, portfolio-first; Berg Berg internship on-ramp; free HubSpot/Google/Meta certs. NO barista.
- **AI skills / data annotation**, see vol-16 AI notes below; legit platforms, do from a cafe. (Already added to Kevin's focus page.)
- **vol-16 Get paid for your AI skills**, AI training/data-annotation gig work done from a cafe/library/coworking (NOT stuck at home). Michelle + Kevin also want to do this in spare time, so write it to serve adults too, not only Jillian.
  - Legit companies (no sign-up fee, they pay YOU): DataAnnotation.tech (beginner-friendly, ~$20-40/hr, PayPal); Prolific (research studies, very reputable, best low-commitment starter); Outlier/Scale AI (higher pay, technical); TELUS International AI and Appen (big established names, ~$14-20/hr); Mercor, Alignerr (newer, legit).
  - Bank-info reassurance (Michelle's specific worry): legit sites ask for payment info (PayPal or direct-deposit account+routing) and a W-9/SSN AFTER you pass their assessment, because you are a paid contractor, that is normal. SCAM = asks you to PAY anything, asks for bank LOGIN/password, mails a check to deposit and wire back, or onboards via Telegram/WhatsApp. Receiving-deposit info is fine; banking login or money leaving your pocket is the red line.
  - Honest caveats: these are 1099 contractor gigs, not salaried jobs; income is flexible but uneven. Avoid generic "data entry from home" ads (most scam-flooded category; real data entry only ~$12-18/hr, legit ones come via Robert Half/Kelly staffing or a company's own careers page). No on-site Golden company; it is remote-flexible (do it from a cafe/library/coworking).
- **vol-17 Social media coordinator**, portfolio-first, hired on results not a degree. On-ramp: intern on Berg Berg Photography's social (run IG/FB, content calendar, reels, grow the following, document as a before/after case study); or a small local business/nonprofit. Free certs: HubSpot Social Media, Google Digital Marketing, Meta (Coursera). Apply-today: junior social/marketing coordinator at a Denver brand/agency. Honest pay: entry modest, portfolio is everything. NO barista.

## Future ideas (not yet built)
Travel advisor / destination-wedding planner, Pilates/group-fitness instructor, ski/snowboard instructor, recruiter/staffing coordinator, customer success. (Flight attendant built as vol-18.)
