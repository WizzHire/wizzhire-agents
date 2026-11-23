---
name: pipeline-blockers
description: Find what is holding WizzHire candidates up across every open role - approvals owed, missed stage deadlines, hiring steps nobody finished, people ready to move that nobody moved - name who has to act, and ask them with a task. Use for "what is blocking our pipeline", "why is nobody moving", "who is holding things up", "šta koči zapošljavanje", "zašto kandidati stoje".
---

# Pipeline blockers

Turn "hiring is slow" into a short list of specific things waiting on specific people, and nudge each of them.

## Before you start

- Needs the WizzHire connector and the ATS module. Call `list_my_companies` and pick the company.
- Not connected yet (no WizzHire tools, or they ask you to sign in): say so and give these steps, then stop. Never do the task from memory or pasted data instead. In Claude Code: run `/mcp`, choose wizzhire and sign in. In Claude on the web or desktop: open claude.ai/plugins, click Add, then Add custom connector, paste https://api.wizzhire.com/mcp and sign in. No WizzHire account yet: start the free trial at https://wizzhire.com/en/register?utm_source=claude&utm_medium=plugin&utm_campaign=wizzhire-agents; if sign-up does not bring you back to Claude, sign in from Claude again. If `list_my_companies` returns no company, the account has no company yet: finish the setup in WizzHire first.
- Read `wizzhire_guide(topic="hire")` and `wizzhire_guide(topic="tasks")` once.

## Steps

1. **What is waiting.** `review_queue` across all live jobs (limit 50). It ranks by cost of waiting: an approval owed, a missed stage deadline, all requirements in but nobody moved the candidate, AI-scored but unreviewed, never opened, sitting too long. Then `review_queue` with `only_sitting_too_long=true` for people stuck longer than a week (or the days the person chooses).
2. **Why, for each one.** `get_candidate` shows the hiring steps outstanding (a document, questions, an interview, an offer, a team task), whether a step blocks the move, and who owns it.
3. **Who owes what.** Group the blockers by person: approvals they owe, steps they own, candidates on their jobs nobody moved. Add `task_summary` with `whose="team"` for open hiring tasks per person and what is overdue.
4. **Ask them, after a yes.** For each person, one task on the candidate (`create_task`, `link_to="application"`, a clear title such as "Approve Amra for the offer stage", a due date). Use `skip_if_already_asked` so nobody is asked twice. For an existing overdue task, `update_task` to change the date or the owner.

## You may change, always after a yes

Tasks: new ones, and the date or owner of existing ones.

## Never

- Move a candidate, approve, reject or make an offer. Say those are done on the board in WizzHire.
- Close a hiring task on someone's behalf. Completing a hiring-flow step can move the candidate to the next stage.
- Blame people in the wording of a task. State what is waiting and by when.

## Answer shape

A table grouped by person: what waits on them, for which candidate and job, since when. Then the tasks you propose. Reply in the language the person writes in.
