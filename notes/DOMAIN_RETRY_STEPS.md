# michelleblomberg.com: retry on Network Solutions, with a 24-hour soak test

**Goal:** get the custom domain live again without leaving Network Solutions, and prove it holds for 24 hours before it goes on a resume.

**Audience:** me, tonight and tomorrow.

**Process:** re-attach the domain in GitHub, then test on a schedule. Ship the resume with the github.io URL until the soak passes.

**Status as of Aug 16, 2026:** DNS verified healthy from BOTH nameservers. The blocker is now a missing CNAME file, which is fixed in the repo and waiting to be pushed.

---

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
