# Example: API Alignment Review (Organisation API vs BIAN Semantic API)

> **Status of this example:** *Illustrative.* The organisation API (`ACME Payments API v2`) is **fictional**. The BIAN side is **verified** against the official `PaymentOrderInitiation.yaml` (BIAN v14.0.0, `info.version: 14.0.0`) in `bian-official/public` @ commit `b58bf4c2c300dd018afc084e9bb24b7adaaa3500`, folder `release14.0.0/semantic-apis/oas3 /yamls/`, checked 2026-11-05. Nothing below is an official BIAN assessment, certification or score.
>
> **Pinned BIAN file:** `https://raw.githubusercontent.com/bian-official/public/b58bf4c2c300dd018afc084e9bb24b7adaaa3500/release14.0.0/semantic-apis/oas3%20/yamls/PaymentOrderInitiation.yaml`

## 1. Business purpose and target Service Domain
`ACME Payments API v2` lets channels create a customer payment instruction, update it, read its status, and read funds/compliance results. The BIAN spec's `info.description` for **Payment Order Initiation** says it "provides a customer payment service. It captures the payer and payee details and other key properties of the payment and initiates the orchestration of the transaction. It provides support for repeating/scheduled payments." → the Service Domain fits the stated purpose.

Alternatives considered: **Payment Rail** (operational interface to payment service providers; not customer instruction capture), **Current Account** (account facility), obsolete **Payment Instruction** (Obsolete in 14.0, RN14 §4.2). Functional Pattern and Business Domain are `Unverified` (Portal not accessible).

## 2. BIAN reference (verified)
| Item | Value |
|---|---|
| Control Record tag | `CR - PaymentOrderInitiationTransaction` |
| BQ tags | `BQ - Compliance`, `BQ - Confirmation`, `BQ - OrderInitiation` |
| Operations (7) | `POST /PaymentOrderInitiation/Initiate` (InCR) · `PUT /PaymentOrderInitiation/{paymentorderinitiationid}/Update` (UpCR) · `GET /PaymentOrderInitiation/{paymentorderinitiationid}/Retrieve` (ReCR) · `GET …/Compliance/{complianceid}/Retrieve` (ReBQ) · `GET …/Confirmation/{confirmationid}/Retrieve` (ReBQ, summary mentions "funds available") · `PUT …/OrderInitiation/{orderinitiationid}/Exchange` (EcBQ, "Verify or accept the payment transaction (results in a payment order)") · `GET …/OrderInitiation/{orderinitiationid}/Retrieve` (ReBQ) |
| Responses per operation | 200, 400, 401, 403, 404, 429, 500; error body `HTTPError{status_code, status, message}` |
| Notable CR payload attributes | `PaymentTransaction`, `PayerReference`, `PayerBankReference`, `PayeeReference`, `PayeeBankReference`, `Amount` (`AmountValue` string/format `Value`, `AmountCurrency` → `Currencycode`), `Currency`, `DateType`/`Date`, `PaymentFeesCharges`, `PaymentMechanism`, `PaymentPurpose`, `PaymentTransactionType`, `RecurringPayment*` |
| Not specified by the file | Security schemes; header parameters (only path parameters appear); PATCH/DELETE (none in any v14.0.0 file) |

## 3. Organisation API (supplied, fictional)
| Method + path | Request/response summary |
|---|---|
| `POST /v2/payments` | body: `{ "amount": 120.50, "ccy": "THB", "from": "...", "to": "...", "reference": "...", "execDate": "2026-12-01" }` → `201` with `{ "id", "state" }` |
| `PATCH /v2/payments/{id}` | update amount / date |
| `GET /v2/payments/{id}` | returns status; **also marks the payment as "viewed"** |
| `GET /v2/payments/{id}/funds-check` | returns `{ "ok": true }` |
| `POST /v2/payments/{id}/cancel` | cancels the payment |
| `DELETE /v2/payments/{id}` | removes a payment record |
| Errors | `{ "code": "E1042", "message": "..." }` for 4xx/5xx |
| Versioning | URL `/v2/`; no BIAN release recorded |
| Status values | `NEW`, `CHECKED`, `SENT`, `FAILED` |

## 4. Operation comparison

| # | Org operation | Closest BIAN operation | Class | Differences / notes | Evidence |
|---|---|---|---|---|---|
| 1 | `POST /v2/payments` | `POST /PaymentOrderInitiation/Initiate` | **Partially aligned** | Same intent (create instruction) and method. Different path structure; payload differences in §5; success code `201` vs BIAN `200`. | OAS14 |
| 2 | `PATCH /v2/payments/{id}` | `PUT /PaymentOrderInitiation/{id}/Update` | **Partially aligned** | Intent matches (UpCR); method differs (PATCH vs PUT). BIAN files contain no PATCH. Whether PATCH is acceptable is an org/architecture decision. | OAS14 (observed: 0 PATCH in 258 files) |
| 3 | `GET /v2/payments/{id}` | `GET …/{id}/Retrieve` | **Semantic mismatch** | Retrieve must be read-only (GUIDE §3.2.5); the org call has a side effect ("viewed"). | GUIDE §3.2.5 |
| 4 | `GET /v2/payments/{id}/funds-check` | `GET …/Confirmation/{confirmationid}/Retrieve` | **Partially aligned** | Fits BQ `Confirmation` ("funds available"). Org returns a boolean; BIAN returns `Confirmation` → `PaymentTransactionFundingCheckResult` (`FundingCheck`). Only the file's schema shows the full structure; compare field by field. BIAN addresses the BQ by an instance id. | OAS14 |
| 5 | (none) | `GET …/Compliance/{complianceid}/Retrieve` | **Missing (if in scope)** | No compliance-check read. Required only if the scope includes compliance results (BSE-SEM-07: default operations are not mandatory). | OAS14 |
| 6 | (none) | `PUT …/OrderInitiation/{orderinitiationid}/Exchange` and `GET …/OrderInitiation/{orderinitiationid}/Retrieve` | **Missing (if in scope)** | No explicit "accept/verify and create the payment order" step; the org flow moves state implicitly (`CHECKED → SENT`). | OAS14 |
| 7 | `POST /v2/payments/{id}/cancel` | none found | **Additional (organisation extension)** | No cancel/Control operation exists in this SD's file; `Control` is not among its 7 operations. Do not assume a BIAN equivalent. Cancellation semantics may sit in another SD or be an extension: `Unverified`. | OAS14 (7 ops listed) |
| 8 | `DELETE /v2/payments/{id}` | none | **Additional / risk** | BIAN files define no DELETE. Deleting financial records raises audit concerns (repo rules). | OAS14; repo rules |

Counts (transparent denominators): BIAN operations in this SD = 7. Organisation operations = 6. Of the 7 BIAN operations: 3 have a counterpart (Initiate, Update, Retrieve → 1 partial, 1 partial, 1 semantic mismatch), 1 partially (Confirmation Retrieve), 3 missing-if-in-scope (Compliance Retrieve, OrderInitiation Exchange, OrderInitiation Retrieve). Organisation-only operations: 2 (cancel, delete). **No overall % score is given** (see `references/bian-validation-framework.md` §7 if requested).

## 5. Payload comparison

| Org field | BIAN attribute (OAS14) | Result | Note |
|---|---|---|---|
| `amount` (number 120.50) | `Amount.AmountValue` (type string, format `Value`) | **Different type** | BIAN carries value as a string; org uses a JSON number. Repo rules also require non-floating representation (REPO-ARCH). |
| `ccy` | `Amount.AmountCurrency` → `Currencycode.Currencycode` (ISO 4217 per description) | **Renamed / restructured** | Org flattens; BIAN nests a `Currencycode` object. |
| `from` / `to` | `PayerReference` / `PayeeReference` (objects `Payer`, `Payee`), plus `PayerBankReference` / `PayeeBankReference`, `PayerProductInstanceReference` / `PayeeProductInstanceReference` | **Different structure** | Org has no bank reference; bank references missing. |
| `reference` | `PaymentTransaction.PaymentTransactionIdentification` (object `Paymentidentification`) | **Probable match** | Needs field-level check in the spec (`Unverified` until the schema `Paymentidentification` is compared). |
| `execDate` | `DateType` + `Date` / `PaymentTransaction.PaymentTransactionDatetime` (`Paymentdatetime`: `PaymentDate` + `PaymentDateType`) | **Partially aligned** | BIAN types the date; `PaymentDateType` enumerates e.g. `RequestedExecutionDate`, `ValueDate`, `DueDate`. Org `execDate` presumably = `RequestedExecutionDate` (assumption, confirm). |
| (none) | `PaymentTransactionType` (`Paymenttypevalues`: e.g. `Domesticpayment`, `Crossborderpayment`) | **BIAN-only** | Org cannot distinguish domestic/cross-border. |
| (none) | `PaymentPurpose` (`Paymentpurposevalues`, e.g. `Salarypayment`) | **BIAN-only** | |
| (none) | `PaymentFeesCharges`, `PaymentMechanism`, `RecurringPayment*` | **BIAN-only** | Recurring/scheduled support is part of the SD description. |
| `state`: `NEW/CHECKED/SENT/FAILED` | `PaymentTransactionStatus` → `Paymenttransactionstatustypevalues` (e.g. `Received`, `Pending`, `Accepted`, `Rejected`, `Acceptedtechnicalvalidation`, `Acceptedsettlementinprocess`, `Acceptedsettlementcompleted`, …) | **Different enum** | Map org values to BIAN values explicitly; do not rename silently. A mapping table is required (BSE-DAT-03). |

## 6. Naming, errors and versioning

| Aspect | BIAN (OAS14) | Organisation | Result |
|---|---|---|---|
| Resource names | `PaymentOrderInitiation`, BQ `Compliance`/`Confirmation`/`OrderInitiation` (PascalCase, action term last) | `payments`, `funds-check`, `cancel` | **Non-standard resource names** (deviation or adapter decision; see BSE-API-09 for the org-rule conflict) |
| Identifiers | `paymentorderinitiationid` etc. (path params) | `{id}` | Mapping needed (BSE-DAT-06) |
| Error body | `HTTPError{status_code,status,message}` | `{code,message}` | **Partially aligned**: no `status_code`/`status`; org code is richer. Org rules also require a correlation id (not in BIAN file). |
| Status codes | 200/400/401/403/404/429/500 | 201 and others | **Partial**: 201 is a legitimate REST choice; record as deviation. |
| Version | `info.version: 14.0.0` | `/v2/`, BIAN release not recorded | **Gap**: record BIAN release, spec version and local version in the contract (BSE-API-07). |
| Security/headers | not defined | not supplied | **Not Verifiable** |

## 7. Findings register

| Finding ID | Area | Element | Expected | Actual | Status | Severity | Gap | Recommendation |
|---|---|---|---|---|---|---|---|---|
| F-API-101 | API | `GET /v2/payments/{id}` | Retrieve is read-only | Marks payment as viewed | Non-Compliant | High | Side effect in a read | Remove the side effect or move it to an explicit update operation |
| F-API-102 | Data | `amount` type | `AmountValue` string + `AmountCurrency` object | JSON number + `ccy` | Partially Compliant | Medium | Type and structure | Adopt string/decimal-safe representation and currency object, or document an adapter |
| F-API-103 | Data | status enum | `Paymenttransactionstatustypevalues` | `NEW/CHECKED/SENT/FAILED` | Partially Compliant | Medium | Value sets differ | Publish mapping table; extend rather than redefine |
| F-API-104 | API | missing `OrderInitiation` and `Compliance` reads | Operations in OAS14 | Absent | Not Verifiable | Low | Need depends on scope | Confirm scope; BIAN default sets are not mandatory (BSE-SEM-07) |
| F-API-105 | API | `DELETE`, `cancel` | none in OAS14 | Present | Partially Compliant | Medium | Organisation extensions; DELETE risks audit trail | Label as extensions; replace DELETE by a status transition |
| F-API-106 | API | versioning | BIAN release traceable | Not recorded | Non-Compliant | Low | No traceability | Add BIAN release and spec version to the contract |
| F-API-107 | API | claim "BIAN-aligned" because path is `/payments` | Evidence-based alignment (BSE-API-08) | No evidence | Non-Compliant | High | Unsupported claim | Remove claim until mapped |

## 8. Recommendations (prioritised)
1. Fix the read side-effect (F-API-101).
2. Decide the BIAN-alignment strategy: **adapter** exposing org resources while mapping to BIAN operations (preserves repo guidance on REST paths) versus **BIAN-style paths** (follows the file literally). Record the decision in an ADR.
3. Align payload types and add the missing BIAN attributes needed by scope (bank references, payment type, purpose, dates typed).
4. Publish enum mapping and error-envelope mapping tables.
5. Record release and versions in the contract.

## 9. Sources and BIAN version
BIAN v14.0 · `OAS14` `PaymentOrderInitiation.yaml` @ `b58bf4c` · GUIDE V8.1 §3.2.5 · RN14 §4.2–4.3 · `references/bian-source-registry.md`.
