---
description: Security, privacy, quality, and review gates for in-scope PDLC changes.
---

# Security & Quality Standards

## Security
- Assign a security owner and risk tier to each production application and material change. Perform threat modeling for new trust boundaries, sensitive-data flows, privileged actions, external integrations, and financially consequential workflows.
- Enforce authentication on protected routes, actions, and frontend integration calls.
- Enforce authorization using roles, entitlements, account ownership, relationship-manager assignment, and maker-checker rules where applicable.
- Enforce object-, property-, and function-level authorization on every API and workflow. Apply deny-by-default, least privilege, separation of duties, and re-check authorization on the server for every state-changing operation.
- Enforce safe client-side input handling, output encoding, and platform-appropriate XSS/CSRF protections for Flutter and web deployments.
- Apply server-side validation, parameterized data access, safe deserialization, SSRF protections, anti-automation controls for sensitive business flows, and resource limits according to the threat model.
- Never log plaintext PII, account numbers, portfolio holdings, tokens, secrets, or credentials.
- Protect sensitive data in transit and in browser storage according to the approved platform standard.
- Define encryption and key-management requirements by data classification and jurisdiction, including approved algorithms/protocols, key ownership, storage, rotation, revocation, and recovery. Do not invent cryptographic parameters; use approved enterprise profiles.
- Use centralized secret management; no hardcoded secrets.
- Include correlation IDs in logs.
- Audit sensitive actions such as login, profile updates, risk-profile changes, suitability decisions, order submission, approval, cancellation, document access, and data export.
- For an adopted FSDM, classify sensitive attributes and document data owner, authoritative source, permitted purpose, lineage, access controls, retention, and masking requirements. Treat the FSDM as a metadata/model reference, not as evidence that the data itself is approved for every use.
- For ISO 20022 flows, protect complete message payloads as sensitive financial data. Do not log raw payment messages; redact or tokenize sensitive elements in diagnostics, traces, and test reports.
- When parsing ISO 20022 XML, use a hardened parser that disables DTD and external-entity resolution and enforces payload-size, nesting-depth, and resource limits. Verify message signatures only when required by the selected scheme/profile, using its approved validation procedure.

## OWASP Security Baselines
Apply OWASP guidance according to the application surface and risk in scope. This section is the canonical OWASP control-selection and evidence policy for the SDLC rules.

- For web applications and web services, use the [OWASP Application Security Verification Standard (ASVS)](https://asvs.owasp.org/) as the source of testable application-security requirements. Record the adopted ASVS version, target verification level, applicable requirement IDs, and rationale based on risk, data classification, and approved regulatory obligations.
- Use version-qualified ASVS identifiers in requirements, plans, reviews, and evidence, such as `v5.0.0-1.2.5`. Confirm the current adopted edition from the official source; do not rely on an unversioned requirement ID when recording control evidence.
- Record the exact edition/version and official source URL for every OWASP project used. Review adopted editions during security planning and when material application risks or OWASP releases change.
- For APIs, use the [OWASP API Security Top 10](https://owasp.org/www-project-api-security/) to identify relevant API risks, including object-, property-, and function-level authorization, sensitive business-flow abuse, resource consumption, inventory, and unsafe API consumption. Map applicable risks to concrete requirements and tests; the Top 10 is a risk-awareness resource, not proof of conformance or a substitute for ASVS verification.
- Use the [OWASP Top 10](https://owasp.org/www-project-top-ten/) as web-application risk-awareness guidance, not as a complete security control catalog or certification claim.
- For native or hybrid mobile applications, use the [OWASP MASVS](https://mas.owasp.org/MASVS/) and [MASTG](https://mas.owasp.org/MASTG/) where applicable. Record the adopted version/profile and map applicable mobile controls to verification evidence; do not impose mobile-only controls on web or backend-only work.
- When the product itself uses LLM or generative-AI features, use the current [OWASP GenAI Security Project and LLM Top 10](https://genai.owasp.org/llm-top-10/) as supplementary threat-modeling guidance. Apply `.github/rules/ai-agent-safety.md` to the SDLC agents and tool use; neither source replaces the other.
- Select only controls applicable to the change and document exclusions with rationale. A Top 10 checklist or scanner result alone does not establish security or standards conformance. Make conformance claims only when the complete adopted scope has objective review and test evidence.

## Privacy And Compliance
Apply only when in scope:
- Maintain a control applicability record by legal entity, jurisdiction, product, data category, processing purpose, and regulator/framework. Record authoritative source/version, accountable owner, evidence, and exclusions; do not assume one jurisdiction's controls apply globally.
- Thailand PDPA consent and privacy controls.
- KYC and AML checks.
- Suitability and risk profiling.
- Product eligibility restrictions.
- Advisory disclosure and consent capture.
- Data retention and deletion rules.
- Regulatory reporting and audit evidence.
- PCI DSS, SWIFT Customer Security Controls Framework, DORA, BCBS 239, or other sector controls only when the system's data, connectivity, legal entity, or regulatory scope makes them applicable and the control owner confirms the scope.

## Secure Delivery and Vulnerability Management
- Require peer review and automated secret, dependency, static-analysis, and infrastructure-as-code checks in the approved delivery pipeline. Record tool/version, scope, findings, and disposition; a clean scanner run is not proof of overall security.
- Maintain component inventory/SBOM, dependency owners, license/security disposition, supported-version policy, and patch SLAs based on severity and exploitability.
- Define vulnerability intake, triage, remediation deadlines, compensating controls, risk acceptance authority, exception expiry, and customer/regulator escalation where required.
- Protect build and release integrity with controlled identities, artifact provenance/signing where supported, environment separation, and approval gates for production promotion.
- Define security incident response, evidence preservation, notification/escalation ownership, and recovery responsibilities for production systems.

## Quality
- Unit tests are mandatory for each frontend/backend surface requiring changes before implementation handoff. All required tests must pass. Separately enforce an 80% code-coverage target for lines, statements, branches, and functions where supported; Flutter uses executable-line coverage. All layers, including validation, API endpoints, UI components, and utilities, use the same coverage gate unless an approved exception states otherwise.
- Verify actual unit-test execution and native coverage reports. Show separate frontend/backend test counts, coverage metrics, commands, and evidence paths. Failed tests, below-threshold coverage, or missing execution/coverage evidence block implementation completion.
- Apply unit-test and coverage gates only to surfaces requiring changes in the story. If no backend changes are required or made, skip backend unit tests and coverage; apply the same rule to unchanged frontend. Report `NOT_APPLICABLE` with `N/A` metrics and approved scope evidence, without requiring suite output or coverage reports. Missing tasks or conflicting scope cannot justify skipping; separately required integration/API/functional checks still apply.
- Critical business rules require positive and negative tests.
- Integration clients require success, timeout, unavailable, malformed response, and retry/fallback tests.
- For in-scope ISO 20022 integrations, test schema and market-profile validation, mandatory/optional elements, cardinality, code-set validity, unsupported versions, business rejection, duplicate/replayed submissions, retries, and end-to-end reference preservation. Use synthetic or approved-masked fixtures.
- Security tests must cover unauthorized, unauthenticated, cross-customer, and privilege-escalation attempts.
- Performance tests must validate stated SLAs.

## Review Blockers
Critical blockers:
- Hardcoded secrets.
- Plaintext sensitive customer or financial data in logs.
- Missing authorization on protected operations.
- Missing input/output sanitization or unsafe rendering paths.
- Missing audit trail for regulated financial actions.
- Requirement or implementation with no traceability for production-impacting behavior.
