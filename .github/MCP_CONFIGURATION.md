---
description: "Workspace mcp-atlassian Jira server configuration and credential input handling."
---

# MCP Configuration

The project includes a Jira MCP server entry at `.vscode/mcp.json`:

```json
{
	"servers": {
		"jira": {
			"type": "stdio",
			"command": "uvx",
			"args": ["mcp-atlassian"],
			"env": {
				"JIRA_URL": "${input:jira-url}",
				"JIRA_USERNAME": "${input:jira-username}",
				"JIRA_API_TOKEN": "${input:jira-api-token}"
			}
		}
	}
}
```

This excerpt omits the unchanged Playwright server and the top-level `inputs` array;
use the full [workspace configuration](../.vscode/mcp.json), not this excerpt as a
replacement file. Inputs are VS Code `promptString` entries; username and API token
set `password: true`. The local provider uses these supplied credentials, not
remote-server OAuth. Do not add Jira credentials, tokens, or customer data to this
repository.

The [QA agent](agents/qa-test-case-generator.agent.md) explicitly allows this
server's issue search/read, project/create/link metadata, issue creation and link
creation tools. The linked QA rules/instructions use the same `jira_*` names.
Jira Tasks and Tests links are created only after explicit approval of generated
test cases. See [startup and troubleshooting](MCP_QUICK_START.md) to restart the
server, enable tools and refresh a chat's tool list.

Use MCP only when configured with approved sources such as:
- Jira project and issue metadata through the configured `jira` server.
- Architecture knowledge base.
- API catalogue.
- Product or risk-rule reference data.
- Compliance control library.
- Internal design-system reference.

Do not query, expose, or generate real customer data, account numbers, holdings, credentials, secrets, tokens, or production data.
