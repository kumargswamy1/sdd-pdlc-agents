# Structure templates

Every output carries status draft, version, date, an evidence table and a Gaps and open questions section, following the handoff standard. Participants in findability tests appear by ID only.

## Candidate qualities (principles/candidate-qualities.md)

```
| ID | Candidate quality | Source (vision, objective, pain point, need, job, blueprint or constraint ID) | Evidence tag |
|---|---|---|---|
| <CQ-NN> | <how the experience must feel or behave> | <ID> | Inference |

Sources skipped: <list, with the reason>
```

## Clustered themes (principles/clustered-themes.md)

```
| Theme ID | Theme | Candidate IDs | Evidence item IDs | Decision (keep, reword or cut) | Decided by (role) |
|---|---|---|---|---|---|
```

## Experience principles (principles/experience-principles.md)

The ID is in the first column and the statement in the second. One pattern for every statement. The default is a short statement, then a reason, then an example. The local config file may replace it.

```
| ID | Principle | Reason (evidence IDs) | Example from a real flow | Tested against (screen or flow) | Verdict | A design it would reject | Owner role | Checked again at |
|---|---|---|---|---|---|---|---|---|
| <EP-NN> | <short statement> | <reason> [<IDs>] | <example> | <screen or flow> | <meets, breaks or unclear> | <design> | <role, blank until named> | <step or event> |

Agreed with (roles): <list> | Date: <YYYY-MM-DD, blank until agreed>
```

## Content and function inventory (ia/content-function-inventory.md)

```
| ID | Item | Content or function | Source (blueprint, feature or system) | Owner role | Keep, change or drop | Job it serves |
|---|---|---|---|---|---|---|
| <IT-NN> | <item> | <content or function> | <source> | <role, or no owner yet> | <blank until decided> | <JB-NN> |
```

## Taxonomy and navigation model (ia/taxonomy.md, ia/navigation-model.md)

```
## Taxonomy
| Concept | Name chosen | Where users used the name (item IDs) | Alternatives considered |
|---|---|---|---|

## Hierarchy
<Groups, depth, and steps per key task.>

## Navigation model
| Level (global, local or in-page) | Items | Tasks served | Rule for search, orientation and return |
|---|---|---|---|

## Labels
| Concept | Label in the users' words | Evidence | Checked against the content standard |
|---|---|---|---|
```

## Sitemap, screen inventory and flows (ia/sitemap.md, screen-inventory.md, flow-diagrams.md)

The ID is in the first column and the text in the second.

```
| ID | Screen | What it holds (item IDs) | Story, job or pain point IDs | Entry points | Journey it belongs to |
|---|---|---|---|---|---|
| <SC-NN> | <screen> | <IT-NN> | <IDs, never empty> | <entry points> | <journey> |

Orphan screens: <list, must be empty before sign-off>

Flow for each key journey: <screens in order, with the decision points>
```

## Findability results (ia/findability-results.md)

```
Test run: <tree test or closed card sort> | Confirmed by (role): <role> | Date: <YYYY-MM-DD>
Success level agreed in the local config file: <level>

| Task | Participants (n) | Succeeded | Went wrong at (node) | Revision proposed | Decision | Decided by (role) |
|---|---|---|---|---|---|---|
```

## Information architecture, final (ia/information-architecture.md)

```
Status: draft until signed | Version: <n> | Date: <YYYY-MM-DD> | Changes since the prior version: <summary>
Owner role: <role> | Sign-off role: <role, name blank until signed>
Checked against the principles: <EP IDs with verdict>
<Sitemap, navigation model, taxonomy and screen inventory, by file name and version.>

## Evidence
| Item ID | Claim | Source | Evidence tag | Confidence |
|---|---|---|---|---|

## Gaps and open questions
- <list>
```
