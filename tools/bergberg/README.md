# Berg Berg Photography Marketing Plan: source

The pages in /bergberg/ are built from these files. Edit here, never the built pages.

* One HTML fragment per tab (index.html, venues.html, and so on). The build adds the header, tabs and footer.
* cal.py holds the week-by-week list (W). Running it writes bergberg/weeks.js and the Calendar rows.
* build.py writes every tab into bergberg/.
* bergberg/carry.js is written by the weekly check: unfinished jobs that show first in This Week.
* bergberg/scripts.js holds the message pop-outs. bergberg/bergberg.js and bergberg.css are edited in place.

Rebuild from the repo root:

    python3 tools/bergberg/cal.py && python3 tools/bergberg/build.py
