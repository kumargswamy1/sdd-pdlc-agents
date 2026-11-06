---
description: Routes security standards (OWASP baseline and secure coding) to PDLC agents across design, specification, planning, implementation, testing, review, and documentation.
---

# Security Standards Routing

Single source of truth for which security standard each PDLC agent applies, at every stage and not only during coding. Coding standards are routed in `.github/rules/coding-standards-routing.md`; financial standards in `.github/rules/financial-standards-routing.md`.

## Standards Inventory

| Standard | File | Use |
|---|---|---|
| OWASP baseline | `.github/rules/security/OWASP Security Guidelines & Best Practices.md` | Top 10 awareness (section 1); secure-development checklist A-R (section 2); mobile (section 3); AI/LLM/RAG/MCP/agentic (section 4); compliance hierarchy (section 5) |
| Secure coding | `.github/rules/security/Secure_Coding_Best_Practices.md` | Implementation-level practices (sections 1-14) and the Pull Request Security Checklist |
| Repository security rules | `.github/rules/security-quality-standards.md` | Mandatory repository controls and review blockers |
| FSDM privacy and regulatory data | `.github/rules/fsdm-standards/reference/02-privacy-and-regulatory-governance.md` | Only when FSDM is `APPLICABLE` (see financial routing) |

The OWASP Top 10 is risk awareness, not a complete specification; use the checklist sections for testable requirements. Where security guidance conflicts with an approved requirement or a repository rule, raise a `CLAR-*` item for a human decision; the stricter control wins unless a human accepts the deviation.

## Selecting Security Sections

Baseline for every project that has code, APIs, data, or infrastructure: OWASP sections 1, 2 and 5, Secure coding sections 1, 2, 6, 7, 8, 11, 12, 13, and the repository security rules. Add by project type or feature:

| Project type / feature in the story | Add |
|---|---|
| Web or browser frontend | OWASP D (session), G (output encoding, browser security); Secure coding 4, 9 |
| Backend, services, APIs | OWASP C (authorization), E, F (input, injection), J (API), L (errors); Secure coding 3, 5, 10 |
| Authentication, sessions, tokens | OWASP B, D; Secure coding 5, 9 |
| Personal, financial, or regulated data | OWASP H (cryptography/data protection), R (privacy); Secure coding 8; plus FSDM `02` when FSDM applies |
| File upload or download | OWASP K |
| Secrets, configuration, infrastructure, CI/CD, dependencies | OWASP I, N, O, P; Secure coding 7, 12; `.github/rules/environment-standards.md` |
| Logging, monitoring, auditing | OWASP M; Secure coding 11 |
| Mobile app (Flutter, iOS, Android) | OWASP section 3 |
| LLM, RAG, MCP, or agentic features | OWASP section 4 |
| Cloud, Databricks, data pipelines | Secure coding 14 |
| Data analytics / ETL with no UI or API | Baseline plus Secure coding 8, 14 and OWASP H, I; mark web/API items `NOT_APPLICABLE` with reason |

Rules:
- Apply the baseline to every project type; apply additions only where the story or detected stack involves the feature. Mark non-applicable items `NOT_APPLICABLE` with evidence rather than omitting them silently.
- Record the decision in `spec.md` under `## Security Standards Applied` with columns `Surface / Feature Area | Standards And Sections | Gaps`. Later stages inherit it and update it when scope changes.
- Security requirements come from the approved source requirements plus controls the standards make mandatory for the feature type; do not invent business requirements. An unclear applicability is a `CLAR-*` item.

## Stage Routing Matrix

| PDLC stage / agent | Security use |
|---|---|
| Context Builder / Context Updater | Record the security posture as evidenced (auth model, data classification, secrets handling, security tooling, mobile/AI features) in the owning context as `IMPLEMENTED`/`DOCUMENTED/REQUIRED`; do not restate standard content |
| Requirement intake / canonical requirements | Inject security and privacy NFRs for the feature types in scope (OWASP A, B, C, H, R; Secure coding 1, 6, 8), citing the source of each |
| Technical Specifier | Threat-model-level design (OWASP A; Secure coding 1): trust boundaries, abuse cases, authn/authz, validation, data protection, API security, logging/audit, secrets; record `## Security Standards Applied` |
| Implementation Planner | Plan security tasks and security tests from the spec (injection, XSS, authorization, secrets, dependency and secret scanning, CI security gates) per Secure coding 13 and OWASP P, Q |
| Implementation Builder | Implement the spec's controls per Secure coding and the selected OWASP sections; parameterized queries, output encoding, no secrets, safe logging; walk the Pull Request Security Checklist before handoff |
| Compliance Reviewer | Review all artifacts at their stage: spec and plan for missing controls, code and tests for violations; use the Pull Request Security Checklist and map to `security-quality-standards.md` blockers |
| API Tester | Authn/authz, validation, injection, rate limiting, error leakage, and token cases (OWASP J, B, C, F; Secure coding 10) where the spec defines the control |
| Functional Automation Test | Browser-security behavior the spec defines: session/token handling, output encoding, no sensitive data in UI, logs, or screenshots (OWASP D, G; Secure coding 9) |
| QA Test Case Generator | Cases only for story-evidenced security controls, using OWASP checklist items; never add rules the story does not imply |
| Technical Documenter | Document implemented controls, threat/abuse assumptions, accepted deviations, and open findings in `SECURITY.md` |
| Traceability Manager | Verify `## Security Standards Applied` is present and each in-scope control traces to task, code, test, and review, or an explicit accepted deviation |

## Findings And Severity

Report results with the stage's existing review format, plus:

`SECURITY_STANDARDS_RESULT: [PASS|WARN|BLOCK|NOT_APPLICABLE|INCOMPLETE_ARTIFACT] [BLOCKERS: <n>] [REASON: <short reason>]`

| Finding | Review severity | Effect |
|---|---|---|
| Hardcoded secret, plaintext sensitive data in logs, injection or authentication bypass, missing authorization on a protected operation | Critical | Blocks handoff |
| Required control missing or violated (server-side validation, output encoding, weak cryptography, unsafe deserialization, insecure session/token handling) | High | Blocks handoff |
| Specified security control without a planned task or test; dependency/secret scanning absent where the plan requires it | Medium | Blocks handoff |
| Security hygiene or documentation deviation | Low | `REVIEW_GATE_WARNING` path |
| Selected security standards not recorded in the spec/plan, or applied without evidence | Medium (`INCOMPLETE_ARTIFACT`) | Blocks until recorded |

Cite file:line (or spec/plan section), the standard file, and the section. Use synthetic data only; never include real secrets, tokens, or customer data in evidence.
