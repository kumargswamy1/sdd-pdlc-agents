# Agents Setup

## Purpose
This folder defines GitHub Copilot agents for a generic spec-driven PDLC workflow.

## Agent Files

```text
.github/agents/api-tester.agent.md
.github/agents/context-builder.agent.md
.github/agents/context-updater.agent.md
.github/agents/figma-extractor.agent.md
.github/agents/functional-automation-test.agent.md
.github/agents/implement.agent.md
.github/agents/planner.agent.md
.github/agents/reviewer.agent.md
.github/agents/specify.agent.md
.github/agents/technical-documenter.agent.md
.github/agents/traceability-manager.agent.md
```

## How To Use
Open GitHub Copilot Chat and select the relevant agent from the agent picker.

For existing requirement documents, use the intake prompt:

```text
.github/prompts/intake-to-spec.prompt.md
```

For a new project or missing project context, start with:

```text
Context Builder
```

The intake workflow produces the BRD and detailed requirements artifacts.

## Reusable Prompt Workflows

Use these prompt files in Copilot Chat when supported:

```text
.github/prompts/intake-to-spec.prompt.md
.github/prompts/intake-to-implementation.prompt.md
```
