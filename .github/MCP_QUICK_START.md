# MCP Quick Start

Jira MCP is configured in `.vscode/mcp.json` through the `jira` server entry. On first use, complete the Atlassian OAuth sign-in requested by VS Code or the MCP client.

The Jira discovery agent expects this exact server key:

```text
jira/*
```

Do not store Jira credentials or tokens in workspace files.

If an approved MCP server is configured, use it to retrieve reference patterns for:
- Existing APIs.
- Existing data models.
- Architecture standards.
- Product metadata.
- Risk and compliance controls.

Do not use MCP to retrieve or expose real customer data.
