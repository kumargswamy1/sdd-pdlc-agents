---
title: Context Playbook
description: Context files and repository rules used by the five core SDLC agents.
---

## Scope

This playbook covers only Technical Specifier, Implementation Planner, Implementation Builder, API Tester, and Functional Automation Test. It assumes Context Builder has created the canonical context files. If a context is not applicable to a project, record `N/A` with evidence rather than treating it as an unexplained gap.

All agents inherit the repository-wide instructions in [copilot-instructions.md](copilot-instructions.md): inspect `.github/contexts/`, read context relevant to the task, and follow applicable `.github/rules/`. The rules column distinguishes files directly named by an agent from shared rules applicable through the stage workflow.

## Context Files

| Context file | Intended content |
| --- | --- |
| [business-context.md](contexts/business-context.md) | Canonical business requirements, rules, workflows, constraints, assumptions, decisions, stakeholders, and acceptance criteria. |
| [domain-context.md](contexts/domain-context.md) | Supplemental industry terminology and references; does not replace project requirements. |
| [frontend-context.md](contexts/frontend-context.md) | Frontend stack, architecture, UI behavior/design, accessibility, responsive behavior, and conventions. |
| [backend-context.md](contexts/backend-context.md) | Backend stack, services, API contracts, data, integrations, security implementation, deployment, and operations. |
| [testing-context.md](contexts/testing-context.md) | Test frameworks, organization, fixtures, CI, coverage configuration, and verification strategy. |
| Additional user context | Relevant user-provided Markdown, Word, PDF, or other designated context; preserve source and authorship. |

## Context Matrix

| Agent | Required context | Conditional context |
| --- | --- | --- |
| [Technical Specifier](agents/specify.agent.md) | [Business](contexts/business-context.md); [frontend](contexts/frontend-context.md), [backend](contexts/backend-context.md), and [testing](contexts/testing-context.md) to assess scope and define applicable specifications. | [Domain](contexts/domain-context.md) and user-provided context when relevant to the story, product, or jurisdiction. |
| [Implementation Planner](agents/planner.agent.md) | [Business](contexts/business-context.md); frontend/backend context for affected surfaces; [testing](contexts/testing-context.md) for verification planning. | [Domain](contexts/domain-context.md) when domain rules affect tasks; additional user context for affected areas. |
| [Implementation Builder](agents/implement.agent.md) | [Business](contexts/business-context.md); the technical context for each changed surface; [testing](contexts/testing-context.md) when implementing required tests. | [Domain](contexts/domain-context.md) when implementation depends on domain-specific rules; other context when directly applicable. |
| [API Tester](agents/api-tester.agent.md) | When `API In Scope: YES`: [Backend](contexts/backend-context.md), [Testing](contexts/testing-context.md), and [Business](contexts/business-context.md) for expected outcomes. | [Domain](contexts/domain-context.md) and user-provided API/security context when they affect the endpoint or test data. |
| [Functional Automation Test](agents/functional-automation-test.agent.md) | When `UI In Scope: YES`: [Business](contexts/business-context.md), [Frontend](contexts/frontend-context.md), and [Testing](contexts/testing-context.md) for expected UI behavior and test conventions. | [Backend](contexts/backend-context.md) when tested flows depend on APIs or backend outcomes; [Domain](contexts/domain-context.md) when needed to validate domain behavior. |

## Rules Matrix

All agents inherit [copilot-instructions.md](copilot-instructions.md), [AI Agent Safety](rules/ai-agent-safety.md), and applicable workflow policy in [PDLC](rules/pdlc.md). Direct rules below are named in the agent definition; conditional rules apply only when the described concern is in scope.

| Agent | Directly named rules | Conditional or shared rules |
| --- | --- | --- |
| [Technical Specifier](agents/specify.agent.md) | [Requirements](rules/requirement-standards.md), [Traceability](rules/traceability-standards.md), [Architecture](rules/architectural-standards.md), [Coding Standards](rules/coding-standards.md) when specifying implementation/test-code conventions, [Security and Quality](rules/security-quality-standards.md), [Versioning](rules/versioning-standards.md), [PDLC](rules/pdlc.md), [Specification Gates](rules/specification-execution-gates.md), and [Implementation Gates](rules/implementation-execution-gates.md) for test applicability/evidence requirements. | [Figma Selection](rules/figma-interactive-selection-guide.md) when interactive screen selection is used; [MCP Usage](rules/mcp-usage-guide.md) when MCP tools are used; [Environment](rules/environment-standards.md) when specifying configuration or secrets. |
| [Implementation Planner](agents/planner.agent.md) | [Architecture](rules/architectural-standards.md), [Coding Standards](rules/coding-standards.md) for implementation/test-code tasks, [Security and Quality](rules/security-quality-standards.md), [Versioning](rules/versioning-standards.md), [Traceability](rules/traceability-standards.md), [PDLC](rules/pdlc.md), [Planning Gates](rules/planning-execution-gates.md), and [Implementation Gates](rules/implementation-execution-gates.md) for unit-test tasks, evidence, and coverage planning. | [Environment](rules/environment-standards.md) when deployment or configuration tasks are in scope; [MCP Usage](rules/mcp-usage-guide.md) when using MCP. |
| [Implementation Builder](agents/implement.agent.md) | [Architecture](rules/architectural-standards.md), [Coding Standards](rules/coding-standards.md), [Security and Quality](rules/security-quality-standards.md), [Environment](rules/environment-standards.md), [Versioning](rules/versioning-standards.md), [Traceability](rules/traceability-standards.md), [PDLC](rules/pdlc.md), [Implementation Gates](rules/implementation-execution-gates.md). | [MCP Usage](rules/mcp-usage-guide.md) when using MCP; [Figma Selection](rules/figma-interactive-selection-guide.md) only if the workflow requires interactive design selection. |
| [API Tester](agents/api-tester.agent.md) | [Coding Standards](rules/coding-standards.md) for generated/modified test code, [Security and Quality](rules/security-quality-standards.md), [Environment](rules/environment-standards.md), [Traceability](rules/traceability-standards.md), [MCP Usage](rules/mcp-usage-guide.md). | [Implementation Gates](rules/implementation-execution-gates.md) for API evidence and applicable handoff; [Versioning](rules/versioning-standards.md) when testing compatibility; [Architecture](rules/architectural-standards.md) when needed to interpret an API contract. |
| [Functional Automation Test](agents/functional-automation-test.agent.md) | [Coding Standards](rules/coding-standards.md) when generating/modifying executable tests. | [Implementation Gates](rules/implementation-execution-gates.md) for UI scope and evidence; [Security and Quality](rules/security-quality-standards.md) for safe test data/security scenarios; [Traceability](rules/traceability-standards.md); [Environment](rules/environment-standards.md) when test configuration is involved; [MCP Usage](rules/mcp-usage-guide.md) when using MCP. |

## Interpretation

- Contexts are scope-dependent, not a checklist requiring every file for every agent. An agent should read the business source and the technical contexts needed to understand its approved work.
- Repository-wide AI safety and relevant stage rules still apply even when they are not repeated in an agent's direct read list.
- Apply BIAN, FSDM, ISO 20022, OWASP, and regulatory controls only when the product, data, integration, or change makes them applicable.
- A missing context needed for a decision is a gap or handoff; it is not permission to invent project facts. Do not read unrelated context merely to satisfy the matrix.
