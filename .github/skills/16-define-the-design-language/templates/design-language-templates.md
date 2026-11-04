# Design language templates

Every output carries status draft, version, date, an evidence table and a Gaps and open questions section, following the handoff standard. Every rule, token and component cites the principle it serves or the place it was observed. Systems and pages appear by ID. Product addresses and organisation names live only in the restricted file named in the local config file.

## Existing system survey (language/existing-system-survey.md)

```
Asked on: <YYYY-MM-DD> | Asked of (role): <role>

| ID | Generic name | Kind (design system, live product, token export or other) | Platform | How it can be viewed (connection, view, export, saved pages or screenshots) | Owner role | Edition in use (version) | Date | Evidence tag |
|---|---|---|---|---|---|---|---|---|
| <S-NN> | <name> | <kind> | <platform> | <how> | <role> | <version, or To verify> | <YYYY-MM-DD> | Evidence |

No existing system or live product: <yes or no. If yes, the route is build from scratch>

What each holds
| Source ID | Tokens | Components | Patterns | Content rules | Accessibility rules | Documentation | Structure (levels, names, modes) | Out of reach |
|---|---|---|---|---|---|---|---|---|

Token file check (build_dtcg.py --check): <result, or no token file>
```

## Currency report (language/currency-report.md)

```
| Source ID | Edition in use | Latest edition found | Where the latest was found | Date of each |
|---|---|---|---|---|

Changes between the two: <list, or To verify if the source gives no edition information>

Drift
| Direction | Item | Where seen |
|---|---|---|
| On the live product, not in the system | <value or component> | <page ID> |
| In the system, not used on the product | <value or component> | <source ID> |

Components the screens need that the system lacks: <SC-NN and component>
Rules that conflict with the experience principles: <rule and EP-NN>
```

## Design language decision (language/design-language-decision.md)

```
| Option | Fit to principles | Fit to brand and platform standards | Cost | Upkeep effort | Where the team would depart |
|---|---|---|---|---|---|
| Adopt as it is | | | | | |
| Update to the latest edition | | | | | |
| Adapt | | | | | |
| Derive from the live product | | | | | |
| Build from scratch | | | | | |

Route chosen: <blank until a person decides> | Decided by (role): <role> | Date: <YYYY-MM-DD>
Role that approves departures from an inherited system: <role, blank until named>
```

## Pages sampled and observed values (derive route only)

```
language/pages-sampled.md
| Page ID | Why included (journey, component type or state) | Capture date | Method (source, stylesheets or screenshots) | Capture confirmed as permitted by (role) |
|---|---|---|---|---|

language/observed-values.csv  (written by extract_css_values.py, one row for each value)
kind,value,count,sources,property,name
```

## Foundations (language/foundations.md)

The ID is in the first column and the rule in the second.

```
| ID | Rule | Foundation (colour, type, spacing, grid, icon or motion) | Principle it serves | Brand or platform standard it follows | Where it comes from (system, observed values or principles) | Decided by (role) |
|---|---|---|---|---|---|---|
| <FD-NN> | <rule> | <foundation> | <EP-NN> | <standard> | <source> | <role> |
```

## Token structure (language/token-structure.md)

```
Default structure (figma-tokens):
Levels: primitive (raw values only), semantic (alias a primitive), component (alias a semantic or a primitive token)
Resolution order for a component value: component token, then semantic token, then primitive token. If none exists, create the token first.

| Collection | Domain | Naming pattern | Modes | Types |
|---|---|---|---|---|
| Colour Styles | Colour primitives | Colour Styles/{Category}/{Hue}/{Hue} {Step} | Light, Dark | color |
| Colour Tokens | Colour semantic and component | color_{context}/{role} | Light, Dark | color |
| Spacing | Spacing scale | spacing_size_{N} | Lg, Md, Sm | dimension |
| Typography | Font, size, weight, line height | <pattern> | Lg, Md, Sm | fontFamily, dimension, fontWeight, number |
| Icon Sizes | Icon dimensions | <pattern> | Sm, Md, Lg | dimension |
| Radius | Corner radius | radius-size/radius_size_{size} | one | dimension |
| Stroke | Line widths | stroke_width/stroke_width_{size} | one | dimension |
| Elevation | Shadow, scrim and opacity | <pattern> | Light, Dark | color, number, shadow |
| Motion | Duration and easing | motion-duration/{name}, motion-easing/{name} | one | duration, cubicBezier |

Colour steps are anchored to contrast against white. A step is never used for a purpose beyond its clearance.
Adapted to the existing system: <differences in names and modes, or none>
Decided by (role): <role> | Date: <YYYY-MM-DD>
```

## Token table (language/tokens.csv)

One row for each token. Group names and the token name are separated by a slash. An alias is written {path/of/token}.

```
path,level,type,value,mode,description,source,evidence,confidence
Colour Styles/Primary Colour/Blue/Blue 60,primitive,color,#0a5ba8,Light,,P01,Evidence,High
color_text/primary,semantic,color,{Colour Styles/Neutral Colour/Grey/Grey 100},all,Body text,,,
color_button-bg/primary_default,component,color,{color_text/primary},all,,,,
spacing_size_8,primitive,dimension,8px,all,,P01,Evidence,High
motion-duration/fast,primitive,duration,200ms,all,,,,
motion-easing/ease-in-out,primitive,cubicBezier,"0.4,0,0.2,1",all,,,,
```

Allowed levels: primitive, semantic, component.
Allowed types: color, dimension, fontFamily, fontWeight, duration, cubicBezier, number, strokeStyle, typography, shadow, border.
Colour is #rgb, #rrggbb or #rrggbbaa. Dimension is a number with px or rem. Duration is a number with ms or s. Font weight is a number from 1 to 1000.
A typography, shadow or border value is a JSON object, and a shadow may be a list. At the semantic and component levels every part holds an alias, except inset and style.

## DTCG token files (tokens/)

```
tokens/design-tokens.<mode>.tokens.json   one file for each mode, or design-tokens.tokens.json when there is one mode
Format: DTCG 2025.10, extension .tokens.json
Written by: build_dtcg.py. Each token carries $type, $value, an optional $description and $extensions with the provenance (source, evidence, confidence and level).
```

## Token validation report (language/token-validation.md)

```
Run on: <YYYY-MM-DD> | Command: <build_dtcg.py command, with file names>
Result: <output of the script, pasted in full>
Errors sent back: <error and where it went (step 10 or a person)>
Existing token file check: <result, or none>
Validated by an official DTCG tool: <yes, no or To verify>
```

## Components (language/component-library.md, component-checks.md)

```
| ID | Component | Purpose | Attributes | States (default, hover, focus, disabled, error) | Tokens used | Screens that need it | Principle it serves | Kept, renamed or added |
|---|---|---|---|---|---|---|---|---|
| <CP-NN> | <name> | <purpose> | <attributes> | <states> | <token paths> | <SC-NN> | <EP-NN> | <decision> |

Reusability check
| Component ID | Has name | Has purpose | Has attributes | Has every state | Fixed values found (not tokens) | Gap |
|---|---|---|---|---|---|---|
```

## Content standard (language/content-standard.md)

```
| Rule ID | Rule | Example | Source of the wording (users' words, existing system or product page ID) |
|---|---|---|---|
| <CS-NN> | <voice, tone, terminology or microcopy rule> | <example> | <source> |

Error message pattern: <what happened, then what to do>
Button label pattern: <a specific verb>
Terminology: <concept, name chosen, names never used>
```

## Accessibility standard (language/accessibility-standard.md)

```
Target: <for example WCAG 2.1 level AA> | Set by (role): <role> | Date: <YYYY-MM-DD>
Lowering the target needs approval from: <role>

| Check ID | Applies to (component type) | Check | How it is checked | Result recorded where |
|---|---|---|---|---|
| <AC-NN> | <type> | <check> | <method> | <file> |
```

## Usage guidelines and patterns (language/usage-guidelines.md, pattern-library.md)

```
| Component ID | Context of use | Do | Don't | Example | Approved by (role) |
|---|---|---|---|---|---|

| Pattern ID | Pattern | Components | Screens where it repeats |
|---|---|---|---|
| <PT-NN> | <pattern> | <CP-NN> | <SC-NN> |
```

## Application gaps (language/application-gaps.md)

```
| Gap ID | Sample screen | Where the system has no token, component or rule | Options (add, exception or raise a request) | Decision | Decided by (role) |
|---|---|---|---|---|---|

Role that approves changes after release: <role, blank until named>
```
