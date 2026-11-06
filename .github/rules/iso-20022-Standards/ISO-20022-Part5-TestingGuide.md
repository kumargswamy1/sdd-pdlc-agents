# ISO 20022: Part 5 - Comprehensive Testing Guide for SDLC Agents

**Version:** 2.0 - Technical Edition  
**Target:** Testing Agents, QA Engineers

---

## 5.1 Test Strategy Framework

### Test Pyramid for ISO 20022

```
                    ▲
                   /│\
                  / │ \  System Integration Tests (5-10%)
                 /  │  \  - End-to-end workflows
                /───┼───\
               /    │    \
              /     │     \  Business Logic Tests (20-30%)
             /      │      \ - Validation rules
            /       │       \
           /───────┼───────\
          /        │        \
         /         │         \
        /          │          \  Unit Tests (60-75%)
       /           │           \ - Field validation, parsing
      /_____________│____________\
```

### Test Categories

| Category | Focus | Tools | Coverage |
|----------|-------|-------|----------|
| **Unit Tests** | XML parsing, field validation, date/amount handling | Python pytest, Java JUnit | 80%+ of code paths |
| **Schema Tests** | XML schema compliance, namespace validation | xmllint, XSD validators | 100% of message types |
| **Business Logic Tests** | Calculation rules, state machines, validation rules | Custom test harnesses | 95%+ of business rules |
| **Integration Tests** | Message flow between systems, end-to-end workflows | API test frameworks | 90%+ of workflows |
| **Performance Tests** | Message throughput, latency, memory usage | Load test tools | SLA compliance |
| **Regression Tests** | Version compatibility, backward compatibility | Automated test suites | 100% pass on each version |

---

## 5.2 Unit Testing: Field Validation

### Test Structure Template

```python
# Test: ISO 20022 Field Validation - pacs.008 Amount
import pytest
from iso20022 import Pacs008MessageValidator, ValidationError

class TestPacs008Amount:
    
    def test_amount_valid_positive_value(self):
        """TC-VAL-001: Valid positive amount with 2 decimals"""
        validator = Pacs008MessageValidator()
        result = validator.validate_amount("1500.50", "EUR")
        assert result.is_valid == True
        
    def test_amount_zero_rejected(self):
        """TC-VAL-002: Zero amount rejected"""
        validator = Pacs008MessageValidator()
        with pytest.raises(ValidationError) as exc_info:
            validator.validate_amount("0.00", "EUR")
        assert "Amount must be > 0" in str(exc_info.value)
    
    def test_amount_negative_rejected(self):
        """TC-VAL-003: Negative amount rejected"""
        validator = Pacs008MessageValidator()
        with pytest.raises(ValidationError):
            validator.validate_amount("-1500.50", "EUR")
    
    def test_amount_exceeds_max(self):
        """TC-VAL-004: Amount exceeds maximum allowed"""
        validator = Pacs008MessageValidator()
        # Max: 9,999,999,999,999.99
        with pytest.raises(ValidationError) as exc_info:
            validator.validate_amount("10000000000000.00", "EUR")
        assert "Amount exceeds maximum" in str(exc_info.value)
    
    def test_amount_excessive_decimals(self):
        """TC-VAL-005: Amount with > 2 decimals rejected"""
        validator = Pacs008MessageValidator()
        with pytest.raises(ValidationError):
            validator.validate_amount("1500.505", "EUR")
    
    def test_amount_non_numeric(self):
        """TC-VAL-006: Non-numeric amount rejected"""
        validator = Pacs008MessageValidator()
        with pytest.raises(ValidationError):
            validator.validate_amount("INVALID", "EUR")
    
    def test_amount_boundary_minimum(self):
        """TC-VAL-007: Minimum valid amount (0.01)"""
        validator = Pacs008MessageValidator()
        result = validator.validate_amount("0.01", "EUR")
        assert result.is_valid == True
    
    def test_amount_boundary_maximum(self):
        """TC-VAL-008: Maximum valid amount"""
        validator = Pacs008MessageValidator()
        result = validator.validate_amount("9999999999999.99", "EUR")
        assert result.is_valid == True
```

### Test Data Sets by Field Type

#### Test Data: IBAN Validation

```python
# Valid IBANs (multiple countries)
VALID_IBANS = [
    ("DE89370400440532013000", "Germany"),
    ("GB82WEST12345698765432", "UK"),
    ("FR1420041010050500013M02606", "France"),
    ("ES9121828374961236258369", "Spain"),
    ("IT60X0542811101000000123456", "Italy"),
    ("AT611904300234573201", "Austria"),
]

# Invalid IBANs
INVALID_IBANS = [
    ("DE12345", "Too short"),
    ("DE123456789012345678901234567890", "Too long"),
    ("XY89370400440532013000", "Invalid country code"),
    ("DE89370400440532013A00", "Contains letter in number part"),
    ("", "Empty string"),
    (None, "Null value"),
]

# Test Cases
def test_iban_valid_all_countries():
    for iban, country in VALID_IBANS:
        assert IbanValidator.validate(iban).is_valid == True

def test_iban_invalid_all_cases():
    for iban, reason in INVALID_IBANS:
        with pytest.raises(ValidationError):
            IbanValidator.validate(iban)
```

#### Test Data: Date/DateTime Validation

```python
# Valid DateTimes (UTC)
VALID_DATETIMES = [
    "2026-11-05T18:28:06Z",  # Standard
    "2026-01-01T00:00:00Z",  # Midnight
    "2026-12-31T23:59:59Z",  # End of day
]

# Invalid DateTimes
INVALID_DATETIMES = [
    "2026-11-05T18:28:06",     # Missing Z
    "2026-11-05T18:28:06+05:30",  # Wrong timezone
    "2026-11-05 18:28:06Z",    # Wrong separator
    "2026-13-01T18:28:06Z",    # Invalid month
    "2026-11-32T18:28:06Z",    # Invalid day
]

# Test Cases
def test_datetime_valid_formats():
    for dt in VALID_DATETIMES:
        assert DateTimeValidator.validate(dt).is_valid == True

def test_datetime_invalid_formats():
    for dt in INVALID_DATETIMES:
        with pytest.raises(ValidationError):
            DateTimeValidator.validate(dt)
```

---

## 5.3 Business Logic Testing

### Test Case: pacs.008 Credit Transfer Full Workflow

```python
class TestPacs008CreditTransferWorkflow:
    
    @pytest.fixture
    def debtor_account(self):
        return {
            "IBAN": "DE89370400440532013000",
            "Currency": "EUR",
            "Balance": 10000.00,
            "Limit": 50000.00,
        }
    
    def test_credit_transfer_sufficient_funds(self, debtor_account):
        """TC-LOGIC-001: Transfer succeeds with sufficient funds"""
        message = Pacs008(
            amount=1500.50,
            debtor_iban=debtor_account["IBAN"],
            creditor_iban="DE75512108001234567890",
            currency="EUR"
        )
        
        validator = Pacs008Validator(debtor_account)
        result = validator.validate_business_logic(message)
        
        assert result.is_valid == True
        assert result.errors == []
    
    def test_credit_transfer_insufficient_funds(self, debtor_account):
        """TC-LOGIC-002: Transfer fails - insufficient funds"""
        message = Pacs008(
            amount=15000.00,  # > 10000 balance
            debtor_iban=debtor_account["IBAN"],
            creditor_iban="DE75512108001234567890",
            currency="EUR"
        )
        
        validator = Pacs008Validator(debtor_account)
        result = validator.validate_business_logic(message)
        
        assert result.is_valid == False
        assert "AM01" in result.error_codes  # Insufficient funds code
    
    def test_credit_transfer_exceeds_limit(self, debtor_account):
        """TC-LOGIC-003: Transfer fails - exceeds daily limit"""
        message = Pacs008(
            amount=55000.00,  # > 50000 limit
            debtor_iban=debtor_account["IBAN"],
            creditor_iban="DE75512108001234567890",
            currency="EUR"
        )
        
        validator = Pacs008Validator(debtor_account)
        result = validator.validate_business_logic(message)
        
        assert result.is_valid == False
        assert "AM04" in result.error_codes  # Limit exceeded code
    
    def test_control_sum_verification(self):
        """TC-LOGIC-004: Message CtrlSum matches transaction sum"""
        transactions = [
            {"Amount": 100.00},
            {"Amount": 200.00},
            {"Amount": 300.00},
        ]
        
        message = Pacs008BatchMessage(
            transactions=transactions,
            ctrl_sum=600.00
        )
        
        validator = Pacs008Validator()
        result = validator.verify_control_sum(message)
        
        assert result.is_valid == True
        assert result.calculated_sum == 600.00
    
    def test_control_sum_mismatch(self):
        """TC-LOGIC-005: Message rejected - CtrlSum mismatch"""
        transactions = [
            {"Amount": 100.00},
            {"Amount": 200.00},
        ]
        
        message = Pacs008BatchMessage(
            transactions=transactions,
            ctrl_sum=350.00  # Should be 300.00
        )
        
        validator = Pacs008Validator()
        result = validator.verify_control_sum(message)
        
        assert result.is_valid == False
        assert result.error == "CtrlSum mismatch: expected 300.00, got 350.00"
```

### Test Case: camt.053 Reconciliation Logic

```python
class TestCamt053BankStatement:
    
    def test_statement_reconciliation_pass(self):
        """TC-RECON-001: Statement reconciles successfully"""
        statement = Camt053(
            opening_balance=10000.00,
            closing_balance=8499.50,
            transactions=[
                {"Amount": -1500.50, "Type": "DBTS"},  # Debit
                {"Amount": 0.00, "Type": "FEES"},      # No net
            ]
        )
        
        reconciler = StatementReconciler()
        result = reconciler.reconcile(statement)
        
        # Verify: opening + sum(transactions) = closing
        assert result.is_reconciled == True
        assert result.calculated_closing == 8499.50
    
    def test_statement_reconciliation_fail(self):
        """TC-RECON-002: Statement fails to reconcile"""
        statement = Camt053(
            opening_balance=10000.00,
            closing_balance=8500.00,  # Should be 8499.50
            transactions=[
                {"Amount": -1500.50, "Type": "DBTS"},
            ]
        )
        
        reconciler = StatementReconciler()
        result = reconciler.reconcile(statement)
        
        assert result.is_reconciled == False
        assert result.expected == 8499.50
        assert result.actual == 8500.00
    
    def test_transaction_time_ordering(self):
        """TC-RECON-003: Transactions must be time-ordered"""
        statement = Camt053(
            transactions=[
                {"Time": "14:30:00", "Amount": 100.00},
                {"Time": "10:15:00", "Amount": 50.00},   # Out of order
                {"Time": "16:45:00", "Amount": 75.00},
            ]
        )
        
        validator = StatementValidator()
        result = validator.validate_transaction_ordering(statement)
        
        assert result.is_valid == False
        assert "Transaction out of chronological order" in result.error
```

---

## 5.4 Schema & Structure Testing

### XML Schema Validation Test

```python
def test_pacs008_schema_validation():
    """TC-SCHEMA-001: Valid pacs.008 passes XSD validation"""
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
    <Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.03.08">
      <CstmrCdtTrfInitn>
        <GrpHdr>
          <MsgId>20261105001</MsgId>
          <CreDtTm>2026-11-05T18:28:06Z</CreDtTm>
          <NbOfTxns>1</NbOfTxns>
          <CtrlSum>1500.50</CtrlSum>
        </GrpHdr>
      </CstmrCdtTrfInitn>
    </Document>"""
    
    schema_validator = XsdValidator("pacs.008.03.08")
    result = schema_validator.validate(xml_content)
    
    assert result.is_valid == True

def test_missing_mandatory_field():
    """TC-SCHEMA-002: Missing MsgId causes validation failure"""
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
    <Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.03.08">
      <CstmrCdtTrfInitn>
        <GrpHdr>
          <CreDtTm>2026-11-05T18:28:06Z</CreDtTm>
          <NbOfTxns>1</NbOfTxns>
          <CtrlSum>1500.50</CtrlSum>
        </GrpHdr>
      </CstmrCdtTrfInitn>
    </Document>"""
    
    schema_validator = XsdValidator("pacs.008.03.08")
    result = schema_validator.validate(xml_content)
    
    assert result.is_valid == False
    assert "MsgId is mandatory" in result.error_message
```

---

## 5.5 Integration Testing

### End-to-End Payment Workflow Test

```python
def test_payment_workflow_end_to_end():
    """TC-E2E-001: Complete payment from order to settlement"""
    
    # Step 1: Create payment order (pacs.008)
    payment_order = Pacs008MessageFactory.create_from_requirements({
        "Debtor": "Acme Corp",
        "Creditor": "Supplier Inc",
        "Amount": 1500.50,
        "Currency": "EUR",
    })
    
    # Step 2: Send to bank system
    bank_system = BankingSystemSimulator()
    response = bank_system.process_payment(payment_order)
    assert response.status == "ACCEPTED"
    
    # Step 3: Verify in statement (camt.053)
    statement = bank_system.get_daily_statement(date="2026-11-05")
    assert any(t["amount"] == 1500.50 for t in statement.transactions)
    
    # Step 4: Verify notification (camt.001)
    notification = bank_system.get_notifications_for("Acme Corp")
    assert len(notification) > 0
    assert notification[0].amount == 1500.50
```

---

## 5.6 Test Data Generation

### Test Data Factory Pattern

```python
class Pacs008TestDataFactory:
    """Factory for generating valid ISO 20022 test messages"""
    
    @staticmethod
    def create_valid_credit_transfer(**overrides):
        """Generate valid pacs.008 with sensible defaults"""
        defaults = {
            "MsgId": f"MSG{int(time.time())}",
            "CreDtTm": datetime.utcnow().isoformat() + "Z",
            "Amount": 1500.50,
            "Currency": "EUR",
            "DebtorIBAN": "DE89370400440532013000",
            "CreditorIBAN": "DE75512108001234567890",
            "Purpose": "Invoice INV-2026-0001",
        }
        defaults.update(overrides)
        return Pacs008Message(**defaults)
    
    @staticmethod
    def create_rejected_transfer(reason_code="AC01"):
        """Generate rejection response"""
        return Pacs008Rejection(
            original_msg_id="MSG123456",
            reason_code=reason_code,
            timestamp=datetime.utcnow().isoformat() + "Z"
        )
```

---

## 5.7 Test Execution Checklist

### Pre-Test
- [ ] All required test data prepared
- [ ] Test environment configured (dev, staging)
- [ ] Connection to ISO 20022 repository available
- [ ] XSD schemas downloaded for all message versions
- [ ] Test database initialized with sample accounts

### Unit Tests
- [ ] Run all field validation tests (100% code coverage)
- [ ] Run all data type tests (identifiers, amounts, dates)
- [ ] Run all parsing/serialization tests
- [ ] Verify error message clarity and correctness

### Business Logic Tests
- [ ] Run all validation rule tests
- [ ] Test all error codes with expected messages
- [ ] Test boundary conditions (min/max amounts, dates)
- [ ] Test state machine transitions

### Integration Tests
- [ ] Test full payment workflow (pacs.008 → camt.053)
- [ ] Test settlement workflow (sese.021 → settlement)
- [ ] Test error recovery and retries
- [ ] Test multi-party workflows

### Regression Tests
- [ ] Run against previous version (backward compatibility)
- [ ] Verify no regression in error handling
- [ ] Verify performance SLAs maintained
- [ ] Verify audit trail completeness

### Performance Tests
- [ ] Process 1000 messages, measure latency (< 100ms/msg)
- [ ] Test memory usage (< 500MB for 10,000 queued messages)
- [ ] Test concurrent processing (500 parallel messages)
- [ ] Measure XML parsing throughput (> 10,000 msgs/sec)

