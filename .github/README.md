# SDLC Agents - Complete Usage Guide

This document describes all available agents in the spec-driven development lifecycle (SDLC) workflow and how to use them.

## Overview

The agents are organized into a sequential SDLC workflow that transforms business requirements into implemented, tested, and documented code. Each agent is specialized for a specific phase and reads/writes standardized artifacts with trace IDs. Run artifacts are written under `output/{RUN_ID}/`.

## Agent Inventory

| # | Agent | File | Phase | Primary Input | Primary Output |
|---|-------|------|-------|---------------|----------------|
| 1 | Context Builder | `context-builder.agent.md` | Context | Confluence, Word/PDF, source code | `.github/contexts/*`, `requirement/Context_{ProjectName}.md` |
| 2 | Context Updater | `context-updater.agent.md` | Context (continuous) | Source/doc/dependency changes | Updated `.github/contexts/*`, `CTX-UPDATE-*` |
| 3 | Figma Extractor | `figma-extractor.agent.md` | Design support | Requirement file with Figma links, `RUN_ID` | `output/{RUN_ID}/specify/figma/` |
| 4 | Technical Specifier | `specify.agent.md` | Specification | Jira key or requirement file | `output/{RUN_ID}/specify/` |
| 5 | Implementation Planner | `planner.agent.md` | Planning | `output/{RUN_ID}/specify/` | `output/{RUN_ID}/plan/` |
| 6 | Implementation Builder | `implement.agent.md` | Implementation | `output/{RUN_ID}/plan/tasks.md` | Source code, unit tests, `output/{RUN_ID}/implement/` |
| 7 | API Tester | `api-tester.agent.md` | Backend API testing | `output/{RUN_ID}/plan/contracts/backend-apis.json` | `<backend-root>/test/api/`, `output/{RUN_ID}/api-tests/` |
| 8 | Functional Automation Test | `functional-automation-test.agent.md` | Component functional testing | `output/{RUN_ID}/plan/frontend/components.md` | `output/{RUN_ID}/functional-tests/` |
| 9 | Quality Tester | `tester.agent.md` | User-workflow QA | Spec, `output/{RUN_ID}/plan/tests/scenarios.md` | `TEST-*` suites and reports |
| 10 | Compliance Reviewer | `reviewer.agent.md` | Review (gates) | Specs, plans, code, tests, docs | `REVIEW-*` findings and status |
| 11 | Technical Documenter | `technical-documenter.agent.md` | Documentation | Spec, components, implementation | `DOC-*` documentation |
| 12 | Traceability Manager | `traceability-manager.agent.md` | Traceability | All artifacts | `requirement/Traceability_Matrix.md` |

All agents are user-invocable. The Playwright-based testing agents (API Tester, Functional Automation Test) use the `playwright` MCP server defined in `.vscode/mcp.json`.

## Agent Workflow Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                      SPEC-DRIVEN DEVELOPMENT FLOW                   │
└─────────────────────────────────────────────────────────────────────┘

Step 1: Context Foundation (prerequisite)
   ↓
   Context Builder
   Context Updater (runs continuously)
   ↓
Step 2: Requirement Intake
   ↓
   Requirement Intake Consolidator (role, see intake prompts)
   Traceability Manager (intake gate)
   ↓
Step 3: Specification
   ↓
   Figma Extractor (when the requirement has Figma links)
   Technical Specifier
   Compliance Reviewer (spec gate)
   ↓
Step 4: Planning
   ↓
   Implementation Planner
   Compliance Reviewer (plan gate)
   ↓
Step 5: Implementation
   ↓
   Implementation Builder (code + unit tests)
   ↓
Step 6: Backend API Testing
   ↓
   API Tester (every API in plan/contracts/backend-apis.json)
   ↓
Step 7: Component Functional Automation
   ↓
   Functional Automation Test (every component in plan/frontend/components.md)
   ↓
Step 8: Quality Assurance
   ↓
   Quality Tester (user-workflow testing)
   ↓
Step 9: Review & Compliance
   ↓
   Compliance Reviewer (code gate)
   ↓
Step 10: Documentation & Traceability
   ↓
   Technical Documenter
   Traceability Manager (final reconciliation)
```

Compliance Reviewer gates stop the flow on Critical findings. Context Updater can run at any point to resync context with the project.

### Design Evidence Rules

| Situation | Spec | Plan and Implementation |
|-----------|------|-------------------------|
| No frontend task (`UI In Scope = NO`) | Figma/screenshots optional (`NOT_REQUIRED`) | Proceed |
| Figma link works | Uses live Figma artifacts | Proceed |
| Figma fails or no Figma link, screenshots from Jira/Confluence or manual upload | Uses screenshots with `SCR-*` IDs (`AVAILABLE`) | Proceed, marked `Design Source: Manual upload (no Figma link)` |
| Frontend in scope, no design evidence at all | Spec created with `PENDING_MANUAL_UPLOAD` | Blocked until screenshots are added and Technical Specifier is re-run |

---

## Agents by Phase

### Phase 1: Context & Foundation

#### **Context Builder**
**File:** `context-builder.agent.md`

**When to use:** 
- Creating comprehensive project context from scratch
- Starting a new project or onboarding a new codebase
- Establishing business, technical, and standards documentation

**What it does:**
- Uses a Confluence link when provided, otherwise attached Word/PDF documents
- Inspects available legacy project documentation, source code, configuration, and tests
- Gathers business, client-domain, stakeholder, and compliance context
- For greenfield projects: prompts user for tech stack and business overview
- Generates tech-specific standards files with best practices
- Preserves and indexes additional user-provided standards under `.github/contexts/`
- Creates unified project context with CTX-* trace IDs

**Output files created:**
- `.github/contexts/project-context.md`
- `.github/contexts/domain-context.md`
- `.github/contexts/frontend-context.md`
- `.github/contexts/backend-context.md`
- `.github/contexts/testing-standards.md`
- Additional user-provided standards when applicable
- `requirement/Context_{ProjectName}.md`
- Updated `requirement/Traceability_Matrix.md`

**User-invocable:** Yes ✅

---

#### **Context Updater**
**File:** `context-updater.agent.md`

**When to use:**
- When Confluence or attached Word/PDF sources change
- After legacy project, dependency, framework, or folder-structure changes
- When client-domain guidance or user-provided standards change
- When the user or a downstream agent requests a context refresh

**What it does:**
- Reviews source documents, existing project files, and context files
- Identifies breaking changes and new features
- Updates project, domain, frontend, backend, and testing context plus affected user-provided standards
- Creates CTX-UPDATE-* IDs for change tracking
- Alerts on MAJOR impact changes

**Triggers automatically on:**
- `package.json`, `pubspec.yaml`, `requirements.txt` changes
- Folder structure reorganization
- Framework version changes
- Confluence or attached-document changes, when detected
- Domain guidance or `.github/contexts/` standards changes

**User-invocable:** Yes

---

### Phase 2: Specification

#### **Figma Extractor**
**File:** `figma-extractor.agent.md`

**When to use:**
- Before or during specification when the requirement file contains Figma links
- Producing design artifacts that Technical Specifier documents per screen

**What it does:**
- Runs the Python pipeline (`.github/scripts/figma_requirements_pipeline.py`)
- Produces parent JSON, parent PNG, and locally cropped screen PNGs
- Builds the effective screen table and `figma_report.md` with SUCCESS/FAILED status
- Reads `FIGMA_API_KEY` from the workspace `.env`; never writes the key to outputs
- Failures (MCP error, rate limit, auth) are non-blocking: Technical Specifier falls back to user story/Confluence screenshots or manual uploads

**Input:**
- `REQ_FILE` (requirement file with Figma file key and node IDs)
- `RUN_ID`

**Output:**
- `output/{RUN_ID}/specify/figma/` (`json/`, `png/`, `png/screens/`, `figma_report.md`)

**User-invocable:** Yes ✅

---

#### **Technical Specifier**
**File:** `specify.agent.md`

**When to use:**
- Converting requirements into technical specifications
- Starting implementation planning for a requirement
- Taking Jira issues as input and creating specs
- Detailing API contracts, database schemas, integration points

**What it does:**
- Accepts Jira issue keys, requirement files, or PRD files
- Fetches issue details and extracts requirements
- Creates canonical requirement markdown files
- Generates implementation-ready technical specifications
- Maps FR-* (Functional) and NFR-* (Non-Functional) to SPEC-* IDs
- Documents data models, API contracts, interface designs

**Input options:**
- Jira key: `ABCAPP-123`
- File path: `requirement/MyApp_Requirements.md`
- Active file (press Enter)

**Reads from:**
- `.github/contexts/project-context.md`
- `.github/contexts/domain-context.md`
- `.github/contexts/frontend-context.md`
- `.github/contexts/backend-context.md`
- `.github/contexts/testing-standards.md` (if present)

**Output:**
- `output/{RUN_ID}/specify/spec.md` with SPEC-* IDs and per-screen design sections
- `output/{RUN_ID}/specify/compliance-validation.md`
- `output/{RUN_ID}/specify/contracts/frontend-integrations.json`
- `output/{RUN_ID}/specify/contracts/backend-apis.json`
- `output/{RUN_ID}/specify/figma/`, `frontend/`, and `backend/` evidence when applicable
- Updated `requirement/Traceability_Matrix.md`

**User-invocable:** Yes ✅

---

### Phase 3: Planning & Architecture

#### **Implementation Planner**
**File:** `planner.agent.md`

**When to use:**
- Breaking down technical specifications into implementation tasks
- Creating task DAGs (directed acyclic graphs)
- Planning sprints and milestone delivery
- Identifying dependencies between tasks

**What it does:**
- Reads technical specifications (SPEC-* IDs)
- Creates detailed implementation plans with task breakdowns
- Generates task DAGs showing dependencies
- Assigns effort estimates and sequencing
- Maps tasks to TASK-* IDs
- Identifies frontend/backend/testing/documentation tasks
- Plans unit test tasks alongside each implementation task
- Inventories frontend components and backend APIs for downstream testing agents

**Reads from:**
- `output/{RUN_ID}/specify/`
- `.github/contexts/frontend-context.md`
- `.github/contexts/backend-context.md`
- `.github/contexts/testing-standards.md`

**Output:**
- `output/{RUN_ID}/plan/plan.md` and `tasks.md` (with `## Pre-submit checks`)
- `output/{RUN_ID}/plan/data-model.md`
- `output/{RUN_ID}/plan/contracts/frontend-integrations.json`
- `output/{RUN_ID}/plan/contracts/backend-apis.json` (input for API Tester)
- `output/{RUN_ID}/plan/frontend/components.md` (input for Functional Automation Test)
- `output/{RUN_ID}/plan/tests/scenarios.md`
- Updated `requirement/Traceability_Matrix.md`

**User-invocable:** Yes ✅

---

### Phase 4: Implementation

#### **Implementation Builder**
**File:** `implement.agent.md`

**When to use:**
- Implementing code from approved plans
- Starting a specific task from the task file
- Creating features, components, or backend services
- Following established standards and patterns

**What it does:**
- Reads implementation plans (TASK-* IDs)
- Generates production-ready code
- Follows tech-stack-specific standards
- Reuses approved components and libraries
- Creates unit tests as part of implementation
- Matches UI to referenced screenshots/Figma designs using the project theme
- Documents code inline with standards

**Reads from:**
- `output/{RUN_ID}/plan/tasks.md` and `output/{RUN_ID}/plan/frontend/components.md`
- `output/{RUN_ID}/specify/spec.md` and `compliance-validation.md`
- All applicable files in `.github/contexts/`
- `.github/rules/implementation-execution-gates.md`

**Output:**
- Implemented source code files
- Unit tests under `frontend/test/unit/` and `backend/test/unit/`
- `output/{RUN_ID}/implement/frontend/`, `backend/`, and `integration/` evidence
- Updated `requirement/Traceability_Matrix.md` (CODE-* IDs)

**User-invocable:** Yes ✅

---

### Phase 5: Backend API Testing

#### **API Tester**
**File:** `api-tester.agent.md`

**When to use:**
- After backend implementation is complete
- Running API tests for the APIs listed in `output/{RUN_ID}/plan/contracts/backend-apis.json`

**What it does:**
- Reads backend tech stack and API standards from `backend-context.md`
- Tests each planned API and controller with Playwright API testing
- Uses the `playwright` MCP server from `.vscode/mcp.json` for live endpoint discovery
- Reports pass/fail/blocked status, contract drift, and coverage gaps

**Inputs:**
- `RUN_ID`
- `output/{RUN_ID}/plan/contracts/backend-apis.json`
- Implemented backend code and related requirements

**Output:**
- `<backend-root>/test/api/` API test suite
- `output/{RUN_ID}/api-tests/attempt-<n>/` execution evidence
- `APT-*` entries in `requirement/Traceability_Matrix.md`

**User-invocable:** Yes ✅

---

### Phase 6: Component Functional Automation

#### **Functional Automation Test**
**File:** `functional-automation-test.agent.md`

**When to use:**
- After implementation is complete
- Running functional tests for the components listed in `output/{RUN_ID}/plan/frontend/components.md`

**What it does:**
- Reads the planner's component inventory and tests each implemented component
- Generates and runs Playwright tests using the `playwright` MCP server
- Maps functional test cases and evidence to component IDs
- Reports pass/fail/blocked status and component coverage gaps

**Inputs:**
- `RUN_ID`
- `output/{RUN_ID}/plan/frontend/components.md`
- Implemented frontend/backend code and related requirements

**Output:**
- `output/{RUN_ID}/functional-tests/attempt-<n>/` test suite and execution evidence
- `FT-*` entries in `requirement/Traceability_Matrix.md`

**User-invocable:** Yes ✅

---

### Phase 7: Quality Assurance

#### **Quality Tester**
**File:** `tester.agent.md`

**When to use:**
- After component functional automation completes
- Testing complete user workflows spanning frontend, backend, and data
- Validating business logic completeness and user experience

**What it does:**
- Reads specifications and planned scenarios
- Designs end-to-end scenarios: happy paths, errors, edge cases, state transitions
- Covers cross-layer flows, performance, accessibility, and security checks
- Maps tests to TEST-* IDs

**Reads from:**
- Specifications with SPEC-* IDs
- `output/{RUN_ID}/plan/tests/scenarios.md`
- All applicable files in `.github/contexts/`

**Output:**
- Executable test files and fixtures
- Test coverage reports
- Updated `requirement/Traceability_Matrix.md` (TEST-* IDs)

**User-invocable:** Yes ✅

---

### Phase 8: Review & Compliance

#### **Compliance Reviewer**
**File:** `reviewer.agent.md`

**When to use:**
- Reviewing any artifact (specs, plans, code, tests, docs)
- Validating compliance with standards and regulations
- Checking security and quality requirements
- Ensuring traceability is maintained

**What it does:**
- Reviews artifacts against compliance criteria
- Validates security, quality, and architecture standards
- Checks for traceability breaks
- Identifies compliance gaps
- Provides severity-graded findings (CRITICAL, HIGH, MEDIUM, LOW)
- Recommends remediation actions
- Verifies regulatory requirement fulfillment

**Can review:**
- Technical specifications (SPEC-* artifacts)
- Implementation plans (TASK-* artifacts)
- Source code (CODE-* artifacts)
- Test suites (TEST-* artifacts)
- Documentation (DOC-* artifacts)

**Output:**
- `REVIEW-*` IDs
- Findings mapped to affected FR/NFR/SPEC/TASK/CODE/TEST IDs
- Overall status: `PASS`, `FAIL`, or `PASS_WITH_WARNINGS`

**User-invocable:** Yes ✅

---

### Phase 9: Documentation & Traceability

#### **Technical Documenter**
**File:** `technical-documenter.agent.md`

**When to use:**
- Creating technical documentation from specifications
- Writing API documentation
- Generating architecture documentation
- Creating deployment and operations guides
- Building developer runbooks

**What it does:**
- Reads specifications and implementations
- Generates comprehensive technical documentation
- Creates API reference documents
- Documents system architecture
- Writes deployment procedures
- Creates troubleshooting guides
- Generates final project documentation

**Reads from:**
- `output/{RUN_ID}/specify/spec.md` (initial documentation)
- `output/{RUN_ID}/plan/frontend/components.md`
- `output/{RUN_ID}/implement/frontend/` and `backend/` (final documentation)
- `.github/contexts/project-context.md` and `domain-context.md`

**Output:**
- README, ARCHITECTURE, DEPLOYMENT, CONFIGURATION, SECURITY, COMPLIANCE, TROUBLESHOOTING, and FRONTEND-INTEGRATIONS documents as applicable
- Updated `requirement/Traceability_Matrix.md` (DOC-* IDs)

**User-invocable:** Yes ✅

---

#### **Traceability Manager**
**File:** `traceability-manager.agent.md`

**When to use:**
- Validating end-to-end traceability
- Tracking requirements through implementation
- Identifying traceability gaps
- Generating traceability reports
- Ensuring all artifacts are linked

**What it does:**
- Maps all trace IDs across workflow phases
- Validates that every requirement is implemented and tested
- Identifies orphaned artifacts
- Detects circular dependencies
- Generates traceability reports
- Maintains `requirement/Traceability_Matrix.md`
- Provides visibility into requirement status

**Tracks:**
- CTX-* (Context) → BRD-* → FR-*/NFR-* (Requirements)
- FR-*/NFR-* → SPEC-* (Specifications)
- SPEC-* → TASK-* (Plans)
- TASK-* → CODE-* (Implementation)
- CODE-* → APT-* (Backend API tests)
- CODE-* → FT-* (Component functional tests)
- CODE-* → TEST-* (User-workflow tests)
- All → REVIEW-* (Compliance review)
- All → DOC-* (Documentation)

**Output:**
- Updated `requirement/Traceability_Matrix.md`
- Traceability gap reports
- Status dashboards

**User-invocable:** Yes ✅

---

## Reference Files

#### **agent-frontmatter-reference.md**
**File:** `agent-frontmatter-reference.md`

**Purpose:**
- Reference guide for agent frontmatter configuration
- Template for creating new agents
- Best practices for agent design
- Contains real-world examples and patterns

**Contains:**
- 10 frontmatter parameters explained
- Best-practice checklist
- Starter template for new agents
- Real-world examples from actual agents

---

## How to Invoke Agents

### In VS Code Chat

1. **Open Copilot Chat** (Ctrl+Shift+I / Cmd+Shift+I)
2. **Select the agent** from the agent dropdown
3. **Provide required inputs** (Jira key, requirement file, `RUN_ID`, etc.)
4. **Agent executes** and produces artifacts under `output/{RUN_ID}/`

Example inputs:

```text
Technical Specifier:       ABCAPP-123  (or requirement/MyApp_Requirements.md)
Implementation Builder:    RUN_ID=ABCAPP-123_20261013
API Tester:                RUN_ID=ABCAPP-123_20261013 API_BASE_URL=http://localhost:9090
Functional Automation Test: RUN_ID=ABCAPP-123_20261013
```

### Workflow Prompts

Prompt files in `.github/prompts/` run multi-agent workflows end to end:

| Prompt | Purpose |
|--------|---------|
| `intake-to-spec.prompt.md` | Consolidate existing requirement docs, validate traceability, generate and review the spec |
| `intake-to-implementation.prompt.md` | Full flow from intake through implementation, API testing, functional testing, QA, review, docs, and traceability |

---

## Traceability IDs

Each phase generates unique trace IDs for linking:

| Phase | ID Prefix | Example | Meaning |
|-------|-----------|---------|---------|
| Context | CTX-* | CTX-TECH-001 | Technology decision |
| Context Update | CTX-UPDATE-* | CTX-UPDATE-001 | Context change |
| Business | BRD-* | BRD-001 | Business requirement |
| Requirements | FR-*, NFR-* | FR-001, NFR-001 | Functional, Non-Functional requirement |
| User Stories | US-* | US-001 | User story |
| Specification | SPEC-* | SPEC-001 | Technical specification |
| Planning | TASK-* | TASK-001 | Implementation task |
| Implementation | CODE-* | CODE-001 | Code artifact |
| Backend API Testing | APT-* | APT-GET-accounts-001 | API test case |
| Component Functional Testing | FT-* | FT-COMP-001-001 | Component functional test |
| Quality Assurance | TEST-* | TEST-001 | User-workflow test case/suite |
| Review | REVIEW-* | REVIEW-001 | Compliance review finding |
| Documentation | DOC-* | DOC-001 | Documentation artifact |

Chain: `CTX → BRD → FR/NFR → SPEC → TASK → CODE → APT → FT → TEST → REVIEW → DOC` (see `.github/rules/traceability-standards.md`).

---

## Recommended Workflow

### Existing Requirement Documents
```
[Context exists per Context Builder]
-> Requirement Intake Consolidator
-> Traceability Manager
-> Technical Specifier
-> Compliance Reviewer
-> Implementation Planner
-> Compliance Reviewer
-> Implementation Builder
-> API Tester
-> Functional Automation Test
-> Quality Tester
-> Compliance Reviewer
-> Technical Documenter
-> Traceability Manager
```

### New Business Problem
```
[Context exists per Context Builder]
-> Context Clarifier
-> BRD Generator
-> Requirements Expander
-> User Story Generator
-> Technical Specifier
-> Implementation Planner
-> Implementation Builder
-> API Tester
-> Functional Automation Test
-> Quality Tester
-> Compliance Reviewer
-> Technical Documenter
-> Traceability Manager
```

Requirement Intake Consolidator, Context Clarifier, BRD Generator, Requirements Expander, and User Story Generator are workflow roles without agent files; the prompts in `.github/prompts/` perform them.

### Continuous Updates
```
• Code, dependency, or document changes → Context Updater
• New requirement → Technical Specifier
• Specification change → Implementation Planner (re-plan)
• Backend change → API Tester (re-run)
• Frontend change → Functional Automation Test (re-run)
• Traceability Manager (runs between phases)
```

---

## Standards Files

Context files in `.github/contexts/` are created by Context Builder and maintained by Context Updater:

- **project-context.md** - Business and technology baseline
- **domain-context.md** - Client industry/domain, terminology, and business rules
- **frontend-context.md** - Frontend tech patterns and best practices
- **backend-context.md** - Backend tech stack, API standards, and patterns (used by API Tester)
- **testing-standards.md** - Testing frameworks and strategies
- Additional user-provided standards indexed by project context

Rules in `.github/rules/` apply across agents:

- **architectural-standards.md**, **security-quality-standards.md**, **environment-standards.md**, **versioning-standards.md**
- **requirement-standards.md**, **traceability-standards.md**, **sdlc.md**
- **specification-execution-gates.md**, **planning-execution-gates.md**, **implementation-execution-gates.md**
- **mcp-usage-guide.md**, **figma-interactive-selection-guide.md**

Templates in `.github/templates/`: `requirements-input-template.md`, `user-story-template.md`.

All agents read from and respect these standards during their work.

---

## Troubleshooting

### "Agent not found"
- Check agent name spelling (case-sensitive)
- Ensure agent file exists in `.github/agents/`
- Agent must have `user-invocable: true` in frontmatter

### "Missing required input"
- Check argument-hint in agent frontmatter
- Provide required file paths, Jira keys, or `RUN_ID`
- Active file must be in workspace

### "Playwright MCP blocked"
- Start the `playwright` server from `.vscode/mcp.json`
- Ensure the app/backend origin is in `--allowed-origins` (defaults: ports 4201 and 9090)

### "Traceability broken"
- Run Traceability Manager to identify gaps
- Check that all IDs reference correctly
- Ensure artifacts follow naming conventions

### "Standards not applied"
- Verify context and standards files exist in `.github/contexts/`
- Check that agent reads from correct standards
- Context Builder should be run first for new projects

---

## Best Practices

1. **Always start with Context Builder** for new projects
2. **Follow the workflow sequence** - don't skip phases
3. **Keep standards files updated** via Context Updater
4. **Run Traceability Manager periodically** to validate
5. **Use Compliance Reviewer** before merging to main
6. **Document decisions** in appropriate standards files
7. **Maintain trace IDs** consistently across all artifacts
8. **Update context** when technology stack changes

---

## Additional Resources

- `.github/copilot-instructions.md` - Central orchestration guide
- `.github/SPEC_DRIVEN_WORKFLOW.md` - Workflow specifications
- `.github/agents/README.md` - Detailed agent usage guide
- `.github/prompts/` - End-to-end workflow prompts
- `.github/rules/` - Execution gates, architecture, security, and traceability rules
- `.github/contexts/` - Project, domain, frontend, backend, and testing context
- `.github/scripts/` - Figma pipeline and agent token-estimation scripts
- `.vscode/mcp.json` - Playwright MCP server configuration
- `requirement/Traceability_Matrix.md` - Live traceability matrix

