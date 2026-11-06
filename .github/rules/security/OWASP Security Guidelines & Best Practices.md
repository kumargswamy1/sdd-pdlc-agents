# OWASP Security Guidelines & Best Practices

## Purpose
A consolidated, implementation-ready OWASP-aligned security baseline covering web applications, APIs, mobile applications, cloud-native workloads, DevSecOps, and AI/agentic systems.

> **Note:** The OWASP Top 10 is a risk-awareness document, not a complete security specification. For testable application-security requirements, use OWASP ASVS alongside the relevant OWASP Cheat Sheets and specialized standards.

---

## 1. OWASP Top 10:2025 for Web Applications

1. **A01:2025 - Broken Access Control**
2. **A02:2025 - Security Misconfiguration**
3. **A03:2025 - Software Supply Chain Failures**
4. **A04:2025 - Cryptographic Failures**
5. **A05:2025 - Injection**
6. **A06:2025 - Insecure Design**
7. **A07:2025 - Authentication Failures**
8. **A08:2025 - Software or Data Integrity Failures**
9. **A09:2025 - Security Logging and Alerting Failures**
10. **A10:2025 - Mishandling of Exceptional Conditions**

---

# 2. Consolidated OWASP Secure-Development Checklist

## A. Secure Design and Threat Modeling

- Document application assets, users, trust boundaries, entry points, data flows, external integrations, and privileged operations.
- Conduct threat modeling during architecture and design, not only before production.
- Identify abuse cases and misuse scenarios alongside normal use cases.
- Apply secure-by-design, secure-by-default, least privilege, defense in depth, fail-safe defaults, separation of duties, and zero-trust principles.
- Define security requirements and acceptance criteria in epics, user stories, BRDs, PRDs, and design specifications.
- Review architectural decisions affecting identity, cryptography, data storage, tenant isolation, network boundaries, and external dependencies.
- Avoid relying on client-side validation or UI restrictions as security controls.
- Minimize the application's attack surface, exposed endpoints, open ports, features, permissions, and stored data.
- Establish explicit security assumptions and validate them through testing.
- Revisit threat models when features, dependencies, data classifications, or deployment architectures change.

## B. Authentication

- Use established identity providers and standard protocols such as OpenID Connect, OAuth 2.0, and SAML where appropriate.
- Require multifactor authentication for privileged and sensitive operations.
- Prefer phishing-resistant authentication such as passkeys or FIDO2 for high-risk scenarios.
- Do not build custom authentication or cryptographic protocols unless absolutely necessary.
- Enforce protection against credential stuffing, brute-force attacks, password spraying, and user enumeration.
- Apply rate limiting, progressive delays, risk detection, and carefully designed account lockouts.
- Store passwords using modern adaptive hashing algorithms such as Argon2id, scrypt, bcrypt, or PBKDF2 with suitable parameters.
- Never store plaintext passwords or reversibly encrypted passwords.
- Use cryptographically secure, single-use, short-lived tokens for password reset and account recovery.
- Avoid security questions based on publicly discoverable information.
- Reauthenticate users before sensitive changes such as password, email, MFA, payment, or privilege changes.
- Rotate or invalidate sessions following password resets, privilege changes, suspected compromise, or logout.
- Do not expose whether an account exists through login, registration, or recovery responses.
- Protect service accounts and machine identities as rigorously as human identities.

## C. Authorization and Access Control

- Enforce authorization on the server for every request.
- Apply deny by default and grant only explicitly required permissions.
- Validate permissions at object, property, function, endpoint, and tenant levels.
- Protect against IDOR and BOLA by verifying that the caller is permitted to access the requested object.
- Never trust object IDs, role names, tenant IDs, ownership flags, or privileges supplied by the client.
- Apply least privilege to users, applications, databases, managed identities, service accounts, and pipelines.
- Separate administrative capabilities from standard user functions.
- Prevent privilege escalation through parameter modification, mass assignment, or hidden endpoints.
- Centralize authorization policy where practical.
- Test both horizontal and vertical privilege-escalation scenarios.
- For multitenant systems, enforce tenant boundaries at every layer, including queries, caching, storage, logs, and messaging.
- Periodically review access rights, stale accounts, privileged roles, and service principals.

## D. Session Management

- Generate session identifiers using a cryptographically secure random generator.
- Never place session IDs or sensitive tokens in URLs.
- Store browser sessions in cookies marked `Secure`, `HttpOnly`, and an appropriate `SameSite` value.
- Regenerate the session identifier after authentication or privilege elevation.
- Enforce idle and absolute session timeouts.
- Invalidate server-side sessions during logout.
- Prevent simultaneous or long-running sessions where the risk requires it.
- Protect state-changing browser requests against CSRF.
- Avoid storing sensitive authentication tokens in browser local storage when a safer cookie-based design is available.
- Do not log session IDs, access tokens, refresh tokens, or authentication secrets.

## E. Input Validation

- Treat all external data as untrusted, including form inputs, headers, cookies, files, database content, queues, partner APIs, and AI-generated data.
- Validate data on the server using positive allowlists wherever possible.
- Validate type, length, format, range, encoding, structure, and business constraints.
- Normalize and canonicalize data before security validation.
- Reject malformed or ambiguous input rather than attempting unsafe correction.
- Use schema validation for JSON, XML, events, messages, and API payloads.
- Apply file-name and path validation to prevent path traversal.
- Do not rely exclusively on regular expressions for complex structured data.
- Validate uploaded file type through content inspection, not only extension or `Content-Type`.
- Enforce request, field, recursion, nesting, and payload-size limits.

## F. Injection Prevention

- Use parameterized queries or prepared statements for SQL, NoSQL, LDAP, and other query languages.
- Never construct commands or queries by concatenating untrusted input.
- Avoid invoking operating-system shells where direct APIs exist.
- Where command execution is unavoidable, use fixed commands and strict allowlists for arguments.
- Apply context-specific output encoding for HTML, JavaScript, CSS, URLs, XML, and other interpreters.
- Use trusted template engines with automatic escaping enabled.
- Prevent server-side template injection by separating templates from user-controlled data.
- Disable dangerous expression-language and deserialization features.
- Do not pass unsanitized input to interpreters, reflection APIs, dynamic evaluation, or code-generation functions.
- Use Content Security Policy as defense in depth, not as the primary XSS control.

## G. Output Encoding and Browser Security

- Encode output according to the destination context.
- Sanitize user-authored HTML with a proven allowlist-based sanitizer.
- Do not insert untrusted data into dangerous DOM APIs such as `innerHTML`, `outerHTML`, or `document.write`.
- Prefer safe DOM APIs such as `textContent`.
- Enforce Content Security Policy with restrictive source definitions and nonces or hashes where applicable.
- Use anti-clickjacking protection through CSP `frame-ancestors`.
- Configure `X-Content-Type-Options: nosniff`.
- Configure an appropriate `Referrer-Policy`.
- Configure `Permissions-Policy` to disable unnecessary browser capabilities.
- Avoid exposing sensitive information in HTML comments, JavaScript bundles, source maps, or client-side configuration.

## H. Cryptography and Data Protection

- Classify data based on confidentiality, integrity, availability, privacy, and regulatory requirements.
- Collect and retain only the data that is actually required.
- Encrypt sensitive information in transit and at rest.
- Use current TLS configurations and validate certificates correctly.
- Do not create custom cryptographic algorithms.
- Use approved, maintained cryptographic libraries.
- Use authenticated encryption modes such as AES-GCM or ChaCha20-Poly1305.
- Avoid obsolete or unsafe algorithms and protocols such as MD5, SHA-1 for security decisions, DES, 3DES, ECB mode, SSL, and outdated TLS versions.
- Generate keys, tokens, salts, nonces, and identifiers using cryptographically secure randomness.
- Store keys in a managed key vault, HSM, or platform-provided secure keystore.
- Separate keys from encrypted data.
- Define key ownership, access policy, rotation, revocation, expiry, backup, and destruction processes.
- Do not hardcode keys, passwords, connection strings, certificates, or API tokens in source code.
- Mask or tokenize sensitive data where full values are unnecessary.
- Securely delete sensitive information when its retention period expires.

## I. Secrets Management

- Use a centralized secret-management service.
- Never commit secrets to source control.
- Scan source code, commits, build artifacts, container images, and logs for exposed secrets.
- Prefer managed identities, workload identities, or short-lived credentials over static secrets.
- Rotate secrets automatically where possible.
- Scope secrets to the smallest required environment and privilege.
- Keep development, test, staging, and production secrets separated.
- Revoke and rotate a secret immediately if exposure is suspected.
- Prevent pull requests, pipeline output, telemetry, and exception messages from disclosing secrets.

## J. API Security

OWASP API Security Top 10:2023 covers BOLA, broken authentication, property-level authorization, resource consumption, function-level authorization, sensitive business flows, SSRF, misconfiguration, inventory management, and unsafe API consumption.

- Authenticate every nonpublic endpoint.
- Enforce object-level, property-level, function-level, and tenant-level authorization.
- Use explicit request and response schemas.
- Prevent mass assignment by binding only approved properties.
- Return only the minimum fields required by the caller.
- Apply pagination and limits to collections.
- Enforce per-user, per-token, per-IP, and per-operation rate limits where appropriate.
- Limit CPU, memory, storage, bandwidth, execution time, and third-party billable operations.
- Prevent automated abuse of sensitive business flows such as purchasing, commenting, registration, account recovery, or reservations.
- Maintain an accurate API and endpoint inventory, including versions, owners, exposure, and deprecation status.
- Retire undocumented, obsolete, beta, and vulnerable API versions.
- Validate webhook authenticity and protect against replay.
- Restrict outbound API calls and validate destinations to prevent SSRF.
- Treat third-party API responses as untrusted input.
- Configure strict connection and response timeouts.
- Do not place secrets or sensitive personal data in query strings.
- Use consistent error responses without internal implementation details.
- Use OAuth scopes and audience restrictions correctly.
- Validate JWT signature, issuer, audience, expiry, algorithm, and relevant claims.
- Never accept unsigned tokens or trust an algorithm selected solely by the token.
- Log API authentication failures, authorization denials, abuse events, and configuration changes.

## K. File Upload and Download

- Allow only explicitly required file types.
- Validate file content, signature, extension, and MIME type.
- Rename uploaded files using server-generated values.
- Enforce file-size, decompression, dimension, and archive-depth limits.
- Store uploads outside the web root.
- Prevent uploaded content from being executed.
- Scan uploaded files for malware where appropriate.
- Use content disarm and reconstruction for high-risk document workflows.
- Prevent ZIP bombs, path traversal, polyglot files, and parser exploits.
- Serve files using safe response headers and controlled content disposition.
- Authorize every file download.
- Do not expose internal storage paths or predictable identifiers.
- Store sensitive files in private storage with short-lived access mechanisms.

## L. Error and Exception Handling

- Handle exceptions centrally and consistently.
- Fail securely and deny access when a security dependency fails.
- Do not expose stack traces, SQL statements, filesystem paths, secrets, internal hostnames, or framework details.
- Return generic errors to users and detailed diagnostic information only to secured telemetry.
- Handle null values, missing fields, invalid states, timeouts, partial failures, concurrency issues, and exhausted resources.
- Roll back incomplete transactions.
- Avoid fail-open behavior for authentication, authorization, validation, or security-policy checks.
- Test negative paths and exceptional conditions deliberately.
- Assign stable correlation IDs that do not contain sensitive information.

## M. Security Logging, Monitoring, and Alerting

- Log authentication attempts, account recovery, authorization failures, administrative operations, security-policy changes, input rejections, and suspicious activity.
- Record who performed an action, what occurred, when it occurred, and the relevant target, without capturing unnecessary sensitive data.
- Protect logs against unauthorized access, modification, deletion, and injection.
- Synchronize system clocks.
- Centralize logs and correlate them across application, API, identity, infrastructure, and data layers.
- Define detection rules and alerts for high-risk events.
- Ensure alerts have owners, severity, escalation paths, and response playbooks.
- Monitor credential attacks, privilege escalation, volume anomalies, destructive operations, and data exfiltration indicators.
- Test whether monitoring and alerting actually detect simulated attacks.
- Define retention policies based on legal, operational, privacy, and investigation requirements.
- Never log passwords, secrets, full tokens, cryptographic keys, sensitive payment data, or unnecessary personal information.

## N. Security Configuration and Hardening

- Maintain secure configuration baselines.
- Disable default accounts, sample applications, debug modes, development consoles, directory listings, and unused features.
- Change default credentials before deployment.
- Apply least privilege to operating systems, containers, databases, and cloud resources.
- Restrict administrative interfaces to trusted networks and identities.
- Keep security headers and CORS policies restrictive.
- Never use wildcard CORS with credentials.
- Separate development, test, and production environments.
- Prevent production data and secrets from being copied into lower environments without appropriate protection.
- Manage infrastructure configuration through version-controlled Infrastructure as Code.
- Scan IaC and deployment manifests for insecure settings.
- Detect configuration drift.
- Perform regular cloud, Kubernetes, container, database, and identity posture reviews.

## O. Software Supply-Chain Security

- Maintain an inventory of direct and transitive dependencies.
- Generate and retain a Software Bill of Materials (SBOM).
- Pin dependency versions and verify integrity.
- Use trusted registries and repositories.
- Scan dependencies for known vulnerabilities and malicious packages.
- Establish remediation SLAs based on exploitability and impact.
- Remove unused dependencies.
- Protect against dependency confusion and typosquatting.
- Review package health, ownership, maintenance status, and provenance.
- Isolate build environments and restrict their network and secret access.
- Protect source-control branches, releases, workflows, runners, and package publishing.
- Require code review for pipeline and build-script changes.
- Sign and verify commits, artifacts, images, and releases where feasible.
- Maintain traceability from source commit to deployed artifact.
- Use reproducible or hermetic builds for higher-assurance systems.
- Continuously monitor deployed components for newly disclosed vulnerabilities.

## P. Secure CI/CD and DevSecOps

- Apply branch protection and mandatory peer review.
- Run secret scanning, SAST, dependency scanning, IaC scanning, and container scanning in CI.
- Add DAST and API security testing in appropriate test environments.
- Define security quality gates for critical and high-severity findings.
- Prevent untrusted pull-request code from accessing privileged runners or production secrets.
- Use isolated, ephemeral build agents where possible.
- Grant pipelines only the permissions required for their function.
- Separate build, approval, and production deployment responsibilities.
- Require explicit approvals for sensitive environments.
- Keep auditable records of build, test, approval, and deployment actions.
- Never print secrets in build logs.
- Sign release artifacts and verify signatures before deployment.
- Include rollback, key revocation, and incident-response procedures in release planning.

## Q. Secure Code Review and Testing

- Review authentication, authorization, validation, cryptography, secrets, data access, business logic, and error-handling changes carefully.
- Use security-focused pull-request checklists.
- Treat generated code and AI-assisted code as untrusted until reviewed and tested.
- Build unit tests for authorization and security-critical business rules.
- Add negative tests, abuse tests, boundary tests, and malformed-input tests.
- Use SAST, SCA, DAST, IAST, fuzzing, API testing, and penetration testing according to risk.
- Do not assume automated scanners provide complete coverage.
- Include manual testing for business-logic vulnerabilities and authorization bypasses.
- Retest remediated findings and prevent regressions.
- Track exceptions and accepted risks with owner, justification, compensating controls, and expiry date.

## R. Privacy

- Apply privacy by design and by default.
- Establish a lawful and documented purpose for processing personal data.
- Collect only necessary information.
- Limit access and retention.
- Provide transparency, consent, and preference controls where required.
- Prevent personal data from appearing in logs, analytics, URLs, and error messages.
- Support correction, deletion, portability, and access requests where applicable.
- Protect backup copies and nonproduction datasets.
- Assess privacy impacts of third-party SDKs, trackers, analytics, AI models, and external processors.
- De-identify or pseudonymize data used for testing and analytics.
- Document cross-border data flows and residency requirements.

---

# 3. Mobile Application Security

OWASP MASVS organizes mobile controls into eight groups: storage, cryptography, authentication and authorization, network communication, platform interaction, code quality, resilience, and privacy.

- Store sensitive data only in platform-provided secure storage.
- Prevent sensitive content from appearing in logs, screenshots, clipboard history, notifications, or backups.
- Use hardware-backed key storage where supported.
- Validate TLS certificates and avoid unsafe trust-manager overrides.
- Secure deep links, app links, intents, exported components, URL schemes, and interprocess communication.
- Protect biometric authentication against bypass and insecure fallback.
- Avoid hardcoded credentials and secrets in application packages.
- Minimize mobile permissions.
- Validate data crossing the application-platform boundary.
- Keep third-party SDKs current and review their privacy behavior.
- Use code signing, integrity verification, obfuscation, and anti-tampering measures according to risk.
- Treat root, jailbreak, emulator, and debugger detection as defense in depth, not as primary authorization controls.
- Test mobile controls using MASTG in addition to static inspection.

---

# 4. AI, LLM, RAG, MCP, and Agentic-System Security

For enterprise copilots, RAG agents, autonomous agents, coding agents, LLM applications, and MCP-based systems:

- Treat prompts, retrieved documents, tool output, model output, and agent-generated code as untrusted.
- Separate trusted system instructions from untrusted user and retrieved content.
- Do not rely on prompt wording as a security boundary.
- Apply authorization before retrieval and again before displaying or acting on data.
- Enforce document-level and chunk-level access control in RAG systems.
- Prevent cross-user and cross-tenant retrieval leakage.
- Minimize the model's tools, permissions, scopes, and accessible data.
- Require explicit approval for destructive, financial, privileged, or externally visible actions.
- Apply deterministic policy checks outside the model.
- Validate model-generated commands, URLs, queries, code, and tool parameters.
- Use allowlists for tools, destinations, operations, file paths, and command arguments.
- Restrict outbound connectivity to prevent SSRF and data exfiltration.
- Sandbox generated code and agent execution.
- Set limits for tokens, steps, execution time, recursion, retries, cost, and resource consumption.
- Prevent uncontrolled agent-to-agent delegation and privilege inheritance.
- Protect system prompts, credentials, connector tokens, model endpoints, and internal instructions.
- Defend against direct and indirect prompt injection.
- Sanitize or isolate retrieved web pages, documents, emails, source repositories, and tool output.
- Do not expose secrets to the model unless strictly required.
- Filter sensitive information before model submission and before output is returned.
- Establish provenance for retrieved content, tools, models, prompts, and generated artifacts.
- Log agent decisions, tool calls, approvals, failures, and policy interventions.
- Red-team prompt injection, data leakage, excessive agency, unsafe tool use, poisoned knowledge, and denial-of-wallet scenarios.
- Maintain human override, kill switch, revocation, and rollback capabilities.
- Evaluate models and agents continuously after prompt, model, tool, or knowledge-base changes.
- Secure MCP servers using strong authentication, authorization, tool allowlisting, input validation, and least-privileged credentials.
- Never assume model output is factually correct, policy-compliant, or safe to execute.

---

# 5. Recommended OWASP Compliance Hierarchy

For an enterprise application, use OWASP resources in this order:

1. **OWASP Top 10:2025** - Risk awareness and common web application risks.
2. **OWASP ASVS 5.0** - Testable web-application security requirements and formal acceptance criteria.
3. **OWASP Cheat Sheet Series** - Implementation-specific secure coding and security guidance.
4. **OWASP API Security Top 10** - API-specific risks and controls.
5. **OWASP MASVS / MASTG** - Mobile-application security requirements and testing.
6. **OWASP GenAI Security guidance** - AI, LLM, RAG, MCP, and agentic-application security.
7. **OWASP SAMM** - Organization-wide secure software development maturity.

## Practical Enterprise Baseline

For most business-critical enterprise applications, a strong baseline is:

- Target **OWASP ASVS Level 2**.
- Address the complete **OWASP Top 10:2025**.
- Apply the **API Security Top 10** for API-based applications.
- Apply **MASVS** for mobile clients.
- Apply **OWASP GenAI Security** guidance for LLM and agentic solutions.
- Implement automated security gates plus manual threat modeling, architecture review, secure-code review, security testing, and penetration testing.

This approach converts OWASP from an awareness exercise into measurable engineering controls that can be incorporated into architecture standards, development standards, pull-request reviews, CI/CD quality gates, and release acceptance criteria.

---

## References

- OWASP Top 10:2025: https://top10.owasp.org/2025/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- OWASP Application Security Verification Standard (ASVS): https://owasp.org/www-project-application-security-verification-standard/
- OWASP API Security: https://owasp.org/www-project-api-security/
- OWASP Mobile Application Security: https://mas.owasp.org/
- OWASP GenAI Security Project: https://genai.owasp.org/
- OWASP SAMM: https://owaspsamm.org/
