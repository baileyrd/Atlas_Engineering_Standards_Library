# ATLAS-NNN - Volume [Roman Numeral] - [Title]

| Field | Value |
|---|---|
| Document ID | ATLAS-NNN |
| Title | Volume [Roman Numeral] - [Title] |
| Short Name | [3-5 letter mnemonic — register in docs/reference/requirement-registry.md] |
| Status | Planned |
| Classification | Normative |
| Scope | [What this volume governs — be specific, not "Entire Atlas Ecosystem" unless it genuinely is] |
| Parent | ATLAS-001 |

## Purpose

[One or two paragraphs: what this volume defines and why it exists as a separate volume from its siblings.]

## Proposed Table of Contents

```text
Chapter 1 [...]
Chapter 2 [...]
```

## Field Definitions

`Short Name`: The mnemonic used as the requirement-ID prefix for this volume (e.g. `FND`, `EVS`). Must be registered in [docs/reference/requirement-registry.md](../reference/requirement-registry.md) before any requirement under it is published.

`Scope`: The systems, artifacts, or processes this volume's requirements apply to. Should be specific enough that a reader can tell whether a given component falls under it.

`Status`: `Planned` (ToC only) → `Draft N.M` (requirements published, still evolving) → `Active` (stable) → `Deprecated` / `Retired` / `Superseded`. This is document-level status, distinct from the per-requirement `Status` field in [requirement-template.md](requirement-template.md).

## Notes

- Once this volume moves from `Planned` to `Draft`, allocate requirement numbers in blocks of 10 per chapter (see the registry for the convention) and add a row to the registry with the highest assigned number.
- Update this volume's entry in [../library-map.md](../library-map.md) and [../../README.md](../../README.md#library-status) when `Status` changes.
