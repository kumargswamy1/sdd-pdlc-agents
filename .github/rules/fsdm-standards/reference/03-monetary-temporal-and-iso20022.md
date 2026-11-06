# Reference 03: Monetary Precision, Bitemporality & ISO 20022 Contracts

Enforce exact representation of financial quantities, dates, timestamps, and canonical payment structures across databases, APIs, event streams, and application code.

## 1. Monetary Representation & Precision Rules
- **Rule 3.1 (Strict Prohibition of Floating-Point Currency):** Never use binary floating-point types (`FLOAT`, `DOUBLE`, `REAL`, `float32`, `float64`, or unvalidated IEEE 754 JSON `number`) to store, transmit, or calculate monetary amounts, balances, fees, interest rates, or exchange rates. Violation of this rule is an immediate `BLOCK`.
- **Rule 3.2 (Physical Database Column Precision):**
  - Standard Monetary Amounts & Balances: `DECIMAL(19, 4)` or `NUMERIC(19, 4)` (supports up to 15 integral digits and 4 fractional digits for sub-unit accounting precision).
  - High-Precision Asset Prices, Net Asset Value (NAV), or Unit Quantities: `DECIMAL(23, 8)` or `NUMERIC(23, 8)`.
  - Foreign Exchange (FX) Rates & Interest Rates: `DECIMAL(18, 10)` or `NUMERIC(18, 10)`.
- **Rule 3.3 (Mandatory Atomic Currency Pairing):** Every monetary amount attribute in a database table, API payload, or event schema must be paired with an explicit 3-character uppercase **ISO 4217** currency code attribute (`currency_code CHAR(3) NOT NULL`). Never assume an implicit default currency.
- **Rule 3.4 (JSON / API Monetary Structure):** In REST OpenAPI, GraphQL, and AsyncAPI JSON payloads, represent monetary values as a composite object with a string-encoded decimal and an ISO 4217 currency code:
  ```json
  "instructedAmount": {
    "amount": "125000.5000",
    "currency": "USD"
  }
  ```

## 2. Bitemporal Modeling & ISO 8601 Temporal Rules
- **Rule 3.5 (UTC Timestamp Standardization):** Store and transmit all system timestamps in Coordinated Universal Time (UTC) formatted per **ISO 8601** (`YYYY-MM-DDTHH:mm:ss.sssZ`) and persisted using `TIMESTAMP WITH TIME ZONE`.
- **Rule 3.6 (Bitemporal Financial State Columns):** Any table tracking financial arrangement terms, interest rate tiers, credit limits, party roles, risk classifications, or account statuses must separate two temporal dimensions:
  1. **Business / Effective Time** (when the business fact is legally true in the real world):
     - `effective_from_utc TIMESTAMP WITH TIME ZONE NOT NULL` (or `effective_from_date DATE NOT NULL`)
     - `effective_to_utc TIMESTAMP WITH TIME ZONE` (nullable or high-date `9999-12-31` for currently active records)
  2. **System / Transaction Time** (when the row was physically recorded or superseded in the database):
     - `recorded_at_utc TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP`
     - `superseded_at_utc TIMESTAMP WITH TIME ZONE` (null if current version)

## 3. ISO 20022 Canonical Payment & Statement Alignment
- **Rule 3.7 (ISO 20022 Semantic Building Blocks):** Payment initiation, clearing, settlement, and account reporting schemas must align field semantics and naming with **ISO 20022** canonical structures:
  - **Customer Credit Transfer Initiation (`pain.001`):**
    * `GrpHdr` (Group Header: `MsgId`, `CreDtTm`, `NbOfTxs`, `CtrlSum`, `InitgPty`)
    * `PmtInf` (Payment Information: `PmtInfId`, `PmtMtd`, `ReqdExctnDt`)
    * `Dbtr` (Debtor Party), `DbtrAcct` (Debtor Account), `DbtrAgt` (Debtor Agent BIC/Clearing ID)
    * `CdtrAgt` (Creditor Agent BIC/Clearing ID), `Cdtr` (Creditor Party), `CdtrAcct` (Creditor Account)
    * `RmtInf` (Remittance Information: `Ustrd` or structured `Strd` creditor reference)
  - **Financial Institution to Financial Institution Customer Credit Transfer (`pacs.008`):**
    * `PmtId` (`InstrId`, `EndToEndId`, `TxId`, and `UETR` - Unique End-to-End Transaction Reference formatted as UUID v4)
    * `IntrBkSttlmAmt` (Interbank Settlement Amount with `Ccy` attribute)
    * `IntrBkSttlmDt` (Interbank Settlement Date)
    * `ChrgBr` (Charge Bearer: `DEBT`, `CRED`, `SHAR`, `SLEV`)
  - **Bank-to-Customer Account Report / Statement / Notification (`camt.052` / `camt.053` / `camt.054`):**
    * `Stmt` / `Ntfctn` / `Rpt` container
    * `Bal` (Balance: `Tp` code such as `OPBD`, `CLBD`, `ITAV`, `CLAV`; `Amt`; `CdtDbtInd`)
    * `Ntry` (Entry: `NtryRef`, `Amt`, `CdtDbtInd` restricted to `CRDT` or `DBIT`, `Sts` restricted to `BOOK`, `PDNG`, `INFO`, `BookgDt`, `ValDt`, `BkTxCd`)