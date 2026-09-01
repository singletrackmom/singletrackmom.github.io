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
  'slug': 'campground', 'name': 'Campground Finder',
  'eyebrow': 'Section &middot; Personal Projects &middot; UX Design',
  'lead': 'Watches named campgrounds for a cancellation and reports the moment a site opens.',
  'summary': 'The good campgrounds are booked eleven months out and the only way in is somebody else&rsquo;s change of plans. <strong>This is here as evidence of the method rather than as a hobby project:</strong> an idea taken through to a working build, which is the outcome Render is meant to produce in a student. Two halves, a search form and a scheduled watcher that writes what it finds to a calendar.',
  'projects': [],
  'status':'Built and used. It ran every day for a month across a Yosemite trip and is currently switched off between trips. The watcher ran daily against Peak One Campground at Dillon Reservoir through June 2026, and a second instance watched Tahoe-shore sites through May. Both are disabled rather than deleted, because the pattern is the useful part.',
 },
 {
  'slug': 'traillog', 'name': 'Trail Log',
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
         '  <p class="eyebrow">Learning experience, UX systems, and AI tools for education</p>',
         '  <p class="lead-sub">I build small, data-light tools, test them with real students, and publish what did not work.</p>',
         '  <div class="prose">', '    <h2 id="work">Work</h2>', '  </div>',
         '  <div class="cards">']
    for s in SECTIONS:
        b.append(f'    <a class="card" href="/v3/{s["slug"]}/"><span class="ct">{s["name"]}</span>'
                 f'<span class="what">{s["lead"]}</span></a>')
    b.append('  </div>')
    return page('Michelle Blomberg', '\n'.join(b))


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
