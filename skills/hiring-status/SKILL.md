---
name: hiring-status
description: Answer "where do things stand?" for every open WizzHire role - applicants per job, who is waiting and who is stuck, overdue hiring tasks and which channels bring people who get hired - in one short read. Use for "hiring status", "how is recruiting going", "pipeline update", "weekly hiring report", "stanje zapošljavanja", "pregled pozicija".
---

# Hiring status

One short, honest read of the hiring pipeline for a founder, a hiring manager or a weekly meeting. This skill only reads.

## Before you start

- Needs the WizzHire connector and the ATS module. Call `list_my_companies` and pick the company.
- Not connected yet (no WizzHire tools, or they ask you to sign in): say so and give these steps, then stop. Never do the task from memory or pasted data instead. In Claude Code: run `/mcp`, choose wizzhire and sign in. In Claude on the web or desktop: open claude.ai/plugins, click Add, then Add custom connector, paste https://api.wizzhire.com/mcp and sign in. No WizzHire account yet: start the free trial at https://wizzhire.com/en/register?utm_source=claude&utm_medium=plugin&utm_campaign=wizzhire-agents; if sign-up does not bring you back to Claude, sign in from Claude again. If `list_my_companies` returns no company, the account has no company yet: finish the setup in WizzHire first.

## Steps

1. **Open roles.** `list_jobs` with `openness="active"`: each job's applicants and how many nobody has opened yet.
2. **Waiting and stuck.** `review_queue` across all live jobs (limit 20): who waits on a decision and why. Then `review_queue` with `only_sitting_too_long=true` for people in one stage longer than a week (or the number of days the person chooses).
3. **Overdue work.** `task_summary` with `whose="team"`: open hiring tasks by due date and per person. Use `list_company_tasks` to name the overdue ones if asked.
4. **Where hires come from,** when the person asks or for a monthly read: `candidate_sources` for the last 90 days. Put each channel's applicants next to how many advanced and were hired, and say which channels bring hires rather than volume.

## Answer shape

- **One line per role:** title, applicants, new and unopened, waiting on a decision, stuck.
- **Needs attention:** the three most urgent items (an approval owed, someone stuck longest, a role with no new applicants).
- **Overdue:** hiring tasks past their date, with who has them.
- **Channels** (when asked): a short table.

End with the single most useful next action and the skill that does it (**review-desk** for waiting candidates, **team-decision** to chase ratings). Under 20 lines. Reply in the language the person writes in.

## Never

- Change anything.
- Turn counts into promises about time to hire, or compare people by speed.
- Show candidate contact details. The tools do not return them.
