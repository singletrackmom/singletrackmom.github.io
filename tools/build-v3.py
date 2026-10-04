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
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v=20261002c">{extra_head}
<link rel="icon" href="/favicon.ico" sizes="any">
</head>'''

HEADER = '''<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="site-head">
  <div class="site-bar">
    <a class="site-name" href="/">Michelle Blomberg</a>
    <nav class="site-nav" aria-label="Primary">
      <a href="/">Home</a>
      <a href="/#work">Work</a>
      <a href="/#personal">Personal</a>
      <a href="/about.html">About</a>
    </nav>
  </div>
</header>

<main id="main">'''

FOOTER = '''</main>

<footer class="sitefoot">
<div class="foot-links"><a href="/">Home</a><a href="/#work">Work</a><a href="/about.html">About</a><a href="#" class="mailme">Email</a><a href="#">Top &uarr;</a></div>
<div class="foot">&copy; 2026 Michelle Blomberg. All rights reserved.</div>
</footer>
<script src="/v3/assets/mail.js"></script>
</body>
</html>'''


# ============================================================ THE CONTENT MODEL
# Every word on the site lives here. Copy carried over from v2, which had the
# right argument and the wrong formatting.

SECTIONS = [
 {
  'slug': 'dial', 'name': 'Dial Your Course', 'thumb': '/course-dialer/cover.jpg',
  'eyebrow': 'Course Design Tools &middot; Case study',
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
  'eyebrow': 'Course Design Tools &middot; Case study',
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
  'eyebrow': 'Student Success Tools &middot; Case study',
  'lead': 'Training wheels for building agents. Students assemble a career-launch environment by hand across the capstone, and leave owning it.',
  'summary': 'Career-readiness work usually disappears when Canvas access ends at graduation. Render is a personal learning environment the student owns: goals, job log, resume vault, skills, networking and interview prep in one place, every piece anchored to one real job the student picks on day one. <strong>Students run the agents in their own free AI accounts and leave with the whole package.</strong> It is built in partnership with campus Career Services, so it reinforces what a career advisor would say.',
  'goal': 'Design students graduate with a portfolio and no method for finding work. The goal is that a student leaves the semester with working career infrastructure they own, rather than a folder of assignments they will never open again.',
  'audience': 'Final-semester students in a capstone course, and the career services staff who would otherwise see them for the first time after graduation.',
  'process': 'Students set goals and pick one real reach job on day one, then build the environment across the AVC 248 capstone. At the end, Render runs a gap analysis between what the student actually built and what that job asks for, and exports the package: their agents and skills as prompt files, a job tracker, their tailored documents, and a personal learning plan. Sign-in is a first name only, kept in the student&rsquo;s own browser. Usability tested with students in March 2026 and revised from what that surfaced.',
  'thumb': '/render/render_cover.jpg',
  'projects': [
    {'group': 'Agents students build inside Render', 'slug': 'counselor', 'name': 'Career Counselor', 'status': 'Prototype', 'blurb': 'One agent that holds the whole picture and names the single next thing to do.', 'summary': 'One agent that holds the whole picture and names the single next thing to do. Most career advice assumes the student already knows what they want. Students who do not know their next move stall, and a list of forty tasks makes it worse. The goal is one move the student can finish this week.', 'goal': 'Most career advice assumes the student already knows what they want. Students who do not know their next move stall, and a list of forty tasks makes it worse. The goal is one move the student can finish this week.', 'audience': 'Capstone students, whether they are applying for jobs, going freelance, or still deciding.', 'process': 'It asks before it advises. It reads the student&rsquo;s goals statement and creative identity, resume and portfolio links, the jobs they saved, and where they are in the semester, then returns one next step sized to the week. It is the only agent in Render that sees everything.', 'outcome': 'Prototype, in the fall capstone pilot.', 'thumb': '/render/render-01-profile.jpg', 'tool': '/render/career-counselor.html', 'tool_label': 'See a worked example'},
    {'group': 'Agents students build inside Render', 'slug': 'job-search', 'name': 'Job Search Agent', 'status': 'Prototype', 'blurb': 'A search agent built from the student&rsquo;s own goals that confirms every job is still open before showing it.', 'summary': 'A search agent built from the student&rsquo;s own goals that confirms every job is still open before showing it. A search result is not proof a job exists. Students lose days applying to postings that closed months ago. The goal is a feed of openings that fit the student and are verified live.', 'goal': 'A search result is not proof a job exists. Students lose days applying to postings that closed months ago. The goal is a feed of openings that fit the student and are verified live.', 'audience': 'Capstone students starting a first professional search, who run the agent in their own AI account.', 'process': 'The student sets the titles, the location, a pay floor, and what to skip. Before a job reaches the feed, the agent opens the employer&rsquo;s own careers page and confirms the posting is there. Fit is judged against the posting&rsquo;s stated requirements, compared with the student&rsquo;s resume and portfolio.', 'outcome': 'Prototype, in the fall capstone pilot.', 'thumb': '/render/render-02-jobs.png', 'tool': '/render/job-search-agent.html', 'tool_label': 'See a worked example'},
    {'group': 'Agents students build inside Render', 'slug': 'hiring-committee', 'name': 'Hiring Committee', 'status': 'Prototype', 'blurb': 'Four synthetic reviewers score an application separately, then say exactly what to fix.', 'summary': 'Four synthetic reviewers score an application separately, then say exactly what to fix. Students send applications without knowing how a committee reads them. The goal is feedback tied to the posting, before a real committee sees the application.', 'goal': 'Students send applications without knowing how a committee reads them. The goal is feedback tied to the posting, before a real committee sees the application.', 'audience': 'Capstone students preparing a resume and portfolio for one specific job.', 'process': 'Four reviewers score the application independently. Every score traces back to one of the minimum qualifications in the posting, so the student can see where it came from, and each reviewer names the specific fix.', 'outcome': 'Prototype, in the fall capstone pilot.', 'thumb': '/render/render-03-resume.png', 'tool': '/render/hiring-panel.html', 'tool_label': 'See a worked example'},
    {'group': 'Agents students build inside Render', 'slug': 'interview-panel', 'name': 'Interview Panel', 'status': 'Prototype', 'blurb': 'The same four reviewers interview the student for that job and coach every answer.', 'summary': 'The same four reviewers interview the student for that job and coach every answer. A first interview is usually the first time a student says their answers out loud. The goal is practice against the real job, with coaching on each answer.', 'goal': 'A first interview is usually the first time a student says their answers out loud. The goal is practice against the real job, with coaching on each answer.', 'audience': 'Capstone students with an application ready for one specific job.', 'process': 'The panel that scored the application now interviews for it. Each question traces to a minimum qualification in the posting, and each answer gets coaching before the next question.', 'outcome': 'Prototype, in the fall capstone pilot.', 'thumb': '/render/render-interview.jpg', 'tool': '/render/interview-panel.html', 'tool_label': 'See a worked example'},
    {'group': 'The same pattern, running on a schedule', 'slug': 'dma-jobs', 'name': 'Digital Media Jobs Feed', 'status': 'Built and running', 'blurb': 'Posts verified entry-level openings to the program Discord every day.', 'summary': 'Posts verified entry-level openings to the program Discord every day. Job boards show students what is popular, not what they can get. The goal is real openings a current student or recent graduate can land, delivered where students already are.', 'goal': 'Job boards show students what is popular, not what they can get. The goal is real openings a current student or recent graduate can land, delivered where students already are.', 'audience': 'Digital Media Arts students and recent graduates, most of them still enrolled and already working.', 'process': 'Runs daily. It checks a log so nothing posts twice, searches, then filters hard on level and pay realism: zero to one year of experience, internships and part-time work preferred, and a pay ceiling so a senior role with a junior title never gets through. Approved jobs post to the jobs channel by webhook.', 'outcome': 'Built and running daily. The filters were tightened after two posts aimed too high, and that correction is written into the rules.', 'thumb': '/discord/discord-cover.png', 'tool': '/discord/overview.html', 'tool_label': 'See the student community'},
    {'group': 'The same pattern, running on a schedule', 'slug': 'find-your-flow', 'name': 'Find Your Flow', 'status': 'Retired, having succeeded', 'blurb': 'One realistic career a day, each paired with a live opening and verified pay.', 'summary': 'One realistic career a day, each paired with a live opening and verified pay. Choosing a career as one giant list is overwhelming. The goal is one honest option at a time, small enough to look at.', 'goal': 'Choosing a career as one giant list is overwhelming. The goal is one honest option at a time, small enough to look at.', 'audience': 'One young person exploring careers.', 'process': 'Each morning the agent picks a career, verifies growth and median pay against the U.S. Bureau of Labor Statistics, finds a real local training path, confirms one live job on an employer&rsquo;s own careers page, and composes a short letter in a locked, phone-first template.', 'outcome': 'Retired, having succeeded. Twenty-seven letters went out, the reader chose a direction and enrolled, and the agent was switched off.', 'thumb': '/flow/flow_cover.jpg', 'tool': '/flow/overview.html', 'tool_label': 'Read the case study'},
  ],
  'status':'Prototype, in pilot this fall in one section of the AVC 248 capstone. Not in production. The interface is being redesigned against updated requirements. The scheduled agents in the second row run outside Render: they are the same pattern with the training wheels off.',
 },
 {
  'slug': 'copamigo', 'name': 'CopaMigo',
  'eyebrow': 'Student Success Tools &middot; Case study',
  'lead': 'Student-facing routing for campus services, so a student asking a question in their own words reaches the right office.',
  'summary': 'Every campus already offers more support than its students can find. The services exist; students just do not know which office handles their problem, or what it is called. <strong>A student describes the situation in plain language, in their own language, and CopaMigo routes them to the right service with a handoff card:</strong> the contact, the hours, and what to ask for. Its answers are written rather than retrieved, drawn from the questions students actually bring and shaped with the offices that handle them. Anonymous, no login.',
  'goal': 'Campus service information is organized the way the institution is organized, not the way a student asks. The goal is that a student describing a problem in their own words, in their own language, reaches the right human being with enough context to make the handoff work.',
  'audience': 'Students who do not know the name of the office they need, and the advising and support staff who currently absorb the routing work by hand.',
  'process': 'Fourteen service modules built on more than a hundred hand-verified college URLs, with a campus picker covering all ten district colleges. A student types or speaks the situation and gets an answer in the same language, plus a handoff card carrying contact details, opening hours and what to ask for. Routine questions are answered inline; everything else reaches a person faster. It is anonymous, with no login.',
  'thumb': '/copamigo/copamigo_cover.jpg?v=2',
  'projects': [],
  'status':'A working prototype, embedded in the Digital Media Arts program&rsquo;s Discord, where students are testing it. The district has licensed an enterprise platform for the same need, and CopaMigo&rsquo;s curated questions and answers, its plain-language routing, and its more than one hundred verified service links are ready to seed that platform. Until then the pilot continues, and what it shows about how students ask for help informs whichever tool ends up in front of every student.',
 },
 {
  'slug': 'adoption', 'name': 'Adoption and Enablement', 'thumb': '/studio/studio-cover.jpg',
  'case': '    <h2>Campus LMS Adoption</h2>\n    <h3>Before</h3>\n    <p>Course materials lived everywhere: individual course websites, handouts and Word documents, an open-source learning management system, a discussion board application, and a shared drive. A team of developers, with students working alongside them through the Teaching and Learning Co-op, an experiential learning program, built one-off pieces for individual instructors.</p>\n    <h3>Options considered</h3>\n    <ul>\n      <li>Join the district&rsquo;s existing Blackboard instance</li>\n      <li>Join another college&rsquo;s system, built on SharePoint</li>\n      <li>Desire2Learn</li>\n      <li>Moodle</li>\n      <li>Build a campus system on open source</li>\n    </ul>\n    <h3>Decision</h3>\n    <p>A campus evaluation and request for proposals, led by the Director of Instructional Technology and sponsored by the dean of administrative services and the vice president of academic affairs. The district instance met the requirements within the budget and staff available, so the campus joined rather than built.</p>\n    <h3>Rollout</h3>\n    <p>A pilot with early adopters came first. Other faculty joined once they saw it working in a colleague&rsquo;s course, and nearly every faculty member was eventually on it. Support ran through a single point of contact helpdesk, workshops, and shared course design standards.</p>\n    <h3>What it taught</h3>\n    <p>Instructional technology and training both sat inside IT, which did not have the faculty ownership that teaching and learning needs. The result was a co-authored proposal for a faculty-run center for teaching and learning. Online course governance at the college is faculty-led today.</p>',
  'eyebrow': 'AI Adoption &middot; Case study',
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
  'eyebrow': 'Personal &middot; Case study',
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
  'eyebrow': 'Personal &middot; Case study',
  'lead': 'A service record that follows a mountain bike for its whole life, so the maintenance history survives the sale.',
  'summary': 'People buy mountain bikes costing five to fifteen thousand dollars and then do not maintain them on schedule, because the schedule is complicated. Suspension is due by ride hours, drivetrains and tires by miles, brake bleeds and sealant by the calendar. Three clocks on one bike. <strong>Also here as evidence of the method:</strong> a specification, a competitive scan, and a working build.',
  'goal': 'People buy mountain bikes costing five to fifteen thousand dollars and then do not maintain them on schedule, because the schedule is complicated: suspension is due by ride hours, drivetrains and tires by miles, brake bleeds and sealant by the calendar. Three clocks on one bike. The goal is a service record that survives the sale.',
  'audience': 'Riders maintaining their own bikes, and the second owner who inherits a machine with no history.',
  'process': 'A written specification and a competitive scan came first, then the build. Three separate service clocks tracked per component, reported against the manufacturer intervals. Strava data is simulated. Nothing persists between reloads, deliberately, so it runs identically as a local file or a hosted page.',
  'tool': '/traillog/', 'tool_label': 'Open Trail Log', 'thumb': '/traillog/traillog-cover.png',
  'projects': [],
  'status':'Built and running on sample data, with a written specification and a competitive scan behind it. Strava is simulated. Nothing persists between reloads, deliberately, so it runs the same as a local file or a hosted page.',
 },
]


# ============================================================ THE FOUR TEMPLATES

def page(title, body, script=None, extra_head='', main_class=None, current=None):
    tail = FOOTER
    if script:
        tail = tail.replace('</body>', f'<script src="{script}"></script>\n</body>')
    header = HEADER
    if current == 'home':
        header = header.replace('<a class="site-name" href="/">', '<a class="site-name" href="/" aria-current="page">').replace('<a href="/">Home</a>', '<a href="/" aria-current="page">Home</a>', 1)
    elif current == 'about':
        header = header.replace('<a href="/about.html">About</a>', '<a href="/about.html" aria-current="page">About</a>', 1)
    if main_class:
        header = header.replace('<main id="main">', f'<main id="main" class="{main_class}">')
    return HEAD.format(title=title, extra_head=extra_head) + '\n' + header + '\n' + body + '\n' + tail + '\n'


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
    if (sec.get('goal') or not any('href' not in p for p in sec['projects'])) and not sec.get('tool'):
        b.append('  <div class="links">')
        b.append(f'    <a class="primary" href="/v3/{sec["slug"]}/overview.html">Overview</a>')
        b.append(f'    <a href="/v3/{sec["slug"]}/prd.html">PRD</a>')
        b.append('  </div>')
    group = None
    for p in sec['projects']:
        if p.get('group') != group or group is None and p is sec['projects'][0]:
            if p is not sec['projects'][0]:
                b.append('  </div>')
            group = p.get('group')
            if group:
                b.append(f'  <p class="feat-label">{group}</p>')
            b.append('  <div class="feat">')
        href = p.get('href') or f"/v3/{sec['slug']}/{p['slug']}/overview.html"
        thumb = p.get('thumb') or sec.get('thumb')
        inner = (f'<img src="{thumb}" alt="">' if thumb else '')
        b.append(f'    <a href="{href}"><span class="feat-thumb">{inner}</span>'
                 f'<span class="feat-body"><span class="feat-t">{p["name"]}</span>'
                 f'<span class="feat-d">{p["status"]}. {p["blurb"]}</span></span></a>')
    if sec['projects']:
        b.append('  </div>')
    if sec.get('case'):
        b += ['  <div class="prose">', sec['case'], '  </div>']
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
         f'  <p class="eyebrow">{sec["eyebrow"]}</p>',
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
         f'  <p class="eyebrow">{sec["eyebrow"]}</p>',
         tabs(sec, proj, 'prd'),
         f'  <p class="lead-sub">{lead}</p>',
         '  <div class="prose">',
         '    <h2>1. Summary</h2>', f'    <p>{(proj or {}).get("summary") or sec["summary"]}</p>',
         '    <h2>2. Goal</h2>', f'    <p>{proj["goal"] if proj else sec["goal"]}</p>',
         '    <h2>3. Users and context</h2>', f'    <p>{proj["audience"] if proj else sec["audience"]}</p>',
         '    <h2>4. How it works</h2>', f'    <p>{proj["process"] if proj else sec["process"]}</p>',
         '    <h2>5. Data, privacy, and governance</h2>',
         '    <p>Each tool collects only what it needs to work and tells the user what that is. Privacy, security and accessibility are reviewed before a pilot starts, not after.</p>',
         '    <h2>Status</h2>', f'    <p>{proj["outcome"] if proj else sec["status"]}</p>',
         '  </div>']
    return page(f'{name} PRD, Michelle Blomberg', '\n'.join(b))


# ============================================================ THE HOME PAGE
# Five tabs. Card titles describe the work; the tool's own name comes second,
# because nobody clicks a name they do not know. A tab with nothing ready to
# show is left out of HOME_TABS until it has something.

HOME_TABS = [
 ('adopt',   'AI Adoption'),
 ('studies', 'Usability Studies'),
 ('student', 'Student Success Tools'),
 ('course',  'Course Design Tools'),
 ('teach',   'Teaching'),
 ('personal','Personal'),
]

HOME_CARDS = [
 # cat, title, tool name, href, thumb, one sentence
 ('adopt','AI Request Intake','AI Opportunity Pipeline','/pipeline/overview.html','/pipeline/pipeline_cover.jpg',
  'Early-stage prototype, in review and revision with the domain. An inventory of the AI tools ten colleges already have, with written requirements for the front door that comes next.'),
 ('adopt','Campus Technology Adoption','Adoption and Enablement','/v3/adoption/','/studio/studio-cover.jpg',
  'Moving a campus from scattered tools onto one learning management system, and the faculty-run model that made adoption stick.'),
 ('studies','Student Journey Barriers Study','Ten-college usability study','/v3/studies/journey/','/airc-sss/cover.svg',
  'Synthetic-student agents walk the real student journey across ten Maricopa colleges to find where students hit barriers, ranked into prioritized AI pilots.'),
 ('studies','Gemini Access Study','What Gemini blocks for students under 18','/v3/studies/gemini/','/gemini-study/evidence/u18-tools-menu.jpg',
  'Twenty-seven course assignments run in an under-18 account and an 18-and-older account, to show a district exactly what younger students cannot do.'),
 ('student','Career Launch Tool','Render','/v3/render/','/render/render_cover.jpg',
  'Training wheels for building agents: students build a career-launch environment by hand and graduate owning the agents. Includes the scheduled agents built on the same pattern.'),
 ('student','Student Support Routing','CopaMigo','/copamigo/overview.html','/copamigo/copamigo_cover.jpg?v=2',
  'A multilingual AI triage tool that answers in the student&rsquo;s own language and routes their problem to the right human service with a warm handoff.'),
 ('course','Course Review Tool','Dial Your Course','/course-dialer/overview.html','/course-dialer/cover.jpg',
  'Drop in a Canvas course and nineteen checks run against it, from seat hours to accessibility to AI resistance, then the fixes come back.'),
 ('course','Syllabus Compliance Check','Syllabus Checker','/syllabus-checker/overview.html','/syllabus-checker/cover.jpg',
  'A submit-and-check tool that verifies syllabi against MCCCD and program requirements, replies to faculty instantly, and logs every submission.'),
 ('course','Authentic Assessment Simulations','AI-resistant assessment','/authentic-assessment/','/authentic-assessment/authentic_cover.svg',
  'Replace the AI-cheatable exam with an authentic task the student performs and defends, including a built suite of graduate data-science simulations.'),
 ('course','AI-Assisted Course Design','Synthetic SMEs','/synthetic-smes/','/synthetic-smes/how-it-works.svg',
  'A panel of AI agents drafts a course against a fixed checklist of quality standards, and the faculty member who would teach it signs off before a student sees it.'),
 ('teach','Client-Work Design Studio','Design Studio','/studio/overview.html','/studio/studio-cover.jpg',
  'Real clients, real briefs, real deadlines. Students took live campus work and shipped it, from a 90-foot mural to motion and publications.'),
 ('teach','Work-Based Learning','Internship Program','/internship/overview.html','/canvas/internships_cover.jpg',
  'Placing and mentoring students in real work with local businesses and industry partners.'),
 ('teach','Curriculum Strategy','Program Design','/program-design/overview.html','/program-design/majors-chart.png',
  'How the Digital Media program is structured, from what industry asks for back to the courses.'),
 ('teach','Program Redesign','Stackable Microcredentials','/microcredentials/overview.html','/microcredentials/stackables-cover.png',
  'Short credentials that stack toward the degree, so students leave each semester with something an employer recognizes.'),
 ('teach','Online Capstone Course','Design Self Promotion, AVC 248','/learning-design/avc248.html','/canvas/avc248/avc248-canvas.jpg?v=2',
  'The capstone where students build a portfolio and run a real job search.'),
 ('teach','Course Redesign','Intro to Digital Arts, AVC 100','/avc100/overview.html','/avc100/skills-chart.png',
  'An introductory course rebuilt backward from measurable outcomes.'),
 ('teach','Curriculum and Course Design','UX Design for Interactive Media','/canvas/avc2xx/design.html','/canvas/avc2xx/ux_cover.jpg',
  'A new course designed from eleven industry competencies and authentically assessed.'),
 ('teach','Student-Taught Project','Design History, AVC 183','/canvas/design-history/overview.html','/canvas/design-history/design_history_cover.jpg',
  'Students research, design and teach a piece of design history to each other.'),
 ('teach','Student-Designed Publication','The Traveler','/traveler/overview.html','/fep/traveler_cover.jpg',
  'The college&rsquo;s award-winning student literary and visual arts publication. I advise the student design team through each production cycle.'),
 ('teach','Student Community','Digital Media Discord','/discord/overview.html','/discord/discord-cover.png',
  'A closed community where students already are, for critique, group work, and tutoring, with an AI agent that posts entry-level jobs daily.'),
 ('teach','Brand System','Campus Cares Hub','/campus-cares/overview.html','/campus-cares/cares_cover.jpg',
  'A brand system for the campus basic-needs hub, designed with students.'),
 ('personal','Trip Planner','Wayfinder','/wayfinder/overview.html','/wayfinder/wayfinder_cover.jpg',
  'A road-trip planner with a campground finder, a cancellation watcher that reports the moment a site opens, and a packing list that remembers what is packed.'),
 ('personal','Bike Service Log','Trail Log','/v3/traillog/','/traillog/traillog-cover.png',
  'A service record that follows a mountain bike for its whole life, so the maintenance history survives the sale.'),
]


FIT_THUMBS = ('/synthetic-smes/how-it-works.svg', '/avc100/skills-chart.png', '/program-design/majors-chart.png')


def home_card(cat, title, tool, href, thumb, desc):
    """Same three lines as a v1 home card: title, subtitle, one sentence."""
    inner = f'<img src="{thumb}" alt="">' if thumb else 'Screenshot to come'
    fit = ' fit' if thumb in FIT_THUMBS else ''
    return (f'    <a href="{href}" data-cat="{cat}"><span class="feat-thumb{fit}">{inner}</span>'
            f'<span class="feat-body"><span class="feat-t">{title}</span>'
            f'<span class="feat-s">{tool}</span>'
            f'<span class="feat-d">{desc}</span></span></a>')


def home_page():
    b = ['  <h1 class="lead-intro">I help colleges decide which AI ideas are worth doing, then get people using the ones that are.</h1>',
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
         '    <p class="askhint">Try: <button type="button" class="askhint-link" onclick="abAsk(\'whatnot\',\'How do you decide what not to build?\')">How do you decide what not to build?</button> <button type="button" class="askhint-link" onclick="abAsk(\'adkar\',\'Do you use ADKAR?\')">Do you use ADKAR?</button> <button type="button" class="askhint-link" onclick="abAsk(\'stem\',\'Have you worked with a STEM audience?\')">Have you worked with a STEM audience?</button></p>',
         '    <div class="asklog" id="abLog"></div>',
         '  </div>',
         '',
         '  <h2 class="work-head" id="work">Work</h2>',
         '  <nav class="tabs" id="worktabs" aria-label="Filter work by section">'
         + '<button type="button" class="tab" data-cat="all" aria-selected="true">All</button>'
         + ''.join(f'<button type="button" class="tab" data-cat="{k}" aria-selected="false">{n}</button>' for k, n in HOME_TABS)
         + '</nav>',
         '  <div class="feat" id="workgrid">']
    for cat, title, tool, href, thumb, desc in HOME_CARDS:
        b.append(home_card(cat, title, tool, href, thumb, desc))
    b.append('  </div>')
    b.append('  <script src="/v3/assets/workfilter.js"></script>')
    return page('Michelle Blomberg', '\n'.join(b), script='/v3/assets/askbar.js', current='home')


def about_page():
    """ABOUT. v1 layout: a small circular portrait floated beside the prose.
    Text copied from the live about.html on 2 Oct 2026. Keep the two in step."""
    b = ['  <h1>About</h1>',
         '  <img class="about-face" src="/cultivate/mblomberg.jpg" alt="Michelle Blomberg">',
         '  <div class="prose">',
         '    <p class="lead-sub">I&rsquo;m a learning experience designer, AI strategist, and innovator, grounded in learning science, focused on closing the gap between what people are taught and what the work actually demands. I prototype with frontier AI every day, and what most AI work skips is the human science: grounding what I design in how people actually think, learn, and adopt is my edge.</p>',
         '    <p>My method doesn&rsquo;t change with the size of the audience. Write the requirements down before anything gets built. Run structured pilots, then make an honest call: scale, modify, or stop.</p>',
         '    <p>The part that takes longest is the people. A tool nobody is trained to use quietly fails, so I plan the training and the support alongside it. I&rsquo;ve done that for twenty years, starting with bringing a campus onto its first campus-wide learning management system. It&rsquo;s the same work now with AI.</p>',
         '    <p>Colleges have remarkable resources; what breaks down is the connection between them and the students who need them most, most of them working adults. When students feel connected and supported, they persist, and that&rsquo;s the problem I focus on now. I co-chair the Student Support and Success domain of the Maricopa district AI Resource Center and sit on its steering committee, working across all ten colleges on how AI can reduce friction in the non-classroom services that decide whether students stay.</p>',
         '    <p>My background spans design, education, and educational technology: from web and graphic design, to UX, to product management at an EdTech startup, to seven years as Director of Instructional Technology for a campus Innovation Center inside IT, to faculty in Digital Media, where I teach design and was Program Director for over a decade. I hold a master&rsquo;s in Educational Technology with an adult online-learning emphasis, and connectivism and personal learning environments are still the floor under everything I design. I convened a campus AI community of practice as a League for Innovation AI Fellow.</p>',
         '    <p>I start from measurable outcomes: what students need to be able to do when they graduate, including the AI skills their industries already expect. Because the goal is demonstrated skill, students show what they can do through authentic, performance-based work: portfolios, presentations, real job searches, networking. Experiential learning is central to how I teach. I built a design studio where students take on real client work with live briefs and hard deadlines, which grew past the course into a grant-funded paid studio I now advise, and I oversee the program&rsquo;s internship, placing and mentoring students in real work with local businesses and industry partners. Giving young people genuine ownership, and watching them rise to it, is some of the most important work I do.</p>',
         '    <p>The question I keep returning to is what still counts as evidence of learning now that an AI model can produce the artifact. So I design assessment around process evidence rather than the finished thing, and I test whether it holds before asking anyone else to adopt it.</p>',
         '  </div>']
    return page('About, Michelle Blomberg', '\n'.join(b), current='about')


# ============================================================ CARRIED-OVER STUDIES
# v1 content, v3 chrome. The words, tables and figures come from the v1 source
# page untouched. The header, tab row and footer are written by this file, so
# they cannot drift. Edit the words in the source file, then re-run this script.

CARRIED = [
 {'out': 'studies/journey', 'src': 'airc-sss', 'eyebrow': 'Usability Studies &middot; Case study',
  'tabs': [('Overview', 'index.html'), ('Method', 'method.html'), ('Agents and ethics', 'agents.html'),
           ('Progress', 'progress.html'), ('What happens next', 'next.html')]},
 {'out': 'studies/gemini', 'src': 'gemini-study', 'eyebrow': 'Usability Studies &middot; Case study',
  'tabs': [('Overview', 'index.html'), ('Assignments', 'assignments.html'), ('Results', 'results.html'),
           ('PRD', 'prd.html'), ('References', 'references.html')]},
]


def carried_page(group, label, fname):
    src = open(os.path.join(ROOT, group['src'], fname), encoding='utf-8').read()
    title = re.search(r'<title>(.*?)</title>', src, re.S).group(1).strip()
    styles = ''.join('\n' + m for m in re.findall(r'<style.*?</style>', src[:src.index('</head>')], re.S))
    m = re.search(r'<main([^>]*)>(.*)</main>', src, re.S)
    cls = re.search(r'class="([^"]*)"', m.group(1))
    body = m.group(2)
    base = f"/v3/{group['out']}/"
    nav = f'<nav class="tabs" aria-label="{group["eyebrow"]} pages">'
    for lab, fn in group['tabs']:
        href = base if fn == 'index.html' else base + fn
        cur = ' aria-current="page"' if fn == fname else ''
        nav += f'<a class="tab" href="{href}"{cur}>{lab}</a>'
    nav += '</nav>'
    body, n = re.subn(r'<nav class="tabs".*?</nav>', lambda _: nav, body, count=1, flags=re.S)
    assert n == 1, f'no tab row found in {fname}'
    body = re.sub(r'<p class="eyebrow">.*?</p>', lambda _: f'<p class="eyebrow">{group["eyebrow"]}</p>', body, count=1, flags=re.S)
    return page(title, body.strip('\n'), extra_head=styles, main_class=cls.group(1) if cls else None)


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


ROOT_META = '''<meta name="description" content="Michelle Blomberg helps colleges decide which AI ideas are worth doing, then get people using them. AI intake, usability research, requirements, pilots and adoption in higher education.">
<meta property="og:type" content="website">
<meta property="og:title" content="Michelle Blomberg, AI adoption and learning experience design in higher education">
<meta property="og:description" content="AI intake, usability research, requirements, pilots and adoption in higher education.">
<meta property="og:url" content="https://michelleblomberg.com/">'''


def emit_root(name, html, written, mismatched):
    """The home page and About also live at the site root. Same page, indexable."""
    html = html.replace('<meta name="robots" content="noindex, nofollow">', ROOT_META if name == 'index.html' else '<meta name="description" content="About Michelle Blomberg.">')
    full = os.path.join(ROOT, name)
    if CHECK:
        if not os.path.exists(full) or open(full, encoding='utf-8').read() != html:
            mismatched.append('../' + name)
        return
    open(full, 'w', encoding='utf-8').write(html)
    written.append('../' + name)


def main():
    written, mismatched = [], []
    emit_root('index.html', home_page(), written, mismatched)
    emit_root('about.html', about_page(), written, mismatched)
    emit('index.html', home_page(), written, mismatched)
    emit('about.html', about_page(), written, mismatched)
    for s in SECTIONS:
        emit(f'{s["slug"]}/index.html', section_page(s), written, mismatched)
        gen = [p for p in s['projects'] if 'href' not in p]
        for p in gen:
            emit(f'{s["slug"]}/{p["slug"]}/overview.html', overview_page(s, p), written, mismatched)
            emit(f'{s["slug"]}/{p["slug"]}/prd.html', prd_page(s, p), written, mismatched)
        if s.get('goal') or not gen:
            emit(f'{s["slug"]}/overview.html', overview_page(s), written, mismatched)
            emit(f'{s["slug"]}/prd.html', prd_page(s), written, mismatched)

    for g in CARRIED:
        for label, fname in g['tabs']:
            emit(f'{g["out"]}/{fname}', carried_page(g, label, fname), written, mismatched)

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
