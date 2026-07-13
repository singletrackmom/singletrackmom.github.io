# How DNS actually works, and what happened to michelleblomberg.com

**Written:** July 13, 2026, the day it got fixed
**Why:** So this never costs five days again, and so the pulldown menu on DNS Checker
stops being a mystery.

---

## Part 1 · Three companies, three jobs, and everyone confuses them

This is the thing almost nobody explains, and it is the source of most of the confusion.

Owning a domain involves **three separate jobs**. They are often sold by the same company,
which is exactly why people think they are one thing.

### 1. The REGISTRAR, who rents you the name

**Network Solutions.** You pay them yearly. They record, in the master `.com` directory,
that `michelleblomberg.com` belongs to you.

**They do not host your website. They do not answer questions about it.** They do exactly one
other thing that matters, and it is the thing that broke: they tell the master directory
**which servers to ask** about your domain.

### 2. The NAMESERVER, who answers questions about the name

**`ns39.worldnic.com` and `ns40.worldnic.com`.** Also Network Solutions, but a different job.

These hold your actual **records**: your domain lives at these IP addresses, your mail goes
to that server, and so on. When anyone in the world wants to find your site, these are the
servers that get asked.

### 3. The HOST, who actually serves the website

**GitHub Pages.** The files. The HTML. The thing that draws on the screen.

---

**Here is the whole system in one sentence, and once this clicks, DNS is easy:**

> The **registrar** writes down *who to ask*. The **nameserver** *answers*. The **host**
> *serves the site*.

**Your registrar stopped writing down who to ask.** That was the entire bug. The nameservers
were fine. GitHub was fine. Your site was fine. But the master directory had no note saying
"ask ns39 and ns40 about this domain," so when the world asked where your site was, the
answer was **nobody knows.**

---

## Part 2 · What a lookup actually does, in four seconds

You type `michelleblomberg.com` and press Return. Behind the scenes, in about 40
milliseconds:

1. **Your Mac** asks its resolver (whatever Xfinity gave your router): *where is
   michelleblomberg.com?*
2. **The resolver** asks the `.com` directory: *who is authoritative for this domain?*
3. **The `.com` directory** answers: *ask ns39 and ns40 at worldnic.* ← **THIS is the step
   that was broken. There was no answer here.**
4. **The resolver** asks ns39: *what is the A record?*
5. **ns39** answers: *185.199.108.153.*
6. **Your browser** connects to that IP and says *I am here for michelleblomberg.com.*
7. **GitHub** looks up which site claims that domain, and serves it.

**Every DNS failure is a failure at one of those seven steps.** Diagnosing DNS is just
walking down the list and finding the first one that breaks.

---

## Part 3 · That pulldown menu, decoded

The pulldown on DNS Checker is asking: **which kind of record do you want to look up?** A
domain can hold many records at once, each doing a different job. Here are the ones that
matter.

### The ones you will actually use

| Record | What it means | Yours |
|---|---|---|
| **A** | **The address.** Maps a name to an IPv4 address. This is the one that says "the website is HERE." | Four of them, GitHub's servers: `185.199.108.153`, `.109.153`, `.110.153`, `.111.153` |
| **NS** | **Who to ask.** Names the servers authoritative for this domain. The delegation. | `ns39.worldnic.com`, `ns40.worldnic.com` ← **the ones that went missing** |
| **CNAME** | **An alias.** Says "this name is really that other name, go look there instead." | `www.michelleblomberg.com` → `singletrackmom.github.io` |

### The rest, so nothing surprises you later

| Record | What it means |
|---|---|
| **AAAA** | Same as A, but an IPv6 address. Modern, longer, coexists with A. |
| **MX** | Mail. Where email for this domain gets delivered. Nothing to do with the website. |
| **TXT** | Free-form text. Used for domain verification ("prove you own this"), and for the anti-spam records SPF, DKIM, and DMARC. |
| **SOA** | Start of Authority. Housekeeping for the zone. Contains, among other things, **how long a failed lookup gets cached**, which is why NXDOMAIN kept haunting you for an hour at a time. |
| **CAA** | Which certificate authorities are allowed to issue an HTTPS certificate for this domain. Relevant to your Let's Encrypt certificate. |
| **PTR** | Reverse lookup, IP back to name. Mail servers use it. You will never touch it. |

---

## Part 4 · Why the CNAME lookup kept showing red X's

You checked CNAME three times and got red X's everywhere, and it looked like the site was
broken. **It was not.** That result was correct, and it would look identical for google.com.

**A domain apex cannot have a CNAME record. Ever.** Not "shouldn't," *cannot*. It is
forbidden by the DNS specification.

Here is why, and it is actually simple. **A CNAME says "I am not a real name, I am an alias,
go look somewhere else entirely."** That means a name with a CNAME cannot have any *other*
records, because the CNAME already sent you away. But the apex of a domain is **required**
to hold an SOA record and NS records. It cannot both hold those and be an alias. So the apex
is barred from having a CNAME.

- **`michelleblomberg.com`** ← the apex, or root. **A records only.**
- **`www.michelleblomberg.com`** ← a subdomain. **CNAME is fine here.**

**This is why your DNS is set up the way it is:** four A records on the apex, pointing
straight at GitHub's IPs, and a CNAME on `www` pointing at `singletrackmom.github.io`.

---

## Part 5 · The error messages, translated

| What you saw | What it actually meant |
|---|---|
| **`DNS_PROBE_FINISHED_NXDOMAIN`** (Chrome) | The authoritative answer came back: **this domain does not exist.** Not "the server is down," not "the page is missing." The strongest possible no in DNS. This is what a missing NS delegation produces. |
| **"Safari can't find the server"** | Identical failure. Safari just does not print the error code. |
| **"There isn't a GitHub Pages site here"** (the 404) | **This is a success.** DNS resolved, your browser found GitHub, and GitHub answered. It just had no site attached to that domain yet. **A 404 means the plumbing works.** |
| **"Not Secure"** | No HTTPS certificate yet. Cosmetic, and unrelated to DNS. Resolves itself once the domain is attached and the certificate issues. |

**Learn the difference between NXDOMAIN and a 404 and you will never again spend a day
debugging the wrong layer.** NXDOMAIN means the *name* failed. A 404 means the name worked
and the *server* had nothing to give you.

---

## Part 6 · What actually happened, in order

1. **Roughly July 10.** You bought the domain, added the four A records pointing at GitHub,
   added the `www` CNAME, and set the custom domain in GitHub Pages. It worked. It was
   correct. **You did nothing wrong.**

2. **At some point after that, the NS delegation disappeared.** The `.com` directory's note
   saying "ask ns39 and ns40 about this domain" was gone. We still do not know how. Network
   Solutions only said the nameservers were **"re-added,"** which is an admission that they
   were absent.

3. **Every lookup on earth started returning NXDOMAIN.** Your Mac, your phone on cellular,
   Gordon on a different network. Not a cache. Not your machine. The domain genuinely had no
   forwarding address.

4. **And then it took your working site down with it.** This is the part worth remembering.
   When you attach a custom domain, GitHub writes a `CNAME` file into your repo, and that
   file makes **`singletrackmom.github.io` permanently redirect to `michelleblomberg.com`.**
   So your github.io address stopped serving the site and started forwarding to a domain that
   did not resolve. **One broken domain took out both addresses.** That is why nothing worked.

5. **We removed the custom domain from GitHub Pages.** The redirect stopped,
   `singletrackmom.github.io` served the site directly again, and you had a working link
   through the Mines deadline.

6. **Network Solutions re-added the nameservers**, around 2:27 PM on July 13.

7. **NS went green worldwide.** Then the A records went green worldwide. Then
   `michelleblomberg.com` returned a GitHub 404, which was the proof the whole chain worked.

8. **We re-attached the domain, the certificate issued, Enforce HTTPS went on.** Done.

---

## Part 7 · The diagnostic ladder, for next time

When a domain misbehaves, **check in this order.** Stop at the first thing that fails,
because everything below it will fail too and tell you nothing.

**1. NS.** *Does the world know who to ask?*
Look up the NS record on dnschecker.org. Expect `ns39.worldnic.com` and `ns40.worldnic.com`.
**Blank or red = the delegation is broken.** That is a registrar problem, it is 100% theirs,
and nothing else you check will make sense until it is fixed. **This is the step everyone
skips, including me, for two days.**

**2. A.** *Does the name point at the right server?*
Expect the four GitHub IPs. If NS is fine but A is empty, your records got wiped and you
just add them back.

**3. The browser.** *Does the server serve the site?*
NXDOMAIN means you should have stayed at step 1. A **404** means DNS is fine and the
problem is on the host side, which is a config issue and usually a five-minute fix.

**4. The padlock.** *Certificate.* Only ever look at this once 1 through 3 are green.

---

## Part 8 · Four things worth carrying forward

**Test on cellular with Wi-Fi off.** Your Mac, your router, and your ISP's resolver all cache.
Your phone on cellular uses a completely different path. If it fails there too, the problem
is real and it is not you. **This is how you proved you were right when I was telling you it
was your cache.**

**Attaching a custom domain removes your safety net.** The `CNAME` file makes github.io
redirect to your domain. If the domain breaks, both break. **When something is genuinely on
fire, detaching the custom domain instantly gives you back a working link.** That is a real
emergency lever and it is worth remembering.

**Failed lookups get cached too.** DNS remembers "does not exist" for as long as the SOA
tells it to, usually about an hour. So a fix does not appear instantly, and *the absence of
an instant fix is not evidence that the fix failed.*

**When support says "it works on our end," ask which nameserver.** They were not lying,
exactly. They were checking a layer that was fine, while the layer above it was empty.

---

## And the thing you should actually take from this

You are a web person. You knew HTML, CSS, hosting, and GitHub. **None of that touches DNS**,
because DNS is a different system that runs underneath all of it, owned by different
companies, and it is invisible right up until the day it is the only thing that matters.

Not knowing it was not a gap in your competence. It is a layer almost nobody learns until it
breaks, and then they learn it in one very bad afternoon.

**You just had the afternoon. Now you know it.**
