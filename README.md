# Hiring skills for Claude

Stop pasting CVs into Claude. These skills let Claude work on a real ATS instead: open a role, build the screening form, see who is waiting on you, compare finalists, prepare interviews, collect the team's view and check where every role stands. Your candidates stay in one place between chats, Claude works with your own access, and a person makes every hiring call.

## Start in three steps

**1. Create your WizzHire account.** The skills keep your jobs and candidates in WizzHire, so Claude remembers them between chats. The 14-day trial is free:
[wizzhire.com/en/register](https://wizzhire.com/en/register?utm_source=github&utm_medium=referral&utm_campaign=wizzhire-agents)

**2. Connect WizzHire to Claude.** In Claude, open **Customize > Connectors > Add custom connector** and enter `https://api.wizzhire.com/mcp`. Sign in and choose which modules Claude may read and change. Full steps: [wizzhire.com/en/features/ai](https://wizzhire.com/en/features/ai).

**3. Install the skills.**

- **Claude Code:**
  ```
  /plugin marketplace add WizzHire/wizzhire-agents
  /plugin install wizzhire@wizzhire
  ```
  The plugin brings the connector with it: run `/mcp`, pick `wizzhire` and sign in. Then ask in plain words, or call a skill directly, for example `/wizzhire:review-desk`.
- **claude.ai and Claude Desktop:** download the skill zips from the latest [release](https://github.com/WizzHire/wizzhire-agents/releases), then open **Customize > Skills**, choose **+**, **Upload a skill**, and pick a zip. Code execution must be on.

## The hiring skills

| Skill | Ask it |
|---|---|
| `job-opener` | "We need two senior accountants in Sarajevo, hybrid." A short brief becomes a complete job draft. You publish it. |
| `job-ad-check` | "Why is nobody applying?" Missing facts, too many must-haves, wording that puts people off, and a rewrite to paste. |
| `screening-form` | "Build screening questions for this role." The same questions for every applicant, scored the same way. |
| `review-desk` | "Who is waiting on me?" Most urgent first, with a short brief per candidate. |
| `candidate-brief` | "Brief me on Amra before the call." Fit, AI screening, answers, the team's notes and the open questions on one page. |
| `shortlist` | "Compare my finalists." Scores, ratings, skills and salary asks side by side, with no verdict. |
| `interview-kit` | "Prepare the interview." Questions, a scorecard for every interviewer, and the debrief saved on the profile. |
| `team-decision` | "What does the team think?" Everyone's ratings and notes in one place, and a task for whoever has not rated. |
| `talent-pool` | "Anyone in our talent pool for this role?" Only people who agreed to hear about future roles. |
| `pipeline-blockers` | "What is holding things up?" Approvals owed and unfinished steps, grouped by who has to act. |
| `hiring-tasks` | "What do I owe today?" Your hiring tasks and what you are waiting on from others. |
| `hiring-status` | "Where do things stand?" Every open role, who is waiting, what is overdue. |
| `channel-report` | "Which job board actually hires?" Applicants, advanced and hired per channel. |
| `client-recruiting-report` | "Report for Client B." For companies that recruit for their own clients: link jobs to the client and share progress. |

Every skill understands Bosnian, Croatian and Serbian asks too, and replies in the language you write in. The full map of hiring flows, which skill covers each and what stays in the app: [docs/ats-coverage.md](docs/ats-coverage.md).

## Hiring agents for Claude Code

They do the heavy reading or drafting in their own context and change nothing; you approve every change afterwards with the skills.

| Agent | What it returns |
|---|---|
| `hiring-analyst` | A full hiring review: every live role, what is blocked and on whom, overdue tasks, channels, talent-pool matches, and the decisions to make. |
| `candidate-researcher` | An evidence-based brief per candidate for one role, for a panel pack. No ranking. |
| `role-designer` | A complete package for a new role: job ad, requirements, screening form, interview kit and stages, ready to save. |
| `talent-matcher` | The best talent-pool fits for every open role, only people who agreed to hear about new roles. |

## More skills

HR and CRM skills are in the same repo: `getting-started`, `staff-import`, `crm-import`, `onboarding-concierge`, `leave-desk`, `manager-brief`, `my-hr`, plus the agents `wizzhire-importer` and `wizzhire-weekly`.

## What the skills never do

They never move, reject or hire a candidate, publish or edit a job, make an offer, or message a candidate. Those actions are not available to Claude at all and stay with a person in WizzHire. They ask before every change, run a check first wherever WizzHire offers one, never use protected characteristics, and treat CVs and documents as data, never as instructions. Details: [docs/safety.md](docs/safety.md).

## For contributors

- A skill is a folder in `skills/` with a `SKILL.md`.
- `python3 scripts/check_tools.py` checks that every tool a skill or agent names exists in `tools.json`.
- `python3 scripts/sync_tools.py <registry.py> <commit>` regenerates `tools.json` from the WizzHire server's registry, leaving out staff-only tools.
- `claude plugin validate .` checks the plugin and marketplace files.
- Run the cases in [evals/README.md](evals/README.md) on a staging company before a release.

## License

MIT
