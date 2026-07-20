# ATLAS-NNN - Volume [Roman Numeral] - [Title]

| Field | Value |
|---|---|
| Document ID | ATLAS-NNN |
| Title | Volume [Roman Numeral] - [Title] |
| Short Name | [3-5 letter mnemonic — register in docs/reference/requirement-registry.md] |
| Status | Seed |
| Classification | Normative |
| Scope | [What this volume will govern — be specific, not "Entire Atlas Ecosystem" unless it genuinely is] |
| Parent | ATLAS-001 |

## Purpose

[One paragraph: what this volume will define and why it exists as a separate volume from its siblings.]

## Trigger

[The specific, real, current consumer need that promotes this volume from Seed to Draft, per `ATLAS-GOV-STD-0001`. Not "when we get to it" — name the actual crate, service, or subsystem whose existence would require this standard.]

## Field Definitions

`Short Name`: The mnemonic used as the requirement-ID prefix for this volume (e.g. `FND`, `EVS`). Must be registered in [docs/reference/requirement-registry.md](../reference/requirement-registry.md) before any requirement under it is published.

`Scope`: The systems, artifacts, or processes this volume's requirements apply to. Should be specific enough that a reader can tell whether a given component falls under it.

`Status`: `Seed` (purpose + trigger only, no requirements yet, per `ATLAS-GOV-STD-0001`) → `Draft N.M` (requirements published, still evolving) → `Active` (stable) → `Deprecated` / `Retired` / `Superseded`. This is document-level status, distinct from the per-requirement `Status` field in [requirement-template.md](requirement-template.md) and from the artifact lifecycle states in ATLAS-001 Chapter 32.

## Notes

- A Seed volume does not get a full table of contents — a plausible-sounding chapter list for a subsystem that doesn't exist yet is exactly the speculative ceremony `ATLAS-PHIL-0102` exists to prevent. The chapter structure gets designed once the trigger fires and there's a real subsystem to structure it around.
- When the trigger fires, promoting Seed → Draft may itself need an RFC per `ATLAS-GOV-STD-0010` if the promotion involves a non-obvious design decision.
- Once Draft, allocate requirement numbers in blocks of 10 per chapter (see the registry for the convention) and add a row to the registry with the highest assigned number.
- Update this volume's entry in [../library-map.md](../library-map.md) and [../../README.md](../../README.md#library-status) when `Status` changes.
