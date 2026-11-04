# Release templates

Every output carries status draft, version, date, an evidence table and a Gaps and open questions section, following the handoff standard. A release is never marked approved by the skill.

## Ownership (maintenance/ownership.md)

```
| Candidate owner role | Duties | Capacity | Knowledge of the principles | Independence from requesters | Chosen |
|---|---|---|---|---|---|
| <role> | <accept changes, review breaking changes, publish, answer questions> | <note> | <note> | <note> | <blank until a person decides> |

Owner role: <role, blank until named> | Decided by (role): <role> | Date: <YYYY-MM-DD>
```

## Change rules (maintenance/change-rules.md)

```
| Rule | Decision | Decided by (role) |
|---|---|---|
| How a change is requested | <route> | <role> |
| Who reviews a request | <role> | |
| Who approves | <role> | |
| How exceptions are handled | <rule> | |
| What counts as a breaking change | <definition> | |
| Version scheme | <for example major for breaking, minor for additions, patch for fixes> | |
| Migration guidance for breaking changes | <required or not> | |
| How long before a removed item disappears | <period> | |
| Role that may block a release | <role> | |
```

## Changelog (maintenance/changelog.md)

Append only. Never edit or delete an entry.

```
| Version | Date | Change | Request ID | Effect on screens | Breaking | Migration guidance | Approved by (role, blank until approved) |
|---|---|---|---|---|---|---|---|
| <n> | <YYYY-MM-DD> | <change> | <request> | <screens affected> | <yes or no> | <link or none> | <blank until approved> |
```

## Current-version file update (ia-and-dls-current-version.md)

```
Design language system row: version, date, status (draft until approved), approver role, location, one line on what changed.
The prior row moves to the version history table. Nothing is deleted.
```

## Drift check (maintenance/drift-check.md)

```
Done by: <a person, or a separate run a person reviewed> | Date: <YYYY-MM-DD>

| Finding | File or step | Version it cites | Current version | What to do (a person decides) |
|---|---|---|---|---|
| <older version cited, change with no changelog entry, or component change with no version change> | <file> | <n> | <n> | <blank until decided> |
```
