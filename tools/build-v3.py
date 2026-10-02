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
     tab       a secondary tab, only when the work will not fit on the
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
  'slug': 'journey', 'name': 'Student Journey Study',
  'eyebrow': 'Section &middot; UX Design &middot; AI Tools &amp; Strategy',
  'lead': 'Ten colleges, one student journey, and a ranked account of where students hit barriers reaching support.',
  'summary': 'A ten-college study of the district student journey, from finding a college through to work. Ten colleges each run advising, financial aid and basic needs in their own way, and the path from a felt need to the right person is full of dead ends. <strong>Fifty synthetic students, each an AI agent built from one fixed persona, walk each college&rsquo;s live site the way that student would and report where they get stuck.</strong> One orchestrator agent sequences the runs. Barriers are logged, severity-rated by more than one rater, and ranked by how many students each gap touches, so the domain can decide where an AI tool, a shared staff workflow, or a person is the right answer. I designed the study and lead it as co-chair of the Student Support and Success domain.',
  'goal': 'Students rarely fail because the help is missing. They fail because they cannot find it, or because the name the college uses is not the word a student would think to type. The goal is to locate exactly where the journey breaks, across ten colleges, and rank the breaks so the fixes happen in the order that matters.',
  'audience': 'The advisors and support staff who would use whatever gets built, who are colleagues rather than obstacles, and the district leadership deciding where to spend. The study is written so it reads as taking routine work off staff, because that is what it is for.',
  'process': 'Fifty demographic-grounded personas are built as specialist agents, with one orchestrator agent that sequences the journey and routes the runs. Each service is walked at each of the ten colleges until added personas surface no new barrier. The walk runs in three parts by access: public tasks that need no login, signed-in tasks on one sanctioned test account, and tasks that wait for the district&rsquo;s incoming Salesforce platform. What breaks is logged and rated by more than one rater, the highest-reach gaps are ranked, and the most promising fixes are piloted before anything scales. Humans decide what to fix. No one is replaced.',
  'tool': '/airc-sss/', 'tool_label': 'Read the study', 'thumb': '/airc-sss/cover.svg',
  'projects': [],
  'status':'In progress. All fifty-two agents are built and have run. The public tasks have run twice across all ten colleges, and the candidate barriers from those runs are registered and waiting on human rating. The signed-in phases have not started and wait on district approval and the data-governance review. Counts are agent runs; no human participant has taken part in this study.',
 },
 {
  'slug': 'dial', 'name': 'Dial Your Course', 'thumb': '/course-dialer/cover.jpg',
  'eyebrow': 'Section &middot; AI Tools &amp; Strategy &middot; Learning Design',
  'lead': 'A Canvas course goes in. Nineteen checks run. What to fix comes back.',
  'summary': 'Dial Your Course reads a real Canvas course package, runs nineteen checks against it, from seat hours to outcome alignment to accessibility, and writes the approved fixes back into the package. <strong>Every check is rule-based and contains no AI.</strong> A quality standard is a published list, so checking against it is a lookup: the same course returns the same answer every time, and every finding traces back to the sentence in the standard that produced it. A faculty member being told their course falls short deserves that traceability. It began as the checks I performed by hand as a peer and lead reviewer for Quality Matters and OSCQR.',
  'projects': [
    {'slug':'syllabus','name':'Syllabus Checker','status':'Built and in use','thumb':'/syllabus-checker/cover.jpg',
     'blurb':'Checks a finished syllabus against the required elements and reports what is missing.',
     'goal':'A syllabus has to carry a set of required elements every term, and the check is done by eye against a list, or not at all.',
     'audience':'Any instructor writing a syllabus, and the program director who reviews it before term.',
     'process':'Rule-based, no AI. The required elements are a published list, so the check is a lookup against that list and the result is the same every run.',
     'outcome':'Built and running as a standalone tool.'},
    {'slug':'quality','name':'Quality Check','status':'Pilot',
     'blurb':'Runs a course against a published quality standard and returns findings sorted into fix, review, and satisfied.',
     'goal':'At my college the standard is OSCQR, alongside seat time, accessibility, and regular substantive interaction. In practice a faculty member checks it by hand at the end of a build, against a rubric written for reviewers rather than for the person doing the work.',
     'audience':'The instructor building the course, and the instructional designer or program director reviewing it. The two want different things from the same run, so the output is ordered for the instructor and complete enough for the reviewer.',
     'process':'Rule-based, no AI, and it carries the most rules of the four. Findings are traceable back to the clause in the standard that produced them.',
     'outcome':'Built and working, in pilot in Digital Media Arts. Findings come back sorted into fix, review and satisfied, each one traced to the clause that produced it.'},
    {'slug':'style','name':'Style Guide','status':'Built and in use',
     'blurb':'Generates Canvas-safe course HTML from a chosen palette and type scale.',
     'goal':'Course pages drift visually across a program because every page is hand-built and Canvas strips what it does not recognize.',
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
  'status':'Pilot. Version 1 is built and working, and it is in pilot in Digital Media Arts. It runs in any browser and inside Canvas, with no server and no account. Version 2 is built and working as a pilot build. Syllabus Checker also runs as a standalone tool.',
 },
 {
  'slug': 'build', 'name': 'Build Your Course', 'thumb': '/authentic-assessment/authentic_cover.svg',
  'eyebrow': 'Section &middot; AI Tools &amp; Strategy &middot; Learning Design',
  'lead': 'Dial Your Course tells you what is wrong. This builds the replacement.',
  'summary': 'Checking a course and building one are different problems with different trust requirements, and collapsing them into one tool would damage both. The checks are deterministic. Building an assessment, or judging whether an open license permits what you are about to do, is not. <strong>So these two tools use AI, and the human stays in every loop.</strong> Nothing is applied automatically: every suggestion arrives as a proposed replacement with four choices, apply, edit first, dismiss with a reason, or defer.',
  'projects': [
    {'slug':'assessment','name':'Authentic Assessment','status':'Pilot build',
     'blurb':'Takes an assignment a student could hand to a model and proposes a replacement that asks for process evidence instead.',
     'goal':'Once a model can produce the artifact, the artifact stops being evidence of learning. The assignment has to ask for something else: the record of making, the response to critique, the decision a student can defend.',
     'audience':'An instructor who now knows a module is weak and has to fix it, which is where most quality processes quietly end.',
     'process':'Uses AI, gated on human acceptance. Nothing leaves the tool until the before and after have been seen side by side. The dismissal reason is recorded, because it is the record of where the method was wrong.',
     'outcome':'Built and working as a pilot build, and it has produced results.'},
    {'slug':'oer','name':'OER Finder','status':'Specified, not built',
     'blurb':'Finds openly licensed material for a module and records the license that permits the use.',
     'goal':'Open material is only usable if the license actually permits what you intend, and that judgment is where most OER adoption stalls.',
     'audience':'An instructor building from open resources without a librarian on call.',
     'process':'Uses AI to find candidates, then records the license and the permission it grants alongside each one. Human acceptance required.',
     'outcome':'Specified and not built. The method has been run by hand.'},
  ],
  'status':'Authentic Assessment is built and working as a pilot build and has produced results. OER Finder is specified and not built. Both methods were first run by hand on a full course: a complete fifteen-week graduate data science course built from open educational resources in a field I do not teach, with four original simulations for its assessments and a recorded oral defense carrying the grade.',
 },
 {
  'slug': 'render', 'name': 'Render',
  'eyebrow': 'Section &middot; AI Tools &amp; Strategy &middot; UX Design',
  'lead': 'A career-launch environment students build across the capstone and keep after graduation.',
  'summary': 'Career-readiness work usually disappears when Canvas access ends at graduation. Render is a personal learning environment the student owns: goals, job log, resume vault, skills, networking and interview prep in one place, every piece anchored to one real job the student picks on day one. <strong>Students run the agents in their own free AI accounts and leave with the whole package.</strong> It is built in partnership with campus Career Services, so it reinforces what a career advisor would say.',
  'goal': 'Design students graduate with a portfolio and no method for finding work. The goal is that a student leaves the semester with working career infrastructure they own, rather than a folder of assignments they will never open again.',
  'audience': 'Final-semester students in a capstone course, and the career services staff who would otherwise see them for the first time after graduation.',
  'process': 'Students set goals and pick one real reach job on day one, then build the environment across the AVC 248 capstone. At the end, Render runs a gap analysis between what the student actually built and what that job asks for, and exports the package: their agents and skills as prompt files, a job tracker, their tailored documents, and a personal learning plan. Sign-in is a first name only, kept in the student&rsquo;s own browser. Usability tested with students in March 2026 and revised from what that surfaced.',
  'tool': '/render/', 'tool_label': 'Open Render', 'thumb': '/render/render_cover.jpg',
  'projects': [],
  'status':'In pilot this fall in one section of the AVC 248 capstone. Not in production.',
 },
 {
  'slug': 'copamigo', 'name': 'CopaMigo',
  'eyebrow': 'Section &middot; AI Tools &amp; Strategy &middot; UX Design',
  'lead': 'Student-facing routing for campus services, so a student asking a question in their own words reaches the right office.',
  'summary': 'Every campus already offers more support than its students can find. The services exist; students just do not know which office handles their problem, or what it is called. <strong>A student describes the situation in plain language, in their own language, and CopaMigo routes them to the right service with a handoff card:</strong> the contact, the hours, and what to ask for. Its answers are written rather than retrieved, drawn from the questions students actually bring and shaped with the offices that handle them. Anonymous, no login.',
  'goal': 'Campus service information is organized the way the institution is organized, not the way a student asks. The goal is that a student describing a problem in their own words, in their own language, reaches the right human being with enough context to make the handoff work.',
  'audience': 'Students who do not know the name of the office they need, and the advising and support staff who currently absorb the routing work by hand.',
  'process': 'Fourteen service modules built on more than a hundred hand-verified college URLs, with a campus picker covering all ten district colleges. A student types or speaks the situation and gets an answer in the same language, plus a handoff card carrying contact details, opening hours and what to ask for. Routine questions are answered inline; everything else reaches a person faster. It is anonymous, with no login.',
  'tool': '/copamigo/', 'tool_label': 'Open CopaMigo', 'thumb': '/copamigo/copamigo_cover.jpg?v=2',
  'projects': [],
  'status':'A working prototype in a program-wide pilot in the Digital Media Arts program. Not in production.',
 },
 {
  'slug': 'adoption', 'name': 'Adoption and Enablement', 'thumb': '/studio/studio-cover.jpg',
  'eyebrow': 'Section &middot; Teaching/Program Design &middot; AI Tools &amp; Strategy',
  'lead': 'Getting people to actually use the thing, which is the part most technology work underestimates.',
  'summary': 'A tool nobody adopts is a tool nobody built. <strong>Twenty years of this work sits behind every other section here.</strong> A campus AI community of practice was convened for the faculty, staff and administrators already using AI, so good practice spreads by example rather than by a policy announced at people. Before that: a fully online faculty development course on designing and teaching online, authored and taught; an eight-year professional development series on course design, assessment and retention; and lead reviewer work under two course quality standards, which is coaching disguised as review.',
  'projects': [
    {'slug':'agents','name':'Autonomous Agents','status':'Built and running',
     'blurb':'Scheduled agents that check their own sources before they post.',
     'goal':'Routine information work that has to happen on a schedule, accurately, whether or not anyone remembers to do it.',
     'audience':'The people who receive the output. One posts verified entry-level openings to a student community every weekday; others maintain dashboards for named individuals.',
     'process':'Each agent searches, opens every source to confirm it is live, drops anything closed or moved, publishes by webhook or to a page, and reports what changed. Validated with golden-set regression checks, template versioning, multiple-run consistency, human review before anything ships, and drift monitoring.',
     'outcome':'Built and running on a schedule. Several have run for months.'},
  ],
  'status':'Ongoing. The community of practice launched this term through the campus teaching and learning center, and its first line of collaborative work is authentic assessment in the age of generative AI, starting from the premise that the answer is assessment design rather than detection software.',
 },
 {
  'slug': 'campground', 'name': 'Campground Finder', 'home': False,
  'eyebrow': 'Section &middot; Personal Projects &middot; UX Design',
  'lead': 'Watches named campgrounds for a cancellation and reports the moment a site opens.',
  'summary': 'The good campgrounds are booked eleven months out and the only way in is somebody else&rsquo;s change of plans. <strong>This is here as evidence of the method rather than as a hobby project:</strong> an idea taken through to a working build, which is the outcome Render is meant to produce in a student. Two halves, a search form and a scheduled watcher that writes what it finds to a calendar.',
  'goal': "The good campgrounds are booked eleven months out and the only way in is somebody else’s change of plans. The goal was to stop refreshing a reservation page by hand.",
  'audience': 'One household, honestly. It is on this site as evidence of the method rather than as a product: an idea taken through a specification to a working build, which is the outcome Render is meant to produce in a student.',
  'process': 'Two halves. A search form for finding candidate sites, and a scheduled watcher that checks named campgrounds daily and writes what it finds straight to a calendar, so the alert arrives where the trip would be planned anyway.',
  'tool': '/wayfinder/', 'tool_label': 'See the trip planner', 'thumb': '/wayfinder/wayfinder_cover.jpg',
  'projects': [],
  'status':'Built and used. It ran every day for a month across a Yosemite trip and is currently switched off between trips. The watcher ran daily against Peak One Campground at Dillon Reservoir through June 2026, and a second instance watched Tahoe-shore sites through May. Both are disabled rather than deleted, because the pattern is the useful part.',
 },
 {
  'slug': 'traillog', 'name': 'Trail Log', 'home': False,
  'eyebrow': 'Section &middot; Personal Projects &middot; UX Design',
  'lead': 'A service record that follows a mountain bike for its whole life, so the maintenance history survives the sale.',
  'summary': 'People buy mountain bikes costing five to fifteen thousand dollars and then do not maintain them on schedule, because the schedule is complicated. Suspension is due by ride hours, drivetrains and tires by miles, brake bleeds and sealant by the calendar. Three clocks on one bike. <strong>Also here as evidence of the method:</strong> a specification, a competitive scan, and a working build.',
  'goal': 'People buy mountain bikes costing five to fifteen thousand dollars and then do not maintain them on schedule, because the schedule is complicated: suspension is due by ride hours, drivetrains and tires by miles, brake bleeds and sealant by the calendar. Three clocks on one bike. The goal is a service record that survives the sale.',
  'audience': 'Riders maintaining their own bikes, and the second owner who inherits a machine with no history.',
  'process': 'A written specification and a competitive scan came first, then the build. Three separate service clocks tracked per component, reported against the manufacturer intervals. Strava data is simulated. Nothing persists between reloads, deliberately, so it runs identically as a local file or a hosted page.',
  'tool': '/traillog/', 'tool_label': 'Open Trail Log',
  'projects': [],
  'status':'Built and running on sample data, with a written specification and a competitive scan behind it. Strava is simulated. Nothing persists between reloads, deliberately, so it runs the same as a local file or a hosted page.',
 },
]


# ============================================================ THE FOUR TEMPLATES

def page(title, body, script=None):
    tail = FOOTER
    if script:
        tail = tail.replace('</body>', f'<script src="{script}"></script>\n</body>')
    return HEAD.format(title=title) + '\n' + HEADER + '\n' + body + '\n' + tail + '\n'


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
    if sec.get('video'):
        b.append(f'  <div class="video-slot"><iframe src="{sec["video"]}" title="{sec["name"]} walkthrough" allowfullscreen style="width:100%;height:100%;border:0;border-radius:10px"></iframe></div>')
    if sec.get('tool'):
        b.append('  <div class="links">')
        b.append(f'    <a class="primary" href="{sec["tool"]}">{sec["tool_label"]}</a>')
        b.append(f'    <a href="/v3/{sec["slug"]}/overview.html">Overview</a>')
        b.append(f'    <a href="/v3/{sec["slug"]}/prd.html">PRD</a>')
        b.append('  </div>')
    if sec['projects']:
        b.append('  <div class="feat">')
        for p in sec['projects']:
            href = f"/v3/{sec['slug']}/{p['slug']}/overview.html"
            thumb = p.get('thumb')
            inner = (f'<img src="{thumb}" alt="">' if thumb else 'Screenshot to come')
            b.append(f'    <a href="{href}"><span class="feat-thumb">{inner}</span>'
                     f'<span class="feat-body"><span class="feat-t">{p["name"]}</span>'
                     f'<span class="feat-d">{p["status"]}. {p["blurb"]}</span></span></a>')
        b.append('  </div>')
    elif not sec.get('tool'):
        b.append('  <div class="links">')
        b.append(f'    <a class="primary" href="/v3/{sec["slug"]}/overview.html">Overview</a>')
        b.append(f'    <a href="/v3/{sec["slug"]}/prd.html">PRD</a>')
        b.append('  </div>')
    b += ['  <div class="prose">', '    <h2>Status</h2>', f'    <p>{sec["status"]}</p>', '  </div>']
    return page(f'{sec["name"]}, Michelle Blomberg', '\n'.join(b))


def overview_page(sec, proj=None):
    """TOOL OVERVIEW. The standard format. No extraneous elements."""
    name = proj['name'] if proj else sec['name']
    lead = proj['blurb'] if proj else sec['lead']
    goal = proj['goal'] if proj else sec['goal']
    aud = proj['audience'] if proj else sec['audience']
    proc = proj['process'] if proj else sec['process']
    stat = proj['outcome'] if proj else sec['status']
    tool = (proj.get('tool') if proj else sec.get('tool'))
    tool_label = (proj.get('tool_label') if proj else sec.get('tool_label'))
    b = [f'  <h1>{name}</h1>',
         f'  <p class="eyebrow">Overview &middot; {sec["eyebrow"].split("&middot;",1)[1].strip()}</p>',
         tabs(sec, proj, 'overview'),
         f'  <p class="lead-sub">{lead}</p>']
    if tool:
        b.append(f'  <div class="links"><a class="primary" href="{tool}">{tool_label}</a></div>')
    b += ['  <div class="prose">',
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
         '    <h2>1. Summary</h2>', f'    <p>{sec["summary"]}</p>',
         '    <h2>2. Goal</h2>', f'    <p>{proj["goal"] if proj else sec["goal"]}</p>',
         '    <h2>3. Users and context</h2>', f'    <p>{proj["audience"] if proj else sec["audience"]}</p>',
         '    <h2>4. How it works</h2>', f'    <p>{proj["process"] if proj else sec["process"]}</p>',
         '    <h2>5. Data, privacy, and governance</h2>',
         '    <p>Each tool collects only what it needs to work and tells the user what that is. Privacy, security and accessibility are reviewed before a pilot starts, not after.</p>',
         '    <h2>Status</h2>', f'    <p>{proj["outcome"] if proj else sec["status"]}</p>',
         '  </div>']
    return page(f'{name} PRD, Michelle Blomberg', '\n'.join(b))


def home_page():
    b = ['  <h1 class="lead-intro">I design learning experiences <br class="brk">and AI strategy for the future <br class="brk">of higher education.</h1>',
         '  <p class="lead-sub">My work sits at the intersection of emerging technology, human-centered design, and helping organizations put new tools to real, practical use. I start with the people and the problem, never the technology: prototype, put it in front of real users, and don&rsquo;t scale until the evidence says it works.</p>',
         '',
         '  <div class="askbar">',
         '    <div class="askrow">',
         '      <img class="ask-face" src="/michelle-memoji.jpg" alt="Michelle Blomberg" onerror="this.style.display=\'none\'">',
         '      <form onsubmit="return abSubmit(event)">',
         '        <input id="abInput" placeholder="Ask me about my work" autocomplete="off" aria-label="Ask me anything about my work">',
         '        <button type="submit" class="go" aria-label="Send">&#10148;</button>',
         '      </form>',
         '    </div>',
         '    <p class="askhint">Try: <button type="button" class="askhint-link" onclick="abAsk(\'future\',\'What do you think about the future of learning in the age of AI?\')">What do you think about the future of learning in the age of AI?</button></p>',
         '    <div class="asklog" id="abLog"></div>',
         '  </div>',
         '',
         '  <div class="prose">',
         '    <p>Most of the work here is deciding what not to build. A quality standard is a published list, so checking against it is a lookup and needs no model. A barrier at one college often already has a working process at another, and finding that match is cheaper than commissioning the tenth version of it. The tools below are the ones that survived that filter.</p>',
         '    <h2 id="work">Work</h2>',
         '  </div>',
         '  <div class="feat">']
    for sec in SECTIONS:
        if sec.get('home') is False:
            continue
        thumb = sec.get('thumb')
        inner = (f'<img src="{thumb}" alt="">' if thumb else 'Screenshot to come')
        b.append(f'    <a href="/v3/{sec["slug"]}/">'
                 f'<span class="feat-thumb">{inner}</span>'
                 f'<span class="feat-body"><span class="feat-t">{sec["name"]}</span>'
                 f'<span class="feat-d">{sec["lead"]}</span></span></a>')
    b.append('  </div>')
    b.append('  <p class="feat-label">Also here</p>')
    b.append('  <div class="feat">')
    for sec in SECTIONS:
        if sec.get('home') is not False:
            continue
        thumb = sec.get('thumb')
        inner = (f'<img src="{thumb}" alt="">' if thumb else 'Screenshot to come')
        b.append(f'    <a href="/v3/{sec["slug"]}/">'
                 f'<span class="feat-thumb">{inner}</span>'
                 f'<span class="feat-body"><span class="feat-t">{sec["name"]}</span>'
                 f'<span class="feat-d">{sec["lead"]}</span></span></a>')
    b.append('  </div>')
    return page('Michelle Blomberg', '\n'.join(b), script='/v3/assets/askbar.js')


def about_page():
    """ABOUT. v1 layout: a small circular portrait floated beside the prose.
    Text copied from the live about.html on 2 Oct 2026. Keep the two in step."""
    b = ['  <h1>About</h1>',
         '  <img class="about-face" src="/cultivate/mblomberg.jpg" alt="Michelle Blomberg">',
         '  <div class="prose">',
         '    <p class="lead-sub">I&rsquo;m a learning experience designer, AI strategist, and innovator, grounded in learning science, focused on closing the gap between what people are taught and what the work actually demands. I prototype with frontier AI every day, and what most AI work skips is the human science: grounding what I design in how people actually think, learn, and adopt is my edge.</p>',
         '    <p>My method doesn&rsquo;t change with the size of the audience. Write the requirements down before anything gets built. Run structured pilots, then make an honest call: scale, modify, or stop.</p>',
         '    <p>The part that takes longest is the people. A tool nobody is trained to use quietly fails, so I plan the training and the support alongside it. I&rsquo;ve done that for twenty years, starting with bringing a campus onto its first learning management system. It&rsquo;s the same work now with AI.</p>',
         '    <p>Colleges have remarkable resources; what breaks down is the connection between them and the students who need them most, most of them working adults. When students feel connected and supported, they persist, and that&rsquo;s the problem I focus on now. I co-chair the Student Support and Success domain of the Maricopa district AI Resource Center and sit on its steering committee, working across all ten colleges on how AI can reduce friction in the non-classroom services that decide whether students stay.</p>',
         '    <p>My background spans design, education, and educational technology: from web and graphic design, to UX, to product management at an EdTech startup, to seven years directing instructional technology in a campus Innovation Center inside IT, to faculty in Digital Media, where I teach design and was Program Director for over a decade. I hold a master&rsquo;s in Educational Technology with an adult online-learning emphasis, and connectivism and personal learning environments are still the floor under everything I design. I convened a campus AI community of practice as a League for Innovation AI Fellow.</p>',
         '    <p>I start from measurable outcomes: what students need to be able to do when they graduate, including the AI skills their industries already expect. Because the goal is demonstrated skill, students show what they can do through authentic, performance-based work: portfolios, presentations, real job searches, networking. Experiential learning is central to how I teach. I built a design studio where students take on real client work with live briefs and hard deadlines, which grew past the course into a grant-funded paid studio I now advise, and I oversee the program&rsquo;s internship, placing and mentoring students in real work with local businesses and industry partners. Giving young people genuine ownership, and watching them rise to it, is some of the most important work I do.</p>',
         '    <p>The question I keep returning to is what still counts as evidence of learning now that an AI model can produce the artifact. So I design assessment around process evidence rather than the finished thing, and I test whether it holds before asking anyone else to adopt it.</p>',
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
