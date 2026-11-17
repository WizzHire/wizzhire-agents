# Hiring flows and what covers them

Every hiring flow in WizzHire today, the skill or agent that helps with it in Claude, and what a person does in the WizzHire app. Checked against the WizzHire server's tools at commit 9e5def8a2.

## Covered in Claude

| Flow | Skill or agent | What Claude does |
|---|---|---|
| Plan a new role | `role-designer` (agent), `job-opener` | Drafts the job ad, requirements, skills, stages to copy, screening form and interview kit; saves the job as a draft |
| Improve a job ad | `job-ad-check` | Reviews clarity, missing facts and excluding wording; writes a version to paste |
| Screening questions | `screening-form` | Builds the form with branching and points; scores and compares answers |
| Daily review | `review-desk` | Who waits on you and why, a brief per candidate; your notes, stars and ratings |
| One candidate in depth | `candidate-brief` | Fit against the job, AI screening with reasons, answers, team notes, open questions |
| Read many applications | `candidate-researcher` (agent) | A brief per candidate for a panel, no ranking |
| Compare finalists | `shortlist` | Scores, ratings, skills and salary asks side by side |
| Interviews | `interview-kit` | Core questions, follow-ups from screening, a scorecard; the debrief saved on the profile |
| Team decision | `team-decision` | Ratings and notes in one place, disagreements shown, tasks for missing ratings |
| Talent pool | `talent-pool`, `talent-matcher` (agent) | People in the company's own pool who agreed to hear about new roles |
| Unblock the pipeline | `pipeline-blockers` | Approvals owed and unfinished steps, grouped by person, with tasks |
| Hiring tasks | `hiring-tasks` | Your hiring to-do list and what you delegated; reschedule, hand over, close |
| Status | `hiring-status`, `hiring-analyst` (agent) | Every open role, waiting and stuck, overdue, channels |
| Channels | `channel-report` | Applicants, advanced and hired per channel |
| Recruiting for clients | `client-recruiting-report` | Links jobs to a CRM client and writes a progress update |

## Done by a person in the WizzHire app

These are not available to Claude by design or not yet:

| Flow | Why it stays in the app |
|---|---|
| Publish a job, edit an existing job | A person decides what goes public. Claude saves drafts and suggests text. |
| Move a candidate between stages, reject, hire | Hiring decisions stay with a person. |
| Approve a stage move | Approvals are a person's decision. |
| Make or change an offer | Money and commitment to a candidate. |
| Schedule interviews | Uses the interviewers' calendars in the app. |
| Attach a screening form to an existing job | Not available as a tool yet; Claude can attach one only when it creates the draft. |
| Invite someone from the talent pool, or add them to a job | Done from the talent pool page, which keeps the record of their agreement. |
| Careers page, branding, open applications | Public pages; set up in the app. |
| Contact candidates | Candidate contact details are never shared with Claude. |
