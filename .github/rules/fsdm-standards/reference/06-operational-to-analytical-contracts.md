# Reference 06: Operational-to-Analytical Data Contracts (ODCS)

Bridge operational application engineering (OLTP microservices) with downstream enterprise risk data aggregation, regulatory reporting, and AI/ML analytical platforms.

## 1. Mandatory Data Contract Definition as Code
- **Rule 6.1 (Version-Controlled Data Contracts):** Every microservice publishing asynchronous domain events or exposing analytical data products must include a machine-readable **Data Contract** (compliant with the Open Data Contract Standard (ODCS), Apache Avro Schema, or JSON Schema Draft 2020-12) checked into version control alongside the application source code.
- **Rule 6.2 (Required Data Contract Metadata):** Every Data Contract must explicitly declare:
  1. **Ownership & Governance:** `domain_name`, `data_product_owner`, `technical_steward_team`, and `source_system_code`.
  2. **Semantic FSDM Mapping:** Mapped FSDM Core Conceptual Area (`InvolvedParty`, `Arrangement`, `Product`, `Event`, `Condition`, `ResourceItem`, `Location`, `Classification`, `BusinessDirection`) and BIAN Service Domain.
  3. **Field-Level Specifications:** Business definition, physical data type, precision/scale, nullability constraint, ISO standard code reference, and mandatory privacy classification tag (`PUBLIC` through `REGULATORY_CRITICAL`).
  4. **Service Level Objectives (SLOs):** Freshness latency target, completeness threshold percentage, availability target, and reconciliation watermark column.

## 2. Schema Evolution & Compatibility Guardrails
- **Rule 6.3 (Transitive Compatibility Enforcement):** All published event schemas and analytical data contracts must enforce `BACKWARD_TRANSITIVE` or `FULL_TRANSITIVE` compatibility in the enterprise schema registry.
- **Rule 6.4 (Breaking Change Prohibition):** The following modifications are strictly prohibited within an existing major schema version (`BLOCK` at CI/CD gate):
  - Deleting or renaming an existing field or column.
  - Changing a field's physical data type or narrowing decimal precision/scale.
  - Changing the semantic definition or currency unit of an existing attribute.
  - Removing an existing enumeration value.
  - Adding a new mandatory (`REQUIRED` / `NOT NULL`) field without providing a deterministic default value.
- **Rule 6.5 (Major Version Migration Protocol):** Any breaking structural change requires publishing a new major schema version (`v2`), maintaining dual-publishing across a documented deprecation window, and verifying downstream consumer migration before retiring `v1`.