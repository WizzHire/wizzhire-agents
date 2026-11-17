# Changelog

## Unreleased

- "Try it without installing": connector steps and starter prompts in the README, and [PROMPTS.md](PROMPTS.md) with 20 prompts for every hiring flow.
- Connector instructions now say **Settings > Plugins > Add custom connector**.
- Issue templates, a security policy and this changelog.
- The tool check now also checks arguments and allowed values, not only tool names.

## v0.3.0 (2026-11-17)

- Six more hiring skills: `candidate-brief`, `pipeline-blockers`, `hiring-tasks`, `channel-report`, `job-ad-check`, `client-recruiting-report`.
- Four hiring agents for Claude Code, read only: `hiring-analyst`, `candidate-researcher`, `role-designer`, `talent-matcher`.
- [docs/ats-coverage.md](docs/ats-coverage.md): every hiring flow and what covers it.
- `scripts/sync_tools.py` regenerates the tool list and leaves out staff-only tools.

## v0.2.0 (2026-11-17)

- Six hiring skills: `screening-form`, `shortlist`, `interview-kit`, `team-decision`, `talent-pool`, `hiring-status`.
- README leads with creating an account, then connecting, then installing.
- `review-desk` no longer claims to brief against job requirements the tools could not read.

## v0.1.0 (2026-11-17)

- First release: `getting-started`, `staff-import`, `crm-import`, `job-opener`, `review-desk`, `onboarding-concierge`, `leave-desk`, `manager-brief`, `my-hr`, and the agents `wizzhire-importer` and `wizzhire-weekly`.
