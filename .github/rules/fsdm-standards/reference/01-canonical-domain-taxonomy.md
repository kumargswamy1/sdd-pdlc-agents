# Reference 01: Canonical Financial Domain Taxonomy (FSDM & BIAN)

Enforce the 9 Core Conceptual Areas of the Financial Services Data Model (FSDM) and align service boundaries with Banking Industry Architecture Network (BIAN) Service Domains.

## 1. Involved Party (`PARTY`)
- **Definition:** Any natural person (individual), legal entity (corporation or organization), government agency, or internal organizational unit in which the financial institution has a business interest.
- **Rule 1.1 (Party vs. Party Role Decoupling):** Never merge an Involved Party's intrinsic legal identity attributes (legal name, date of birth, date of incorporation, sovereign national or tax identification numbers) with their transient business relationship role (Borrower, Depositor, Guarantor, Merchant, Payee, Counterparty, Employee).
- **Rule 1.2 (Single Canonical Party Identity):** A natural person or legal entity must exist as a single conceptual Party entity linked via one-to-many associative relationships to `PARTY_ROLE` and `ARRANGEMENT_PARTY_ROLE`. Creating separate identity tables for "Customer", "Merchant", and "Guarantor" that duplicate legal identity attributes is a critical (`BLOCK`) violation.

## 2. Arrangement / Agreement (`ARRANGEMENT`)
- **Definition:** A formal, legally binding or operational agreement between two or more Involved Parties establishing terms, conditions, rights, and obligations (such as a Deposit Account Agreement, Credit Facility Agreement, Collateral Agreement, or Payment Mandate).
- **Rule 1.3 (Product vs. Arrangement Separation):** A `PRODUCT` defines the marketable catalog specification and standard institutional terms (for example, "Commercial Revolving Credit Line"). An `ARRANGEMENT` is the specific instantiated contract held by an Involved Party under that Product (for example, "Facility Agreement #883920"). Never store customer-specific balances or contracted rates on a `PRODUCT` entity, and never duplicate static product catalog descriptions across individual `ARRANGEMENT` records.

## 3. Product (`PRODUCT`)
- **Definition:** A bundled set of financial services, features, and standard conditions offered by the institution to the market or used internally.
- **Rule 1.4 (Composable Product Hierarchy):** Model complex products as assemblies of reusable product components linked to standardized `CONDITION` entities rather than monolithic flat tables.

## 4. Event & Transaction (`EVENT`)
- **Definition:** A discrete business or financial occurrence happening at a specific point in time that records an interaction or triggers a state transition in an Arrangement, Party, or Resource Item (such as a Funds Transfer, Interest Accrual, KYC Verification Event, or Address Update Event).
- **Rule 1.5 (Immutable Event vs. Derived State Separation):** Strictly separate immutable Point-in-Time Events (`FINANCIAL_TRANSACTION`, `ARRANGEMENT_LIFECYCLE_EVENT`) from derived Point-in-Time Balances or Snapshots (`ARRANGEMENT_BALANCE`, `ARRANGEMENT_STATUS`). Balances must always be reconcilable from the underlying immutable event stream.

## 5. Condition (`CONDITION`)
- **Definition:** Specific eligibility criteria, pricing tiers, interest rate schedules, fee matrices, credit limits, or regulatory restrictions attached to a Product or Arrangement.
- **Rule 1.6 (Parameterized Rule Modeling):** Model Conditions as structured, effective-dated data entities linked to Products or Arrangements—never as unparsed free-text blobs or hardcoded conditional logic embedded inside application services.

## 6. Resource Item (`RESOURCE_ITEM`)
- **Definition:** Tangible or intangible assets owned, managed, or tracked by the institution or pledged by a Party (such as real estate collateral, payment cards, point-of-sale terminals, hardware security tokens, or financial securities certificates).

## 7. Location (`LOCATION`)
- **Definition:** Physical geographic addresses, digital channels, electronic network endpoints (email, phone, IP address), or branch coordinates.
- **Rule 1.7 (Associative Location Binding):** Decouple `LOCATION` entities from `PARTY` and `ARRANGEMENT` entities via an effective-dated associative table (`PARTY_LOCATION_ADDRESS_ROLE`) declaring the usage purpose (`RESIDENTIAL`, `REGISTERED_OFFICE`, `BILLING`, `TAX_DOMICILE`).

## 8. Classification (`CLASSIFICATION`)
- **Definition:** Standardized hierarchical schemes used to categorize Parties, Arrangements, Products, Events, and Risks (such as industry sector codes, customer segmentation tiers, credit risk grades, and regulatory asset classes).

## 9. Business Direction (`BUSINESS_DIRECTION`)
- **Definition:** Institutional objectives, risk appetite statements, internal governance policies, financial budgets, and regulatory compliance targets that govern operational execution.