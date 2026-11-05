---
title: Context Management
description: What context is, what is needed to create it, how Context Builder produces it, and which PDLC agents use it.
---

Context is the foundation every PDLC agent builds on. This document explains what it is, what is needed to create it, how Context Builder produces it, and which agents use it. 

## 1. What Is Context and Why Contextualization Matters

**Context** is the verified, source-cited knowledge about a project, stored as files in `.github/contexts/`. It covers the business requirements and rules, the industry domain, the frontend and backend technology and conventions, and the testing approach. Agents read these files before they start work.

**Contextualization** is the process of gathering that knowledge, checking it against sources, routing each fact to the file that owns it, and keeping it current as the project changes.

Agents do not remember a project between runs. Without written context, each agent guesses, and different agents guess differently.

| Without context | With context |
|-----------------|--------------|
| Agents assume a generic tech stack and conventions | Agents follow the stack and patterns found in the project |
| Business rules are re-interpreted at each stage | One canonical source of business rules in `business-context.md` |
| Specs, plans and code can contradict each other | Every stage reads the same files, so outputs stay consistent |
| Facts cannot be traced to a source | Each fact cites its source and carries a `CTX-*` trace ID |
| Documents drift as the code changes | Context Updater keeps the files aligned with sources and code |
| Domain and compliance needs are easy to miss | Domain terms and compliance obligations are recorded once and reused |

Context is a prerequisite, not an optional step. Run Context Builder first for a new project.

## 2. Information Needed to Create Context

Context Builder needs at least one requirements source or an existing codebase. For a greenfield project with no code, it asks for the planned stack.

| Information | What to provide |
|-------------|-----------------|
| Business context | Product purpose, industry, target users, business outcomes |
| Requirements | Every requirement with actors, triggers, flows, validations, calculations and acceptance criteria |
| Business logic and rules | Eligibility and decision rules, state changes, permissions, exceptions |
| Constraints and decisions | Scope boundaries, assumptions, risks, regulatory and operational limits |
| Stakeholders and success criteria | Owners, sponsors, user groups, measurable outcomes |
| Domain knowledge | Industry terminology, regulations, reference material |
| Frontend details | Framework and version, routing, state, screens, themes, colours, fonts, spacing, accessibility |
| Backend details | Runtime, services, API routes and contracts, data, integrations, authentication, deployment |
| Testing details | Frameworks, test layout, mocks, coverage rules, CI test execution |
| Other standards | Any extra standards the user wants agents to follow |

**Where this information comes from, in priority order:**

1. A Confluence link (preferred). **Note:** Confluence connection requires MCP (Model Context Protocol) configuration. Context Builder will establish the MCP connection to Confluence to fetch and parse content directly.
2. Attached Word or PDF documents, when no Confluence link is given.
3. The existing or legacy project: documentation, source code, configuration and tests.
4. Answers from the user, for greenfield projects or to resolve conflicts the sources cannot settle.

Never put real customer data, credentials, tokens or secret values in any context file.

## 3. How to build the Context

**File:** `context-builder.agent.md`

Context Builder is started manually. It creates context only when the target file is missing or objectively empty. It never overwrites substantive content or user-authored standards.

### Sample Prompts

Here are examples of how to invoke Context Builder for different scenarios:

**Scenario 1: Building from Confluence**
```
Build context from https://confluence.company.com/pages/viewpage.action?pageId=12345678

Requirements are documented in Confluence. Extract business requirements, technical stack, frontend and backend details, and testing approach. Create all missing context files and assign CTX-* trace IDs.
```

**Scenario 2: Building from Attached Documents**
```
Build context from the attached Product_Requirements_Document.docx and Technical_Architecture.pdf

The PRD contains business requirements and user stories. The Technical Architecture document specifies the backend stack, API contracts, and database design. Create business-context.md and backend-context.md. For missing information (frontend design, testing), ask what the planned tech stack is.
```

**Scenario 3: Building from Existing Codebase**
```
Build context for the project at /path/to/existing-project

Inspect the code from the given path of the sourcecode. Infer the frontend stack (e.g., React, Angular), backend stack (e.g., Node.js, Python, Go), testing frameworks, and implemented features. Extract business logic from code. Create all context files and note any gaps.
```

**Scenario 4: Building from Multiple Sources**
```
Build context using:
- Confluence page: https://confluence.company.com/pages/viewpage.action?pageId=87654321 (business requirements)
- Attached file: Architecture_Decisions.pdf (technical decisions)
- Existing codebase at /path/to/repo (current implementation reference)

Reconcile conflicting information: trust the Confluence document for requirements, and the codebase for what is actually implemented. Note any gaps or mismatches in the output.
```

**What it takes as input:**

| Input | How it is used |
|-------|----------------|
| Confluence link | Preferred source for requirements and business context. Requires MCP connection to Confluence to fetch and parse content. If access fails or MCP is not configured, it asks for a manual export or an alternative source |
| Attached Word or PDF documents | Fallback source. A file the user explicitly designates, such as "this is the backend-context", is placed unchanged in `.github/contexts/` |
| Existing or legacy project | Always inspected when available. Code shows implemented behaviour; documents show intended behaviour |
| Files already in `.github/contexts/` | Read as sources and preserved. Never edited |
| Repository rules in `.github/rules/` | Applied while the context is written |
| User answers | Planned stack and open questions for greenfield projects, or conflicts the sources cannot resolve |

**What it does:**

1. Gathers and reads the context sources.
2. Classifies the project as existing or greenfield, and asks only for decisions it cannot verify.
3. Extracts evidence and routes each fact to the file that owns it, without duplicating content across files.
4. Marks each finding `IMPLEMENTED`, `DOCUMENTED/REQUIRED`, `USER-PROVIDED`, `RECOMMENDED` or `N/A`, with the source. Unknown details are written as `N/A` with a reason, not guessed.
5. Creates the missing context files and assigns `CTX-*` trace IDs.
6. Reports the files created or skipped, then stops for human review.

**What it outputs:**

| Output file | Contents |
|-------------|----------|
| `.github/contexts/business-context.md` | Canonical business context: requirements, business logic and rules, workflows, constraints, assumptions, stakeholders, acceptance criteria. For existing projects it also holds a feature catalogue. It links to the technical contexts and does not repeat their detail |
| `.github/contexts/domain-context.md` | Supplemental industry terminology and reference material, linked from `business-context.md` |
| `.github/contexts/frontend-context.md` | Frontend stack and architecture, screens and components, and detailed UI design such as themes, fonts and styles |
| `.github/contexts/backend-context.md` | Backend stack, APIs and contracts, data, integrations, security, deployment and operations |
| `.github/contexts/testing-context.md` | Test frameworks, structure, mocks, coverage and strategy |
| Additional or designated files in `.github/contexts/` | User-provided standards and designated source files, preserved and indexed in `business-context.md` |

A file that already has substantive content is reported as `SKIPPED_EXISTING`, and any change to it goes to Context Updater. After the run, a person reviews the files, then manually starts the next stage. When the source code, documents or dependencies change later, a person starts [Context Updater](README.md#context-updater).



## 4. What is Standards and Role of Standards

**How Standards Complement Context**

Context defines *what* the project needs (requirements, business rules, tech stack, domain knowledge). Standards define *how* the project delivers it (architecture, testing, security, quality gates, traceability). Together, they ensure every agent makes consistent, auditable decisions:

- **Context** = source of truth for requirements and tech choices
- **Standards** = guardrails that shape how requirements become code, tests, and documentation

Standards are applied by Context Builder during context creation and enforced by every agent during execution. If an agent detects a conflict between context and standards, it records the gap and requests explicit resolution or a Context Updater run.

**Standards Present and Related Rules Files**

| Standard Category | Related Rules Files | Coverage |
|---|---|---|
| **Coding Standards** | [`coding-standards.md`](coding-standards.md), [`architectural-standards.md`](architectural-standards.md) | Cross-language baseline for readable, secure code; input validation at trust boundaries, structured logging with correlation IDs, secret protection, dependency management, error handling with domain-prefixed codes (AUTH-XXX, CUST-XXX, ORDER-XXX, KYC-XXX, AML-XXX), BIAN vocabulary alignment |
| **Security & Compliance** | [`security-quality-standards.md`](security-quality-standards.md), [`architectural-standards.md`](architectural-standards.md), [`coding-standards.md`](coding-standards.md) | Authentication/authorization, role-based access control, PII masking, centralized secret management, OWASP controls, audit trails for sensitive actions |
| **Quality & Testing** | [`security-quality-standards.md`](security-quality-standards.md), [`implementation-execution-gates.md`](implementation-execution-gates.md), [`qa-test-case-generator.rules.md`](qa-test-case-generator.rules.md) | 80% unit-test coverage gates, security testing (unauthorized/privilege-escalation scenarios), integration testing, dependency scanning, SBOM requirements |
| **Banking & Regulatory** | [`architectural-standards.md`](architectural-standards.md), [`security-quality-standards.md`](security-quality-standards.md), [`versioning-standards.md`](versioning-standards.md) | Thailand PDPA, KYC/AML screening, maker-checker workflows, ISO 20022 message versioning, audit compliance |
| **Data Protection & Privacy** | [`security-quality-standards.md`](security-quality-standards.md), [`architectural-standards.md`](architectural-standards.md), [`environment-standards.md`](environment-standards.md), [`versioning-standards.md`](versioning-standards.md) | Data classification (PII, SENSITIVE_FINANCIAL, CONFIDENTIAL, PUBLIC), masking rules, FSDM versioning, database migrations with rollback |
| **AI Agent Safety** | [`ai-agent-safety.md`](ai-agent-safety.md), [`coding-standards.md`](coding-standards.md) | Trust-boundary controls for external content, tool-use verification, data protection for secrets/PII, OWASP GenAI Security guidance for LLM features |

**Critical Standards for Specification and Planning**

- [`architectural-standards.md`](architectural-standards.md) — Architecture principles and dependency rules
- [`traceability-standards.md`](traceability-standards.md) — Trace ID assignment and matrix maintenance
- [`security-quality-standards.md`](security-quality-standards.md) — Security and compliance review criteria
