# Dial Your Course, the plan (chronological)

One file, kept in the tool's folder so nothing scatters. Read it top to bottom and act in order. Two goals, in priority order: **(1) get a job. (2) If possible, make money from the tool; best case, sell it.** Not legal advice; the legal steps are pointers to confirm with an attorney.

## The one truth to hold the whole way through
Nobody writes a check for an idea or a solo prototype. Big companies build features themselves, or they buy traction, customers, or teams. So this tool's realistic payoff is **proof that gets you hired**, not a product that makes you rich. Protect it so a sale stays possible, but point your energy at the job. Everything below is sequenced around that.

## How big companies absorb a tool like this (the four mechanics)
Only one of these is "buy," and it is the least likely for a solo prototype.
1. **They build it themselves.** If it is just a feature, they clone it. A prototype cannot stop that. This is the real risk, and the reason to move fast and get inside rather than compete from outside.
2. **They partner** via their marketplace (Instructure Partner Network / EduAppCenter): you make it an LTI integration, institutions license it, the company lists it and takes a cut. The common third-party path.
3. **They acquire a company** that has paying customers and revenue, not a solo prototype.
4. **They acqui-hire** a small team for the talent.

You do not have a company, customers, or a team yet, so a straight purchase is the least likely outcome. What you have is the idea, the build, and (after the pilot) proof it works and that faculty want it. That is why **"get hired to build it inside a company" is the realistic win**, and why the plan below front-loads the pilot and the job search, not a sales pitch.

---

## PHASE 0, this week, before anything else (verify and protect)
Do these first; they can change everything downstream.

1. **Confirm you own the tool (you very likely do).** Strong facts in your favor, per Michelle: built **off-contract** (she is a 9-month employee, so summer is her own time), on **her own computer**, on **her own Claude account**, with **no district resources, systems, or data** involved. That is close to a textbook case for personal ownership, not employer ownership. She started it last week, tests it only on her **archived course sandbox** (no live Maricopa course, no student data), and pays for Claude herself. The scary version (built on district time, systems, or real course data) does not apply. The only thing left, for peace of mind, is to skim the Maricopa/RFA intellectual-property policy for any clause that reaches work "related to your field" even off-hours. Most faculty IP policies favor the faculty member for independently created work, so this should confirm ownership. If the language is clean, this worry is fully closed; if anything is ambiguous, a union rep or an attorney settles it fast. No longer a hard gate, just a confirmation.
2. **Check the public-employee rules.** Moonlighting/outside-work policies, and conflict of interest (selling to a vendor your district buys from can be a conflict). Know the lines before you pitch anyone.
3. **Rotate the exposed Anthropic key.** A live key is hardcoded in `copamigo/index.html` and is publicly readable. Revoke/rotate it at console.anthropic.com. Beyond the abuse risk, a live key in a public tool reads as careless if a company looks at your work.
4. **Keep the working tool private (mostly done).** The live-tool links are off the portfolio, the overview says it is IP with a demo on request, and the copyright notice is now in every page footer. Add the same "© 2026 Michelle Blomberg. All rights reserved." to the walkthrough video and any slides.

## PHASE 1, this fall, the must-do: build the proof (the pilot)
Everything, every path, depends on this. Without it you have an idea; with it you have evidence.

1. **Run a real pilot** with faculty at GCC, then a few other Maricopa colleges.
2. **Capture hard numbers:** courses run, hours saved versus reviewing by hand, the specific problems it caught, whether the corrected package reimported cleanly, and direct faculty quotes.
3. **Package the proof:** a one-page case study (Goal / Audience / Process + the results) and a three-minute video walkthrough. Code stays private; the video and results are what you show.

## PHASE 2, this fall in parallel, the job search (your #1 priority)
3 interviews out of 100 applications is a **channel problem, not a talent problem.** Cold applications convert at 2 to 5 percent, so the channel is the issue. Fix it in this order:

1. **Ask your network for warm intros instead of applying cold.** Referred candidates get interviews at several times the cold rate. You have 447 LinkedIn connections, a college president, Sonal, and an EDUCAUSE network. This is the biggest lever you are not pulling.
2. **Finish the LinkedIn profile** (drafted in `JobSearch/LinkedIn_Audit_and_ToDo.md`): the empty Projects section, the missing job descriptions, and the new About. A blank profile kills momentum the moment a hiring manager clicks through. Also flip on the Follow button (Settings and Privacy, Visibility, Followers, Make follow primary).
3. **Target roles you actually fit** (learning-experience design, UX, AI-building), not the 5-year-PM reqs. Poor-fit applications depress the rate and demoralize you.
4. **Diagnose your funnel.** Of the 3 interviews, how far did each go? Getting interviews but not offers is an interview-craft or role-fit problem, a different fix than getting more interviews.
5. **Register the copyright** once Phase 0 confirms you own it. Go to copyright.gov, use the eCO system, register the **video** (audiovisual work) and the **code** (computer program), about $45 to $65 each. Keep the certificates in the `course-dialer/` folder. Optional: trademark the name "Dial Your Course" via USPTO TEAS (~$250 to $350) if the brand matters. Skip patents; too slow, costly, and hard for a solo edu tool.

## PHASE 3, Sept 29 to Oct 2, EDUCAUSE (your leverage event)
Treat it as three things at once: a **job fair**, a **networking room**, and a **partner-pitch opportunity.** Meet Instructure and edtech product people in person, mention the tool and the pilot, and collect contacts. One conference can move all three goals.

## PHASE 4, late fall / winter, pick the vehicle (now that you have proof)
With pilot evidence in hand, choose the path, ranked for your situation (solo faculty, no capital, wants income and impact):

1. **Get hired to build it inside an edtech company.** Highest probability, income now, reaches millions, and the tool is your portfolio. "They steal it" becomes "they hired the inventor." This is also your job search, so the two are one plan.
2. **Grant or consortium-funded shared infrastructure** (a foundation, a state system, a Quality Matters/OLC partnership). Money without investors; scales to many faculty. Write a two-page concept plus budget.
3. **License it as an ecosystem partner product** (a few paying colleges, then acquirable). A real business, the most work, needs an LLC and hosting.
4. **Sale/acquisition.** Lowest probability, and only becomes real after 1 to 3 create traction. The lottery ticket, kept alive by protecting the IP, not the plan.

## The target list (it is a list, not one company)
Two buckets. **Companies** can buy, license, or hire you. **Nonprofits** almost never buy, but they open doors, lend credibility, and can partner or fund.

**Companies (buyers / employers):**
- **Instructure (Canvas)** — biggest reach, ideal employer. Slower, and more likely to just build a feature, so lead with hired/partnered.
- **Cidi Labs (DesignPLUS / commercial UDOIT)** — closest competitor, smaller, missing exactly your pedagogy + build layer. A small specialist is often a *more* realistic acquirer/acqui-hire than a giant. Likely your highest-value conversation after Instructure. **Caution: direct competitor, NDA before you show anything, never the code.**
- **Anthology (Blackboard/Ally), D2L, YuJa** — accessibility/LMS players who could want the pedagogy layer. Secondary.
- **AI course-builder startups** (Coursebox, LearnWorlds, etc.) — could want your audit/grounding side, but may just build it.

**Nonprofits / associations (connectors, partners, credibility, NOT buyers):**
- **EDUCAUSE** — convener and publisher, not a product company. Will not buy. Powerful for presenting, publishing (EDUCAUSE Review), community groups, and meeting the companies above.
- **OLC (Online Learning Consortium)** — owns the new 2025 Course Review Scorecard that is replacing OSCQR, which your tool operationalizes. Realistic as a **partner, endorser, or grant collaborator**; strong conference/community (OLC Accelerate).
- **Quality Matters** — same idea (your tool automates the countable part of their rubric). Partner/endorse, not buy.
- **SUNY/OSCQR, UCF (UDOIT's origin)** — universities, not buyers; possible academic collaborators. OSCQR is sunsetting, lower priority.
- **The League for Innovation** — your **AI Fellowship** = a built-in network of community colleges and corporate partners. Prime connector: present the capstone, work the Fellow network, ask League staff for intros.

**Who is the real target?** For a **sale or a job**: the companies, Instructure first, Cidi Labs a close (maybe more realistic) second. For **connections, credibility, partnership, or grant money that still reaches faculty**: the nonprofits, especially EDUCAUSE, OLC, and your League Fellowship. Use the nonprofits to reach the companies; do not wait on the nonprofits for a check.

## PHASE 5, when you approach a company, the exact moves
1. **Warmest door first:** Maricopa's Canvas admin can introduce you to the district's **Instructure Customer Success Manager**. Then **InstructureCon** (their annual conference). Then the **Instructure Partner Network** application. Then LinkedIn to their product managers/directors for course quality, accessibility, and teaching and learning, warm intro first, never cold.
2. **The pitch, almost word for word:** "I built a tool that solves the seat-time and course-quality review problem for faculty. I have N faculty using it, and here is what it caught and saved. I am exploring whether it fits as a partner integration or whether it is something I would be better off building inside Canvas. Could I have 20 minutes?" Let them pick the vehicle (partner, acquire, or hire).
3. **NDA before you show code or a live demo.** Use `course-dialer/NDA_TEMPLATE.md` (mutual NDA; it gives them no license and no ownership of what you show, and obligates no one to a deal). Fill the brackets, export a PDF, get it signed.
4. **Never sign anything without an attorney,** an IP assignment, a term sheet, or a job offer that claims your side projects. Find one advisor who has sold a tool to an LMS.

## PHASE 6, keep perspective (the honest odds)
- **Sell it for retire-money:** very low. Nobody pays retire-money for a solo prototype or a small tool with a few customers; that is a modest deal at best. Retire-level money needs a real company with revenue, which is years and a team you do not have time for.
- **Make any money from the tool (license/grant):** low-to-modest and slow. A side stream, not a windfall.
- **Tool gets you a job:** the high-probability, high-value payoff. The real money is the salary it helps you land.
- **The tool is narrow** (Canvas-only, seat-time, OSCQR, which OLC is now replacing). Great as a portfolio piece; limited as a product without broadening.
- **You do not have time for a startup** on top of the fall course crunch, the job search, and the Sonal chain. Pick the job path; let the tool serve it.
- **Sustainability:** the plan has to be doable while tired. A weekly all-nighter is not a plan.

**Bottom line:** point your energy at the job (profile, warm intros, builder identity, the pilot as proof, EDUCAUSE). Keep the tool protected so the sale stays possible, but understand its real return is opening doors, not writing you a check. You are closer than 3-out-of-100 makes you feel; you have been fighting through the weakest channel with an unfinished profile.

---

## Where this lives
This file: `course-dialer/IP_AND_SELLING_PLAN.md`. Companion docs in the same `course-dialer/` folder: `prd.html` (the product), `V2_RESEARCH_LANDSCAPE.md` (the market and features), `NEXT.md` (build handoff), and `NDA_TEMPLATE.md` (for company demos). Nothing about this plan is anywhere else.
