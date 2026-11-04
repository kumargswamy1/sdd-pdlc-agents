# Journey templates

Every output carries status draft, version, date, an evidence table and a Gaps and open questions section, following the handoff standard. The layout follows the IBM As-is Scenario Map: phases as columns and rows for doing, thinking and feeling. Entries are written without screens, buttons or other interface elements.

## Journey scope (journeys/journey-scope.md)

```
| Persona | Journey | Trigger (where it starts) | Outcome (where it ends) | Chosen by (role) | Agreed with | Date |
|---|---|---|---|---|---|---|
| <persona label> | <journey name> | <trigger> | <outcome> | <role, blank until chosen> | <roles> | <YYYY-MM-DD> |

Options considered: <the candidate scopes and the criteria used>
```

## Stage by action grid and annotated map (journeys/stage-action-grid.md, as-is-journey-map.md)

Each cell holds one answer, with item IDs in brackets. Doing is Evidence. Thinking and feeling are Inference.

```
| Row | Phase 1: <name in the user's words> | Phase 2: <name> | Phase 3: <name> |
|---|---|---|---|
| Doing | <answer> [<item IDs>] | <answer> [<IDs>] | <answer> [<IDs>] |
| Touchpoints | <answer> [<IDs>] | <answer> [<IDs>] | <answer> [<IDs>] |
| Tools (by type) | <answer> [<IDs>] | <answer> [<IDs>] | <answer> [<IDs>] |
| Thinking | <answer> [<IDs>] | <answer> [<IDs>] | <answer> [<IDs>] |
| Feeling | <answer> [<IDs>] | <answer> [<IDs>] | <answer> [<IDs>] |
| Pain points (register IDs only) | <PP-NN> | <PP-NN> | <PP-NN> |
| High, low or neither | <label, decided by a person> | <label> | <label> |
| Blank areas | <what we still need to learn> | <...> | <...> |
```

## As-is journey blueprint (journeys/as-is-journey-blueprint.md)

Adds the lanes behind each phase. Tag each cell Evidence, or Assumption when no expert input exists.

```
| Phase | User action | Frontstage (what the user is given) | Backstage (roles, rules, processing) | Support (systems and manual processes) | Physical evidence | Handoff: information that passes and context that is lost |
|---|---|---|---|---|---|---|
| <phase> | <answer> | <answer> | <answer> [<tag>] | <answer> [<tag>] | <answer> | <answer> |
```

## Playback (in the blueprint file)

```
## Playback
- Certain (Evidence entries): <list>
- Gaps (Inference entries, Assumption entries and blank areas): <list>
- Claims to check with participants and experts: <list>
```

## Validated blueprint (journeys/as-is-journey-blueprint-validated.md)

```
Status: draft until signed | Version: <n> | Date: <YYYY-MM-DD>
Signer role: <role, name blank until signed> | Signed on: <YYYY-MM-DD, blank until signed>
Refresh trigger: <what prompts an update, or To verify>

## Corrections made in the walk-through
| Phase | Entry | Correction (correct, keep and mark open, or remove) | Source of the correction | Decided by (role) |
|---|---|---|---|---|

<The corrected grid and blueprint follow.>

## Gaps and open questions
- <list>
```
