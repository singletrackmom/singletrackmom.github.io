import pathlib,re
import os
SRC=pathlib.Path(__file__).resolve().parent
OUT=pathlib.Path(os.environ.get('BB_OUT', SRC.parents[1]/'bergberg'))
TABS=[('index.html','Start'),('venues.html','Venues'),('planners.html','Planners'),('seo.html','SEO'),('blog.html','Blog'),('instagram.html','Instagram'),('calendar.html','Calendar'),('pricing.html','Pricing'),('competitors.html','Competitors'),('clients.html','Clients')]
DESC={'index.html':'The Berg Berg Photography marketing plan: what to do first, and why.',
'venues.html':'Venues to visit, albums and brochures to bring, and how to get on preferred vendor lists.',
'planners.html':'Wedding planners Berg Berg Photography has worked with, and how to stay on their lists.',
'seo.html':'How Google and AI search find wedding photographers, and a free checklist to fix the site.',
'blog.html':'How to write a wedding blog post step by step, with a six-month blog calendar.',
'instagram.html':'Whether to post on Instagram, how it works now, collab posts, and a 12-week posting calendar.',
'calendar.html':'Week by week: where to go, who to email and what to post, December through May.',
'competitors.html':'What other foothills and Denver wedding photographers charge, and what it means for your prices.',
'pricing.html':'Pricing ideas: a Kevin-only package, a budget option that doesn’t cheapen the rest, and AI for culling.',
'clients.html':'Answering inquiries, delivering galleries, asking for reviews and selling albums.'}
HEAD='''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<link rel="icon" href="/favicon.ico" sizes="any">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow,noarchive">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="bergberg.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bb-head">
  <div class="bb-bar">
    <p class="bb-name"><a href="index.html">Berg Berg Photography Marketing Plan</a></p>
    <p class="bb-back"><a href="/focus/index.html">&larr; Back to Focus</a></p>
  </div>
  <nav class="tabs" aria-label="Plan sections">
{tabs}
  </nav>
</header>
<main id="main">
'''
FOOT='''</main>
<footer class="toolfoot">
<a href="/focus/index.html">&larr; Back to Focus</a>
<div style="margin-top:.4rem">Updated November 2026</div>
</footer>
<script src="scripts.js"></script>
<script src="carry.js"></script>
<script src="weeks.js"></script>
<script src="bergberg.js"></script>
</body>
</html>
'''
for f,name in TABS:
    body=(SRC/f).read_text()
    tabs='\n'.join(f'    <a href="{g}"'+(' aria-current="page"' if g==f else '')+f'>{n}</a>' for g,n in TABS)
    title=('Berg Berg Photography Marketing Plan' if f=='index.html' else f'{name} &middot; Berg Berg Photography Marketing Plan')
    (OUT/f).write_text(HEAD.format(title=title,desc=DESC[f],tabs=tabs)+body+FOOT)
    print('built',f)
