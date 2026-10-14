# MCP Configuration

The project includes a Jira MCP server entry at `.vscode/mcp.json`:

```json
{
	"servers": {
		"jira": {
			"type": "http",
			"url": "https://mcp.atlassian.com/v1/mcp"
		}
	}
}
```

The Atlassian remote server uses OAuth through the MCP client. Do not add Jira credentials, tokens, or customer data to this repository.

Use MCP only when configured with approved sources such as:
- Jira project and issue metadata through the configured `jira` server.
- Architecture knowledge base.
- API catalogue.
- Product or risk-rule reference data.
- Compliance control library.
- Internal design-system reference.

Do not query, expose, or generate real customer data, account numbers, holdings, credentials, secrets, tokens, or production data.
