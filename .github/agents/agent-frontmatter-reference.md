# Custom Agent Frontmatter Reference

This guide explains the 10 supported top-level frontmatter parameters for `.agent.md` files, what each one does, and how to use them effectively.

## 1. description
What it is:
A required discovery string used by the system to decide when this agent should be selected or delegated to.

Purpose:
Improve routing accuracy.

How to use:
- Start with `Use when:` and include task keywords.
- Be specific about domain and output.

Good example:
`description: "Use when: generating technical specifications from canonical project requirements."`

## 2. name
What it is:
Agent display name.

Purpose:
Human-readable identity in agent picker and logs.

How to use:
- Keep it short and role-focused.
- Use title case.

Good example:
`name: "Technical Specifier"`

## 3. tools
What it is:
Allowed tool set for the agent.

Purpose:
Security and focus through least privilege.

How to use:
- Include only tools needed for the role.
- Add MCP tools using exact server key wildcard, for example `figma-context-mcp/*`.
- Keep broad aliases only when required.

Good example:
`tools: [read, edit, search, execute, figma-context-mcp/*]`

## 4. user-invocable
What it is:
Visibility control for direct user selection.

Purpose:
Control whether users can pick this agent manually.

How to use:
- Set `true` for user-facing specialist agents.
- Set `false` for internal subagents only.

Good example:
`user-invocable: true`

## 5. model
What it is:
Model selection for this agent.

Purpose:
Pin capability/cost profile for a specific workflow.

How to use:
- Use single model for consistency.
- Use fallback list for resilience.

Good examples:
`model: "GPT-5 (copilot)"`
`model: ["Claude Sonnet 4.5 (copilot)", "GPT-5 (copilot)"]`

## 6. argument-hint
What it is:
Guidance shown to users about what to pass as input.

Purpose:
Improve invocation quality and reduce ambiguous prompts.

How to use:
- Keep it short and action-oriented.
- Mention expected identifiers, paths, or run IDs.

Good example:
`argument-hint: "Provide requirement file path and RUN_ID."`

## 7. agents
What it is:
Allowlist of subagents this agent can invoke.

Purpose:
Constrain orchestration and prevent accidental delegation sprawl.

How to use:
- Omit to allow all available subagents.
- Set explicit list to enforce workflow boundaries.
- Set empty list to prevent any subagent delegation.

Good examples:
`agents: ["Compliance Reviewer", "Traceability Manager"]`
`agents: []`

## 8. disable-model-invocation
What it is:
Flag to prevent this agent from being invoked as a subagent by other agents.

Purpose:
Protect specialized agents from unintended chaining.

How to use:
- Use `true` when the agent should be manually run only.
- Keep `false` for normal reusable specialists.

Good example:
`disable-model-invocation: false`

## 9. handoffs
What it is:
Structured transitions to other agents.

Purpose:
Enable multi-stage workflows with explicit routing.

How to use:
- Define clear transition points and intent.
- Keep handoff targets minimal and deterministic.

Good practice:
Use handoffs for predictable stage boundaries, such as spec generation to compliance review.

## 10. hooks
What it is:
Lifecycle command hooks that run at specific events.

Purpose:
Automate deterministic checks, guardrails, and post-processing.

How to use:
- Add only stable, fast commands.
- Prefer `PreToolUse` for policy enforcement and `PostToolUse` for formatting or checks.
- Keep timeouts explicit.

Example:
```yaml
hooks:
  PreToolUse:
    - type: command
      command: "./scripts/block-dangerous-cmds.sh"
      timeout: 10
  PostToolUse:
    - type: command
      command: "./scripts/auto-lint.sh"
      timeout: 20
```

## Best-Practice Starter Template

```yaml
---
description: "Use when: <specific task with strong keywords>"
name: "<Role Name>"
tools: [read, search]
user-invocable: true
argument-hint: "Provide <required inputs>."
model: "GPT-5 (copilot)"
---
```

## Real-World Examples From Current Codebase

### Example 1: Technical Specifier Agent
```yaml
---
description: "Use when: generating technical specifications from canonical project requirements."
name: "Technical Specifier"
tools: [read, search, execute, edit]
user-invocable: true
argument-hint: "Enter Jira key (e.g., ABCAPP-123), requirement file path, or press Enter for active file."
agents: ["Compliance Reviewer", "Traceability Manager"]
---
```

### Example 2: Implementation Builder Agent
```yaml
---
description: "Use when: implementing code from approved plans and task files."
name: "Implementation Builder"
tools: [read, search, execute, edit]
user-invocable: true
agents: ["Compliance Reviewer", "Quality Tester", "Traceability Manager"]
---
```

### Example 3: Context Builder Agent
```yaml
---
description: "Use when: creating comprehensive project context with business, technical, and standards documentation from scratch by extracting from source code and applying standards during creation."
name: "Context Builder"
tools: [read, search, execute, edit]
user-invocable: true
---
```

### Example 4: Internal Orchestration Agent (Hidden)
```yaml
---
description: "Internal: Orchestrates GitHub backlog workflows including triage, discovery, sprint planning."
name: "GitHub Backlog Manager"
tools: [read, search, execute, edit]
user-invocable: false
agents: ["Researcher Subagent", "Plan Validator"]
disable-model-invocation: false
---
```

## Best-Practice Checklist

1. Make `description` precise enough to route correctly.
2. Keep `tools` minimal and role-specific.
3. Use exact MCP server keys from `.vscode/mcp.json`.
4. Use `user-invocable: false` for internal orchestration agents.
5. Add `argument-hint` for consistent user input (especially for agents expecting file paths or IDs).
6. Use `agents` allowlist if delegation must be controlled (e.g., spec agents should delegate to Compliance Reviewer).
7. Add hooks only for deterministic and quick checks.
8. Test one real invocation after each frontmatter change.
9. Reference actual agents in your `agents` allowlist (e.g., "Technical Specifier", "Compliance Reviewer").
10. For spec-driven workflows, chain: Specifier → Compliance Reviewer → Planner → Builder → Tester → Documenter.
