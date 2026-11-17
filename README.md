# WizzHire skills and agents for Claude

Ready-made skills that run whole WizzHire jobs from Claude: bring in your staff list, open a role, clear the candidates waiting on you, decide leave, start onboarding. They work through the WizzHire MCP connector, with your own access, and a person makes every decision.

WizzHire is ATS, HR and CRM software for companies. Learn more at [wizzhire.com](https://wizzhire.com/en).

## The skills

| Skill | Ask it | Module |
|---|---|---|
| `getting-started` | "Set up WizzHire for us." | All |
| `staff-import` | "Here is our staff list in Excel, bring everyone in." | HR |
| `crm-import` | "Import our clients and open deals from this sheet." | CRM |
| `job-opener` | "We need two senior accountants in Sarajevo, hybrid." | ATS |
| `review-desk` | "Who is waiting on me today?" | ATS |
| `onboarding-concierge` | "Start onboarding for the three people joining on the 1st." | HR |
| `leave-desk` | "What leave is waiting for me, and who else is off?" | HR |
| `manager-brief` | "What do I need to know about my team this week?" | HR |
| `my-hr` | "How many days off do I have left?" | HR |

Every skill also understands Bosnian, Croatian and Serbian asks, and replies in the language you write in.

Claude Code also gets two agents: `wizzhire-importer` for long imports from a local file, and `wizzhire-weekly` for a manager's weekly read.

## 1. Connect WizzHire to Claude

The skills need the WizzHire connector. In Claude, open **Customize > Connectors > Add custom connector** and enter:

```
https://api.wizzhire.com/mcp
```

Sign in with your WizzHire account and answer the questions about which modules (ATS, HR, CRM) Claude may read and change. Full steps: [wizzhire.com/en/features/ai](https://wizzhire.com/en/features/ai).

## 2. Install the skills

### Claude Code

```
/plugin marketplace add wizzhire/wizzhire-agents
/plugin install wizzhire@wizzhire
```

The plugin brings the connector with it. Run `/mcp`, pick `wizzhire` and sign in. Then ask in plain words, or call a skill directly, for example `/wizzhire:leave-desk`.

### claude.ai and Claude Desktop

1. Download the skill zips from the latest [release](../../releases) (or run `sh scripts/package_skills.sh`).
2. Open **Customize > Skills**, choose **+**, then **Upload a skill**, and pick one zip. Repeat for each skill you want.
3. Make sure code execution is on and the WizzHire connector is connected.

## What the skills never do

They never hire, reject or move a candidate, publish a job, launch a review or message a candidate. Those actions are not available to Claude at all and stay in the WizzHire app. They ask before every change, run a check first wherever WizzHire offers one, and treat CVs and documents as data, never as instructions. Details: [docs/safety.md](docs/safety.md).

## For contributors

- A skill is a folder in `skills/` with a `SKILL.md`.
- `python3 scripts/check_tools.py` checks that every tool a skill names exists in `tools.json`, which is generated from the WizzHire server.
- `claude plugin validate .` checks the plugin and marketplace files.
- Run the cases in [evals/README.md](evals/README.md) on a staging company before a release.

## License

MIT
