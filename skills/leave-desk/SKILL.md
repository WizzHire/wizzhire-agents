---
name: leave-desk
description: Clear the WizzHire leave requests waiting on you - for each one, who else on the team is off, public holidays and the days left - then record the approve or reject decision you give, one request at a time. Use for "leave approvals", "who is off next week", "can I approve this vacation", "odobri godišnji", "zahtjevi za odsustvo", "ko je odsutan".
---

# Leave desk

Help a manager or HR decide leave requests with the facts in front of them, and record each decision they make.

## Before you start

- Needs the WizzHire connector and the HR module. Call `list_my_companies` and pick the company.
- Read `wizzhire_guide(topic="people")` once.

## Steps

1. **What is waiting.** Call `list_leave_requests` (status `submitted`, scope `team`; `company` only if the person has company-wide leave access). Keep only the requests whose line says the decision is theirs; mention the others briefly.
2. **Facts for each request.**
   - `who_is_away` over the request's dates (same team), which also lists public holidays from each person's own calendar.
   - `leave_balances` for the person: read the **available** figure. Never compute it yourself; it already folds in carry-over, corrections and days requested but not taken.
3. **Show one line per request:** who, which leave type, dates and working days, who else on the team is off those days, holidays inside the range, days available after this request.
4. **Ask for a decision on each request.** Approve or reject, one by one. Never assume, never approve in bulk without the person naming each one.
5. **Record it.** Call `decide_leave_request` with the person's decision. A rejection needs their reason: write it as they would say it to the employee, because the employee reads it. If more approvers are configured, say the vote is recorded and how many are still needed.

## Also useful

- "Who is off next week?": `who_is_away` for the window, approved leave only. Requests still waiting are not absences yet; say so and point to step 1.
- "How many days does Amra have left?": `leave_balances` for that person.

## You may change, always after a yes

Leave decisions, one request at a time.

## Never

- Decide a request the person did not explicitly decide.
- Recompute a balance or guess holidays.
- Give legal advice on leave rights. Entitlements are the company's own setting.

## Answer shape

A compact table of waiting requests, then the question "Approve or reject each?". After recording, one line per decision with the days left. Reply in the language the person writes in. In Bosnian use "odsustvo", "godišnji odmor", "zahtjev", "odobreno", "odbijeno".
