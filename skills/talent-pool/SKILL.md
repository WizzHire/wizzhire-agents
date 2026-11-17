---
name: talent-pool
description: Find people in your company's own WizzHire talent pool who agreed to hear about future roles and fit a role you are opening, with the reason each one fits. Only people with current agreement are ever suggested. Use for "anyone in our talent pool for this role", "search our candidate database", "talent pool", "baza kandidata", "imamo li nekoga u bazi".
---

# Talent pool

Before advertising a role, check whether someone who already agreed to hear from the company fits it.

This is the company's own talent pool: people who applied or were added and agreed to be kept for future roles. The agreement is recorded in WizzHire, it can expire, and people can withdraw at any time. This skill only ever suggests people whose agreement is current.

## Before you start

- Needs the WizzHire connector and the ATS module with the talent pool. Call `list_my_companies` and pick the company.
- Read `wizzhire_guide(topic="hire")` once.
- This skill needs the WizzHire `search_talent_pool` tool. If it is not available on this connection yet, say so plainly and point to the talent pool page in WizzHire; do not try to rebuild the pool from old applications.

## Steps

1. **The role.** Find it with `list_jobs`. If the WizzHire `get_job` tool is available, read its requirements and skills; otherwise ask the person what matters most (skills, level, location, availability).
2. **Search the pool.** Call `search_talent_pool` with the filters that matter (skills, words from the title, location). It returns only people who agreed to be kept for future roles.
3. **Shortlist the fits.** Up to ten people, each with one or two lines on why they fit, from their title, skills, tags and the roles they were in before. Say what is unknown.
4. **Next step for the person.** Inviting someone to the role, or adding them to it, is done from the talent pool page in WizzHire, which keeps the record of what they agreed to. Offer to create a reminder task with `list_teammates` and `create_task`, after a yes.

## Never

- Suggest anyone whose agreement is missing, expired, declined or withdrawn, or work around the tool's filter.
- Use rejected or old applications outside the talent pool to find people.
- Show contact details. The tools do not return them; contacting people happens in WizzHire.
- Use or infer age, gender, family status, nationality, health or photo.

## Answer shape

A short list: name, current title, why they fit, what is unknown. Then the one next step. Reply in the language the person writes in.
