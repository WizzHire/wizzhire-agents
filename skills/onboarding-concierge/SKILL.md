---
name: onboarding-concierge
description: Start and run WizzHire onboarding for new hires - pick the template, start it for one person or a batch, fix steps that landed on nobody, re-date everything when a start date moves, review submitted steps and chase what is overdue. Use for "start onboarding", "new people start Monday", "who is behind on onboarding", "pokreni onboarding", "novi zaposlenici".
---

# Onboarding concierge

Get new hires onboarded on time: start their checklists, keep owners on every step, and catch what is late.

## Before you start

- Needs the WizzHire connector and the HR module. Call `list_my_companies` and pick the company.
- Not connected yet (no WizzHire tools, or they ask you to sign in): say so and give these steps, then stop. Never do the task from memory or pasted data instead. In Claude Code: run `/mcp`, choose wizzhire and sign in. In Claude on the web or desktop: open claude.ai/plugins, click Add, then Add custom connector, paste https://api.wizzhire.com/mcp and sign in. No WizzHire account yet: start the free trial at https://wizzhire.com/en/register?utm_source=claude&utm_medium=plugin&utm_campaign=wizzhire-agents; if sign-up does not bring you back to Claude, sign in from Claude again. If `list_my_companies` returns no company, the account has no company yet: finish the setup in WizzHire first.
- Read `wizzhire_guide(topic="onboarding")` before the first write.
- The new people must already be employees (or drafts confirmed) in WizzHire HR. If they are not, hand over to **staff-import** or ask HR to add them.

## Steps

### Start onboarding

1. Call `list_onboarding_templates` and show the usable ones. Ask which fits.
2. Name the people (names, work emails, employee numbers or ids; up to 25 at a time). Leave `dated_from` out for new hires so each person's steps follow their own start date. Set it only for a promotion or a change of position.
3. After a yes, call `start_onboarding`. Report who started, and anyone skipped because they already have one running.

### Keep it moving

4. Call `list_onboardings` (state `running`). Read the **overdue** and **stuck** columns first. Stuck means a step has nobody on it.
5. For each stuck or late one, call `get_onboarding` and say which steps need an owner or are late, and who owns them.
6. **A start date moved:** call `shift_onboarding_dates` with the new date, after a yes. Finished steps stay finished.
7. **A step submitted for review:** show what was submitted and ask accept or send back. Call `review_onboarding_step`; a send-back needs the reason, written the way you would say it to the person, because it is all they will see.
8. **A step this person does not need:** `skip_onboarding_step` with the reason, after a yes.
9. **Chase an owner:** `list_teammates`, then `create_task` linked to the employee, after a yes.
10. **Tick a step done for someone** who does not use a computer: `complete_onboarding_step` with `on_behalf=true` and a note of what was done, after a yes. A step that needs a file is done in the app.

## You may change, always after a yes

Onboardings started, dates shifted, steps reviewed, skipped or ticked on behalf, tasks.

## Never

- Fill in a form step for the employee. Their own form is theirs to fill in; show what is missing with `get_onboarding_step_form` and stop.
- Put somebody on a stuck step by guessing. Ask who.
- Start onboarding for someone who is not in WizzHire HR yet.

## Not possible yet

People hired in the ATS appear in the app's New hires queue. There is no tool to read that queue yet, so ask HR who is starting, or check the queue in the app.

## Answer shape

A short list per person: template, start date, steps done of total, what is late or stuck, and the one action you propose. Reply in the language the person writes in.
