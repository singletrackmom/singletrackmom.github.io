#!/usr/bin/env python3
"""
prd-requirements.py, writes the buildable parts of every PRD from one data file.

GOAL     Every PRD carries acceptance criteria, dependencies, an out-of-scope list and
         the questions still to settle, in the same place and the same format.
AUDIENCE Michelle, and every future Claude session.
PROCESS  Edit tools/prd-requirements.json, then run:  python3 tools/prd-requirements.py
         Each block is written between marker comments, so re-running replaces it.
         Never edit a block by hand inside a PRD: change the data file and re-run.
"""
import json, os, re, html, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = json.load(open(os.path.join(ROOT, 'tools', 'prd-requirements.json'), encoding='utf-8'))


def curl(s):
    s = s.replace('—', ', ').replace('–', ' to ')
    s = re.sub(r'"([^"]*)"', '“\\1”', s).replace("'", '’')
    return html.escape(s, quote=False)


def blocks(d):
    acc = ('<h3>Requirements and acceptance criteria</h3>\n'
           '<p>Each requirement is one behavior. The checks beside it are what a builder or tester confirms '
           'before that requirement is called done. Status reflects what this document records as built.</p>\n'
           '<table>\n<thead><tr><th>#</th><th>Area</th><th>Requirement</th><th>Done when</th><th>Status</th></tr></thead>\n<tbody>\n')
    for r in d['requirements']:
        acc += ('<tr><td>' + curl(r['id']) + '</td><td>' + curl(r['area']) + '</td><td>' + curl(r['requirement'])
                + '</td><td><ul>' + ''.join('<li>' + curl(x) + '</li>' for x in r['done_when']) + '</ul></td><td>'
                + curl(r['status'].replace('Unknown', 'Not recorded')) + '</td></tr>\n')
    acc += '</tbody>\n</table>\n'
    dep = ('<h3>Dependencies</h3>\n<p>What has to be in place, and who provides it.</p>\n<table>\n'
           '<thead><tr><th>Needed</th><th>Provided by</th><th>Needed for</th></tr></thead>\n<tbody>\n'
           + ''.join('<tr><td>' + curl(x['what']) + '</td><td>' + curl(x['owner']) + '</td><td>' + curl(x['needed_for']) + '</td></tr>\n'
                     for x in d['dependencies']) + '</tbody>\n</table>\n')
    oos = '<h3>Out of scope</h3>\n<ul>\n' + ''.join('<li>' + curl(x) + '</li>\n' for x in d['out_of_scope']) + '</ul>\n'
    q = ''
    if d.get('questions'):
        q = ('<h3>Questions to settle before the next build</h3>\n<ol>\n'
             + ''.join('<li>' + curl(x) + '</li>\n' for x in d['questions']) + '</ol>\n')
    return {'acc': acc, 'dep': dep, 'oos': oos, 'q': q}

# which numbered section each block closes
AFTER = {'acc': 'How it works', 'dep': 'Build and portability', 'oos': 'Rollout', 'q': 'Open questions and risks'}


def place(t, key, body, path):
    a, b = f'<!-- prd-req:{key} -->', f'<!-- /prd-req:{key} -->'
    block = a + '\n' + body + b + '\n\n'
    if a in t:
        return re.sub(re.escape(a) + r'.*?' + re.escape(b) + r'\n*', lambda m: block if body else '', t, flags=re.S)
    if not body:
        return t
    m = re.search(r'<h2[^>]*>\s*(?:\d+\.\s*)?' + re.escape(AFTER[key]) + r'\s*</h2>', t)
    if not m:
        sys.exit(f'{path}: no section called {AFTER[key]}')
    nxt = t.find('<h2', m.end())
    if nxt < 0:
        nxt = t.find('</main>', m.end())
    return t[:nxt] + block + t[nxt:]


for path, d in DATA.items():
    full = os.path.join(ROOT, path)
    t = open(full, encoding='utf-8').read()
    for key, body in blocks(d).items():
        t = place(t, key, body, path)
    open(full, 'w', encoding='utf-8').write(t)
    print('wrote', path, len(d['requirements']), 'requirements')
