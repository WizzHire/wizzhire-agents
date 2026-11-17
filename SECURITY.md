# Security

## Reporting a problem

Please report security problems privately through GitHub: open the **Security** tab of this repository and choose **Report a vulnerability**, or go straight to [the private report form](https://github.com/WizzHire/wizzhire-agents/security/advisories/new). Do not open a public issue.

This covers the skills and agents in this repository and the WizzHire MCP connector they use (`https://api.wizzhire.com/mcp`). Examples worth reporting:

- a skill or agent that can be made to change data without the person's confirmation;
- a way for text inside a CV, document or message to make Claude act on it;
- a tool returning data the connected person should not be able to see, such as candidate contact details;
- anything that lets one company's data reach another company.

We acknowledge reports within three working days and keep you updated until the issue is fixed. Please give us reasonable time to fix a problem before discussing it publicly.

## Supported versions

Only the latest release receives fixes. Claude Code updates the plugin from this repository; claude.ai and Claude Desktop users should upload the skill zips from the latest release.
