# ISO 20022 Standards - Master Reference Index for SDLC Agents

**Version:** 2.0 - Deep Technical Edition  
**Last Updated:** November 5, 2026  
**Audience:** Requirements Analysis Agents, Implementation Agents, Testing Agents

---

## Quick Navigation

This comprehensive guide is organized into 5 specialized documents:

| Document | Purpose | Agents | Content |
|----------|---------|--------|---------|
| **Part 1: Architecture** | Message structure, validation framework, versioning | All | Core concepts, data types, error codes, message envelope |
| **Part 2: Payments** | Credit transfers, direct debits, returns | Requirements, Implementation, Testing | pacs.* messages, business rules, test cases |
| **Part 3: Cash Management** | Statements, balance reporting, notifications | Requirements, Implementation, Testing | camt.* messages, reconciliation logic |
| **Part 4: Securities** | Trade settlement, confirmations, corporate actions | Requirements, Implementation, Testing | sese.* messages, settlement rules |
| **Part 5: Testing Guide** | Comprehensive testing strategies and examples | Testing | Unit tests, business logic tests, E2E tests |

---

## 1. Document Overview & How to Use

### For Requirements Analysis Agents

**Use these documents to:**
1. Understand what ISO 20022 domain applies to business requirement
2. Map requirements to specific message types (pacs.008, camt.053, etc.)
3. Extract detailed business rules and validation requirements
4. Define acceptance criteria and test scenarios
5. Document regulatory and compliance needs

**Start with:**
- Part 1, Section 1.1-1.3: Message structure and patterns
- Domain-specific part (2/3/4): Business rules for your domain
- Section: Agent Checklists (each part) → Requirements Analysis subsection

**Deliverables:**
- Requirements specification with ISO 20022 message mappings
- List of all business rules and validations
- Test case definitions
- Acceptance criteria with error codes

### For Implementation Agents

**Use these documents to:**
1. Understand detailed field structure and validation
2. Generate code templates for message parsing/generation
3. Implement business logic and validation rules
4. Build error handling and recovery mechanisms
5. Create data models and database schemas

**Start with:**
- Part 1, Section 1.1: XML Message Envelope and Header
- Part 1, Section 1.2: Data Types and Formats
- Part 1, Section 1.4: Validation Framework
- Domain-specific part: Core Field Structure and Field Definitions

**Deliverables:**
- Message parsers/serializers for each message type
- Field validation implementations
- Business logic calculation code
- Error response generation
- Audit trail logging

### For Testing Agents

**Use these documents to:**
1. Generate comprehensive test cases
2. Create test data sets with edge cases
3. Validate business logic implementation
4. Test error handling and rejection codes
5. Verify end-to-end workflows

**Start with:**
- Part 5: Comprehensive Testing Guide
- Each domain part: Test Cases section
- Part 5, Section 5.2-5.6: Test templates and factories

**Deliverables:**
- Unit test suite (field validation, parsing)
- Business logic test suite (rules, calculations)
- Integration test suite (end-to-end workflows)
- Test data factory and generators
- Regression test suite

---

## 2. Key Concepts Reference

### Message Naming: `[DOMAIN].[TYPE].[CATEGORY].[VERSION]`

**Examples:**
- `pacs.008.03.08` = Payments.CreditTransfer.CustomerTransfer.V03.08
- `camt.053.02.09` = CashManagement.Statement.BankToCustomer.V02.09
- `sese.021.02.10` = Securities.Settlement.DeliveryInstruction.V02.10

**Domain Codes:**
- `pacs` = Payments (credit transfers, direct debits)
- `camt` = Cash Management (statements, balances)
- `sese` = Securities Settlement (trades, orders)
- `fxtr` = FX Trading (foreign exchange)
- `cres` = Credit Management (loans, facilities)
- `trad` = Trade Services (letters of credit)
- `admi` = Administrative (system messages)

### Critical Fields in Every Message

Every ISO 20022 message has a Business Application Header with:

```
MsgId (Message ID)          → Unique per sender per day
CreDtTm (Creation DateTime) → UTC timestamp (YYYY-MM-DDTHH:mm:ssZ)
BizMsgIdr (Message Defn)    → Format: pacs.008.03.08
MsgDefIdr                   → Correlates request to response
Fr/To (From/To)             → Sender/receiver BIC or ID
```

### Validation Levels (Part 1, Section 1.4)

1. **Level 1: Structural** - XML schema, data types, length
2. **Level 2: Business Rules** - Field interdependencies, code sets
3. **Level 3: Compliance** - Sanctions, thresholds, audit requirements
4. **Level 4: Integration** - SLA, party agreements, network availability

### Common Error Codes

**Payment Errors (pacs.*):**
- `AC01` = Invalid Account Number
- `AC02` = Invalid Debtor Account
- `AC03` = Invalid Creditor Account
- `AC04` = Account Closed
- `AM01` = Insufficient Funds
- `AM02` = Duplicate Transaction
- `AM04` = Amount Exceeds Limit
- `FRAD` = Suspected Fraud
- `SGNR` = Invalid/Missing Signature

**Generic Errors:**
- `CUST` = Customer-Initiated Rejection
- `RJCT` = Rejected (unspecified reason)
- `NOOR` = No Outstanding Requests
- `AGRD` = Agreement Discrepancy

---

## 3. Workflow Integration Guide

### Typical Payment Workflow (pacs messages)

```
Party A                    Payment System               Party B
  │                             │                         │
  ├─── pacs.008 (payment) ────>│                         │
  │       (credit transfer)     │                         │
  │                      ┌─────┴──────────┐              │
  │                      │ Validate       │              │
  │                      │ Reconcile      │              │
  │                      │ Check funds    │              │
  │                      └─────┬──────────┘              │
  │                             │                         │
  │                  ┌──────────┴──────────┐             │
  │                  │ Accept or Reject?   │             │
  │                  └──────────┬──────────┘             │
  │                             │                         │
  │<─── camt.001 (notify) ──────│                         │
  │       (debit notification)  │                         │
  │                             │                         │
  │                             ├─────────────────────>│
  │                             │ Settlement (pacs.009)  │
  │                             │                        ├─>
  │                             │                        │
  │                    ┌────────┴────────┐              │
  │                    │ camt.053 (stmt) │              │
  │                    │ (daily summary) │              │
  │                    └────────┬────────┘              │
  │                             │                         │
  │<─── camt.053 (statement)────│                         │
  │                             │                         │
```

### Typical Settlement Workflow (sese messages)

```
Buyer                          Settlement Agent               Seller
  │                                   │                          │
  ├─── sese.008 (trade conf) ───────>│                          │
  │                                   │                          │
  │                                   ├─── sese.008 ────────────>│
  │                                   │                          │
  │<──── sese.008 (matched) ──────────│<──── sese.008 (matched) ──
  │                                   │                          │
  ├─── sese.021 (settlement) ────────>│                          │
  │       (DVP instruction)           │                          │
  │                                   │                          │
  │                            ┌──────┴──────┐                   │
  │                            │ Matching    │                   │
  │                            │ Securities  │                   │
  │                            │ Cash        │                   │
  │                            └──────┬──────┘                   │
  │                                   │                          │
  │<─── pacs.008 (cash) ──────────────│                          │
  │       (buyer pays cash)           │                          │
  │                                   │                          │
  │<─── sese.021 (execution) ────────>│─── sese.021 ────────────>│
  │       (settlement complete)       │ (securities transferred)  │
  │                                   │                          │
```

---

## 4. Implementation Patterns

### Pattern 1: Request-Response

**Used by:** Account queries, balance requests, reconciliation queries
**Example:** camt.004 (Request opening balance) → camt.004 (Response)
**Key Fields:** RelatdRef (correlation ID) ties request to response

### Pattern 2: One-Way Notification

**Used by:** Statement delivery, notifications, broadcast
**Example:** camt.053 (Daily statement sent to all account holders)
**Key Fields:** Account ID, period dates, no response required

### Pattern 3: Multi-Step Workflow

**Used by:** Settlement, trade lifecycle
**Example:** Trade → Confirm → Settle → Payment → Completion
**Key Fields:** Transaction ID flows through all related messages

### Pattern 4: Exception Handling

**Used by:** Rejections, corrections, cancellations
**Example:** pacs.008 → [validation fail] → pacs.025 (rejection)
**Key Fields:** Original transaction ID, reason code, error narrative

---

## 5. Data Dictionary - Common Fields

### Party Identification

| Format | Example | Usage | Validation |
|--------|---------|-------|-----------|
| **BIC** | DEUTDEFF | Bank ID | ISO 9362, 8 or 11 chars |
| **IBAN** | DE89370400440532013000 | Account ID | ISO 13616, country-specific length |
| **Proprietary ID** | ACME123456 | Custom ID | Max 35 chars, alphanumeric |

### Amount & Currency

| Format | Example | Usage | Validation |
|--------|---------|-------|-----------|
| **Amount** | 1500.50 | Transaction amount | Decimal 1-18 digits, 2 decimals |
| **Currency Code** | EUR, USD | ISO standard | ISO 4217, 3 uppercase letters |
| **Exchange Rate** | 1.2545 | FX translation | Decimal 1-11 digits, 4-6 decimals |

### Dates & Times (All UTC)

| Format | Example | Usage | Validation |
|--------|---------|-------|-----------|
| **Date** | 2026-11-05 | Business date | YYYY-MM-DD |
| **DateTime** | 2026-11-05T18:28:06Z | Exact timestamp | YYYY-MM-DDTHH:mm:ssZ |
| **Settlement Date** | 2026-11-07 | T+0, T+1, T+2, or T+3 | >= 2 business days from trade |

### Identifiers & Codes

| Format | Example | Usage | Validation |
|--------|---------|-------|-----------|
| **ISIN** | US0378331005 | Security ID | ISO 6166, exactly 12 chars |
| **MIC** | XETRA | Market ID | ISO 10383, 4 chars |
| **Reason Code** | AC01 | Error code | ISO 20022 standard, 4 chars |

---

## 6. Quick Reference by Agent Role

### Requirements Analysis Agent Checklist

**Phase 1: Business Requirement Analysis**
- [ ] Identify financial domain (payment, settlement, reporting)
- [ ] Identify business process (single transaction, batch, workflow)
- [ ] Identify parties involved (bank, customer, counterparty, third-party)
- [ ] List all data inputs and outputs needed
- [ ] Document SLAs (timeliness, accuracy, availability)
- [ ] List regulatory requirements (audit, sanctions, compliance)

**Phase 2: ISO 20022 Mapping**
- [ ] Select applicable domain (pacs, camt, sese, etc.)
- [ ] Select specific message types (e.g., pacs.008, camt.053)
- [ ] Map each business requirement to message field
- [ ] Document all business rules and validation requirements
- [ ] Extract all error scenarios and rejection codes
- [ ] Verify coverage (no unmapped requirements)

**Phase 3: Specification Handoff**
- [ ] Create traceability matrix (requirement → message → field)
- [ ] Generate test case templates (from Part 5)
- [ ] Document acceptance criteria with error codes
- [ ] Create implementation checklist (from domain part)

### Implementation Agent Checklist

**Phase 1: Design**
- [ ] Select XML parser library (xmltodict, lxml, etc.)
- [ ] Design data model (classes for each message type)
- [ ] Design validation layer (4-level validation)
- [ ] Design error handling (exception hierarchy)
- [ ] Design audit logging (field-level logging)

**Phase 2: Core Development**
- [ ] Implement message envelope and header handling
- [ ] Implement field validation (all data types)
- [ ] Implement business rule validation
- [ ] Implement error response generation
- [ ] Implement message parsing (XML → Object)
- [ ] Implement message generation (Object → XML)

**Phase 3: Integration**
- [ ] Integrate with message queue (if async)
- [ ] Integrate with database (persistence layer)
- [ ] Integrate with external systems (bank API, settlement)
- [ ] Implement idempotency (duplicate detection)
- [ ] Implement retry logic (exponential backoff)

**Phase 4: Verification**
- [ ] Run implementation checklist from domain part
- [ ] Verify all error codes return correct response
- [ ] Verify audit logging captures all fields
- [ ] Verify backward compatibility (prior versions)
- [ ] Performance test (throughput, latency, memory)

### Testing Agent Checklist

**Phase 1: Test Planning**
- [ ] Extract all test cases from requirements doc
- [ ] Extract all test cases from domain parts (2-4)
- [ ] Design test data factory (Part 5, Section 5.6)
- [ ] Plan test environment setup
- [ ] Plan test execution timeline

**Phase 2: Unit Testing**
- [ ] Create test suite for field validation (Part 5, Section 5.2)
- [ ] Create test suite for data type validation
- [ ] Create test suite for message parsing
- [ ] Achieve 100% code coverage of validation layer
- [ ] Document any found defects

**Phase 3: Business Logic Testing**
- [ ] Create test suite for each business rule (Part 5, Section 5.3)
- [ ] Create test suite for reconciliation (camt.053)
- [ ] Create test suite for settlement matching (sese.021)
- [ ] Create test suite for all error codes
- [ ] Test boundary conditions and edge cases

**Phase 4: Integration Testing**
- [ ] Create end-to-end workflow tests (Part 5, Section 5.5)
- [ ] Test request-response patterns (query → response)
- [ ] Test notification patterns (statement delivery)
- [ ] Test error recovery and retry logic
- [ ] Test concurrent message processing

**Phase 5: Regression & Performance**
- [ ] Run entire test suite against new version
- [ ] Test backward compatibility (prior versions)
- [ ] Performance test (throughput, latency, memory)
- [ ] Stress test (high volume, long duration)
- [ ] Generate test report with coverage metrics

---

## 7. Common Implementation Patterns (Code Templates)

### Message Parsing Template (Python)

```python
import xml.etree.ElementTree as ET

class Pacs008Parser:
    def parse(self, xml_string):
        root = ET.fromstring(xml_string)
        message = {
            'msg_id': root.find('.//{urn:iso:std:iso:20022:tech:xsd:pacs.008}MsgId').text,
            'created_at': root.find('.//{urn:iso:std:iso:20022:tech:xsd:pacs.008}CreDtTm').text,
            'amount': root.find('.//{urn:iso:std:iso:20022:tech:xsd:pacs.008}InstdAmt').text,
            'currency': root.find('.//{urn:iso:std:iso:20022:tech:xsd:pacs.008}InstdAmt').get('Ccy'),
        }
        return message

class Pacs008Validator:
    def validate(self, message):
        errors = []
        
        # Level 1: Structural
        if not message.get('msg_id'):
            errors.append({'code': 'STRUCT-001', 'msg': 'MsgId is mandatory'})
        
        # Level 2: Business Rules
        amount = float(message.get('amount', 0))
        if amount <= 0:
            errors.append({'code': 'BR-001', 'msg': 'Amount must be > 0'})
        if amount > 9999999999999.99:
            errors.append({'code': 'BR-002', 'msg': 'Amount exceeds maximum'})
        
        # Level 3: Compliance (add sanctions check, etc.)
        
        return {'valid': len(errors) == 0, 'errors': errors}
```

### Message Generation Template

```python
class Pacs008Generator:
    def generate_from_dict(self, data):
        root = ET.Element('Document', xmlns='urn:iso:std:iso:20022:tech:xsd:pacs.008.03.08')
        
        msg_element = ET.SubElement(root, 'CstmrCdtTrfInitn')
        grp_hdr = ET.SubElement(msg_element, 'GrpHdr')
        
        ET.SubElement(grp_hdr, 'MsgId').text = data['msg_id']
        ET.SubElement(grp_hdr, 'CreDtTm').text = data['created_at']
        
        return ET.tostring(root, encoding='unicode')
```

---

## 8. Version Support & Migration

**Current Active Versions:**
- pacs.008.03.08 (Payments Credit Transfer V3.8) - STABLE
- camt.053.02.09 (Statement V2.9) - STABLE
- sese.021.02.10 (Settlement V2.10) - STABLE

**Version Support Timeline:**
- **V3.x**: Supported until 2028-11
- **V2.x**: Supported until 2025-11
- **V1.x**: Deprecated (no support)

**Migration Strategy:**
- Support current + 1 prior version during transition
- Provide mapping layer for message conversion
- Plan 12-month deprecation notice before dropping version

---

## 9. Regulatory & Compliance

### Data Protection Requirements
- **PII Handling:** Never log customer PII (names, account numbers)
- **Message Signing:** Digital signatures for non-repudiation on high-value txns
- **Encryption:** TLS 1.3+ for all transport, AES-256 for at-rest

### Audit & Compliance
- **Audit Trail:** Log all message fields, user actions, validation results
- **Retention:** Keep logs for 7 years minimum (per financial regulations)
- **Access Control:** Role-based access to message data
- **Sanctions Screening:** Check all parties against OFAC/EU lists

---

## 10. Support & Escalation

### When to Use Which Document

| Question | Document |
|----------|----------|
| "What does this error code mean?" | Part 1, Section 1.5 |
| "What fields are required for pacs.008?" | Part 2, Section 2.2 |
| "How do I test the reconciliation logic?" | Part 5, Section 5.3 |
| "What's the XML structure for camt.053?" | Part 3, Section 3.2 |
| "How do settlement workflows work?" | Part 4, Sections 4.2-4.3 |

### Document Maintenance
- Updated quarterly with new error codes and clarifications
- Version tracked in Git with change history
- Feedback welcomed via GitHub issues with label `[iso20022]`

---

**EOF**

