# CopaMigo, Hosting + API Options to a Pilot

**For:** Michelle Blomberg, solo builder, no institutional pilot support
**Goal:** move CopaMigo off the personal GitHub, ideally onto a Maricopa (work) GitHub org, and let it call an AI model safely, with the credential server-side and never in the browser.
**Written:** July 2026

---

## 1. Where CopaMigo actually stands today

I read the live tool before writing this, so the recommendation is grounded in the real code, not the PRD's aspiration.

- **It is a single static HTML page.** `copamigo/index.html` is vanilla JavaScript, no framework, no backend, hosted on GitHub Pages. That part is exactly what the PRD (`copamigo/prd.html`) describes.
- **It calls the model directly from the browser, with the key baked into the page.** Line 568 of `copamigo/index.html` holds the Anthropic key as an obfuscated character-code array (`[115,107,45,...].map(c=>String.fromCharCode(c)).join('')`), and line 1792 does `fetch('https://api.anthropic.com/v1/messages', ...)` with that key in the `x-api-key` header. Obfuscation is not protection: anyone who opens the page source or the network tab can read the key. The PRD already names this as "the one thing that must change before a student uses the tool."
- **This is the whole problem to solve.** A key in a static page is a *published* key. That is a property of the delivery model, and the Dial Your Course PRD (`course-dialer/prd.html`, section 6, "Is the model swappable") says the same thing: "a credential cannot reside in the client... this is not mitigable by obfuscation."

**The Dialer's escape hatch does not work for CopaMigo.** Dial Your Course can use the "bridge" pattern: the page composes a prompt, a *faculty member* pastes it into a sanctioned model, and pastes the reply back. No server, no key. That is fine for one instructor reviewing their own course. It is impossible for CopaMigo, because CopaMigo's users are **anonymous students** who will never paste anything into a second tool. A student-facing tool that calls a model needs a **real server-side key behind a proxy.** There is no no-infrastructure shortcut here. That is the single fact that shapes every option below.

**The privacy posture that must survive any move:** no PII, no login, no MEID, no name, no student record. The only thing that leaves the browser is the question text and the answer, with no identity attached. Any hosting choice has to keep that line: the proxy stays stateless, logs only anonymous routing counts, and retains no conversation text. That rules out any option that forces an account, a login, or a stored transcript on the student.

---

## 2. The shape of the fix (true for every option)

Every workable path is the same architecture:

```
Student's browser (static page)  ──HTTPS──►  a small server-side "proxy"
   no key, no PII                             holds the ONE key as a secret
                                              adds the system prompt
                                              calls Claude/Gemini
                                              returns only the answer text
```

The static frontend can live on **GitHub Pages under a Maricopa org** (or anywhere). It calls the proxy with `fetch()`. The proxy is the only thing that knows the key. The choices below are really just *"who runs that little proxy, and how hard is it to stand up."*

Two things every proxy must do so the browser can call it:
1. **Store the key as a secret** (an environment variable / secret store), never in code that ships to the browser.
2. **Send CORS headers** (`Access-Control-Allow-Origin`) so the GitHub Pages domain is allowed to call it, and answer the preflight `OPTIONS` request.

---

## 3. The options

### 3a. GitHub Pages on a Maricopa / work GitHub org (the frontend home)

**What it is:** the same static hosting the tool uses now, but under a `github.com/<maricopa-org>` account instead of the personal `singletrackmom` one. Organization Pages work the same as user Pages.

**The catch:** GitHub Pages is **static-only. It cannot hold a secret and cannot run server code.** So Pages is never the whole answer for CopaMigo, it is only the *frontend*. The API key has to live in a companion piece (one of the proxies in 3b–3d). Pages serves the HTML/JS; the JS calls the proxy.

**Anonymous student-facing?** Yes, that is what Pages is for, public static pages.

**Cost:** free for public repos. (Private-repo Pages needs a paid GitHub plan; not needed here since the page has no secrets.)

**Effort/skill:** trivial, she already does this.

**Privacy fit:** perfect. Static page holds nothing.

**The real question is org control, not tech.** Moving the *repo* to a Maricopa org means someone at Maricopa with org-admin rights adds her and lets her create/transfer the repo. If that governance door is not open (and "no pilot support" suggests it may not be), she can still get off her *personal* GitHub by creating a **separate, plain personal-but-project GitHub account/org** or a new org she owns, which at least separates CopaMigo from her portfolio site. The Maricopa org is the ideal; a clean separate namespace she owns is the fallback that is fully in her control today.

**Pros:** free, familiar, keeps the exact current frontend.
**Cons:** provides zero backend, so it is always half of a two-part answer. Getting onto the *Maricopa* org depends on district IT cooperation she does not currently have.

*Sources:* [GitHub Pages docs](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)

---

### 3b. Serverless function proxies she owns (the key lives server-side)

These are the "most portable, institution-ready" answers. She writes ~30 lines of proxy code, deploys it, sets the key as a secret, and points the Pages frontend at it. She owns the code and can move it to district infrastructure later with almost no change. Four candidates:

#### Cloudflare Workers  ★ top serverless pick
- **What:** a tiny JavaScript function on Cloudflare's edge. You deploy one file that receives the student's question, adds the system prompt, calls Claude/Gemini with the key, returns the answer.
- **Secret storage:** `wrangler secret put ANTHROPIC_API_KEY`. Secrets are encrypted and are **not visible in the dashboard or CLI after you set them.** They reach the Worker as a variable; nothing ships to the browser.
- **CORS:** you add the `Access-Control-Allow-Origin` header in the Worker and handle the `OPTIONS` preflight. A few lines.
- **Anonymous student-facing?** Yes. No account required of the student.
- **Free tier:** **100,000 requests/day**, 10 ms CPU per request. For a pilot at one college that is enormous headroom, effectively free.
- **Effort/skill:** moderate. Node/`wrangler` CLI, one deploy. She vibe-codes, so this is within reach; it is the steepest of the "she owns it" options but the most robust.
- **Privacy fit:** excellent. Stateless, logs nothing unless you tell it to, key encrypted.
- **Pros:** generous free tier, fast, the most professional/portable result, resume-worthy ("I own the proxy"). Nothing about it is proprietary.
- **Cons:** a real dev toolchain (CLI, deploy), a Cloudflare account, more moving parts than Apps Script.

*Sources:* [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/), [Workers secrets](https://developers.cloudflare.com/workers/configuration/secrets/), [Workers limits](https://developers.cloudflare.com/workers/platform/limits/)

#### Google Apps Script  ★ fastest, most familiar
- **What:** a script published as a web app. `doPost(e)` receives the question, `UrlFetchApp.fetch()` calls the model, returns the answer. **She already runs Apps Script relays for Render and Rough Cut,** so this is the shortest path from what she knows.
- **Secret storage:** `PropertiesService` Script Properties hold the key out of the code.
- **CORS:** Apps Script server-to-server calls are *not* CORS-restricted (server to Anthropic is fine). The wrinkle is the *browser to Apps Script* leg: a published web app returns permissive access, but Apps Script does not let you set arbitrary CORS headers cleanly, so the usual pattern is a "simple" POST (often `text/plain` content type to dodge preflight) and parse JSON server-side. This is a known, solved annoyance, the same shape as her existing relays.
- **Anonymous student-facing?** Yes, publish "execute as me, access: anyone." Student needs no Google login.
- **Free tier:** free with a Gmail/Workspace account. `UrlFetchApp` has a **daily quota** (roughly 20,000 calls/day on consumer accounts, higher on Workspace). Fine for a pilot; not unlimited.
- **Effort/skill:** **lowest.** She has literally done this twice already.
- **Privacy fit:** good, with one caveat: it runs on *her* Google account, not district infrastructure, so "data-sovereign" is true for the student (no PII, nothing stored) but the relay is her personal tenant, not Maricopa's. Log nothing and it stays clean.
- **Pros:** she can stand this up today, no new tool to learn, free.
- **Cons:** the CORS/preflight fiddliness, the daily quota ceiling, it lives on her personal Google account (portability to the district is a rewrite, not a copy), and executives may see "Apps Script relay on a personal Gmail" as prototype-grade, not production.

*Sources:* [Apps Script quotas](https://developers.google.com/apps-script/guides/services/quotas), [UrlFetchApp guide](https://justin.poehnelt.com/posts/definitive-guide-to-urlfetchapp/), [Claude API CORS note](https://simonw.substack.com/p/claudes-api-now-supports-cors-requests)

#### Netlify Functions
- **What:** a serverless function that deploys alongside static hosting. You can host the *frontend and* the proxy together on Netlify, or keep the frontend on Pages and use Netlify only for the function.
- **Secret storage:** environment variables, with a "Secrets Controller" for stricter handling. Note the AWS-Lambda 256-character cap on env-var values (Anthropic keys fit).
- **Bonus:** Netlify now ships an **AI Gateway**, it auto-injects `ANTHROPIC_API_KEY`/`ANTHROPIC_BASE_URL` and proxies to Claude/OpenAI/Gemini, so you may not even manage your own key for prototyping. Convenient, but it is *their* gateway in the path, which is a data-flow question for a student tool; prefer your own key + your own function to keep the data path clean.
- **CORS:** you set headers in the function. Straightforward.
- **Free tier:** the free plan is now **credit-based (300 credits/month, hard cap, no overage)**; functions/requests draw from that pool. Watch the "one project over limit pauses *all* your projects" behavior. Enough for a small pilot, but the metering is less transparent than Cloudflare's flat 100k/day.
- **Effort/skill:** moderate, similar to Cloudflare, arguably a touch simpler if you host the whole thing on Netlify.
- **Privacy fit:** good if you use your own key and log nothing.
- **Pros:** frontend + backend in one place, decent DX.
- **Cons:** the credit model is fiddly to reason about; the account-wide pause is a real gotcha; the AI Gateway convenience puts a third party in the path unless you opt out.

*Sources:* [Netlify pricing](https://www.netlify.com/pricing/), [Netlify function env vars](https://docs.netlify.com/build/functions/environment-variables/), [Netlify AI Gateway](https://docs.netlify.com/build/ai-gateway/overview/)

#### Vercel Functions
- **What:** same idea as Netlify, serverless function next to static hosting.
- **Secret storage:** environment variables per project.
- **Free tier:** Hobby plan, ~150,000 function invocations/month, 4 CPU-hours, 60-second timeout.
- **The disqualifier:** **the Hobby (free) plan is non-commercial, personal use only.** A tool serving a *college's* students is arguably institutional/commercial use, which Vercel's terms say needs the paid Pro plan. For an official student-facing pilot that is a licensing risk not worth taking. **Not recommended for CopaMigo** on the free tier; fine only for private testing.
- **Privacy fit:** technically fine, but the terms problem overrides.
- **Pros:** good DX.
- **Cons:** free tier's non-commercial restriction makes it the wrong fit for a college pilot.

*Sources:* [Vercel Hobby plan](https://vercel.com/docs/plans/hobby), [Vercel function limits](https://vercel.com/docs/functions/limitations)

---

### 3c. Lovable (the AI app builder)

**What it is in 2025–2026:** a "vibe-coding" AI app builder. You describe the app in prompts and it generates a real **React + Vite + Tailwind** codebase, with a native **Supabase** integration for database/auth and a GitHub sync. It also *hosts* the result (preview URL, custom domains on paid).

**Does it give you a server-side key?** Yes, this is the important part. Through its Supabase integration, **secrets are stored in the Supabase project and read by Supabase Edge Functions; they never appear in the app's client code or repo, and Lovable itself does not read the secret values back.** So an LLM API key can live server-side in an Edge Function, exactly the proxy pattern CopaMigo needs. Lovable can absolutely wire up "student asks → Edge Function calls the model → answer returns" without exposing the key.

**Can it call an LLM API?** Yes, via the Edge Function it generates (or its own AI features). You point the function at Claude or Gemini.

**Portability (can she own it and leave?):** **Yes, and this is Lovable's best trait.** It generates conventional, exportable React/TypeScript on Supabase, not a locked proprietary format. You can push to GitHub, export, self-host, or hand it to engineers. There are even community tools to migrate Lovable Cloud data to a standalone Supabase project. So using Lovable does *not* trap her.

**Cost:** free tier is ~5 credits/day (up to ~150/month), enough to prototype. Pro is **$25/month** (100 credits + custom domain + private projects). Business $50/month adds SSO and data opt-out.

**Anonymous student-facing?** Yes, if you design it that way (no forced login). You must deliberately keep the no-PII posture, Lovable will happily add Supabase auth and a user table if you let it, which is the opposite of what CopaMigo wants. The discipline is on you.

**Privacy fit:** workable but requires care. The key stays server-side (good). The risk is *scope creep*: Lovable's default instinct is to add accounts, databases, and stored data. To keep the data-sovereign line you must tell it to store no conversation text and collect no student identity, and verify what the generated Edge Function logs.

**Pros:** **fastest path to a hosted, backed, key-safe app** if she wants to rebuild the UI; server-side secrets solved for her; genuinely portable code she owns; low cost. Good for a quick, credible-looking pilot.
**Cons:** it wants to rebuild CopaMigo as a React app (her current tool is one hand-tuned HTML file with carefully worded system prompts and 100+ verified links, all of which she'd migrate/re-verify); the platform pushes toward accounts/data that violate the no-PII posture unless firmly steered; monthly cost for the useful tier; hosting sits with a startup vendor until she exports.

*Sources:* [Lovable + Supabase integration](https://docs.lovable.dev/integrations/supabase), [Lovable review 2026](https://www.nocode.mba/articles/lovable-ai-app-builder), [Supabase for AI builders](https://supabase.com/solutions/ai-builders)

---

### 3d. Supabase (backend-as-a-service) with Edge Functions, paired with a static or Lovable frontend

**What it is:** the backend under Lovable, usable on its own. A Supabase project gives you **Edge Functions** (Deno/TypeScript serverless functions) plus a secret store. You keep the current static `index.html` on GitHub Pages and add *one* Edge Function as the proxy. This is the "serverless proxy she owns" pattern (like Cloudflare) but on Supabase, and it is the natural graduation path if she ever does want a database later.

**Secret storage:** Supabase project secrets, read in the Edge Function via Deno env vars. Not shipped to the browser.

**CORS:** you set headers in the function; standard.

**Anonymous student-facing?** Yes. You do *not* have to enable auth. Keep it a bare function.

**Free tier:** **500,000 Edge Function invocations/month**, 2s CPU per request. Ample for a pilot. (Free projects pause after ~1 week of inactivity, a minor operational note.)

**Effort/skill:** moderate, comparable to Cloudflare, Deno/TypeScript.

**Privacy fit:** excellent if you use only the Edge Function and store nothing. Supabase *can* store data, but you are not obligated to; a lone function retains nothing.

**Pros:** very generous free tier, real infrastructure, owns-it-and-portable, and it is the same backend Lovable uses so you can start hand-rolled and adopt Lovable's UI later (or vice versa). A clean, credible answer.
**Cons:** another account/toolchain; the "it's a database company" framing may tempt scope creep toward storing data; free-tier project pausing.

*Sources:* [Supabase Edge Functions](https://supabase.com/docs/guides/functions), [Edge Function secrets](https://supabase.com/docs/guides/functions/secrets), [Edge Function limits](https://supabase.com/docs/guides/functions/limits)

---

### 3e. The district-hosted / sanctioned-API path (the "right" long-term answer)

**What it would require:** Maricopa (or GCC) stands up a **server-side proxy on district infrastructure** holding **one institutional credential**, a Claude for Education account, or, given the district is standardizing on Google Gemini, a **Gemini endpoint on Vertex AI** inside the district Google Cloud project. The proxy authenticates through existing single sign-on if desired (though for an anonymous student tool, no login is the point), forwards the question, returns the answer, and rotates the key on the standard schedule. The CopaMigo frontend then points at that district URL instead of a personal proxy. Because every AI call already runs through one request function, moving providers is "change the endpoint, the auth header, and the response-parse shape," not a rebuild (the PRD's "Moving from Claude to Gemini" section covers exactly this).

**Why it is blocked right now:** there is **no institutional pilot support.** A district proxy needs a cloud project, an owned endpoint, a data-handling position, and IT time, none of which is on offer today. This is the same wall the Dialer PRD calls "the institutional ask," requested only *with pilot evidence behind it, never in advance of any.*

**The minimal ask if the door ever opens:** one sanctioned endpoint reachable from a district-controlled proxy (Vertex AI if the district has a Google Cloud project, *not* the end-user Gemini-in-Workspace surface, which exposes no programmable endpoint), one server-side credential rotated normally, and a one-line data-handling position: *only the anonymous question text is sent, nothing is stored, no PII exists to govern.* Because CopaMigo sends no student data by design, that data-handling review is unusually short, which is the argument to lead with.

**Pros:** the only path that is truly data-sovereign on *district* infrastructure, scales past a pilot, and satisfies procurement. It is the destination.
**Cons:** not available now; depends entirely on someone at the district funding a proxy. You cannot pilot on it, which is why you need one of the above to *produce the evidence* that unlocks it.

---

## 4. Ranked recommendation for Michelle's exact situation

Her constraints: solo, no pilot support, wants off personal GitHub, needs a real server-side key (no bridge possible), bilingual anonymous student-facing, must stay no-PII and data-sovereign, and wants a result that is credible to district IT later.

The honest tension is **fastest-to-a-pilot** vs **most-portable/institution-ready.** These pull in different directions, so here is a ranked path that gets a pilot up quickly *without* building something she has to throw away.

### #1 (recommended): Keep the static frontend, add a Cloudflare Workers proxy she owns
Frontend stays the current hand-tuned `index.html` (moved to a GitHub org she controls, Maricopa if the door opens, a clean separate namespace if not). The key moves into a **Cloudflare Worker** she owns: 100k requests/day free, encrypted secret, stateless, logs nothing. This is the best balance: it is a small, well-scoped build (not a UI rewrite), it kills the exposed-key problem the right way, it keeps every carefully-worded prompt and verified link exactly as they are, and the result is *portable and professional*, when the district proxy path opens, she reconfigures one endpoint and the architecture is already correct. It is also the most defensible thing to show the Maricopa AI CIO: "the credential is already off the client, on infrastructure I own, and it moves to yours by changing a URL."

**Why not Apps Script as #1, given it's more familiar?** Because Apps Script lives on her *personal Google account*, has a lower daily quota, and reads as prototype plumbing to an IT reviewer. Cloudflare is barely more work and produces an institution-ready result. But see the fallback.

### #2 (fastest, use if she wants a pilot live this week): Google Apps Script proxy
She has built this exact pattern twice (Render, Rough Cut). Publish a web app, store the key in Script Properties, `UrlFetchApp` to Claude, handle the simple-POST/CORS shape she already knows. Live in an afternoon, free. Accept that it sits on her personal Google account and has a daily quota, both fine for a bounded one-college pilot, and plan to graduate to #1 (or the district proxy) before any wide rollout. **This is the pragmatic pick if the choice is "a working pilot on Apps Script now" vs "a perfect Worker in three weeks."**

### #3 (if she wants to modernize the whole app): Supabase Edge Function, optionally with a Lovable-rebuilt UI
If she ever decides to rebuild CopaMigo's UI (React, nicer to maintain), do it on **Supabase Edge Functions** (500k invocations/month free, key server-side), and optionally use **Lovable** to generate the frontend fast, then export the code so she owns it. Powerful and future-proof, but it is a bigger lift than #1/#2 and invites the exact account/data scope-creep the no-PII posture forbids, so only take this if UI modernization is a goal in itself, not just to fix the key.

### Avoid for this tool: Vercel free tier
Its Hobby plan is non-commercial-only; a college student tool is the wrong side of that line. Fine for private testing, not for an official pilot.

### The destination (not a pilot option): district proxy on Vertex AI / Claude for Education
This is where it should end up. You cannot start here (no pilot support), but #1 is deliberately built so the move is a one-endpoint change. Lead the eventual ask with the short data-handling story: no PII, nothing stored, only anonymous question text sent.

---

## 5. Concrete next steps

**For #1 (Cloudflare Worker, recommended):**
1. Create a free Cloudflare account and install the `wrangler` CLI.
2. Write a ~30-line Worker: read the POSTed question, add CopaMigo's system prompt, call `api.anthropic.com/v1/messages` with the key, return only the answer. Add `Access-Control-Allow-Origin` for the Pages domain and handle `OPTIONS`.
3. `wrangler secret put ANTHROPIC_API_KEY` to store the key encrypted.
4. In `copamigo/index.html`, delete the char-code key array (line 568) and change the `fetch` on line 1792 from `api.anthropic.com` to the Worker URL. The browser now holds nothing.
5. Move the repo to the GitHub org she controls (Maricopa if available; otherwise a clean separate namespace off her personal portfolio).
6. Rotate/replace the currently-exposed Anthropic key immediately, since it has been public in the page.

**For #2 (Apps Script fallback, if she wants it live now):**
1. New Apps Script project, `doPost(e)` calls the model via `UrlFetchApp`, key in `PropertiesService`.
2. Deploy as a web app, "execute as me, access: anyone."
3. Point `index.html`'s fetch at the web-app URL, remove the embedded key, using the same simple-POST shape as her Render/Rough Cut relays.
4. Same key rotation step.

**Do first, regardless of option:** rotate the Anthropic key that is currently sitting in the published page. It should be treated as compromised.

---

## 6. One-line summary

Move CopaMigo's frontend to a GitHub org she controls and put the API key behind a small server-side proxy she owns, a **Cloudflare Worker** for the portable, institution-ready result, or a **Google Apps Script relay** (which she already knows) for the fastest pilot, keeping the tool stateless and no-PII so it can later repoint to a district Vertex AI / Claude for Education proxy with a single endpoint change. Avoid Vercel's non-commercial free tier for a student pilot, and rotate the currently-exposed key now.
