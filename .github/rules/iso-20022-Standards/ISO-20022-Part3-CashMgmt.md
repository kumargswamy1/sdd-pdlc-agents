# ISO 20022: Part 3 - Cash Management (CAM) Domain for SDLC Agents

**Version:** 2.0 - Technical Edition  
**Domain Code:** `camt`  
**Primary Messages:** camt.001-camt.099

---

## 3.1 Cash Management Domain Overview

The Cash Management domain covers:
- Account information and statements
- Balance and liquidity reporting
- Intraday position management
- Account queries and responses
- Debit/credit notifications

### Message Categories

| Category | Messages | Primary Use |
|----------|----------|-----------|
| **Notifications** | camt.001, camt.002 | Alert parties of debit/credit events |
| **Statements** | camt.053, camt.054 | Daily/intraday account statements |
| **Account Info** | camt.004 | Opening/closing balance reports |
| **Liquidity** | camt.003, camt.020 | Position and liquidity reporting |
| **Queries** | camt.004, camt.005, camt.006 | Request account information |
| **Proprietary** | camt.030+ | Custom cash management extensions |

---

## 3.2 Bank Statement Message

### Message: camt.053 (Bank to Customer Account Statement)

**Use:** Bank sends daily (or intraday) account statement to customer

**Business Rules:**
- BR1: Statement covers exactly one account for one day
- BR2: Account must exist and be active
- BR3: OpeningBalance + NetDebits/Credits = ClosingBalance
- BR4: Timestamp must be end-of-day in bank timezone
- BR5: All transactions must be time-sequenced (ascending)
- BR6: Partial statements allowed mid-day (marked as "intraday")
- BR7: Daily statement must be final (marked as "final" vs "interim")
- BR8: Reconciliation required: sum(transactions) = ClosingBalance - OpeningBalance

**Core Field Structure:**

```xml
<BkToCstmrStmt>
  <!-- Group Header -->
  <GrpHdr>
    <MsgId>STMT20261105001</MsgId>
    <CreDtTm>2026-11-05T23:59:59Z</CreDtTm>
    <MsgPgntn>
      <PgNb>1</PgNb>
      <LastPgInd>true</LastPgInd>
    </MsgPgntn>
  </GrpHdr>
  
  <!-- Statement -->
  <Stmt>
    <StmtId>20261105-EUR-001</StmtId>
    <CrtnDtTm>2026-11-05T23:59:59Z</CrtnDtTm>
    <FrToDt>
      <FrDt>2026-11-05</FrDt>
      <ToDt>2026-11-05</ToDt>
    </FrToDt>
    
    <!-- Account Identification -->
    <Acct>
      <Id>
        <IBAN>DE89370400440532013000</IBAN>
      </Id>
      <Ccy>EUR</Ccy>
      <AcctSvc>CACC</AcctSvc>
    </Acct>
    
    <!-- Account Owner -->
    <AcctOwner>
      <Nm>Acme Corp</Nm>
      <Id>
        <BusAcctId>
          <Id>COMPANY12345</Id>
        </BusAcctId>
      </Id>
    </AcctOwner>
    
    <!-- Opening Balance -->
    <Bal>
      <Tp>
        <CdOrPrtry>
          <Cd>OPBD</Cd>
        </CdOrPrtry>
      </Tp>
      <Amt Ccy="EUR">10000.00</Amt>
      <CdtDbtInd>CRDT</CdtDbtInd>
      <Dt>2026-11-05</Dt>
    </Bal>
    
    <!-- Transactions -->
    <Ntry>
      <Amt Ccy="EUR">1500.50</Amt>
      <CdtDbtInd>DBTS</CdtDbtInd>
      <Sts>BOOK</Sts>
      <BookgDt>
        <Dt>2026-11-05</Dt>
      </BookgDt>
      <ValDt>
        <Dt>2026-11-05</Dt>
      </ValDt>
      <BkTxCd>
        <Domn>
          <Cd>PMNT</Cd>
          <Fmly>
            <Cd>CCTI</Cd>
            <SubFmly>
              <Cd>PCUT</Cd>
            </SubFmly>
          </Fmly>
        </Domn>
      </BkTxCd>
      <RltdPties>
        <Cdtr>
          <Nm>Supplier Inc</Nm>
        </Cdtr>
      </RltdPties>
      <RmtInf>
        <Ustrd>Invoice INV-2026-0001</Ustrd>
      </RmtInf>
      <AddtlRf>INV-2026-0001</AddtlRf>
    </Ntry>
    
    <!-- Closing Balance -->
    <Bal>
      <Tp>
        <CdOrPrtry>
          <Cd>CLBD</Cd>
        </CdOrPrtry>
      </Tp>
      <Amt Ccy="EUR">8499.50</Amt>
      <CdtDbtInd>CRDT</CdtDbtInd>
      <Dt>2026-11-05</Dt>
    </Bal>
  </Stmt>
</BkToCstmrStmt>
```

**Field Definitions & Validation:**

| Field | Type | Mandatory | Validation |
|-------|------|-----------|-----------|
| **StmtId** | String 1-35 | Yes | Unique per account per day |
| **CrtnDtTm** | DateTime | Yes | UTC, end of business day |
| **IBAN** | String 1-34 | Yes | Valid per ISO 13616 |
| **Currency** | Code (3) | Yes | ISO 4217 |
| **OpeningBalance** | Decimal | Yes | Must match prior day closing |
| **ClosingBalance** | Decimal | Yes | Opening + all debits/credits |
| **TransactionAmount** | Decimal | Yes | > 0 |
| **Sts (Status)** | Code | Yes | BOOK, PEND, etc. |
| **BookingDate** | Date | Yes | <= ValuationDate |
| **TransactionCode** | Code | Conditional | ISO 20022 tx code |
| **Reconciliation** | Arithmetic | Yes | Sum(transactions) = close - open |

**Balance Type Codes:**
- `OPBD` = Opening Balance
- `CLBD` = Closing Balance
- `INTE` = Interim Balance
- `AVLB` = Available Balance

**Transaction Status Codes:**
- `BOOK` = Booked (final)
- `PEND` = Pending (temporary)
- `RSVD` = Reserved
- `POPC` = Processed Overnight

**Test Cases - Requirements Agent:**

```
TC-CAM-001: Valid daily statement
  Inputs: 10 transactions, opening 10000.00, closing 8499.50
  Expected: Statement accepted, reconciliation passes
  
TC-CAM-002: Intraday statement (partial)
  Inputs: 5 transactions as of 12:00 UTC, MarkAsInterim
  Expected: Statement accepted with INTE status
  
TC-CAM-003: Reconciliation mismatch
  Inputs: Opening 10000.00, sum of txns = 1500.50, closing 7999.00
  Expected: Validation error, sum != close - open
  
TC-CAM-004: Transaction out of sequence
  Inputs: Txn1 time 14:30, Txn2 time 10:15
  Expected: Validation error, not time-sorted
  
TC-CAM-005: Multiple account statements in single message
  Inputs: 2 accounts in one document
  Expected: Schema error or split required (1 account per stmt)
```

---

## 3.3 Debit/Credit Notification Message

### Message: camt.001 (Bank Sends Debit/Credit Notification)

**Use:** Real-time notification when transaction hits account

**Business Rules:**
- BR1: Sent immediately after booking (near real-time)
- BR2: Contains single transaction detail
- BR3: Amount and party information included
- BR4: Referenced document (invoice, order) included if available
- BR5: May be sent before statement for intraday visibility
- BR6: Multiple notifications may arrive before statement delivery

**Core Field (Simplified):**

```xml
<CdtNtfctn>
  <Ntry>
    <Amt Ccy="EUR">1500.50</Amt>
    <CdtDbtInd>CRDT</CdtDbtInd>
    <Sts>BOOK</Sts>
    <BookgDt>2026-11-05T14:30:00Z</BookgDt>
    <Cdtr>
      <Nm>Acme Corp</Nm>
    </Cdtr>
    <Dbtr>
      <Nm>Supplier Inc</Nm>
    </Dbtr>
    <RmtInf>
      <Ustrd>Invoice INV-2026-0001</Ustrd>
    </RmtInf>
  </Ntry>
</CdtNtfctn>
```

---

## 3.4 Account Query & Response

### Message: camt.004 (Opening Balance)

**Use:** Request or send opening/closing balance for account

**Business Rules:**
- BR1: Response must include both opening and closing balance
- BR2: Date range must span exactly 1 business day
- BR3: Currency must match account currency
- BR4: Balance must be final (not estimated)
- BR5: Timestamp must be after business close

**Core Fields:**

```xml
<AcctOpngBal>
  <Acct>
    <IBAN>DE89370400440532013000</IBAN>
  </Acct>
  <Bal>
    <Amt Ccy="EUR">10000.00</Amt>
    <Dt>2026-11-05</Dt>
    <CdtDbtInd>CRDT</CdtDbtInd>
  </Bal>
</AcctOpngBal>
```

---

## 3.5 Liquidity & Position Reporting

### Message: camt.020 (Account Holder Requests Cash Activity)

**Use:** Customer requests cash position/liquidity information

**Business Rules:**
- BR1: Request includes date range (typically 1-30 days)
- BR2: Response includes net position for requested period
- BR3: Can filter by transaction type
- BR4: Can request forecast vs actual positions
- BR5: Response timestamp must be "as of" date requested

**Use Case Example:**

```
Requester:  Treasury dept of large corporation
Purpose:    Understand liquidity position across 5 accounts
Request:    "Give me position for all accounts, past 7 days"
Response:   camt.020 with daily net position for each account
Action:     Treasury decides on fund transfers between accounts
```

---

## 3.6 Agent Checklists for Cash Management Domain

### Requirements Analysis Checklist
- [ ] Identify statement frequency (daily, intraday, on-demand)
- [ ] Define reconciliation requirements
- [ ] List all account types to be managed (CACC, SVGS, etc.)
- [ ] Determine notification triggers (amount threshold, tx type)
- [ ] Define balance types needed (opening, closing, available)
- [ ] Specify transaction filtering needs (by type, party, amount)
- [ ] Document archival requirements (retention period)
- [ ] Define intraday reporting requirements

### Implementation Checklist
- [ ] Implement camt.053 parser for statement ingestion
- [ ] Create reconciliation logic (opening + txns = closing)
- [ ] Implement transaction time-sequencing validation
- [ ] Create balance calculation routines
- [ ] Implement camt.001 notification handler
- [ ] Create query/response handlers (camt.004)
- [ ] Implement intraday vs daily logic
- [ ] Create debit/credit indicator handling
- [ ] Implement status code handling (BOOK, PEND, etc.)
- [ ] Create audit trail for all statement operations

### Testing Checklist
- [ ] Test valid daily statement (10 transactions)
- [ ] Test reconciliation pass and fail scenarios
- [ ] Test intraday partial statement handling
- [ ] Test transaction sequencing (out-of-order detection)
- [ ] Test all balance type codes
- [ ] Test all transaction status codes
- [ ] Test multiple currency handling
- [ ] Test large statement (1000+ transactions)
- [ ] Test pagination for large statements
- [ ] Test IBAN validation for multiple countries
- [ ] Test timestamp handling and timezone issues
- [ ] Test multi-day statement errors (must be single day)

