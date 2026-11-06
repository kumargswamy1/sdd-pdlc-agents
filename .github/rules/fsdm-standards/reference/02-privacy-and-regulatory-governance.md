# Reference 02: Data Classification, Privacy & Regulatory Lifecycle Controls

Every data entity, database column, API attribute, and event field must enforce strict data privacy, sovereignty, and lifecycle governance controls.

## 1. Canonical Data Sensitivity Classification Taxonomy
Every schema attribute must carry an explicit metadata classification tag selected from the following six levels:
- `PUBLIC`: Non-sensitive institutional reference data approved for public disclosure (such as public branch coordinates or published product catalog names).
- `INTERNAL`: Low-sensitivity operational metadata (such as internal system identifiers or non-sensitive lookup descriptions).
- `CONFIDENTIAL`: Proprietary commercial, corporate, or financial data (such as institutional pricing terms, aggregated portfolio metrics, or internal credit policies).
- `RESTRICTED_PII`: Direct or indirect Personal Identifiable Information identifying a natural person (such as full legal name, residential address, email address, telephone number, IP address, device identifier, or customer account number).
- `SENSITIVE_PERSONAL_DATA`: High-risk personal attributes subject to heightened statutory protection under data privacy laws (such as biometric templates, health or medical records, criminal history, religious or philosophical beliefs, or minor status).
- `REGULATORY_CRITICAL`: Sovereign national identification numbers, tax identification numbers, passport numbers, payment card Primary Account Numbers (PAN), cryptographic keys, authentication credentials, and central bank regulatory reporting attributes.

## 2. Sovereign Identifier & Credential Protection Rules
- **Rule 2.1 (Zero Cleartext Exposure in Logs & URLs):** Attributes classified as `RESTRICTED_PII`, `SENSITIVE_PERSONAL_DATA`, or `REGULATORY_CRITICAL` must never be written in plaintext to application logs, exception stack traces, telemetry spans, URL path parameters, or URL query strings.
- **Rule 2.2 (Encryption, Tokenization, and Blind Indexing):**
  - Sovereign national IDs, tax IDs, passport numbers, and payment card numbers must use field-level encryption or Format-Preserving Encryption (FPE) / deterministic tokenization in non-production environments and analytical data lakes.
  - Where exact-match database lookup is required on encrypted identifiers, store a dedicated blind-index column computed using `HMAC-SHA256` with an enterprise-managed secret key rotated via a hardware security module (HSM) or key management service (KMS).

## 3. Consent & Data Lifecycle Management Rules
- **Rule 2.3 (Verifiable Consent Linkage):** Any schema or service that processes personal data for marketing, cross-selling, third-party distribution, or external bureau checks must maintain an explicit foreign-key or token reference to `consent_arrangement_id`, recording `purpose_code`, `consent_status` (`GRANTED`, `WITHDRAWN`, `EXPIRED`), `granted_at_utc`, and `withdrawn_at_utc`.
- **Rule 2.4 (Retention & Crypto-Shredding Readiness):** Every persistent table storing `RESTRICTED_PII` or `SENSITIVE_PERSONAL_DATA` must define a `retention_policy_code` and support automated purging, deterministic anonymization, or subject-level crypto-shredding upon expiration of the statutory retention period while preserving anonymized financial ledger totals.