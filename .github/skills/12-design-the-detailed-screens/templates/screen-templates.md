# Screen templates

Every output carries status draft, version, date, an evidence table and a Gaps and open questions section, following the handoff standard, and names the design system version used. Screens are designed by a person in the team's design tool. These files hold the readiness check, the plan, the references and the checks. Product addresses and organisation names live only in the restricted file named in the local config file.

## Design system readiness (screens/design-system-readiness.md)

```
Checked on: <YYYY-MM-DD> | Checked by: <executor or role>
Mode: <concept prototype or detailed design>
For concept prototype mode, instruction: <tests/prototype-instruction.md, date, role of the person who gave it>
Design language system version used: <version from ia-and-dls-current-version.md> | Status: <approved, draft or missing> | Date: <YYYY-MM-DD>

| Part | Present | Readable | Version | Notes |
|---|---|---|---|---|
| Current-version file | <yes or no> | <yes or no> | | |
| Foundations | | | | |
| Component library | | | | |
| DTCG token files (build_dtcg.py --check result) | | | | |
| Content standard | | | | |
| Accessibility standard | | | | |

Missing, draft or unreachable: <list>
Ready: <yes or no>
If not ready: run 16-define-the-design-language (or 21-maintain-the-design-language if a release is pending).

Decision when not ready (a person): <wait, proceed on the approved part, or exploratory spike> | Decided by (role): <role> | Approver of the exception: <role> | Date: <YYYY-MM-DD>
Exploratory outputs are labelled "exploratory, not referenced to the design system" and are not passed on in H18 or H19.
```

## Existing designs (screens/existing-designs.md)

```
Asked on: <YYYY-MM-DD> | Asked of (role): <role>
No existing designs: <yes or no>

| ID | Generic name | Form (design file in any tool, screenshot or image, live product, code prototype or older version) | How it can be viewed (link, connection or view) | Owner role | Date | Screens or flows it covers | Evidence tag |
|---|---|---|---|---|---|---|---|
| <D-NN> | <name> | <form> | <how> | <role> | <YYYY-MM-DD> | <SC-NN or flow> | <Evidence, or Inference for values read from an image> |
```

## Comparison with the design system (screens/design-reference-comparison.md)

```
| Design ID | Screen or flow | Matches (component, token and pattern IDs) | Deviates (value that differs from a token, component not in the library, layout that breaks a pattern) | Not in the design system | Evidence tag |
|---|---|---|---|---|---|
```

## Standardisation decisions (screens/standardisation-decisions.md)

```
| Design ID | Options (reference only, bring in as it is, standardise, leave out) | Effect on consistency | Decision | Changes needed to standardise | Decided by (role) | Date |
|---|---|---|---|---|---|---|
| <D-NN> | <options> | <effect> | <blank until a person decides> | <list> | <role> | <YYYY-MM-DD> |
```

## Screen plan (screens/screen-plan.md)

The ID is in the first column and the screen name in the second.

```
Information architecture version: <from ia-and-dls-current-version.md> | Design language system version: <version>

| ID | Screen | Mode (concept prototype or detailed design) | Concept proposal ID (concept prototype mode) | Story, job or pain point IDs | Evidence IDs | Principle IDs | Components (CP IDs) | Tokens | Patterns (PT IDs) | Existing design (D IDs) and standardisation decision | States | Build order (decided by a person) | Orphan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <SC-NN> | <screen> | <mode> | <CP-NN or none> | <IDs, never empty> | <IDs> | <EP-NN> | <CP-NN> | <token paths> | <PT-NN> | <D-NN, decision> | <empty, loading, populated, error and others> | <blank until decided> | <yes or no> |

Features excluded because concept testing rejected them: <FT-NN list>
```

## Component, token and pattern requests (screens/component-requests.md)

```
| Request ID | Screen | Kind (component, token or pattern) | Need | Closest item in the design system | Why it does not meet the need | Status (raised, decided) | Decided by (role) |
|---|---|---|---|---|---|---|
```

## Screen links (screens/screen-links.md)

```
| Screen ID | Link to the screen in the design tool | Version of the screen | Built by (role) | Design system version used |
|---|---|---|---|---|
```

## Content fit (screens/content-fit.md)

```
| Screen ID | String | Component | Length | Maximum for the component | Result (fits, overflows or To verify) |
|---|---|---|---|---|---|
```

## State and interaction specifications (screens/state-interaction-specs.md)

```
## <Screen ID> <screen>
Stories: <IDs> | Business rules: <IDs> | Principles: <IDs>

### States
| State | Content | Recovery or next step |
|---|---|---|
| Empty | | |
| Loading | | |
| Populated | | |
| Error | <what happened> | <what to do next> |
| Success | | |

### Behaviour
| Control | Given | When | Then |
|---|---|---|---|

### Accessibility needs
| Need (tab order, focus, alt text, touch size) | Applies to | Source in the accessibility standard |
|---|---|---|
```

## Design system references (screens/design-system-references.csv, reference-check.md)

One row for each component, token or pattern used on each screen.

```
screen,kind,ref,version
<SC-NN>,component,<CP-NN>,<design system version>
<SC-NN>,token,<token path with / between group names, for example color_text/primary>,<version>
<SC-NN>,pattern,<PT-NN>,<version>
```

Support files for the check, written from the design system: a components CSV with an id column, a patterns CSV with an id column, and a screens CSV with a screen column.
reference-check.md holds the output of check_references.py and what was done about each finding (MISSING, STALE or NO REFERENCE).

## Flow files (screens/flow-screens.csv, screens/flow-links.csv, screens/flow-check.md)

```
flow-screens.csv:  screen,role          (role is start, end or step)
flow-links.csv:    from,to
flow-check.md:     the output of check_flows.py, and what was done about each finding
```

## Prototype (screens/prototype.md)

```
Prototype link: <link> | Version: <n> | Date: <YYYY-MM-DD>
Flows wired: <test tasks and key flows> | Flows not wired: <list>
Matches the documentation version: <version>
```

## Prototype build log (screens/prototype-build-log.md), concept prototype mode

```
Built on: <YYYY-MM-DD> | Design system version: <n> | Instruction: <tests/prototype-instruction.md, date>
Code location: <folder named in the local config file> | Stack: HTML and CSS | tokens.css built by tokens_to_css.py: <result>

| Screen ID | Concept proposal ID | Components (CP IDs) | Tokens read from | Simulated data or behaviour | Not built |
|---|---|---|---|---|---|

Accessibility: keyboard operation <checked, how> | focus visible <checked> | target <standard and level>
Requests raised for missing elements: <C-IDs, or none>
Reviewed by a designer (role): <role, blank until reviewed> | Date: <YYYY-MM-DD>
```
