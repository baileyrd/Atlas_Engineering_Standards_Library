# Requirement Template

```text
Identifier:
Title:
Statement:
Rationale:
Applicability:
Dependencies:
Verification:
References:
Status:
```

## Field Definitions

`Identifier`: Permanent requirement identifier.

`Title`: Short human-readable requirement name.

`Statement`: Normative requirement using `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, or `MAY`.

`Rationale`: Reason the requirement exists.

`Applicability`: Systems, artifacts, processes, or contexts to which the requirement applies.

`Dependencies`: Related requirements, standards, RFCs, or architecture decision records.

`Verification`: How the requirement can be checked through review, static analysis, testing, tooling, certification, or audit.

`References`: Supporting documents.

`Status`: Draft, Active, Deprecated, Retired, or Superseded.

## Retirement Convention

Per `ATLAS-CHARTER-0006`, identifiers are never reused — retiring a requirement means marking it, not deleting or renumbering it. Where a requirement is published in the lightweight heading-plus-statement form (rather than the full template above), mark retirement by appending `(Retired)` to the title and replacing the body with:

```text
Retired; superseded by <canonical ID>, which states the same requirement[, at <reason: charter authority | controlling strength | etc.>]. This identifier remains reserved and MUST NOT be reused (ATLAS-CHARTER-0006).
```

