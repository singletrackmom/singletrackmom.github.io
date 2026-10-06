/* askbar.js, the "Ask me about my work" widget on the v2 front page.

   GOAL     Answer the handful of questions a screener actually asks, on the
            page, without making them read six sections first.
   AUDIENCE Anyone landing on the front page cold.
   PROCESS  A keyword table maps a typed question to one of the prepared
            answers below. There is no model call and no network request:
            this is a matcher over written answers, not a chatbot.

   WHY THIS FILE EXISTS SEPARATELY
     v2/index.html was built by copying the v1 markup, and the markup came
     across while this script did not. The result was a hero widget that
     threw a ReferenceError on the first click, on a page whose headline is
     "I build AI tools." Caught in the v2 audit, 30 Aug 2026. Kept external
     so it can never be lost in a copy again.

   EDITING THE ANSWERS
     A is the answer bank, MATCH maps trigger words to a key in A. Every
     answer is public-facing prose, so the accuracy guardrails in CLAUDE.md
     apply to it exactly as they apply to a page.
*/
(function(){
    window.toggleAgent=function(){ var i=document.getElementById('abInput'); if(i){ i.scrollIntoView({behavior:'smooth',block:'center'}); setTimeout(function(){i.focus();},150); } };
    var A = {
      syntheticsme: "An experiment: can a panel of AI agents draft a rigorous graduate course in a field outside my own? An expert reviewer judged about 78 percent usable as built, so it is a starting point for a faculty member, never a replacement for one. <a href='/synthetic-smes/'>See the case study &rarr;</a>",
      sme: "A subject-matter expert, the person who owns the accuracy of the content. In my work an AI agent can stand in to speed up a first draft, but a named human expert confirms it before a student sees it. <a href='/synthetic-smes/skill.html'>How the skill works &rarr;</a>",
      syntheticstudent: "An AI agent given the profile of a typical incoming learner. It reads a draft the way that student would and flags where they would get lost, so a human knows what to check with real students. <a href='/synthetic-smes/skill.html'>See the agent panel &rarr;</a>",
      agents: "Three roles: a subject-matter expert, an instructional designer, and a synthetic student. They draft and critique each other&rsquo;s work, and a human directs them and owns the result. <a href='/synthetic-smes/skill.html'>Meet the panel &rarr;</a>",
      buildskill: "Yes, I write and maintain my own. A skill packages the standards so every build starts compliant, and in Gemini the equivalent is a Gem. <a href='/synthetic-smes/skill.html'>See the build skill &rarr;</a>",
      crossdiscipline: "Yes, that is why it is a skill and not a one-off. The standards travel, the expert agent is recast for the new field, and a human expert still reviews the result. <a href='/synthetic-smes/'>See the case study &rarr;</a>",
      dialer: "Drop in a Canvas course and nineteen checks run against it, from seat hours to accessibility to AI resistance. Approve the fixes and get a package back, ready to reimport. <a href='/course-dialer/overview.html'>See it &rarr;</a>",
      focus: "Closing the gap between what people are taught and what the work demands. I design learning experiences and AI tools that take friction off students and staff while keeping people at the center.",
      about: "I&rsquo;m a learning experience designer and AI strategist, grounded in learning science, with more than 20 years in higher education. <a href='/about.html'>Read more &rarr;</a>",
      background: "Graphic and web design, then UX, then product management at an EdTech startup, then seven years as Director of Instructional Technology, then faculty and Program Director in Digital Media. <a href='/about.html'>Read more &rarr;</a>",
      render: "A career-launch tool where students build their own agents by hand and leave owning them. It is a prototype now and goes into the capstone course in January. <a href='/render/overview.html'>See Render &rarr;</a>",
      district: "A usability study across all ten Maricopa colleges. Synthetic-student agents walk the real student journey to find where students hit barriers, ranked into AI pilots. <a href='/studies/journey/'>See the study &rarr;</a>",
      copamigo: "A multilingual tool that points a stuck student to the right office, with answers supplied by the staff who do the work. It is in pilot in one program. <a href='/copamigo/overview.html'>See CopaMigo &rarr;</a>",
      future: "When a model can produce the answer in seconds, what matters is the judgment around it: asking good questions, spotting when the AI is wrong, defending a decision. So the process becomes the evidence, the way design has always been taught.",
      teaching: "Backward design, competency over seat time, and authentic work students defend out loud. AI is a thinking partner, used with judgment.",
      philosophy: "What still counts as evidence of learning when a model can produce the artifact? I assess the process, the iteration and the decision a student can defend, not only the finished thing.",
      favorite: "Experiential learning: real clients, real projects. Students do the work for someone who needs it, and they rise to it. <a href='/studio/overview.html'>See the studio &rarr;</a>",
      tools: "Claude, in Cowork. What matters to me is the agentic setup: an AI that can act across my files and run on a schedule, with reusable skills so every build starts ahead.",
      mac: "A Mac, obviously. The machine matters far less than what you make with it. But it&rsquo;s a Mac.",
      proudest: "Students who nearly gave up, then finished and launched careers. More than any single project.",
      looking: "Yes, for roles in learning experience design or AI strategy and adoption in higher education. The best way to reach me is <a href='#' class='mailme'>email</a>.",
      mines: "I would love to work at Mines. Starting from a problem a department or a student has and getting it to something people use is the work I do now across a ten-college district, and I would like it to be my whole job.",
      cu: "Yes. Sitting down with an office, mapping how the work runs, and deciding whether AI helps is what I do now across a ten-college district, and I would like it to be my whole job, in Colorado.",
      location: "I&rsquo;m based in Colorado and teach online for Arizona&rsquo;s Maricopa district. I&rsquo;m open to online roles or roles in the Western US.",
      states: "The Western US outside Arizona, including Colorado, Utah and the Mountain West.",
      dreamjob: "A team that treats higher education as a design and research problem: turning emerging AI into pilots, measuring what improves learning, and keeping people at the center.",
      accessibility: "Accessibility is in the first draft, not a retrofit. I design to WCAG and caption every video. <a href='/course-dialer/overview.html'>See the tool that checks it &rarr;</a>",
      aiproof: "Make the assessment the professional task. The student does the work and defends the decisions out loud, which no model can hand back. <a href='/authentic-assessment/'>See the research &rarr;</a>",
      students: "Students build the real thing: real clients, real briefs, real deadlines. <a href='/studio/overview.html'>See the studio &rarr;</a>",
      lms: "I build in the LMS, not around it. Courses ship as clean Canvas packages with accessibility and outcome alignment already in the file. <a href='/avc100/overview.html'>See a rebuilt course &rarr;</a>",
      oer: "I design from open and licensed materials, which keeps the cost off students and the copyright clean.",
      data: "I measure what the course is for: outcomes, persistence, and whether a student comes back for the next class.",
      pilot: "Everything runs as a pilot before it runs as a policy. The success measure is set before the pilot starts.",
      faculty: "A tool nobody is trained to use quietly fails, so I plan the training alongside it. I also convened a campus AI community of practice. <a href='/adoption/'>Adoption work &rarr;</a>",
      privacy: "Students are told what is collected and why, and my tools collect only what they need to work. Privacy is settled before a pilot starts.",
      adults: "Most of my learners are working adults with jobs, children and fifteen honest minutes. I design for competency over seat time.",
      contact: "You can reach me at <a href=\'#\' class=\'mailme\'>michelleblomberg [at] gmail</a>.",
      lxd: "An instructional designer builds the course, a learning technologist runs the tools, and a learning experience designer starts from the learner and designs the whole experience. The titles overlap. My training is in both design and learning theory.",
      lifecycle: "Backward. Write measurable outcomes, decide what evidence proves them, design the activities, build with accessibility from the start, pilot, then measure against the same outcomes and revise.",
      backwarddesign: "Start at the end (Wiggins and McTighe): define the outcomes, decide what evidence proves them, then design the instruction. Every module has to trace back to an outcome.",
      scaffolding: "Break a hard skill into supported steps, then remove the support as the student gains competence. Model it, guide practice, hand off.",
      alignment: "Outcomes, assessments and activities all point at the same target (Biggs). Dial Your Course checks exactly that. <a href='/course-dialer/overview.html'>See it &rarr;</a>",
      strengths: "I&rsquo;m trained in both design and the science of how people learn, and I build what I design. I write the requirements first, test with real users, and plan the training alongside the tool.",
      programreview: "As Program Director I ran the program review every three years: enrollment, outcomes and course performance, written up as the case for budget and resources.",
      adkar: "Adoption decides whether anything gets used. I took Prosci&rsquo;s ADKAR workshop at the EDUCAUSE Annual Conference and use its five steps to see what a project is waiting on. <a href='/adoption/'>Adoption work &rarr;</a>",
      scrum: "The product owner role is familiar ground. As a product manager at an EdTech startup I owned the roadmap, wrote the requirements and set priorities with engineering.",
      usability: "I ran usability studies as a product manager, I teach UX design, and I designed two district studies. <a href='/studies/journey/'>Student journey &rarr;</a> <a href='/studies/gemini/'>Gemini access &rarr;</a>",
      stem: "Yes. At the University of Michigan College of Engineering I was Online Learning Coordinator and instructional designer, working daily with engineering faculty on courses for working engineers.",
      built: "Yes. As a product manager I took web-delivered educational software from requirements to release, and as a director I ran a campus&rsquo;s learning platforms for seven years. The AI work here is newer, and each piece is labeled prototype or pilot.",
      intake: "A front door for AI requests: what does the office need, does something already exist, and is it a training, process or tool problem. It is in development with my district domain. <a href='/pipeline/overview.html'>See it &rarr;</a>",
      whatnot: "Start with the people and the problem, check whether a tool already exists, and write the requirements before anything gets made. Often the answer is training, not a tool.",
      value: "Set the baseline and the success measure before the pilot starts. A pilot is a test with an end date, not a destination.",
      governance: "Privacy, security and accessibility are reviewed before a pilot starts, and anything an AI drafts gets a named person&rsquo;s sign-off before it reaches a student.",
      product: "Yes. As Product Manager for higher education at ProQuest&rsquo;s XanEdu division I wrote the requirements engineers built from, ran usability studies and set the roadmap. <a href='/cultivate/cv.html'>Full CV &rarr;</a>",
      designstudio: "I started as a graphic designer at Q LTD in Ann Arbor, working on large web projects alongside the authors of <em>Information Architecture for the World Wide Web</em>. <a href='/cultivate/cv.html'>Full CV &rarr;</a>",
      director: "For seven years I was Director of Instructional Technology for a campus Innovation Center, leading the platforms and a team that included three developers. I also co-led the district LMS committee. <a href='/cultivate/cv.html'>Full CV &rarr;</a>",
      servicedesk: "Yes. I set up a single point of contact helpdesk that won an OIT technology award, and wrote ITIL service agreements. <a href='/cultivate/cv.html'>Full CV &rarr;</a>",
      vendor: "I ran a campus LMS evaluation and RFP and contributed to the district RFP that led to Canvas. As a product manager I sat on the vendor side too.",
      stakeholders: "A large part of my work is translating between technical and non-technical people: faculty, deans and district leadership. I sit on the steering committee of the district AI Resource Center.",
      technical: "I build with AI every day: prompts, agents, skills, scheduled agents, and front ends in HTML, CSS and JavaScript. I find the problem, prototype it and write the requirements, alongside the engineers who take it to production.",
      education: "A Master of Education in Educational Technology from Northern Arizona University, with an emphasis on adult online learning. My research was on connectivism and personal learning environments.",
      training: "The League for Innovation AI Fellows program, an EDUCAUSE microcredential in AI for instructional design, Google&rsquo;s Generative AI Leader training, and Anthropic Academy courses. <a href='/cultivate/cv.html'>Full CV &rarr;</a>",
      awards: "The Gaucho Globe Award for open educational resources, two One Maricopa Awards, and an OIT technology award. The student publication I advise has won national design awards. <a href='/cultivate/cv.html'>Full CV &rarr;</a>",
      mantra: "Done is better than perfect. And less is more.",
      whitespace: "Horror vacui is the fear of empty space, the urge to fill every corner of a page. I teach students to resist it. White space is doing work, and less is more.",
      fallback: "Try asking about CopaMigo, Render, the district study, AI intake, how I decide what not to build, adoption, or my background. Everything else is in <a href='/cultivate/cv.html'>my CV &rarr;</a>"
    };
    var MATCH = [
      ['mantra',['mantra','motto','tell your students','tell my students','tell students','your saying','catchphrase','done is better','less is more']],
      ['whitespace',['horror vacui','horror vacuii','white space','whitespace','empty space','negative space']],
      ['mines',['school of mines',' mines','orediggers']],
      ['cu',['anschutz','university of colorado',' cu ',' cu?',' cu.',' cu,','cu denver','cu boulder']],
      ['adkar',['adkar','prosci','change management','change-management','adoption','resistance','rollout','roll out']],
      ['scrum',['scrum','agile','product owner','pspo','backlog','sprint']],
      ['stem',['stem','engineer','six sigma','michigan','hyflex','scientist','technical audience']],
      ['usability',['usability','user research','user testing','ux research','user experience','ux']],
      ['intake',['intake','pipeline','prioriti','front door','requests','opportunity']],
      ['product',['product manag','requirements','requirement','roadmap','xanedu','proquest','startup','prd','spec','managed a product','real product']],
      ['designstudio',['design studio','q ltd','information architecture','o\'reilly','oreilly','polar bear','graphic design','agency','ia ']],
      ['servicedesk',['itil','help desk','helpdesk','service desk','ticket','teamdynamix','incident','service management']],
      ['vendor',['vendor','rfp','procure','purchas','buy or build','build or buy','buy vs','evaluate a tool','evaluation']],
      ['director',['director','innovation center','managed a team','manage people','supervis','led a team','leadership','developers']],
      ['stakeholders',['stakeholder','executive','non-technical','nontechnical','present','communicat','deans','leadership team']],
      ['technical',['technical','code','coding','program','api','agent evaluation','evals','llm','prompt','build agents','developer']],
      ['education',['degree','master','bachelor','education','college did','graduate school','nau','school did']],
      ['training',['certif','training','credential','courses have you','professional development','pmp']],
      ['awards',['award','recognition','honor']],
      ['whatnot',['decide what','not to build','discovery']],
      ['built',['production','shipped','real tool','launched','tool design','ever built','built anything','only prototypes']],
      ['value',['value','roi','metric','measure success','kpi','baseline']],
      ['governance',['governance','responsible','ethic','policy','risk']],
      ['programreview',['program review','program assessment','academic program review','assess the program','program-level assessment','program level assessment','justify budget','resource allocation','program health','justify spending','as director']],
      ['strengths',['set you apart','sets you apart','sets your work apart','stand out','your strengths','what do you bring','what makes you a','what makes a great learning','what makes a strong','great learning experience designer','differentiator','best fit for']],
      ['lxd',['learning experience design','learning experience designer','lxd','instructional designer','instructional design','learning technologist','oled']],
      ['lifecycle',['lifecycle','life cycle','course design process','design process','how do you design a course','course development','start to finish','addie']],
      ['backwarddesign',['backward design','backwards design','wiggins','mctighe','understanding by design','start with the end','begin with the end']],
      ['scaffolding',['scaffold','scaffolding','vygotsky','zone of proximal','gradual release']],
      ['alignment',['constructive alignment','biggs','aligned to outcomes','align the course','align a course','outcome alignment']],
      ['syntheticstudent',['synthetic student','synthetic learner','simulated student','student agent','synthetic-student']],
      ['syntheticsme',['synthetic sme','synthetic smes','synthetic-sme','simulated sme','sme project','synthetic subject','synthetic expert']],
      ['agents',['ai agents','agent panel','the agents','which agents','what agents','how many agents','synthetic agents','panel of agents','synthetic professor','synthetic professors','synthetic faculty']],
      ['sme',['subject-matter expert','subject matter expert','what is a sme','what is an sme','whats a sme','define sme','sme mean','sme stand']],
      ['buildskill',['write skill','writing skill','write a skill','write your own skill','claude skill','what is a skill','whats a skill','build a skill','reusable skill','how do skills','create a skill']],
      ['crossdiscipline',['other discipline','across discipline','other subject','another subject','different subject','different field','other field','another field','beyond data science','across subjects','another discipline','other disciplines']],
      ['dialer',['dial your course','dialer','course dialer','nineteen check','19 check','audit a course','audit a canvas','course audit']],
      ['accessibility',['accessib','wcag','ada','screen reader','caption','508','disab']],
      ['aiproof',['cheat','chatgpt do it','ai can do','ai proof','ai-resistant','ai resistant','authentic assessment','can a model','academic integrity']],
      ['students',['students build','student work','real client','real project','experiential','studio','portfolio work']],
      ['lms',['lms','canvas','blackboard','imscc','course build','build the course','course shell']],
      ['oer',['oer','open education','textbook','copyright','licens','zero cost','free textbook']],
      ['data',['analytics','data','metric','kpi','measure','evidence','retention','persistence','outcomes data']],
      ['pilot',['pilot','scale','roll out','rollout','test it','efficacy','prove']],
      ['faculty',['faculty','train','professional development','change management','adoption','stakeholder','buy-in','buy in']],
      ['privacy',['privacy','pii','ferpa','student data','ethic','governance','security']],
      ['adults',['adult learn','working adult','andrago','competency','cbe','competency-based']],
      ['proudest',['proud','accomplishment','achievement','best work','most proud']],
      ['tools',['favorite ai tool','favorite tool','favorite ai','ai tool','ai tools','which ai','what ai do you use','tools you use','what tools','favorite app','favorite model','claude','cowork','opus']],
      ['favorite',['favorite','favourite','love about','best part','enjoy','like most']],
      ['philosophy',['mcluhan','mcluan','mccluhan','medium is the message','the medium','philosophy','your take','worldview','what do you believe']],
      ['focus',['focus','what do you do','your work','mission','centered on']],
      ['render',['render','ple','personal learning','career','capstone','learning plan']],
      ['district',['district','sss','maricopa','barrier','journey','colleges','league','fellows','student success','study']],
      ['copamigo',['copamigo','copa','routing','triage','support bot']],
      ['future',['future','agentic','coming','next','trend','vision','2026','going','online learning']],
      ['teaching',['teach','teaching','assess','assessment','pedagog','classroom','course']],
      ['background',['background','experience','career','resume','cv','history','worked']],
      ['about',['who','yourself','about you','your story','tell me about you']],
      ['contact',['contact','email','reach','connect','linkedin','get in touch']],
    ];
    function labelFor(k){ return ({product:'Have you managed a real product?',designstudio:'Design studio background?',director:'Have you led a technology team?',servicedesk:'ITIL and service desk experience?',vendor:'Vendor evaluation and RFPs?',stakeholders:'Working with leadership?',technical:'How technical are you?',education:'Your degrees?',training:'Recent training?',awards:'Awards?',adkar:'Do you use ADKAR?',scrum:'Do you know Scrum?',stem:'Have you worked with a STEM audience?',usability:'How do you run usability research?',intake:'How do you handle AI intake?',whatnot:'How do you decide what not to build?',built:'Have you shipped real tools?',value:'How do you measure value?',governance:'Governance and responsible use?',strengths:'What sets your work apart?',programreview:'Program-level assessment?',lxd:'ID vs LXD vs technologist?',lifecycle:'Lifecycle of a course?',backwarddesign:'What is backward design?',scaffolding:'What is scaffolding?',alignment:'How do you align a course?',syntheticsme:'What are Synthetic SMEs?',sme:'What is a SME?',syntheticstudent:'What is a synthetic student?',agents:'The AI agent panel',buildskill:'Do you write your own skills?',crossdiscipline:'Would it work in other disciplines?',dialer:'What is Dial Your Course?',accessibility:'How do you handle accessibility?',aiproof:'Assessment a model cannot complete?',students:'Students building real projects?',lms:'Do you build in the LMS?',oer:'OER and copyright?',data:'How do you measure it?',pilot:'How do you pilot and scale?',faculty:'How do you get faculty on board?',privacy:'Student data and ethics?',adults:'Designing for adult learners?',focus:'Focus of your work',about:'Who are you?',background:'Your background',render:'Tell me about Render',district:'The district AI study',copamigo:'What is CopaMigo?',future:'The future of learning',teaching:'Your teaching approach',philosophy:'Your philosophy',favorite:'Favorite part of the job',tools:'Your favorite AI tool',proudest:'Proudest work',looking:'Open to new roles?',location:'Where are you based?',states:'States open to',dreamjob:'Your dream job',contact:'How do I reach you?',mac:'Mac or PC?',mantra:'Your mantra?',whitespace:'Horror vacui?'})[k]||k; }
    function add(cls, html){ var l=document.getElementById('abLog'); var d=document.createElement('div'); d.className='ab-msg '+cls; d.innerHTML=html; l.appendChild(d); l.scrollTop=l.scrollHeight; }
    window.abAsk=function(key, text){ document.getElementById('abLog').innerHTML=''; add('ab-user', text || labelFor(key)); setTimeout(function(){ add('ab-bot', A[key]||A.fallback); }, 200); };
    window.abSubmit=function(e){ e.preventDefault(); var i=document.getElementById('abInput'); var t=(i.value||'').toLowerCase().trim(); if(!t) return false; t=' '+t+' '; document.getElementById('abLog').innerHTML=''; add('ab-user', i.value); i.value=''; var key='fallback'; outer: for(var m=0;m<MATCH.length;m++){ for(var w=0;w<MATCH[m][1].length;w++){ if(t.indexOf(MATCH[m][1][w])>-1){ key=MATCH[m][0]; break outer; } } } setTimeout(function(){ add('ab-bot', A[key]); }, 200); return false; };
  })();
