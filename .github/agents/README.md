# SDLC Agents - Complete Usage Guide

This document describes all available agents in the spec-driven development lifecycle (SDLC) workflow and how to use them.

## Overview

The agents are organized into a sequential SDLC workflow that transforms business requirements into implemented, tested, and documented code. Each agent is specialized for a specific phase and reads/writes standardized artifacts with trace IDs.

## Agent Workflow Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                      SPEC-DRIVEN DEVELOPMENT FLOW                   │
└─────────────────────────────────────────────────────────────────────┘

Step 1: Context Foundation
   ↓
   Context Builder
   Context Updater (runs continuously)
   ↓
Step 2: Requirements & Specification
   ↓
   Technical Specifier
   ↓
Step 3: Planning & Architecture (includes unit test planning)
   ↓
   Implementation Planner
   ↓
Step 4: Implementation & Unit Testing
   ↓
   Implementation Builder (creates code + unit tests)
   ↓
Step 4b: Backend API Testing
   ↓
   API Tester (tests planned APIs from backend-apis.json)
   ↓
Step 5: Component Functional Automation
   ↓
   Functional Automation Test (tests planned components from components.md)
   ↓
Step 6: Quality Assurance - Functional Testing
   ↓
   Quality Tester (designs broader user-workflow tests)
   ↓
Step 7: Review & Compliance
   ↓
   Compliance Reviewer
   ↓
Step 8: Documentation & Traceability
   ↓
   Technical Documenter
   Traceability Manager
   ↓
Step 8 (Design Support - Parallel)
   ↓
   Figma Extractor
   ↓
All Phases: Continuous Validation
   ↓
   Compliance Reviewer (throughout)
```

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

### Phase 2: Requirements & Specification

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

**Output:**
- `requirement/{ProjectName}_Specification.md` with SPEC-* IDs
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
- Planning unit tests alongside implementation

**What it does:**
- Reads technical specifications (SPEC-* IDs)
- Creates detailed implementation plans with task breakdowns
- Generates task DAGs showing dependencies
- **Plans unit tests as part of each implementation task** (not separate)
- **Plans functional/end-to-end test scenarios** for Quality Tester to execute
- Assigns effort estimates and sequencing
- Maps tasks to TASK-* IDs
- Identifies frontend/backend/testing/documentation tasks
- Includes unit test framework references (Jest, pytest, JUnit, etc.)
- Documents unit test coverage targets (80%+ for business logic, 90%+ for validation)

**Unit Test Planning Includes:**
- **Backend unit tests** for each service, controller, model, middleware
- **Frontend unit tests** for each component, hook, service, utility
- **Test framework** selection and configuration
- **Mock data** and fixture strategies
- **Coverage targets** and verification commands
- **Integration test** dependencies on backend contract verification

**Reads from:**
- Specifications with SPEC-* IDs
- `.github/contexts/frontend-context.md`
- `.github/contexts/backend-context.md`
- `.github/contexts/testing-standards.md` (unit test patterns and examples)

**Output:**
- `requirement/{ProjectName}_Plan.md` with TASK-* IDs
- `plan.md/tasks.md` including unit test tasks (BLOCKED_BY implementation tasks)
- `plan.md` Functional Test Scenarios section (for Quality Tester)
- Task dependency graph
- Updated `requirement/Traceability_Matrix.md`

**User-invocable:** Yes ✅

---

### Phase 4: Implementation & Unit Testing

#### **Implementation Builder**
**File:** `implement.agent.md`

**When to use:**
- Implementing code from approved plans
- Starting a specific task from the task file
- Creating features, components, or backend services
- Following established standards and patterns
- Creating unit tests alongside implementation (test-driven development)
- Matching UI implementation to screenshot/Figma designs with project theme consistency

**What it does:**
- Reads implementation plans (TASK-* IDs)
- Generates production-ready code
- **Creates unit tests as part of implementation** (not separately)
- **Matches UI exactly to screenshots/Figma designs** while applying project theme, color palette, and styling
- Follows tech-stack-specific standards
- Reuses approved components and libraries
- Documents code inline with standards
- Verifies visual fidelity against reference designs

**Visual Implementation Verification:**
- Colors match project theme palette (no custom hex values contradicting brand)
- Typography aligns with project type scale (fonts, sizes, weights)
- Spacing follows project design tokens (padding, margins, gaps)
- Component styling uses approved project components
- All states and variants from screenshot are implemented
- No visual gaps or deviations from reference design

**Reads from:**
- Plans with TASK-* IDs
- `.github/contexts/frontend-context.md`
- `.github/contexts/backend-context.md`
- `.github/contexts/testing-standards.md` (unit test patterns and examples)
- `.github/agents/planner.agent.md` for unit test coverage targets

**Output:**
- Implemented source code files
- Unit test files (backend and frontend)
- Code comments and documentation
- Unit test coverage reports
- Updated `requirement/Traceability_Matrix.md` (CODE-* and TEST-* IDs)

**User-invocable:** Yes ✅

---

### Phase 4b: Backend API Testing

#### **API Tester**
**File:** `api-tester.agent.md`

**When to use:**
- After Implementation Builder completes the planned backend APIs
- Executing API tests for every API listed in `output/{RUN_ID}/plan/contracts/backend-apis.json`

**What it does:**
- Uses `backend-context.md` for tech stack and API standards
- Maps each planned API to its controller and reports contract drift
- Generates Playwright API tests under `<backend-root>/test/api/` and runs them with evidence
- Uses the Playwright MCP server from `.vscode/mcp.json` for live endpoint discovery

**Inputs:**
- `RUN_ID`
- `output/{RUN_ID}/plan/contracts/backend-apis.json`
- `.github/contexts/backend-context.md`, backend source, specs, and planned scenarios

**Output:**
- API tests in `<backend-root>/test/api/`
- `output/{RUN_ID}/api-tests/attempt-<n>/` with inventory, cases, reports, JUnit, and logs
- `APT-*` entries in `requirement/Traceability_Matrix.md`

**User-invocable:** Yes ✅

---

### Phase 5: Component Functional Automation

#### **Functional Automation Test**
**File:** `functional-automation-test.agent.md`

**When to use:**
- After Implementation Builder completes the planned frontend components
- Executing functional tests for every component listed in `output/{RUN_ID}/plan/frontend/components.md`

**What it does:**
- Uses the planner's component inventory as the required test scope
- Verifies implementation readiness and maps cases to component IDs
- Generates and runs component-level Playwright tests with evidence
- Reports component-level passes, failures, blockers, and coverage gaps

**Inputs:**
- `RUN_ID`
- `output/{RUN_ID}/plan/frontend/components.md`
- Implemented code, specifications, planned scenarios, API contracts, and relevant context

**Output:**
- `output/{RUN_ID}/functional-tests/attempt-<n>/` with tests, reports, JUnit, logs, and evidence

**User-invocable:** Yes ✅

### Phase 6: Quality Assurance - User Workflows

#### **Quality Tester**
**File:** `tester.agent.md`

**When to use:**
- Creating end-to-end and functional test scenarios after implementation is complete
- Testing complete user workflows spanning frontend, backend, and database
- Validating business logic completeness and user experience
- Creating BDD/Gherkin-style test scenarios

**What it does:**
- Reads technical specifications and functional requirements
- Creates end-to-end test scenarios for user workflows
- Plans functional test cases covering happy paths, error scenarios, edge cases
- Maps tests to SPEC-* requirements and acceptance criteria
- Focuses on **user-facing behavior**, not isolated components
- **Note:** Unit tests are created during implementation (planning and implementation phases), not here

**Tests user workflows like:**
- Complete user journeys (login → search → filter → select → checkout)
- Error handling (invalid inputs, API failures, network errors)
- State transitions and workflow progression
- Data integrity (create-read-update-delete operations)
- Cross-layer flows (UI → API → Backend → Database)
- Performance and accessibility

**Reads from:**
- Specifications with SPEC-* IDs
- `plan.md` Functional Test Scenarios section
- `.github/contexts/frontend-context.md`
- `.github/contexts/backend-context.md`

**Output:**
- Functional test scenarios (BDD/Gherkin format)
- End-to-end test cases
- Test execution reports
- Updated `requirement/Traceability_Matrix.md` with functional test references

**User-invocable:** Yes ✅

---

### Phase 7: Review & Compliance

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
- Compliance review report
- Issues and findings
- Remediation recommendations

**User-invocable:** Yes ✅

---

### Phase 8: Documentation & Traceability

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
- Specifications with SPEC-* IDs
- Implementation code with CODE-* IDs
- `.github/contexts/project-context.md`
- `.github/contexts/domain-context.md`

**Output:**
- API documentation
- Architecture documentation
- Deployment guides
- Runbooks and troubleshooting guides
- Project README
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
- CODE-* → TEST-* (Tests)
- All → DOC-* (Documentation)

**Output:**
- Updated `requirement/Traceability_Matrix.md`
- Traceability gap reports
- Status dashboards

**User-invocable:** Yes ✅

---

### Phase 9: Design Integration (Parallel)

#### **Figma Extractor**
**File:** `figma-extractor.agent.md`

**When to use:**
- Extracting Figma design artifacts from requirements
- Converting design files to structured design data
- Creating effective screen tables and cropped images
- Mapping design screens to specification sections

**What it does:**
- Reads requirement file with Figma links
- Extracts design metadata from Figma
- Downloads screenshots and design assets
- Crops and organizes screen images
- Generates effective screen tables
- Creates figma_report.md with design analysis
- Maps design screens to requirement sections

**Input:**
- Requirement file path with Figma file key and node IDs

**Output:**
- `figma_report.md` - Design extraction report
- Parent JSON - Complete Figma tree structure
- Parent PNG - Full screenshot at scale
- Cropped screen PNGs - Individual screen images
- Effective screen table - Design structure mapping

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
2. **Type agent name** or use the agent dropdown
3. **Provide required inputs** (file paths, Jira keys, etc.)
4. **Agent executes** and produces artifacts

### Command Line

```bash
# From VS Code terminal or command line
# (if MCP server integration is configured)
copilot-agent "Context Builder"
copilot-agent "Technical Specifier" --file requirement/MyApp_Requirements.md
copilot-agent "Implementation Builder" --plan requirement/MyApp_Plan.md
```

### From Requirements

Agents can be triggered from requirement markdown files with frontmatter:

```markdown
---
trigger-agent: "Technical Specifier"
input-file: "requirement/MyApp_Requirements.md"
---

# My Requirement
...
```

---

## Traceability IDs

Each phase generates unique trace IDs for linking:

| Phase | ID Prefix | Example | Meaning |
|-------|-----------|---------|---------|
| Context | CTX-* | CTX-TECH-001 | Technology decision |
| Context Update | CTX-UPDATE-* | CTX-UPDATE-001 | Context change |
| Requirements | FR-*, NFR-*, BRD-* | FR-001, NFR-001 | Functional, Non-Functional requirement |
| Specification | SPEC-* | SPEC-001 | Technical specification |
| Planning | TASK-* | TASK-001 | Implementation task |
| Implementation | CODE-* | CODE-001 | Code artifact |
| Testing | TEST-* | TEST-001 | Unit test case/suite |
| Documentation | DOC-* | DOC-001 | Documentation artifact |

---

## UI Implementation & Visual Design Fidelity

### Screenshot/Figma Design Matching

**Principle**: UI implementation MUST match the referenced screenshot or Figma design exactly, while applying the project's theme, color palette, and styling standards.

**Screenshot as Binding Acceptance Evidence:**
- Screenshots linked in specification are not optional inspiration—they define visual acceptance criteria
- Every visible element, spacing relationship, color, and state in the screenshot must be implemented
- Visual gaps, silent omissions, or design deviations are implementation failures

**Theme & Styling Consistency:**
- Colors: Use project color palette and design tokens, not custom hex values that contradict brand
- Typography: Apply project type scale (fonts, sizes, weights, line heights)
- Spacing: Follow project design tokens for padding, margins, gaps, and alignment
- Components: Reuse approved project components; do not create custom variants that conflict with system
- States: Implement all visual states shown in screenshot (normal, hover, active, disabled, loading, error, empty)

**Implementation Verification Checklist:**
- ✅ Every control, label, icon matches screenshot exactly
- ✅ Colors align with project palette
- ✅ Typography matches project type scale
- ✅ Spacing and alignment follow design tokens
- ✅ Component styling uses approved project components
- ✅ All states and variants from screenshot are present
- ✅ No custom styling overrides project theme
- ✅ Visual comparison against PNG at target viewport shows 100% match

**Planning Requirement:**
- Implementation Planner creates explicit visual fidelity verification tasks
- Tasks include acceptance criteria: "UI matches referenced screenshot 100%"
- Verification includes color, typography, spacing, component usage, and theme consistency

**Manual-Upload Design Source (No Figma Link):**
- When screens come from Jira/Confluence screenshots or manual uploads, Technical Specifier assigns `SCR-*` screen IDs and sets `DESIGN_EVIDENCE_STATUS: AVAILABLE`
- Planning and implementation proceed without Figma JSON, marked `Design Source: Manual upload (no Figma link)`
- Values that cannot be measured exactly from a screenshot are marked `APPROXIMATE_FROM_SCREENSHOT` and mapped to the nearest design token
- Figma extraction failures (MCP error, rate limit) are recorded as gaps, not blockers
- Only a frontend story with no design evidence at all (`PENDING_MANUAL_UPLOAD`) blocks planning and implementation

---

## Unit Testing & Quality Assurance Separation

### Unit Testing (Planning + Implementation Phases)

**When**: Planned during Implementation Planner phase, created during Implementation Builder phase

**Who**: Implementation Builder creates unit tests as part of implementation

**What**: Isolated component/module testing
- Frontend: Components, hooks, services, utilities, state management
- Backend: Services, controllers, models, middleware
- Coverage targets: 80%+ for business logic, 90%+ for validation

**How**: Created during implementation using tech-stack-specific frameworks
- Frontend: Jest, Vitest, React Testing Library, Flutter test
- Backend: pytest, Jest, JUnit, unittest

**Why**: Unit tests verify implementation correctness and enable safe refactoring

**Test Structure:**

Frontend:
```
frontend/test/unit/
├── components/          # Component unit tests
├── hooks/              # Hook tests
├── services/           # Service/API tests
├── utils/              # Utility function tests
├── state/              # State management tests
└── __mocks__/          # Mock data and fixtures
```

Backend:
```
backend/test/unit/
├── controllers/        # API endpoint tests
├── services/          # Business logic tests
├── models/            # Database model tests
├── middleware/        # Middleware tests
├── utils/             # Utility function tests
└── fixtures/          # Test data and mocks
```

---

### Functional Testing (Quality Assurance Phase)

**When**: After implementation is complete

**Who**: Quality Tester creates functional/end-to-end tests

**What**: Complete user workflow testing
- User journeys (login → search → select → checkout)
- Error scenarios and edge cases
- Cross-layer flows (UI → API → Backend → Database)
- Performance and accessibility
- End-to-end BDD/Gherkin-style scenarios

**How**: Created using BDD frameworks or end-to-end test tools
- BDD: Gherkin syntax for readable test scenarios
- E2E: Playwright, Cypress, or similar tools
- Manual testing when appropriate

**Why**: Functional tests verify complete system behavior and user experience

---

### Coverage Targets

| Layer | Target | Priority | Who Creates |
|-------|--------|----------|-------------|
| Business Logic Unit Tests | 80%+ | CRITICAL | Implementation Builder |
| Validation Unit Tests | 90%+ | CRITICAL | Implementation Builder |
| API Endpoint Tests | 75%+ | HIGH | Implementation Builder |
| UI Component Tests | 70%+ | HIGH | Implementation Builder |
| Error Handling Tests | 80%+ | HIGH | Implementation Builder |
| User Workflow Tests | 100% coverage | CRITICAL | Quality Tester (functional) |
| Edge Case Tests | 80%+ coverage | HIGH | Quality Tester (functional) |

---

## Recommended Workflow

### New Project
```
1. Context Builder (establish baseline)
   ↓
2. Business input → BRD Builder (if needed)
   ↓
3. Requirements → Technical Specifier
   ↓
4. Spec → Implementation Planner (plans implementation + unit tests + functional tests)
   ↓
5. Plan → Implementation Builder (creates code + unit tests)
   ↓
6. Code → Compliance Reviewer (validates quality and coverage)
   ↓
7. Implementation → Quality Tester (creates functional/end-to-end tests)
   ↓
8. Tests + Code → Compliance Reviewer (final validation)
   ↓
9. All artifacts → Technical Documenter
   ↓
10. All → Traceability Manager (validate end-to-end)
```

### Existing Project
```
1. Context Builder (scan and establish)
   ↓
2. Requirement input → Technical Specifier
   ↓
3-10. Same as New Project
```

### Continuous Updates
```
• Code changes → Context Updater (automatic trigger)
• New requirement → Technical Specifier
• Specification change → Implementation Planner (re-plan including unit tests)
• Implementation → Includes unit tests (planned + created together)
• Quality Tester → Functional tests after implementation complete
• Traceability Manager (runs between phases)
```

### Key Principles
1. **Unit Tests with Implementation**: Created during implementation phase, not after
2. **Functional Tests Separate**: Quality Tester creates end-to-end tests after implementation
3. **Planning Includes Testing**: Planner defines unit test strategy alongside implementation tasks
4. **Test Coverage Target**: 80%+ for business logic, 90%+ for validation (set in planning, achieved during implementation)

---

## Standards Files

Each project has standards files created/maintained by agents:

- **project-context.md** - Business and technology baseline
- **domain-context.md** - Client industry/domain, terminology, business rules, and constraints
- **frontend-context.md** - Frontend tech patterns and best practices
- **backend-context.md** - Backend tech patterns and best practices
- **testing-standards.md** - Testing frameworks and strategies (includes unit test patterns)
- **general-standards.md** - Optional user-provided cross-cutting standards (git, CI/CD, security, infrastructure)

All agents read from and respect these standards during their work.

---

## Troubleshooting

### "Agent not found"
- Check agent name spelling (case-sensitive)
- Ensure agent file exists in `.github/agents/`
- Agent must have `user-invocable: true` in frontmatter

### "Missing required input"
- Check argument-hint in agent frontmatter
- Provide required file paths or Jira keys
- Active file must be in workspace

### "Traceability broken"
- Run Traceability Manager to identify gaps
- Check that all IDs reference correctly
- Ensure artifacts follow naming conventions

### "Standards not applied"
- Verify context and standards files exist in `.github/contexts/`
- Check that agent reads from correct standards
- Context Builder should be run first for new projects

### "Test coverage incomplete"
- Run Quality Tester for comprehensive test design
- Check testing-standards.md for tech-stack patterns
- Ensure Implementation Builder includes unit tests
- Verify test file locations follow project structure

---

## Best Practices

1. **Always start with Context Builder** for new projects
2. **Follow the workflow sequence** - don't skip phases
3. **Keep standards files updated** via Context Updater
4. **Run Quality Tester** to ensure comprehensive unit test coverage
5. **Run Traceability Manager periodically** to validate
6. **Use Compliance Reviewer** before merging to main
7. **Document decisions** in appropriate standards files
8. **Maintain trace IDs** consistently across all artifacts
9. **Update context** when technology stack changes
10. **Include unit tests** with every implementation task

---

## Additional Resources

- `.github/copilot-instructions.md` - Central orchestration guide
- `.github/SPEC_DRIVEN_WORKFLOW.md` - Workflow specifications
- `requirement/Traceability_Matrix.md` - Live traceability matrix
- `.github/contexts/testing-standards.md` - Unit test patterns and frameworks
- `.github/instructions/` - All standards and guidelines
- `.github/rules/` - Project-specific rules and architecture standards

