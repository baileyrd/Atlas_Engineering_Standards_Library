# 0002 - Distribute Unix Philosophy Coverage Into Owning Chapters, Audited by a Matrix

**Status:** Accepted. The Robustness sub-decision below is superseded by [ADR-0003](0003-robustness-gets-its-own-requirement.md); everything else stands.

## Context

[ADR-0001](0001-unix-philosophy-as-foundational.md) declared Unix design philosophy load-bearing for Atlas and added Composability and Economy to ATLAS-000 Article III, Mechanism-Not-Policy as Doctrine D11, and four requirements (`ATLAS-PHIL-0100` through `ATLAS-PHIL-0103`) in a Unix Design Heritage subsection of ATLAS-001 Chapter 6.

Auditing the full source philosophy against ATLAS-000 and ATLAS-001 showed the claim was only partly true. Nine of its elements had no requirement behind them:

- Text streams as the universal interface — nothing governed the format at a composition point.
- Everything is a file — nothing asked for a uniform abstraction over resource kinds.
- Representation — nothing preferred data-driven logic over encoded control flow.
- Generation — nothing preferred generated artifacts over hand-maintained ones.
- Diversity — a standards library with no stated deviation path is a "one true way" claim by construction.
- Repair — `ATLAS-CORR-0020` and `ATLAS-FAIL-0010` covered representing and propagating failures, but nothing required a detected fault to surface *promptly* rather than be deferred.
- Transparency — `ATLAS-OBS-0001` covered production telemetry, not designing for inspection.
- Optimization — Doctrine D2 covered architecture-before-optimization and `ATLAS-VAL-0081` covered measurement, but nothing required correctness first.
- Parsimony — `ATLAS-PHIL-0100` covered where new capability goes, not whether a new component should be built at all.

A foundational principle that half the library doesn't implement is decoration, which is the exact failure ADR-0001 set out to prevent.

## Decision

Close all nine gaps, but place each requirement in the chapter that already owns its subject matter rather than growing Chapter 6's heritage subsection into a parallel philosophy library. Chapter 6 keeps only what has no better home: `ATLAS-PHIL-0104` (Reuse Before Construction) and `ATLAS-PHIL-0105` (No Single Prescribed Approach). The rest land in Chapters 11, 14, 16, 18, 24, 26, 29, and 39.

Add [`docs/reference/unix-philosophy-coverage.md`](../reference/unix-philosophy-coverage.md) as the audit artifact: every element of the source philosophy in one column, the requirement carrying it in the other. Robustness is recorded there as deliberately derived — Raymond states it as a consequence of transparency and simplicity, and giving it a fourth identifier alongside `ATLAS-PHIL-0030`, `ATLAS-CORR-0070`, and `ATLAS-OBS-0040` would be the restatement `ATLAS-LANG-0010` argues against.

> **Superseded by [ADR-0003](0003-robustness-gets-its-own-requirement.md).** This paragraph's reasoning is preserved as written, per `ATLAS-GOV-ADR-0010`. It was reversed on review: the derivation explains where robustness comes from, but nothing in the library stated what a component must *do* under conditions its specification never modeled. `ATLAS-CORR-0080` now states it.

## Consequences

- Each rule is now citable where an engineer would already be reading. An argument about a component's wire format lands on `ATLAS-COMP-0030` in the Composability chapter, not on a philosophy chapter forty chapters away.
- The coverage claim is now falsifiable. A retired or reworded requirement leaves a visible empty cell, and the matrix's maintenance rule makes repairing it part of the same pull request.
- Cost accepted: the philosophy is no longer readable in one place. The matrix is the mitigation, and Chapter 6 now points at it explicitly.
- `ATLAS-LANG-0020` (Documented Deviation) gives every `SHOULD` in the library an explicit, recorded escape hatch. This is intended: an unusable standard gets ignored silently, which is worse than one that is deviated from on the record.
- `ATLAS-PHIL-0104` (Reuse Before Construction) is citable against building a component the ecosystem already has — a check that applies to Atlas's own libraries, not only to third-party dependencies.

## Alternatives Rejected

- **Expand Chapter 6 with all nine requirements.** Rejected: it would concentrate the philosophy where it reads well and leave the chapters that govern the actual decisions unchanged — the same decorative outcome, relocated. It also splits subject matter, putting interface design in a philosophy chapter while Chapter 24 stays silent on it.
- **Add only the matrix, mapping gaps to the nearest existing requirement.** Rejected: it documents a gap as coverage. "Nearest existing requirement" for text streams was nothing at all, and stretching `ATLAS-COMP-0010` to mean it would have made the matrix a fiction.
- **Treat the gaps as consumer-gated under `ATLAS-GOV-STD-0001`.** Rejected: consumer-gating governs *new volumes* drafted speculatively. These requirements have a current consumer — ATLAS-000 Article III and ADR-0001, which already assert this philosophy governs Atlas. Closing a gap in an existing foundational claim is not speculative drafting.
- **Copy the source philosophy document into the repository verbatim.** Rejected: it would create a second normative-looking source that drifts from the requirements, in a library whose whole premise is that requirements carry authority. The matrix enumerates every element it checks against, so the audit is self-contained without duplicating the source.
