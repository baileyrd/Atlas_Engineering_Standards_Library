# Requirement ID Registry

This registry is the single source of truth for requirement identifier prefixes across the Atlas Engineering Standards Library. Per ATLAS-CHARTER-0006, identifiers are never reused. This document exists so that no two chapters — in the same volume or across future volumes — independently pick the same prefix.

## Format

```text
ATLAS-<PREFIX>-<NNNN>
ATLAS-<DOMAIN>-<SUBDOMAIN>-<NNNN>
```

- `<PREFIX>` / `<DOMAIN>` is a short, all-caps mnemonic for the owning chapter or topic area, assigned below.
- `<NNNN>` is a zero-padded, four-digit, permanently-assigned number, allocated in blocks of 10 (`0001-0009` for a chapter's first requirements, then `0010`, `0020`, `0030`, ...) so that new requirements can be inserted near related ones without renumbering anything.
- Some domains are **shared families**: a volume-level prefix (e.g. `SEC`) can be extended with a subdomain (e.g. `SEC-CRYPTO`, `SEC-FND`) when more than one chapter or volume needs to allocate under the same domain. Anyone introducing a new subdomain under a shared family MUST register it below before publishing requirements under it.

## Active Prefixes

Derived directly from requirements currently published in [ATLAS-000](../ATLAS-000-foundation-charter.md), [ATLAS-001](../volumes/ATLAS-001-foundation.md), [ATLAS-100](../volumes/ATLAS-100-architecture.md), [ATLAS-200](../volumes/ATLAS-200-versioning.md), [ATLAS-300](../volumes/ATLAS-300-rust-workspace-cargo.md), [ATLAS-500](../volumes/ATLAS-500-security-architecture.md), [ATLAS-600](../volumes/ATLAS-600-engineering-toolchain.md), and [ATLAS-800](../volumes/ATLAS-800-ecosystem-standards.md).

| Prefix | Owning Document | Chapter / Topic | Highest Assigned | Next Free Block |
|---|---|---|---|---|
| `CHARTER` | ATLAS-000 | Charter-level normative requirements | 0007 | 0010 |
| `FND` | ATLAS-001 | Ch. 1-3 — Purpose, Vision, Mission | 0022 | 0030 |
| `PHIL` | ATLAS-001 | Ch. 6 — Engineering Philosophy | 0105 | 0110 |
| `VAL` | ATLAS-001 | Ch. 7 — Core Values | 0091 | 0100 |
| `GOAL` | ATLAS-001 | Ch. 8 — Design Goals | 0111 | 0120 |
| `NONGOAL` | ATLAS-001 | Ch. 9 — Non-Goals | 0090 | 0100 |
| `CORR` | ATLAS-001 | Ch. 10 — Correctness | 0080 | 0090 |
| `CLAR` | ATLAS-001 | Ch. 11 — Clarity | 0030 | 0040 |
| `EXPL` | ATLAS-001 | Ch. 12 — Explicitness | 0030 | 0040 |
| `MOD` | ATLAS-001 | Ch. 13 — Modularity | 0020 | 0030 |
| `COMP` | ATLAS-001 | Ch. 14 — Composability | 0030 | 0040 |
| `DET` | ATLAS-001 | Ch. 15 — Determinism | 0020 | 0030 |
| `OBS` | ATLAS-001 | Ch. 16 — Observability | 0040 | 0050 |
| `SEC-FND` | ATLAS-001 | Ch. 17 — Security (foundational tenet) | 0030 | 0040 |
| `PERF` | ATLAS-001 | Ch. 18 — Performance | 0030 | 0040 |
| `MAINT` | ATLAS-001 | Ch. 19 — Maintainability | 0030 | 0040 |
| `EVOL` | ATLAS-001 | Ch. 20 — Evolvability | 0020 | 0030 |
| `LAYER` | ATLAS-001 | Ch. 21 — Layered Architecture | 0010 | 0020 |
| `BOUND` | ATLAS-001 | Ch. 22 — Boundary Design | 0010 | 0020 |
| `DEP` | ATLAS-001 | Ch. 23 — Dependency Direction | 0010 | 0020 |
| `IFACE` | ATLAS-001 | Ch. 24 — Interface Design | 0020 | 0030 |
| `STATE` | ATLAS-001 | Ch. 25 — State Management | 0010 | 0020 |
| `FAIL` | ATLAS-001 | Ch. 26 — Failure Handling | 0020 | 0030 |
| `RES` | ATLAS-001 | Ch. 27 — Resource Management | 0010 | 0020 |
| `SPEC` | ATLAS-001 | Ch. 28 — Specification-Driven Development | 0030 | 0040 |
| `AUTO` | ATLAS-001 | Ch. 29 — Automation | 0020 | 0030 |
| `VERIFY` | ATLAS-001 | Ch. 30 — Validation | 0010 | 0020 |
| `COMPAT` | ATLAS-001 | Ch. 31 — Compatibility | 0010 | 0020 |
| `LIFE` | ATLAS-001 | Ch. 32 — Lifecycle Management | 0031 | 0040 |
| `KNOW` | ATLAS-001 | Ch. 33 — Knowledge Preservation | 0010 | 0020 |
| `GOV-STD` | ATLAS-001 | Ch. 34 — Standards Process | 0020 | 0030 |
| `GOV-RFC` | ATLAS-001 | Ch. 35 — RFC Process | 0020 | 0030 |
| `GOV-ADR` | ATLAS-001 | Ch. 36 — Architecture Decision Records | 0010 | 0020 |
| `GOV-CHANGE` | ATLAS-001 | Ch. 37 — Change Management | 0010 | 0020 |
| `GOV-REVIEW` | ATLAS-001 | Ch. 38 — Review Process | 0064 | 0070 |
| `LANG` | ATLAS-001 | Ch. 39 — Requirement Language | 0020 | 0030 |
| `TERM` | ATLAS-001 | Ch. 40 — Terminology | 0010 | 0020 |
| `DOC` | ATLAS-001 | Ch. 41 — Document Conventions | 0010 | 0020 |
| `FUTURE` | ATLAS-001 | Ch. 42 — Future Evolution | 0010 | 0020 |
| `ARCH` | ATLAS-100 | Ch. 1-6 — Runtime/Domain Authority through Backend/Platform Adapters | 0110 | 0120 |
| `EVS` | ATLAS-200 | Ch. 1-6 — Versioning Philosophy through Release Mechanics | 0051 | 0060 |
| `EVS-PROTOCOL` | ATLAS-200 | Ch. 7 — Protocol Versioning | 0060 | 0070 |
| `RWC` | ATLAS-300 | Ch. 1-7 — Workspace Coordination through Cargo Feature Architecture | 0200 | 0210 |
| `SEC-THREAT` | ATLAS-500 | Ch. 1 — Threat Modeling | 0020 | 0030 |
| `SEC-BOUNDARY` | ATLAS-500 | Ch. 2 — Trust Boundaries, Untrusted Data, and Zero Trust | 0080 | 0090 |
| `TOOL` | ATLAS-600 | Ch. 1-10 — Repository/Branching Model through Exact Rust Toolchain Selection | 0380 | 0390 |
| `STD-DIAG` | ATLAS-800 | Ch. 1 — Diagnostic Correlation | 0070 | 0080 |

## Shared Domain Families

A shared family is a prefix that multiple documents allocate under, each with its own subdomain suffix. Registering here reserves the subdomain; it does not require the requirements to exist yet.

| Family | Subdomain | Reserved By | Status |
|---|---|---|---|
| `SEC` | `SEC-FND` | ATLAS-001 Ch. 17 | Active |
| `SEC` | `SEC-THREAT` | ATLAS-500 Ch. 1 | Active |
| `SEC` | `SEC-BOUNDARY` | ATLAS-500 Ch. 2 | Active |
| `SEC` | `SEC-CRYPTO`, `SEC-AUTH`, `SEC-IDENTITY`, `SEC-KEY`, `SEC-SUPPLY` | ATLAS-500 (Draft — see its Deferred section) | Reserved, not yet in use |
| `EVS` | `EVS-PROTOCOL` | ATLAS-200 Ch. 7 | Active |
| `EVS` | `EVS-API`, `EVS-ABI`, `EVS-SCHEMA` | ATLAS-200 (Draft — see its Deferred section) | Reserved, not yet in use |
| `STD` | `STD-DIAG` | ATLAS-800 Ch. 1 | Active |

When a new volume needs a security-, versioning-, or ecosystem-standard-adjacent requirement group, it MUST extend the applicable `SEC`, `EVS`, or `STD` family with a new subdomain registered here rather than inventing an unrelated prefix.

## Reserved Prefixes for Seed Volumes

These volumes have no published requirements yet (`Status: Seed` — see `ATLAS-GOV-STD-0001`). The short names below are proposed in each volume's metadata table and reserved here to prevent collision once a real trigger promotes the volume to Draft. They are not normative until then.

| Prefix | Volume | Title |
|---|---|---|
| `SDK` | ATLAS-400 | Volume V — SDK Architecture |
| `PLUG` | ATLAS-700 | Volume VIII — Plugin and Extension Architecture |
| `REF` | ATLAS-900 | Volume X — Reference Architectures |

## Maintenance Rule

Whenever a PR adds a new requirement chapter or a new prefix/subdomain, it MUST update this registry in the same PR. A PR that introduces an `ATLAS-<PREFIX>-<NNNN>` identifier not listed here (or reuses a "Next Free Block" number without incrementing it) should be treated as incomplete review, per CONTRIBUTING.md.
