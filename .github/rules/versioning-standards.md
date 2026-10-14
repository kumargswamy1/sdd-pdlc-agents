# Versioning Standards

## API Versioning
- Version public APIs under `/api/v1`.
- Breaking changes require a new major API version.
- Additive changes should be backward compatible.

## Database Changes
- Use migrations.
- Include rollback guidance when possible.
- Never make destructive data changes without explicit approval and backup strategy.

## Release Notes
Every release should include:
- Features.
- Fixes.
- Security changes.
- Data model changes.
- Migration steps.
- Known risks.
- Trace IDs and GitHub issue references.

## Commit And PR Traceability
Include relevant issue IDs and major trace IDs in PR descriptions.
