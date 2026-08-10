# Render classroom pilot, request to District OIT

**Prepared by:** Michelle Blomberg, Residential Faculty, Digital Media Arts, Glendale Community College
**For:** District OIT (Gordon Inman and the OIT AI/security team)
**Date:** August 2026
**Status:** Permission and small-budget request for a bounded, one-semester classroom pilot

---

## What I am asking for, in one sentence

Permission to run a bounded classroom pilot of Render, a career-readiness web tool I built, in one or two of my AVC248 sections for a single semester, powered by one paid Google Gemini API key behind a small server-side proxy with a hard spend cap, and confirmation that the de-identified, no-PII design below satisfies district policy.

I am not asking OIT to build or maintain an application. I am asking whether I may run this pilot, ideally on a Gemini key OIT provisions so it sits under our district agreement, whether the data posture is acceptable, and how I am allowed to pay the small API cost.

---

## Goal, Audience, Process

**Goal.** Let students in a career course use an AI career assistant (resume help, job-posting analysis, cover-letter alignment, and a coaching "should I apply?" fit report) inside one tool, without any student handling an API key, creating an AI account, or exposing personal data. Prove the tool works with real students this term so a district-supported version can follow if it earns one.

**Audience.** My AVC248 students (entry-level, community-college). 24 students confirmed in one section, up to 44 if the second section runs.

**Process (how it actually works).** Render is a static web page. When a student asks for AI help, the page sends only the text of the task to a small proxy. The proxy holds the single Gemini API key as an encrypted secret, adds the instructions, calls Gemini over HTTPS, and returns only the answer text. The student's browser never holds the key. Nothing is stored on the server. This is the same no-PII, data-sovereign model the district already favored over vendor tools that harvest student data.

---

## What Render is

Render is a single web page (HTML and JavaScript, hosted on GitHub Pages) that walks a student through career preparation: building a resume, researching and pasting a real job posting, getting the resume and cover letter aligned to that posting, and receiving a coaching fit report that tells them, in a mentoring tone, whether the job is a reach or a strong match and how to strengthen the application. It is a prototype heading toward this pilot. It is not in production.

Authentication is first name only, kept in the browser. There is no login, no MEID, no student record.

---

## The architecture, in IT terms

```
Student browser (static page)        Small serverless proxy              Google Gemini
  no API key                  HTTPS    holds ONE Gemini key       HTTPS   (paid API tier)
  no PII       ───────────────────►    as an encrypted secret  ─────────► returns only text
  sends only task text                 adds the instructions
                                       stores nothing, logs
                                       only anonymous counts
```

Three facts that matter to a security review:

1. **No secret ships to the browser.** The API key lives only inside the proxy (a Cloudflare Worker, or a Google Apps Script relay, both of which store the key as an encrypted server-side secret). Viewing the page source or the network tab reveals nothing usable.
2. **The proxy is stateless.** It keeps no database, stores no conversation text, and retains no student identity. It logs only anonymous request counts for cost tracking. If someone obtained the logs they would find no student and no content.
3. **It is reversible and bounded.** One key powers the whole class. Revoke that key and the tool goes dark instantly. There is nothing to clean up, no accounts to deprovision, no stored data to purge.

The proxy can also rate-limit each student per day, so total usage physically cannot exceed the approved spend cap (see cost section).

---

## Where the Gemini key comes from (the real decision for OIT)

Our district Gemini is the Workspace chat app, which does not expose a programmable API. A tool like Render has to call the Gemini API, which uses an API key. There are two ways to source that key, and I am fine with either:

- **Preferred: OIT provisions a Gemini API key on a district Google Cloud project (Vertex AI).** Then the pilot runs under our district cloud agreement on district infrastructure, and OIT holds and rotates the key.
- **Fallback for a fast pilot: a paid Gemini API key I hold**, billed against the approved budget. On the paid API tier, Google contractually does not use the data for training. This is a Google paid-tier term, separate from the Workspace agreement, and it applies to any paid Gemini API key.

Either way, the pilot uses the **paid** tier, never the free tier (the free tier is the only one that trains on inputs).

---

## Data and privacy posture (the no-PII question)

The tool is built to send no personally identifiable information to the AI, by design.

**What never leaves the browser as identity:** no name, no address, no phone, no email, no MEID, no student ID, no student record. First name is used only as a label inside the student's own browser.

**The resume question, answered honestly.** Students build a resume of employment history, skills, education, and accomplishments, with the direct identifiers stripped: no name, no home address, no phone, no personal email. My read is that the direct identifiers are the clear PII to remove, and that job titles, employers, skills, and coursework are not direct identifiers. I want to be careful rather than overconfident: a rich enough combination of details could in principle point back to one person, so the pilot pairs three mitigations with that de-identification, and I am asking OIT and, if needed, the FERPA authority to confirm the position rather than assuming it.

The three mitigations:

- **Strip all direct identifiers** from anything the student enters, enforced in the tool and taught as a rule.
- **Tell students plainly** not to enter anything they would not be comfortable posting publicly, covered in the AI-ethics unit that opens the course.
- **Use the paid Gemini API tier**, on which Google contractually excludes the data from model training. This means that even if a student forgets and leaves a name on a resume, it is not used to train the model. Only the free consumer tier trains on inputs. This is the concrete reason to route students through this tool rather than letting them paste resumes into free Gemini or free ChatGPT on their own, which is what they will otherwise do.

Nothing is stored on the server, so there is no transcript to govern, breach, or retain.

---

## Does this break any district rules? The open questions for OIT

I built this to fit the district's no-student-data line, so I am not aware of a rule it breaks. The honest open questions I need OIT to rule on are these:

1. **May I run a bounded pilot** in one or two AVC248 sections for one semester, on a Gemini key OIT provisions if possible, or on a paid key I hold if the district path is not ready in time.
2. **Is the de-identified-resume position above acceptable** under the district's PII and FERPA interpretation, and is there anything additional you want stripped or added.
3. **How am I permitted to pay** the small API cost below. I expect to secure roughly $150 (see cost). Can course fees, a small purchase, or professional-development funds cover it, and what is the mechanism you need me to use.
4. **Path to district infrastructure.** If the pilot proves out, I would like it to move onto the district-hosted faculty-pilot server space I already proposed, so this becomes a supported tool rather than a personal one.

---

## Cost estimate

A single AI interaction sends roughly 4,000 input tokens (the instructions, the student's de-identified profile, a pasted job posting, and their resume text) and returns about 1,500 output tokens. At current published rates that is about 1.7 cents per interaction on Gemini Flash ($1.50 per million input, $7.50 per million output).

For a full 4.5-month term:

| Usage per student | 24 students | 44 students |
|---|---|---|
| Light (75 per term) | about $31 | about $56 |
| Realistic (150 per term) | about $61 | about $112 |
| Heavy (300 per term) | about $122 | about $224 |

**What I would ask to budget:** $150 for the term. That comfortably covers a normal term for the full 44 students, and I would set a hard spend cap at that figure in the billing dashboard so cost cannot exceed it, plus a small per-student daily limit in the proxy so a heavy stretch cannot push past the cap while keeping the tool running all semester. The proxy itself is free (Cloudflare Workers allows 100,000 requests per day on the free plan; a class this size uses a small fraction).

Model note: Gemini Flash is the target model, chosen for quality on resume-coaching and fit-report reasoning. Final model tier to confirm after a hands-on quality test in Google AI Studio.

Rates verified August 2026. Sources at the end.

---

## Why this is low risk

- One or two sections, one semester, then we stop and evaluate.
- One key, capped spend, revocable in seconds.
- No PII sent, nothing stored, no accounts, no student data to govern.
- Paid tier, so Google does not train on the data.
- Runs on district-provisioned Vertex AI if OIT prefers, and moves onto district server space later with a single endpoint change.

---

## The specific asks, restated for a quick yes or no

1. May I run this bounded, single-semester pilot in one or two AVC248 sections.
2. Will OIT provision a Gemini API key on a district Cloud project, or may I use a paid key I hold for the pilot.
3. Confirm the de-identified, no-PII data posture is acceptable, or tell me what to change.
4. Tell me how I am allowed to pay the roughly $150 cost, and the dollar cap you want on it.
5. Agree in principle that a proven pilot can migrate onto district-hosted server space later.

---

## Sources for the pricing figures

- Google Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Cloudflare Workers limits and pricing: https://developers.cloudflare.com/workers/platform/limits/
