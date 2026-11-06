# ISO 20022: Part 2 - Payments (PAY) Domain for SDLC Agents

**Version:** 2.0 - Technical Edition  
**Domain Code:** `pacs`  
**Primary Messages:** pacs.001-pacs.099

---

## 2.1 Payments Domain Overview

The Payments domain covers domestic and international payment transactions including:
- Credit transfers (wire transfers, ACH)
- Direct debits (recurring payments, collections)
- Payment returns and corrections
- Liquidity and funding management

### Message Categories

| Category | Messages | Use Case |
|----------|----------|----------|
| **Credit Transfer** | pacs.008, pacs.009 | Initiate payment order |
| **Direct Debit** | pacs.003, pacs.004 | Initiate collection or refund |
| **Status/Return** | pacs.025-pacs.029 | Payment status, returns, rejections |
| **Liquidity** | pacs.010-pacs.014 | Liquidity reporting, positioning |
| **Proprietary** | pacs.030+ | Vendor-specific extensions |

---

## 2.2 Credit Transfer Messages

### Message: pacs.008 (Customer Credit Transfer)

**Use:** Customer instructs bank to transfer funds to beneficiary

**Business Rules:**
- BR1: Amount must be > 0 and ≤ party credit limit
- BR2: DebtorAccount balance must be ≥ Amount + Charges
- BR3: ValueDate must be ≥ TransactionDate
- BR4: RemittanceInformation is mandatory for domestic transfers, optional for international
- BR5: BeneficiaryAccountID format varies by country (IBAN in EU, account# elsewhere)
- BR6: For amounts > country threshold, approval required
- BR7: Sanctions check must pass before processing
- BR8: Payment purpose/narrative max 350 chars, no special characters

**Core Field Structure:**

```xml
<CstmrCdtTrfInitn>
  <!-- Group Header -->
  <GrpHdr>
    <MsgId>20261105001</MsgId>
    <CreDtTm>2026-11-05T18:28:06Z</CreDtTm>
    <NbOfTxns>1</NbOfTxns>
    <CtrlSum>1500.50</CtrlSum>
  </GrpHdr>
  
  <!-- Payment Information -->
  <PmtInf>
    <PmtInfId>PAYMENT20261105001</PmtInfId>
    <PmtMtd>TRF</PmtMtd>
    
    <!-- Debtor Details -->
    <Dbtr>
      <Nm>Acme Corp</Nm>
      <Id>
        <BusAcctId>
          <Id>12345678</Id>
        </BusAcctId>
      </Id>
    </Dbtr>
    <DbtrAcct>
      <Id>
        <IBAN>DE89370400440532013000</IBAN>
      </Id>
      <Ccy>EUR</Ccy>
    </DbtrAcct>
    <DbtrAgt>
      <FinInstnId>
        <BIC>DEUTSCHEFF</BIC>
      </FinInstnId>
    </DbtrAgt>
    
    <!-- Credit Transfer Transaction -->
    <CdtTrfTxInf>
      <PmtId>
        <InstrId>INSTR20261105001</InstrId>
        <EndToEndId>E2E20261105001</EndToEndId>
      </PmtId>
      <Amt>
        <InstdAmt Ccy="EUR">1500.50</InstdAmt>
      </Amt>
      <ExctnDt>2026-11-05</ExctnDt>
      
      <!-- Beneficiary Details -->
      <CdtrAgt>
        <FinInstnId>
          <BIC>DEUTDEFF</BIC>
        </FinInstnId>
      </CdtrAgt>
      <Cdtr>
        <Nm>Supplier Inc</Nm>
      </Cdtr>
      <CdtrAcct>
        <Id>
          <IBAN>DE75512108001234567890</IBAN>
        </Id>
      </CdtrAcct>
      
      <!-- Remittance Information -->
      <RmtInf>
        <Ustrd>Invoice INV-2026-0001</Ustrd>
      </RmtInf>
      
      <!-- Purpose Code -->
      <Purp>
        <Cd>PMEN</Cd>
      </Purp>
    </CdtTrfTxInf>
  </PmtInf>
</CstmrCdtTrfInitn>
```

**Field Definitions & Validation:**

| Field | Type | Length | Mandatory | Validation |
|-------|------|--------|-----------|-----------|
| **MsgId** | String | 1-35 | Yes | Unique per day per sender |
| **CreDtTm** | DateTime | - | Yes | Must be UTC (Z suffix) |
| **NbOfTxns** | Integer | 1-15 | Yes | Sum of all payment instructions |
| **CtrlSum** | Decimal | 1-18.2 | Yes | Total amount of all transactions |
| **Amount** | Decimal | 1-18.2 | Yes | > 0, ≤ credit limit |
| **Currency** | Code (3) | 3 | Yes | ISO 4217 code |
| **ValueDate** | Date | - | No | ≥ TransactionDate |
| **IBAN** | String | 1-34 | Conditional | Valid IBAN per ISO 13616 |
| **BIC** | String | 8,11 | Conditional | Valid BIC per ISO 9362 |
| **Narrative** | String | 1-350 | No | Max 5 lines × 70 chars |
| **PurposeCode** | Code | 4 | No | ISO 20022 purpose codes |

**Test Cases - Requirements Agent:**

```
TC-PAY-001: Valid domestic credit transfer
  Inputs: Amount 1500.50 EUR, domestic IBAN, existing narrative
  Expected: Message accepted, CtrlSum calculated correctly
  
TC-PAY-002: International credit transfer without narrative (allowed)
  Inputs: Amount 5000.00 USD, international IBAN, no narrative
  Expected: Message accepted (narrative optional for intl)
  
TC-PAY-003: Amount exceeds limit
  Inputs: Amount 100000.00 EUR, debtor limit 50000.00
  Expected: Message rejected with code AM04
  
TC-PAY-004: Invalid IBAN format
  Inputs: IBAN "DE12345", Amount 1000
  Expected: Schema validation failure, error 400
  
TC-PAY-005: ValueDate before TransactionDate
  Inputs: TxnDate 2026-11-05, ValueDate 2026-11-04
  Expected: Business rule validation failure
```

---

### Message: pacs.009 (Interbank Credit Transfer)

**Use:** Bank-to-bank payment, correspondent banking

**Business Rules:**
- BR1: Replaces pacs.008 for interbank operations
- BR2: MustVerifyCounterpartyBIC before sending
- BR3: InstructedAmount (amount sent to receiving bank) vs InterbankSettledAmount
- BR4: ChargeSplitIndicator (who pays the bank fees)
- BR5: InformationToPayingAgent field for bank-specific instructions (max 140 chars)
- BR6: SenderCorrespondent and ReceiverCorrespondent required for multileg chains

**Key Differences from pacs.008:**
- Bank-to-bank instead of customer-to-bank
- More detailed correspondent chain support
- Additional fee/charge handling
- Intermediary bank details required for multileg payments

**Test Cases - Implementation Agent:**

```
TC-PAY-006: Multileg payment through 3 banks
  Setup: Debtor Bank A -> Correspondent B -> Creditor Bank C
  Expected: ChargeSplit handled correctly at each leg
  
TC-PAY-007: Instructed Amount vs Settled Amount differs
  Inputs: Instructed 1000 USD, charges 10 USD, Settled 990 USD
  Expected: All amounts validated, fees correctly deducted
```

---

## 2.3 Direct Debit Messages

### Message: pacs.003 (Debit Mandate Initiation)

**Use:** Creditor initiates direct debit collection

**Business Rules:**
- BR1: MandateID must be unique per debtor-creditor pair
- BR2: MandateValidation: Mandate must be active and not revoked
- BR3: DebtorAccount cannot be frozen or restricted
- BR4: For SEPA: Max 2.5% of average monthly balance
- BR5: CollectionDate must be working day in debtor's country
- BR6: Debtor has right to refuse (reject) up to 8 weeks after debit

**Core Field Structure (Simplified):**

```xml
<DrctDbtInitn>
  <GrpHdr>
    <MsgId>DD20261105001</MsgId>
    <CreDtTm>2026-11-05T18:28:06Z</CreDtTm>
  </GrpHdr>
  
  <PmtInf>
    <PmtMtd>DD</PmtMtd>
    <Dbtr>
      <Nm>Customer ABC</Nm>
    </Dbtr>
    <DbtrAcct>
      <Id>
        <IBAN>DE89370400440532013000</IBAN>
      </Id>
    </DbtrAcct>
    
    <!-- Mandate -->
    <MndtRltdInf>
      <MndtId>MANDATE-12345</MndtId>
      <MndtSts>ACTV</MndtSts>
      <FrstCollnDt>2026-11-15</FrstCollnDt>
    </MndtRltdInf>
    
    <DrctDbtTxInf>
      <Amt>
        <InstdAmt Ccy="EUR">150.00</InstdAmt>
      </Amt>
      <CollnDt>2026-11-15</CollnDt>
    </DrctDbtTxInf>
  </PmtInf>
</DrctDbtInitn>
```

**Field Validations:**
- MandateStatus ∈ {ACTV, INACTV, PEND, RLVD} (Active, Inactive, Pending, Revoked)
- CollectionDate must be >= today + 5 working days
- Amount must be within limit defined by mandate
- Debtor cannot be flagged for dispute

---

## 2.4 Payment Status & Rejection Messages

### Message: pacs.025 (Rejection Message)

**Use:** Payment rejected at any processing point

**Rejection Reason Codes:**
- `AC01`: Invalid Account Number
- `AC02`: Invalid Debtor Account
- `AC03`: Invalid Creditor Account
- `AC04`: Account Closed
- `AM01`: Insufficient Funds
- `AM02`: Duplicate Transaction
- `AM04`: Amount Exceeds Limit
- `CUST`: Customer Initiated Cancellation
- `FRAD`: Suspected Fraud
- `SGNR`: Invalid/Missing Signature

**Response Structure:**

```xml
<Rjctn>
  <RjctdTxn>
    <OrgnlInstrId>INSTR20261105001</OrgnlInstrId>
    <OrgnlEndToEndId>E2E20261105001</OrgnlEndToEndId>
    <RjctnRsn>
      <Cd>AC01</Cd>
      <TxtRsn>Invalid Account Number Format</TxtRsn>
    </RjctnRsn>
  </RjctdTxn>
</Rjctn>
```

---

## 2.5 Agent Checklists for Payments Domain

### Requirements Analysis Checklist
- [ ] Identify payment type (credit transfer, direct debit, return)
- [ ] Determine domestic vs international requirements
- [ ] List all party identification methods (BIC, IBAN, proprietary IDs)
- [ ] Document approval workflows (manual/automatic)
- [ ] Define charge/fee split responsibility
- [ ] List sanctions check requirements
- [ ] Document audit logging requirements
- [ ] Identify SLA for payment processing

### Implementation Checklist
- [ ] Implement pacs.008 parser and serializer
- [ ] Implement all rejection code handlers
- [ ] Create validation for IBAN/BIC formats
- [ ] Implement CtrlSum calculation and validation
- [ ] Create charge calculation and splitting logic
- [ ] Implement timestamp validation (UTC only)
- [ ] Create error response generation
- [ ] Implement idempotency (duplicate detection)
- [ ] Create audit trail logging

### Testing Checklist
- [ ] Test valid pacs.008 with various currencies
- [ ] Test pacs.008 with missing optional fields
- [ ] Test all rejection codes (AC01-AC04, AM01-AM04, etc.)
- [ ] Test CtrlSum mismatch detection
- [ ] Test IBAN validation for multiple countries
- [ ] Test charge splitting logic
- [ ] Test timestamp validation and timezone handling
- [ ] Test idempotency key processing
- [ ] Performance: Process 1000 payments in < 5 minutes

