# Future state templates

Every output carries status draft, version, date, an evidence table and a Gaps and open questions section, following the handoff standard. Entries are written without screens or other interface elements.

## To-be journey blueprint (journeys/to-be-journey-blueprint.md)

Keep the phases of the validated as-is blueprint. One answer per cell, with IDs in brackets.

```
| Row | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| Label (unchanged, changed, removed or merged) | <label> | <label> | <label> |
| What the user does now | <answer> [<IDs>] | <answer> | <answer> |
| Features in place | <feature IDs> | <feature IDs> | <feature IDs> |
| Pain points addressed (register IDs only) | <PP-NN> | <PP-NN> | <PP-NN> |
| Backstage change | <answer> | <answer> | <answer> |
```

## Changes, removals and merges (journeys/to-be-changes.md)

```
| Change ID | Phase | Change | Feature that causes it | Pain point IDs | Kind (change, removal or merge) | Reason | Status |
|---|---|---|---|---|---|---|---|
| <CH-NN> | <phase> | <change> | <feature ID> | <PP-NN, or unlinked> | <kind> | <reason> | <blank until reviewed> |
```

## Feature list (features/feature-list.md)

The ID is in the first column and the text in the second.

```
| ID | Feature | Ideas merged | Pain point or job IDs | Fits principles (EP IDs, or To verify) | Evidence tag | Decision on merge | Decided by (role) |
|---|---|---|---|---|---|---|---|
| <FT-NN> | <feature, written as a user outcome> | <idea IDs> | <PP-NN, JB-NN, or unlinked> | <IDs> | <tag> | <merged, kept apart or dropped> | <role> |

## Dropped ideas
| Idea ID | Reason | Decided by (role) |
|---|---|---|

## Exact duplicates removed
| Idea ID removed | Identical to | 
|---|---|
```
