# Reference 07: Standardized FSDM Governance Output Contract

Every AI SDLC stage evaluation executed by the FSDM Governance Agent must output two structured sections:
1. A machine-parsable JSON verdict block fenced with ```json that automated CI/CD pipeline gates evaluate to allow or block progression.
2. A concise Markdown Remediation Report providing exact, copy-ready schema or code fixes for every violation detected.

## 1. Machine-Readable JSON Output Schema

```json
{
  "sdlc_stage": "STAGE_1_REQUIREMENTS | STAGE_2_DATA_MODEL | STAGE_3_API_EVENT | STAGE_4_CODE | STAGE_5_CICD_GATE",
  "overall_verdict": "PASS | WARN | BLOCK | INCOMPLETE_ARTIFACT",
  "reference_files_evaluated": [
    ".github/rules/fsdm-standards/reference/01-canonical-domain-taxonomy.md"
  ],
  "summary_metrics": {
    "total_checks_executed": 0,
    "critical_blockers": 0,
    "warnings": 0,
    "passed_checks": 0
  },
  "fsdm_domain_mappings": [
    {
      "artifact_entity": "string",
      "fsdm_core_concept": "InvolvedParty | Arrangement | Product | Event | Condition | ResourceItem | Location | Classification | BusinessDirection",
      "bian_service_domain": "string",
      "highest_data_classification": "PUBLIC | INTERNAL | CONFIDENTIAL | RESTRICTED_PII | SENSITIVE_PERSONAL_DATA | REGULATORY_CRITICAL"
    }
  ],
  "findings": [
    {
      "finding_id": "FSDM-MOD3-001",
      "reference_file": ".github/rules/fsdm-standards/reference/03-monetary-temporal-and-iso20022.md",
      "rule_violated": "Rule 3.1 (Strict Prohibition of Floating-Point Currency)",
      "severity": "BLOCK | WARN",
      "location": "Exact table.column, JSON path, or file:line",
      "violation_description": "Precise technical explanation of the architectural or regulatory violation.",
      "deterministic_remediation": "Exact SQL DDL, OpenAPI snippet, or source code modification required to resolve the violation."
    }
  ]
}
```

## 2. Deterministic Verdict Threshold Rules
- **`BLOCK`:** Must be set whenever one or more findings have `"severity": "BLOCK"`. Mandatory `BLOCK` triggers include:
  - Floating-point data types (`FLOAT`, `DOUBLE`, `REAL`, or unvalidated JSON `number`) used for monetary amounts or rates.
  - Monetary amount fields missing a paired ISO 4217 `currency_code` attribute.
  - Conflated `Involved Party` identity and `Party Role` tables, or merged `Product` and `Arrangement` entities.
  - Missing privacy classification tags or unmasked `RESTRICTED_PII` / `REGULATORY_CRITICAL` fields exposed in logs, URL paths, or query parameters.
  - Destructive `UPDATE` or `DELETE` operations on posted financial ledger or transaction tables.
  - Missing BCBS 239 lineage attributes (`source_system_code`, `trace_correlation_id`, `created_at_utc`, `created_by_actor_id`, `schema_version`) or missing `idempotency_key` enforcement on financial mutations.
  - Unversioned breaking changes in SQL DDLs, OpenAPI specs, or analytical data contracts.
- **`WARN`:** Set only when zero `BLOCK` findings exist, and remaining issues are limited to minor non-breaking documentation enhancements or naming refinements.
- **`PASS`:** Set only when zero `BLOCK` and zero `WARN` findings exist across all loaded reference files.
- **`INCOMPLETE_ARTIFACT`:** Set when the input artifact omits required structural context (such as data types, primary keys, or payload schemas) necessary to perform deterministic verification.

## 3. Markdown Remediation Report Structure
Immediately following the JSON block, output a Markdown report containing:
1. **Executive Gate Summary:** Stage evaluated, overall verdict, and reference files loaded.
2. **Canonical FSDM Mapping Table:** Markdown table showing each entity/component mapped to its FSDM Core Concept, BIAN Service Domain, and Privacy Classification.
3. **Remediated Artifact / Code Diff:** Production-ready, fully compliant replacement SQL DDL, OpenAPI/AsyncAPI specification, or source code block with all `BLOCK` and `WARN` findings resolved.