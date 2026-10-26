---
description: "Start workspace Jira MCP tools for story retrieval and approved QA test case creation."
---

# MCP Quick Start

Jira MCP is configured in [mcp.json](../.vscode/mcp.json) through the `jira` server
entry, using the local `uvx mcp-atlassian` stdio provider, not Atlassian remote OAuth.
Install `uv` so `uvx` is on the VS Code process PATH. The first server start may
download the provider package.

1. Run **MCP: List Servers** in the VS Code Command Palette.
2. Select **jira**, then **Start** or **Restart** and approve the server trust prompt.
3. Enter the Jira base URL, username/email and API token when prompted. Username
   and token prompts are masked; do not paste credentials into chat or source files.
4. Open the chat tool picker (**Configure Tools**) and confirm the `jira` tools are
   enabled. Select **QA Test Case Generator**; start a new chat if the existing
   session still has a stale tool list.
5. Request test cases with one story key. Review the local cases before explicitly
   approving Jira Task and Tests-link creation.

The QA agent allows `jira/jira_get_issue`, `jira/jira_search`,
`jira/jira_get_project_issue_types`, `jira/jira_get_create_fields`,
`jira/jira_get_link_types`, `jira/jira_create_issue` and `jira/jira_create_issue_link`.
Other agents that use `jira/*` still refer to this same server key. The local
provider does not expose the remote provider's `getJiraIssue`/`createJiraIssue`
method names.

If startup fails, inspect the server's **Show Output** without sharing credentials.
Missing tools, authentication failures, missing create permissions or an unavailable
Tests link type must be reported explicitly; configuration alone does not prove a
successful Jira connection. If an API token was previously saved in the workspace,
rotate it in Jira and enter its replacement through the prompt.

If an approved MCP server is configured, use it to retrieve reference patterns for:

- Existing APIs.
- Existing data models.
- Architecture standards.
- Product metadata.
- Risk and compliance controls.

Do not use MCP to retrieve or expose real customer data.
