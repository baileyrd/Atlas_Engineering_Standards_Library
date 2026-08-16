# 0003 - Robustness Gets Its Own Requirement

**Status:** Accepted
**Supersedes:** the Robustness sub-decision in [ADR-0002](0002-unix-philosophy-coverage-distributed.md). The rest of ADR-0002 — distributing Unix philosophy coverage into owning chapters, audited by a matrix — stands unchanged.

## Context

[ADR-0002](0002-unix-philosophy-coverage-distributed.md) closed nine Unix philosophy coverage gaps but deliberately left a tenth open. Raymond states Robustness as a consequence — "the child of transparency and simplicity" — so ADR-0002 recorded it as *derived*, arguing that a dedicated requirement would restate `ATLAS-PHIL-0030`, `ATLAS-CORR-0070`, and `ATLAS-OBS-0040` under a fourth identifier, against `ATLAS-LANG-0010` and `ATLAS-PHIL-0102`.

That argument was raised for review and rejected by the maintainer. On re-examination it conflated two different things:

- **Where robustness comes from.** Simplicity and transparency, correctly — that part of the derivation holds and is not in dispute.
- **What a component must do.** Nothing in the library stated this. `ATLAS-CORR-0010` requires validating external input, but validation presumes the valid set was enumerated correctly; it says nothing about the residue — inputs, orderings, and environmental conditions nobody thought to enumerate. `ATLAS-FAIL-0001`, `ATLAS-FAIL-0010`, and `ATLAS-FAIL-0020` govern faults the component *detects*. Neither reaches the case of a component in a state its author never modeled.

The derived framing therefore claimed coverage the library did not have. A matrix row reading "derived" was doing the exact job ADR-0002 rejected in its own second alternative: documenting a gap as coverage.

## Decision

Add `ATLAS-CORR-0080` (Robustness Under Unanticipated Conditions) to ATLAS-001 Chapter 10, requiring a component to remain in a defined state under conditions its specification did not anticipate — continuing correctly where it can, failing per `ATLAS-FAIL-0020` where it cannot, and in no case continuing in an indeterminate state.

Place it in Correctness rather than Failure Handling: robustness is what correctness degrades into at the edge of the specification, and Chapter 26 governs faults already detected. Chapter 10 gains a short Robustness subsection stating the derivation explicitly, so the relationship to simplicity and transparency survives even though the requirement now stands on its own.

Remove the matrix's Derived Coverage section. With no derived rows left, keeping the section would be the speculative ceremony `ATLAS-PHIL-0102` exists to prevent; its one useful governance rule moves into the Maintenance Rule.

## Consequences

- Every element of the source philosophy now maps to at least one requirement, with no exceptions and no explanatory footnote standing in for one. The matrix's "a row with no requirement is a gap" claim is now literally true.
- `ATLAS-CORR-0080` is `MUST`-strength, so `ATLAS-LANG-0020` (Documented Deviation) does not apply to it. This is intended: a component whose behavior is undefined under unanticipated input is not exercising engineering judgment, and there is no context in which "indeterminate" is the right answer.
- Cost accepted: some overlap with `ATLAS-CORR-0010` and the `FAIL` family at the margins. The requirement is scoped to the *unanticipated* case specifically to keep that overlap narrow, but a reviewer citing all three at once on the same defect is a foreseeable outcome.
- ADR-0002's reasoning is preserved rather than rewritten, per `ATLAS-GOV-ADR-0010`. The record now shows a decision made, reviewed, and reversed — which is the point of keeping ADRs permanent.

## Alternatives Rejected

- **Leave it derived, as ADR-0002 decided.** Rejected by the maintainer on review. The behavioral gap above is the substantive reason the original call was wrong, independent of who raised it.
- **Put it in Chapter 26 (Failure Handling).** Rejected: Chapter 26 governs detected faults, and the defining case for robustness is the condition that was never modeled well enough to be detected as a fault. Filing it there would have buried it under the wrong precondition.
- **Add a Robustness chapter to Part III.** Rejected: inserting a chapter renumbers Chapters 11 through 42 and breaks every cross-reference in the volume, against `ATLAS-CHARTER-0006`'s stability intent — a disproportionate cost for one requirement.
- **Restate it at charter level in ATLAS-000 Article III.** Rejected: the Charter's principles are co-equal foundational properties, and robustness genuinely is derived from Correctness and Clarity, which are already there. The derivation was never the error; the missing behavioral requirement was.
