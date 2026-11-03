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

## Agent Mapping

| Agent | Context files used | Standards and rules used |
| --- | --- | --- |
| [Technical Specifier](agents/specify.agent.md) | [Project](contexts/business-context.md), [Domain](contexts/domain-context.md), [Frontend](contexts/frontend-context.md), [Backend](contexts/backend-context.md), [Testing](contexts/testing-context.md), and other applicable user-provided context. | Direct: [Requirements](rules/requirement-standards.md), [Traceability](rules/traceability-standards.md), [Architecture](rules/architectural-standards.md), [Security and Quality](rules/security-quality-standards.md), [Versioning](rules/versioning-standards.md), [PDLC](rules/pdlc.md), [Specification Gates](rules/specification-execution-gates.md). Shared: [AI Agent Safety](rules/ai-agent-safety.md), [Implementation Gates](rules/implementation-execution-gates.md) for implementation evidence it plans. |
| [Implementation Planner](agents/planner.agent.md) | [Project](contexts/business-context.md), [Domain](contexts/domain-context.md), [Frontend](contexts/frontend-context.md), [Backend](contexts/backend-context.md), [Testing](contexts/testing-context.md), and other applicable user-provided context. | Direct: [Architecture](rules/architectural-standards.md), [Security and Quality](rules/security-quality-standards.md), [Versioning](rules/versioning-standards.md), [Traceability](rules/traceability-standards.md), [PDLC](rules/pdlc.md), [Planning Gates](rules/planning-execution-gates.md). Shared: [AI Agent Safety](rules/ai-agent-safety.md), [Implementation Gates](rules/implementation-execution-gates.md) for planned test evidence and coverage. |
| [Implementation Builder](agents/implement.agent.md) | [Project](contexts/business-context.md), [Domain](contexts/domain-context.md), [Frontend](contexts/frontend-context.md), [Backend](contexts/backend-context.md), [Testing](contexts/testing-context.md), and other applicable user-provided context. | Direct: [Architecture](rules/architectural-standards.md), [Security and Quality](rules/security-quality-standards.md), [Environment](rules/environment-standards.md), [Versioning](rules/versioning-standards.md), [Traceability](rules/traceability-standards.md), [PDLC](rules/pdlc.md), [Implementation Gates](rules/implementation-execution-gates.md). Shared: [AI Agent Safety](rules/ai-agent-safety.md) and other rules applicable to the implementation scope. |
| [API Tester](agents/api-tester.agent.md) | [Backend](contexts/backend-context.md) is required; also [Testing](contexts/testing-context.md), [Project](contexts/business-context.md), [Domain](contexts/domain-context.md), and relevant user-provided API/security context. | Direct: [Security and Quality](rules/security-quality-standards.md), [Environment](rules/environment-standards.md), [Traceability](rules/traceability-standards.md), [MCP Usage](rules/mcp-usage-guide.md). Shared: [AI Agent Safety](rules/ai-agent-safety.md), [Implementation Gates](rules/implementation-execution-gates.md) for API evidence, [PDLC](rules/pdlc.md). |
| [Functional Automation Test](agents/functional-automation-test.agent.md) | [Project](contexts/business-context.md), [Domain](contexts/domain-context.md), [Frontend](contexts/frontend-context.md), [Backend](contexts/backend-context.md), [Testing](contexts/testing-context.md), and other context relevant to the tested components. | The agent definition does not directly name `.github/rules/` files. Shared: [AI Agent Safety](rules/ai-agent-safety.md), [Security and Quality](rules/security-quality-standards.md) for safe test data/security scope, [Implementation Gates](rules/implementation-execution-gates.md) for UI scope/evidence, [Traceability](rules/traceability-standards.md), [PDLC](rules/pdlc.md). |

## Usage Notes

- Use `business-context.md` for approved business intent and expected outcomes. Do not infer expected behavior from the current implementation.
- Use frontend, backend, and testing context only for technical details relevant to the task.
- Apply BIAN, FSDM, ISO 20022, OWASP, and regulatory controls only when applicable to the project scope; the owning rules define their use and evidence.
- A missing or empty required context is a documented gap or handoff, not permission to invent project facts. Preserve conflicts and follow the relevant stage gate.
