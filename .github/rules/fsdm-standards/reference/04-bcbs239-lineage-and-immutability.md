# Reference 04: BCBS 239 Risk Data Lineage, Auditability & Ledger Immutability

Enforce Basel Committee on Banking Supervision (BCBS 239) principles for risk data accuracy, completeness, adaptability, and auditability across all operational and analytical data stores.

## 1. Mandatory BCBS 239 Lineage & Audit Metadata Envelope
Every persistent database table and asynchronous domain event envelope must include the following standardized lineage fields:
- `record_id` / `event_id`: Globally unique record or event identifier (UUID v4 or time-ordered UUID v7).
- `source_system_code`: Canonical identifier of the originating application or microservice registered in the enterprise architecture catalog (`VARCHAR(64) NOT NULL`).
- `trace_correlation_id`: End-to-end distributed trace correlation identifier propagated across synchronous HTTP calls and asynchronous message brokers (`VARCHAR(64) NOT NULL`).
- `created_at_utc`: Immutable system timestamp of record creation (`TIMESTAMP WITH TIME ZONE NOT NULL`).
- `created_by_actor_id`: Authenticated principal, service account, or batch execution identifier that created the record (`VARCHAR(128) NOT NULL`).
- `schema_version`: Semantic version (`MAJOR.MINOR.PATCH`) of the table or event contract (`VARCHAR(16) NOT NULL`).

## 2. Immutable Financial Ledger & Posting Rules
- **Rule 4.1 (Append-Only Financial Postings):** Posted financial transactions, accounting journal entries, and settlement records are strictly **immutable**. Application code, ORM entities, and database permissions must prohibit `UPDATE` or `DELETE` operations on posted ledger tables. Any code or migration executing destructive updates on posted financial entries is an immediate `BLOCK`.
- **Rule 4.2 (Compensating Reversal Pattern):** Corrections, cancellations, adjustments, or chargebacks to a posted transaction must be executed by inserting a new compensating reversal record (`entry_type = 'REVERSAL'` with inverted `credit_debit_indicator`) containing an explicit foreign key reference (`original_transaction_id`) pointing to the original immutable entry.
- **Rule 4.3 (Double-Entry Accounting Integrity):** Any core accounting or sub-ledger posting service must enforce balanced debit (`DBIT`) and credit (`CRDT`) legs within an atomic database transaction boundary (or a deterministic saga with compensating ledger entries) where the sum of debits strictly equals the sum of credits per ISO 4217 currency code.

## 3. Idempotency & Reconciliation Readiness
- **Rule 4.4 (Mandatory Idempotency Key Enforcement):** Every state-mutating financial API endpoint and asynchronous event consumer must require, persist, and enforce a unique constraint on `idempotency_key` (or `UETR` / `EndToEndId`) to guarantee exactly-once financial posting semantics during network retries or broker redeliveries.
- **Rule 4.5 (Deterministic Reconciliation Watermarks):** Transactional tables must expose monotonic sequence numbers, booking dates (`booking_date`), and batch control totals to support automated real-time and end-of-day (EOD) reconciliation between operational microservices, general ledgers, and regulatory risk data warehouses.