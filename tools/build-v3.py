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

# THE LAUNCH SWITCH. False: v3 lives at /v3/ only and the old home page stays at the root.
# True: the v3 home page and About are also written to the site root and every menu points there.
# Michelle flips this, nobody else. Set to True on 4 Oct 2026 at her instruction: launch.
# The previous home page and About are archived at /v1/.
PROMOTE = True

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
      <a href="/#work">Work</a>
      <a href="/about.html">About</a>
    </nav>
  </div>
</header>

<main id="main">'''

FOOTER = '''</main>

<footer class="sitefoot">
<div class="foot-links"><a href="/#work">Work</a><a href="/about.html">About</a><a href="#" class="mailme">Email</a><a href="#">Top &uarr;</a></div>
<div class="foot">&copy; 2026 Michelle Blomberg. All rights reserved.</div>
</footer>
<script src="/v3/assets/mail.js?v=20261004e"></script>
<script src="/v3/assets/opendetail.js?v=20261004e"></script>
</body>
</html>'''


# ============================================================ THE CONTENT MODEL
# Every word on the site lives here. Copy carried over from v2, which had the
# right argument and the wrong formatting.

SECTIONS = [
 {
  'slug': 'dial', 'name': 'Dial Your Course', 'prd_href': '/course-dialer/prd.html', 'thumb': '/course-dialer/cover.jpg',
  'eyebrow': 'Course Design Tools &middot; Case study',
  'lead': 'A Canvas course goes in. Nineteen checks run. What to fix comes back.',
  'summary': 'Dial Your Course reads a real Canvas course package, runs nineteen checks against it, from seat hours to outcome alignment to accessibility, and writes the approved fixes back into the package. <strong>Every check is rule-based and contains no AI.</strong> A quality standard is a published list, so checking against it is a lookup: the same course returns the same answer every time, and every finding traces back to the sentence in the standard that produced it. A faculty member being told their course falls short deserves that traceability. It began as the checks I performed by hand as a peer and lead reviewer for Quality Matters and OSCQR.',
  'projects': [
    {'slug':'syllabus','name':'Syllabus Checker','prd_href':'/syllabus-checker/prd.html','status':'Built and in use','thumb':'/syllabus-checker/cover.jpg',
     'blurb':'Checks a finished syllabus against the required elements and reports what is missing.',
     'goal':'A syllabus has to carry a set of required elements every term, and the check is done by eye against a list, or not at all.',
     'audience':'Any instructor writing a syllabus, and the program director who reviews it before term.',
     'process':'Rule-based, no AI. The required elements are a published list, so the check is a lookup against that list and the result is the same every run.',
     'outcome':'Built and running as a standalone tool.'},
    {'slug':'quality','name':'Quality Check','status':'In use',
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
  'slug': 'build', 'name': 'Build Your Course', 'no_prd': True, 'thumb': '/authentic-assessment/authentic_cover.svg',
  'eyebrow': 'Course Design Tools &middot; Case study',
  'lead': 'Dial Your Course tells you what is wrong. This builds the replacement.',
  'summary': 'Checking a course and building one are different problems with different trust requirements, and collapsing them into one tool would damage both. The checks are deterministic. Building an assessment, or judging whether an open license permits what you are about to do, is not. <strong>So these two tools use AI, and the human stays in every loop.</strong> Nothing is applied automatically: every suggestion arrives as a proposed replacement with four choices, apply, edit first, dismiss with a reason, or defer.',
  'projects': [
    {'slug':'assessment','no_prd':True,'name':'Authentic Assessment','status':'Pilot build',
     'blurb':'Takes an assignment a student could hand to a model and proposes a replacement that asks for process evidence instead.',
     'goal':'Once a model can produce the artifact, the artifact stops being evidence of learning. The assignment has to ask for something else: the record of making, the response to critique, the decision a student can defend.',
     'audience':'An instructor who now knows a module is weak and has to fix it, which is where most quality processes quietly end.',
     'process':'Uses AI, gated on human acceptance. Nothing leaves the tool until the before and after have been seen side by side. The dismissal reason is recorded, because it is the record of where the method was wrong.',
     'outcome':'Built and working as a pilot build, and it has produced results.'},
    {'slug':'oer','no_prd':True,'name':'OER Finder','status':'Specified, not built',
     'blurb':'Finds openly licensed material for a module and records the license that permits the use.',
     'goal':'Open material is only usable if the license actually permits what you intend, and that judgment is where most OER adoption stalls.',
     'audience':'An instructor building from open resources without a librarian on call.',
     'process':'Uses AI to find candidates, then records the license and the permission it grants alongside each one. Human acceptance required.',
     'outcome':'Specified and not built. The method has been run by hand.'},
  ],
  'status':'Authentic Assessment is built and working as a pilot build and has produced results. OER Finder is specified and not built. Both methods were first run by hand on a full course: a complete fifteen-week graduate data science course built from open educational resources in a field I do not teach, with four original simulations for its assessments and a recorded oral defense carrying the grade.',
 },
 {
  'slug': 'render', 'name': 'Render', 'prd_href': '/render/prd.html', 'tool': '/render/', 'tool_label': 'Live tool',
  # The written overview at /render/overview.html is THE Render overview. The generated section page
  # forwards to it, and the cards below are written into it between the render-cards markers.
  'canonical': '/render/overview.html',
  'tabs_all': [('Overview', '/render/overview.html', 'overview'), ('Live tool', '/render/', 'tool'),
               ('Walkthrough', '/render/walkthrough.html', 'walk'), ('Student example', '/render/sample-dashboard.html', 'sample'),
               ('AI Mentor', '/v3/render/counselor/overview.html', 'counselor'), ('Job search', '/v3/render/job-search/overview.html', 'job-search'),
               ('Will I Get an Interview?', '/v3/render/hiring-committee/overview.html', 'hiring-committee'),
               ('Interview panel', '/render/interview-panel.html', 'interview-panel'),
               ('Skills', '/render/training-plan-agent.html', 'skills'), ('PRD', '/render/prd.html', 'prd')],
  'eyebrow': 'Student Success Tools &middot; Case study',
  'lead': 'Training wheels for building agents. Students assemble a career-launch environment by hand across the capstone, and leave owning it.',
  'summary': 'Career-readiness work usually disappears when Canvas access ends at graduation. In Render, students build four agents by hand: an AI mentor that coaches them through the whole class and pushes them to find a human one, a job search agent, and, for every job they pick, a panel that reads their application and then interviews them. Each agent hands what it finds to the next, and the gaps they turn up become the student&rsquo;s learning plan. <strong>Students run the agents in their own free AI accounts and leave with the whole package.</strong> It is built in partnership with campus Career Services, so it reinforces what a career advisor would say.',
  'goal': 'Design students graduate with a portfolio and no method for finding work. The goal is that a student leaves the semester with working career infrastructure they own, rather than a folder of assignments they will never open again.',
  'audience': 'Final-semester students in a capstone course, and the career services staff who would otherwise see them for the first time after graduation.',
  'process': 'Students paste in the resume they wrote by hand, then build each agent from the same five parts: role, context, task, rules and handoff. The AI mentor comes first and they check in with it after every step. For each job they align their resume and cover letter themselves, and that job&rsquo;s own panel says whether the application is likely to get an interview and what to change in the resume, the letter and the portfolio. The gap list builds along the way, and the AI mentor turns it into a professional development plan, a networking plan and a path to a human mentor. Students leave with the agents as plain text files, the plans, and a one-page method for building the next one. An earlier version was usability tested with students and revised from what that surfaced.',
  'thumb': '/render/workshop-02-search.png',
  'projects': [
    {'group': 'Agents students build inside Render', 'slug': 'counselor', 'name': 'AI Mentor', 'status': 'In pilot', 'blurb': 'Built first, and it stays for the whole class. It coaches the student toward the interview, turns their gaps into a learning plan and a network, and keeps pushing them to find a human mentor.', 'summary': 'Built first, and it stays for the whole class. It coaches the student toward the interview, turns their gaps into a learning plan and a network, and keeps pushing them to find a human mentor. Most career advice assumes the student already knows what they want. Students who do not know their next move stall, and a list of forty tasks makes it worse. The goal is one move the student can finish this week.', 'goal': 'Most career advice assumes the student already knows what they want. Students who do not know their next move stall, and a list of forty tasks makes it worse. The goal is one move the student can finish this week.', 'audience': 'Capstone students, whether they are applying for jobs, going freelance, or still deciding.', 'process': 'It says it is an AI, and it asks before it advises. After every step the student pastes in an update: where each job stands, what each panel asked for, the gap list so far, and whether they have a human mentor yet. It helps them choose which openings to go after, work through a panel&rsquo;s changes without writing for them, and practice what the interview flagged. Until the student has a human mentor, every check-in ends with one small step toward finding one. At the end it returns three plans: professional development, networking, and finding a human mentor. Every reply ends with one thing to do this week.', 'outcome': 'In pilot this semester.', 'thumb': '/render/workshop-05-counselor.png', 'tool': '/render/agent-workshop.html', 'tool_label': 'Open the workshop'},
    {'group': 'Agents students build inside Render', 'slug': 'job-search', 'name': 'Job Search Agent', 'status': 'In pilot', 'blurb': 'A search agent the student builds from their own goals. It confirms every job is still open, and it notices what the postings keep asking for.', 'summary': 'A search agent the student builds from their own goals. It confirms every job is still open, and it notices what the postings keep asking for. A search result is not proof a job exists. Students lose days applying to postings that closed months ago. The goal is a feed of openings that fit the student and are verified live.', 'goal': 'A search result is not proof a job exists. Students lose days applying to postings that closed months ago. The goal is a feed of openings that fit the student and are verified live.', 'audience': 'Capstone students starting a first professional search, who run the agent in their own AI account.', 'process': 'The student sets the titles, the location, where to look, what a job must have, and what to skip. Before a job reaches the list, the agent opens the employer&rsquo;s own careers page and confirms the posting is there. It also lists what the postings keep asking for that the student&rsquo;s resume does not show yet, and that list starts the learning plan.', 'outcome': 'In pilot this semester.', 'thumb': '/render/workshop-02-search.png', 'tool': '/render/agent-workshop.html', 'tool_label': 'Open the workshop'},
    {'group': 'Agents students build inside Render', 'slug': 'hiring-committee', 'name': 'Will I Get an Interview?', 'status': 'In pilot', 'blurb': 'Every job gets its own panel of four. They read the resume the student aligned by hand, the cover letter they wrote, and their portfolio, then say what to change in each.', 'summary': 'Every job gets its own panel of four. They read the resume the student aligned by hand, the cover letter they wrote, and their portfolio, then say what to change in each. Students send applications without knowing how a committee reads them. The goal is feedback tied to the posting, before a real committee sees the application.', 'goal': 'Students send applications without knowing how a committee reads them. The goal is feedback tied to the posting, before a real committee sees the application.', 'audience': 'Capstone students with a resume and cover letter they wrote and aligned by hand for one specific job.', 'process': 'The student names four people who fit the employer. They read the whole application against the posting. Each requirement is marked met, partly met or not yet, with the line that shows it. The panel agrees on the odds, Reach, Possible or Strong, then lists what to change in the resume, the cover letter and the portfolio. It does not rewrite them. The student does, with the AI mentor&rsquo;s coaching, then runs the panel again.', 'outcome': 'In pilot this semester.', 'thumb': '/render/workshop-07-panel-read.png', 'tool': '/render/agent-workshop.html', 'tool_label': 'Open the workshop'},
    {'group': 'Agents students build inside Render', 'slug': 'interview-panel', 'name': 'Interview Panel', 'href': '/render/interview-panel.html', 'status': 'In pilot', 'blurb': 'The four people who read the application for that job now interview the student for it, coach every answer, and say what to fix in the portfolio first.', 'summary': 'The four people who read the application for that job now interview the student for it, coach every answer, and say what to fix in the portfolio first. A first interview is usually the first time a student says their answers out loud. The goal is practice against the real job, with coaching on each answer.', 'goal': 'A first interview is usually the first time a student says their answers out loud. The goal is practice against the real job, with coaching on each answer.', 'audience': 'Capstone students with an application ready for one specific job.', 'process': 'The interview is aligned to the job: a different job means a different panel and different questions. The panel asks one question at a time. Questions come from the posting&rsquo;s minimum qualifications, and one asks the student to walk through a portfolio piece. Coaching comes after the last answer, with the answers to practice and what to change in the portfolio before the real interview. The student takes both to the AI mentor.', 'outcome': 'In pilot this semester.', 'thumb': '/render/workshop-04-interview.png', 'tool': '/render/agent-workshop.html', 'tool_label': 'Open the workshop'},
    {'group': 'Job search agents on a schedule', 'slug': 'dma-jobs', 'name': 'Digital Media Jobs Feed', 'status': 'Built and running', 'blurb': 'Posts verified entry-level openings to the program Discord every day.', 'summary': 'Posts verified entry-level openings to the program Discord every day. Job boards show students what is popular, not what they can get. The goal is real openings a current student or recent graduate can land, delivered where students already are.', 'goal': 'Job boards show students what is popular, not what they can get. The goal is real openings a current student or recent graduate can land, delivered where students already are.', 'audience': 'Digital Media Arts students and recent graduates, most of them still enrolled and already working.', 'process': 'Runs daily. It checks a log so nothing posts twice, searches, then filters hard on level and pay realism: zero to one year of experience, internships and part-time work preferred, and a pay ceiling so a senior role with a junior title never gets through. Approved jobs post to the jobs channel by webhook.', 'outcome': 'Built and running daily. The filters were tightened after two posts aimed too high, and that correction is written into the rules.', 'thumb': '/discord/discord-cover.png', 'tool': '/discord/overview.html', 'tool_label': 'See the student community'},
    {'group': 'Job search agents on a schedule', 'slug': 'find-your-flow', 'name': 'Find Your Flow', 'status': 'Retired, having succeeded', 'blurb': 'One realistic career a day, each paired with a live opening and verified pay.', 'summary': 'One realistic career a day, each paired with a live opening and verified pay. Choosing a career as one giant list is overwhelming. The goal is one honest option at a time, small enough to look at.', 'goal': 'Choosing a career as one giant list is overwhelming. The goal is one honest option at a time, small enough to look at.', 'audience': 'One young person exploring careers.', 'process': 'Each morning the agent picks a career, verifies growth and median pay against the U.S. Bureau of Labor Statistics, finds a real local training path, confirms one live job on an employer&rsquo;s own careers page, and composes a short letter in a locked, phone-first template.', 'outcome': 'Retired, having succeeded. Twenty-seven letters went out, the reader chose a direction and enrolled, and the agent was switched off.', 'thumb': '/flow/flow_cover.jpg', 'tool': '/flow/overview.html', 'tool_label': 'Read the case study'},
    {'group': 'Job search agents on a schedule', 'name': 'Focus', 'status': 'Runs daily', 'href': '/focus/overview.html', 'thumb': '/focus/focus_cover.jpg', 'blurb': 'Finds fresh photo-gig leads and a marketing idea for a working photographer, published to a private board.'},
    {'group': 'Job search agents on a schedule', 'name': 'Soar', 'status': 'Runs weekly', 'href': '/soar/overview.html', 'thumb': '/soar/soar_cover.jpg', 'blurb': 'Rebuilds an aerospace dashboard for a college-bound engineer: news, launches, clubs, and a live internship watch.'},
    {'group': 'Job search agents on a schedule', 'name': 'Summer Work', 'status': 'Runs on a schedule', 'href': '/summerwork/overview.html', 'thumb': '/summerwork/summerwork_cover.jpg', 'blurb': 'Finds high-paying, flexible summer gig work, verified live on employers&rsquo; own sites.'},
    {'group': 'Professional development model', 'name': 'Cultivate', 'status': 'Refreshes on every visit', 'href': '/cultivate/overview.html', 'thumb': '/cultivate/cultivate_cover.jpg', 'blurb': 'A personal hub for professional development and a curated news feed. The first AI build, the experiment that started all of this.'},
  ],
  'status':'In pilot this semester in two sections of the capstone course, Design Self Promotion. The agent workshop is the newest part of the tool, added during the pilot. The job search agents in the second row run outside Render on a schedule: the same search pattern with the training wheels off. Cultivate is the model for the professional development side, the learning plan.',
 },
 {
  'slug': 'copamigo', 'name': 'CopaMigo', 'prd_href': '/copamigo/prd.html', 'canonical': '/copamigo/overview.html',
  'eyebrow': 'Student Success Tools &middot; Case study',
  'lead': 'Student-facing routing for campus services, so a student asking a question in their own words reaches the right office.',
  'summary': 'Every campus already offers more support than its students can find. The services exist; students just do not know which office handles their problem, or what it is called. <strong>A student describes the situation in plain language, in their own language, and CopaMigo routes them to the right service with a handoff card:</strong> the contact, the hours, and what to ask for. Its answers are written rather than retrieved, drawn from the questions students actually bring and shaped with the offices that handle them. Anonymous, no login.',
  'goal': 'Campus service information is organized the way the institution is organized, not the way a student asks. The goal is that a student describing a problem in their own words, in their own language, reaches the right human being with enough context to make the handoff work.',
  'audience': 'Students who do not know the name of the office they need, and the advising and support staff who currently absorb the routing work by hand.',
  'process': 'Fourteen service modules built on more than a hundred hand-verified college URLs, with a campus picker covering all ten district colleges. A student types or speaks the situation and gets an answer in the same language, plus a handoff card carrying contact details, opening hours and what to ask for. Routine questions are answered inline; everything else reaches a person faster. It is anonymous, with no login.',
  'thumb': '/copamigo/copamigo_cover.jpg?v=2',
  'projects': [],
  'status':'In pilot, embedded in the Digital Media Arts program&rsquo;s Discord, where students are testing it. Each service office confirms, corrects and adds answers in its own words through a staff intake form. Its curated questions and answers, plain-language routing, and more than one hundred verified service links work on their own and can also seed an enterprise platform.',
 },
 {
  'slug': 'adoption', 'name': 'Adoption and Enablement', 'no_prd': True, 'thumb': '/v3/assets/adoption-path.svg',
  'hero_alt': 'The Innovation Center&rsquo;s campus LMS adoption in three steps. Discover: scattered tools, including course websites, handouts, Word documents, a shared drive, a discussion board and an open-source system. Evaluate: five options, with the district platform chosen. Adopt: one platform, with a pilot first and nearly all faculty following.',
  'eyebrow': 'Adoption &middot; Case study',
  'lead': 'Getting people to actually use the thing, which is the part most technology work underestimates.',
  'summary': 'Building a tool is half the work. The other half is whether people use it, which makes adoption part of the job for anyone who leads projects or builds products. That has been true of every role behind this section: moving a campus onto one learning platform, turning four helpdesks into one, moving forty-five faculty online in weeks, and convening a campus AI community of practice. A half-day Prosci workshop on the ADKAR Model at the EDUCAUSE Annual Conference gave that experience a structure: awareness, desire, knowledge, ability and reinforcement, in that order. Applied to current projects, the model showed which step each one was waiting on.',
  'goal': 'The goal is that people actually use what gets introduced, and keep using it after the person who introduced it steps back.',
  'audience': 'Faculty, staff and administrators asked to change how they work, and the leaders sponsoring the change.',
  'process': 'Make the case for the change, earn the desire to take part, teach what people need to know, support them while they practice, and reinforce it until it holds. In practice: written requirements, a pilot with early adopters, results that recruit the rest, and ownership with the people doing the work.',
  'projects': [
    {'slug': 'community-of-practice', 'technology': ['Monthly meetings, with a group chat for the work in between.'], 'process_list': ['<strong>Authentic assessment.</strong> The first line of collaborative work: what still counts as evidence of learning in the age of generative AI.', '<strong>AI ethics.</strong> Testing, and input to the campus technology committee on its work on AI ethics.', '<strong>Emerging AI.</strong> Presenting new AI content to the college with the Center for Teaching, Learning and Engagement.', '<strong>District input.</strong> Advising the district AI Resource Center&rsquo;s steering committee from a practitioner&rsquo;s point of view.'], 'outcomes': 'Thirty members, meeting monthly, in its first term. It is the only practitioner community of practice in the district.</p>\n    <p>The group already gives input in three directions: to the campus technology committee on AI ethics, to the teaching and learning center on emerging AI content, and to the district AI Resource Center&rsquo;s steering committee.', 'status_line': 'Active. Founded this term, thirty members, meeting monthly.', 'name': 'AI Community of Practice', 'sub': 'Campus early adopters', 'status': 'Launched this term', 'thumb': '/v3/assets/cm-cop.svg', 'blurb': 'Adoption by example: thirty early adopters from faculty, staff and administration show colleagues what works. The only practitioner community of practice in the district, advising the campus and the district on AI.', 'goal': 'People across campus were already using AI, each on their own, with no place to compare notes. The goal is that good practice spreads by example. Colleagues who are unsure about AI get to watch practitioners work, which persuades in a way an argument or a policy does not.</p>\n    <p>The community exists so that the people furthest along are visible, connected to each other, and available to the rest of the college.', 'audience': 'Thirty early adopters from faculty, staff and administration. Every member already uses AI in teaching, student support or design, and each brings a different expertise.</p>\n    <p>The wider audience is everyone who draws on what the group learns: colleagues deciding whether and how to use AI, the campus technology committee, the Center for Teaching, Learning and Engagement, and the district AI Resource Center.', 'process': 'Michelle Blomberg founded the community through the Center for Teaching, Learning and Engagement and has led its meetings so far. Leadership is shared by design: there is no single chair, and roles are distributed across the members.</p>\n    <p>The group meets once a month and keeps working between meetings in a group chat. Members share out the AI work each of them is doing, so everyone knows who to go to in each area, and they help each other on projects. It is not a training program and not a governance body. It is practitioners working together, and passing what they learn to the people who need it.</p>\n    <p>Its current lines of work:', 'outcome': 'Launched this term.', 'no_prd': True},
    {'slug': 'emergency-online', 'hero_alt_own': 'An online course page in a learning management system: a side menu, a welcome video recorded by the instructor, and a first module with a video, an assignment, a discussion and a live session on Zoom.', 'name': 'Emergency Move to Online Teaching', 'sub': '45 faculty, one department', 'status': 'Completed', 'thumb': '/v3/assets/cm-online.svg', 'no_prd': True, 'blurb': 'A condensed training on the last day on campus, then one-on-one mentoring, moved 45 Art and Humanities faculty online in weeks. Most had never taught online.', 'goal': 'The college was going remote, and there was one day left on campus. Forty-five members of the Art and Humanities department had to move their courses online, and most of them had never taught online. The goal was that every one of them could teach their own course, online, right away.', 'audience': 'Forty-five Art and Humanities faculty, most of them new to online teaching, and the students in their courses.', 'process': 'A condensed version of the full online-teaching training, delivered in person on the last day anyone was on campus. There was no time for the complete program, so it covered the two things people needed first: how to make videos, and how to use Canvas.</p>\n    <p>Then came the part that made it work: individual mentoring. Faculty were supported one at a time to build their courses and get everything they needed done.', 'technology': ['Canvas, for the courses themselves.', 'Zoom, for live class sessions and for the mentoring.', 'Google Drive tools, for shared files and materials.'], 'outcomes': 'Forty-five faculty moved their courses fully online within weeks, with one-on-one coaching continuing after the move.', 'status_line': 'Completed.'},
    {'slug': 'helpdesk', 'outcomes': 'Faster, more consistent support, recognized with an OIT technology award.', 'status_line': 'Completed.', 'technology': ['One campus phone number with a phone tree.', 'A shared help email address in place of individual inboxes.', 'Helpdesk ticket software, introduced at the same time, routing each request by function.'], 'name': 'Single Point of Contact Helpdesk', 'sub': 'One phone number, one email', 'status': 'OIT technology award', 'thumb': '/v3/assets/cm-helpdesk.svg', 'blurb': 'Four separate places to ask for help became one, with requests routed to functions, not to individual people. Recognized with an OIT technology award.', 'goal': 'Help was split four ways, and people had to know which one to contact before they could ask: a student helpdesk in the Innovation Center with no single owner, where staff took turns answering; a staff helpdesk in IT; classroom and office technology support, run by the library; and campus police. Some requests went to one person. Learning management system questions came to a single inbox, and if that person was not checking email, the issue sat. The goal was one place to ask, and help that did not depend on any one person.', 'audience': 'Students, faculty and staff who needed help, and the teams who answered.', 'process': 'One phone number for the whole campus, with a phone tree to every place a person could get help. Email changed at the same time: addresses that had gone to individual people by name now went into helpdesk software, introduced alongside the new number, and were routed to functions, not to individuals. Learning management system questions went to all the LMS specialists, student issues to student support, staff issues to staff support. Earlier, at the University of Michigan College of Engineering, the same idea at smaller scale: helped roll out the Center for Professional Development&rsquo;s first ticket system, then developed the training and trained all staff on it.', 'outcome': 'Faster, more consistent support, recognized with an OIT technology award.', 'no_prd': True},
    {'slug': 'lms-adoption', 'outcomes': 'Other faculty joined once they saw it working in a colleague&rsquo;s course, and nearly every faculty member was eventually on it.', 'status_line': 'Completed.', 'technology': ['Blackboard, on the district&rsquo;s shared instance.', 'Replaced: individual course websites, an open-source learning management system, a discussion board application and a shared drive.', 'Evaluated and not chosen: another college&rsquo;s SharePoint-based system, Desire2Learn, Moodle, and a campus build on open source.'], 'name': 'Campus LMS Adoption', 'sub': 'Discover, evaluate, adopt', 'status': 'Nearly all faculty on one platform', 'thumb': '/v3/assets/adoption-path.svg', 'blurb': 'Five options weighed, one chosen, a pilot with early adopters, and nearly all faculty on one platform.', 'goal': 'Course materials lived everywhere: individual course websites, handouts and Word documents, an open-source learning management system, a discussion board application, and a shared drive. The campus Innovation Center built and ran the tools, with students working alongside its developers through the Teaching and Learning Co-op, an experiential learning program. The goal was one platform.', 'audience': 'Faculty across a campus of about 30,000 students, and the students in their courses.', 'process': 'A campus evaluation and request for proposals, run jointly by the Director of Instructional Technology and the Director of Training, and sponsored by the vice president of administrative services and the vice president of academic affairs. Five options were weighed: joining the district&rsquo;s existing Blackboard instance, joining another college&rsquo;s system built on SharePoint, Desire2Learn, Moodle, or building a campus system on open source. The district instance met the requirements within the budget and staff available, so the campus joined rather than built. A pilot with early adopters came first, supported by a single point of contact helpdesk, workshops, shared course design standards, and a fully online course, written and taught for the rollout, that prepared instructors to design and teach online.', 'outcome': 'Other faculty joined once they saw it working in a colleague&rsquo;s course, and nearly every faculty member was eventually on it.', 'no_prd': True},
  ],
  'status':'Ongoing. The next step is further Prosci training, to plan for adoption from the start of a project.',
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
        header = header.replace('<a class="site-name" href="/">', '<a class="site-name" href="/" aria-current="page">')
    elif current == 'about':
        header = header.replace('<a href="/about.html">About</a>', '<a href="/about.html" aria-current="page">About</a>', 1)
    if not PROMOTE:
        def back(x):
            return x.replace('href="/"', 'href="/v3/"').replace('href="/#', 'href="/v3/#').replace('href="/about.html"', 'href="/v3/about.html"')
        header, tail = back(header), back(tail)
    if main_class:
        header = header.replace('<main id="main">', f'<main id="main" class="{main_class}">')
    return HEAD.format(title=title, extra_head=extra_head) + '\n' + header + '\n' + body + '\n' + tail + '\n'


def plain(text):
    """Body copy carries no bold. Headings do the emphasis."""
    return re.sub(r'</?strong>', '', text)


def tool_tab(label):
    """The tab label for a link out to the thing itself. Short, like every other tab."""
    l = (label or '').lower()
    if 'worked example' in l:
        return 'Worked example'
    if 'case study' in l or 'community' in l:
        return 'Case study'
    return 'Live tool'


def tabs(sec, proj, current):
    """ONE tab row, at the top, plain text. Overview, the live thing if there is one, PRD.
    The PRD is linked from here and from nowhere else. No pill buttons, anywhere."""
    if sec.get('tabs_all'):
        # One hand-kept tab row shared by every page of the section, generated or not.
        here = proj['slug'] if proj else current
        out = f'  <nav class="tabs" aria-label="{sec["name"]} sections">'
        for label, href, key in sec['tabs_all']:
            cur = ' aria-current="page"' if key == (current if current == 'prd' else here) else ''
            out += f'<a class="tab" href="{href}"{cur}>{label}</a>'
        return out + '</nav>'
    base = f"/v3/{sec['slug']}/" + (f"{proj['slug']}/" if proj else '')
    src = proj if proj else sec
    items = [('Overview', (base + 'overview.html') if proj else base, 'overview')]
    if src.get('tool'):
        items.append((tool_tab(src.get('tool_label')), src['tool'], 'tool'))
    real = src.get('prd_href') or (sec.get('prd_href') if proj else None)
    if real:
        items.append(('PRD', real, 'prd'))   # the written PRD, never a generated summary
    elif not src.get('no_prd'):
        items.append(('PRD', base + 'prd.html', 'prd'))
    if len(items) < 2:
        return ''
    out = f'  <nav class="tabs" aria-label="{(proj or sec)["name"]} sections">'
    for label, href, key in items:
        cur = ' aria-current="page"' if key == current else ''
        out += f'<a class="tab" href="{href}"{cur}>{label}</a>'
    return out + '</nav>'


def cards(sec):
    """The row, or rows, of cards for a section's projects."""
    b, group = [], None
    for p in sec['projects']:
        if p is sec['projects'][0] or p.get('group') != group:
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
    return b


def section_page(sec):
    """SECTION PAGE. Same anatomy as every overview: title, eyebrow, tabs, lead, hero, then the sections."""
    if sec.get('goal'):
        return overview_page(sec)
    b = [f'  <h1>{sec["name"]}</h1>',
         f'  <p class="eyebrow">{sec["eyebrow"]}</p>',
         f'  <p class="lead-sub">{sec["lead"]}</p>']
    if sec.get('thumb'):
        b.append(f'  <div class="hero-media"><img src="{sec["thumb"]}" alt="{sec.get("hero_alt") or sec["name"]}"></div>')
    b += ['  <div class="prose">', f'    <p>{plain(sec["summary"])}</p>', '  </div>']
    b += cards(sec)
    b += ['  <div class="prose">', '    <h2>Status</h2>', f'    <p>{sec["status"]}</p>', '  </div>']
    return page(f'{sec["name"]}, Michelle Blomberg', '\n'.join(b))


def overview_page(sec, proj=None):
    """OVERVIEW. The standard format: title, eyebrow, tabs, lead, hero, Goal, Audience, Process, Status."""
    name = proj['name'] if proj else sec['name']
    lead = proj['blurb'] if proj else sec['lead']
    goal = proj['goal'] if proj else sec['goal']
    aud = proj['audience'] if proj else sec['audience']
    proc = proj['process'] if proj else sec['process']
    stat = (proj.get('outcome') or proj.get('outcomes') or proj.get('status', '')) if proj else sec['status']
    b = [f'  <h1>{name}</h1>',
         f'  <p class="eyebrow">{sec["eyebrow"]}</p>',
         tabs(sec, proj, 'overview'),
         f'  <p class="lead-sub">{lead}</p>']
    hero = (proj.get('thumb') if proj else None) or sec.get('thumb')
    if hero:
        b.append(f'  <div class="hero-media"><img src="{hero}" alt="{(sec.get("hero_alt") if not (proj and proj.get("thumb")) else None) or name}"></div>')
    b += ['  <div class="prose">',
         '    <h2>Goal</h2>', f'    <p>{goal}</p>']
    if not proj:
        b.append(f'    <p>{plain(sec["summary"])}</p>')
    src = proj if proj else sec
    b += ['    <h2>Audience</h2>', f'    <p>{aud}</p>',
         '    <h2>Process</h2>', f'    <p>{proc}</p>']
    if src.get('process_list'):
        b += ['    <ul class="stack">'] + [f'      <li>{t}</li>' for t in src['process_list']] + ['    </ul>']
    if src.get('technology'):
        b += ['    <h2>Technology</h2>', '    <ul class="stack">'] + [f'      <li>{t}</li>' for t in src['technology']] + ['    </ul>']
    if src.get('outcomes'):
        b += ['    <h2>Outcomes</h2>', f'    <p>{src["outcomes"]}</p>']
        stat = src.get('status_line') or stat
    b.append('  </div>')
    if not proj:
        b += cards(sec)
        if sec.get('case'):
            b += ['  <div class="prose">', sec['case'], '  </div>']
    b += ['  <div class="prose">', '    <h2>Status</h2>', f'    <p>{stat}</p>', '  </div>']
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
         '    <h2>1. Summary</h2>', f'    <p>{plain((proj or {}).get("summary") or sec["summary"])}</p>',
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
 ('studies', 'AI Strategy'),
 ('student', 'Student Success Tools'),
 ('course',  'Course Design Tools'),
 ('adopt',   'Adoption'),
 ('teach',   'Teaching'),
]

HOME_CARDS = [
 # cat, title, tool name, href, thumb, one sentence
 ('studies','Student Support Routing','CopaMigo','/copamigo/overview.html','/copamigo/copamigo_cover.jpg?v=2',
  'In pilot in the program&rsquo;s Discord. A multilingual AI triage tool that answers in the student&rsquo;s own language and routes the problem to the right human service, with answers supplied by the staff who do the work.'),
 ('studies','Student Journey Barriers Study','Ten-college usability study','/v3/studies/journey/','/airc-sss/cover.svg',
  'Synthetic-student agents walk the real student journey across ten Maricopa colleges to find where students hit barriers, ranked into prioritized AI pilots.'),
 ('studies','AI Intake Model','AI Opportunity Pipeline','/pipeline/overview.html','/pipeline/pipeline_cover.jpg',
  'Requirements and an early prototype for taking in AI requests, whether for a tool or an agentic workflow. It starts from the problem a department has, not from the technology. It has not yet taken a live request.'),
 ('studies','Gemini Access Study','Examples of what Gemini blocks for students under 18','/v3/studies/gemini/','/gemini-study/gemini-cover.png',
  'Twenty-seven course assignments run in an under-18 account and an 18-and-older account, to show a district exactly what younger students cannot do.'),
 ('student','Career Launch Tool','Render','/render/overview.html','/render/render_cover.jpg',
  'Training wheels for building agents: students build a career-launch environment by hand and graduate owning the agents. Includes the scheduled agents built on the same pattern.'),
 ('student','Student Support Routing','CopaMigo','/copamigo/overview.html','/copamigo/copamigo_cover.jpg?v=2',
  'In pilot in the program&rsquo;s Discord. A multilingual AI triage tool that answers in the student&rsquo;s own language and routes the problem to the right human service, with answers supplied by the staff who do the work.'),
 ('student','Curriculum Strategy','Program Design','/program-design/overview.html','/program-design/majors-chart.png',
  'How the Digital Media program is structured, from what industry asks for back to the courses.'),
 ('student','Program Redesign','Stackable Microcredentials','/microcredentials/overview.html','/microcredentials/stackables-cover.png',
  'Short credentials that stack toward the degree, so students leave each semester with something an employer recognizes.'),
 ('student','Program Recruitment Outreach','Rough Cut','/roughcut/overview.html','/roughcut/roughcut_cover.jpg',
  'Recruitment outreach for all four digital media programs, designed end to end with AI and aimed at the teachers and advisors who already have future students in their classrooms.'),
 ('student','Student Community','Digital Media Discord','/discord/overview.html','/discord/discord-cover.png',
  'A closed community where students already are, for critique, group work, and tutoring, with an AI agent that posts entry-level jobs daily.'),
 ('course','Course Review Tool','Dial Your Course','/course-dialer/overview.html','/course-dialer/cover.jpg',
  'Drop in a Canvas course and nineteen checks run against it, from seat hours to accessibility to AI resistance, then the fixes come back.'),
 ('course','Syllabus Compliance Check','Syllabus Checker','/syllabus-checker/overview.html','/syllabus-checker/cover.jpg',
  'A submit-and-check tool that verifies syllabi against MCCCD and program requirements, replies to faculty instantly, and logs every submission.'),
 ('course','Authentic Assessment Simulations','AI-resistant assessment','/authentic-assessment/','/authentic-assessment/authentic_cover.svg',
  'Replace the AI-cheatable exam with an authentic task the student performs and defends, including a built suite of graduate data-science simulations.'),
 ('course','AI-Assisted Course Design','Synthetic SMEs','/synthetic-smes/','/synthetic-smes/how-it-works.svg',
  'A panel of AI agents drafts a course against a fixed checklist of quality standards, and the faculty member who would teach it signs off before a student sees it.'),
 ('adopt','AI Community of Practice','Campus early adopters','/v3/adoption/community-of-practice/overview.html','/v3/assets/cm-cop.svg',
  'Adoption by example: thirty early adopters from faculty, staff and administration show colleagues what works. The only practitioner community of practice in the district, advising the campus and the district on AI.'),
 ('adopt','Student Journey Barriers Study','Ten-college usability study','/v3/studies/journey/','/airc-sss/cover.svg',
  'Synthetic-student agents walk the real student journey across ten Maricopa colleges to find where students hit barriers, ranked into prioritized AI pilots.'),
 ('adopt','Emergency Move to Online Teaching','45 faculty, one department','/v3/adoption/emergency-online/overview.html','/v3/assets/cm-online.svg',
  'A condensed training on the last day on campus, then one-on-one mentoring, moved 45 Art and Humanities faculty online in weeks. Most had never taught online.'),
 ('adopt','Single Point of Contact Helpdesk','One phone number, one email','/v3/adoption/helpdesk/overview.html','/v3/assets/cm-helpdesk.svg',
  'Four separate places to ask for help became one, with requests routed to functions, not to individual people. Recognized with an OIT technology award.'),
 ('adopt','Campus LMS Adoption','Discover, evaluate, adopt','/v3/adoption/lms-adoption/overview.html','/v3/assets/adoption-path.svg',
  'Five options weighed, one chosen, a pilot with early adopters, and nearly all faculty on one platform.'),
 ('teach','Student-Designed Publication','The Traveler','/traveler/overview.html','/fep/traveler_cover.jpg',
  'The college&rsquo;s award-winning student literary and visual arts publication. I advise the student design team through each production cycle.'),
 ('teach','Client-Work Design Studio','Design Studio','/studio/overview.html','/studio/studio-cover.jpg',
  'Real clients, real briefs, real deadlines. Students took live campus work and shipped it, from a 90-foot mural to motion and publications.'),
 ('teach','Work-Based Learning','Internship Program','/internship/overview.html','/canvas/internships_cover.jpg',
  'Placing and mentoring students in real work with local businesses and industry partners.'),
 ('teach','Online Capstone Course','Design Self Promotion, AVC 248','/learning-design/avc248.html','/canvas/avc248/avc248-canvas.jpg?v=2',
  'The capstone where students build a portfolio and run a real job search.'),
 ('teach','Course Redesign','Intro to Digital Arts, AVC 100','/avc100/overview.html','/avc100/skills-chart.png',
  'An introductory course rebuilt backward from measurable outcomes.'),
 ('teach','Curriculum and Course Design','UX Design for Interactive Media','/canvas/avc2xx/design.html','/canvas/avc2xx/ux_cover.jpg',
  'A new course designed from eleven industry competencies and authentically assessed.'),
 ('teach','Student-Taught Project','Design History, AVC 183','/canvas/design-history/overview.html','/canvas/design-history/design_history_cover.jpg',
  'Students research, design and teach a piece of design history to each other.'),
 ('teach','Brand System','Campus Cares Hub','/campus-cares/overview.html','/campus-cares/cares_cover.jpg',
  'A brand system for the campus basic-needs hub, designed with students.'),
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
    b = ['  <h1 class="lead-intro">I design learning experiences and AI strategy for the future of higher education.</h1>',
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
         '  <h2 class="work-head" id="work">Work</h2>',
         '  <nav class="tabs" id="worktabs" aria-label="Filter work by section">'
         + ''.join(f'<button type="button" class="tab" data-cat="{k}" aria-selected="{"true" if i == 0 else "false"}">{n}</button>' for i, (k, n) in enumerate(HOME_TABS))
         + '</nav>',
         '  <div class="feat" id="workgrid">']
    for cat, title, tool, href, thumb, desc in HOME_CARDS:
        b.append(home_card(cat, title, tool, href, thumb, desc))
    b.append('  </div>')
    b.append('  <script src="/v3/assets/workfilter.js?v=20261004e"></script>')
    return page('Michelle Blomberg', '\n'.join(b), script='/v3/assets/askbar.js?v=20261004e', current='home')


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
 {'out': 'studies/journey', 'src': 'airc-sss', 'eyebrow': 'AI Strategy &middot; Adoption &middot; Case study',
  'tabs': [('Overview', 'index.html'), ('Method', 'method.html'), ('Agents and ethics', 'agents.html'),
           ('Progress', 'progress.html'), ('What happens next', 'next.html')]},
 {'out': 'studies/gemini', 'src': 'gemini-study', 'eyebrow': 'AI Strategy &middot; Case study',
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
# TOP LEVEL. When PROMOTE is True every generated page is written at the site root, not under /v3/.
# Three sections share a name with a folder that already holds a live tool (its index.html is the tool
# itself, and that file is never overwritten or renamed). Their case study pages go in a /case/
# subfolder of that same folder. Everything else takes its own top-level folder.
# The page model above still spells addresses as /v3/...; top() rewrites them at write time, so
# flipping PROMOTE back to False puts everything back under /v3/ with no other change.
MOVE = {'studies': 'studies', 'adoption': 'adoption', 'dial': 'dial', 'build': 'build',
        'campground': 'campground', 'render': 'render/case', 'copamigo': 'copamigo/case',
        'traillog': 'traillog/case'}
ASSET_FILES = ('askbar.js', 'workfilter.js', 'mail.js', 'opendetail.js', 'adoption-path.svg',
               'cm-cop.svg', 'cm-ctle.svg', 'cm-helpdesk.svg', 'cm-online.svg')


def top(html):
    for k, v in MOVE.items():
        html = html.replace(f'/v3/{k}/', f'/{v}/')
    return html.replace('/v3/assets/', '/assets/')


def top_path(path):
    head, _, rest = path.partition('/')
    return MOVE[head] + '/' + rest


def stub(title, target):
    """What is left at an old /v3/ address: a page that sends the visitor on."""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="{target}">
<title>{title}</title>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<main id="main">
  <h1>This page has moved</h1>
  <p><a href="{target}">Go to the new address</a>.</p>
</main>
</body>
</html>
'''


def emit(path, html, written, mismatched):
    if PROMOTE:
        title = re.search(r'<title>(.*?)</title>', html, re.S).group(1).strip()
        if path in ('index.html', 'about.html'):
            target = '/' if path == 'index.html' else '/about.html'
        else:
            new = top_path(path)
            target = '/' + (new[:-len('index.html')] if new.endswith('/index.html') else new)
            _write(os.path.join(ROOT, new), top(html), '../' + new, written, mismatched)
        _write(os.path.join(OUT, path), stub(title, target), path, written, mismatched)
        return
    _write(os.path.join(OUT, path), html, path, written, mismatched)


def _write(full, html, path, written, mismatched):
    if CHECK:
        if not os.path.exists(full) or open(full, encoding='utf-8').read() != html:
            mismatched.append(path)
        return
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(html)
    written.append(path)


ROOT_META = '''<meta name="description" content="Michelle Blomberg designs learning experiences and AI strategy for the future of higher education.">
<meta property="og:type" content="website">
<meta property="og:title" content="Michelle Blomberg, learning experience design and AI in higher education">
<meta property="og:description" content="Michelle Blomberg designs learning experiences and AI strategy for the future of higher education.">
<meta property="og:url" content="https://michelleblomberg.com/">'''


def emit_root(name, html, written, mismatched):
    """The home page and About also live at the site root. Same page, indexable."""
    html = top(html).replace('<meta name="robots" content="noindex, nofollow">', ROOT_META if name == 'index.html' else '<meta name="description" content="About Michelle Blomberg.">')
    full = os.path.join(ROOT, name)
    if CHECK:
        if not os.path.exists(full) or open(full, encoding='utf-8').read() != html:
            mismatched.append('../' + name)
        return
    open(full, 'w', encoding='utf-8').write(html)
    written.append('../' + name)


def inject_cards(sec, written, mismatched):
    """Write the section's cards into its hand-written overview, between two marker comments."""
    full = os.path.join(ROOT, sec['canonical'].lstrip('/'))
    old = open(full, encoding='utf-8').read()
    a, b = '<!-- render-cards:start -->', '<!-- render-cards:end -->'
    if a not in old or not sec['projects']:
        return   # nothing to write: this overview carries no cards
    block = a + '\n' + top('\n'.join(cards(sec))) + '\n' + b
    new = re.sub(re.escape(a) + r'.*?' + re.escape(b), lambda m: block, old, flags=re.S)
    if CHECK:
        if new != old:
            mismatched.append('..' + sec['canonical'])
        return
    open(full, 'w', encoding='utf-8').write(new)
    written.append('..' + sec['canonical'])


def main():
    written, mismatched = [], []
    if PROMOTE and not CHECK:
        import shutil
        for f in ASSET_FILES:   # edit these in v3/assets/, the build copies them to /assets/
            if f.endswith('.js'):   # the chatbot's answers link to pages, so its addresses move too
                open(os.path.join(ROOT, 'assets', f), 'w', encoding='utf-8').write(top(open(os.path.join(OUT, 'assets', f), encoding='utf-8').read()))
            else:
                shutil.copyfile(os.path.join(OUT, 'assets', f), os.path.join(ROOT, 'assets', f))
    if PROMOTE:
        emit_root('index.html', home_page(), written, mismatched)
        emit_root('about.html', about_page(), written, mismatched)
    emit('index.html', home_page(), written, mismatched)
    emit('about.html', about_page(), written, mismatched)
    for s in SECTIONS:
        if s.get('canonical'):
            emit(f'{s["slug"]}/index.html', stub(s['name'] + ', Michelle Blomberg', s['canonical']), written, mismatched)
            inject_cards(s, written, mismatched)
        else:
            emit(f'{s["slug"]}/index.html', section_page(s), written, mismatched)
        gen = [p for p in s['projects'] if 'href' not in p]
        for p in s['projects']:   # a project whose page is hand-written: forward its old generated address
            if p.get('href') and p.get('slug'):
                emit(f'{s["slug"]}/{p["slug"]}/overview.html', stub(p['name'] + ', Michelle Blomberg', p['href']), written, mismatched)
        for p in gen:
            emit(f'{s["slug"]}/{p["slug"]}/overview.html', overview_page(s, p), written, mismatched)
            real = p.get('prd_href') or s.get('prd_href')
            if real:
                emit(f'{s["slug"]}/{p["slug"]}/prd.html', stub(p['name'] + ' PRD, Michelle Blomberg', real), written, mismatched)
            elif not p.get('no_prd'):
                emit(f'{s["slug"]}/{p["slug"]}/prd.html', prd_page(s, p), written, mismatched)
        if s.get('canonical'):
            emit(f'{s["slug"]}/overview.html', stub(s['name'] + ', Michelle Blomberg', s['canonical']), written, mismatched)
        elif s.get('goal') or not gen:
            emit(f'{s["slug"]}/overview.html', overview_page(s), written, mismatched)
            if s.get('prd_href'):
                emit(f'{s["slug"]}/prd.html', stub(s['name'] + ' PRD, Michelle Blomberg', s['prd_href']), written, mismatched)
            elif s.get('no_prd'):
                emit(f'{s["slug"]}/prd.html', stub(s['name'] + ', Michelle Blomberg', f'/v3/{s["slug"]}/'), written, mismatched)
            else:
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
