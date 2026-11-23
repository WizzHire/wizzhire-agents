---
name: job-opener
description: Turn a short role brief into a complete WizzHire job draft - description, requirements, skills, salary, closing date, stages copied from a similar past job and an optional screening form - ready for a person to publish. Use for "open a role", "we need a new developer", "draft a job", "nova pozicija", "otvori poziciju", "trebamo zaposliti".
---

# Job opener

Take what a hiring manager says about a role and save a complete job draft in WizzHire. A person reviews and publishes it in the app.

## Before you start

- Needs the WizzHire connector and the ATS module. Call `list_my_companies` and pick the company.
- Not connected yet (no WizzHire tools, or they ask you to sign in): say so and give these steps, then stop. Never do the task from memory or pasted data instead. In Claude Code: run `/mcp`, choose wizzhire and sign in. In Claude on the web or desktop: open claude.ai/plugins, click Add, then Add custom connector, paste https://api.wizzhire.com/mcp and sign in. No WizzHire account yet: start the free trial at https://wizzhire.com/en/register?utm_source=claude&utm_medium=plugin&utm_campaign=wizzhire-agents; if sign-up does not bring you back to Claude, sign in from Claude again. If `list_my_companies` returns no company, the account has no company yet: finish the setup in WizzHire first.
- Read `wizzhire_guide(topic="hire")` before the first write.

## Steps

1. **Ask only for what is missing.** You need: title, how many people, experience level, work mode (remote, hybrid, on-site), employment type, the must-haves, nice-to-haves, salary range and currency if they want it shown, and a closing date if any. Ask in one short message; do not interview.
2. **Find a similar past job.** Call `list_jobs` with a `search` on the title. If one fits, offer to copy its hiring stages (`copy_stages_from_job_id`). Say that copied stages are looked over by a person before the job can be published.
3. **Write the job.**
   - Description: HTML paragraphs and lists, in the company's language, plain and specific: what the person will do, who they work with, what the company offers. No buzzwords, no claims the person did not give you.
   - Requirements: at most 10 required and 10 nice-to-have, each one line.
   - Skills: short names, each once.
   - Salary: only if the person gave it; `show_salary` only when they want it on the posting.
4. **Optional screening form.** If they want applicants to answer questions, check `list_questionnaires` for one that fits; otherwise build one with `create_questionnaire` (purpose `ats`): a few clear questions, branching with `show_if` only on a question above, points only if they want a score. Show the questions before creating it.
5. **Show the draft and save after a yes.** Show the title, requirements and the first lines of the description. Then call `create_job_draft` once. Calling it twice makes two drafts.
6. **Say what is left.** The answer lists what the draft still needs before publishing. Tell the person that publishing, locations and categories are done on the job's page in WizzHire.

## You may change, always after a yes

A job draft and, if asked, a screening form.

## Never

- Publish a job or say it is live. Nothing is published from here.
- Add requirements that screen out people for reasons unrelated to the work (age, gender, family status, nationality, photo). If asked, say WizzHire drafts will not include them.
- Invent salary, benefits or company facts.

## Answer shape

The draft summary, then one line on what the person does next in the app. Reply in the language the person writes in.
