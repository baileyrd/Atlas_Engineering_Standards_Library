# ATLAS-300 - Volume IV - Rust Workspace and Cargo Architecture

| Field | Value |
|---|---|
| Document ID | ATLAS-300 |
| Title | Volume IV - Rust Workspace and Cargo Architecture |
| Short Name | RWC |
| Status | Seed |
| Classification | Normative |
| Scope | Rust workspace layout, crate organization, Cargo manifests, build profiles, and toolchain policy |
| Parent | ATLAS-001 |

## Purpose

Volume IV will define how Atlas uses Rust workspaces, crates, Cargo manifests, feature flags, build profiles, dependency management, MSRV policy, unsafe Rust policy, and reproducible builds.

## Trigger

When Atlas has a second real crate, forcing an actual choice about workspace layout, which crates version in lockstep versus independently (a real, argued precedent for this exists — see the versioning approach documented for a sibling ecosystem, which this volume will draw on rather than invent from scratch), and shared manifest conventions. A single-crate workspace has no grouping decision to make yet.
