---
title: Context Management System Integration Guide
description: Complete guide to the Context Builder and Context Updater agents, their role in the PDLC, and integration with existing agents
author: PDLC Architecture Team
ms.date: 2026-10-07
ms.topic: guide
---

# Context Management System Integration Guide

## Overview

The Context Management System provides a foundational layer for all PDLC workflows in your organization. It consists of two specialized agents:

1. **Context Builder** - Initializes comprehensive project context, technology standards, and traceability documents
2. **Context Updater** - Maintains context alignment as the project evolves

These agents work together to ensure all downstream agents (Specifier, Planner, Builder, Tester) operate from a single source of truth about business drivers, technology choices, and architectural standards.

## Architecture

### Context Layers

```
┌─────────────────────────────────────────────────────────┐
│           Business Context Layer                        │
│  (requirement/Context_{ProjectName}.md)                 │
│  - Business drivers, stakeholders, compliance needs    │
│  - Success criteria, scope boundaries                  │
│  - CTX-* IDs for traceability                          │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│      Technology Context Layer                           │
│  (.github/contexts/project-context.md)                      │
│  - Technology baseline (versions, dependencies)        │
│  - Repository architecture, design system             │
│  - Links to domain and user-provided context           │
└─────────────────────────────────────────────────────────┘
                          ↓
┌──────────────────┬──────────────────┬──────────────────┬──────────────────┐
│ Domain           │ Frontend         │ Backend          │ Testing          │
│ Context          │ Context          │ Context          │ Standards        │
│ (contexts/)      │ (contexts/)      │ (contexts/)      │ (contexts/)      │
├──────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ - Industry       │ - Architecture   │ - API design     │ - Unit testing   │
│ - Terminology    │ - Components     │ - Services       │ - Integration    │
│ - Business rules │ - State mgmt     │ - Persistence    │ - BDD/Gherkin    │
│ - Regulations    │ - Routing        │ - Auth/Authz     │ - Coverage       │
│ - Constraints    │ - HTTP client    │ - Middleware     │ - Fixtures       │
└──────────────────┴──────────────────┴──────────────────┴──────────────────┘
```

### Agent Workflows

#### Context Builder Workflow

```
1. Gather Business & Technical Context
   ├─ Read Confluence when provided; otherwise use attached Word/PDF documents
   ├─ Inspect available legacy project documentation, source code, configuration, and tests
   ├─ Gather business, domain, stakeholder, and compliance needs
   ├─ Detect tech stack: frontend, backend, testing frameworks
   ├─ Create CTX-* IDs for traceability
   └─ Document findings

2. Create Technology-Specific Standards Files
   ├─ frontend-context.md (based on detected frontend tech)
   ├─ backend-context.md (based on detected backend tech)
   └─ testing-standards.md (based on detected test frameworks)

3. Create Unified Context Document
   ├─ .github/contexts/project-context.md
   ├─ .github/contexts/domain-context.md (client industry/domain and business rules)
   ├─ Index additional user-provided standards under .github/contexts/
   └─ Link source evidence and guidance for downstream agents

4. Populate Traceability
   ├─ Create requirement/Context_{ProjectName}.md
   └─ Update requirement/Traceability_Matrix.md with CTX-* mappings
```

#### Context Updater Workflow

```
1. Detect Changes in Project State
   ├─ Review Confluence or attached Word/PDF changes and available legacy project files
   ├─ Scan configuration files (package.json, pubspec.yaml, etc.)
   ├─ Inventory domain context and user-provided standards
   ├─ Check folder structure reorganization
   ├─ Monitor dependency and framework version updates
   └─ Categorize as MINOR/MODERATE/MAJOR impact

2. Analyze Change Impact
   ├─ Assess effect on standards files
   ├─ Check for conflicts with existing context
   └─ Identify implications for active specs/plans

3. Update Context Files
   ├─ Sync .github/contexts/project-context.md
   ├─ Sync .github/contexts/domain-context.md
   ├─ Update frontend-context.md (if frontend changes)
   ├─ Update backend-context.md (if backend changes)
   └─ Update testing-standards.md (if testing changes)
   └─ Preserve and update affected user-provided standards when warranted

4. Track Changes in Traceability
   ├─ Create CTX-UPDATE-* IDs for tracked changes
   ├─ Update requirement/Context_{ProjectName}.md with change history
   └─ Escalate MAJOR changes for approval
```

## Integration with Existing Agents

### Updated Agent Dependencies

#### Technical Specifier
**Reads from context:**
- `.github/contexts/project-context.md` - Technology baseline, architecture patterns
- `.github/contexts/frontend-context.md` - Frontend patterns, component library, architectural layers
- `.github/contexts/backend-context.md` - API design, validation patterns, persistence approaches

**Impact:** Specifier uses tech standards to validate frontend/backend design choices, recommend existing components, and ensure specs align with project conventions.

#### Implementation Planner
**Reads from context:**
- `.github/contexts/project-context.md` - Technology baseline, approved patterns
- `.github/contexts/frontend-context.md` - Frontend folder structure, layer boundaries
- `.github/contexts/backend-context.md` - Backend service layers, API versioning
- `.github/contexts/testing-standards.md` - Test structure, coverage requirements

**Impact:** Planner uses tech standards to structure frontend and backend tasks, define test task requirements, and ensure task dependencies reflect project architecture.

#### Implementation Builder
**Reads from context:**
- `.github/contexts/frontend-context.md` - Reusable components, approved libraries, code structure
- `.github/contexts/backend-context.md` - Service patterns, middleware setup, API conventions
- `.github/contexts/testing-standards.md` - Test patterns, fixtures, test location conventions

**Impact:** Builder follows tech standards to create consistent implementation, reuse existing components, and generate tests matching project patterns.

#### Quality Tester
**Reads from context:**
- `.github/contexts/testing-standards.md` - Test frameworks, coverage targets, fixture strategies
- `.github/contexts/frontend-context.md` - Frontend testing patterns, component testing approaches
- `.github/contexts/backend-context.md` - Backend testing patterns, mock data strategies

**Impact:** Tester creates test designs and implementations aligned with project standards, using approved frameworks and patterns.

#### Traceability Manager
**Reads from context:**
- `.github/contexts/project-context.md` - Baseline for context version tracking
- `requirement/Context_{ProjectName}.md` - CTX-* ID mapping and change history
- `requirement/Traceability_Matrix.md` - CTX-* to downstream artifact mappings

**Tracks:**
- CTX-* IDs from Context Builder
- CTX-UPDATE-* IDs from Context Updater
- Impact of context changes on active specs/plans/code

## Traceability Flow

```
CTX-* IDs
   ↓
requirement/Context_{ProjectName}.md
   ↓
requirement/Traceability_Matrix.md (maps CTX-* to BRD/FR/NFR)
   ↓
.github/contexts/project-context.md (business + tech)
   ↓
frontend/backend/testing-standards.md (tech-specific patterns)
   ↓
SPEC-* (specification phase reads standards)
   ↓
TASK-* (planner reads standards)
   ↓
CODE-* (builder reads standards)
   ↓
TEST-* (tester reads standards)
```

## File Structure

### Context Files Managed by Context Builder

```
.github/contexts/
├─ project-context.md             # Unified business + tech baseline
├─ domain-context.md              # Client industry/domain and business rules
├─ frontend-context.md            # Frontend application patterns
├─ backend-context.md             # Backend application patterns
├─ testing-standards.md           # Testing tech patterns
└─ <user-provided-context>.md    # Additional standards/context when applicable

requirement/
├─ Context_{ProjectName}.md      # Detailed context with CTX-* IDs
├─ Traceability_Matrix.md        # Updated with CTX-* mappings
└─ [existing requirement files]
```

### Version History Tracking

Context files include version history sections:

```markdown
## Version History

| Version | Date | Changes | Breaking |
|---------|------|---------|----------|
| 1.0 | 2026-10-07 | Initial context | No |
| 1.1 | 2026-10-15 | Framework version upgrade | No |
| 1.2 | 2026-10-22 | Express 4.18 upgrade | No |
```

Context updates also maintain a changelog:

```markdown
## Update History

| Date | Phase | Changes | Detector | Impact |
|------|-------|---------|----------|--------|
| 2026-10-15 | Implementation | Framework version upgrade | Context Updater | MINOR |
```

## Usage Scenarios

### Scenario 1: New Project Kickoff

1. **Run Context Builder** with business requirements and detected tech stack
   - Outputs: project-context.md, standards files, Context_ProjectName.md
   - Traceability: CTX-* IDs created

2. **All downstream agents** read from the created context files
   - Specifier uses standards for frontend/backend design validation
   - Planner uses standards for task structuring
   - Builder uses standards for implementation patterns
   - Tester uses standards for test design

### Scenario 2: Technology Upgrade (e.g., Framework Version Change)

1. **Context Updater** detects version change in configuration files
2. **Updates** frontend-context.md with new patterns, deprecations, migration guidance
3. **Tracks** change with CTX-UPDATE-* ID
4. **Escalates** to Traceability Manager if MAJOR
5. **Active specs/plans** are flagged if they reference old patterns

### Scenario 3: Architecture Refactoring

1. **Project changes** folder structure (e.g., split services into modules)
2. **Context Updater** detects structure change
3. **Updates** backend-context.md and project-context.md with new architecture
4. **Traceability Manager** assesses impact on active implementations
5. **Affected implementations** are re-validated against new standards

### Scenario 4: Parallel Development

1. **Context Updater** runs weekly to sync detected changes
2. **Specifier** reads current standards for new features
3. **Builder** implements using latest standards
4. **Tester** validates against latest testing patterns
5. **All agents** work from single source of truth

## Best Practices

### For Context Builder

- **Detect tech stack automatically** by scanning configuration files before asking the user
- **Include specific versions and dependencies** in all standards files
- **Document domain principles** (e.g., banking, healthcare) that constrain design choices
- **Create clarification questions** for ambiguous business needs
- **Link all CTX-* IDs** to downstream BRD/FR/NFR/SPEC mappings

### For Context Updater

- **Run automatically** when dependency or configuration files change (via pre-commit or CI/CD)
- **Never silently modify** approved guidance; escalate breaking changes
- **Preserve decision history** with detailed change logs
- **Categorize impact** (MINOR/MODERATE/MAJOR) to guide escalation
- **Check downstream impact** on active specs and plans before applying major changes

### For Downstream Agents

- **Read context files first** before starting any phase (Spec, Plan, Build, Test)
- **Validate design choices** against standards before accepting new patterns
- **Document deviations** from standards with clear reasoning
- **Use traceability** to link all work back to context decisions
- **Flag standards conflicts** for Context Updater to resolve

### For Traceability Manager

- **Track context lifecycle** from CTX-* creation through all PDLC phases
- **Audit context changes** to understand downstream impact
- **Validate** that specs/plans/code align with current standards
- **Escalate** when specs reference outdated patterns
- **Maintain chain of custody** for all context decisions

## Troubleshooting

### Issue: Standards Files Not Found

**Solution:** Run Context Builder to initialize context for the project. Context Builder scans the project structure and creates all necessary standards files.

### Issue: Specs Reference Outdated Standards

**Solution:** Check `requirement/Traceability_Matrix.md` for CTX-UPDATE-* entries. Run Context Updater to detect latest changes, then re-validate affected specs against current standards.

### Issue: Build/Test Failures After Standards Update

**Solution:** Context Updater tracks all changes with CTX-UPDATE-* IDs and escalates MAJOR changes. Review the escalation, assess impact on active implementations, and coordinate re-validation with affected builders/testers.

### Issue: Context Files Out of Sync

**Solution:** Run Context Updater with `--force-rescan` to detect all changes in project state and sync all context files. Review change log to understand what was updated.

## Command Reference

### Context Builder Invocation

```bash
# Initialize context for a new project
# Run: Context Builder agent with user-provided business context and tech stack

# Example user input:
"Create context for a web/mobile application. Frontend: React/Vue, state management, routing.
Backend: Node.js/Python, API framework. Testing: Jest/pytest. Compliance: GDPR, applicable regulations."

# Outputs:
# - .github/contexts/project-context.md
# - .github/contexts/frontend-context.md
# - .github/contexts/backend-context.md
# - .github/contexts/testing-standards.md
# - requirement/Context_ProjectName.md
# - Updated requirement/Traceability_Matrix.md
```

### Context Updater Invocation

```bash
# Automatic trigger on dependency/config changes
# Manual trigger: Context Updater agent

# Scans:
# - package.json, pubspec.yaml, requirements.txt, etc.
# - Folder structure changes
# - Configuration files (.env.*, tsconfig.json, etc.)
# - CI/CD pipeline changes

# Outputs:
# - Updated applicable .github/contexts/*.md files
# - Updated requirement/Context_{ProjectName}.md with change history
# - Updated requirement/Traceability_Matrix.md with CTX-UPDATE-* IDs
```

## See Also

- [Specification Execution Gates](./../rules/specification-execution-gates.md) - Spec validation using context
- [Planning Execution Gates](./../rules/planning-execution-gates.md) - Plan validation using context
- [Implementation Execution Gates](./../rules/implementation-execution-gates.md) - Implementation validation using context
- [Traceability Standards](./../rules/traceability-standards.md) - Context ID tracking and mapping

## Summary

The Context Management System provides:

✅ **Single source of truth** for business drivers, technology decisions, and architectural standards  
✅ **Automatic detection** of tech stack and project structure  
✅ **Synchronized standards** across frontend, backend, and testing  
✅ **End-to-end traceability** from business context through implementation  
✅ **Continuous alignment** as projects evolve, via Context Updater  
✅ **Conflict detection** when context drifts from active work  

**Result:** All PDLC agents operate from current, validated context, eliminating ambiguity and ensuring consistent implementation quality.
