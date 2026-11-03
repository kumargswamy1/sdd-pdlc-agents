# Versioning Standards

## API Versioning
- Version public APIs under `/api/v1`.
- Breaking changes require a new major API version.
- Additive changes should be backward compatible.
- Maintain an inventory of public, partner, and internal APIs with owner, consumers, data classification, lifecycle status, support window, and deprecation notice.
- Require consumer-impact analysis and contract compatibility checks before changing published interfaces. Define sunset date, migration guide, overlap period, telemetry/usage checks, and rollback or compatibility plan before retirement.
- For event/message schemas, define compatibility rules for producers/consumers, schema registry ownership, unknown-field handling, replay/backfill, and poison-message behavior where applicable.

## ISO 20022 Message Versioning
Apply when an integration exchanges ISO 20022 messages.

This section owns compatibility, coexistence, migration, and retirement policy. Business message requirements and scheme/profile selection belong in `.github/rules/requirement-standards.md`; technical message handling belongs in `.github/rules/architectural-standards.md`.

- Track the ISO 20022 message-definition version, schema version, scheme/market-practice guideline version, and API version as separate contract identifiers. Do not assume that changing one automatically versions the others.
- Treat changes to message definitions, code sets, usage guidelines, or local extensions as integration contract changes. Assess compatibility for senders and receivers and document any field, cardinality, or semantic changes.
- Define the supported-version policy, coexistence period, rejection behavior for unsupported versions, migration plan, and retirement date with the relevant scheme and integration owners.
- Keep the exact approved schema and usage-guideline artifacts traceable to the release and validation evidence.

## Database Changes
- Use migrations.
- Include tested rollback or forward-recovery guidance for every production-impacting migration; state when rollback is unsafe and how recovery will be performed.
- Never make destructive data changes without explicit approval and backup strategy.
- Use expand/contract migrations for independently deployed producers and consumers. Verify backups, restore procedures, data reconciliation, and migration observability before destructive cleanup.

## FSDM and Data Schema Versioning
Apply when an organization-adopted FSDM or its implementation schema changes.

- Track the FSDM authority/model edition separately from internal logical-model, database schema, API, and ISO 20022 message versions. Do not assume one version change automatically versions the others.
- Assess changes to definitions, identifiers, attributes, relationships, cardinality, constraints, and lifecycle semantics for producer/consumer compatibility.
- Document version support, migration and backfill strategy, coexistence, rollback/recovery, downstream impact, and retirement of obsolete mappings. Destructive data migrations require explicit approval and a tested recovery plan.
- Keep the approved source model, mapping artifacts, migration versions, and validation evidence traceable to the release.

## Release Notes
Every release should include:
- Features.
- Fixes.
- Security changes.
- Data model changes.
- Migration steps.
- Known risks.
- Trace IDs and GitHub issue references.
- API/data/event schema changes, compatibility status, deprecations, rollout sequence, operational impacts, and rollback/recovery notes.
- Security/control changes, exceptions granted or expiring, and required operator/customer actions.

## Commit And PR Traceability
Include relevant issue IDs and major trace IDs in PR descriptions.
