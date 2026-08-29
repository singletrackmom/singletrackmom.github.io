# michelleblomberg.com, the domain and DNS record

**Status: RESOLVED and stable.** Live since 16 August 2026, confirmed working 29 August 2026. This file is the archive of a five-day outage in July plus a second failure in August, kept because the domain broke twice and the second cause was different from the first.

**Goal:** never lose five days to DNS again, and know in one minute which layer is broken.
**Audience:** me, the next time the site will not load.
**Process:** check the CNAME file first, then walk the diagnostic ladder below. Do not guess and do not clear the cache.

---

## ⚡ IF THE SITE IS DOWN, READ ONLY THIS BOX

**1. Check the `CNAME` file at the repo root first, before touching DNS.** It must contain exactly `michelleblomberg.com` and nothing else. **That file IS the GitHub Pages custom-domain setting**; GitHub reads the domain out of it, and the Settings → Pages box is just a friendlier door to writing the same file. A missing CNAME file was the entire cause of the August failure, and it cost days of DNS debugging that was looking at the wrong layer.

**2. Test on your phone with Wi-Fi OFF, cellular only.** Cellular uses a completely different resolver than your Mac, your router, or your ISP. This is how you proved you were right in July when support kept telling you it was your cache. It was never the cache.

**3. Learn the two error messages.** `DNS_PROBE_FINISHED_NXDOMAIN` means the NAME failed, a DNS problem. A **404** means the name worked and the server had nothing to give you, a hosting problem. A 404 is good news; it means the plumbing works.

**4. The emergency lever.** GitHub → repo → Settings → Pages → Custom domain → clear the box → Save. Attaching a custom domain writes the CNAME file, which makes `singletrackmom.github.io` redirect to `michelleblomberg.com`, so a broken domain takes BOTH addresses down. Clearing the box stops the redirect instantly and serves the site from github.io again. Use this any time the domain misbehaves and something important is due.

---

## What broke, twice

| When | Cause | Fix |
|---|---|---|
| **July 10 to 13** | The NS delegation went missing at Network Solutions. The `.com` directory had no note saying "ask ns39 and ns40 about this domain," so every lookup on earth returned NXDOMAIN. Network Solutions said the nameservers were **"re-added,"** which is an admission they were absent. They never explained how. Ticket **I-26067315**. | They re-added the delegation. Then the two worldnic nameservers disagreed for a while, making resolution a coin flip. That settled on its own; both now answer NOERROR with a matching SOA serial. |
| **Through August 16** | The `CNAME` file had been removed from the repo during the July emergency workaround and was never put back. | Restoring `CNAME` fixed it. No registrar change, no Cloudflare move. |

## Is it solved for good?

**Mostly, but not structurally.** Two things are worth knowing:

- **The CNAME file can go missing again**, because removing it is exactly what the emergency lever does. If you ever detach the custom domain in a hurry, put the file back afterward or the site quietly serves from github.io.
- **The domain still resolves through ns39 and ns40 at worldnic**, the same two nameservers that disagreed in July. Network Solutions never explained the original delegation loss. If the intermittent NXDOMAIN ever returns, **the durable fix is to move DNS hosting to Cloudflare (free) while keeping the domain registered at Network Solutions.** That removes worldnic from the resolution path entirely. It is a web form, no Terminal, and it takes 24 to 48 hours to take effect, so it cannot be done in a hurry. Steps are in the July section below.

**Not an open task.** Do not carry "move to Cloudflare" as a to-do. It is the contingency plan, not work to be done.

## What goes on a resume

**`michelleblomberg.com`.** The old rule saying to use `singletrackmom.github.io` on submitted applications was written in July while the domain was flapping, and it is retired.

---

# Appendix A · The August resolution, in full

## What happened, start to finish

### July: intermittent NXDOMAIN
The domain resolved sometimes and not others, minutes apart, across different networks and different resolvers. The working theory (below, and it looks right) was that one of the two worldnic nameservers was serving the zone while the other answered NXDOMAIN, making every lookup a coin flip.

### July: the workaround
Because the site was unusable and it was in the middle of a job search, **the custom domain was detached from GitHub Pages and the `CNAME` file was removed from the repo.** The site fell back to `singletrackmom.github.io`, which worked. That was the right call at the time.

### The advice given in July, which was NOT followed
Moving DNS hosting to Cloudflare (keeping the domain registered at Network Solutions) was recommended as the durable fix, because it removes worldnic from the resolution path entirely. **This was never done, and it turned out not to be necessary.**

### August 16: what we actually found
Two separate problems had stacked on top of each other:

**Problem 1, the DNS flap: appears to have been fixed by the provider at some point.** Tested on August 16 using DNS-over-HTTPS, which reports which authoritative server answered:

| Nameserver | IP | Result |
|---|---|---|
| ns39.worldnic.com | 162.159.26.212 | `Status: 0` NOERROR, all four GitHub A records |
| ns40.worldnic.com | 162.159.27.146 | `Status: 0` NOERROR, all four GitHub A records |

SOA serial `126071214` consistent on both. The two servers agree, which is exactly the condition that was failing in July. Network Solutions most likely republished the zone as routine maintenance and never told anyone.

**Problem 2, the real remaining blocker: the `CNAME` file was gone.** Removing it in July was a deliberate workaround, but it meant that even with perfect DNS, GitHub Pages did not claim the domain and could not serve it. **This was the actual reason the site would not load in August.**

### The fix, in full
1. Created `CNAME` at the repo root containing one line: `michelleblomberg.com`
2. Pushed it.
3. That was it. GitHub Pages picked it up automatically and the site came up.

**Note:** the GitHub web UI was never used. Michelle could not log in to github.com that night. It did not matter, because pushing the file does the same job.

### Verified working on August 16
- `michelleblomberg.com` serves the site
- `michelleblomberg.com/copamigo` returns CopaMigo
- `michelleblomberg.com/render` returns the Render dashboard
- All portfolio links on the resume and cover letter now point at the custom domain

---

## If it breaks again, do this in order

1. **Check the `CNAME` file exists** at the repo root and contains exactly `michelleblomberg.com`. This is the most likely cause and the cheapest to check. Verify at:
   `https://raw.githubusercontent.com/singletrackmom/singletrackmom.github.io/main/CNAME`
2. **Check whether it is actually a DNS failure.** Look at the browser error. `DNS_PROBE_FINISHED_NXDOMAIN` means DNS. A 404 or a certificate warning means something else and DNS is fine.
3. **If it is NXDOMAIN, test both nameservers.** Cannot use `dig` from the assistant sandbox (port 53 blocked), but DNS-over-HTTPS works and reports which server answered:
   `https://dns.google/resolve?name=michelleblomberg.com&type=A`
   Run it several times. The `Comment` field shows the responding server. If one returns NOERROR and another returns NXDOMAIN, the July flap is back.
4. **Only then consider Cloudflare.** It remains the durable fix if worldnic starts flapping again. Free, domain stays at Network Solutions, only the two nameserver records change. Do not do it preemptively.

## What to tell a future Claude session

> "The domain is fixed. We never moved to Cloudflare and we are still on Network Solutions. The problem was that the CNAME file had been removed from the repo, and that file is the GitHub Pages setting. Read `tools/DNS_michelleblomberg.md`."


## The 24-hour soak test (use this any time the domain is re-attached)

Check at roughly these intervals. Any single failure means it is flapping and the domain should come off the resume until it settles.

| When | Test | Pass looks like |
|---|---|---|
| +15 min | Load `https://michelleblomberg.com` | Site loads, padlock, no warning |
| +15 min | Load `https://www.michelleblomberg.com` | Redirects to the apex, loads |
| +1 hr | Load on **phone, cellular data, wifi off** | Loads. Different resolver path, this is the important one |
| +3 hr | dnschecker.org, A record | Green nearly everywhere |
| Next morning | Load the site, then check the A record again | Both clean |
| +24 hr | Load a deep link: `michelleblomberg.com/render` | Loads |

**Watch for exactly one thing:** `DNS_PROBE_FINISHED_NXDOMAIN`. That is the old symptom. A 404 or a cert warning is a different, less serious problem.

**Decision rule:** zero failures in 24 hours means the domain is safe to keep on the resume. Any NXDOMAIN means fall back to `singletrackmom.github.io` and consider Cloudflare.

---
---

# ORIGINAL JULY WRITE-UP, kept for reference

**Goal at the time:** Get a second opinion from Gordon on why michelleblomberg.com resolved intermittently.

**Status at the time:** Unresolved as of July 13, 2026.

## The setup

- **Domain:** michelleblomberg.com
- **Registered:** July 9, 2026
- **Registrar:** Network Solutions
- **Authoritative nameservers:** `ns39.worldnic.com` (162.159.26.212), `ns40.worldnic.com` (162.159.27.146)
- **Site:** GitHub Pages, repo `singletrackmom/singletrackmom.github.io`

**DNS records as configured (still correct today, do not change these):**

| Type | Host | Value |
|---|---|---|
| A | `@` | 185.199.108.153 |
| A | `@` | 185.199.109.153 |
| A | `@` | 185.199.110.153 |
| A | `@` | 185.199.111.153 |
| CNAME | `www` | singletrackmom.github.io |

That is the standard, correct GitHub Pages apex plus www configuration.

## The symptom

`michelleblomberg.com` flipped between working and not working, minutes apart, with no configuration change. When it failed, Chrome returned `DNS_PROBE_FINISHED_NXDOMAIN`, which means the DNS system affirmatively answered "this domain does not exist."

Observed across a laptop on home wifi, a phone on cellular, and a colleague on a different ISP. So not a local cache and not the router.

## Evidence collected in July

1. **The `www` CNAME record was healthy worldwide.** dnschecker.org showed green from every resolver.
2. **The apex CNAME lookup showed all red X, and this is a red herring.** An apex domain cannot have a CNAME record (RFC 1034). That is exactly why GitHub Pages requires four A records at the apex. The X's mean "no CNAME here," which is correct. Network Solutions support pointed at this check. It proves nothing. Do not chase it.
3. **The apex A records were correct and visible globally** when queried via DNS-over-HTTPS.
4. **But whatsmydns showed roughly a third of global resolvers returning nothing** for the A record. A correctly served zone answers everywhere.
5. **WHOIS was clean.** No `clientHold`, no suspension, nameservers correct at the registry.
6. **The site itself was up.** GitHub Pages served fine whenever DNS resolved.

## The July theory, which held up

**One of the two authoritative nameservers was intermittently answering NXDOMAIN for a zone correctly published on the other.**

Reasoning:
1. **It could not be GitHub.** NXDOMAIN is issued at the DNS layer; the browser never receives an IP and never contacts GitHub. A GitHub fault surfaces as a 404, a TLS error, or a timeout, never as "this domain does not exist."
2. **It was not local cache.** Reproduced on cellular and on a separate ISP.
3. **It was not propagation.** Propagation is monotonic. A propagated domain does not un-propagate.
4. **It was not a registry hold.** WHOIS showed none.
5. **The minute-scale flapping ruled out negative caching.** The SOA negative TTL of 3600 would have kept it dark for a full hour per bad answer. It recovered in minutes, meaning each lookup got a live answer and those answers contradicted each other.
6. **A per-query coin flip between two disagreeing nameservers produces exactly this pattern.**

## The test that would have confirmed it

```
dig @ns39.worldnic.com michelleblomberg.com A +norecurse
dig @ns40.worldnic.com michelleblomberg.com A +norecurse
```

Network Solutions never ran it. In August the DNS-over-HTTPS equivalent showed both servers answering correctly, so the condition had cleared.

## What Network Solutions said, and why it did not hold up

| Their answer | Why it was wrong |
|---|---|
| "Wait for propagation, up to 48 hours." | Four days had elapsed. Records were already visible globally. Propagation does not oscillate. |
| "Check with GitHub." | NXDOMAIN is returned before the browser ever contacts GitHub. |
| "Look at this CNAME checker." | They pointed at the apex CNAME check, which correctly shows nothing, because apex domains cannot have CNAMEs. Irrelevant. |


---

# Appendix B · The verification method and the 24-hour soak test

## What changed since July

Last month the working theory was that one worldnic nameserver served the zone and the other returned NXDOMAIN, making every lookup a coin flip. That theory looks correct, and it also looks **resolved**.

Tested tonight using DNS-over-HTTPS, which reports which authoritative server answered:

| Nameserver | IP | Result |
|---|---|---|
| ns39.worldnic.com | 162.159.26.212 | `Status: 0` NOERROR, all four GitHub A records |
| ns40.worldnic.com | 162.159.27.146 | `Status: 0` NOERROR, all four GitHub A records |

SOA serial `126071214` consistent across both. The two servers agree, which is the condition that was failing.

**Honest limits of that test:** it is a sample taken at one moment, it goes through a recursive layer rather than querying each nameserver directly the way `dig @ns39` would, and the site itself did not load end to end (explained by the missing CNAME file, but not proven). Hence the soak test below.

**Second, independent problem found tonight:** the `CNAME` file had been removed from the repo. Without it GitHub Pages does not claim the domain, so even perfect DNS would fail. That file is now restored.

---

## Steps tonight

1. **Push the repo.** The `CNAME` file containing `michelleblomberg.com` is already saved and will appear in GitHub Desktop with the other changes.

2. **Confirm DNS records at Network Solutions.** They should already be correct; verify nothing drifted. Four A records on `@`:
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`

   One CNAME on `www` pointing to `singletrackmom.github.io`

   Do **not** add a CNAME on `@`. An apex domain cannot hold one. The red X on that check is correct and is a red herring.

3. **Re-attach the domain in GitHub.** Repo → **Settings** → **Pages** → **Custom domain** → type `michelleblomberg.com` → **Save**. Wait for the green DNS check.

4. **Wait for the certificate**, then tick **Enforce HTTPS**. Usually minutes; can take up to an hour. If the box is greyed out, the cert is still issuing. Leave it and come back.

---

## The 24-hour soak test

Check at roughly these intervals. Any single failure means it is still flapping and the domain does not go on the resume.

| When | Test | Pass looks like |
|---|---|---|
| +15 min | Load `https://michelleblomberg.com` | Site loads, padlock, no warning |
| +15 min | Load `https://www.michelleblomberg.com` | Redirects to the apex, loads |
| +1 hr | Load on **phone, cellular data, wifi off** | Loads. Different resolver path, this is the important one |
| +3 hr | dnschecker.org → A record → `michelleblomberg.com` | Green nearly everywhere |
| +8 hr | Reload the site in a fresh private window | Loads |
| Next morning | Load site, then dnschecker A record again | Both clean |
| +24 hr | Load one deep link: `michelleblomberg.com/render` | Loads |

**Watch for the specific failure:** `DNS_PROBE_FINISHED_NXDOMAIN`. That is the old symptom. A 404 or a cert warning is a different, less serious problem.

---

## Decision rule

- **Zero failures in 24 hours** → swap the resume and cover letter to `michelleblomberg.com` links. Tell me and I will rebuild the PDF.
- **Any NXDOMAIN** → the flap is back. Keep `singletrackmom.github.io` on all materials and move DNS to Cloudflare, which removes worldnic from the path entirely. Free, domain stays registered at Network Solutions, only the two nameserver records change.

**Until the soak passes, every application ships with `singletrackmom.github.io`.** It is guaranteed live. A working plain URL beats a pretty broken one on a design application.

---

## If you call Network Solutions again

The one question worth asking, which nobody has answered yet:

> "Please run `dig @ns39.worldnic.com michelleblomberg.com A` and `dig @ns40.worldnic.com michelleblomberg.com A` and tell me whether both return the four A records with the authoritative answer flag, and whether the SOA serial matches on both. I am not asking about propagation and not asking about GitHub."

If they say "wait for propagation" or "check with GitHub," those answers do not apply. Propagation does not oscillate, and NXDOMAIN is returned before a browser ever contacts GitHub.


---

# Appendix C · How DNS actually works, the primer

Written in July so the pulldown menu on DNS Checker stops being a mystery. The reasoning here is still correct and is the fastest way back up to speed.

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
