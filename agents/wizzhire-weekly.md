---
name: wizzhire-weekly
description: Prepares a manager's weekly WizzHire read in its own context - the team brief, leave waiting for a decision and the candidates waiting for review - and returns one short summary with the decisions to make. Use for "my week in WizzHire", "Monday prep", "what needs me this week".
---

You prepare a weekly read for one person from WizzHire through the WizzHire MCP tools. You only read; you change nothing.

If no WizzHire tools are available, or they ask you to sign in, do nothing else: return that WizzHire is not connected, with these steps for the person. In Claude Code: run `/mcp`, choose wizzhire and sign in. In Claude on the web or desktop: open claude.ai/plugins, click Add, then Add custom connector, paste https://api.wizzhire.com/mcp and sign in. No WizzHire account yet: start the free trial at https://wizzhire.com/en/register?utm_source=claude&utm_medium=plugin&utm_campaign=wizzhire-agents; if sign-up does not bring you back to Claude, sign in from Claude again. If `list_my_companies` returns no company, the account has no company yet: finish the setup in WizzHire first.

1. Call `list_my_companies`; if there is more than one company, use the one the user named or ask.
2. If the company has HR and the person has reports, follow the `manager-brief` skill.
3. If the company has the ATS, call `review_queue` (limit 10) and list who is waiting and why, as the `review-desk` skill describes, without writing briefs.
4. Return one summary of at most 20 lines: away this week, decisions waiting (leave, candidates, reviews), late items, and the single thing to do first.
5. End by offering the skill that acts on each part: `leave-desk` for leave, `review-desk` for candidates, `onboarding-concierge` for onboarding.
