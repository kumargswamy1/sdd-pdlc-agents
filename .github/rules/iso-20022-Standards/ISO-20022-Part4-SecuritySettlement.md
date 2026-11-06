# ISO 20022: Part 4 - Securities Settlement (SEC) Domain for SDLC Agents

**Version:** 2.0 - Technical Edition  
**Domain Code:** `sese`  
**Primary Messages:** sese.001-sese.099

---

## 4.1 Securities Settlement Domain Overview

The Securities Settlement domain covers:
- Trade orders and confirmations
- Settlement instruction matching
- Corporate action processing
- Portfolio management and reconciliation
- Collateral management

### Message Categories

| Category | Messages | Use Case |
|----------|----------|----------|
| **Trade Orders** | sese.001-007 | Place/amend/cancel security orders |
| **Confirmations** | sese.008-020 | Trade confirmation and matching |
| **Settlement** | sese.021-038 | Settlement instruction and matching |
| **Corporate Actions** | sese.039-050 | Dividends, splits, redemptions |
| **Portfolio/Positions** | sese.051-075 | Holdings, valuations, reconciliation |
| **Collateral** | sese.076-089 | Collateral allocation and margining |
| **Account** | sese.090-105 | Account management and statements |

---

## 4.2 Settlement Instructions Message

### Message: sese.021 (Settlement Instruction)

**Use:** Instruct settlement of security transaction (Delivery vs Payment)

**Business Rules:**
- BR1: Must reference matched trade confirmation (from sese.008+)
- BR2: Securities identified by ISIN (International Security ID) or CUSIP
- BR3: Settlement must be DVP (Delivery vs Payment) - atomic exchange
- BR4: SettlementDate must be T+0, T+1, T+2, or T+3 (trading standard)
- BR5: Quantity must match trade confirmation exactly
- BR6: Cash amount must match price × quantity from trade
- BR7: Depository instructions required (where to move securities)
- BR8: Cash settlement bank details required

**Core Field Structure:**

```xml
<SctiesSttlmInstr>
  <!-- Group Header -->
  <GrpHdr>
    <MsgId>SETTLE20261105001</MsgId>
    <CreDtTm>2026-11-05T09:00:00Z</CreDtTm>
  </GrpHdr>
  
  <!-- Settlement Instruction -->
  <SttlmInstr>
    <SttlmInstrId>INSTR-SETTLE-001</SttlmInstrId>
    <RefTrnsSd>
      <Ref>TRADE-CONF-001</Ref>
    </RefTrnsSd>
    
    <!-- Security Details -->
    <Fin2PartySctiesSttlmInstr>
      <SctiesSttlmInstrBase>
        <SttlmDt>2026-11-07</SttlmDt>
        
        <!-- Security Identification -->
        <Isin>US0378331005</Isin>
        <Qty>
          <Qty>1000</Qty>
        </Qty>
        
        <!-- Delivering Party (Seller) -->
        <Dvry>
          <DvryPty>
            <Id>
              <BIC>TRADERDEFF</BIC>
            </Id>
          </DvryPty>
          <DvryAcct>
            <Id>SELLER-ACC-001</Id>
          </DvryAcct>
          <!-- Depository Details -->
          <SctyDpst>
            <Id>
              <BIC>DEPODEFF</BIC>
            </Id>
          </SctyDpst>
        </Dvry>
        
        <!-- Cash Details (Buyer pays) -->
        <Amt>
          <InstdAmt Ccy="USD">95000.00</InstdAmt>
        </Amt>
        
        <!-- Receiving Party (Buyer) -->
        <Rcvry>
          <RcvyPty>
            <Id>
              <BIC>BUYERDEFF</BIC>
            </Id>
          </RcvyPty>
          <RcvyAcct>
            <Id>BUYER-ACC-001</Id>
          </RcvyAcct>
        </Rcvry>
        
        <!-- Cash Settlement Bank -->
        <CashSttlmAgt>
          <FinInstnId>
            <BIC>BANKDEFF</BIC>
          </FinInstnId>
        </CashSttlmAgt>
        
        <!-- Settlement Type: DVP -->
        <SttlmTyp>DVP</SttlmTyp>
      </SctiesSttlmInstrBase>
    </Fin2PartySctiesSttlmInstr>
  </SttlmInstr>
</SctiesSttlmInstr>
```

**Field Definitions & Validation:**

| Field | Type | Mandatory | Validation |
|-------|------|-----------|-----------|
| **SttlmDt** | Date | Yes | T+0/T+1/T+2/T+3 from trade date |
| **ISIN** | String 12 | Yes | Valid per ISO 6166 |
| **Quantity** | Integer | Yes | > 0, must match trade |
| **Amount** | Decimal | Yes | = Qty × Price, correct to 2 decimals |
| **BIC** | String 8,11 | Conditional | Valid per ISO 9362 |
| **SettlementType** | Code | Yes | DVP (Delivery vs Payment) |
| **CashCurrency** | Code 3 | Yes | ISO 4217, must match trade currency |

**Settlement Type Codes:**
- `DVP` = Delivery vs Payment (atomic exchange, most common)
- `FOP` = Free of Payment (securities transfer, cash separate)
- `DTC` = Delivery vs Cash (less common)

**Test Cases - Requirements Agent:**

```
TC-SEC-001: Valid DVP settlement for stock trade
  Inputs: ISIN US0378331005, Qty 1000, Amount 95000.00 USD, SettlementDate T+2
  Expected: Message accepted, all validations pass
  
TC-SEC-002: Settlement amount mismatch
  Inputs: Price 95.00, Qty 1000, Amount 94500.00 (should be 95000)
  Expected: Validation error, Amount != Qty × Price
  
TC-SEC-003: Settlement date violation (T+4)
  Inputs: TradeDate 2026-11-05, SettlementDate 2026-11-09 (T+4)
  Expected: Validation error, only T+0 to T+3 allowed
  
TC-SEC-004: Invalid ISIN format
  Inputs: ISIN "US-00378-331005"
  Expected: Schema validation error
  
TC-SEC-005: FOP settlement (free of payment)
  Inputs: SettlementType FOP, no cash amount required
  Expected: Message accepted without Amount field
```

---

## 4.3 Trade Confirmation Message

### Message: sese.008 (Trade Confirmation)

**Use:** Confirm trade details between parties

**Business Rules:**
- BR1: Must be sent within 24 hours of trade execution
- BR2: Contains trade price, quantity, settlement terms
- BR3: Both parties must confirm match before settlement
- BR4: Confirmation references original trade order
- BR5: Counterparty details must be present
- BR6: Commission/fees itemized separately
- BR7: Confirmation status: pending vs matched vs unmatched

**Confirmation Status Codes:**
- `MTCH` = Matched (both parties confirmed)
- `UMCH` = Unmatched (pending other party confirmation)
- `DFLT` = Default (party failed to confirm in time)

**Key Fields (Trade Details):**

```xml
<Trd>
  <TrdId>TRADE-20261105-001</TrdId>
  <TradDt>
    <Dt>2026-11-05</Dt>
  </TradDt>
  <SctySd>
    <SctySdMtchgSts>MTCH</SctySdMtchgSts>
    <OrgnlTradDt>TRADE-20261105-001</OrgnlTradDt>
    <QtyAndPricDtls>
      <Qty>
        <Qty>1000</Qty>
      </Qty>
      <Prc>
        <Prc>95.00</Prc>
      </Prc>
    </QtyAndPricDtls>
  </SctySd>
  
  <!-- Commissioning -->
  <Comssn>
    <Amt Ccy="USD">950.00</Amt>
  </Comssn>
</Trd>
```

---

## 4.4 Corporate Action Message

### Message: sese.039 (Corporate Action Notification)

**Use:** Notify holders of dividend, split, redemption, or other action

**Business Rules:**
- BR1: Identifies security undergoing corporate action
- BR2: Details action type (dividend, split, redemption, etc.)
- BR3: Record date and payment date specified
- BR4: Dividend amount or split ratio provided
- BR5: Tax implications noted (if applicable)
- BR6: Action is mandatory (must be processed)

**Corporate Action Type Codes:**
- `DRIP` = Dividend Reinvestment Plan
- `DVCA` = Dividend / Capital Gains
- `CAEV` = Cash Event
- `SPLI` = Stock Split
- `RDMD` = Redemption
- `DVSC` = Dividend Scrip (stock dividend)

**Example: Dividend Distribution**

```xml
<CorpActnNtfctn>
  <CorpActn>
    <CorpActnId>CAP-DIV-2026-001</CorpActnId>
    <Isin>US0378331005</Isin>
    <ActnTp>DVCA</ActnTp>
    <RecordDt>2026-11-15</RecordDt>
    <PaymentDt>2026-12-01</PaymentDt>
    <DividendPerShare Ccy="USD">0.50</DividendPerShare>
  </CorpActn>
</CorpActnNtfctn>
```

**Test Cases - Requirements Agent:**

```
TC-SEC-006: Dividend notification
  Inputs: ISIN, Dividend 0.50 USD per share, Record Date 2026-11-15
  Expected: Message accepted, payment calculation correct
  
TC-SEC-007: Stock split 2-for-1
  Inputs: ISIN, Split Ratio 2:1, Effective Date 2026-11-20
  Expected: Holdings doubled, price halved
  
TC-SEC-008: Mandatory redemption
  Inputs: Bond ISIN, Redemption at 100%, Date 2026-12-31
  Expected: All holders must deliver securities on redemption date
```

---

## 4.5 Agent Checklists for Securities Settlement Domain

### Requirements Analysis Checklist
- [ ] Identify traded securities (stocks, bonds, derivatives)
- [ ] Define settlement terms (DVP, FOP, DTC)
- [ ] Specify settlement timeline (T+0, T+1, T+2, T+3)
- [ ] List depository/custodian information
- [ ] Define cash settlement details (currency, bank)
- [ ] Document corporate action types needed
- [ ] Specify reconciliation frequency
- [ ] Define collateral requirements

### Implementation Checklist
- [ ] Implement sese.021 parser (settlement instruction)
- [ ] Implement sese.008 parser (trade confirmation)
- [ ] Create ISIN validation logic
- [ ] Implement DVP settlement matching
- [ ] Create settlement date validation (T+0 to T+3)
- [ ] Implement corporate action processor
- [ ] Create dividend/split calculation logic
- [ ] Implement reconciliation matching
- [ ] Create depository instruction handlers
- [ ] Implement status tracking (matched, unmatched, settled)

### Testing Checklist
- [ ] Test valid DVP settlement instruction
- [ ] Test settlement amount calculation (qty × price)
- [ ] Test settlement date validation (T+0 to T+3)
- [ ] Test invalid ISIN detection
- [ ] Test trade confirmation matching (both parties)
- [ ] Test corporate action processing (dividend, split)
- [ ] Test dividend payment calculations
- [ ] Test stock split adjustment (qty, price)
- [ ] Test FOP settlement (no cash amount)
- [ ] Test commission/fee itemization
- [ ] Test reconciliation matching between parties
- [ ] Test ex-dividend date handling

