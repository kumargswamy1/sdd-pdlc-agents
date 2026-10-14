# Agents Setup

## Purpose
This folder defines GitHub Copilot agents for a generic spec-driven PDLC workflow.

## Agent Files

```text
.github/agents/requirement-intake-consolidator.agent.md
.github/agents/context-clarifier.agent.md
.github/agents/brd-generator.agent.md
.github/agents/requirements-expander.agent.md
.github/agents/user-story-generator.agent.md
.github/agents/specify.agent.md
.github/agents/planner.agent.md
.github/agents/implement.agent.md
.github/agents/reviewer.agent.md
.github/agents/tester.agent.md
.github/agents/technical-documenter.agent.md
.github/agents/traceability-manager.agent.md
.github/agents/context-standards-builder.agent.md
```

## How To Use
Open GitHub Copilot Chat and select the relevant agent from the agent picker.

For existing docs, start with:

```text
Requirement Intake Consolidator
```

For a new business problem, start with:

```text
Context Clarifier
```

## Reusable Prompt Workflows

Use these prompt files in Copilot Chat when supported:

```text
.github/prompts/intake-to-spec.prompt.md
.github/prompts/intake-to-implementation.prompt.md
```
