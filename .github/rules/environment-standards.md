# Environment Standards

## Configuration
- Use environment variables for runtime configuration.
- Use centralized secret management for credentials and tokens.
- Do not commit secrets.
- Provide `.env.example` with safe placeholder values only.
- Define a configuration contract for each deployable component: name, type, owner, default, allowed values/range, required environments, reload behavior, and failure behavior when invalid or missing.
- Validate configuration at startup and fail closed for security-critical settings. Do not silently fall back to insecure defaults.
- Separate development, test, staging, and production identities, secrets, endpoints, keys, and data. Production credentials or customer data must not be copied into lower environments.
- Prefer workload identity and short-lived credentials over static secrets when supported. Define issuance, access, rotation, revocation, expiry monitoring, and incident response ownership.
- Store only non-sensitive placeholders in examples. Include required configuration in deployment automation and prohibit manual undocumented production overrides.

## Naming
Use clear prefixes:
- `APP_`
- `AUTH_`
- `API_`
- `FEATURE_`
- `UI_`
- `KYC_`
- `AML_`
- `MARKET_DATA_`
- `NOTIFICATION_`
- `DOCUMENT_`

## Required Documentation
Document:
- Variable name.
- Type, schema, permitted values/range, and default behavior.
- Purpose.
- Required/optional.
- Example safe value.
- Owning system.
- Rotation requirement for secrets.
- Environments where it is used, validation behavior, and change/reload procedure.

## Data Protection
No real customer PII, account numbers, holdings, credentials, tokens, or production integration secrets in local configs or examples.
For application configuration and secret-handling controls, apply the relevant OWASP ASVS requirements selected in `.github/rules/security-quality-standards.md`; record version-qualified control IDs when they are in scope.
- Classify configuration and secrets; prevent secrets from appearing in startup errors, telemetry, crash reports, command output, or support bundles.
- Apply least privilege to runtime identities and validate network egress, storage, and service-to-service access against the approved deployment trust boundaries.
