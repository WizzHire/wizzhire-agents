---
name: hiring-tasks
description: Your WizzHire hiring to-do list - screening reviews, questionnaire reviews, approvals and anything a colleague asked of you on a candidate - most pressing first, plus what you delegated that is late; reschedule, hand over or close your own tasks. Use for "my hiring tasks", "what do I owe today", "what did I ask others for", "moji zadaci u zapošljavanju", "šta trebam danas uraditi".
---

# Hiring tasks

The person's own hiring work in one list, and a quick way to keep it moving.

## Before you start

- Needs the WizzHire connector. Call `list_my_companies` and pick the company.

## Steps

1. **What I owe.** `list_my_tasks` with `module="hire"` (default `scope="open"`, sorted by priority). Show overdue and today first. Each row says which candidate or job it is about.
2. **What I am waiting on.** `list_my_tasks` with `module="hire"` and `delegated=true`, and `due="overdue"` for what is late.
3. **Context on request.** For a task about a candidate, `get_candidate` shows what the step needs.
4. **Act, after a yes, one task at a time:**
   - new date, priority or owner: `update_task` (owners from `list_teammates`)
   - a reminder to a colleague: `create_task` on the same candidate with `skip_if_already_asked`
   - done: `complete_task`, only for a task the person says is finished. If the task is a hiring-flow step on a candidate, say first that closing it can move the candidate to the next stage, and ask again.

## You may change, always after a yes

The person's tasks and tasks they created: dates, priority, owner, done.

## Never

- Close a task the person did not say is finished.
- Do the review, approval or decision a task asks for. Point to where it is done in WizzHire.

## Answer shape

Two short lists: **On you** (overdue, today, this week) and **Waiting on others** (late first). Then "Change a date, hand one over, or close one?". Reply in the language the person writes in.
