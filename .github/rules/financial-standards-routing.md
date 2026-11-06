---
description: Stage-to-standard routing for BIAN, FSDM, and ISO 20022 across the PDLC agents, with applicability, evidence, status, and severity rules.
---

# Financial Standards Routing (BIAN, FSDM, ISO 20022)

Single source of truth for which banking/financial-data standard each PDLC agent must load and apply. Agents reference this file instead of duplicating the matrix.

## Standards And Entry Points

| Standard | Scope | Entry point (read first) | Progressive-disclosure content |
|---|---|---|---|
| BIAN v14.0 | Business capability and Service Domain mapping, Semantic API alignment, service boundaries | `.github/rules/bian-standards/references/bian-validation-framework.md` (workflows, evidence labels, finding format) | `references/bian-concepts.md`, `bian-v14-service-domain-index.md`, `bian-release-14-changes.md`, `bian-rule-catalog.md`, `bian-source-registry.md`; `examples/` |
| FSDM | Canonical data entities, privacy classification, monetary/temporal precision, BCBS 239 lineage, ledger immutability, master/reference data, data contracts | `.github/rules/fsdm-standards/reference/` files selected by the FSDM stage table below | `reference/01`-`07`; output contract in `07-compliance-output-schema.md` |
| ISO 20022 | Payment (`pacs.*`), cash-management (`camt.*`), securities-settlement (`sese.*`) message mapping, validation, error codes, tests | `.github/rules/iso-20022-Standards/ISO-20022-MASTER-INDEX.md` | `ISO-20022-Part1-Architecture.md` to `Part5-TestingGuide.md` |

Load only the files the current stage needs. Do not load every reference file unless performing a full cross-stage audit.

### FSDM Reference Files By Stage (`.github/rules/fsdm-standards/reference/`)

| FSDM stage | Artifacts | Load |
|---|---|---|
| 1 Requirements and domain discovery | BRDs, epics, stories, domain models | `01`, `02`, `07` |
| 2 Logical and physical data modeling | ERDs, DBML, schemas, DDL | `01`, `02`, `03`, `04`, `05`, `07` |
| 3 API and event schema design | OpenAPI, GraphQL, AsyncAPI, Avro, JSON Schema | `02`, `03`, `04`, `06`, `07` |
| 4 Application code and data access | Source, ORM entities, repositories, queries | `02`, `03`, `04`, `05`, `07` |
| 5 Testing and CI/CD gate | Fixtures, seed data, migrations, PR diffs | `02`, `06`, `07` |

PDLC mapping: Specifier = stages 1-3; Planner = stages 2-5 planning; Builder = stages 2-4; Reviewer, API Tester, and test agents = the stage matching the artifact reviewed or tested (stage 5 for tests and gates). FSDM verdicts use `07-compliance-output-schema.md`; evidence is the exact entity, column, JSON path, or `file:line`.

## Applicability (Decide Once, In The Spec)

Determine applicability per standard from the approved requirements, trace history, and implementation footprint. Record it with evidence; never assume it and never invent standards requirements the source does not imply.

| Standard | `APPLICABLE` when the story involves | `NOT_APPLICABLE` when |
|---|---|---|
| BIAN | A banking capability, product/service domain, banking API, or service boundary (accounts, payments, lending, cards, customer, KYC/AML, limits, etc.) | Purely non-banking UI or tooling change with no banking capability or API |
| FSDM | Persisted or transmitted financial or customer data: money amounts/rates, parties, accounts/arrangements, products, financial events/ledger, PII/regulatory data, schemas, APIs, events, analytical contracts | No data model, API/event schema, financial computation, or sensitive-data change |
| ISO 20022 | Payments, transfers, direct debits, returns, statements/balance reporting, notifications, securities settlement, or interfaces exchanging/aligning with ISO 20022 messages | No payment, statement, settlement, or ISO 20022-aligned interface |

- Record the decision in `spec.md` under `## Financial Standards Applicability` with columns `Standard | Applicability | Evidence (FR/NFR/SPEC/code path) | Scope Notes`.
- `NOT_APPLICABLE` requires cited evidence. Missing or ambiguous evidence is a clarification item (`CLAR-*`), not an exemption.
- Downstream stages inherit the spec decision; reclassify as `APPLICABLE` if planning or implementation introduces an in-scope change.

## Stage Routing Matrix

| PDLC stage / agent | BIAN (workflow numbers per `bian-validation-framework.md` section 2) | FSDM (stage per the FSDM stage table above) | ISO 20022 |
|---|---|---|---|
| Context Builder / Context Updater | Record candidate business capabilities and Service Domains as `CTX-DOMAIN-*` with evidence labels; do not decide mappings | Record data classifications, regulatory data obligations, and canonical entity vocabulary in context | Record message families and interfaces in use (`pacs`, `camt`, `sese`) with source evidence |
| Requirement intake / canonical requirements | Map each capability to a candidate Service Domain with status `ALIGNED`, `EXTENDED`, `UNMAPPED`, or `NOT_APPLICABLE` | Stage 1: map business nouns to FSDM core concepts; inject privacy/retention/lineage NFRs | Map payment/statement/settlement requirements to message types and business rules |
| Technical Specifier | 2.1/2.2: Service Domain, Control Record, BQs, operations, Semantic API file; 2.4 for API contract delta | Stage 1-3: entity mapping, data model, API/event schema requirements (`x-fsdm-*`, money, headers, classification) | Part 1 + domain part: message mapping, field-level rules, validation levels, error codes, `Dbtr/Cdtr/UETR/EndToEndId` alignment |
| Implementation Planner | Tasks for Service Domain / API alignment and gap closure; each task traces to mapped SD | Stage 2-4: tasks for DDL, schema, code, lineage, idempotency, redaction; Stage 5: invariant and contract tests | Tasks for parsers/serializers, validators, error responses, audit trail; tests per Part 5 |
| Implementation Builder | 2.4: implemented API and component boundaries match the mapped Service Domain; record deviations | Stage 2-4: DDL, schema, and code rules (BLOCK on float money, mutable ledger, PII in logs/URLs, missing lineage) | Implement per domain part; apply 4-level validation and error handling from Part 1 |
| Compliance Reviewer | 2.3/2.6: architecture and compliance findings with evidence labels | All stages: verdict per `reference/07-compliance-output-schema.md` | Verify field, rule, validation-level, and error-code coverage; test coverage per Part 5 |
| API Tester | 2.4: operation-level contract checks (action term, method, payload) when BIAN-aligned | Stage 3/5: money format, idempotency replay, headers, PII-in-URL, error redaction | Valid/invalid message cases, business-rule rejections, error codes |
| Functional Automation Test | Only for flows mapped to a Service Domain | Stage 5: synthetic data only; multi-currency, rounding, bitemporal display | End-to-end payment/statement/settlement workflows per Part 5 |
| QA Test Case Generator | Cases for mapped business capabilities and rules | Cases for financial invariants and data-contract rules | Cases from Part 5 templates and error-code catalogue |
| Technical Documenter | Document SD mapping, deviations, and `EXTENDED`/`UNMAPPED` decisions | Document data classification, lineage, retention, contracts | Document message mappings, validation, and error handling |
| Traceability Manager | Verify `BIAN-*` mapping IDs trace to FR/SPEC/TASK/CODE/TEST | Verify `FSDM-*` finding IDs resolved or accepted | Verify ISO message mapping trace to SPEC/TASK/CODE/TEST |

## Conflict And Precedence

1. Approved requirements and stage hard gates are binding; standards do not add business scope. A standards rule that conflicts with an approved requirement is raised as a `CLAR-*` item for a human decision, not silently resolved.
2. Where FSDM and ISO 20022 both constrain a payment or statement payload, satisfy both: FSDM governs data typing, classification, and lineage; ISO 20022 governs message structure and business rules.
3. BIAN is descriptive architecture guidance. Apply the `bian-standards` evidence labels (`Official BIAN`, `BIAN-derived`, `Architecture recommendation`, `Unverified`); never claim BIAN compliance or certification, and never invent Service Domains, BQs, or operations. Use the v14.0 index to verify existence.
4. This repository's technical rules (`architectural-standards.md`, `security-quality-standards.md`, `versioning-standards.md`) still apply. Surface conflicts (for example, FSDM `Idempotency-Key`/`X-Trace-Correlation-Id` headers versus the `X-Correlation-ID` contract) as `CLAR-*` for a human decision; do not choose silently.
5. Do not reproduce standards documents in outputs. Cite file and section.

## Evidence And Traceability

- Create mapping IDs where a standard drives a decision: `BIAN-*` (Service Domain mapping), `FSDM-*` (data/finding), `ISO-*` (message mapping). Carry them in the existing chain: `FR/NFR -> SPEC -> TASK -> CODE -> TEST -> REVIEW -> DOC`; add them to the `Evidence and Rationale`/notes of the existing matrix columns, do not change matrix columns.
- Every mapping cites the standard file/section used and, for BIAN, the release and evidence label.
- Use synthetic data only. No real customer data, account numbers, credentials, or production data in any standards evidence.

## Findings, Severity, And Status

Report standards results using the stage's existing review format, plus this line:

`FINANCIAL_STANDARDS_RESULT: [PASS|WARN|BLOCK|NOT_APPLICABLE|INCOMPLETE_ARTIFACT] [BIAN: <PASS|WARN|BLOCK|NOT_APPLICABLE>] [FSDM: <PASS|WARN|BLOCK|NOT_APPLICABLE>] [ISO20022: <PASS|WARN|BLOCK|NOT_APPLICABLE>] [BLOCKERS: <n>] [REASON: <short reason>]`

Severity mapping into the `.github/rules/pdlc.md` review policy:

| Standard result | Review severity | Effect |
|---|---|---|
| FSDM `BLOCK` finding | High (Critical for PII/secret exposure or mutable ledger) | Blocks handoff |
| FSDM `WARN` finding | Low | `REVIEW_GATE_WARNING` path |
| FSDM `INCOMPLETE_ARTIFACT` | Medium | Blocks until the missing specification is supplied |
| BIAN Critical/High/Medium | Same severity | Blocks handoff |
| BIAN Low/Informational | Low | `REVIEW_GATE_WARNING` path |
| BIAN `Unverified` claim stated as fact, or fabricated Service Domain/BQ/operation | Critical | Blocks handoff |
| ISO 20022 required-field, validation-level, or business-rule gap | High | Blocks handoff |
| ISO 20022 missing test or error-code coverage | Medium | Blocks handoff |
| ISO 20022 naming/documentation gap | Low | `REVIEW_GATE_WARNING` path |

An applicable standard with no evidence of being applied is `INCOMPLETE_ARTIFACT`, never `PASS`.
