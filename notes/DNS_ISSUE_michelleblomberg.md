# michelleblomberg.com: intermittent NXDOMAIN

**Goal:** Get a second opinion from Gordon on why michelleblomberg.com resolves intermittently, and whether the diagnosis below is right before I escalate further with Network Solutions.

**Audience:** Gordon (programmer, uses GitHub regularly). Also me, so I stop re-explaining this from scratch.

**Process:** Symptoms observed over three days, records verified against public resolvers, authoritative data pulled via DNS-over-HTTPS, plus a working theory and the specific test that would confirm or kill it.

**Status:** Unresolved as of July 13, 2026. Network Solutions has not yet run the one query that settles it.

---

## The setup

- **Domain:** michelleblomberg.com
- **Registered:** July 9, 2026 (four days old)
- **Registrar:** Network Solutions
- **Authoritative nameservers:** `ns39.worldnic.com` (162.159.26.212), `ns40.worldnic.com` (162.159.27.146)
- **Site:** GitHub Pages, repo `singletrackmom/singletrackmom.github.io`
- **CNAME file in repo:** `michelleblomberg.com`
- **Enforce HTTPS:** on (cert issued successfully)

**DNS records as configured:**

| Type | Host | Value |
|---|---|---|
| A | `@` | 185.199.108.153 |
| A | `@` | 185.199.109.153 |
| A | `@` | 185.199.110.153 |
| A | `@` | 185.199.111.153 |
| CNAME | `www` | singletrackmom.github.io |

That is the standard, correct GitHub Pages apex + www configuration.

---

## The symptom

`michelleblomberg.com` **flips between working and not working, minutes apart**, with no configuration change in between.

When it fails, Chrome returns:

```
DNS_PROBE_FINISHED_NXDOMAIN
This site can't be reached
```

NXDOMAIN means the DNS system is affirmatively answering **"this domain does not exist."** Not a timeout. Not a server error. A denial that the name is registered at all.

Observed across:

- My laptop on home wifi
- My phone on **cellular** (completely different resolver path)
- A colleague on a different ISP entirely

So it is not my local DNS cache, and not my router. Multiple independent networks see it.

**Timing:** it was up, then down within about five minutes, then up again. Fast. Minute-scale, not hour-scale.

---

## Evidence collected

### 1. The `www` CNAME record is healthy worldwide

dnschecker.org, CNAME lookup on `www.michelleblomberg.com`: **green check from every resolver tested**, all returning `singletrackmom.github.io.`

Confirmed resolving: Google, Quad9 (Berkeley), OpenDNS (San Francisco), NextDNS (Wilmington), VeriSign (Virginia), Quad9 (San Francisco), NeuStar (Ashburn), and more.

**The record is published and propagated.**

### 2. The apex CNAME lookup shows all red X, and this is a red herring

dnschecker.org, CNAME lookup on `michelleblomberg.com` (no www): red X across the board.

**This is expected and correct.** An apex domain cannot have a CNAME record. That is a DNS protocol rule (RFC 1034), which is exactly why GitHub Pages requires four A records at the apex instead. The X's mean "no CNAME here," which is the right answer.

Network Solutions support pointed me at this check. It proves nothing. Do not chase it.

### 3. The apex A records are correct and visible globally

Queried via Google DNS-over-HTTPS:

```
michelleblomberg.com  A  185.199.108.153  (TTL 3600)
michelleblomberg.com  A  185.199.109.153
michelleblomberg.com  A  185.199.110.153
michelleblomberg.com  A  185.199.111.153
Status: 0 (NOERROR)
```

Cross-checked on nslookup.io against Cloudflare's resolver: same four A records, correct NS records, no stray AAAA, no stray CNAME, no TXT.

### 4. But whatsmydns showed roughly a third of global resolvers returning **nothing** for the A record

Resolving fine: New York, Dallas, Atlanta, Boston, Alabama, Canada, Brazil, Spain, France, Netherlands, Germany, South Africa, Russia, Pakistan, Singapore, South Korea.

Returning **no answer at all**: Mexico City, Turkey, India, Thailand, China, Adelaide, Melbourne.

A correctly served zone answers everywhere. This is inconsistent.

### 5. The SOA record

```
NS39.WORLDNIC.com. namehost.WORLDNIC.com. 126071214 10800 3600 604800 3600
```

Fields: serial `126071214`, refresh `10800`, retry `3600`, expire `604800`, **negative-cache TTL `3600`**.

### 6. WHOIS is clean

- Created July 9, 2026. Expires July 9, 2027.
- Domain status: `clientTransferProhibited` **only**. That is the ordinary registrar lock.
- **No `clientHold`, no `serverHold`, no suspension.**
- Nameservers present and correct at the registry.

So the domain is properly registered and properly delegated. Nothing is suspended.

### 7. The site itself is up

I have loaded `https://michelleblomberg.com` successfully from outside my network multiple times today, full content, valid cert. GitHub Pages is serving fine.

`singletrackmom.github.io` resolves green globally.

### 8. `www` redirects to the apex

Typing `www.michelleblomberg.com` bounces to `michelleblomberg.com`. **This is expected**, because the CNAME file in the repo says `michelleblomberg.com`, so GitHub treats the bare domain as canonical and 301s www to it.

Consequence: **there is no fallback.** When the apex is down, www dies with it, because www just redirects into the apex. Both addresses share the same single point of failure.

---

## The theory

**One of the two authoritative nameservers is intermittently answering NXDOMAIN for a zone that is correctly published on the other.**

Reasoning:

1. **It cannot be GitHub.** NXDOMAIN is issued at the DNS layer. The browser never receives an IP address, so it never opens a connection to GitHub at all. GitHub cannot cause a failure at a step it does not participate in. A GitHub fault would surface as a 404, a TLS error, or a timeout, never as "this domain does not exist."

2. **It cannot be my local cache.** It reproduces on cellular and on a colleague's separate ISP.

3. **It is not propagation.** Propagation is monotonic: records spread outward and stay. My domain is not gradually coming online, it is oscillating. A propagated domain does not un-propagate. Also, the records are demonstrably already visible worldwide (evidence 1 and 3).

4. **It is not a registry hold.** WHOIS shows no hold status (evidence 6).

5. **The minute-scale flapping rules out negative caching as the driver.** If a bad NXDOMAIN were simply being cached, the SOA negative TTL of 3600 would keep the domain dark for a full hour per bad answer. It recovers in minutes. That means each lookup is getting a **live** answer from an authoritative server, and those live answers are contradicting each other.

6. **A per-query coin flip between two disagreeing nameservers produces exactly this pattern.** Recursive resolvers alternate between `ns39` and `ns40`. If one serves the zone and the other denies it, then whether the site loads depends on which server that particular lookup happened to hit. Different people, and the same person minutes apart, get different answers. That is precisely what is happening.

**In one sentence: the zone appears to be published on one worldnic nameserver and not the other, so resolution is a coin toss.**

---

## The test that confirms or kills it

Query the apex against each nameserver **individually**:

```
dig @ns39.worldnic.com michelleblomberg.com A +norecurse
dig @ns40.worldnic.com michelleblomberg.com A +norecurse
```

- **Both return the four A records with the AA (authoritative answer) flag** → theory is wrong, look elsewhere (next suspects: the .com delegation, or an anycast node within worldnic's network serving stale data).
- **One returns NOERROR with the records, the other returns NXDOMAIN** → confirmed. Network Solutions needs to republish the zone to the failing server.

Also worth checking:

```
dig michelleblomberg.com SOA @ns39.worldnic.com
dig michelleblomberg.com SOA @ns40.worldnic.com
```

If the **serial numbers differ**, the two servers are out of sync and that is the smoking gun.

**Gordon: this is the query I need run.** I cannot run `dig` (no Terminal comfort, and my assistant's sandbox blocks outbound port 53). Network Solutions has refused to run it so far and keeps telling me to wait for propagation or check with GitHub.

---

## What Network Solutions has said, and why it does not hold up

| Their answer | Why it is wrong |
|---|---|
| "Wait for propagation, up to 48 hours." | Four days elapsed. Records already visible globally. Propagation does not oscillate. |
| "Check with GitHub." | NXDOMAIN is returned before the browser ever contacts GitHub. GitHub is serving the site correctly right now. |
| "Look at this CNAME checker." | They pointed me at the apex CNAME check, which correctly shows nothing, because apex domains cannot have CNAMEs. Irrelevant. |

---

## Options on the table

1. **Force Network Solutions to fix their nameservers.** Correct outcome, but I am not getting traction, and my site is unusable in the meantime.

2. **Move DNS hosting to Cloudflare** (free), keeping the domain registered at Network Solutions. Nothing about the site or the domain changes; only the two nameserver records at the registrar are swapped. Removes worldnic from the resolution path entirely. Takes a few hours to a day to propagate.

3. **Remove the custom domain from GitHub Pages** so `singletrackmom.github.io` serves directly, bypassing Network Solutions entirely. Instant, reversible, but I lose the custom domain temporarily, and it is already printed on my professional materials.

**Constraint:** michelleblomberg.com is on my resume and materials and is in active use during a job search. I need it working, not replaced.

---

## Gordon, the questions I actually need answered

1. Does the two-disagreeing-nameservers theory hold up, or am I missing a more likely cause?
2. Can you run the `dig` queries above against ns39 and ns40 and tell me whether they agree?
3. Is there anything about a four-day-old domain, or about Network Solutions / worldnic specifically, that would explain this?
4. Would moving DNS to Cloudflare actually fix it, or would I just be moving the problem?
