#!/usr/bin/env python3
"""
build-v3.py, the v3 site generator.

GOAL     Make drift structurally impossible. Every v3 page is GENERATED from the
         content model in this one file, so the header, nav, footer and page
         skeleton are identical on every page by construction rather than by care.
         Change the nav here, re-run, all pages update.

AUDIENCE Michelle, and every future Claude session.

PROCESS      python3 tools/build-v3.py          write the site
             python3 tools/build-v3.py --check  verify pages match the model, write nothing

WHY IT EXISTS
     v2 failed twice over. Its stylesheet grew from a real vocabulary of 45 class
     names to 384, because pages were hand-built and each one added what it needed.
     And its chrome was copied page to page, which is how v1 ended up with 19
     header variants and 22 footer variants across 273 pages. A template that
     nobody regenerates from is just a page somebody copied once.

THE TWO HARD RULES
     1. assets/site.css is FROZEN at its 45 classes. This generator emits ONLY
        those classes. If a page needs something that does not exist, stop and
        decide with Michelle. Do not add a class.
     2. This file never touches a running tool. Tools carry their own branding
        and a footer of one back arrow plus a copyright. The portfolio showcases
        them; it does not reach into them.

PAGE TYPES, four and no more
     section   the section landing page: summary at the top, cards to its projects
     overview  one per project, the standard format
     prd       one per project
     tab       a secondary tab, only when the work genuinely will not fit on the
               overview (the student journey study is the case this exists for)
"""
import os, sys, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'v3')
CHECK = '--check' in sys.argv

# ============================================================ THE LOCKED CHROME
# Defined once. Written into every page. Never edited in a page.

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<link rel="stylesheet" href="/assets/site.css">
<link rel="icon" href="/favicon.ico" sizes="any">
</head>'''

HEADER = '''<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="site-head">
  <div class="site-bar">
    <a class="site-name" href="/v3/">Michelle Blomberg</a>
    <nav class="site-nav" aria-label="Primary">
      <a href="/v3/">Home</a>
      <a href="/v3/#work">Work</a>
      <a href="/v3/about.html">About</a>
    </nav>
  </div>
</header>

<main id="main">'''

FOOTER = '''</main>

<footer class="sitefoot">
<div class="foot-links"><a href="/v3/">Home</a><a href="/v3/#work">Work</a><a href="/v3/about.html">About</a><a href="#" class="mailme">Email</a><a href="#">Top &uarr;</a></div>
<div class="foot">&copy; 2026 Michelle Blomberg. All rights reserved.</div>
</footer>
</body>
</html>'''


# ============================================================ THE CONTENT MODEL
# Every word on the site lives here. Copy carried over from v2, which had the
# right argument and the wrong formatting.

SECTIONS = [
 {
  'slug': 'intake', 'name': 'AI Opportunity Intake',
  'eyebrow': 'Section &middot; AI Tools &amp; Strategy',
  'lead': 'A front door for AI requests, so a district decides what to build on evidence rather than on who asked loudest.',
  'summary': 'Departments arrive with a problem, not a use case. Without somewhere for those requests to land, they get answered one at a time by whoever is nearest, and a platform gets bought because two peer institutions already have one. <strong>This is the intake, scoring and disposition model that prevents that.</strong> A request is shaped into a use case, scored on value, feasibility, readiness, risk, privacy and accessibility, and then sorted four ways: it becomes a pilot, it needs more discovery, it is a training or process problem rather than an AI problem, or it is declined. The governance framework behind it moves an approved idea into a sandboxed pilot and then to production, with a sunset date attached so nothing sits in pilot forever.',
  'projects': [],
  'status':'The governance framework is written and in review with the district AI CIO. It adapts the NIST AI Risk Management Framework, EDUCAUSE AI governance guidance, WCET and ITIL practice into a path a faculty member can actually follow, and every option in it is screened against a hard line: no student data, no personally identifiable information.',
 },
 {
  'slug': 'journey', 'name': 'Student Journey Study',
  'eyebrow': 'Section &middot; UX Design &middot; AI Tools &amp; Strategy',
  'lead': 'Ten colleges, one student journey, and a severity-ranked account of where it breaks.',
  'summary': 'A service inventory across ten colleges found that the same service carries a different name at every one of them, which hides something useful: a barrier stalling students at one campus often already has a working process at another. <strong>Finding that match is cheaper than building anything.</strong> The study runs three research personas against a task taxonomy, scores every barrier on a Nielsen severity rating confirmed by a second rater, and produces a prioritised roadmap that separates what an agent should answer from what belongs with a person. It is scoped to locate where agentic workflows can take routine work off advising staff, and the findings feed solution evaluation across three paths: a vendor product, an existing enterprise capability, or a build.',
  'projects': [],
  'status':'Instruments built and a method pilot of twelve walkthroughs complete, with fieldwork under way. Counts are agent runs; no human participant has taken part in this study. Colleges are reported anonymously.',
 },
 {
  'slug': 'dial', 'name': 'Dial Your Course',
  'eyebrow': 'Section &middot; AI Tools &amp; Strategy &middot; Learning Design',
  'lead': 'A Canvas course goes in. What to fix comes back. Each of the four checks runs on its own, or hands off to the next.',
  'summary': 'Four checks that read a real Canvas course package and report what falls short of the quality standard, then write the approved fixes back into the package. <strong>Every check is rule-based and contains no AI.</strong> A quality standard is a published list, so checking against it is a lookup: the same course returns the same answer every time, and every finding traces back to the sentence in the standard that produced it. A faculty member being told their course falls short deserves that traceability.',
  'projects': [
    {'slug':'syllabus','name':'Syllabus Checker','status':'Built and in use',
     'blurb':'Checks a finished syllabus against the required elements and reports what is missing.',
     'goal':'A syllabus has to carry a set of required elements every term, and the check is done by eye against a list, or not at all.',
     'audience':'Any instructor writing a syllabus, and the program director who reviews it before term.',
     'process':'Rule-based, no AI. The required elements are a published list, so the check is a lookup against that list and the result is the same every run.',
     'outcome':'Built and running as a standalone tool.'},
    {'slug':'quality','name':'Quality Check','status':'In build',
     'blurb':'Runs a course against a published quality standard and returns findings sorted into fix, review, and satisfied.',
     'goal':'At my college the standard is OSCQR, alongside seat time, accessibility, and regular substantive interaction. In practice a faculty member checks it by hand at the end of a build, against a rubric written for reviewers rather than for the person doing the work.',
     'audience':'The instructor building the course, and the instructional designer or program director reviewing it. The two want different things from the same run, so the output is ordered for the instructor and complete enough for the reviewer.',
     'process':'Rule-based, no AI, and it carries the most rules of the four. Findings are traceable back to the clause in the standard that produced them.',
     'outcome':'One full audit of AVC 100 returned 28 findings across 34 pages, 27 graded items and 17 rubrics, sorted into two to fix, eleven to review and fifteen satisfied. The most useful finding was not a failure: fourteen of twenty-seven graded items carried no course outcome.'},
    {'slug':'style','name':'Style Guide','status':'Built and in use',
     'blurb':'Generates Canvas-safe course HTML from a chosen palette and type scale.',
     'goal':'Course pages drift visually across a program because every page is hand-built and Canvas strips what it does not recognise.',
     'audience':'Faculty building Canvas pages who are not designers and should not have to be.',
     'process':'A palette and a type scale are chosen, and the tool emits HTML that survives the Canvas editor.',
     'outcome':'Built and in use across course builds.'},
    {'slug':'seat-time','name':'Seat Time','status':'Built and running',
     'blurb':'Estimates the real time a module asks of a student, against the credit hours it claims.',
     'goal':'Credit hours imply a time commitment, and nobody measures whether a module actually matches it.',
     'audience':'The instructor building the module, and the reviewer checking the claim.',
     'process':'Rule-based estimation across the module contents, reported against the stated credit hours.',
     'outcome':'Built and running against a real course.'},
  ],
  'round_trip':'The checks are only half of it. Approved changes are written back into the course package and the cartridge is repackaged for reimport, so the loop closes rather than ending in a list somebody retypes by hand. The package is opened, read, rewritten and rebuilt entirely inside the browser tab. Nothing is uploaded.',
  'status':'Syllabus Checker is built and in use as a standalone tool. Style Guide is built and in use. Seat Time is built and running against a real course. Quality Check is in build, and it is the one carrying the most rules. The four are being folded into one interface.',
 },
 {
  'slug': 'build', 'name': 'Build Your Course',
  'eyebrow': 'Section &middot; AI Tools &amp; Strategy &middot; Learning Design',
  'lead': 'Dial Your Course tells you what is wrong. This builds the replacement.',
  'summary': 'Checking a course and building one are different problems with different trust requirements, and collapsing them into one tool would damage both. The checks are deterministic. Building an assessment, or judging whether an open licence permits what you are about to do, is not. <strong>So these two tools use AI, and the human stays in every loop.</strong> Nothing is applied automatically: every suggestion arrives as a proposed replacement with four choices, apply, edit first, dismiss with a reason, or defer.',
  'projects': [
    {'slug':'assessment','name':'Authentic Assessment','status':'In build',
     'blurb':'Takes an assignment a student could hand to a model and proposes a replacement that asks for process evidence instead.',
     'goal':'Once a model can produce the artifact, the artifact stops being evidence of learning. The assignment has to ask for something else: the record of making, the response to critique, the decision a student can defend.',
     'audience':'An instructor who now knows a module is weak and has to fix it, which is where most quality processes quietly end.',
     'process':'Uses AI, gated on human acceptance. Nothing leaves the tool until the before and after have been seen side by side. The dismissal reason is recorded, because it is the record of where the method was wrong.',
     'outcome':'Run by hand on a full course. In build, and the less finished of the two.'},
    {'slug':'oer','name':'OER Finder','status':'Specified, not built',
     'blurb':'Finds openly licensed material for a module and records the licence that permits the use.',
     'goal':'Open material is only usable if the licence actually permits what you intend, and that judgement is where most OER adoption stalls.',
     'audience':'An instructor building from open resources without a librarian on call.',
     'process':'Uses AI to find candidates, then records the licence and the permission it grants alongside each one. Human acceptance required.',
     'outcome':'Specified and not built. The method has been run by hand.'},
  ],
  'status':'Authentic Assessment is in build and the less finished of the two. OER Finder is specified and not built. Both have been run by hand on a full course, which is where the evidence comes from: a complete fifteen-week graduate data science course built from open educational resources in a field I do not teach, with four original simulations for its assessments and a recorded oral defence carrying the grade.',
 },
 {
  'slug': 'render', 'name': 'Render',
  'eyebrow': 'Section &middot; AI Tools &amp; Strategy &middot; UX Design',
  'lead': 'A career-services tool that walks a student from no portfolio to a shipped one, in seven phases.',
  'summary': 'Built for students who need career materials and have no idea where to start. Seven phases, a single HTML file, vanilla JavaScript, and the Sonnet API. <strong>Authentication is a first name and nothing else.</strong> No personally identifiable information is collected and state lives in the browser, because a tool students are asked to trust should not be collecting them.',
  'projects': [],
  'status':'Prototype. Usability tested in March 2026 and heading toward a pilot in Fall 2026. Not in production.',
 },
 {
  'slug': 'copamigo', 'name': 'CopaMigo',
  'eyebrow': 'Section &middot; AI Tools &amp; Strategy &middot; UX Design',
  'lead': 'Student-facing routing for campus services, so a student asking a question in their own words reaches the right office.',
  'summary': 'Fourteen modules, multilingual, built on more than a hundred verified college URLs. The problem it addresses is that campus service information is organised the way the institution is organised, not the way a student asks. <strong>It collects no student data and no personally identifiable information</strong>, which is a hard constraint rather than a feature: the district declined a vendor AI add-on specifically because it would have collected student data.',
  'projects': [],
  'status':'Early prototype in testing. Not in production.',
 },
 {
  'slug': 'adoption', 'name': 'Adoption and Enablement',
  'eyebrow': 'Section &middot; Teaching/Program Design &middot; AI Tools &amp; Strategy',
  'lead': 'Getting people to actually use the thing, which is the part most technology work underestimates.',
  'summary': 'A tool nobody adopts is a tool nobody built. <strong>Twenty years of this work sits behind every other section here.</strong> More than 45 faculty were moved to fully online teaching in a matter of weeks and then coached one at a time until they could run their own courses without help. A campus AI community of practice was founded to surface the use already happening quietly rather than to announce a policy at people. Before that: a fully online faculty development course on designing and teaching online, authored and taught; an eight-year professional development series on course design, assessment and retention; and lead reviewer work under two course quality standards, which is coaching disguised as review.',
  'projects': [
    {'slug':'agents','name':'Autonomous Agents','status':'Built and running',
     'blurb':'Scheduled agents that verify their own sources and publish without a person in the loop.',
     'goal':'Routine information work that has to happen on a schedule, accurately, whether or not anyone remembers to do it.',
     'audience':'The people who receive the output. One posts verified entry-level openings to a student community every weekday; others maintain dashboards for named individuals.',
     'process':'Each agent searches, opens every source to confirm it is live, drops anything closed or moved, publishes by webhook or to a page, and reports what changed. Validated with golden-set regression checks, template versioning, multiple-run consistency, human review before anything ships, and drift monitoring.',
     'outcome':'Built and running on a schedule. Several have run for months.'},
  ],
  'status':'Ongoing. The community of practice launched this term through the campus teaching and learning centre, and its first line of collaborative work is authentic assessment in the age of generative AI, starting from the premise that the answer is assessment design rather than detection software.',
 },
 {
  'slug': 'campground', 'name': 'Campground Finder', 'home': False,
  'eyebrow': 'Section &middot; Personal Projects &middot; UX Design',
  'lead': 'Watches named campgrounds for a cancellation and reports the moment a site opens.',
  'summary': 'The good campgrounds are booked eleven months out and the only way in is somebody else&rsquo;s change of plans. <strong>This is here as evidence of the method rather than as a hobby project:</strong> an idea taken through to a working build, which is the outcome Render is meant to produce in a student. Two halves, a search form and a scheduled watcher that writes what it finds to a calendar.',
  'projects': [],
  'status':'Built and used. It ran every day for a month across a Yosemite trip and is currently switched off between trips. The watcher ran daily against Peak One Campground at Dillon Reservoir through June 2026, and a second instance watched Tahoe-shore sites through May. Both are disabled rather than deleted, because the pattern is the useful part.',
 },
 {
  'slug': 'traillog', 'name': 'Trail Log', 'home': False,
  'eyebrow': 'Section &middot; Personal Projects &middot; UX Design',
  'lead': 'A service record that follows a mountain bike for its whole life, so the maintenance history survives the sale.',
  'summary': 'People buy mountain bikes costing five to fifteen thousand dollars and then do not maintain them on schedule, because the schedule is genuinely complicated. Suspension is due by ride hours, drivetrains and tires by miles, brake bleeds and sealant by the calendar. Three clocks on one bike. <strong>Also here as evidence of the method:</strong> a specification, a competitive scan, and a working build.',
  'projects': [],
  'status':'Built and running on sample data, with a written specification and a competitive scan behind it. Strava is simulated. Nothing persists between reloads, deliberately, so it runs the same as a local file or a hosted page.',
 },
]


# ============================================================ THE FOUR TEMPLATES

def page(title, body):
    return HEAD.format(title=title) + '\n' + HEADER + '\n' + body + '\n' + FOOTER + '\n'


def tabs(sec, proj, current):
    """Overview and PRD are real links to real files, never a script that hides panels."""
    base = f"/v3/{sec['slug']}/" + (f"{proj['slug']}/" if proj else '')
    items = [('Overview', base + 'overview.html'), ('PRD', base + 'prd.html')]
    out = f'  <nav class="tabs" aria-label="{sec["name"]} sections">'
    for label, href in items:
        cur = ' aria-current="page"' if label.lower() == current else ''
        out += f'<a class="tab" href="{href}"{cur}>{label}</a>'
    return out + '</nav>'


def section_page(sec):
    """SECTION PAGE. Summary at the top. A video slot for the walkthrough, later."""
    b = [f'  <h1>{sec["name"]}</h1>',
         f'  <p class="eyebrow">{sec["eyebrow"]}</p>',
         f'  <p class="lead-sub">{sec["lead"]}</p>',
         '  <div class="prose">',
         f'    <p>{sec["summary"]}</p>',
         '  </div>']
    if sec['projects']:
        b.append('  <div class="cards">')
        for p in sec['projects']:
            href = f"/v3/{sec['slug']}/{p['slug']}/overview.html"
            b.append(f'    <a class="card" href="{href}"><span class="ct">{p["name"]}</span>'
                     f'<span class="when">{p["status"]}</span><span class="what">{p["blurb"]}</span></a>')
        b.append('  </div>')
    else:
        b.append('  <div class="cards">')
        b.append(f'    <a class="card" href="/v3/{sec["slug"]}/overview.html">'
                 f'<span class="ct">Overview</span><span class="what">What it is, who it serves, and how it was built.</span></a>')
        b.append(f'    <a class="card" href="/v3/{sec["slug"]}/prd.html">'
                 f'<span class="ct">PRD</span><span class="what">The written requirements behind it.</span></a>')
        b.append('  </div>')
    b += ['  <div class="prose">', '    <h2>Status</h2>', f'    <p>{sec["status"]}</p>', '  </div>']
    return page(f'{sec["name"]}, Michelle Blomberg', '\n'.join(b))


def overview_page(sec, proj=None):
    """TOOL OVERVIEW. The standard format. No extraneous elements."""
    name = proj['name'] if proj else sec['name']
    lead = proj['blurb'] if proj else sec['lead']
    goal = proj['goal'] if proj else sec['summary']
    aud = proj['audience'] if proj else 'Documented on the section page.'
    proc = proj['process'] if proj else 'Documented on the section page.'
    stat = proj['outcome'] if proj else sec['status']
    b = [f'  <h1>{name}</h1>',
         f'  <p class="eyebrow">Overview &middot; {sec["eyebrow"].split("&middot;",1)[1].strip()}</p>',
         tabs(sec, proj, 'overview'),
         f'  <p class="lead-sub">{lead}</p>',
         '  <div class="prose">',
         '    <h2>Goal</h2>', f'    <p>{goal}</p>',
         '    <h2>Audience</h2>', f'    <p>{aud}</p>',
         '    <h2>Process</h2>', f'    <p>{proc}</p>',
         '    <h2>Status</h2>', f'    <p>{stat}</p>',
         '  </div>']
    return page(f'{name}, Michelle Blomberg', '\n'.join(b))


def prd_page(sec, proj=None):
    """PRD. Fixed core sections, in this order, on every PRD."""
    name = proj['name'] if proj else sec['name']
    lead = proj['blurb'] if proj else sec['lead']
    b = [f'  <h1>{name}</h1>',
         f'  <p class="eyebrow">PRD &middot; {sec["eyebrow"].split("&middot;",1)[1].strip()}</p>',
         tabs(sec, proj, 'prd'),
         f'  <p class="lead-sub">{lead}</p>',
         '  <div class="prose">',
         '    <h2>1. Summary</h2>', f'    <p>{lead}</p>',
         '    <h2>2. Goal</h2>', f'    <p>{proj["goal"] if proj else sec["summary"]}</p>',
         '    <h2>3. Users and context</h2>', f'    <p>{proj["audience"] if proj else "Documented on the section page."}</p>',
         '    <h2>4. How it works</h2>', f'    <p>{proj["process"] if proj else "Documented on the section page."}</p>',
         '    <h2>5. Data, privacy, and governance</h2>',
         '    <p>No student data and no personally identifiable information is collected. This is a hard constraint across every tool here, not a feature of one of them.</p>',
         '    <h2>Status</h2>', f'    <p>{proj["outcome"] if proj else sec["status"]}</p>',
         '  </div>']
    return page(f'{name} PRD, Michelle Blomberg', '\n'.join(b))


def home_page():
    b = ['  <h1>Michelle Blomberg</h1>',
         '  <p class="eyebrow">AI adoption, enablement, and governance in higher education</p>',
         '  <p class="lead-sub">I find where AI is worth using inside an institution, decide what is worth building, and build the ones that are.</p>',
         '  <div class="prose">',
         '    <p>Most of the work here is deciding what not to build. A quality standard is a published list, so checking against it is a lookup and needs no model. A barrier at one college often already has a working process at another, and finding that match is cheaper than commissioning the tenth version of it. The tools below are the ones that survived that filter.</p>',
         '    <h2 id="work">Work</h2>', '  </div>',
         '  <div class="cards">']
    for s in SECTIONS:
        if s.get('home') is False:
            continue
        b.append(f'    <a class="card" href="/v3/{s["slug"]}/"><span class="ct">{s["name"]}</span>'
                 f'<span class="what">{s["lead"]}</span></a>')
    b.append('  </div>')
    return page('Michelle Blomberg', '\n'.join(b))


def about_page():
    """ABOUT. v1 layout: a small circular portrait floated beside the prose.
    Written to lead with technology adoption and governance, not with teaching."""
    b = ['  <h1>About</h1>',
         '  <img class="about-face" src="/cultivate/mblomberg.jpg" alt="Michelle Blomberg">',
         '  <div class="prose">',
         '    <p class="lead-sub">I work on how large institutions actually adopt new technology: what is worth doing, who it affects, what it costs to support, and whether anyone uses it once it ships.</p>',
         '    <p>I co-chair the Student Support and Success domain of the AI Resource Center at the Maricopa Community Colleges, one of the largest community college districts in the country at ten colleges and more than 140,000 students, and I sit on its steering committee. My part is the intake side: departments bring a problem, I shape it into a use case, score it on value, readiness, risk and privacy, and sort it into a pilot, more discovery, a training problem, or a decline. I wrote the framework the Center uses to move an approved idea into a sandboxed pilot and then to production, adapted from the NIST AI Risk Management Framework and EDUCAUSE guidance, with a sunset date attached so nothing sits in pilot forever.</p>',
         '    <p>Before that I directed a campus instructional technology centre for seven years, with developers, service agreements and platform selections running through it. I defined requirements, wrote service agreements, ran a learning platform evaluation and request for proposal against vendor alternatives, managed cross-functional teams to delivery, and stood up the campus single point of contact support desk. Earlier still I was a product manager for web-delivered education software, writing the requirements engineers built from and running the usability studies behind them.</p>',
         '    <p>What I know that most people working on institutional AI do not is what happens at the far end, in the departments that have to absorb the change. I have moved more than 45 faculty onto a new platform in a matter of weeks and then coached them one at a time until they could run without me. Adoption is the part that decides whether any of this was worth doing, and it is the part that gets budgeted last.</p>',
         '    <p>I build as well as specify. A student career tool on the Claude API now in pilot, a multilingual service routing tool in testing, a course quality suite whose core checks are deliberately rule-based with no model in them, and a set of scheduled agents that verify their own sources and publish unattended. The rule-based decision is the one I would defend hardest: a published standard is a lookup, so the same input should return the same answer every time, and a person told their work falls short deserves to see the clause that produced the finding.</p>',
         '    <p>The constraint under all of it is that these tools collect no student data and no personally identifiable information. That is not a feature, it is the reason the work is allowed to exist: the district declined a vendor AI add-on specifically because it would have collected student data, so building something data-sovereign beats buying something that harvests.</p>',
         '    <p>I hold a master&rsquo;s in educational technology, with graduate research in connectivism and personal learning environments, and a bachelor of fine arts in visual communications, which is why the documents and interfaces I put in front of stakeholders tend to land. I am a League for Innovation AI Fellow. I teach in Digital Media at Glendale Community College in Arizona and was Program Director there for over a decade, and I still teach, because staying close to the people a system is supposed to serve is how I know when it is not working.</p>',
         '    <p>A few things here are personal builds rather than institutional work: a campground cancellation watcher, a service log for a mountain bike, a road trip planner. They are on the site because they are the same method at small scale, taken from an idea to a specification to a working thing, which is the outcome I am trying to produce in students.</p>',
         '  </div>']
    return page('About, Michelle Blomberg', '\n'.join(b))


# ============================================================ EMIT
def emit(path, html, written, mismatched):
    full = os.path.join(OUT, path)
    if CHECK:
        if not os.path.exists(full) or open(full, encoding='utf-8').read() != html:
            mismatched.append(path)
        return
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(html)
    written.append(path)


def main():
    written, mismatched = [], []
    emit('index.html', home_page(), written, mismatched)
    emit('about.html', about_page(), written, mismatched)
    for s in SECTIONS:
        emit(f'{s["slug"]}/index.html', section_page(s), written, mismatched)
        if s['projects']:
            for p in s['projects']:
                emit(f'{s["slug"]}/{p["slug"]}/overview.html', overview_page(s, p), written, mismatched)
                emit(f'{s["slug"]}/{p["slug"]}/prd.html', prd_page(s, p), written, mismatched)
        else:
            emit(f'{s["slug"]}/overview.html', overview_page(s), written, mismatched)
            emit(f'{s["slug"]}/prd.html', prd_page(s), written, mismatched)

    if CHECK:
        if mismatched:
            print(f'\n  CRITICAL ({len(mismatched)})  v3 pages edited by hand, not regenerated')
            for m in mismatched:
                print('     v3/' + m)
            print('\n  Edit tools/build-v3.py and re-run it. Never hand-edit a generated page.\n')
            return 1
        print('\n  ok   v3 matches the generator\n')
        return 0

    print(f'\n  built {len(written)} pages into v3/')
    for w in written:
        print('     v3/' + w)
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
