# Example: Service Domain Architecture Validation

> **Status of this example:** *Illustrative.* The "design under review" (components `ACME-*`) is **fictional** and contains no real data. It is written as if a user supplied it, so it is treated as **actual design evidence**, never as a BIAN definition. The BIAN-side expectations (SD names, CR/BQ tags, operations, lifecycle changes) are verified against `RN14` and the official v14.0.0 OpenAPI files (`OAS14`, commit `b58bf4c2c300dd018afc084e9bb24b7adaaa3500`, checked 2026-11-05). Functional Pattern and Business Area/Domain are `Unverified` (Portal not accessible).
>
> **Scope:** payments and current-account servicing slice · **BIAN release:** v14.0 · **Rating profile:** Default · **Disclaimer:** internal architecture review, not a BIAN certification.

## 1. Design under review (supplied, fictional)

| Component | Stated responsibilities (from the supplied design document) |
|---|---|
| `ACME-Payments` | Receives payment requests from channels; validates payer/payee; checks funds by reading the ledger; sends to the clearing connector; stores payment status; keeps its own copy of account balances for speed. |
| `ACME-CoreAccounts` | Opens and maintains current accounts; posts debits/credits; calculates interest; stores the transaction log; exposes `GET /accounts/{id}?action=block` which also blocks the account. |
| `ACME-Auth` | Authenticates customers (password, biometrics) and issues tokens. |
| `ACME-Clearing` | Formats and sends outbound payments to external schemes; receives inbound payments. |
| `ACME-Risk` | Fraud scoring (rules and ML models). |
| `ACME-Legacy-PI` | Cites the BIAN "**Payment Instruction**" Service Domain as its mapping. |
| (nothing) | Customer notification on payment status is mentioned as a requirement but no component is named. |

## 2. Responsibility → Service Domain mapping

| Component responsibility | Candidate Service Domain (v14.0) | Basis | Status |
|---|---|---|---|
| Authenticate (password, biometrics, token) | Party Authentication (`CR - PartyAuthenticationAssessment`; BQs `Password`, `Biometric`, …) | OAS14 | ALIGNED |
| Capture payment, payer/payee, status | Payment Order Initiation (`CR - PaymentOrderInitiationTransaction`) | OAS14 | ALIGNED (see F-ARC-001) |
| Fund check inside Payments | Payment Order Initiation BQ `Confirmation` **or** Current Account BQ `AmountBlock` | OAS14 | Overlap (F-ARC-001) |
| Own copy of balances | Current Account / Position Keeping data (no single owner proven) | Derived | Overlap (F-DAT-001) |
| Open/maintain account; debit/credit; interest | Current Account (`CR - CurrentAccountFacility`; BQs `DebitandCredit`, `Interest`, …) | OAS14 | ALIGNED |
| Transaction log | Position Keeping (`CR - FinancialPositionLog`) or Current Account BQ | Derived | Partial: log is inside CoreAccounts |
| Outbound/inbound scheme formatting | Payment Rail (`CR - PaymentRailOperatingSession`; BQs `OutboundTransaction`, `InboundTransaction`) | OAS14 | ALIGNED |
| Fraud scoring | Fraud Evaluation (`CR - FraudEvaluationAssessment`; BQs `RuleSetsandDecisionTrees`, `Models`) | OAS14 | ALIGNED (note: model *design/maintenance* is a different SD, Fraud Model) |
| Customer notification | none named | – | Gap (F-ARC-003) |
| "Payment Instruction" citation | Payment Instruction (**Obsolete in 14.0**) | RN14 §4.2 | Lifecycle finding (F-LIF-001) |

## 3. Positive findings

| ID | Observation | Evidence | Status |
|---|---|---|---|
| P-001 | Authentication is isolated from payment capture, matching the separate Party Authentication responsibility. | Design: `ACME-Auth` vs `ACME-Payments`; OAS14 `PartyAuthentication.yaml` (CR `PartyAuthenticationAssessment`) | Compliant for this boundary (responsibility separation only; not an API-conformance claim) |
| P-002 | Scheme connectivity sits in its own component, consistent with Payment Rail's role as the operational interface to payment service providers. | OAS14 `PaymentRail.yaml` (CR `PaymentRailOperatingSession`, BQs `OutboundTransaction`/`InboundTransaction`) | Compliant for this boundary |
| P-003 | Fraud scoring is separate from payment capture. | OAS14 `FraudEvaluation.yaml` | Compliant for this boundary |

## 4. Findings register

| Finding ID | Area | Element | Expected Standard | Actual Design | Status | Severity | Evidence | Gap | Recommendation |
|---|---|---|---|---|---|---|---|---|---|
| F-LIF-001 | Lifecycle | `ACME-Legacy-PI` mapped to "Payment Instruction" | Payment Instruction is **Obsolete** in 14.0; replaced by Payment Order Initiation "in next release" (Official, RN14 §4.2). Payment Initiation was also renamed Payment Order Initiation (RN14 §4.3). | Design cites "Payment Instruction". | Non-Compliant | High | RN14 §4.2–4.3; `PaymentOrderInitiation.yaml` exists in OAS14, no `PaymentInstruction.yaml` | Obsolete SD named as the mapping target. | Re-map to Payment Order Initiation (current name), keep "Payment Instruction" as a legacy alias in the glossary, record the release. *(Architecture recommendation)* |
| F-ARC-001 | Architecture | Funds check in `ACME-Payments` and balance copy | One Control Record per SD; each information item should have one governing SD (BSE-STR-04, Derived). Payment Order Initiation has BQ `Confirmation` (funds check, per OAS14 summary "funds available"); Current Account holds the account facility and `AmountBlock`. | Payments reads the ledger and keeps its own balances; CoreAccounts also owns balances. | Partially Compliant | High | Design §1; OAS14 `PaymentOrderInitiation.yaml` (`Confirmation/Retrieve`), `CurrentAccount.yaml` (`AmountBlock`) | Two components decide/hold funds availability; ownership unclear. | Decide the owner of funds availability. If Current Account owns balances, Payments should request confirmation rather than keep a copy; if a cached copy is needed, label it a non-authoritative projection. *(Architecture recommendation)* |
| F-API-001 | API | `GET /accounts/{id}?action=block` | Retrieve operations are read-only and do not change state (Official, GUIDE §3.2.5; BSE-SEM-05). In OAS14, retrieval is `GET …/Retrieve` and state changes use PUT/POST operations (e.g. `POST …/AmountBlock/Initiate`). | A GET also blocks the account. | Non-Compliant | Critical | Design §1; GUIDE §3.2.5; OAS14 `CurrentAccount.yaml` `AmountBlock/Initiate` (POST) | Side-effect behind a read operation; breaks read-only semantics (and HTTP safety). | Split into a read (`Retrieve`) and a state-changing operation aligned to the BQ `AmountBlock` (`Initiate` / `Update`). *(Architecture recommendation)* |
| F-ARC-002 | Architecture | Transaction log and interest inside `ACME-CoreAccounts` | Position Keeping maintains a log of monetary transactions posted to product facilities (OAS14 description); Current Account exposes BQs `DebitandCredit`, `Interest`, … but no separate log CR. | Log stored inside CoreAccounts with no stated boundary. | Not Verifiable | Medium | Design §1; OAS14 descriptions only | Cannot decide from the sources whether a separate log component is expected; BIAN does not prescribe deployment (GUIDE §3.5, BSE-ARC-06). | Document whether the log is a logical Position Keeping responsibility inside the same deployment unit. Mapping, not splitting, is the requirement. |
| F-ARC-003 | Architecture | Customer notification | A stated requirement without an owner. Candidate SDs not identified: needs Portal lookup. | No component named. | Not Verifiable | Medium | Design §1 | Missing responsibility owner; the correct SD is **not determined here** (do not guess from names). | Run Service Domain identification (Workflow 2) in the Portal; assign an owner. |
| F-ARC-004 | Architecture | `ACME-Risk` combines scoring with ML model lifecycle | Fraud Evaluation applies tests; a separate SD ("Fraud Model") handles design and maintenance of fraud models (OAS14 description of `FraudModel`). | One component does both. | Partially Compliant | Low | Design §1; OAS14 `FraudModel.yaml`, `FraudEvaluation.yaml` | Two behaviours in one component; may be legitimate in one deployment unit. | Map the two responsibilities explicitly even if deployed together. |
| F-API-002 | API | Status codes | OAS14 operations declare 200/400/401/403/404/429/500 with `HTTPError{status_code,status,message}`. | Not supplied. | Not Verifiable | Informational | – | No API spec provided for comparison. | Supply OpenAPI to run Workflow 4. |
| F-IMP-001 | Implementation | Claim of "BIAN-compliant" in the design cover page | Compliance must be evidenced per element (BSE-API-08, BSE-IMP-04). | Statement without evidence. | Non-Compliant | High | Design §0 (cover page) | Unsupported claim. | Replace with a mapping table and per-area status; remove certification wording. |

## 5. Summary

| Status \ Severity | Critical | High | Medium | Low | Info |
|---|---|---|---|---|---|
| Compliant (boundary-level) | – | – | – | – | 3 positives |
| Partially Compliant | – | 1 | – | 1 | – |
| Non-Compliant | 1 | 2 | – | – | – |
| Not Verifiable | – | – | 2 | – | 1 |
| Not Applicable | – | – | – | – | – |

No numerical score is given: the supplied design has too few scored items and 3 of 11 are not verifiable; see `references/bian-validation-framework.md` §7 for the method if one is requested.

## 6. Recommended next steps (prioritised)
1. **Critical:** remove the side-effect from `GET` (F-API-001).
2. **High:** replace Payment Instruction with Payment Order Initiation (F-LIF-001); decide funds-availability ownership (F-ARC-001); remove unevidenced compliance claim (F-IMP-001).
3. **Medium:** resolve notification owner using the Portal (F-ARC-003); document log boundary (F-ARC-002).
4. **Low:** map fraud scoring vs model management explicitly (F-ARC-004).

## 7. Limitations
Functional Pattern, Business Area/Domain, full CR/BQ definitions and first-order connections were not available (Portal registration); SD role statements are the one-sentence descriptions in the OAS14 `info.description`. The design is fictional, so business correctness needs domain-owner review.

## 8. Sources and BIAN version
BIAN v14.0 · `RN14` §4.2–4.3 · `OAS14` @ `b58bf4c` (`PaymentOrderInitiation`, `CurrentAccount`, `PartyAuthentication`, `PaymentRail`, `FraudEvaluation`, `FraudModel`, `PositionKeeping`) · GUIDE V8.1 §3.2.5 · `references/bian-source-registry.md`.
