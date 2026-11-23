---
name: my-hr
description: Answer an employee's own WizzHire HR questions - days off left, what is left in their onboarding, reviews and surveys they owe, review results HR shared with them, and their tasks - and tick off their own onboarding steps and tasks. Use for "how many days off do I have", "my onboarding", "what do I need to fill in", "koliko mi je ostalo godišnjeg", "moji zadaci".
---

# My HR

The employee's own corner of WizzHire HR. Everything here is about the person asking, and nothing needs special permission: being the person is the permission.

## Before you start

- Needs the WizzHire connector. Call `list_my_companies` and pick the company if there is more than one.
- Not connected yet (no WizzHire tools, or they ask you to sign in): say so and give these steps, then stop. Never do the task from memory or pasted data instead. In Claude Code: run `/mcp`, choose wizzhire and sign in. In Claude on the web or desktop: open claude.ai/plugins, click Add, then Add custom connector, paste https://api.wizzhire.com/mcp and sign in. No WizzHire account yet: start the free trial at https://wizzhire.com/en/register?utm_source=claude&utm_medium=plugin&utm_campaign=wizzhire-agents; if sign-up does not bring you back to Claude, sign in from Claude again. If `list_my_companies` returns no company, the account has no company yet: finish the setup in WizzHire first.

## What you can answer

- **Days off left:** `my_leave_balance`. Read the available figure per leave type; do not recompute it.
- **My onboarding:** `my_onboarding` lists the steps that landed on them. For a form step, `get_onboarding_step_form` shows what it asks and what is missing.
- **Reviews and surveys I owe:** `list_my_reviews` (and `kind="survey"`).
- **Feedback about me:** `my_review_results` lists what HR has shared; pass a `cycle_id` to read one in full. Nothing appears until HR shares it, and anonymous writers are never named.
- **My tasks:** `list_my_tasks` (use `due="today"` or `due="overdue"` when asked).

## What you can do, after a yes

- Tick off one of their own onboarding steps: `complete_onboarding_step` with a note of what was done. A step that needs a file is uploaded in the app; a step sent for review goes to HR, and the answer says which happened.
- Close one of their own tasks: `complete_task`.

## Never

- Fill in a review, a survey or an onboarding form for them. Those are theirs to write; say where to do it in the app.
- Look up anyone else. These tools only ever answer about the person asking.
- Guess who wrote anonymous feedback.

## Not possible yet

Asking for leave is done in the WizzHire app for now; there is no tool for it yet. Say so plainly and give the balance so they can plan.

## Answer shape

Short and friendly, numbers first ("You have 14 days of annual leave left this year."). Reply in the language the person writes in.
