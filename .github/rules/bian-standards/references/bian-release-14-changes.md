# BIAN v14.0 Lifecycle and Change Reference

Lookup table for renamed, obsolete, replaced and new artefacts, so older names are not treated as current.

- **Source:** BIAN v14.0.0 Release Notes v1.0 (20 Feb 2026), `RN14` in [bian-source-registry.md](bian-source-registry.md). Section numbers below refer to that document.
- **Evidence label:** Official BIAN for every row unless marked otherwise. Only names and change types are recorded; no document text is reproduced.
- **Scope:** changes **introduced in 14.0** relative to 13.0. Changes made in earlier releases (11, 12, 13) are **not** covered; fetch the corresponding release notes (URLs in the registry) before assessing a design that targets an older release.
- **Cross-check done:** where the OpenAPI files in `bian-official/public` @ `b58bf4c` could be checked, the result is in the "Verified in OAS14" column.

## 1. Service Domains

### 1.1 New in 14.0 (RN14 §4.1)
| Working group | New Service Domains | Note from RN14 |
|---|---|---|
| Incentive Program | Incentive Program Directory; Rewards Menu; Rewards Inventory; Rewards Delivery; Incentive Account; Issued Certificate Directory; Partner Management; Operations Log; Partner Administration | BQs currently undefined; to be defined in a later release. |
| Payment | Payee Management; Customer Consent; Payment Orchestration; Payment Confirmation; Payment Settlement | |
| Card | Corporate Card Service | |
| Insurance | Funeral Policy; Claim Assessment; Claim Administration | BQs defined under the rationalisation approach. |

**Verified in OAS14:** no file named for Payee Management, Customer Consent, Payment Orchestration, Payment Confirmation, Payment Settlement or Corporate Card Service exists in `release14.0.0/semantic-apis/oas3 /yamls/`. The release notes do not say these have APIs; treat their API availability as **Unverified**. Funeral Policy, Claim Assessment, Claim Administration and all Incentive/Rewards/Partner Management/Operations Log SDs have files with `paths: {}` (no operations), consistent with RN14 §11.

### 1.2 Obsolete in 14.0 (RN14 §4.2)
| Obsolete SD | Lifecycle change | Stated replacement ("in next release") | Verified in OAS14 |
|---|---|---|---|
| Payment Execution | Registered → Obsolete | Payment Settlement | no file |
| Payment Instruction | Registered → Obsolete | Payment Order Initiation | no file |
| Payment Order | Registered → Obsolete | Payment Confirmation | no file |
| ACH Operations | Registered → Obsolete | Payment Rail | no file |
| Correspondent Bank Operations | Registered → Obsolete | Payment Rail | no file |
| Direct Debit Collection | Provisional → Obsolete | none stated | no file |
| Direct Debits Service | Provisional → Obsolete | none stated | no file |

Rule of use: a design that cites an obsolete SD is a **Lifecycle** finding. Recommend the stated replacement only as "named by BIAN as replacement in the next release"; the replacement SD may itself be new and without an API (e.g. Payment Settlement, Payment Confirmation).

### 1.3 Renamed (RN14 §4.3) and replaced (§4.5)
| Old name | New name | Verified in OAS14 |
|---|---|---|
| Brokered Product | Brokered Product Proxy | `BrokeredProductProxy.yaml` exists, `paths: {}` |
| Payment Rail Operations | Payment Rail | `PaymentRail.yaml` exists |
| Payment Initiation | Payment Order Initiation | `PaymentOrderInitiation.yaml` exists |
| Credit Card Position Keeping | Card Transaction Tracking | `CardTransactionTracking.yaml` exists, `paths: {}` |
| Product Broker Agreement (replaced) | Partner Agreement | `PartnerAgreement.yaml` exists |

### 1.4 Documentation updated (RN14 §4.4)
Role / executive summary / example of use / key features updated for: Position Keeping, Payment Order Initiation, Payment Rail, Financial Gateway, Card Terminal Operation, Card Terminal Administration, Card Transaction Capture, Card Clearing, Card Financial Settlement, Credit Card, Card Transaction Tracking, Customer Billing, Merchant Acquiring Facility. Re-read the current definition for these before assessing a design.

## 2. Functional Pattern changes (RN14 §5)
| Service Domain | Change |
|---|---|
| Card Network Participant Facility | Fulfill → Agree Term |
| Fiduciary Agreement | Fulfill → Agree Term |
| Consumer Advisory Services | Fulfill → Advise |
| Corporate Tax Advisory | Fulfill → Advise |
| Legal Advisory | Fulfill → Advise |

A pattern change alters the Control Record's generic artifact and BQ type, so BQs of these SDs may differ from older material.

## 3. Behavior Qualifier changes (RN14 §6)

### 3.1 Renamed (SDs affected in parentheses; abbreviated where RN14 lists many)
| Old BQ | New BQ | SDs (RN14 §6.2) |
|---|---|---|
| Account Statement | Financial Status Tracking | Credit Card, Credit Facility, Current Account, Corporate Current Account, Loan, Corporate Loan, Consumer Loan, Merchandising Loan, Mortgage Loan, Savings Account, Term Deposit, Virtual Account |
| Service Fee; Fees | Charge | Merchandising Loan, Merchant Acquiring Facility, Mortgage Loan, Savings Account, Term Deposit, Virtual Account, Cash Concentration, Cash Management And Account Services, Consumer Advisory Services, Consumer Loan, Corporate Current Account, Corporate Loan, Corporate Tax Advisory, Credit Card, Credit Facility, Current Account, Custody Administration, Fiduciary Agreement, Investment Account, Leasing, Legal Advisory, Loan, Card Clearing |
| Withdrawal | Debit and Credit | Merchandising Loan, Mortgage Loan, Corporate Loan, Consumer Loan, Leasing, Loan, Current Account, Corporate Current Account, Savings Account, Investment Account, Term Deposit, Cash Management and Account Services, Virtual Account |
| Booking Authorization | Booking | Consumer Loan, Corporate Current Account, Corporate Loan, Current Account, Internal Bank Account, Merchandising Loan, Mortgage Loan, Savings Account, Term Deposit, Virtual Account |
| Collateral | Collateral Allocation | Leasing, Loan, Merchandising Loan, Mortgage Loan, Corporate Loan |
| Payment Initiation | Payment Batch | Direct Debit |
| Card Transaction | Card Payment | Credit Card |
| Product Association | Credit Allocation | Credit Facility |
| Renewal → (replaced) | Rollover | Term Deposit |
| Syndicate Assembly | Syndicate | Syndicated Loan |
| Dividends and Interest | Dividend | Custody Administration |
| Securities Reporting | Regulatory Submission | Custody Administration |
| Instrument Definition; Specification | Instrument Design | ECM And DCM; Private Placement; Public Offering |
| Legal Advisory Arrangement | Legal | Legal Advisory |
| Market Opportunities | Opportunity | Investment Portfolio Management |
| Tax Optimization | Taxation | Consumer Advisory Services |
| Administer | Administration | Corporate Lease |
| Check | Confirmation | Commissions |
| Bank Guarantee Collections Task | Collection | Bank Guarantee |
| M&A Candidate Selection and Evaluation Topic | Merger and Acquisition | Mergers and Acquisitions Advisory |
| Market Making Security Traded Position Fulfillment | Position Tracking | Market Making |

Additional renames not tabulated: Factoring SD (three "...Fulfillment" BQs → "Factoring Evaluation / Purchase / Processing"); Trust Services SD (five "...Fulfillment" BQs → "Loan Agency and Administration", "Court Liaison", "Financing", "Project Finance", "Escrow"); Corporate Finance SD ("...Topic" BQs → "Tactical Funding", "Strategic Funding", "Capital Structuring"); Public Offering SD ("Public Placement Instrument Registration Fulfillment" → "Item Registration"). See RN14 §6.2 for the complete list.

**Verified in OAS14:** Current Account exposes BQs `DebitandCredit`, `Charge`, `Booking` (and no `Withdrawal`, `ServiceFee`, `BookingAuthorization`); schema `FinancialStatusTracking` is present.

### 3.2 Deleted (RN14 §6.1)
Leasing: "Clearing and Settlement". Notional Pooling: "Notional Account Consolidated Position Fulfillment", "Notional Account Arrangement Fulfillment". Card Network Participant Facility: "Participant Service", "Participant Account". Virtual Account: "Virtual Account Configuration Fulfillment", "Statement". Standing Order: "Standing Order Fulfillment". Trust Services: "Trust Estate, Inheritance and Income Tax Fulfillment", "Trust Tax and Expense Fulfillment". Fiduciary Agreement: "Assessment and Reporting", "Fulfillment". Direct Debit: "Batch Debit", "Verify Mandate", "Funds Available Check", "Payment Tracking".

### 3.3 Replaced (RN14 §6.3) — selected, high-impact entries
| Service Domain | Old BQ → New BQ |
|---|---|
| Market Making | "Market Making Quote Fulfillment" → Quote; "Market Making Buy and Sell Order Fulfillment" → Order |
| Notional Pooling | "Notional Account Interest Allocation Fulfillment" → Cash Transfer |
| Merchant Acquiring Facility | "Participant Service" → Service; "Merchant Account" → Support Facility |
| Virtual Account | "Virtual Account Maintenance Fulfillment" → Maintenance; "Credit Transfer" → Debit and Credit |
| Merchandising Loan / Mortgage Loan / Leasing | "Financial Accounting" → Booking; "Financial Instrument" → Financial Status Tracking |
| Loan | "Restructuring" → Modification |
| Currency Exchange | "FX Transaction Pricing" → Quote |
| Market Order | "Customer Processing" → Quote |
| Consumer Investments | "Funding Check" → Confirmation |
| Investment Portfolio Management | "Track" → Financial Status Tracking; "Trade Initiation" → Trade |
| Product Combination | "Embedded Product Control" → Support Facility |
| Private Placement, Project Finance, Public Offering, Fiduciary Agreement, Syndicated Loan, Corporate Finance, Standing Order | see RN14 §6.3 for the full list |

## 4. Other v14.0 changes relevant to assessments
- **Control Record / metamodel diagrams** (RN14 §7): new core diagrams for Functional Patterns, Generic Artifacts, BQ Types, Service Operation Action Terms; ArchiMate diagrams per BQ type; new CR models for Funeral Policy, Claim Assessment, Claim Administration. *No metamodel diagram was updated or added in 14.0 (§2).*
- **BOM** (RN14 §8): new data-type diagrams (Involvement, Document, Arrangement, Agreement, Instruction, Transaction, Location, Rule Set, Feature, Product, Assessment, Account, Payment, Condition, Card, Cash, Customer, Loan, Securities, Market, Insurance) and BOM diagrams for Funeral Policy, Claim Assessment, Claim Administration, Discount Pricing.
- **Scenarios** (RN14 §9): five new Payment scenarios (names in `bian-concepts.md` §10).
- **Wireframes** (RN14 §10): Bank Incentive Program, Product & Price, Payments Hub, Card Model.
- **Release rationale** (RN14 §1): rationalisation of Service Domain definitions, unnecessary Service Operations eliminated, more ISO 20022 links.
- **Counts v13.0 → v14.0** (RN14 §1): Service Domains 327 → 322; Business Capabilities 586 → 586; Business Objects 1537 → 1585; Service Operations 5139 → 4905; Semantic APIs 249 → 242 (values read from the RN14 Figure 1 data table; its column headers are in the order Service Domains, Business Domains, Business Capabilities, BOM diagrams, CR diagrams, Business Objects, BO attributes, Service Operations, E2E scenarios, Service Connections, Connections with operations, Semantic APIs).
