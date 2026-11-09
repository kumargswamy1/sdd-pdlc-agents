# Enterprise Standards Instructions
 
## Purpose
 
This repository uses centrally managed HVE Core agents.
 
The HVE Core agent definitions MUST NOT be modified.
 
Enterprise and project-specific standards are maintained in this
repository and MUST be applied as additional context when generating
or modifying artifacts.
 
## Mandatory Standards for Requirement Agents
 
The following HVE agents MUST apply the banking standards defined
under `.github/rules`:
 
- BRD Builder Agent
- PRD Builder Agent
- Jira BackLog Manager Agent
 
Before generating or modifying an artifact, these agents MUST read:
 
1. `.github/rules/bian-standards/*`
2. `.github/rules/iso-20022-standards/*`
 
Preserve centrally managed HVE agent definitions, canonical templates,
stage boundaries, tracker permissions, and existing approval gates.
 
Read [Financial Standards Routing](rules/financial-standards-routing.md)
and load the references relevant to the current stage and artifact.
Do not assume that a folder reference or wildcard loads its contents.
 
### BIAN references
 
For banking capability or Service Domain mapping, read:
 
- [Validation framework](rules/bian-standards/references/bian-validation-framework.md)
- [Concepts](rules/bian-standards/references/bian-concepts.md)
- [Source registry](rules/bian-standards/references/bian-source-registry.md)
- Relevant rules from [Rule catalogue](rules/bian-standards/references/bian-rule-catalog.md)
- Relevant entries from [Service Domain API index](rules/bian-standards/references/bian-v14-service-domain-index.md)
- Relevant [release changes](rules/bian-standards/references/bian-release-14-changes.md)
 
Read the relevant example for formatting or assessment depth only.
Examples are illustrative, not evidence of the project's requirements.
 
### ISO 20022 references
 
Start with [Master index](rules/iso-20022-Standards/ISO-20022-MASTER-INDEX.md).
 
Then load only applicable material:
 
- [Part 1: Architecture](rules/iso-20022-Standards/ISO-20022-Part1-Architecture.md)
- [Part 2: Payments](rules/iso-20022-Standards/ISO-20022-Part2-Payments.md)
- [Part 3: Cash management](rules/iso-20022-Standards/ISO-20022-Part3-CashMgmt.md)
- [Part 4: Securities settlement](rules/iso-20022-Standards/ISO-20022-Part4-SecuritySettlement.md)
- [Part 5: Testing](rules/iso-20022-Standards/ISO-20022-Part5-TestingGuide.md)
  when defining or reviewing validation and tests.
 
Treat these local documents as guidance. Verify standards-specific claims
against the selected official definitions and approved usage profiles.
Do not assume the local documents cover every ISO 20022 business area.
 
## Establish Applicability and the Project Baseline
 
Evaluate BIAN and ISO 20022 separately.
 
Reuse an approved project baseline when available. Otherwise identify
missing decisions and request confirmation of:
 
- Banking process, participants, jurisdiction, and integration scope
- Target BIAN release
- Applicable ISO 20022 message definitions and exact versions
- Market, scheme, or bank-specific usage profile
 
The local BIAN references target v14.0; this is a reference baseline,
not automatic approval to migrate or adopt that release.
 
A local guide's document version is not an ISO message version.
 
Record applicability, baseline, and their sources in existing supported
artifact sections. Distinguish Not Applicable from insufficient evidence.
 
## Apply BIAN by Responsibility, Not Name Similarity
 
For each material banking capability:
 
1. Identify the business outcome, behavior, asset, and lifecycle.
2. Compare at least two plausible Service Domain candidates when available.
   Explain rejected alternatives and any insufficient candidate evidence.
3. Evaluate documented responsibilities, Control Record, Behavior Qualifiers,
   and operations before selecting a mapping.
4. Check renamed, obsolete, replaced, or unavailable artifacts against the
   target release.
5. Keep business capabilities, Service Domains, process steps, microservices,
   and deployment units distinct.
 
The Service Domain API index proves only the structural metadata it contains.
It does not establish Business Area, Business Domain, Functional Pattern,
capability relationships, or first-order connections.
 
Cite authoritative evidence for those attributes or mark them Unverified.
Label inference from Control Record names as BIAN-derived, not Official BIAN.
Never fabricate endpoints for domains without published operations.
 
BSE-* rule identifiers are internal catalogue identifiers, not BIAN IDs.
 
## Apply ISO 20022 by Business Exchange and Selected Definition
 
Identify the business exchange, sender, receiver, direction, trigger,
and expected outcome before selecting a message or family.
 
Verify the selected message identifier, version, namespace, root element,
field paths, cardinality, data types, code lists, and header requirements
against approved authoritative sources.
 
Distinguish:
 
- Message-schema requirements
- Market or scheme usage-profile requirements
- Regulatory requirements
- Bank-specific business rules
- Implementation recommendations
 
Do not infer mandatory rules from examples, numerical message ranges,
generic field tables, or test snippets.
 
A BIAN-to-ISO mapping requires its own evidence. Use official ISO-extended
BIAN annotations where applicable; otherwise label it a proposed integration
mapping.
 
## Standards Traceability and Validation
 
Preserve existing requirement, AC, specification, task, and test identifiers.
 
For each applicable mapping record:
 
| Requirement / AC ID | Standard / release / profile | Mapping / element | Source locator | Evidence type | Validation status | Gap / decision |
|---------------------|------------------------------|-------------------|----------------|---------------|-------------------|----------------|
 
Use the established BIAN evidence and finding labels. Distinguish mapping
status from demonstrated implementation alignment.
 
Where relevant, include Business Area, Business Domain, Service Domain,
Control Record, Behavior Qualifier, operation, ISO business concept,
message definition, and exact element path. Do not guess missing fields.
 
Acceptance criteria must state the condition, observable result,
applicable rule source, and evidence required to pass. Add standards-related
scenarios only within approved scope; raise proposed scope changes for review.
 
Separate schema validation, usage-profile validation, business-semantic
validation, and integration checks. Record tools, versions, inputs, results,
and checks not executed. Schema success alone does not prove conformance.
 
If evidence is missing, preserve:
- BIAN Mapping: Requires Review
- ISO 20022 Mapping: Requires Review
 
Generic drafting may continue with explicit unresolved assumptions.
Do not publish unresolved mappings as approved or claim unsupported conformance.
 
Carry the baseline, mappings, evidence, deviations, and validation expectations
through downstream handoffs. Pass relevant context explicitly to any permitted
subagent; do not assume automatic inheritance.
 
Internal alignment assessments are not BIAN certification or ISO 20022
implementation conformance certification.