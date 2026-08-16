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
