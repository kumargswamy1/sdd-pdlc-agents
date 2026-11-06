# Secure Coding Best Practices

## Purpose
Embed security into design, implementation, review, testing, deployment, and incident response instead of treating it as a final-stage check.

## 1. Secure by Design
- Perform threat modeling for new systems, major features, trust-boundary changes, and sensitive-data flows.
- Identify assets, actors, entry points, dependencies, abuse cases, and mitigations.
- Minimize attack surface and disable unnecessary features, endpoints, ports, and permissions.
- Use secure framework defaults and document every security-sensitive deviation.
- Classify data and define retention, residency, encryption, and access requirements early.

## 2. Input Validation
- Treat all external input as untrusted, including headers, files, messages, database content, and downstream API responses.
- Validate type, length, range, format, structure, allowed values, and business meaning.
- Prefer allow-list validation over deny lists.
- Enforce server-side validation even when the client validates input.
- Limit upload size, file type, archive expansion, and processing time.
- Normalize input carefully before validation when multiple representations are possible.

## 3. Injection Prevention
- Use prepared statements or parameterized queries for SQL and other query languages.
- Never create commands by concatenating untrusted values.
- Avoid invoking shells or interpreters. If required, use safe APIs and fixed argument lists.
- Validate identifiers that cannot be parameterized against an allow list.
- Use least-privilege database identities and restrict stored-procedure permissions.

## 4. Cross-Site Scripting and Output Encoding
- Use framework-native escaping by default.
- Encode output for the exact context: HTML, attribute, JavaScript, CSS, or URL.
- Do not insert untrusted content into raw HTML or script contexts.
- Sanitize rich HTML with an approved, maintained sanitizer.
- Consider a restrictive Content Security Policy as defense in depth.

## 5. Authentication and Credential Handling
- Use approved identity platforms and standard protocols.
- Prefer managed identity or workload identity over stored credentials.
- Require multifactor authentication for privileged operations where supported.
- Do not implement custom password storage. Use approved identity providers or strong adaptive password hashing.
- Protect authentication flows against enumeration, brute force, replay, and session fixation.

## 6. Authorization and Least Privilege
- Enforce authorization on every protected server-side operation.
- Deny by default and grant the minimum required permissions.
- Validate resource ownership and tenant boundaries to prevent insecure direct object references.
- Separate administrative and application identities.
- Time-bound and review privileged access.
- Do not rely on hidden UI controls or client-side checks as authorization.

## 7. Secret Management
- Never hardcode secrets, tokens, passwords, certificates, or connection strings.
- Store secrets in an approved central secret-management service such as a key vault.
- Restrict secret access by workload identity and least privilege.
- Rotate secrets and certificates and define expiration alerts.
- Prevent secrets from entering source control, build logs, telemetry, images, or artifacts.
- Run secret scanning in developer workflows and CI/CD.

## 8. Cryptography and Data Protection
- Use approved platform cryptographic libraries and algorithms.
- Do not create custom encryption schemes.
- Encrypt sensitive data in transit and at rest.
- Manage keys separately from encrypted data and protect key access.
- Use cryptographically secure random generators for security-sensitive values.
- Avoid exposing sensitive data in URLs, logs, analytics, exception messages, and caches.

## 9. Session, Token, and Browser Security
- Use secure, HttpOnly, and appropriate SameSite cookie settings.
- Use short-lived tokens and validate issuer, audience, signature, lifetime, and required claims.
- Protect state-changing browser requests against CSRF.
- Rotate sessions after privilege changes and invalidate them on sign-out or compromise.
- Do not expose sensitive tokens to untrusted browser scripts.

## 10. API and Service Security
- Require authentication and authorization for protected endpoints.
- Validate content type, payload size, schema, and request rate.
- Use timeouts and bounded retries for outbound calls.
- Prevent server-side request forgery by controlling destinations, protocols, redirects, and DNS behavior.
- Return minimal error details to callers while retaining secure diagnostics internally.
- Apply versioning and deprecation practices without weakening older supported versions.

## 11. Logging, Monitoring, and Response
- Log authentication events, authorization failures, privileged changes, validation failures, and suspicious activity.
- Protect logs from tampering and restrict access.
- Exclude secrets and unnecessary sensitive data.
- Define alerting, triage, classification, remediation, verification, release, and post-mortem processes.
- Maintain a security response plan and clear escalation paths.

## 12. Dependencies, Build, and Supply Chain
- Pin or constrain dependencies and use trusted package sources.
- Generate and retain dependency inventories or SBOMs where required.
- Scan source, dependencies, infrastructure templates, containers, and artifacts.
- Sign and verify artifacts where the delivery platform supports it.
- Protect CI/CD identities and minimize pipeline permissions.
- Patch critical vulnerabilities within the organization's defined service level.

## 13. Security Testing
Automate suitable controls in CI/CD:
- Static application security testing
- Secret scanning
- Software composition analysis
- Infrastructure-as-code scanning
- Container image scanning
- Dynamic application security testing for deployed web applications
- Unit and integration tests for authorization and input validation

Manually review high-risk changes involving authentication, authorization, cryptography, sensitive data, infrastructure exposure, or trust boundaries.

## 14. Cloud and Databricks Considerations
- Apply role-based access control to notebooks, jobs, tables, storage, and compute.
- Use secure network paths and encrypted connections.
- Store workspace secrets in approved secret scopes backed by governed secret stores where possible.
- Prevent secrets and sensitive records from appearing in notebooks and job output.
- Enable audit logging and review access regularly.

## Pull Request Security Checklist
- Threat model updated when trust boundaries or sensitive flows changed.
- Inputs are validated and outputs encoded for context.
- Queries and commands are parameterized.
- Authentication and authorization are enforced server-side.
- Secrets are externalized and managed through approved identities and stores.
- Logs and errors contain no sensitive values.
- Dependencies and artifacts pass required scans.
- Security-critical behavior has automated tests.
- Residual risks and exceptions are documented and approved.

---
Source basis: `Coding_Standard_V1.0.docx`, Security Best Practices, Secure Coding Practices, Security Testing and Validation, Databricks security, peer-review checklist, and CI/CD scanning guidance.
