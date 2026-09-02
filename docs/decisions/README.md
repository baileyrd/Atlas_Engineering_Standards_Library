# Architecture Decision Records

Durable records of significant, non-obvious architectural decisions, per `ATLAS-GOV-ADR-0001`. An ADR is never deleted or renumbered; a decision that gets superseded gets a new ADR that references the one it replaces.

Not every decision needs one — only those significant enough to need standalone discoverability outside the pull request or document that made them (see ATLAS-001 Chapter 36 for the distinction between an RFC and an ADR).

## Format

Each ADR states:

- **Context** — the situation that forced a decision.
- **Decision** — what was decided.
- **Consequences** — what follows from it, including costs accepted.
- **Alternatives Rejected** — what else was considered and why it lost.

## Index

| ID | Title | Status |
|---|---|---|
| [0001](0001-unix-philosophy-as-foundational.md) | Unix Philosophy as a Foundational Principle, Not an Addendum | Accepted |
| [0002](0002-unix-philosophy-coverage-distributed.md) | Distribute Unix Philosophy Coverage Into Owning Chapters, Audited by a Matrix | Accepted (Robustness sub-decision superseded by 0003) |
| [0003](0003-robustness-gets-its-own-requirement.md) | Robustness Gets Its Own Requirement | Accepted |
| [0004](0004-program-integrity-governance-scales-by-responsibility.md) | Program-Integrity Governance Scales by Responsibility, Not Headcount | Accepted |
| [0005](0005-promote-atlas-100-from-exercised-architecture-evidence.md) | Promote ATLAS-100 from Exercised Architecture Evidence | Accepted |
| [0006](0006-promote-atlas-300-from-exercised-rust-workspace-evidence.md) | Promote ATLAS-300 from Exercised Rust Workspace Evidence | Accepted |
| [0007](0007-promote-atlas-500-from-exercised-trust-boundary-evidence.md) | Promote ATLAS-500 from Exercised Trust-Boundary Evidence | Accepted |
| [0008](0008-promote-atlas-800-from-exercised-diagnostic-correlation-evidence.md) | Promote ATLAS-800 from Exercised Diagnostic-Correlation Evidence | Accepted |
| [0009](0009-govern-exact-rust-toolchain-selection-by-evidence-need.md) | Govern Exact Rust Toolchain Selection by Evidence Need | Accepted |
| [0010](0010-activate-cargo-feature-strategy-from-unified-workspace-evidence.md) | Activate Cargo Feature Strategy from Unified Workspace Evidence | Accepted |
