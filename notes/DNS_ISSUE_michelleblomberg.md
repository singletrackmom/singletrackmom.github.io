# michelleblomberg.com: SOLVED, August 16, 2026

> ## ✅ RESOLVED. Read this box before anything else.
>
> **The domain works. We did NOT move to Cloudflare. We did NOT change registrars. Network Solutions is still the registrar and worldnic is still hosting DNS.**
>
> **What actually fixed it:** the `CNAME` file was missing from the repo. Putting it back fixed everything. That file is not a nicety, **it IS the GitHub Pages custom-domain setting.** GitHub Pages reads the domain out of that file. The Settings → Pages box in the GitHub web UI is just a friendlier door to writing the same file.
>
> **If it breaks again, check the CNAME file first, before touching DNS.**
>
> Everything below the line is the original July diagnosis, kept because the reasoning was correct and may be useful if the flapping returns.

---

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

> "The domain is fixed. We never moved to Cloudflare and we are still on Network Solutions. The problem was that the CNAME file had been removed from the repo, and that file is the GitHub Pages setting. Read `notes/DNS_ISSUE_michelleblomberg.md`."


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
