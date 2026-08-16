# Unix Philosophy Coverage

[ADR-0001](../decisions/0001-unix-philosophy-as-foundational.md) established Unix design philosophy — McIlroy's core tenet, the foundational Unix principles, and Raymond's Rules from *The Art of Unix Programming* — as load-bearing for Atlas rather than decorative. A claim like that is only worth what it can be checked against, so this reference maps every element of that source philosophy to the Atlas requirement or principle that addresses it.

Read it two ways:

- **As an audit.** Every row below names the requirement that carries the rule. A row with no requirement is a gap, and gaps are defects, not deferred work.
- **As a routing table.** When a design argument turns on one of these rules, this tells you which Atlas requirement to cite instead of appealing to Unix philosophy in the abstract.

Requirements referenced here live in [ATLAS-000](../ATLAS-000-foundation-charter.md) and [ATLAS-001](../volumes/ATLAS-001-foundation.md). Identifiers are cited rather than linked, because an identifier is permanent (`ATLAS-CHARTER-0006`) while a heading anchor is not.

## Core Tenet

| Source element | Statement | Covered by |
|---|---|---|
| Do one thing and do it well | A tool has a single focused purpose; feature accumulation is a design smell, and new capability belongs in a new tool composed with the old ones | `ATLAS-PHIL-0100`, ATLAS-000 Article III (Composability) |

## Foundational Principles

| Source element | Statement | Covered by |
|---|---|---|
| Composability | Small, orthogonal tools chain into pipelines to solve problems no single tool anticipated | ATLAS-000 Article III (Composability); `ATLAS-COMP-0001`, `ATLAS-COMP-0010`, `ATLAS-COMP-0020` |
| Text streams as the universal interface | Programs read and write plain text, because text is the one format every other program, language, and human can consume; bespoke formats create coupling | `ATLAS-COMP-0030` |
| Silence is golden | Succeed quietly; produce output only for a requested result or an error | `ATLAS-PHIL-0103`; ATLAS-000 Article III (Economy) |
| Mechanism, not policy | Provide capability, let the caller decide how to apply it | ATLAS-000 Doctrine D11; `ATLAS-PHIL-0101` |
| Everything is a file | Expose heterogeneous resources through one uniform abstraction so the same small tools operate on all of them | `ATLAS-IFACE-0020` |

## Raymond's Rules

| Rule | Meaning | Covered by |
|---|---|---|
| Modularity | Simple parts, clean interfaces | `ATLAS-MOD-0001`, `ATLAS-MOD-0010`, `ATLAS-MOD-0020` |
| Clarity | Clarity beats cleverness | ATLAS-000 Article III (Clarity); `ATLAS-CLAR-0001`, `ATLAS-CLAR-0002`, `ATLAS-CLAR-0020` |
| Composition | Design programs to be connected to other programs | `ATLAS-COMP-0001`, `ATLAS-COMP-0010`, `ATLAS-COMP-0030` |
| Separation | Separate policy from mechanism; interfaces from engines | ATLAS-000 Doctrine D11; `ATLAS-PHIL-0101`, `ATLAS-LAYER-0001`, `ATLAS-DEP-0001` |
| Simplicity | Add complexity only where you must | `ATLAS-PHIL-0030`, `ATLAS-CORR-0070`, `ATLAS-NONGOAL-0060` |
| Parsimony | Write a big program only when nothing else will do | `ATLAS-PHIL-0104`, `ATLAS-DEP-0010`, `ATLAS-NONGOAL-0031` |
| Transparency | Design for visibility — make inspection and debugging easy | `ATLAS-OBS-0040`, `ATLAS-OBS-0001`, `ATLAS-GOAL-0070` |
| Robustness | Robustness is the child of transparency and simplicity | Derived — see [Derived Coverage](#derived-coverage) |
| Representation | Fold knowledge into data so program logic can be dumb | `ATLAS-CLAR-0030` |
| Least Surprise | Do the least surprising thing | `ATLAS-PHIL-0080` |
| Silence | When a program has nothing surprising to say, say nothing | `ATLAS-PHIL-0103` |
| Repair | Fail loudly, and as soon as possible | `ATLAS-FAIL-0020`, `ATLAS-FAIL-0010`, `ATLAS-CORR-0020` |
| Economy | Programmer time is expensive; conserve it over machine time | ATLAS-000 Article III (Economy); `ATLAS-PHIL-0102`, ATLAS-001 Chapter 7 (rank 5) |
| Generation | Write programs to write programs when you can | `ATLAS-AUTO-0020` |
| Optimization | Prototype before polishing; get it working before optimizing | `ATLAS-PERF-0030`, ATLAS-000 Doctrine D2, `ATLAS-VAL-0081` |
| Diversity | Distrust all claims of "one true way" | `ATLAS-PHIL-0105`, `ATLAS-LANG-0020`, `ATLAS-CHARTER-0004` |
| Extensibility | Design for the future — it arrives sooner than you think | `ATLAS-GOAL-0110`, `ATLAS-EVOL-0010`, ATLAS-000 Article III (Longevity) |

## Why It Endures

The four properties the source philosophy attributes to small, sharp tools are the outcomes Atlas is trying to buy, so each maps to the requirement that produces it rather than to a requirement restating it.

| Property | Produced by |
|---|---|
| Testable — a single-purpose tool has a small behavioral surface | `ATLAS-PHIL-0100`, `ATLAS-CORR-0050`, `ATLAS-DET-0020` |
| Replaceable — narrow interfaces make swapping implementations cheap | `ATLAS-LAYER-0010`, `ATLAS-DEP-0001`, `ATLAS-IFACE-0010` |
| Recombinable — utility compounds as the toolset grows | `ATLAS-COMP-0010`, `ATLAS-COMP-0030`, `ATLAS-IFACE-0020` |
| Comprehensible — each piece fits in one head | `ATLAS-CLAR-0020`, `ATLAS-PHIL-0060`, `ATLAS-MAINT-0001` |

## Derived Coverage

One rule is deliberately carried by other requirements rather than its own.

**Robustness.** Raymond states robustness as a *consequence* — "the child of transparency and simplicity" — not an independent practice. Giving it a dedicated requirement would restate `ATLAS-PHIL-0030` (complexity management), `ATLAS-CORR-0070` (complexity risk), and `ATLAS-OBS-0040` (design for inspection) under a fourth identifier, which `ATLAS-PHIL-0102` and `ATLAS-LANG-0010` both argue against. Its two behavioral halves are already required directly: surviving unexpected input is `ATLAS-CORR-0010`, and failing predictably when survival isn't possible is `ATLAS-FAIL-0001`, `ATLAS-FAIL-0010`, and `ATLAS-FAIL-0020`.

This is the only derived row. Any future rule mapped this way MUST be listed here with its reasoning rather than left with an empty cell in the tables above.

## Maintenance Rule

This document is the audit trail for a foundational claim, so it goes stale in exactly one way: a requirement named here gets retired, renumbered in effect (superseded), or reworded such that it no longer carries the rule mapped to it.

A pull request that retires or supersedes any requirement cited above MUST update the corresponding row in the same pull request, per the same rule that governs [the requirement registry](requirement-registry.md). A row whose requirement is retired without a replacement is a coverage gap and MUST be treated as a defect against ADR-0001, not as an accepted loss.
