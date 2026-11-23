---
name: manager-brief
description: A one-screen Monday brief for a line manager from WizzHire - who on the team is away in the next two weeks, leave waiting for a decision, new people's onboarding, reviews the manager owes and late tasks they delegated. Use for "what do I need to know about my team", "Monday brief", "team this week", "šta trebam znati o timu", "pregled tima".
---

# Manager brief

Give a line manager everything about their team that needs attention this week, in one short read. This skill only reads.

## Before you start

- Needs the WizzHire connector and the HR module. Call `list_my_companies` and pick the company.
- Not connected yet (no WizzHire tools, or they ask you to sign in): say so and give these steps, then stop. Never do the task from memory or pasted data instead. In Claude Code: run `/mcp`, choose wizzhire and sign in. In Claude on the web or desktop: open claude.ai/plugins, click Add, then Add custom connector, paste https://api.wizzhire.com/mcp and sign in. No WizzHire account yet: start the free trial at https://wizzhire.com/en/register?utm_source=claude&utm_medium=plugin&utm_campaign=wizzhire-agents; if sign-up does not bring you back to Claude, sign in from Claude again. If `list_my_companies` returns no company, the account has no company yet: finish the setup in WizzHire first.
- The person must have reports in the org chart. If `list_my_team` returns nobody, say so and stop.

## Steps

1. `list_my_team`: who reports to them and where each person is today (working, on which shift, on leave), plus how many leave requests are waiting.
2. `who_is_away` with `scope="my_team"` from today for 14 days: approved leave and public holidays.
3. `list_leave_requests` (status `submitted`, scope `team`): what waits for their decision.
4. `list_onboardings` with `scope="my_team"` (state `running`): new people, overdue and stuck steps.
5. `list_my_reviews`: reviews they still have to write (and surveys, with `kind="survey"`).
6. `list_my_tasks` with `delegated=true` and `due="overdue"`: what they asked of others that is late. Also `list_my_tasks` with `due="today"` for their own.

## Answer shape

Five short sections, skipping any that are empty:

- **Away:** names with dates.
- **Waiting on you:** leave requests (offer **leave-desk** to decide them) and reviews to write.
- **New people:** onboarding progress, anything overdue or stuck.
- **Late:** delegated tasks past their date, with who has them.
- **Today:** their own tasks due today.

End with the one thing most worth doing first. Keep it under 15 lines. Reply in the language the person writes in.

## Never

- Change anything. Offer the right skill instead (leave-desk, onboarding-concierge).
- Show anything beyond the manager's own reports. The tools already limit this; do not work around a refusal.
