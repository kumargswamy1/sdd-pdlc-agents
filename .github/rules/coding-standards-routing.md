---
description: Routes coding standards to PDLC agents by technology stack and stage.
---

# Coding Standards Routing

Single source of truth for which coding standards each PDLC agent applies. Security guidance is routed separately in `.github/rules/security-standards-routing.md`; financial/banking standards in `.github/rules/financial-standards-routing.md`.

## Standards Inventory

| Standard | File | Applies to |
|---|---|---|
| General coding | `.github/rules/coding-standards/General_Coding_Best_Practices.md` | Every project and stack (always) |
| React.js | `.github/rules/coding-standards/React_JS_Coding_Best_Practices.md` | React/JavaScript/TypeScript web frontends |
| .NET backend | `.github/rules/coding-standards/DotNet_Backend_Coding_Best_Practices.md` | C#/.NET backends and services |
| Python | `.github/rules/coding-standards/Python_Coding_Best_Practices.md` | Python code, including Python backends, scripts, and PySpark code |
| PySpark/Databricks | `.github/rules/coding-standards/PySpark_Databricks_Coding_Best_Practices.md` | PySpark, Spark SQL, Databricks notebooks and jobs (apply together with Python) |

Repository-level rules still apply: `.github/rules/architectural-standards.md`, `.github/rules/versioning-standards.md`, `.github/rules/environment-standards.md`. Where a coding standard conflicts with an approved requirement or those rules, raise a `CLAR-*` item for a human decision; do not choose silently.

## Selecting Standards By Stack

Identify the frontend and backend technology from `.github/contexts/frontend-context.md`, `.github/contexts/backend-context.md`, and `.github/contexts/testing-context.md`, falling back to manifests and source (`package.json`, `pubspec.yaml`, `*.csproj`, `pom.xml`, `requirements.txt`, `pyproject.toml`) when context is missing. Select per surface:

| Detected stack | Load |
|---|---|
| Any stack | General coding |
| React / JS / TS frontend | + React.js |
| .NET / C# backend | + .NET backend |
| Python backend, scripts, or tooling | + Python |
| PySpark / Databricks / Spark SQL | + PySpark/Databricks and Python |
| Flutter / Dart, iOS, Android, Node.js, Java, Go, or any stack without a file above | General coding only; record `NO_STACK_SPECIFIC_STANDARD` and follow the project's own frontend/backend context. Do not borrow another stack's rules |

Rules:
- General coding applies to every project type, including those with no stack-specific file.
- Stack-specific files refine General coding. If they disagree, the stack-specific rule wins for style and framework usage.
- Load only the sections a stage needs; each file is organised by numbered section with a Review Checklist.
- Never invent rules for a stack that has no standard file. Record the gap in the spec and ask the human to supply a standard if one is needed.
- Record the selection per surface in `spec.md` under `## Coding Standards Applied` with columns `Surface | Detected Stack | Standards Loaded | Gaps`. Later stages inherit it and update it only if the stack changes.

## Stage Routing Matrix

| PDLC stage / agent | Coding standards use |
|---|---|
| Context Builder / Context Updater | Record the detected stack and applicable standard files in the owning frontend/backend/testing context as `DOCUMENTED/REQUIRED` (`NO_STACK_SPECIFIC_STANDARD` where none exists); do not restate standard content |
| Technical Specifier | Detect stack, record `## Coding Standards Applied`; specify structure, naming, error handling, and testing conventions only as the selected standards and requirements require |
| Implementation Planner | Plan a lint/format/analyzer task per changed surface and unit-test tasks that follow the selected standard's testing section |
| Implementation Builder | Implement per General coding plus the stack standard; run the repository formatter/linter/analyzers; walk each selected standard's Review Checklist before handoff |
| Compliance Reviewer | Review code and tests against General coding and the stack standard's Review Checklist; cite file:line and section |
| API Tester | Use the backend standard's API design and exception-handling sections for contract and error-envelope checks |
| Functional Automation Test | Use the frontend standard's accessibility and testing sections where they define testable behavior |
| QA Test Case Generator | Add cases only for story-evidenced rules; never invent standards requirements |
| Technical Documenter | Document applied standards, deviations, and gaps (`NO_STACK_SPECIFIC_STANDARD`) in `ARCHITECTURE.md` |
| Traceability Manager | Verify `## Coding Standards Applied` is present and carried through plan, code, and review |

## Findings And Severity

Report results with the stage's existing review format, plus:

`CODING_STANDARDS_RESULT: [PASS|WARN|BLOCK|NOT_APPLICABLE|INCOMPLETE_ARTIFACT] [STACK_GAPS: <n>] [BLOCKERS: <n>] [REASON: <short reason>]`

| Finding | Review severity | Effect |
|---|---|---|
| Violation of a stack-specific or General rule affecting correctness, maintainability, or testability (swallowed exceptions, unmanaged async, missing tests for changed code) | Medium | Blocks handoff |
| Formatter/linter/analyzer failing on changed code | Medium | Blocks handoff |
| Style, naming, or documentation deviation | Low | `REVIEW_GATE_WARNING` path |
| Selected standards not recorded in the spec/plan, or applied without evidence | Medium (`INCOMPLETE_ARTIFACT`) | Blocks until recorded |
| Stack without a standard file (`NO_STACK_SPECIFIC_STANDARD`) | Informational | Record only; not a failure |

Cite file:line, the standard file, and the section. Security findings follow `.github/rules/security-standards-routing.md`.
