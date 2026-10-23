# Project Context Record — SDD PDLC Agents

**Project:** Spec-Driven PDLC Agents (`sdd-pdlc-agents`)  
**Created:** 2026-10-22  
**Status:** Source-backed repository context; no product BRD supplied  
**Primary context:** `.github/contexts/project-context.md`

## Purpose and Scope

This record captures verified context about the repository's agent-driven software delivery workflow and local design/token-analysis tools. The repository is not itself a deployed product application. Client identity, end-user product workflows, product success measures, and a product BRD are `N/A` because no such source documents were provided.

## Verified Context Facts

| CTX ID | Context fact | Evidence |
|---|---|---|
| CTX-PROJECT-001 | Repository provides reusable spec-driven PDLC agent definitions, prompts, rules, templates, and helper scripts. | `.github/README.md`, `.github/agents/`, `.github/rules/`, `.github/prompts/`, `.github/scripts/` |
| CTX-FLOW-001 | Human participants manually initiate each stage; agents stop at defined handoffs rather than auto-starting later stages. | `.github/rules/pdlc.md`, `.github/copilot-instructions.md` |
| CTX-REVIEW-001 | Critical/High/Medium findings block until remediation/re-review or explicit human acceptance; Low-only `FAIL` emits warning and may proceed; mixed severities follow the highest. | `.github/rules/pdlc.md` |
| CTX-TRACE-001 | Workflow traceability spans context, BRD, requirements, stories, specs, tasks, code, tests, reviews, and docs. | `.github/rules/traceability-standards.md` |
| CTX-TECH-001 | Python implements Figma REST/extraction CLI; Node scripts analyze local Copilot logs and export token-use estimates. | `.github/scripts/*.py`, `.github/scripts/*.js` |
| CTX-FIGMA-001 | Figma pipeline uses parent JSON/PNG requests and local screen cropping, reports effective screen nodes and artifact paths. | `.github/scripts/figma_requirements_pipeline.py`, `.github/scripts/README.md` |
| CTX-TOKEN-001 | Token tools report observed usage counters where present and otherwise character-based estimates; estimates are not exact tokens. | `.github/scripts/estimate_agent_loop_tokens.js`, `.github/scripts/export_agent_token_estimates_csv.js` |
| CTX-DOMAIN-001 | No client/product domain is confirmed; banking-related rules are conditional examples for downstream projects. | `.github/ARCHITECTURE.md`, `.github/rules/security-quality-standards.md` |
| CTX-DOMAIN-002 | Banking/privacy controls are conditional guidance, not a confirmed client scope. | `.github/rules/security-quality-standards.md` |
| CTX-BUSINESS-001 | Human-controlled lifecycle and evidence-backed handoff rules. | `.github/rules/pdlc.md` |
| CTX-COMPLIANCE-001 | Severity-based review stop/warning behavior. | `.github/rules/pdlc.md` |
| CTX-STAKEHOLDER-001 | Human participants initiate stages; Copilot agents perform bounded roles. | `.github/copilot-instructions.md`, `.github/agents/*.agent.md` |
| CTX-FRONTEND-001 | No product UI source, theme implementation, or rendered screens are present. | Repository inventory; `.github/contexts/frontend-context.md` |
| CTX-BACKEND-001 | No product server, API, database, or application persistence exists; Figma REST calls are tool integrations only. | Repository inventory; `.github/contexts/backend-context.md` |
| CTX-TEST-001 | No automated test files, runner, or CI test configuration were found; a syntax-check command is documented for the Figma pipeline. | `.github/scripts/README.md`; repository inventory |
| CTX-SECURITY-001 | Figma token is runtime secret input; local Copilot logs/resources may contain sensitive conversation material. | `.github/scripts/figma_rest_cli.py`, token-analysis scripts |
| CTX-DESIGN-001 | Product color palette, typography, spacing, component library, and theme values are `N/A`; only downstream generic UI guidance and Figma ingestion tooling exist. | `.github/rules/architectural-standards.md`, `.github/scripts/` |
| CTX-QUALITY-001 | Downstream changed frontend/backend surfaces require tests and independently enforced 80% supported coverage metrics. | `.github/rules/implementation-execution-gates.md`, `.github/rules/security-quality-standards.md` |

## Open Questions / Unavailable Facts

- Product/client BRD, user stories, domain-specific business calculations, personas, approval owners, deployment environment, and production service integrations: `N/A` — not present in source material.
- Exact Python/Node supported versions, release version, CI/test execution, and full deployment strategy: `N/A` — no package/release/CI configuration found.
- Actual product UI screens and visual design values: `N/A` — no product UI or Figma design artifact supplied.

No assumptions were added to fill these gaps.

## Update History

| Date | Phase | Changes | Detector | Impact Level |
|---|---|---|---|---|
| 2026-10-22 | Initial context creation | Recorded repository features, workflow rules, technology/tooling, design/UI/backend/test scope, and evidence-backed N/A values. | Manual source review | MODERATE |
