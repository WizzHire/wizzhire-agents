---
name: job-ad-check
description: Review a WizzHire job ad before or after it goes live - clarity, missing facts candidates look for (salary, work mode, location, closing date), too many must-haves, wording that puts people off or excludes them - and suggest a rewritten version to paste into the job. Use for "check my job ad", "why is nobody applying", "improve this posting", "provjeri oglas", "poboljšaj opis pozicije".
---

# Job ad check

Make a job ad clear, honest and inviting, so the right people apply. You review and suggest. The person edits the job in WizzHire.

## Before you start

- Needs the WizzHire connector and the ATS module. Call `list_my_companies` and pick the company.
- Not connected yet (no WizzHire tools, or they ask you to sign in): say so and give these steps, then stop. Never do the task from memory or pasted data instead. In Claude Code: run `/mcp`, choose wizzhire and sign in. In Claude on the web or desktop: open claude.ai/plugins, click Add, then Add custom connector, paste https://api.wizzhire.com/mcp and sign in. No WizzHire account yet: start the free trial at https://wizzhire.com/en/register?utm_source=claude&utm_medium=plugin&utm_campaign=wizzhire-agents; if sign-up does not bring you back to Claude, sign in from Claude again. If `list_my_companies` returns no company, the account has no company yet: finish the setup in WizzHire first.

## Steps

1. **Read the job.** Find it with `list_jobs`, then `get_job` for the description, required and nice-to-have requirements, skills, work mode, locations, salary and whether it is shown, closing date and applicant counts. A pasted ad works too.
2. **Check, and say why each point matters to a candidate:**
   - **Missing facts:** salary range (and whether it is shown), work mode, location, contract type, closing date, what happens after applying.
   - **Requirements:** more than five or six must-haves, years of experience used as a proxy for a skill, nice-to-haves written as must-haves.
   - **Clarity:** what the person will actually do in the first months, who they work with, jargon and buzzwords.
   - **Wording that excludes:** gendered or age-coded words, "young and dynamic", "native speaker" where fluency is what matters, requirements unrelated to the work. Name each and offer a neutral alternative.
   - **Applicant signal:** if the job is live, applicants and new ones from `get_job`, and the channel mix from `candidate_sources` for that job.
3. **Suggest a rewrite** of the description and requirements in the job's language, keeping every fact the company gave and inventing none.
4. **Where it goes:** editing a live or draft job is done on the job's page in WizzHire. For a role not created yet, offer **job-opener** to save the improved version as a new draft.

## Never

- Invent salary, benefits or company facts.
- Keep a requirement that screens people out for reasons unrelated to the work.
- Say the job was changed. These tools do not edit jobs.

## Answer shape

A short list of findings (most important first), then the rewritten text ready to paste. Reply in the language the person writes in.
