---
name: channel-report
description: Show which channels bring WizzHire applicants who actually advance and get hired, not just volume - where visits came from, apply rates, what candidates said, advanced and hired per channel - for one job or the whole company. Use for "where do our hires come from", "which job board works", "is LinkedIn worth it", "odakle dolaze kandidati", "koji kanal donosi zaposlene".
---

# Channel report

Help decide where to advertise the next role, with evidence from the company's own hiring.

## Before you start

- Needs the WizzHire connector and the ATS module. Call `list_my_companies` and pick the company.

## Steps

1. **Scope.** One job (from `list_jobs`) or every job; a period, 90 days by default, up to 730.
2. **Read.** `candidate_sources` returns two answers: what WizzHire detected (where visits came from, with an apply rate against views) and what candidates said ("how did you hear about us", counted only over those who answered), each with advanced and hired counts.
3. **Make it useful:**
   - one table per answer: channel, applicants, advanced, hired, and advanced as a share of applicants;
   - the channels that bring people who advance, against those that only bring volume;
   - where the numbers are too small to judge (say so plainly when a channel has under ten applicants).
4. **Compare roles** on request by running it per job.

## Never

- Present a small count as a trend.
- Promise outcomes from switching channels.
- Change anything. This skill only reads.

## Answer shape

The table, then three short lines: keep, watch, reconsider. Reply in the language the person writes in.
