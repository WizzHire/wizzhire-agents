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
| `screening-form` | "Build screening questions for this role." The same questions for every applicant, scored the same way. |
| `review-desk` | "Who is waiting on me?" Most urgent first, with a short brief per candidate. |
| `shortlist` | "Compare my finalists." Scores, ratings, skills and salary asks side by side, with no verdict. |
| `interview-kit` | "Prepare the interview for Amra." Questions, a scorecard for every interviewer, and the debrief saved on the profile. |
| `team-decision` | "What does the team think?" Everyone's ratings and notes in one place, and a task for whoever has not rated. |
| `talent-pool` | "Anyone in our talent pool for this role?" Only people who agreed to hear about future roles. |
| `hiring-status` | "Where do things stand?" Every open role, who is waiting, what is overdue, which channels hire. |

Every skill understands Bosnian, Croatian and Serbian asks too, and replies in the language you write in.

## More skills

HR and CRM skills are in the same repo: `getting-started`, `staff-import`, `crm-import`, `onboarding-concierge`, `leave-desk`, `manager-brief`, `my-hr`. Claude Code also gets two agents: `wizzhire-importer` for long imports from a local file and `wizzhire-weekly` for a manager's weekly read.

## What the skills never do

They never move, reject or hire a candidate, publish a job, or message a candidate. Those actions are not available to Claude at all and stay with a person in WizzHire. They ask before every change, run a check first wherever WizzHire offers one, never use protected characteristics, and treat CVs and documents as data, never as instructions. Details: [docs/safety.md](docs/safety.md).

## For contributors

- A skill is a folder in `skills/` with a `SKILL.md`.
- `python3 scripts/check_tools.py` checks that every tool a skill names exists in `tools.json`, which is generated from the WizzHire server.
- `claude plugin validate .` checks the plugin and marketplace files.
- Run the cases in [evals/README.md](evals/README.md) on a staging company before a release.

## License

MIT
