# ISO 20022: Part 1 - Architecture & Framework for SDLC Agents

**Version:** 2.0 - Technical Edition  
**Target Audience:** Requirements Analysis, Implementation, Testing Agents

---

## 1.1 Message Structure & Components

### XML Message Envelope
Every ISO 20022 message has a standardized envelope with header and body:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:[Domain].[MessageType]"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <[MessageType]>
    <!-- Message group -->
    <!-- Business application header (optional) -->
    <BizAppHdr>
      <Fr><!-- Sender --></Fr>
      <To><!-- Recipient --></To>
      <BizMsgIdr><!-- Unique Message ID --></BizMsgIdr>
      <MsgDefIdr><!-- Message Definition Identifier --></MsgDefIdr>
      <BizProcPrtry><!-- Business Process --></BizProcPrtry>
      <CreDtTm><!-- Creation DateTime UTC --></CreDtTm>
      <RelatdRef><!-- Related Reference --></RelatdRef>
      <Sgntr><!-- Signature for non-repudiation --></Sgntr>
    </BizAppHdr>
    <!-- Message group: domain-specific content -->
    <[MessageGroup]>
      <!-- Domain-specific elements -->
    </[MessageGroup]>
  </[MessageType]>
</Document>
```

### Message Header Mandatory Fields (Business Application Header)

| Field | Format | Description | Validation |
|-------|--------|-------------|-----------|
| **Fr** (From) | Max 35 chars | Sender identification (BIC or proprietary ID) | Must match sending party |
| **To** (To) | Max 35 chars | Recipient identification | Must be valid endpoint |
| **BizMsgIdr** | Max 35 chars | Unique message identifier per sender | Must be unique per sender per day |
| **MsgDefIdr** | Format: `[Domain].[Type].[SubType].[Version]` | Message definition ID (e.g., `pacs.008.03.08`) | Must match message namespace |
| **CreDtTm** | ISO 8601 UTC | Message creation timestamp | Must be in UTC format (YYYY-MM-DDTHH:mm:ssZ) |
| **Sgntr** | XML Signature | Digital signature for non-repudiation | Optional but recommended for high-value transactions |
| **RelatdRef** | Max 35 chars | Reference to related previous message | For request-response correlation |

### Message Naming Convention

```
[DOMAIN].[TYPE].[CATEGORY].[VERSION]

Examples:
pacs.008.03.08     = Payments.CreditTransfer.CustomerTransfer.V03.08
sese.021.02.10     = Securities.Settlement.DeliveryInstruction.V02.10
camt.053.02.09     = CashManagement.Statement.BankToCustomer.V02.09
```

**Domain Codes:**
- `pacs` = Payments
- `sese` = Securities Settlement
- `fxtr` = FX Trading
- `cres` = Credit Management
- `camt` = Cash Management
- `trad` = Trade Services
- `admi` = Administrative

---

## 1.2 Data Type Framework

### Core Data Types Used Across All Domains

#### 1. Identifiers (Codes & References)

| Type | Format | Example | Rules |
|------|--------|---------|-------|
| **BIC** | ISO 9362 | DEUTDEFF | 8 or 11 characters, alphanumeric |
| **IBAN** | ISO 13616 | DE89370400440532013000 | Up to 34 chars, alphanumeric |
| **ISIN** | ISO 6166 | US0378331005 | Exactly 12 chars, alphanumeric |
| **MIC** | ISO 10383 | XETRA | Market Identifier Code, 4 chars |
| **Currency Code** | ISO 4217 | USD, EUR, GBP | Exactly 3 uppercase letters |
| **Country Code** | ISO 3166-1 | US, DE, GB | Exactly 2 uppercase letters |
| **Proprietary ID** | Max 35 chars | ACME123456 | Free-form identifier, sender-defined |

#### 2. Amount & Quantity

| Type | Format | Example | Validation |
|------|--------|---------|-----------|
| **Amount** | Decimal 1-18 digits, 2 decimals | 1500.50 | Positive, max 16 integer digits |
| **Rate** | Decimal 1-11 digits, 4-6 decimals | 1.2545 | Exchange rates, interest rates |
| **Percentage** | Decimal 1-5 digits, 2-4 decimals | 12.50 | Commission, fees, rates |
| **Quantity** | Integer | 100 | Security quantities, contract units |

#### 3. Dates & Times (All UTC)

| Type | Format | Example | Rules |
|------|--------|---------|-------|
| **Date** | ISO 8601 | 2026-11-05 | YYYY-MM-DD |
| **DateTime** | ISO 8601 UTC | 2026-11-05T18:28:06Z | YYYY-MM-DDTHH:mm:ssZ |
| **Time** | ISO 8601 | 18:28:06 | HH:mm:ss in UTC |

#### 4. Text & Names

| Type | Max Length | Usage | Character Set |
|------|-----------|-------|----------------|
| **Name** | 70 chars | Party names, beneficiary names | ASCII + special characters |
| **Address** | 70 chars × 5 lines | Full address, max 5 lines | ASCII + special characters |
| **Narrative/Description** | 350 chars × 10 lines | Remittance info, purpose | ASCII + special characters |
| **Reason Code** | 4 chars | Rejection reason, status | Standardized codes per domain |

---

## 1.3 Common Message Flows & Patterns

### Pattern 1: Request-Response (Synchronous)

```
Party A (Initiator)          Party B (Responder)
    |                             |
    |--- [REQUEST MESSAGE] ------>|
    |                             |
    |                         [Process]
    |<--- [CONFIRMATION MSG] ------|
    |<--- [REJECTION MSG] ---------|
```

**Example: Account Query & Response**
- Request: `camt.004` (Demand Deposit Account Opening Request)
- Response: `camt.001` (Debit/Credit Notification with account details)

### Pattern 2: One-Way Notification (Asynchronous)

```
Party A (Sender)             Party B (Receiver)
    |                             |
    |--- [NOTIFICATION] --------->|
    |                             |
    |                         [Process]
```

**Example: Statement Delivery**
- Notification: `camt.053` (Bank Statement) sent daily to customer

### Pattern 3: Multi-Step Workflow

```
Party A          Settlement Agent          Party B
  |                    |                      |
  |-- pacs.008 ------->|                      |
  |  (Payment Order)   |                      |
  |                    |-- pacs.009 -------->|
  |                    | (Inter-bank Trans)  |
  |                    |                     |
  |                    |-- camt.050 -------->|
  |                    | (Liquidity Status)  |
  |                    |                     |
  |<-- camt.049 ------|                      |
  | (Position Info)                          |
```

### Pattern 4: Exception Handling & Rejections

```
Initiator          Processing Point          Responder
    |                    |                        |
    |--- [ORDER] ------->|                        |
    |                    | [VALIDATION FAIL]      |
    |<-- [REJECTION] ----|                        |
    |                    |                        |
    |--- [CORRECTED] --->|                        |
    |                    |-- [SUCCESS] ---------->|
```

**Rejection Response Codes (camt.029/030):**
- `NOOR` = No Outstanding Requests
- `RJCT` = Rejected
- `ACPT` = Accepted
- `ACTC` = Accepted Technical Compliance

---

## 1.4 Validation Framework

### Validation Levels

#### Level 1: Structural Validation
- XML schema compliance
- Required field presence
- Data type conformance
- Length constraints

#### Level 2: Business Rule Validation
- Field interdependencies (e.g., if Amount > 10000, then RequireApproval = true)
- Code set validation (currency code must be ISO 4217)
- Logical consistency (FromDate < ToDate)
- Completeness rules (all mandatory fields for transaction type present)

#### Level 3: Regulatory & Compliance Validation
- Sanctions screening (party names against OFAC list)
- Threshold limits (transaction amount within limits)
- Audit trail requirements (all fields logged)
- Non-repudiation (digital signatures where required)

#### Level 4: Integration Validation
- Interparty agreement compliance
- SLA validation (message within agreed timeframe)
- Format version compatibility
- Party endpoint availability

### Common Validation Rules by Field Type

#### Currency/Amount Fields
```
Rule: Amount must be positive (> 0)
Rule: Amount ≤ 9,999,999,999,999.99
Rule: Currency code must be ISO 4217
Rule: If SWIFT GPI transfer, amount > 0 and ≤ party credit limit
```

#### Party Identification (Sender/Receiver)
```
Rule: BIC must be ISO 9362 compliant (8 or 11 chars)
Rule: If using proprietary ID, must be pre-registered with counterparty
Rule: Receiver must be active endpoint in network
Rule: Sender must have authentication credentials
```

#### Dates & Times
```
Rule: All timestamps must be UTC (Z suffix)
Rule: CreationTime must be ≤ CurrentTime
Rule: ValueDate ≥ TransactionDate
Rule: MessageDate must be within past 90 days (for compliance)
```

#### Narrative/Reference Fields
```
Rule: Max 350 characters for remittance information
Rule: Only ASCII characters allowed (or UTF-8 if agreed)
Rule: StructuredReference format must match regex: ^[A-Z0-9]{1,35}$
Rule: UnstructuredNarrative max 5 lines × 70 chars
```

---

## 1.5 Error Codes & Exception Handling

### Standard HTTP/Transport Level Errors

| Code | Message | Remediation |
|------|---------|-------------|
| **400** | Bad Request | Validate XML schema, correct field format, retry |
| **401** | Unauthorized | Verify credentials, re-authenticate, retry |
| **403** | Forbidden | Check party permissions, contact administrator |
| **404** | Not Found | Verify endpoint URL, check party registration |
| **429** | Rate Limited | Implement exponential backoff, retry after delay |
| **500** | Server Error | Implement retry logic, contact support if persistent |
| **503** | Service Unavailable | Implement circuit breaker, use fallback endpoint |

### ISO 20022 Business-Level Error Codes

#### Rejection Reason Codes (Generic)

| Code | Reason | Field Issue | Recovery |
|------|--------|------------|----------|
| **CUST** | Customer Specific Reason | Document in audit log | Investigate with customer |
| **FRAD** | Suspected Fraud | All critical fields | Contact sender immediately |
| **NOOR** | No Outstanding Requests | Reference field | Verify prior message was sent |
| **RJCT** | Rejected | Unspecified | Check validation error details |
| **UPAY** | Unmatched Payment | Reference number | Investigate transaction history |
| **SCOR** | Scoring Related | Risk assessment | Review compliance rules |
| **AGRD** | Agreement Discrepancy | Contract terms | Verify counterparty agreement |

#### Payment-Specific Rejection Codes (pacs messages)

| Code | Reason | Common Cause | Fix |
|------|--------|-------------|-----|
| **AC01** | Invalid Account Number | Malformed IBAN | Verify IBAN format (ISO 13616) |
| **AC02** | Invalid Debtor Account | Account doesn't exist | Check account holder details |
| **AC03** | Invalid Creditor Account | Beneficiary IBAN wrong | Obtain correct IBAN from beneficiary |
| **AC04** | Account Closed | Account no longer active | Use alternative account or verify status |
| **AM01** | Insufficient Funds | Balance < transfer amount | Check available balance |
| **AM02** | Duplicate Transaction | Exact duplicate within timeframe | Check if already processed |
| **AM04** | Amount Exceeds Limit | Exceeds transaction limit | Split into multiple transfers or request limit increase |
| **AVLF** | Available Funds Unavailable | Funds not yet cleared | Schedule for later date |
| **CUST** | Customer Initiated Cancellation | Sender requested stop | Confirm cancellation with sender |
| **FF01** | Invalid File Format | Message structure error | Correct XML schema violations |
| **RLTI** | Return Liquidity Time Issue | Insufficient time for processing | Retry during business hours |
| **SGNR** | Invalid/Missing Signature | Non-repudiation failure | Re-sign message with correct certificate |

---

## 1.6 Message Versioning & Compatibility

### Version Numbering Scheme

```
Format: V[Major].[Minor]
Examples:
- V03.08 = Version 3, Release 8 (current stable)
- V02.10 = Version 2, Release 10 (legacy)
```

**Version Mapping:**
- Major version bump: Significant structural changes, breaking changes
- Minor version bump: Field additions, optional enhancements, clarifications

### Backward Compatibility Strategy

| Scenario | Rule | Implementation |
|----------|------|-----------------|
| **Adding Optional Field** | Compatible | Old systems ignore; new systems populate |
| **Removing Field** | Breaking | Requires major version bump |
| **Changing Field Type** | Breaking | Requires major version bump |
| **Renaming Field** | Breaking | Requires major version bump |
| **Changing Cardinality** | Breaking/Compatible | Depends on change direction |

### Version Support Timeline

```
Release    Introduced    Stable    Deprecated    End of Life
V03.08     2024-11       2025-02   2027-11       2028-11 (3-year support)
V02.10     2021-11       2022-02   2024-11       2025-11 (3-year support)
V01.09     2018-08       2019-02   2021-08       2022-08 (DEPRECATED)
```

**Agent Implementation Rule:**
- Support current version (V03.08) + one prior (V02.10)
- Provide deprecation warnings for older versions
- Maintain mapping/translation layer for 12 months after deprecation

---

## 1.7 Agent Implementation Checklist - Architecture

### Requirements Analysis Agent
- [ ] Identify relevant ISO 20022 domain (PAY, SEC, CAM, etc.)
- [ ] Map business process to message patterns (request-response, one-way, workflow)
- [ ] Document all mandatory and optional fields needed
- [ ] List all validation rules applicable to use case
- [ ] Identify error scenarios and rejection codes needed
- [ ] Document version compatibility requirements (which versions must be supported?)
- [ ] Define party identification scheme (BIC, proprietary ID, IBAN)
- [ ] Map security requirements to signature/encryption needs

### Implementation Agent
- [ ] Generate XML namespace declarations for selected message version
- [ ] Create data model with all field definitions (type, length, format)
- [ ] Implement Level 1-3 validation logic per Section 1.4
- [ ] Generate error handling code for all relevant error codes
- [ ] Create message parsing and serialization functions
- [ ] Implement backward compatibility layer for multiple versions
- [ ] Generate code templates for BizAppHdr (envelope)
- [ ] Set up audit logging for all message fields

### Testing Agent
- [ ] Create test cases for valid message structures
- [ ] Create test cases for invalid/malformed XML
- [ ] Generate test data for all field types (identifiers, amounts, dates)
- [ ] Test all Level 1 validation rules
- [ ] Test all Level 2 business rule validations
- [ ] Test error response generation for each error code
- [ ] Test version compatibility and version mismatch scenarios
- [ ] Create performance tests for large message batches
- [ ] Verify audit trail logging completeness

