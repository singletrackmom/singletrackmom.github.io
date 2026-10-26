#!/usr/bin/env python3
"""One Canvas packager for every course: canvas/<course>/course.html in, a Canvas .imscc out.

Reads the page that tools/course-build/build.py produces (details.lesson modules, div.el graded
items with data-* attributes, rubrics, objectives, instructor notes) and writes one Common Cartridge
with modules, pages, assignments, discussions, rubrics, weighted groups and term dates.

What comes from where:
  - course list and course code: build.py COURSES (imported, never edited here)
  - term calendars (start, closures, finals) and per-course extras: TERMS and EXTRA below
  - everything else: the course page itself

Per-course hooks in EXTRA (all optional):
  term           default term key ('fall2027', 'spring2027'); --term overrides
  file           output file name to keep (so existing links do not break)
  variant        text added to the Canvas course title, e.g. 'storyteller'
  red            True puts GCC red #CB3338 on title boxes; default is purple #7a5080 (public builds)
  groups         [(name, weight), ...]; aliases maps page group names onto them
  merge_into_ai  Module 0 sections (div ids) appended to the AI in This Course page
  ai_append      static fragment files appended to the AI in This Course page
  site_pages     [(page title, html file)] site pages added to Module 0 as Canvas pages
  m0_docs        (subheader, [(page title, fragment file)]) extra Module 0 pages under a subheader
  note_inserts   {module: (fragment file, regex in fragment, text in note to replace)}
  private_terms  words allowed only on Instructor Notes pages (an answer key, for example)
  cycles         {item id: 'mid'|'wknd'|'final'} for items whose markup has no data-cycle yet

Usage (from the repo root):
  python3 tools/course-build/package.py avc150                    build canvas/avc150/<file>.imscc
  python3 tools/course-build/package.py avc150 --term spring2027  same course, another term
  python3 tools/course-build/package.py --all                     every course on the shared build
  python3 tools/course-build/package.py avc150 --out drafts/x     write to a scratch folder instead
  python3 tools/course-build/package.py --check path/to/file.imscc [course]   validate a package

Never hand-edit a package; edit the course page and rebuild. Every item is imported unpublished.
"""
import os, re, sys, html, hashlib, zipfile, importlib.util, datetime as dt, xml.dom.minidom
from bs4 import BeautifulSoup, Comment

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CANVAS = os.path.join(ROOT, 'canvas')

sys.dont_write_bytecode = True   # importing build.py must not leave a __pycache__ in the repo
_spec = importlib.util.spec_from_file_location('course_build', os.path.join(HERE, 'build.py'))
_build = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_build)
COURSES = _build.COURSES

PURPLE, RED = '#7a5080', '#CB3338'
TINT = {PURPLE: '#f7f4f8', RED: '#fbeff0'}

D = dt.date
# Terms. Week n starts on a Saturday: start + 7(n-1), plus one week for each break week before it.
# Default deadlines: mid = Thursday of the week (post Wednesday, close Friday);
# wknd = the Sunday after (post Saturday, close Monday); final = finals due date.
# A due date or hard close on a closure moves to the next open day; moves over one day are flagged.
TERMS = {
    'spring2027': dict(
        label='Spring 2027', file='Spring2027', start=D(2027, 1, 16),
        break_weeks=[9],                      # spring break 15 to 21 Mar: Week 9 starts after it
        closures={D(2027, 1, 18): 'Martin Luther King Jr. Day', D(2027, 2, 15): 'Presidents Day',
                  **{D(2027, 3, d): 'spring break' for d in range(15, 22)}},
        final_due=D(2027, 5, 13),             # Thursday of finals week (Michelle, 25 Oct 2026); finals 10 to 14 May
        conclude=D(2027, 5, 15)),
    'fall2027': dict(
        label='Fall 2027', file='Fall2027', start=D(2027, 8, 21),
        break_weeks=[14],                     # Thanksgiving week: Week 14 starts after it
        # [verify] Fall 2027 closures against the published 2027 to 2028 GCC calendar
        closures={D(2027, 9, 6): 'Labor Day', D(2027, 11, 11): 'Veterans Day',
                  **{D(2027, 11, d): 'Thanksgiving break' for d in range(25, 29)}},
        final_due=D(2027, 12, 16),            # Thursday of finals week (Michelle, 25 Oct 2026); [verify] Fall 2027 calendar
        conclude=D(2027, 12, 18)),
}

DEFAULT_GROUPS = [('Process Work', 40.0), ('Projects', 35.0), ('Exercises', 25.0)]

_S150 = 'drafts/avc150-build/static/'
EXTRA = {
    'avc100': dict(term='spring2027'),   # AVC100 runs spring, summer and fall; builds are dated Spring 2027 (CLAUDE.md, 24 Oct 2026)
    'avc150': dict(
        term='fall2027', file='AVC150_Fall2027_DRAFT.imscc', variant='storyteller',
        merge_into_ai=['consent'], ai_append=[_S150 + 'withdraw.frag'],
        site_pages=[('The Teller and Tools', 'canvas/avc150/forms.html')],
        m0_docs=('Consent documents', [
            ('The One-Minute AI Explanation', _S150 + 'the-one-minute-ai-explanation.frag'),
            ('Project Information Sheet', _S150 + 'project-information-sheet.frag'),
            ('Consent Affirmation', _S150 + 'consent-affirmation.frag'),
            ('Video Consent Script', _S150 + 'video-consent-script.frag'),
            ('Signed Agreement', _S150 + 'signed-agreement.frag')]),
        note_inserts={1: (_S150 + 'instructor-notes-module-2.frag', r'<li>Planted problems \(instructor key\).*?</li>',
                          '<li>The planted-problems answer key is kept only on the unpublished Instructor Notes: Module 1 page in Canvas.</li>')},
        private_terms=['Glenn Dale']),
    'avc183': dict(term='spring2027', file='AVC183_Spring2027.imscc'),
    'avc190': dict(term='fall2027', file='AVC190_Fall2027_DRAFT.imscc',
                   groups=[('Process Work', 40.0), ('Projects', 35.0), ('Exercises, Quizzes and Reflections', 25.0)],
                   aliases={'Exercises': 'Exercises, Quizzes and Reflections'}),
    'avc248': dict(term='spring2027', file='AVC248_Spring2027_DRAFT.imscc'),
    'avc283': dict(term='fall2027', file='AVC283_Fall2027_DRAFT.imscc'),
    'avc2xx': dict(
        term='fall2027', file='AVC2XX_Fall2027_DRAFT.imscc',
        groups=[('Process Work', 40.0), ('Projects', 35.0), ('Exercises, Quizzes and Reflections', 25.0)],
        aliases={'Exercises': 'Exercises, Quizzes and Reflections'},),
}

TH = 'border:1px solid #999999;padding:6px 8px;text-align:left;background-color:#f2f2f2;'
TD = 'border:1px solid #999999;padding:6px 8px;vertical-align:top;'
NS = 'xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd"'


def asc(s):
    return ''.join(c if ord(c) < 128 else '&#%d;' % ord(c) for c in s)


def esc(s):
    return asc(html.escape(s, quote=False))


def slug(s):
    s = re.sub(r'[‘’“”]', '', html.unescape(s).lower())
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:70]


def fmt(d):
    return d.strftime('%A %-d %B')


def iso(d):
    return d.isoformat() + 'T19:00:00'   # noon Arizona time


def canvasify(frag):
    s = BeautifulSoup(frag, 'html.parser')
    for c in s.find_all(string=lambda t: isinstance(t, Comment)):
        c.extract()
    for t in s.find_all(class_='vh'):
        t.decompose()
    for d in s.find_all('div', class_='tw'):
        d.unwrap()
    for tb in s.find_all('table'):
        tb.attrs = {'style': 'border-collapse:collapse;width:100%;margin:0 0 16px;'}
    for th in s.find_all('th'):
        th.attrs = {k: v for k, v in th.attrs.items() if k == 'scope'}; th['style'] = TH
    for td in s.find_all('td'):
        td['style'] = TD
    for tag in s.find_all(True):
        for a in list(tag.attrs):
            if a in ('class', 'id') or a.startswith('data-'):
                if not (tag.name == 'a' and a == 'id'):
                    del tag[a]
    for a in s.find_all('a'):
        if a.get('href', '').startswith('#'):
            a.unwrap()
    return str(s)


def h2_to_h3(x):
    return re.sub(r'<(/?)h2>', r'<\1h3>', x)


def inner(t):
    return ''.join(str(c) for c in t.children)


def read(p):
    return open(os.path.join(ROOT, p), encoding='utf-8').read()


def frag_body(p, color):
    t = read(p)
    m = re.search(r'<body>\n?(.*)\n?</body>', t, re.S)
    t = m.group(1) if m else t
    if not t.lstrip().startswith('<'):
        t = '<' + t.lstrip()          # repairs a fragment saved without its first "<"
    return t.replace(PURPLE, color)


class Course:
    def __init__(self, c, term_key=None):
        if c not in COURSES:
            raise SystemExit('%s: not in build.py COURSES' % c)
        self.c, self.x = c, EXTRA.get(c, {})
        tk = term_key or self.x.get('term')
        if not tk:
            raise SystemExit('%s: no term set; pass --term spring2027 or --term fall2027' % c)
        self.term = TERMS[tk]
        self.color = RED if self.x.get('red') else PURPLE
        self.groups = self.x.get('groups', DEFAULT_GROUPS)
        self.aliases = self.x.get('aliases', {})
        self.files, self.resources, self.modules, self.rubrics, self.items = {}, [], [], [], []
        self.warn = []
        code = COURSES[c]['code'].upper()
        if term_key and term_key != self.x.get('term'):
            self.fname = '%s_%s_DRAFT.imscc' % (code, self.term['file'])
        else:
            self.fname = self.x.get('file') or '%s_%s_DRAFT.imscc' % (code, self.term['file'])

    # ---------- ids, boxes, dates
    def gid(self, *k):
        return 'g' + hashlib.md5((self.c + '|' + '|'.join(k)).encode()).hexdigest()

    def title_box(self, t):
        return ('<div style="background-color:%s;color:#ffffff;padding:16px 20px;margin:0 0 20px;">'
                '<h2 style="margin:0;color:#ffffff;">%s</h2></div>') % (self.color, t)

    def week_start(self, n):
        extra = sum(1 for b in self.term['break_weeks'] if n >= b)
        return self.term['start'] + dt.timedelta(days=7 * (n - 1 + extra))

    def open_day(self, d):
        while d in self.term['closures']:
            d += dt.timedelta(days=1)
        return d

    def dates(self, did, week, cycle):
        if cycle == 'final':
            due = self.term['final_due']
        else:
            ws = self.week_start(week)
            due = ws + dt.timedelta(days=5 if cycle == 'mid' else 8)
        post = due - dt.timedelta(days=1)
        note = 'Finals week.' if cycle == 'final' else ''
        cl = self.term['closures']
        if due in cl:
            nd = self.open_day(due)
            note = '%s is %s, a college closure, so this deadline moves to %s at noon.' % (due.strftime('%A'), cl[due], nd.strftime('%A'))
            if (nd - due).days > 1:
                self.warn.append('%s: due date %s falls in %s; moved %d days to %s. Decide.' % (did, due, cl[due], (nd - due).days, nd))
            due = nd
        close = due + dt.timedelta(days=1)
        if close in cl:
            nc = self.open_day(close)
            note = '%s is %s, a college closure, so the hard close moves to %s at noon.' % (close.strftime('%A'), cl[close], nc.strftime('%A'))
            if (nc - close).days > 1:
                self.warn.append('%s: hard close %s falls in %s; moved %d days to %s. Decide.' % (did, close, cl[close], (nc - close).days, nc))
            close = nc
        if post in cl:
            self.warn.append('%s: Discord post day %s is %s.' % (did, post, cl[post]))
        return post, due, close, note

    def deadline_box(self, kind, discord, post, due, close, note):
        li = []
        if discord == 'pre':
            li.append('Discord post: %s at noon, with three critique comments by the due time' % fmt(post))
        elif kind == 'discussion':
            li.append('Post: %s at noon' % fmt(post))
        elif discord in ('none', 'no'):
            li.append('No Discord post; submit in Canvas only')
        li.append('%s: %s at noon' % ('Due (post and three comments)' if kind == 'discussion' else 'Due in Canvas', fmt(due)))
        li.append('Hard close: %s at noon. Work submitted after the due time and before the hard close loses 10%%; nothing is accepted after the hard close.' % fmt(close))
        b = ('<h3>Deadline</h3><div style="background-color:%s;border:2px solid %s;padding:10px 14px;margin:0 0 16px;">'
             '<p style="margin:0 0 4px;"><strong>All times Arizona time.</strong></p><ul style="margin:0;">') % (TINT[self.color], self.color)
        b += ''.join('<li>%s</li>' % x for x in li) + '</ul>'
        if note:
            b += '<p style="margin:6px 0 0;">%s</p>' % note
        return b + '</div>'

    # ---------- resources
    def page_html(self, title, body, ident):
        return ('<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n<title>%s</title>\n'
                '<meta name="identifier" content="%s"/>\n<meta name="editing_roles" content="teachers"/>\n'
                '<meta name="workflow_state" content="unpublished"/>\n</head>\n<body>\n%s\n</body>\n</html>\n') % (esc(title), ident, asc(body))

    def add_page(self, title, body):
        ident = self.gid('page', title)
        path = 'wiki_content/%s.html' % slug(title)
        if path in self.files:
            raise SystemExit('%s: two pages named %r' % (self.c, title))
        self.files[path] = self.page_html(title, body, ident)
        self.resources.append((ident, 'webcontent', path, [path], []))
        return (self.gid('mi', title), 'WikiPage', title, ident)

    def group(self, g):
        g = self.aliases.get(g, g)
        if g not in dict(self.groups):
            self.warn.append('unknown grading group %r' % g)
        return g

    # ---------- reading items
    def item_info(self, e, week):
        """Return a dict for a graded div.el, or None for an ungraded one."""
        if e.get('data-id'):
            ih = e.find('p', class_='ih')
            return dict(did=e['data-id'], kind=e.get('data-type', 'assignment'), pts=int(e['data-pts']),
                        grp=self.group(e['data-group']), week=int(e.get('data-week') or week),
                        cycle=e.get('data-cycle') or self.x.get('cycles', {}).get(e['data-id']) or self.no_cycle(e['data-id'], week),
                        discord=e.get('data-discord', 'no'), name=(ih.find('b') if ih else (e.find('h3') or e.find('h4'))).get_text().strip(),
                        tags=(e.get('data-obj') or '').split(), legacy=False)
        meta = e.find('p', class_='meta')
        m = meta and re.match(r'\s*(\d+) points? · (.+)', meta.get_text())
        if not (e.get('id') and m):
            return None
        did = e['id']
        grp = self.group(m.group(2).strip())
        meas = e.find('p', class_='measures')
        tags = re.findall(r'\d+\.\d+', meas.get_text().split('which')[0]) if meas else []
        cyc = self.x.get('cycles', {}).get(did)
        if not cyc:
            cyc = 'wknd'; self.warn.append('%s: no data-cycle; used the weekend deadline' % did)
        return dict(did=did, kind='assignment', pts=int(m.group(1)), grp=grp, week=week, cycle=cyc,
                    discord='pre' if grp in ('Process Work', 'Projects') else 'none',
                    name=e.find(['h4', 'b']).get_text().strip(), tags=tags, legacy=True)

    def no_cycle(self, did, week):
        self.warn.append('%s: no data-week or data-cycle; used the module week (%d) and the weekend deadline' % (did, week))
        return 'wknd'

    def parse_rubric(self, e, info):
        dflt = ('Objective ' if len(info['tags']) == 1 else 'Objectives ') + ' and '.join(info['tags']) if info['tags'] else ''
        for tb in e.find_all('table'):
            cap = tb.find('caption')
            prev = tb.find_previous_sibling(['h3', 'h4', 'h5', 'p'])
            after_head = prev is not None and prev.get_text().strip().lower() in ('rubric', 'grading')
            if not (('rub' in (tb.get('class') or [])) or (cap and 'rubric' in cap.get_text().lower()) or after_head):
                continue
            mt = cap and re.search(r'(\d+) points', cap.get_text())
            total = int(mt.group(1)) if mt else None     # else: read the Total row below
            crit = []
            for tr in (tb.find('tbody') or tb).find_all('tr'):
                cells = tr.find_all(['th', 'td'])
                if not cells or cells[0].name == 'th' and cells[0].get('scope') == 'col':
                    continue
                desc = cells[0].get_text(' ', strip=True)
                if desc == 'Total':
                    if total is None:
                        total = int(re.search(r'\d+', cells[-1].get_text()).group(0))
                    continue
                ev = cells[1].get_text(' ', strip=True)
                tag = ev if ev.startswith('Objective') else ('Objective ' + ev if ev else dflt)
                crit.append((desc, float(re.search(r'\d+(?:\.\d+)?', cells[-1].get_text()).group(0)), tag))
            if total is None:
                total = sum(c[1] for c in crit)
            return total, crit
        for p in e.find_all('p'):
            b = p.find('b')
            m = b and re.match(r'(?:Rubric \((\d+)\)|Grading \((\d+) points?\)):', b.get_text())
            if not m:
                continue
            total = int(m.group(1) or m.group(2))
            txt = p.get_text().split(':', 1)[1].strip().rstrip('.')
            crit, carry = [], ''
            for part in txt.split('; '):
                part = carry + part.strip()
                mm = (re.match(r'(.+?) (\d+(?:\.\d+)?)(?: \(((?:Course Competency \d+, )?Objectives? [\d. and]+)\))?$', part)
                      or re.match(r'(.+?) \((\d+(?:\.\d+)?)(?: points?)?\)()$', part))   # "criterion (N)" form
                if not mm:
                    carry = part + '; '; continue   # a criterion that itself contains "; "
                carry = ''
                crit.append((mm.group(1), float(mm.group(2)), mm.group(3) or dflt))
            if carry:
                self.warn.append('%s: rubric text not parsed: %r' % (info['did'], carry))
            return total, crit
        return None, None

    def rubric_xml(self, ident, title, pts, crit):
        out = ['  <rubric identifier="%s">' % ident, '    <read_only>false</read_only>', '    <title>%s</title>' % esc(title),
               '    <reusable>false</reusable>', '    <public>false</public>', '    <points_possible>%d</points_possible>' % pts,
               '    <hide_score_total>false</hide_score_total>', '    <free_form_criterion_comments>false</free_form_criterion_comments>', '    <criteria>']
        for i, (d, p, tag) in enumerate(crit, 1):
            cid = '%s_%d' % (ident[-6:], i)
            d = d[0].upper() + d[1:]
            rs = [('Full', 'Meets the criterion', float(p))]
            if p >= 2:
                rs.append(('Partial', 'Partly meets the criterion', p / 2))
            rs.append(('Missing', 'Missing or does not meet the criterion', 0.0))
            out += ['      <criterion>', '        <criterion_id>%s</criterion_id>' % cid, '        <points>%.1f</points>' % p,
                    '        <description>%s%s</description>' % (esc(d), ' (%s)' % tag if tag else ''),
                    '        <long_description>%s</long_description>' % tag, '        <ratings>']
            for j, (rd, rl, rp) in enumerate(rs, 1):
                out += ['          <rating>', '            <description>%s</description>' % rd, '            <long_description>%s</long_description>' % rl,
                        '            <points>%.1f</points>' % rp, '            <criterion_id>%s</criterion_id>' % cid, '            <id>%s_r%d</id>' % (cid, j), '          </rating>']
            out += ['        </ratings>', '      </criterion>']
        return '\n'.join(out + ['    </criteria>', '  </rubric>'])

    def critique_line(self, e, info):
        """One line for the module overview's Critique (Discord) list."""
        if info['kind'] == 'discussion':
            return 'posted and discussed on Discord as described on its page.'
        if info['discord'] == 'pre':
            for b in e.find_all('b'):
                if b.get_text().startswith('Discord'):
                    seg = []
                    for x in b.next_siblings:
                        if getattr(x, 'name', None) == 'b':
                            break
                        seg.append(str(x))
                    t = ''.join(seg).strip()
                    if t:
                        return t
            return 'post on Discord the day before it is due; three comments.'
        return 'no Discord post; submit in Canvas only.'

    # ---------- one graded item
    def add_item(self, e, info, objs):
        did, nm, pts, kind = info['did'], info['name'], info['pts'], info['kind']
        post, due, close, note = self.dates(did, info['week'], info['cycle'])
        e2 = BeautifulSoup(str(e), 'html.parser').find('div')
        for t in e2.find_all(['p'], class_=['ih', 'meta']):
            t.decompose()
        if info['legacy']:
            h = e2.find(['h4']); h and h.decompose()
        else:
            h = e2.find('h4')                       # an item titled with an h4 (AVC2xx): drop the duplicate title
            if h and h.get_text().strip() == info['name']:
                h.decompose()
        tb = e2.find('div', recursive=False)
        if tb and tb.find('h3') and 'background' in (tb.get('style') or ''):
            tb.decompose()
        for h4 in e2.find_all('h4'):
            if h4.get_text().strip() == 'Objectives':
                nx = h4.find_next_sibling()
                if nx and nx.name in ('ol', 'ul'):
                    nx.decompose()
                h4.decompose()
        meas = e2.find('p', class_=['meas', 'measures'])
        if not meas:
            for pp in e2.find_all('p', recursive=False):
                if re.match(r'\s*\d+ points?,', pp.get_text()):
                    pp.string = re.sub(r'^\s*\d+ points?, [^.]+\.\s*', '', pp.get_text())
                    meas = pp; break
        meas_html = str(meas) if meas else ''
        if meas:
            meas.decompose()
        obj_html = ''.join(objs.get(t) or self.all_objs.get(t, '') for t in info['tags'])
        body = self.title_box(html.escape(nm, quote=False))
        if obj_html:
            body += '<h3>Objectives</h3><ul>%s</ul>' % obj_html
        elif kind == 'quiz':
            body += '<h3>Objectives</h3><p>This quiz confirms that you have read the syllabus. It does not measure a module objective.</p>'
        body += '<p><strong>%d points, %s.</strong></p>' % (pts, info['grp']) + canvasify(meas_html) + canvasify(inner(e2))
        body = re.sub(r'<p [^>]*>', '<p>', body)
        body += self.deadline_box(kind, info['discord'], post, due, close, note)
        total, crit = self.parse_rubric(e, info)
        rid = None
        if crit:
            if total != pts or sum(c[1] for c in crit) != pts:
                self.warn.append('%s: rubric total %s, criteria sum %d, item points %d' % (did, total, sum(c[1] for c in crit), pts))
            rid = self.gid('rubric', did)
            self.rubrics.append((rid, nm, pts, crit))
        aid = self.gid('asg', did)
        gref = self.gid('group', info['grp'])

        def settings(root_ns):
            x = ['<assignment identifier="%s" %s>' % (aid, NS) if root_ns else '<assignment identifier="%s">' % aid,
                 '  <title>%s</title>' % esc(nm), '  <time_zone_edited>Arizona</time_zone_edited>', '  <due_at>%s</due_at>' % iso(due),
                 '  <lock_at>%s</lock_at>' % iso(close), '  <unlock_at/>', '  <module_locked>false</module_locked>',
                 '  <assignment_group_identifierref>%s</assignment_group_identifierref>' % gref, '  <workflow_state>unpublished</workflow_state>']
            if rid:
                x += ['  <rubric_identifierref>%s</rubric_identifierref>' % rid, '  <rubric_use_for_grading>true</rubric_use_for_grading>',
                      '  <rubric_hide_score_total>false</rubric_hide_score_total>']
            x += ['  <assignment_overrides></assignment_overrides>', '  <allowed_extensions></allowed_extensions>', '  <has_group_category>false</has_group_category>',
                  '  <points_possible>%.1f</points_possible>' % pts, '  <grading_type>points</grading_type>', '  <all_day>false</all_day>',
                  '  <submission_types>%s</submission_types>' % ('discussion_topic' if kind == 'discussion' else 'online_upload,online_text_entry,online_url'),
                  '  <turnitin_enabled>false</turnitin_enabled>', '  <peer_reviews>false</peer_reviews>', '  <omit_from_final_grade>false</omit_from_final_grade>',
                  '  <post_policy><post_manually>false</post_manually></post_policy>', '</assignment>']
            return x

        if kind == 'discussion':
            tid, mid = self.gid('topic', did), self.gid('topicmeta', did)
            self.files['%s.xml' % tid] = ('<?xml version="1.0" encoding="UTF-8"?>\n<topic xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imsdt_v1p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imsdt_v1p1  http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imsdt_v1p1.xsd">\n'
                                          '  <title>%s</title>\n  <text texttype="text/html">%s</text>\n</topic>\n') % (esc(nm), html.escape(asc(body)))
            meta = ['<?xml version="1.0" encoding="UTF-8"?>', '<topicMeta identifier="%s" %s>' % (mid, NS), '  <topic_id>%s</topic_id>' % tid,
                    '  <title>%s</title>' % esc(nm), '  <type>topic</type>', '  <discussion_type>threaded</discussion_type>', '  <pinned>false</pinned>',
                    '  <require_initial_post>false</require_initial_post>', '  <workflow_state>unpublished</workflow_state>', '  <module_locked>false</module_locked>',
                    '  <allow_rating>false</allow_rating>', '  <only_graders_can_rate>false</only_graders_can_rate>', '  <sort_by_rating>false</sort_by_rating>']
            meta += ['  ' + l for l in settings(False)] + ['</topicMeta>']
            self.files['%s.xml' % mid] = '\n'.join(meta) + '\n'
            self.resources.append((tid, 'imsdt_xmlv1p1', None, ['%s.xml' % tid], [mid]))
            self.resources.append((mid, 'associatedcontent/imscc_xmlv1p1/learning-application-resource', '%s.xml' % mid, ['%s.xml' % mid], []))
            ref, ctype = tid, 'DiscussionTopic'
        else:
            hp = '%s/%s.html' % (aid, slug(nm))
            self.files[hp] = '<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n<title>%s</title>\n</head>\n<body>\n%s\n</body>\n</html>\n' % (esc(nm), asc(body))
            self.files['%s/assignment_settings.xml' % aid] = '<?xml version="1.0" encoding="UTF-8"?>\n' + '\n'.join(settings(True)) + '\n'
            self.resources.append((aid, 'associatedcontent/imscc_xmlv1p1/learning-application-resource', hp, [hp, '%s/assignment_settings.xml' % aid], []))
            ref, ctype = aid, 'Assignment'
        self.items.append(dict(info, rid=rid, due=due, close=close))
        return (self.gid('mi', did), ctype, nm, ref), (nm, due, close)

    # ---------- Module 0: course information pages
    def module0_pages(self, body):
        buckets, order, cur = {}, [], 'overview'
        def put(k, x):
            if k not in buckets:
                buckets[k] = []; order.append(k)
            buckets[k].append(x)
        for t in list(body.children):
            name = getattr(t, 'name', None)
            if name is None:
                put(cur, t); continue
            tid, cls = t.get('id'), t.get('class') or []
            if name == 'h3':
                cur = 'start' if tid in ('grading', 'competencies', 'competency-map') else ('ai' if tid == 'ai' else 'overview')
                if tid == 'ai':
                    buckets.setdefault('ai', []); order.append('ai') if 'ai' not in order else None
                    continue
                put(cur, t)
            elif name == 'div' and tid and 'el' not in cls:
                cur = tid
                put(tid, t)
            elif name == 'details' and 'instrnote' in cls:
                put('notes', t)
            elif name == 'div' and 'el' in cls:
                cur = 'overview'; put('overview', t)
            else:
                put(cur, t)
        def html_of(k, title=None):
            out = ''
            for t in buckets.get(k, []):
                if getattr(t, 'name', None) == 'div' and t.get('id') == k:
                    s = inner(t)
                    if title:
                        s = re.sub(r'^\s*<h3[^>]*>\s*%s\s*</h3>' % re.escape(title), '', s)
                    out += s
                else:
                    out += str(t)
            return out
        pages = []
        if 'start' in buckets:
            b = self.title_box('Start Here') + h2_to_h3(canvasify(html_of('start', 'Welcome')))
            b += '<p>Course materials are shared under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener">CC BY-NC-SA 4.0</a>.</p>'
            pages.append(('Start Here', b))
        if 'syllabus' in buckets:
            pages.append(('Syllabus and College Policies', self.title_box('Syllabus and College Policies') + canvasify(html_of('syllabus', 'Syllabus and College Policies'))))
        merge = self.x.get('merge_into_ai', [])
        if 'ai' in buckets:
            b = self.title_box('AI in This Course') + canvasify(html_of('ai'))
            for k in merge:
                b += canvasify(html_of(k))
            for f in self.x.get('ai_append', []):
                b += frag_body(f, self.color)
            pages.append(('AI in This Course', b))
        for k in order:
            if k in ('overview', 'start', 'syllabus', 'ai', 'notes') or (k in merge and 'ai' in buckets):
                continue
            h = buckets[k][0].find('h3') if hasattr(buckets[k][0], 'find') else None
            title = h.get_text().strip() if h else k.replace('-', ' ').title()
            pages.append((title, self.title_box(html.escape(title, quote=False)) + canvasify(html_of(k, title))))
        for title, f in self.x.get('site_pages', []):
            fs = BeautifulSoup(read(f), 'html.parser').find('main')
            for t in fs.find_all(['nav', 'h1']) + fs.find_all('p', class_='eyebrow'):
                t.decompose()
            pages.append((title, self.title_box(title) + h2_to_h3(canvasify(re.sub(r'</?div[^>]*>', '', inner(fs))))))
        ov = BeautifulSoup('<div>%s</div>' % ''.join(str(t) for t in buckets.get('overview', []) + buckets.get('notes', [])), 'html.parser').find('div')
        return ov, pages

    # ---------- modules
    def build(self):
        src = os.path.join(CANVAS, self.c, 'course.html')
        s = open(src, encoding='utf-8').read()
        if '<!-- build:main -->' not in s:
            self.warn.append('course page is not on the shared build yet')
        soup = BeautifulSoup(s, 'html.parser')
        main = soup.find('main')
        banner = main.find('div', class_='banner')
        self.title_text = banner.find('h1').get_text().strip() if banner else COURSES[self.c]['code']
        self.all_objs = {}
        for li in main.find_all('li'):
            b = li.find('b')
            mk = b and re.fullmatch(r'\s*(\d+\.\d+)\s*', b.get_text()) and li.get_text().strip().startswith(b.get_text().strip())
            if mk:
                self.all_objs.setdefault(b.get_text().strip(), str(li))
        for det in main.find_all('details', class_='lesson'):
            summ = det.find('summary')
            num = int(re.search(r'\d+', summ.find(class_='mnum').get_text()).group(0))
            lt = BeautifulSoup(str(summ.find(class_='ltitle')), 'html.parser')
            for t in lt.find_all(class_=['mnum', 'vh']):
                t.decompose()
            mtitle = lt.get_text().strip().lstrip(':').strip()
            mwk_t = summ.find(class_='mwk')
            mwk = BeautifulSoup(str(mwk_t), 'html.parser') if mwk_t else None
            if mwk:
                for t in mwk.find_all(class_='vh'):
                    t.decompose()
            mwk = re.sub(r'\s+', ' ', mwk.get_text()).strip(' ,') if mwk else ''
            week = int(re.search(r'Week (\d+)', mwk).group(1)) if re.search(r'Week (\d+)', mwk) else num + 1
            body = BeautifulSoup(str(det.find('div', class_='lbody')), 'html.parser').find('div')
            m0_pages = []
            if num == 0 or det.get('id') == 'start-here':
                body, m0_pages = self.module0_pages(body)
            notes = body.find_all('details', class_='instrnote')
            note_html = ''.join(inner(n.find('div', class_='inbody') or n) for n in notes)
            for n in notes:
                n.decompose()
            objs = {}
            ol = body.find(['ul', 'ol'], class_='obj')
            for li in (ol.find_all('li') if ol else []):
                b = li.find('b')
                k = b.get_text().strip() if b and li.get_text().strip().startswith(b.get_text().strip()) else (re.match(r'\s*(\d+\.\d+)', li.get_text()) or [None, None])[1]
                if k:
                    objs[k] = str(li)
            graded = []
            for e in body.find_all('div', class_='el'):
                info = self.item_info(e, week)
                if info:
                    graded.append((e, info))
            # overview page
            items, due_lines = [], []
            for e, info in graded:
                info['crit_line'] = self.critique_line(e, info)
                ii, dl = self.add_item(e, info, objs)
                items.append(ii); due_lines.append(dl)
                e.decompose()
            alist = ''.join('<li>%s (%d points, %s)</li>' % (html.escape(i['name'], quote=False), i['pts'], i['grp']) for _, i in graded)
            dlist = ''.join('<li>%s at noon (hard close %s at noon): %s</li>' % (fmt(d), fmt(c), html.escape(n, quote=False)) for n, d, c in sorted(due_lines, key=lambda x: x[1]))
            h3s = body.find_all('h3')
            ah = next((h for h in h3s if h.get_text().strip() == 'Assessment'), None)
            has_crit = any(h.get_text().strip().startswith('Critique') for h in h3s)
            clist = '' if has_crit else ''.join('<li><b>%s:</b> %s</li>' % (html.escape(i['name'], quote=False), i['crit_line']) for e, i in graded)
            if clist:
                alist_html = '<ul>%s</ul><h3>Critique (Discord)</h3><ul>%s</ul>' % (alist, clist)
            else:
                alist_html = '<ul>%s</ul>' % alist
            if alist:
                if ah:
                    ah.insert_after(BeautifulSoup(alist_html, 'html.parser'))
                else:
                    body.append(BeautifulSoup('<h3>Assessment</h3>' + alist_html, 'html.parser'))
            dh = next((h for h in h3s if h.get_text().strip().startswith('Due')), None)
            if dlist:
                if dh:
                    for sib in list(dh.next_siblings):
                        if getattr(sib, 'name', None) == 'h3':
                            break
                        sib.extract()
                    dh.insert_after(BeautifulSoup('<ul>%s</ul>' % dlist, 'html.parser'))
                else:
                    body.append(BeautifulSoup('<h3>Due</h3><ul>%s</ul>' % dlist, 'html.parser'))
            oh = next((h for h in h3s if h.get_text().strip() == 'Objectives'), None)
            if oh:
                ws = self.week_start(week)
                wk = re.sub(r'Week %d\b' % week, 'Week %d (%s to %s)' % (week, ws.strftime('%-d %B'), (ws + dt.timedelta(days=6)).strftime('%-d %B %Y')), mwk, 1)
                oh.insert_before(BeautifulSoup('<p>%s</p>' % html.escape(wk, quote=False), 'html.parser'))
                nxt = oh.find_next_sibling()
                if not (nxt and nxt.name == 'p' and 'By the end of this module' in nxt.get_text()):
                    oh.insert_after(BeautifulSoup('<p>Module %d objectives. By the end of this module, you will be able to:</p>' % num, 'html.parser'))
            ov_title = 'Module %d Overview: %s' % (num, mtitle)
            ov_body = self.title_box(html.escape(ov_title, quote=False)) + h2_to_h3(canvasify(inner(body)))
            mitems = [self.add_page(ov_title, ov_body)]
            for t, b in m0_pages:
                mitems.append(self.add_page(t, b))
            if m0_pages and self.x.get('m0_docs'):
                sub, docs = self.x['m0_docs']
                mitems.append((self.gid('mi', 'sub', sub), 'ContextModuleSubHeader', sub, None))
                for t, f in docs:
                    mitems.append(self.add_page(t, frag_body(f, self.color)))
            if m0_pages and items:
                mitems.append((self.gid('mi', 'graded-sub'), 'ContextModuleSubHeader', 'Graded work', None))
            mitems += items
            if note_html.strip():
                nt = 'Instructor Notes: Module %d' % num
                nb = canvasify(note_html)
                ins = self.x.get('note_inserts', {}).get(num)
                if ins:
                    f, rx, old = ins
                    key = re.search(rx, frag_body(f, self.color), re.S)
                    if key and old in nb:
                        nb = nb.replace(old, key.group(0))
                    else:
                        self.warn.append('note insert for Module %d did not apply' % num)
                mitems.append(self.add_page(nt, self.title_box(nt) + '<p><strong>Unpublished. Never shown to students.</strong></p>' + nb))
            self.modules.append((self.gid('module', str(num)), 'Module %d: %s' % (num, mtitle), mitems))
        self.graded_el_count = sum(1 for e in main.find_all('div', class_='el') if e.get('data-id') or self.item_info(e, 0))
        self.ungraded = [(e.get('id') or (e.find(['h4', 'b']) or e).get_text()[:40]) for e in main.find_all('div', class_='el') if not (e.get('data-id') or self.item_info(e, 0))]
        self.finish()

    def finish(self):
        t = self.term
        title = '%s %s, %s (DRAFT%s)' % (COURSES[self.c]['code'], self.title_text, t['label'], ', ' + self.x['variant'] if self.x.get('variant') else '')
        cs = 'course_settings/'
        self.files[cs + 'course_settings.xml'] = ('<?xml version="1.0" encoding="UTF-8"?>\n<course identifier="%s" %s>\n  <title>%s</title>\n  <course_code>%s</course_code>\n'
            '  <start_at>%sT07:00:00</start_at>\n  <conclude_at>%sT06:59:00</conclude_at>\n  <time_zone>America/Phoenix</time_zone>\n'
            '  <group_weighting_scheme>percent</group_weighting_scheme>\n  <apply_assignment_group_weights>true</apply_assignment_group_weights>\n'
            '  <grading_standard_enabled>true</grading_standard_enabled>\n  <is_public>false</is_public>\n  <default_view>modules</default_view>\n</course>\n') % (
            self.gid('course'), NS, esc(title), COURSES[self.c]['code'], t['start'].isoformat(), (t['conclude'] + dt.timedelta(days=1)).isoformat())
        self.files[cs + 'assignment_groups.xml'] = '<?xml version="1.0" encoding="UTF-8"?>\n<assignmentGroups %s>\n' % NS + ''.join(
            '  <assignmentGroup identifier="%s">\n    <title>%s</title>\n    <position>%d</position>\n    <group_weight>%.1f</group_weight>\n  </assignmentGroup>\n'
            % (self.gid('group', g), esc(g), i + 1, w) for i, (g, w) in enumerate(self.groups)) + '</assignmentGroups>\n'
        self.files[cs + 'rubrics.xml'] = '<?xml version="1.0" encoding="UTF-8"?>\n<rubrics %s>\n' % NS + '\n'.join(self.rubric_xml(*r) for r in self.rubrics) + '\n</rubrics>\n'
        mm = ['<?xml version="1.0" encoding="UTF-8"?>', '<modules %s>' % NS]
        for p, (mid, mt, items) in enumerate(self.modules, 1):
            mm += ['  <module identifier="%s">' % mid, '    <title>%s</title>' % esc(mt), '    <workflow_state>unpublished</workflow_state>', '    <position>%d</position>' % p,
                   '    <require_sequential_progress>false</require_sequential_progress>', '    <items>']
            for q, (iid, ct, it, ref) in enumerate(items, 1):
                mm += ['      <item identifier="%s">' % iid, '        <content_type>%s</content_type>' % ct, '        <workflow_state>unpublished</workflow_state>', '        <title>%s</title>' % esc(it)]
                if ref:
                    mm.append('        <identifierref>%s</identifierref>' % ref)
                mm += ['        <position>%d</position>' % q, '        <new_tab/>', '        <indent>0</indent>', '      </item>']
            mm += ['    </items>', '  </module>']
        self.files[cs + 'module_meta.xml'] = '\n'.join(mm + ['</modules>']) + '\n'
        self.files[cs + 'canvas_export.txt'] = '%s, draft cartridge built by tools/course-build/package.py.\n' % title
        mf = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<manifest identifier="%s" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource" xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lomresource_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lommanifest_v1p0.xsd">' % self.gid('manifest'),
              '  <metadata>', '    <schema>IMS Common Cartridge</schema>', '    <schemaversion>1.1.0</schemaversion>',
              '    <lomimscc:lom><lomimscc:general><lomimscc:title><lomimscc:string>%s</lomimscc:string></lomimscc:title></lomimscc:general></lomimscc:lom>' % esc(title),
              '  </metadata>', '  <organizations>', '    <organization identifier="org_1" structure="rooted-hierarchy">', '    <item identifier="LearningModules">']
        for mid, mt, items in self.modules:
            mf += ['      <item identifier="%s">' % mid, '        <title>%s</title>' % esc(mt)]
            for iid, ct, it, ref in items:
                mf += ['        <item identifier="%s"%s>' % (iid, ' identifierref="%s"' % ref if ref else ''), '          <title>%s</title>' % esc(it), '        </item>']
            mf.append('      </item>')
        mf += ['    </item>', '    </organization>', '  </organizations>', '  <resources>']
        for ident, typ, href, fl, deps in self.resources:
            mf.append('    <resource identifier="%s" type="%s"%s>' % (ident, typ, ' href="%s"' % href if href else ''))
            mf += ['      <file href="%s"/>' % f for f in fl] + ['      <dependency identifierref="%s"/>' % d for d in deps] + ['    </resource>']
        mf += ['    <resource identifier="%s" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="course_settings/canvas_export.txt">' % self.gid('settings')]
        mf += ['      <file href="course_settings/%s"/>' % f for f in ('course_settings.xml', 'module_meta.xml', 'assignment_groups.xml', 'rubrics.xml', 'canvas_export.txt')]
        mf += ['    </resource>', '  </resources>', '</manifest>']
        self.files['imsmanifest.xml'] = '\n'.join(mf) + '\n'
        self.content_checks()

    def content_checks(self):
        if sum(w for _, w in self.groups) != 100:
            self.warn.append('group weights do not add to 100')
        names = dict(self.groups)
        for i in self.items:
            if i['grp'] not in names:
                self.warn.append('%s: group %r is not a Canvas group' % (i['did'], i['grp']))
        priv = self.x.get('private_terms', [])
        for p, c in self.files.items():
            if not p.endswith(('.html', '.xml')):
                continue
            notes = '/instructor-notes-' in p
            if '\u2014' in c or '&#8212;' in c or 'href="#"' in c:
                self.warn.append('%s: em dash or empty link' % p)
            low = c.lower()
            for bad in ('data-instr', 'instrnote', '{{'):
                if bad in low:
                    self.warn.append('%s: leftover %r' % (p, bad))
            for mark in ('[verify', '[instructor to create', 'tbd'):
                if mark in low and not (mark == 'tbd' and not re.search(r'\btbd\b', low)):
                    self.warn.append('%s: contains %r' % (p, mark))
            if not notes and ('Instructor notes' in c or 'Unpublished. Never shown' in c):
                self.warn.append('%s: instructor text on a student page' % p)
            for w in priv:
                if w in c and not notes:
                    self.warn.append('%s: private term %r outside Instructor Notes' % (p, w))

    def write(self, out_dir):
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, self.fname)
        with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
            z.writestr('imsmanifest.xml', self.files['imsmanifest.xml'])
            for p in sorted(self.files):
                if p != 'imsmanifest.xml':
                    z.writestr(p, self.files[p])
        return path


def check(path, course=None):
    """Open a package and check it: zip, manifest, files, rubric totals, and item count against the page."""
    probs = []
    z = zipfile.ZipFile(path)
    names = set(z.namelist())
    man = z.read('imsmanifest.xml').decode('utf-8')
    xml.dom.minidom.parseString(man.encode('utf-8'))
    for n in names:
        if n.endswith('.xml'):
            try:
                xml.dom.minidom.parseString(z.read(n))
            except Exception as ex:
                probs.append('%s does not parse: %s' % (n, ex))
    for f in re.findall(r'<file href="([^"]+)"', man):
        if f not in names:
            probs.append('manifest file missing: ' + f)
    rids = set(re.findall(r'<resource identifier="([^"]+)"', man))
    for r in set(re.findall(r'identifierref="([^"]+)"', man)) - rids:
        probs.append('manifest reference to a missing resource: ' + r)
    rub = z.read('course_settings/rubrics.xml').decode('utf-8')
    rpts = {}
    for m in re.finditer(r'<rubric identifier="([^"]+)">(.*?)</rubric>', rub, re.S):
        tot = float(re.search(r'<points_possible>([\d.]+)', m.group(2)).group(1))
        crit = sum(float(x) for x in re.findall(r'<criterion>\s*<criterion_id>[^<]*</criterion_id>\s*<points>([\d.]+)', m.group(2)))
        rpts[m.group(1)] = tot
        if abs(tot - crit) > 1e-6:
            probs.append('rubric %s: criteria %.1f, total %.1f' % (m.group(1), crit, tot))
    asg = []
    for n in names:
        if n.endswith('assignment_settings.xml') or (n.endswith('.xml') and '<topicMeta' in z.read(n).decode('utf-8')[:400]):
            x = z.read(n).decode('utf-8')
            pts = float(re.search(r'<points_possible>([\d.]+)', x).group(1))
            r = re.search(r'<rubric_identifierref>([^<]+)', x)
            title = re.search(r'<title>([^<]*)', x).group(1)
            asg.append((title, pts, r and r.group(1)))
            if r and abs(rpts.get(r.group(1), -1) - pts) > 1e-6:
                probs.append('%s: rubric %s points, item %s' % (title, rpts.get(r.group(1)), pts))
    norub = [a[0] for a in asg if not a[2]]
    n_el = None
    if course:
        c = Course(course); soup = BeautifulSoup(open(os.path.join(CANVAS, course, 'course.html'), encoding='utf-8').read(), 'html.parser')
        els = soup.find('main').find_all('div', class_='el')
        n_el = sum(1 for e in els if e.get('data-id') or c.item_info(e, 0))
        if n_el != len(asg):
            probs.append('graded items on the page %d, assignments in the package %d' % (n_el, len(asg)))
    return dict(files=len(names), assignments=len(asg), graded_on_page=n_el, rubrics=len(rpts), without_rubric=norub, problems=probs)


def run(c, term=None, out=None):
    k = Course(c, term)
    k.build()
    path = k.write(out or os.path.join(CANVAS, c))
    tot = {}
    for i in k.items:
        tot[i['grp']] = tot.get(i['grp'], 0) + i['pts']
    print('%s: built %s' % (c, os.path.relpath(path, ROOT)))
    print('  modules %d, pages %d, assignments %d (discussions %d), rubrics %d; graded items on page %d; ungraded el kept on overview pages: %s' % (
        len(k.modules), sum(1 for r in k.resources if r[1] == 'webcontent'), len(k.items), sum(1 for i in k.items if i['kind'] == 'discussion'),
        len(k.rubrics), k.graded_el_count, ', '.join(k.ungraded) or 'none'))
    print('  group points', tot)
    for w in k.warn:
        print('  - ' + w)
    return path


def main(argv):
    if not argv:
        print(__doc__); return 0
    if argv[0] == '--check':
        r = check(argv[1], argv[2] if len(argv) > 2 else None)
        for k, v in r.items():
            print('%s: %s' % (k, v))
        return 1 if r['problems'] else 0
    term = out = None
    if '--term' in argv:
        i = argv.index('--term'); term = argv[i + 1]; del argv[i:i + 2]
        if term not in TERMS:
            raise SystemExit('term must be one of ' + ', '.join(TERMS))
    if '--out' in argv:
        i = argv.index('--out'); out = os.path.join(ROOT, argv[i + 1]); del argv[i:i + 2]
    if argv[0] == '--all':
        targets = [c for c in COURSES if '<!-- build:main -->' in open(os.path.join(CANVAS, c, 'course.html'), encoding='utf-8').read()]
        skipped = [c for c in COURSES if c not in targets]
        if skipped:
            print('not on the shared build yet, skipped: ' + ', '.join(skipped))
    else:
        targets = argv
    for c in targets:
        if not (term or EXTRA.get(c, {}).get('term')):
            print('%s: skipped, no term set in EXTRA; pass --term' % c); continue
        run(c, term, out)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
