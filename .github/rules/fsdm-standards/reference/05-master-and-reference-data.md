# Reference 05: Master Data Management (MDM) & Reference Data Standards

Prevent fragmented data silos, unjoinable domain projections, and hardcoded business enumerations across distributed microservices.

## 1. Golden-Source Enterprise Key Binding
- **Rule 5.1 (Mandatory Enterprise Master Identifiers):** Microservices that store or process domain projections of Parties, Products, Arrangements, Organizational Units, or General Ledger Accounts must store and index the authoritative **Enterprise Master Identifier** issued by the golden-source system of record:
  - `enterprise_party_id` (links to Enterprise Party / Customer MDM)
  - `enterprise_product_code` (links to Enterprise Product Catalog)
  - `enterprise_arrangement_id` (links to Enterprise Agreement Registry)
  - `organization_unit_code` / `cost_center_code` (links to Enterprise Hierarchy)
  - `gl_account_code` (links to Enterprise Chart of Accounts)
- **Rule 5.2 (Zero-Loss Cross-Domain Joinability):** Local service surrogate primary keys are permitted for internal relational indexing, but every outbound REST response, published domain event, and analytical snapshot must include the canonical Enterprise Master Identifier so downstream risk and regulatory systems can aggregate exposures without lossy entity resolution.

## 2. Reference Data Externalization & International Code Sets
- **Rule 5.3 (Prohibition of Hardcoded Business Reference Data):** Never hardcode volatile business reference enumerations (such as industry sector classifications, occupation codes, regulatory asset classes, branch codes, fee waiver reason codes, or KYC risk tiers) as static constants in application source code or unversioned database `CHECK` constraints. Reference values must be resolved from versioned reference tables or configuration services.
- **Rule 5.4 (Mandatory International Standard Code Sets):** Enforce standardized international code formats across all schemas:
  - **Countries & Subdivisions:** **ISO 3166-1 alpha-2** (`CHAR(2)`) or **ISO 3166-1 alpha-3** (`CHAR(3)`), and **ISO 3166-2** for administrative subdivisions.
  - **Currencies:** **ISO 4217** alphabetic code (`CHAR(3)`).
  - **Financial Institution Identifiers:** **ISO 9362** Business Identifier Code (`BIC`, ` VARCHAR(11)`) and **ISO 17442** Legal Entity Identifier (`LEI`, `CHAR(20)`).
  - **Securities Identification:** **ISO 6166** International Securities Identification Number (`ISIN`, `CHAR(12)`) and **ISO 10962** Classification of Financial Instruments (`CFI`, `CHAR(6)`).
  - **Merchant Category Codes:** **ISO 18245** Retail Financial Services Merchant Category Code (`MCC`, `CHAR(4)`).
  - **Language Codes:** **ISO 639-1** (`CHAR(2)`) or **IETF BCP 47** locale tags.