# Render Backend Options (decision doc)

**The problem in one line:** Render's front-end is built. What is missing is a small **backend** so (1) each student logs in and their data persists across any computer, and (2) Render's AI runs on one shared, secret API key. Both needs are solved by the same small piece.

## Three things that get mixed up (keep them separate)
1. **Render's AI** runs on **one Anthropic API key** (pay-as-you-go), held on a server, shared by the whole class. You do not buy 24 of anything for this.
2. **Student logins + saved data** need a **backend** (authentication + a database). This is the missing piece.
3. **A student's own Claude account** is a separate, third thing, only used if they run their personal career agent in their own chat later. It does NOT power Render.

## Why a backend is required (your two worries, answered)
- **"School computers do not save permanently."** Right, browser localStorage gets wiped and does not follow the student. A **database** stores each student's data under their login, so it follows them to any machine and survives a wiped lab computer.
- **The API key cannot live in the page.** If the Claude key is in the HTML/JS, anyone can view-source and steal it. It must sit on a **server**. That same server can also handle logins and storage. So one small backend solves both problems at once.

---

## Option A (recommended): keep Render's front-end, add Supabase
- **What:** Supabase gives you a hosted database + email/password login out of the box, plus serverless "edge functions" that hold the Claude API key and make the AI calls for you.
- **Student experience:** each student signs up with an email and password; their Render data saves to the cloud and follows them to any computer.
- **The API key:** lives inside the edge function, never in the page; every student's AI call goes through it on one pooled key, so you only pay for what is used and dropouts cost nothing.
- **Effort:** moderate, and you KEEP all the Render UI you already built. You wire "save/load" to Supabase and route the AI calls through an edge function.
- **Privacy:** you control the data; keep sending no PII to the AI (unchanged). Student records live in your Supabase project, which is FERPA-manageable, confirm specifics with the district.
- **Cost:** Supabase free tier likely covers a 24-student class; Claude API usage is pay-as-you-go and small for text tasks.

## Option B: rebuild in an app builder (Lovable, Bolt, Replit)
- **What:** these tools generate a full app (front-end + backend + login + database) from prompts. Lovable and Bolt typically use Supabase under the hood, so this is really Option A with the wiring auto-generated.
- **Pro:** fastest path to a working backend if you are happy to rebuild the interface in their tool; less hand-wiring.
- **Con:** you would re-create Render's polished UI in their framework, trading your hand-built front-end for their generated one, with some platform lock-in.
- **Honest note on "is Lovable better than Claude":** it is not better or worse, it is a *different kind of tool*, an app builder with a backend baked in. Underneath it is the same Supabase-style backend as Option A. Choose it if you would rather one tool generate everything than keep and extend what you have.
- **Cost:** a subscription to the builder, plus the same database and API costs.

## Option C (stopgap for the Fall pilot, least work): proxy + Save/Load, no accounts yet
- **What:** no accounts or database. Students keep using Save-to-File / Load-from-File (the JSON export/import already in Render) to move their data. You add only a tiny serverless proxy (a Cloudflare Worker or a Vercel function) so the shared API key is off the page.
- **Pro:** minimal work, fine for a small first pilot.
- **Con:** data still does not auto-persist on shared lab machines, students must save and reload their file each session. Not a long-term answer.
- **When:** if you want to pilot in Fall 2026 before committing to the full backend, then migrate to Option A.

---

## Your specific questions, answered
- **"If each student has a Claude account, will this help?"** Not for Render itself (Render runs on the API key). Student Claude accounts only matter for them running their own agent in their own chat later.
- **"Can we have one API account they each log into?"** One API key powers Render's AI for everyone, server-side. Their logins are a separate backend feature (Option A or B). Do not buy 24 separate accounts.
- **"Can we have internal agents in the tool?"** Yes. Render already calls the API for internal AI functions (job analysis, gap analysis, cover-letter help, etc.). With a backend you could later add scheduled or daily ones.
- **"School computers do not save permanently, can we fix that?"** Yes, with the database in Option A or B (data follows the login). Option C only mitigates it with manual save/load.
- **"Should I switch to Lovable?"** That is Option B, a valid path. It is mainly a rebuild-versus-keep decision, the backend underneath is the same.

## Recommendation
- **Long term:** Option A, keep your Render front-end and add Supabase auth + database + a small edge-function API proxy. Most capability for the least rework, and you keep your design.
- **Fast Fall 2026 pilot:** you can start with Option C (proxy + save/load) and migrate to A after the pilot proves the course.
- I can prototype the Supabase login + a Claude API proxy whenever you want to start.

## One thing to confirm with the district (Sonal / Jordan)
Where student records may legally live under FERPA: a Supabase project you control, versus a Maricopa-hosted database option. This decides where Option A's data sits, worth asking before building.
