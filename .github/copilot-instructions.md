# Copilot Instructions - Spec-Driven Development

This repository uses a spec-driven PDLC workflow for software development.

## Default Behavior
- Prefer the agents in `.github/agents/`.
- Follow centralized rules in `.github/rules/`.
- Use templates in `.github/templates/`.
- Preserve traceability through every artifact.
- Treat GitHub issues, branches, commits, and pull requests as trace metadata when available.

## Context Management (Prerequisite for All Workflows)

**Context creation and maintenance is foundational to all PDLC workflows.**

### Context Loading For Every Agent

Before starting a task, every agent must inspect `.github/contexts/` and read the files relevant to its scope. Keep using the existing context filenames, and also consider any additional files added to the folder. Read explicitly designated Word/PDF context files as well as Markdown files; use the project-context index when available. Do not load unrelated files. Treat context as guidance alongside task requirements and current source evidence. Context Builder creates new context only, Context Updater owns context maintenance, and other agents must not modify context files unless explicitly assigned that work.

### Initial Context Setup
For new projects or when context does not exist, use a single unified agent:

```text
Context Builder (Unified - Merged)
  → Uses a Confluence link when provided; otherwise uses attached Word/PDF documents
  → Inspects available legacy project documentation, source code, configuration, and tests
  → Extracts tech stack from source code (package.json, config files, folder structure)
  → Gathers business and client-domain context from supplied sources
  → Applies standards DURING context creation (integrated, not separate)
  → Creates `.github/contexts/project-context.md` (business + tech baseline with standards refs)
  → Creates `.github/contexts/domain-context.md` (industry/domain context and business rules)
  → Creates `.github/contexts/frontend-context.md` (patterns extracted from code)
  → Creates `.github/contexts/backend-context.md` (patterns extracted from code)
  → Creates `.github/contexts/testing-standards.md` (patterns extracted from code)
  → Preserves and indexes additional user-provided standards under `.github/contexts/`
  → Creates `requirement/Context_{ProjectName}.md` (detailed context with CTX-* IDs)
  → Updates `requirement/Traceability_Matrix.md` with CTX-* IDs
```

**No MCP file validation needed** - all context extracted directly from source code and project structure.
**Standards are embedded, not separate** - as context is discovered, standards are applied to ensure consistency.

### Context Maintenance
As project evolves, keep context synchronized:

```text
Context Updater
  (triggered by: Confluence/document changes, legacy project or code changes, domain guidance, custom standards, or user request)
  → reviews source documents, project structure, configuration, and all context files
  → detects changes (MINOR/MODERATE/MAJOR)
  → updates project/domain/technology/testing context and affected user-provided standards
  → tracks changes with CTX-UPDATE-* IDs
  → escalates MAJOR changes for approval
  → updates `requirement/Traceability_Matrix.md`
```

## Human-Initiated Stages
- Every PDLC agent is started manually by a human. Each agent produces its output, stops, and emits `NEXT_STEP` naming the next agent; the human reviews the output and runs that agent.
- No agent or prompt may start the next stage automatically. Agents have `disable-model-invocation: true` and must not be invoked as subagents. The only exception is Figma Extractor, which Technical Specifier may invoke within the specification stage.

## Required Flow
For existing source requirement folders:

```text
[Context exists per Context Builder]
-> Requirement Intake Consolidator
-> Traceability Manager
-> Technical Specifier
-> Compliance Reviewer
-> Implementation Planner
-> Compliance Reviewer
-> Implementation Builder
-> API Tester (tests every API in output/{RUN_ID}/specify/spec.md when `API In Scope: YES`)
-> Functional Automation Test (tests every UI behavior in output/{RUN_ID}/specify/spec.md when `UI In Scope: YES`)
-> Quality Tester
-> Compliance Reviewer
-> Technical Documenter
-> Traceability Manager
```

For new business problems:

```text
[Context exists per Context Builder]
-> Context Clarifier
-> BRD Generator
-> Requirements Expander
-> User Story Generator
-> Technical Specifier
-> Implementation Planner
-> Implementation Builder
-> API Tester (tests every API in output/{RUN_ID}/specify/spec.md when `API In Scope: YES`)
-> Functional Automation Test (tests every UI behavior in output/{RUN_ID}/specify/spec.md when `UI In Scope: YES`)
-> Quality Tester
-> Compliance Reviewer
-> Technical Documenter
-> Traceability Manager
```

## Design Evidence Handling
- Figma is optional when the story has no frontend task.
- Figma failures (MCP error, rate limit, auth) never block. Technical Specifier falls back to Jira/Confluence screenshots or manual uploads, assigns `SCR-*` screen IDs, and records `Design Source: Manual upload (no Figma link)`.
- Planning and implementation proceed with manual-upload design evidence and carry the design-source note forward.
- Only a frontend story with no design evidence at all (`DESIGN_EVIDENCE_STATUS: PENDING_MANUAL_UPLOAD`) blocks planning and implementation until screenshots are added to `output/{RUN_ID}/specify/figma/png/screens/` and Technical Specifier is re-run.

## Parallel Context Updates
**At any point in the PDLC, a human may run Context Updater to:**
- Sync technology versions and dependencies
- Sync changes from Confluence pages or attached Word/PDF sources
- Update client industry/domain context and user-provided standards
- Update architectural guidance when code patterns evolve
- Flag conflicts between detected state and approved specs/plans
- Maintain alignment between project reality and documented standards

## Domain-Specific Controls
Apply regulatory and domain controls only when in scope:
- Privacy controls (e.g., GDPR, PDPA, CCPA).
- KYC and AML checks when applicable.
- Customer risk profiling and suitability assessments.
- Consent and disclosure capture.
- Approval workflows (e.g., maker-checker).
- Role-based access control and audit trails.
- Regulatory reporting evidence and compliance.

## Data Protection
Never include real customer PII, sensitive account information, credentials, secrets, tokens, or production data in generated artifacts, examples, tests, commits, PR descriptions, or documentation.
