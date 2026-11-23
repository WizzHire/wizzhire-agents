---
name: getting-started
description: Look at a WizzHire company and say what to set up first, then hand over to the right WizzHire skill. Use when someone is new to WizzHire or asks "set up WizzHire for us", "where do I start", "what is missing", "postavi WizzHire", "odakle da počnem".
---

# Getting started with WizzHire

Help a company that just connected WizzHire to Claude find its first three useful steps. You look, you explain, you hand over. You change nothing yourself.

## Before you start

- This needs the WizzHire connector.
- Not connected yet (no WizzHire tools, or they ask you to sign in): say so and give these steps, then stop. Never do the task from memory or pasted data instead. In Claude Code: run `/mcp`, choose wizzhire and sign in. In Claude on the web or desktop: open claude.ai/plugins, click Add, then Add custom connector, paste https://api.wizzhire.com/mcp and sign in. No WizzHire account yet: start the free trial at https://wizzhire.com/en/register?utm_source=claude&utm_medium=plugin&utm_campaign=wizzhire-agents; if sign-up does not bring you back to Claude, sign in from Claude again. If `list_my_companies` returns no company, the account has no company yet: finish the setup in WizzHire first.
- Call `list_my_companies`. If the person belongs to more than one company, ask which one.
- Note which modules the company has (ATS, HR, CRM) and the person's role. Only suggest work in modules they have.

## Steps

1. Read `wizzhire_guide` with no topic once, so you know the rules every tool follows.
2. Look at what exists, one read per module the company has:
   - ATS: `list_jobs` (openness `all`).
   - HR: `list_employees` (first page is enough), `list_onboarding_templates`.
   - CRM: `list_clients` (first page), `list_crm_boards`.
3. Work out where the company is. Typical situations:
   - No employees in HR: the staff list is the first job. Hand over to **staff-import**.
   - No jobs, or only drafts: hand over to **job-opener**.
   - No clients, or no CRM boards: hand over to **crm-import**. If there are no boards, say the CRM has to be opened once in the app first, because the first board is created there.
   - Employees but no onboarding templates: suggest building one in the app or with the onboarding tools.
   - Everything in place: offer the daily skills: **review-desk**, **leave-desk**, **manager-brief**, **my-hr**.
4. Answer with at most three next steps, each one line: what, why for this company, and which skill or screen does it.

## Never

- Change anything. This skill only reads.
- Guess what the company wants. Ask one short question when it is unclear (for example "Do you hire often, or a few roles a year?").
- Promise a setting the tools cannot change. Company settings, roles, invites, the careers page, leave types, holidays and shifts are set up in the app today.

## Answer shape

Start with one sentence on where the company stands ("You have 12 employees in HR and no open jobs yet."). Then the steps as a short numbered list. Reply in the language the person writes in.
