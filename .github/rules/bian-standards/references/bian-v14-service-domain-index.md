# BIAN v14.0.0 Service Domain API Index (generated, structural metadata only)

> **Evidence label:** Official BIAN (structural metadata extracted from official OpenAPI files; no descriptive text reproduced).
> **BIAN release:** 14.0.0 · **Flavour:** BOM-extended OAS 3.x
> **Source:** `bian-official/public` @ commit `b58bf4c2c300dd018afc084e9bb24b7adaaa3500` (committed 2026-02-12), path `release14.0.0/semantic-apis/oas3 /yamls/` (the folder name contains a trailing space in the official repository). License of repository: Apache-2.0.
> **Generated:** 2026-11-05 by scanning every `*.yaml` file in that folder.
> **Count:** 258 files = 242 with at least one operation + 16 with `paths: {}` (Service Domains without Service Operations, therefore no API endpoints; matches the v14.0 release notes section 11 list).

## How to use
- Use this index to **confirm that a Service Domain, Control Record (CR) or Behavior Qualifier (BQ) name exists in v14.0.0** before citing it. Search with `grep -i "<term>" references/bian-v14-service-domain-index.md`.
- A name that is **absent** from this index is *not* proof that it does not exist in the BIAN model: this index only covers Service Domains that have a published API file. Business Area, Business Domain, Functional Pattern, asset type and Business Capability are **not** in the OpenAPI files and are therefore **not** in this index; take them from the BIAN Portal / Service Landscape (see `bian-source-registry.md`).
- Columns: `File stem` = official file name without `.yaml` (use for URLs) · `Title` = `info.title` · `CR tag` = Control Record tag (`CR - ...`) · `CR-level actions` = action terms exposed directly on the Control Record · `BQs` = Behavior Qualifier tags (`BQ - ...`) · `Ops` = number of HTTP operations in the file.
- Action terms are those that actually occur in the path suffix. A BQ's own action terms are in the specification file itself.
- **Not found by name in this folder** although named in the v14.0 release notes (status Unverified; they may exist only in the member-gated model): Payee Management, Customer Consent, Payment Orchestration, Payment Confirmation, Payment Settlement, Corporate Card Service. See `bian-release-14-changes.md`.

| File stem | Title | CR tag | CR-level actions | BQs | Ops |
|---|---|---|---|---|---|
| ATMNetworkOperations | ATM Network Operations | ATMNetworkOperatingSession | Control, Exchange, Execute, Request, Retrieve, Update, Initiate | CashDistribution, NetworkOperation, DeviceTracking, FinancialDocumentHandling, FinancialTransactionCapture | 28 |
| AccountReconciliation | Account Reconciliation | AccountReconciliationProcedure | Control, Exchange, Initiate, Retrieve, Notify, Request, Execute, Update | AccountAssessment, AccountResolution | 22 |
| AccountRecovery | Account Recovery | AccountRecoveryProcedure | Initiate, Update, Exchange, Retrieve | Writedown, Negotiation, Modification, Planning, Assessment | 17 |
| AccountsReceivable | Accounts Receivable | AccountsReceivableProcedure | Control, Exchange, Retrieve, Execute, Initiate, Update, Request | Payment, ReceivablesEvaluation, Resolution, CustomerNegotiation | 22 |
| AdvancedVoiceServicesManagement | Advanced Voice Services Management | VoiceChannelManagementPlan | Create, Exchange, Retrieve, Request, Update | MaintenanceAndUpgrades, CapacityPlanning, Troubleshooting | 15 |
| AdvancedVoiceServicesOperations | Advanced Voice Services Operations | VoiceChannelOperatingSession | Initiate, Update, Control, Request, Retrieve | Inbound, Outbound | 9 |
| Advertising | Advertising | AdvertisingCampaignManagementPlan | Create, Update, Grant, Request, Retrieve | MarketTracking, PerformanceAssessment, CampaignDirection | 18 |
| ArchiveServices | Archive Services | ArchiveOperatingSession | Exchange, Request, Update, Execute, Retrieve, Notify, Control, Initiate | DocumentMaintenance, DocumentCapture, DocumentRetrieval | 29 |
| AssetAndLiabilityManagement | Asset And Liability Management | AssetAndLiabilityPortfolioStrategy | Update, Request, Grant, Retrieve | TransactionAlignment | 8 |
| AssetSecuritization | Asset Securitization | AssetSecuritizationTransaction | Control, Exchange, Execute, Request, Retrieve, Update, Initiate | Placement, Selection, Securitization | 22 |
| BankDrafts | Bank Drafts | BearerDocumentTransaction | Exchange, Control, Execute, Retrieve, Initiate, Notify, Update, Request | BankGuaranteedPaymentRemittance, CustomerPayment, BearerDocumentCreationandRegistration, BankGuaranteedPaymentSpecification | 36 |
| BankGuarantee | Bank Guarantee | BankGuaranteeTransaction | Control, Exchange, Initiate, Notify, Request, Retrieve, Update, Execute | Collection, BankGuaranteeDefinitionandPricing, CustomerPayment, BankGuaranteePayout, CustomerCollateralAllocation, BankGuaranteeIssuanceandBooking | 50 |
| BranchCurrencyDistribution | Branch Currency Distribution | CashDistributionProcedure | Exchange, Control, Execute, Request, Initiate, Update, Retrieve | DistributionPlanning, InventoryProvisioning, InventoryDistributionOversight, DistributionVehicleAdministration | 21 |
| BranchCurrencyManagement | Branch Currency Management | BranchCashAllocation | Capture, Exchange, Control, Initiate, Update, Retrieve | InventoryAllocation | 12 |
| BranchLocationManagement | Branch Location Management | BranchLocationManagementPlan | Capture, Control, Exchange, Grant, Initiate, Retrieve, Request, Update | ProductandServicePlanning, CustomerLiaison, StaffandLocationPlanning, Troubleshooting | 27 |
| BranchLocationOperations | Branch Location Operations | BranchLocationAdministrativePlan | Control, Create, Exchange, Grant, Notify, Request, Retrieve, Update | CashInventoryHandling | 14 |
| BrandManagement | Brand Management | BrandManagementPlan | Request, Update, Grant, Retrieve | BrandAdvice, Troubleshooting | 13 |
| BrokeredProductProxy | Brokered Product Proxy | - | - | - | 0 |
| BusinessDevelopment | Business Development | BusinessDevelopmentStrategy | Update, Grant, Exchange, Create, Request, Retrieve, Capture | - | 7 |
| BusinessUnitManagement | Business Unit Management | BusinessUnitManagementPlan | Create, Exchange, Update, Request, Retrieve | Troubleshooting, Performance | 12 |
| CardAuthorization | Card Authorization | CreditCardAuthorizationAssessment | Update, Evaluate, Exchange, Execute, Request, Grant, Retrieve, Control | DeviceCheck, Authentication, FraudCheck, CreditCheck, StandIn, Authorization | 16 |
| CardCase | Card Case | CardCaseProcedure | Update, Initiate, Control, Exchange, Execute, Retrieve, Request | Consolidation, Chargeback, Arbitration, Resolution | 17 |
| CardClearing | Card Clearing | CardClearingProcedure | Initiate, Update, Retrieve | Capture, Addressing, FXConversion, Charge, Matching, Reconciliation, Routing | 13 |
| CardCollections | Card Collections | CardCollectionsProcedure | Initiate, Update, Control, Execute, Request, Retrieve | Assignment, PaymentTerms, Payment, Resolution | 16 |
| CardFinancialSettlement | Card Financial Settlement | CardFinancialSettlementProcedure | Initiate, Update, Retrieve, Control | Consolidation, Processing, Payment, Instruction | 12 |
| CardNetworkParticipantFacility | Card Network Participant Facility | CardNetworkParticipantAgreement | Initiate, Update, Retrieve, Control | - | 4 |
| CardTerminalAdministration | Card Terminal Administration | CardPOSDeviceAllocation | Update, Request, Provide, Retrieve | Allocation | 11 |
| CardTerminalOperation | Card Terminal Operation | CardPOSNetworkOperatingSession | Retrieve, Update, Initiate, Control | Capture, Authorization, Batch | 15 |
| CardTransactionCapture | Card Transaction Capture | CardFinancialCaptureTransaction | Exchange, Execute, Control, Initiate, Request, Retrieve, Update | TransactionConsolidation, TransactionAuthorization, TransactionCapture, TransactionReversal | 22 |
| CardTransactionSwitch | Card Transaction Switch | CardTransactionSwitchOperatingSession | Initiate, Update, Exchange, Retrieve, Control | TransactionCapture | 7 |
| CardTransactionTracking | Card Transaction Tracking | - | - | - | 0 |
| CardeCommerceGateway | Card eCommerce Gateway | eCommerceGatewayOperatingSession | Control, Retrieve | CardPayment, TransactionBatch, CardAuthentication, TransactionAuthorization | 14 |
| CaseRootCauseAnalysis | Case Root Cause Analysis | CustomerCaseRootCauseAnalysis | Request, Execute, Retrieve, Initiate, Update | CreditandFraudRelatedIssueAnalysis, OperationsandServicingIssueAnalysis, ProductandServiceIssueAnalysis | 20 |
| CashConcentration | Cash Concentration | AccountBalanceSweepingFacility | Control, Request, Exchange, Notify, Execute, Update, Initiate, Retrieve, Activate | CashTransfer | 16 |
| CashManagementAndAccountServices | Cash Management And Account Services | CashManagementAndAccountServicesFacility | Initiate, Update, Control, Retrieve | Interest, Charge, Sweep, DebitandCredit, Payment, IssuedDevice, PositivePay, Deposit, AmountBlock | 34 |
| CentralCashHandling | Central Cash Handling | CentralCashAllocation | Capture, Control, Exchange, Initiate, Retrieve, Update | ProjectionandAllocation, TrackingandAllocation | 18 |
| ChannelActivityAnalysis | Channel Activity Analysis | ChannelActivityAnalysis | Exchange, Evaluate, Request, Retrieve | CustomerFraud, MerchantFraud, MerchantBehavior, CustomerBehavior, Bot, DeviceError | 16 |
| ChannelActivityHistory | Channel Activity History | ChannelActivityLog | Initiate, Retrieve, Control, Update | Event | 7 |
| ChequeLockBox | Cheque Lock Box | LockBoxFacility | Notify, Control, Exchange, Execute, Initiate, Request, Retrieve, Update | IssueResolution, Payment, TransactionBatch | 25 |
| ChequeProcessing | Cheque Processing | ChequeProcessingOperatingSession | Control, Exchange, Execute, Initiate, Retrieve, Request, Update | FinancialTransactionInitiation, ChequeExceptionHandling, ChequeExtraction | 13 |
| ClaimAdministration | Claim Administration | - | - | - | 0 |
| ClaimAssessment | Claim Assessment | - | - | - | 0 |
| CollateralAllocationManagement | Collateral Allocation Management | CollateralAssetAllocation | Update, Retrieve, Exchange, Capture | - | 4 |
| CollateralAssetAdministration | Collateral Asset Administration | CollateralAssetAdministrativePlan | Create, Update, Retrieve | Valuation, Maintenance | 12 |
| Collections | Collections | CollateralAssetLiquidationProcedure | Control, Exchange, Execute, Initiate, Retrieve, Update, Request | CollateralValuation, CollateralLiquidation, DebtFactoring, CollectionsAssessment, CollectionsAccountUpdate | 24 |
| CommissionAgreement | Commission Agreement | EmployeeCommissionAgreement | Initiate, Request, Control, Exchange, Grant, Retrieve, Update | CommissionTerm | 14 |
| Commissions | Commissions | CommissionTransaction | Retrieve, Control, Exchange, Execute, Initiate, Request, Update | Confirmation, Calculation, Payment | 17 |
| CompetitorAnalysis | Competitor Analysis | CompetitorAnalysis | Evaluate, Execute, Request, Retrieve | ProductCompetitiveAnalysis | 6 |
| ComplianceReporting | Compliance Reporting | ComplianceReportingAdministrativePlan | Request, Initiate, Retrieve, Update, Capture | Consolidation, ComplianceAssessment, Remediation | 18 |
| ConsumerAdvisoryServices | Consumer Advisory Services | ConsumerAdvice | Update, Initiate, Control, Request, Retrieve | FinancialPlanning, Taxation, ProductGuidance, Charge | 19 |
| ConsumerInvestments | Consumer Investments | ConsumerSecuritiesOrderTransaction | Initiate, Update, Retrieve | Quote, Confirmation, Compliance, OrderInitiation | 8 |
| ConsumerLoan | Consumer Loan | ConsumerLoanFacility | Initiate, Update, Control, Retrieve | Interest, Charge, Disbursement, Maintenance, DebitandCredit, Repayment, AmountBlock, IssuedDevice, Booking, Modification | 29 |
| ContactCenterManagement | Contact Center Management | ContactCenterManagementPlan | Update, Create, Exchange, Request, Retrieve | Performance, Troubleshooting | 12 |
| ContactCenterOperations | Contact Center Operations | ContactCenterAdministrativePlan | Create, Update, Control, Execute, Request, Retrieve | Assignment, PeakLoad, Troubleshooting | 18 |
| ContactHandler | Contact Handler | CustomerContactOperatingSession | Initiate, Update, Control, Exchange, Execute, Retrieve, Request | Authentication, Routing, Session, History | 16 |
| ContactRouting | Contact Routing | CustomerServicingResourceAllocation | Provide, Control, Update, Exchange, Capture, Retrieve | Allocation | 12 |
| ContractorandSupplierAgreement | Contractor and Supplier Agreement | SupplierAgreement | Control, Evaluate, Exchange, Grant, Notify, Update, Request, Retrieve | LegalTerm, PolicyTerm, RegulatoryTerm | 26 |
| CorporateAction | Corporate Action | CorporateActionProcedure | Control, Initiate, Execute, Exchange, Notify, Request, Retrieve, Update | SecurityMergersandAcquisitionAction, SecurityDividendPayment, SecurityRightsIssueAction, SecuritySpin-OffAction, StockSplitorReversalAction | 43 |
| CorporateCurrentAccount | Corporate Current Account | CorporateCurrentAccountFacility | Initiate, Update, Control, Retrieve | Interest, Charge, Sweep, DebitandCredit, Payment, IssuedDevice, AmountBlock, Deposit, Booking | 34 |
| CorporateFinance | Corporate Finance | CorporateFinanceServicesAdvice | Exchange, Initiate, Update, Control, Request, Execute, Notify, Retrieve | StrategicFunding, Taxation, CapitalStructuring, TacticalFunding | 36 |
| CorporateLease | Corporate Lease | CorporateLeaseFacility | Control, Exchange, Execute, Initiate, Retrieve, Request, Update | Administration, Fulfill | 18 |
| CorporateLoan | Corporate Loan | CorporateLoanFacility | Initiate, Update, Control, Retrieve | Interest, Charge, Disbursement, Maintenance, DebitandCredit, Repayment, AmountBlock, Booking, IssuedDevice, Modification | 29 |
| CorporatePayrollServices | Corporate Payroll Services | EmployeePaymentServicesFacility | Control, Initiate, Execute, Notify, Request, Retrieve, Update | IssueResolution | 14 |
| CorporateTaxAdvisory | Corporate Tax Advisory | CorporateTaxAdvice | Initiate, Update, Request, Retrieve, Control | Taxation, Charge | 14 |
| CorporateTreasury | Corporate Treasury | CorporateTreasuryManagementPlan | Update, Capture, Retrieve | Securitization, Liquidity, StrategicFunding, TacticalFunding, BankRates | 11 |
| CorporateTrustServices | Corporate Trust Services | CorporateTrustServicesFacility | Control, Exchange, Execute, Initiate, Notify, Request, Retrieve, Update | ProjectFinance, Escrow, CourtLiaison, Financing, LoanAgencyandAdministration | 43 |
| Correspondence | Correspondence | CorrespondenceOperatingSession | Request, Initiate, Update, Control, Execute, Retrieve | Outbound, OutboundWithResponse, Inbound, BlockMailing | 18 |
| CorrespondentBankDirectory | Correspondent Bank Directory | CorrespondentBankDirectoryEntry | Register, Update, Request, Retrieve | - | 4 |
| CorrespondentBankRelationshipManagement | Correspondent Bank Relationship Management | CorrepondentBankRelationshipManagementPlan | Control, Create, Exchange, Notify, Grant, Request, Retrieve, Update | RelationshipReciprocityAssessment, IncidentTroubleshootingOversight, RelationshipDevelopment | 26 |
| CounterpartyAdministration | Counterparty Administration | CounterpartyDirectoryEntry | Control, Execute, Register, Request, Notify, Update, Retrieve | CounterpartyEntityReference, CounterpartyPermittedTransaction | 19 |
| CreditCard | Credit Card | CreditCardFacility | Initiate, Retrieve, Update, Control | Interest, Charge, Billing, Repayment, CardPayment, IssuedDevice, CreditPlan | 28 |
| CreditFacility | Credit Facility | CreditLineFacility | Retrieve, Initiate, Update | CreditAllocation, Charge | 10 |
| CreditManagement | Credit Management | CreditPricingAssessment | Evaluate, Grant, Update, Exchange, Retrieve | - | 5 |
| CreditRiskModels | Credit Risk Models | CreditRiskModelSpecification | Retrieve, Capture, Exchange, Initiate, Control, Request, Update | FunctionalRequirements, Production, Testing | 19 |
| CreditRiskOperations | Credit Risk Operations | TradingCreditPositionMeasurement | Control, Evaluate, Execute, Notify, Request | TradingCounterpartyCreditLimitIndicator | 10 |
| CurrencyExchange | Currency Exchange | CurrencyExchangeTransaction | Execute, Initiate, Control, Exchange, Retrieve, Request, Update | FXTransactionCapture, DocumentHandling, Quote | 18 |
| CurrentAccount | Current Account | CurrentAccountFacility | Initiate, Update, Control, Retrieve | Interest, Charge, Sweep, DebitandCredit, Payment, IssuedDevice, Booking, Deposit, AmountBlock | 34 |
| CustodyAdministration | Custody Administration | CustodyFacility | Retrieve, Request, Initiate, Control, Exchange, Execute, Update | Settlement, Dividend, SafeKeeping, Charge, RegulatorySubmission | 26 |
| CustomerAccessEntitlement | Customer Access Entitlement | CustomerAccessProfileAgreement | Evaluate, Update, Exchange, Request, Control, Grant, Retrieve | Restrictions, Preferences | 13 |
| CustomerAgreement | Customer Agreement | CustomerAgreement | Evaluate, Update, Exchange, Control, Request, Grant, Retrieve | LegalTerm, RegulatoryTerm, PolicyTerm | 16 |
| CustomerBehaviorInsights | Customer Behavior Insights | CustomerBehaviorAnalysis | Evaluate, Exchange, Request, Execute, Retrieve | Insight | 9 |
| CustomerBehaviorModels | Customer Behavior Models | CustomerBehaviorModelSpecification | Create, Execute, Request, Retrieve | FunctionalRequirements, Testing, Production | 15 |
| CustomerBilling | Customer Billing | CustomerBillingProcedure | Initiate, Update, Control, Execute, Request, Retrieve | Invoicing, TrackingandReminders, Payment | 15 |
| CustomerCampaignDesign | Customer Campaign Design | CustomerCampaignSpecification | Update, Create, Control, Exchange, Capture, Execute, Request, Retrieve | - | 8 |
| CustomerCampaignExecution | Customer Campaign Execution | CustomerCampaignProcedure | Initiate, Update, Control, Exchange, Execute, Request, Retrieve | CandidateSelection, Execution, AnalysisFeedback | 18 |
| CustomerCampaignManagement | Customer Campaign Management | CustomerCampaignPortfolioManagementPlan | Create, Update, Request, Grant, Retrieve | MarketTracking, PerformanceAssessment, CampaignDirection | 18 |
| CustomerCase | Customer Case | CustomerCaseProcedure | Initiate, Update, Control, Exchange, Execute, Request, Retrieve | Analysis, Determination, Resolution | 14 |
| CustomerCaseManagement | Customer Case Management | CustomerCaseManagementPlan | Create, Update, Exchange, Request, Retrieve | Rules, Performance | 11 |
| CustomerCreditRating | Customer Credit Rating | CustomerCreditRatingState | Initiate, Control, Exchange, Execute, Request, Retrieve | Alerts, InternalReporting, ExternalReporting | 12 |
| CustomerEventHistory | Customer Event History | CustomerEventLog | Control, Retrieve, Initiate, Update | Relationship, Sales, Servicing, ProductProcessing, Fraud, Life | 22 |
| CustomerFinancialInsights | Customer Financial Insights | CustomerFinancialPositionAnalysis | Retrieve | - | 1 |
| CustomerOffer | Customer Offer | CustomerOfferProcedure | Update, Control, Execute, Retrieve, Exchange, Request, Initiate | FacilityApplication, Disclosures, Underwriting, Credit, Compliance, Audit, CollateralAllocation, Booking, CorrespondenceandDocuments, Agreement, ProductInitialization | 34 |
| CustomerPortfolio | Customer Portfolio | CustomerPortfolioAnalysis | Evaluate, Update, Request, Retrieve | PerformanceAnalysis | 10 |
| CustomerPosition | Customer Position | CustomerPositionState | Initiate, Update, Control, Execute, Request, Retrieve | Cashflow, Credit, CollateralAllocation | 19 |
| CustomerProductAndServiceEligibility | Customer Product And Service Eligibility | CustomerEligibilityAssessment | Evaluate, Update, Exchange, Execute, Request, Grant, Retrieve | EligibilityCheck, NextBest | 11 |
| CustomerProductandServiceDirectory | Customer Product and Service Directory | CustomerProductAndServiceDirectoryEntry | Control, Execute, Notify, Register, Request, Update, Retrieve | Product, Service | 19 |
| CustomerProposition | Customer Proposition | CustomerPropositionAgreement | Control, Evaluate, Exchange, Grant, Notify, Request, Retrieve, Update | BankDefinedProductandServiceTerm, CustomerDefinedProductandServiceTerm | 21 |
| CustomerRelationshipManagement | Customer Relationship Management | CustomerRelationshipManagementPlan | Create, Update, Control, Request, Grant, Exchange, Retrieve | Development, Incident, Contact | 22 |
| CustomerSurveys | Customer Surveys | - | - | - | 0 |
| CustomerTaxHandling | Customer Tax Handling | CustomerTaxObligationFacility | Initiate, Update, Control, Execute, Request, Retrieve | Consolidation, Analysis, Reporting | 14 |
| CustomerWorkbench | Customer Workbench | CustomerWorkbenchOperatingSession | Retrieve, Initiate, Update, Control | SWUpdate, Broadcast, Browsing, Contact, ProductandServiceAccess | 23 |
| DealerDesk | Dealer Desk | DealerDeskOperatingSession | Exchange, Execute, Control, Initiate, Request, Notify, Retrieve, Update | DealerDeskConsolidatedPositionTracking, DealerDeskTradingAssignmentandLimits, InformationFeedAdministration | 29 |
| DelinquentAccountHandling | Delinquent Account Handling | DelinquentAccountProcedure | Initiate, Update, Control, Execute, Retrieve | Assessment, Contact, Payment, Resolution | 16 |
| DirectDebit | Direct Debit | DirectDebitFacility | Control, Exchange, Execute, Retrieve, Update, Initiate, Request | PaymentBatch, Reporting | 11 |
| DirectDebitMandate | Direct Debit Mandate | DirectDebitMandateDirectoryEntry | Register, Retrieve, Update, Control | MandateRegistration | 10 |
| Disbursement | Disbursement | DisbursementTransaction | Initiate, Update, Control, Exchange, Execute, Request, Retrieve | - | 7 |
| DocumentDirectory | Document Directory | DocumentDirectoryEntry | Exchange, Request, Control, Execute, Notify, Register, Retrieve, Update | DocumentAmendmentProperties, DocumentArchivingProperties, DocumentReferenceProperties, DocumentUpdateHistoryProperties, DocumentVerificationProperties, DocumentVersionProperties | 44 |
| DocumentServices | Document Services | DocumentServiceProcedure | Control, Exchange, Execute, Initiate, Notify, Request | - | 6 |
| ECMAndDCM | ECM And DCM | ECMAndDCMFacility | Initiate, Update, Exchange, Request, Retrieve | InstrumentDesign, Prospectus, Placement | 14 |
| EnterpriseArchitecture | Enterprise Architecture | EnterpriseArchitectureSpecification | Capture, Control, Exchange, Retrieve, Initiate, Request, Update | TechnologyInfrastructure, BusinessArchitecture, ApplicationArchitecture, Organization, InformationArchitecture | 27 |
| Factoring | Factoring | FactoringFacility | Exchange, Control, Execute, Initiate, Notify, Request, Retrieve, Update | AccountReceivableFactoring, FactoringProcessing, FactoringEvaluation, FactoringPurchase | 36 |
| FiduciaryAgreement | Fiduciary Agreement | - | - | Fiduciary, Charge | 8 |
| FinancialAccounting | Financial Accounting | FinancialBookingLog | Initiate, Update, Control, Retrieve | LedgerPosting | 7 |
| FinancialGateway | Financial Gateway | FinancialGatewayOperatingSession | Initiate, Update, Control, Request, Retrieve | Inbound, Outbound | 9 |
| FinancialInstrumentReferenceDataManagement | Financial Instrument Reference Data Management | FinancialInstrumentDirectoryEntry | Control, Execute, Notify, Register, Request, Retrieve, Update | DebtInstrument, Equity, Futures, Option, Warrant, Currency | 40 |
| FinancialInstrumentValuation | Financial Instrument Valuation | MarketAssetValuationProcedure | Control, Exchange, Execute, Initiate, Notify, Request, Retrieve, Update | AssetValuationApproachSelection, AssetValuationInformationConsolidation, AssetValuation | 29 |
| FinancialMarketAnalysis | Financial Market Analysis | FinancialMarketAnalysis | Execute, Retrieve, Initiate, Request, Update | FinancialMarketInsight | 10 |
| FinancialMarketResearch | Financial Market Research | FinancialMarketResearchDirectoryEntry | Register, Update, Execute, Request, Retrieve | - | 5 |
| FinancialStatementAssessment | Financial Statement Assessment | FinancialStatementAssessment | Evaluate, Execute, Grant, Notify, Request, Retrieve | AssetandLiabilityValuationTest, LiquidityandCashFlowTest, RiskTest, SensitivityTest | 26 |
| FraudDiagnosis | Fraud Diagnosis | FraudDiagnosisAnalysis | Update, Evaluate, Exchange, Request, Retrieve | EconomicModel, CustomerBehavior, AnalystReview | 9 |
| FraudEvaluation | Fraud Evaluation | FraudEvaluationAssessment | Evaluate, Exchange, Execute, Grant, Request, Retrieve | RuleSetsandDecisionTrees, Models | 8 |
| FraudModel | Fraud Model | FraudModelSpecification | Create, Execute, Retrieve, Request | FunctionalRequirements, Testing, Production | 15 |
| FraudResolution | Fraud Resolution | FraudResolutionProcedure | Initiate, Exchange, Update, Retrieve | CaseAnalysis, CaseDetermination, CaseResolution | 9 |
| FuneralPolicy | Funeral Policy | - | - | - | 0 |
| GuidelineCompliance | Guideline Compliance | GuidelineComplianceAssessment | Evaluate, Retrieve, Update, Exchange, Request | - | 5 |
| HedgeFundAdministration | Hedge Fund Administration | HedgeFundAdministrativePlan | Create, Exchange, Notify, Control, Grant, Request, Update, Retrieve | FundAccounting, FundEnrolmentCertification, FundDevelopment, FundInvestor_MiddleandBackOfficeService, FundInflowsandOutflow, FundFinancialReporting, FundManagement, FundPerformanceFee, FundTaxAdministration | 62 |
| ITStandardsAndGuidelines | IT Standards And Guidelines | TechnologyStandardsSpecification | Exchange, Request, Capture, Control, Retrieve, Initiate, Update | DevelopmentToolingandEnvironment, ITPoliciesandGuidelines, ProductTestingandDeploymentMechanisms, ProductionPlatformsandInfrastructure, ProductionEnvironmentandSupportServices | 37 |
| IncentiveAccount | Incentive Account | - | - | - | 0 |
| IncentiveProgramDirectory | Incentive Program Directory | - | - | - | 0 |
| InformationProviderOperation | Information Provider Operation | InformationFeedOperatingSession | Initiate, Retrieve, Execute, Update, Control, Request, Exchange, Notify | - | 8 |
| IntellectualPropertyPortfolio | Intellectual Property Portfolio | IntellectualPropertyAdministrativePlan | Initiate, Update, Retrieve | Maintenance, Assignment | 14 |
| InteractiveHelp | Interactive Help | - | - | HelpServiceSelection | 4 |
| InterbankRelationshipManagement | Interbank Relationship Management | BankRelationshipManagementPlan | Create, Update, Control, Exchange, Request, Grant, Retrieve | Contact | 11 |
| InternalAudit | Internal Audit | InternalAuditAssessment | Exchange, Grant, Execute, Initiate, Request, Retrieve, Update | Audit | 14 |
| InternalBankAccount | Internal Bank Account | InternalBankAccountFacility | Control, Capture, Notify, Initiate, Retrieve, Update | Booking | 7 |
| InvestmentAccount | Investment Account | InvestmentAccountFacility | Initiate, Update, Control, Retrieve | DebitandCredit, CorporateAction, Charge, Deposit | 25 |
| InvestmentPortfolioAnalysis | Investment Portfolio Analysis | ManagedInvestmentPortfolioAnalysis | Evaluate, Exchange, Request, Execute, Retrieve | PerformanceAnalysis | 9 |
| InvestmentPortfolioManagement | Investment Portfolio Management | ManagedInvestmentPortfolioFacility | Control, Initiate, Update, Exchange, Execute, Request, Retrieve | Opportunity, FinancialStatusTracking, Trade | 14 |
| InvestmentPortfolioPlanning | Investment Portfolio Planning | ManagedInvestmentPortfolioAgreement | Evaluate, Update, Control, Exchange, Retrieve, Request, Grant | InvestmentTerms | 11 |
| IssuedCertificateDirectory | Issued Certificate Directory | - | - | - | 0 |
| IssuedDeviceAdministration | Issued Device Administration | IssuedDeviceAllocation | Initiate, Update, Control, Exchange, Retrieve | PasswordAssignment, QuestionAssignment, BiometricAssignment, DeviceAssignment, ReaderAssignment, ChequesAssignment, TokenAssignment | 39 |
| IssuedDeviceTracking | Issued Device Tracking | IssuedDeviceState | Control, Initiate, Update, Retrieve | InternalNotification, ExternalReport | 10 |
| KnowledgeExchange | Knowledge Exchange | IntellectualPropertyExchangeOperatingSession | Execute, Initiate, Control, Retrieve, Exchange, Request, Update | IndexingandPublication, CaptureandClassification, Review_RefinementandEditing, Archiving, MaintenanceandAccessAdministration | 23 |
| LeadandOpportunityManagement | Lead and Opportunity Management | LeadandOpportunityProcedure | Update, Initiate, Control, Exchange, Retrieve | Development | 10 |
| Leasing | Leasing | LeasingFacility | Control, Execute, Exchange, Request, Initiate, Retrieve, Update | Charge, Payment, Sweep, Deposit, CollateralAllocation, CorporateAction, IssuedDevice, FinancialStatusTracking, DebitandCredit, Interest, AmountBlock | 44 |
| LeasingItemAdministration | Leasing Item Administration | LeasingItemAdministrativePlan | Capture, Control, Exchange, Grant, Initiate, Retrieve, Request, Update | Assurance, ItemRegistration, Valuation | 20 |
| LegalAdvisory | Legal Advisory | - | - | - | 0 |
| LegalCompliance | Legal Compliance | LegalComplianceAssessment | Exchange, Request, Evaluate, Update, Retrieve | - | 5 |
| LegalEntityDirectory | Legal Entity Directory | LegalEntityDirectoryEntry | Register, Control, Update, Exchange, Request, Execute, Retrieve | Reference, Profile, Associations | 13 |
| LetterofCredit | Letter of Credit | LetterOfCreditTransaction | Control, Exchange, Execute, Initiate, Notify, Request, Retrieve, Update | CustomerCollateralAllocation, LetterofCreditIssuance, CustomerPayment, LetterofCreditDefinitionandPricing, SellerObligationConfirmation, LetterofCreditDemandPayment | 50 |
| Loan | Loan | LoanFacility | Initiate, Update, Control, Retrieve | Charge, Interest, Disbursement, DebitandCredit, Maintenance, Repayment, Modification | 24 |
| LoanSyndication | Loan Syndication | SyndicatedLoanApplicationProcedure | Retrieve, Initiate, Update, Control | - | 4 |
| LocationDataManagement | Location Data Management | LocationDirectoryEntry | Register, Update, Control, Request, Retrieve, Execute, Exchange | Location, Use, Occupancy | 14 |
| ManagementManual | Management Manual | ManagementManualSpecification | Capture, Control, Initiate, Exchange, Retrieve, Request, Update | CompanyMissionandPolicies, EmploymentRelatedProceduresandGuidelines, LegalandRegulatoryObligationsandGuidelines, OperationalSecurityProceduresandGuidelines, OperationalandProductionProceduresandGuidelines, StaffManagementProceduresandGuidelines | 31 |
| MarketAnalysis | Market Analysis | GeneralMarketResearchAnalysis | Evaluate, Execute, Request, Retrieve | CompetitiveAnalysis | 5 |
| MarketDataSwitchOperation | Market Data Switch Operation | InformationFeedSwitchOperatingSession | Update, Initiate, Control, Execute, Retrieve, Request | FeedUpload, InternalPublication, Distribution | 18 |
| MarketInformationManagement | Market Information Management | FinancialMarketInformationAdministrativePlan | Update, Exchange, Execute, Request, Create, Control, Grant, Retrieve | Improvement, Reporting, Consolidation | 16 |
| MarketMaking | Market Making | MarketMakingFacility | Control, Initiate, Exchange, Execute, Notify, Request, Retrieve, Update | Quote, Order, PositionTracking | 29 |
| MarketOrder | Market Order | MarketOrderTransaction | Initiate, Update, Retrieve | Confirmation, Quote, Compliance, TradeInitiation | 8 |
| MarketOrderExecution | Market Order Execution | MarketTradeTransaction | Request, Initiate, Update, Retrieve | Position, TradeInitiation, Quote | 16 |
| MarketResearch | Market Research | GeneralMarketResearchDirectoryEntry | Register, Update, Execute, Request, Retrieve | - | 5 |
| MerchandisingLoan | Merchandising Loan | MerchandisingLoanFacility | Control, Exchange, Execute, Initiate, Retrieve, Request, Update | Billing, Charge, Payment, Sweep, CollateralAllocation, Deposit, IssuedDevice, DebitandCredit, Booking, Interest, FinancialStatusTracking, AmountBlock | 47 |
| MerchantAcquiringFacility | Merchant Acquiring Facility | MerchantAcquiringFacility | Update, Initiate, Control, Request, Retrieve | SupportFacility, Clearing, Charge, Chargeback, Settlement | 19 |
| MerchantRelations | Merchant Relations | MerchantRelationshipAgreement | Request, Exchange, Control, Notify, Retrieve, Update, Evaluate, Grant | OperationalTerm, RegulatoryTerm, LegalTerm | 26 |
| MergersandAcquisitionsAdvisory | Mergers and Acquisitions Advisory | MergersAndAcquisitionAdvice | Exchange, Initiate, Notify, Request, Update, Control, Execute, Retrieve | MergerandAcquisition | 15 |
| MortgageLoan | Mortgage Loan | MortgageLoanFacility | Control, Exchange, Execute, Initiate, Retrieve, Update, Request | Billing, Charge, Payment, Sweep, Deposit, CollateralAllocation, IssuedDevice, DebitandCredit, Booking, Interest, FinancialStatusTracking, AmountBlock | 47 |
| MutualFundAdministration | Mutual Fund Administration | MutualFundAdministrativePlan | Control, Create, Exchange, Grant, Notify, Request, Retrieve, Update | FundAccounting, FundDevelopment, FundEnrolment, FundFinancialReporting, FundInflowsandOutflow, FundInvestor_MiddleandBackOfficeService, FundManagementFee, FundTaxAdministration | 56 |
| NotionalPooling | Notional Pooling | NotionalPoolingFacility | Control, Exchange, Notify, Request, Initiate, Retrieve, Update, Execute | CashTransfer | 15 |
| OpenItemManagement | Open Item Management | OpenItemProcedure | Control, Request, Retrieve, Update, Initiate | Tracking, Repayment | 11 |
| OperationalGateway | Operational Gateway | OperationalGatewayOperatingSession | Execute, Initiate, Control, Exchange, Request, Notify, Update, Retrieve | InboundMessage, OutboundWithResponse, OutboundMessage | 29 |
| OperationsLog | Operations Log | - | - | - | 0 |
| OrderAllocation | Order Allocation | SecuritiesAllocationProcedure | Exchange, Control, Initiate, Execute, Request, Notify, Retrieve, Update | ApplyOrderAllocationRules, Update(PartiallyCompleted)MarketOrder | 22 |
| PartnerAdministration | Partner Administration | - | - | - | 0 |
| PartnerAgreement | Partner Agreement | PartnerAgreement | Exchange, Update, Control, Evaluate, Request, Grant, Retrieve | LegalTerm, RegulatoryTerm, PolicyTerm | 16 |
| PartnerManagement | Partner Management | - | - | - | 0 |
| PartyAssetDirectory | Party Asset Directory | - | - | AssetProperties, AssetEstimatedValue, AssetInsurance, AssetMaintenance | 12 |
| PartyAuthentication | Party Authentication | PartyAuthenticationAssessment | Update, Evaluate, Exchange, Execute, Request, Grant, Retrieve | Password, Question, Document, Device, Biometric, Behavior | 19 |
| PartyLifecycleManagement | Party Lifecycle Management | PartyRelationshipAdministrativePlan | Initiate, Update, Control, Exchange, Execute, Request, Retrieve | Qualification, Documentation, Precedents, IdentityProofing | 15 |
| PartyReferenceDataDirectory | Party Reference Data Directory | PartyReferenceDataDirectoryEntry | Register, Control, Update, Retrieve, Request, Execute, Exchange | Demographics, Reference, Associations, BankRelations | 17 |
| PartyRoutingProfile | Party Routing Profile | PartyState | Initiate, Request, Update, Retrieve, Control, Execute | Status, Rating, Alert | 18 |
| PaymentOrderInitiation | Payment Order Initiation | PaymentOrderInitiationTransaction | Initiate, Update, Retrieve | Compliance, Confirmation, OrderInitiation | 7 |
| PaymentRail | Payment Rail | PaymentRailOperatingSession | Control, Exchange, Execute, Initiate, Notify, Request, Retrieve, Update | InboundTransaction, OutboundTransaction, PaymentAccountReconciliation, PaymentClearingandSettlement | 36 |
| PointofService | Point of Service | PointofServiceOperatingSession | Update, Initiate, Control, Execute, Request, Retrieve | Assisted, Automated, Interaction, Inventory, CashPosition | 23 |
| PositionKeeping | Position Keeping | FinancialPositionLog | Initiate, Update, Control, Retrieve | FinancialTransactionCapture | 7 |
| PositionManagement | Position Management | FinancialPositionState | Initiate, Update, Control, Request | TrialTransaction, TransactionApplication | 10 |
| PrivatePlacement | Private Placement | PrivatePlacementFacility | Exchange, Execute, Control, Initiate, Notify, Request, Retrieve, Update | Placement, Maintenance, InstrumentDesign | 29 |
| ProcessingOrder | Processing Order | ProcessingOrderProcedure | Control, Exchange, Execute, Initiate, Notify, Request, Retrieve, Update | - | 8 |
| ProductCombination | Product Combination | ProductCombinationFacility | Control, Exchange, Execute, Initiate, Retrieve, Request, Update | Fulfillment, TransferPricing, SupportFacility | 21 |
| ProductDeployment | Product Deployment | ProductandServiceDeploymentDevelopment | Create, Update, Exchange, Control, Capture, Request, Grant, Retrieve | Systems, ITOperations, HROperations, SalesandMarketing, Servicing, Production, ProductionSupport | 36 |
| ProductDesign | Product Design | ProductorServiceSpecification | Create, Execute, Request, Retrieve | FunctionalRequirements, Testing, Production | 15 |
| ProductDirectory | Product Directory | ProductDirectoryEntry | Update, Register, Request, Retrieve | Operations, SalesandMarketing, Servicing, Production | 16 |
| ProductExpertSalesSupport | Product Expert Sales Support | SalesSpecialistSupportAdministrativePlan | Retrieve, Create, Update, Request | Assignment | 10 |
| ProductInventoryDistribution | Product Inventory Distribution | ProductInventoryDistributionAdministrativePlan | Capture, Control, Exchange, Grant, Initiate, Retrieve, Update, Request | Oversight, Distribution, Mailing, Provisioning | 24 |
| ProductInventoryItemManagement | Product Inventory Item Management | ProductInventoryAllocation | Update, Request, Retrieve | Assignment | 8 |
| ProductMatching | Product Matching | ProducttoCustomerCombinationAssessment | Exchange, Execute, Grant, Evaluate, Retrieve, Update, Request | BankandCampaignAlignment, ProductEligibility, ContextCriteria, ProductTypeSelection | 19 |
| ProductPortfolio | Product Portfolio | ProductPortfolioAnalysis | Evaluate, Update, Request, Retrieve | PerformanceAnalysis | 10 |
| ProductQualityAssurance | Product Quality Assurance | ProductandServiceAssessment | Exchange, Execute, Grant, Initiate, Retrieve, Request, Update | FunctionalConsistencyChecks, ProcessingErrorandIntegrityChecks, ResiliencyandPerformanceChecks, UsabilityChecks | 19 |
| ProductSalesSupport | Product Sales Support | ProductSalesSupportAdministrativePlan | Control, Create, Exchange, Grant, Notify, Request, Retrieve, Update | StaffAssignment, StaffAvailabilityTracking | 20 |
| ProductServiceAgency | Product Service Agency | ServiceProviderAgreement | Control, Evaluate, Exchange, Grant, Request, Notify, Retrieve, Update | LegalTerm, PolicyTerm, RegulatoryTerm | 26 |
| ProductTraining | Product Training | ProductTrainingProcedure | Exchange, Control, Execute, Initiate, Retrieve, Request, Update | ContentDevelopment, ServiceDelivery, ServiceScheduling, ServiceEvaluation | 28 |
| ProductionRelease | Production Release | ProductionSystemAssessment | Evaluate, Exchange, Update, Grant, Retrieve, Request | FunctionalRisk, ProductionRisk, BusinessRisk, OperationalRisk | 14 |
| ProgramTrading | Program Trading | ProgramTradingOperatingSession | Control, Exchange, Execute, Initiate, Notify, Request, Retrieve, Update | ProgramTradeExecution, ProgramTradedPortfolioAlgorithm, ProgramTradedPortfolioMaintenance | 29 |
| ProjectFinance | Project Finance | ProjectFinanceFacility | Control, Execute, Exchange, Initiate, Notify, Request, Retrieve, Update | Placement, Maintenance, Repayment, InstrumentDesign | 36 |
| PromotionalEvents | Promotional Events | PromotionalEventManagementPlan | Request, Grant, Retrieve, Update, Create | MarketTracking, ImpactAssessment, Participation | 18 |
| ProspectCampaignDesign | Prospect Campaign Design | ProspectCampaignSpecification | Execute, Update, Control, Create, Exchange, Capture, Request, Retrieve | - | 8 |
| ProspectCampaignExecution | Prospect Campaign Execution | ProspectCampaignProcedure | Initiate, Control, Execute, Retrieve, Update, Exchange, Request | Execution, CandidateSelection, AnalysisFeedback | 18 |
| ProspectCampaignManagement | Prospect Campaign Management | ProspectCampaignPortfolioManagementPlan | Grant, Request, Retrieve, Create, Update | MarketTracking, CampaignDirection, PerformanceAssessment | 18 |
| PublicOffering | Public Offering | PublicOfferingFacility | Control, Initiate, Execute, Notify, Exchange, Request, Retrieve, Update | Compliance, ItemRegistration, Underwriting, InstrumentDesign, Prospectus, Placement | 50 |
| PublicReferenceDataManagement | Public Reference Data Management | GlobalStandardSpecification | Capture, Control, Initiate, Exchange, Request, Retrieve, Update | GlobalReferenceData | 9 |
| QuoteManagement | Quote Management | QuotationProcedure | Control, Exchange, Execute, Initiate, Notify, Request, Retrieve, Update | MarketQuoteSelection, MarketQuoteRequest | 22 |
| RegulatoryAndLegalAuthority | Regulatory And Legal Authority | RegulatoryAndLegalAuthorityRelationshipManagementPlan | Capture, Exchange, Control, Grant, Retrieve, Request, Initiate, Update | RepresentBankInterests, Troubleshooting, MaintainRelations, EstablishRelations | 25 |
| RegulatoryCompliance | Regulatory Compliance | RegulatoryComplianceAssessment | Retrieve, Evaluate, Request, Update, Capture | - | 5 |
| RegulatoryReporting | Regulatory Reporting | RegulatoryComplianceAdministrativePlan | Update, Request, Retrieve, Create | Consolidation, Authoring, Enquiries | 13 |
| RewardPointsAccount | Reward Points Account | RewardPointsLog | Capture, Control, Exchange, Grant, Initiate, Retrieve, Request, Update | Capture, Expiration | 16 |
| RewardPointsAwardsAndRedemption | Reward Points Awards And Redemption | RewardPointsTransaction | Exchange, Execute, Initiate, Retrieve, Request, Update | Award, Redemption | 14 |
| RewardsDelivery | Rewards Delivery | - | - | - | 0 |
| RewardsInventory | Rewards Inventory | - | - | - | 0 |
| RewardsMenu | Rewards Menu | - | - | - | 0 |
| SalesProduct | Sales Product | ProductandServiceAgreement | Evaluate, Update, Retrieve, Control | OperationalTerm | 9 |
| SalesProductAgreement | Sales Product Agreement | SalesProductAgreement | Evaluate, Update, Control, Exchange, Request, Grant, Retrieve | LegalTerm, RegulatoryTerm, PolicyTerm | 16 |
| SavingsAccount | Savings Account | SavingsAccountFacility | Initiate, Update, Control, Retrieve | Charge, Interest, Sweep, DebitandCredit, Payment, IssuedDevice, Booking, AmountBlock, Deposit | 34 |
| SecuritiesFailsProcessing | Securities Fails Processing | SecurityTradingFailsProcedure | Control, Execute, Exchange, Initiate, Request, Notify, Retrieve, Update | SecuritiesFailAnalysis, SecuritiesFailDetermination | 22 |
| SecuritiesPositionKeeping | Securities Position Keeping | SecuritiesPositionLog | Initiate, Update, Control, Retrieve | SecuritiesTransactionCapture | 7 |
| SegmentDirection | Segment Direction | SegmentStrategy | Update, Request, Create, Exchange, Capture, Retrieve, Grant | Initiative | 13 |
| ServiceDirectory | Service Directory | ServiceDirectoryEntry | Control, Execute, Notify, Register, Request, Retrieve, Update | AccessControlServicing, ArrangementServicing, ProductAccessServicing, RelationshipServicing, ServiceDeliveryServicing, SalesServicing | 43 |
| ServiceProviderOperations | Service Provider Operations | ServiceProviderRegistrationOperatingSession | Retrieve | - | 1 |
| ServicingActivityAnalysis | Servicing Activity Analysis | ServicingRootCauseAnalysis | Request, Execute, Initiate, Update, Retrieve | RootCauseAlgorithm | 8 |
| ServicingEventHistory | Servicing Event History | ServicingEventLog | Initiate, Update, Control, Retrieve | Assignment, Session, Issue, ServicingFacility | 16 |
| ServicingIssue | Servicing Issue | ServicingIssueProcedure | Control, Exchange, Execute, Initiate, Notify, Request, Retrieve, Update | ProductionIssueAnalysis, ProductionIssueDetermination, ProductionIssueResolution | 29 |
| ServicingMandate | Servicing Mandate | ServicingMandateAgreement | Evaluate, Update, Control, Exchange, Request, Grant, Retrieve | CustomerMandate | 13 |
| ServicingOrder | Servicing Order | ServicingOrderProcedure | Initiate, Update, Control, Exchange, Execute, Request, Retrieve | - | 7 |
| SessionDialogue | Session Dialogue | CustomerContactSessionProcedure | Initiate, Update, Control, Exchange, Execute, Request, Retrieve | Query, Authentication, Sales, Offer, ProductorService, Case, Order, Intelligence, History | 35 |
| SpecialPricingConditions | Special Pricing Conditions | SpecialPricingConditionsDirectoryEntry | Control, Exchange, Execute, Initiate, Retrieve, Request, Update | PricingTerms | 10 |
| StandingOrder | Standing Order | StandingOrderFacility | Control, Exchange, Execute, Initiate, Retrieve, Request, Update | StandingOrderPayment | 11 |
| StockLendingandRepos | Stock Lending and Repos | RepoTransaction | Control, Exchange, Execute, Initiate, Notify, Request, Retrieve, Update | RepoTransactionCashTransfer, RepoTransactionInitiation, RepoTransactionSecurityTransfer | 29 |
| SubCustodianAgreement | Sub Custodian Agreement | SubCustodianAgreement | Control, Evaluate, Exchange, Grant, Notify, Request, Retrieve, Update | LegalTerm, PolicyTerm, RegulatoryTerm | 26 |
| SuitabilityChecking | Suitability Checking | SuitabilityAssessment | Evaluate, Update, Exchange, Request, Grant, Retrieve | - | 6 |
| SyndicateManagement | Syndicate Management | SyndicateMembership | Grant, Notify, Control, Request, Register, Retrieve, Update | SyndicateComplianceClauses, SyndicateEligibilityClauses | 13 |
| SyndicatedLoan | Syndicated Loan | SyndicatedLoanFacility | Control, Exchange, Execute, Initiate, Retrieve, Update, Request | Fulfillment, Origination, Syndicate, InstrumentDesign | 24 |
| SystemDevelopment | System Development | ITSystemDevelopment | Update, Create, Control, Request, Exchange, Retrieve | FunctionalSpecification, TechnicalSpecification, SoftwareandDataSpecification, TestingSpecification, UsageSpecification | 31 |
| SystemsAdministration | Systems Administration | ITSystemAdministrativePlan | Capture, Grant, Exchange, Control, Initiate, Retrieve, Update, Request | Assurance, CapacityPlanningandResilience, Configuration, Inventory | 24 |
| TermDeposit | Term Deposit | TermDepositFacility | Initiate, Update, Control, Retrieve | Interest, Charge, Sweep, DebitandCredit, Payments, IssuedDevice, Booking, Rollover, AmountBlock, Deposit | 35 |
| TermDepositFrameworkAgreement | Term Deposit Framework Agreement | TermDepositFrameworkAgreementFacility | Initiate, Retrieve, Update | - | 3 |
| TradeClearing | Trade Clearing | TradeClearingProcedure | Control, Exchange, Execute, Initiate, Notify, Request, Update, Retrieve | MarketTradeConfirmation, MarketTradeFundsandSecurityAvailabilityAssurance, MarketTradeMatching, MarketTradeOutTradeResolution, MarketTradeSettlementInitiation | 43 |
| TradeConfirmationMatching | Trade Confirmation Matching | TradeMatchingOperatingSession | Exchange, Control, Execute, Initiate, Notify, Request, Update, Retrieve | TransactionConfirmationAffirmation, UnmatchedMarketTradeEscalation, TransactionReporting | 29 |
| TradeSettlement | Trade Settlement | TradeSettlementProcedure | Control, Exchange, Execute, Initiate, Notify, Request, Retrieve, Update | MarketTradeCashSettlement, MarketTradeSettlementConfirmation, MarketTradeSecuritiesSettlement | 29 |
| TradeandPriceReporting | Trade and Price Reporting | MarketTradeReportingOperatingSession | Exchange, Control, Execute, Initiate, Notify, Request, Retrieve, Update | TransactionReporting | 15 |
| TraderPositionOperations | Trader Position Operations | TradedPositionOperatingSession | Control, Exchange, Execute, Initiate, Notify, Request, Update, Retrieve | TradeCaptureandReporting, TradeDealBlotter, TradeQuoteandPricing, TraderSecurityPositionManagementandAnalysis, TraderTradingPermissionsandLimits | 43 |
| TradingBookOversight | Trading Book Oversight | TradingPositionManagementPlan | Control, Notify, Update, Exchange, Grant, Request, Retrieve, Create | TradingBookAnalysisandReporting, TradingBookRiskMitigation | 20 |
| TransactionAuthorization | Transaction Authorization | InteractiveTransactionAssessment | Evaluate, Request, Retrieve, Exchange, Update, Execute, Grant | - | 7 |
| TransactionEngine | Transaction Engine | TransactionScheduleFacility | Initiate, Update, Control, Exchange, Execute, Retrieve | - | 6 |
| TrustServices | Trust Services | CorporateTrustServicesFacility | Control, Exchange, Execute, Initiate, Notify, Update, Request, Retrieve | CourtLiaison, LoanAgencyandAdministration | 22 |
| Underwriting | Underwriting | UnderwritingAssessment | Evaluate, Update, Execute, Request, Exchange, Grant, Retrieve | - | 7 |
| UnitTrustAdministration | Unit Trust Administration | UnitTrustAdministrativePlan | Control, Create, Notify, Request, Exchange, Grant, Update, Retrieve | FundAccounting, FundInvestor_MiddleandBackOfficeService, FundEnrolment, FundFinancialReporting, FundManagementFee, FundTaxAdministration | 44 |
| VirtualAccount | Virtual Account | VirtualAccountFacility | Capture, Control, Exchange, Execute, Retrieve, Grant, Request, Initiate, Update | DirectDebit, Payment, Charge, Interest, FinancialStatusTracking, AmountBlock, IssuedDevice, Booking | 42 |
| eBranchManagement | eBranch Management | eBranchChannelManagementPlan | Create, Update, Exchange, Request, Retrieve | MaintenanceAndUpgrades, CapacityPlanning, Troubleshooting | 15 |
| eBranchOperations | eBranch Operations | eBranchChannelOperatingSession | Initiate, Update, Request, Retrieve, Control | Inbound, Outbound | 9 |
| eTradingWorkbench | eTrading Workbench | eTradingWorkbenchOperatingSession | Execute, Exchange, Control, Initiate, Notify, Request, Retrieve, Update | MarketOrderInitiation, MarketOrderQuotation, MarketPriceAnalysis, InvestmentPortfolioValuation | 36 |
