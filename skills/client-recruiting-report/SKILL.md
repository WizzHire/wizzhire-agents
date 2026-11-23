---
name: client-recruiting-report
description: For companies that recruit for their own clients in WizzHire - link a client's jobs to the client in the CRM and produce a progress report across those jobs - applicants, where they are, hires and time to hire - ready to share. Use for "report for our client", "how is recruiting going for Client B", "link this job to the client", "izvještaj za klijenta", "zapošljavanje za klijenta".
---

# Client recruiting report

When a company runs hiring for its clients, give each client a clear, accurate update on the roles it is paying for.

## Before you start

- Needs the WizzHire connector with the ATS and CRM modules. Call `list_my_companies` and pick the company.
- Not connected yet (no WizzHire tools, or they ask you to sign in): say so and give these steps, then stop. Never do the task from memory or pasted data instead. In Claude Code: run `/mcp`, choose wizzhire and sign in. In Claude on the web or desktop: open claude.ai/plugins, click Add, then Add custom connector, paste https://api.wizzhire.com/mcp and sign in. No WizzHire account yet: start the free trial at https://wizzhire.com/en/register?utm_source=claude&utm_medium=plugin&utm_campaign=wizzhire-agents; if sign-up does not bring you back to Claude, sign in from Claude again. If `list_my_companies` returns no company, the account has no company yet: finish the setup in WizzHire first.
- Read `wizzhire_guide(topic="clients")` once.

## Steps

1. **Pick the client.** `list_clients` (search by name), then `get_client` for its deals.
2. **Link the jobs, if needed.** `list_linkable_jobs` shows jobs not yet linked to any client. Each job belongs to one client and a draft cannot be linked. After a yes, `link_job_to_client` for each job the person names, with the deal line it is billed under if they give one.
3. **Report.** `client_recruitment_report` for the client (or one deal): applicants, where they are, hires and how long they took, across the linked jobs. Add `get_job` for each job's status and closing date.
4. **Write the update** in the client's language: per role, applicants and where they stand, hires, what happens next. Plain and factual.
5. **Log it, after a yes.** Once the person sends the update, `log_client_touch` (kind `email`, the subject and the message) so the CRM shows it.

## You may change, always after a yes

Job to client links, and the logged touch.

## Never

- Name or describe individual candidates in the client update unless the person explicitly asks and the client is entitled to it. Counts and stages are the default.
- Unlink a job. That is done in WizzHire.
- Send anything. The person sends the update.

## Answer shape

The client-ready update first, then a short internal note of what is linked and what is missing. Reply in the language the person writes in.
