# Environment Standards

## Configuration
- Use environment variables for runtime configuration.
- Use centralized secret management for credentials and tokens.
- Do not commit secrets.
- Provide `.env.example` with safe placeholder values only.

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
- Purpose.
- Required/optional.
- Example safe value.
- Owning system.
- Rotation requirement for secrets.

## Data Protection
No real customer PII, account numbers, holdings, credentials, tokens, or production integration secrets in local configs or examples.
