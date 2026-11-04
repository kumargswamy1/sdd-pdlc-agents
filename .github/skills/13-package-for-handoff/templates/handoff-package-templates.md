# Handoff package templates

The handoff file itself follows handoff-template.md. These templates cover the pieces around it.

## Annotated design documentation (design-docs/design-documentation.md)

```
# Design documentation: <title>

Status: draft | Version: <n> | Date: <YYYY-MM-DD> | Changes: <what changed since the prior version, or first version>
Approver: <role, name blank until signed off>

| Screen or section ID | Note | Story or job IDs | Accessibility needs | Evidence item IDs |
|---|---|---|---|---|
| <ID> | <short note, with real content and no placeholders> | <IDs> | <for example tab order, alt text> | <IDs> |

## Gaps and open questions
- <list>
```

## Open issues (handoffs/open-issues.md)

```
| Issue ID | Issue | Raised by (check or person role) | Owner role | Status | Item IDs |
|---|---|---|---|---|---|
| <OI-NN> | <unresolved, deferred or flagged> | <source> | <role> | <open, deferred or flagged> | <IDs> |
```

## Send record (handoffs/send-record.md)

```
| Date | Handoff ID | File and version | Recipients (roles or IDs) | Medium | Comment window ends | Confirmed by (role) |
|---|---|---|---|---|---|---|
| <YYYY-MM-DD> | <H-ID> | <file, version> | <recipients> | <medium> | <YYYY-MM-DD> | <role> |
```

## Send preparation (shown to the person before they confirm)

```
Handoff: <H-ID, title, version>
Recipients: <list>
Content: <file names>
Medium: <from the local config file>
Timing: <send date, and how long receivers have to comment before the review meeting>
Open issues going with it: <count>
Items without evidence going with it: <count>
Confirm: <blank until a person confirms>
```
