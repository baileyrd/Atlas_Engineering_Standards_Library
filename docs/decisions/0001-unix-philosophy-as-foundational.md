# 0001 - Unix Philosophy as a Foundational Principle, Not an Addendum

**Status:** Accepted

## Context

ATLAS-000 and ATLAS-001 originated from an unstructured brainstorm that escalated turn by turn from "define a versioning approach" into a 10-volume normative standards library, with permanent requirement identifiers and heavy governance ceremony (RFC process, ADRs, formal review) drafted before a single line of Atlas code existed. Nothing in the resulting Foundational Principles (ATLAS-000 Article III) or Engineering Philosophy (ATLAS-001 Chapter 6) reflected the maintainer's actual, practiced design philosophy: Unix minimalism (McIlroy's "do one thing and do it well," composability, "silence is golden," "mechanism, not policy") and Raymond's Rules (parsimony, economy, distrust of "one true way"). That philosophy already governs the maintainer's other repositories and is documented independently in a personal `PHILOSOPHY.md` that underlies their global engineering defaults.

A "Foundation" volume that doesn't ground itself in the actual philosophy driving engineering judgment is hollow — it would describe a library disconnected from how its own author builds software.

## Decision

Add Composability and Economy as co-equal Foundational Principles in ATLAS-000 Article III (not a subordinate note), Mechanism-Not-Policy as Doctrine D11, and a Unix Design Heritage subsection with four checkable requirements in ATLAS-001 Chapter 6. Treat this as load-bearing: subsequent volumes are expected to cite these principles the same way they cite Correctness or Security, and Chapter 34's consumer-gating rule (don't draft a volume speculatively) is itself a direct application of Economy to the standards-writing process.

## Consequences

- The library's own growth is now self-constrained: `ATLAS-GOV-STD-0001` prohibits drafting ATLAS-100 and ATLAS-300 through ATLAS-900 in full until a real consumer need exists, rather than continuing the brainstorm's pattern of writing plausible-sounding content for subsystems that don't exist yet.
- Some existing content written under the original maximalist framing (heavy ceremony, exhaustive per-chapter structure) may read as being in tension with these principles until revisited; this ADR doesn't retroactively rewrite everything, only establishes the principle going forward.
- Requirement `ATLAS-PHIL-0102` (Justified Complexity) is now citable as a reason to reject a proposed requirement, chapter, or process that doesn't have a demonstrated need behind it — a real check against scope creep in future RFCs.

## Alternatives Rejected

- **Leave Unix philosophy as personal, unstated context.** Rejected: it would keep governing decisions invisibly (via the maintainer's judgment calls) rather than being a citable principle other contributors or an AI assistant could apply consistently — exactly the kind of undocumented knowledge `ATLAS-KNOW-0001` and the Charter's Longevity principle argue against.
- **Add it as an appendix or "style guide" rather than Article III.** Rejected: subordinating it would have preserved the original 7-principle framing as primary and Unix philosophy as decoration, which misrepresents its actual weight in how decisions get made.
- **Rewrite ATLAS-000/001 from scratch instead of amending in place.** Rejected for this decision specifically: the existing principles (Correctness, Clarity, Security, etc.) are not in conflict with Unix philosophy, they're compatible with it — amendment was sufficient and preserved identifier stability (`ATLAS-CHARTER-0006`) for everything that didn't need to change.
