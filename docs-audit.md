# Documentation Audit

Audit date: 2026-09-01; post-PR #49 reconciliation: 2026-09-02
Scope: all tracked Markdown documentation, repository validation, documentation workflow, ADR index, requirement registry, and declared volume status/deferred areas. Public API doc-comments and generated documentation are not applicable to this documentation-only repository.

The auditor had read portions of the standards earlier in the session. To reduce confirmation bias, this pass re-derived ground truth from `git ls-files`, the GitHub workflow, `tools/validate_docs.py`, the ADR file set, requirement headings, status metadata, and immutable source evidence before classifying claims.

## Findings

| ID | Doc | Where | Claim | Classification | Ground truth | Resolution / next action | Size |
|---|---|---|---|---|---|---|---|
| DOC-001 | `docs/volumes/ATLAS-300-rust-workspace-cargo.md` | Purpose | “exact toolchain pinning remain[s] deferred” | stale | ATLAS-600 Chapter 10 and ADR-0009 activate exact developer/CI toolchain selection; ATLAS-300's Deferred section already says it is no longer deferred | Correct the Purpose statement while preserving Cargo/MSRV ownership | S |
| DOC-002 | Cross-volume evidence claims | Trigger Evidence / ADR context | Nexa and `rusty_data_os` are exercised evidence | unverifiable | The Atlas checkout named source systems but recorded no immutable source revision or artifact links | Add `docs/reference/evidence-provenance.md` with verified immutable revisions, artifacts, scope, and limitations | M |
| DOC-003 | `README.md`, volume metadata, Seed volumes | Library Status / Status | Three volumes are `Seed`; Draft volumes are intentionally partial | accurate | ATLAS-400, ATLAS-700, and ATLAS-900 contain purpose and trigger only; Draft volumes retain explicit Deferred tables under `ATLAS-GOV-STD-0001` | Do not expand without real trigger evidence | — |
| DOC-004 | `docs/reference/requirement-registry.md` | Active Prefixes | Prefix ownership and next-free blocks reflect published requirements | accurate | `tools/validate_docs.py` reports 330 unique registered requirement IDs; manual highest-ID review matches the registry | None | — |
| DOC-005 | `docs/decisions/README.md` | Index | ADR index covers the decision record set | accurate | ADR files 0001-0009 each have an index row | None | — |
| DOC-006 | `CONTRIBUTING.md` / CI | Validation description | `validate-docs` checks IDs, SUMMARY reachability, and internal file links | accurate | `.github/workflows/validate-docs.yml` runs `tools/validate_docs.py`, which implements those checks | None | — |
| DOC-007 | Documentation validation | Whole repository | Heading fragments and prose claims are protected from drift | missing | Before Issue #46, `tools/validate_docs.py` checked target files but not Markdown heading fragments or semantic claims | PR #47 added tested anchor validation; semantic prose remains review-owned | M |
| DOC-008 | `README.md` | Documentation Site | `mdbook serve` is the local preview path | unverifiable | Before Issue #46, `book.toml` was coherent but CI did not build the book | PR #47 pinned mdBook `0.5.4`, verified its release digest, and added the book build to required CI | M |
| DOC-009 | `docs/reference/project-development-governance-lessons.md` | Recommended normative follow-up | Seven program-integrity controls still require a future ATLAS-001 amendment | stale | ATLAS-001 already owns all seven controls through `ATLAS-SPEC-0020`, `ATLAS-SPEC-0030`, `ATLAS-MAINT-0030`, `ATLAS-LIFE-0010`/`0020`-`0031`, and `ATLAS-GOV-REVIEW-0020`-`0060` | Replace the obsolete future-work section with an exact control-to-requirement map | S |
| DOC-010 | `docs/volumes/ATLAS-300-rust-workspace-cargo.md` | Deferred Cargo feature strategy | Multiple supported feature combinations create real compatibility, dependency, or validation differences requiring shared policy | accurate | Rusty Mill evidence record `EVID-RM-FEATURES-2026-09-02` demonstrates materially different isolated-package and unified-workspace feature graphs. ADR-0010 accepted that evidence and PR #49 added the bounded feature-strategy requirements `ATLAS-RWC-0140` through `ATLAS-RWC-0200`. | Resolved by PR #49. Keep the remaining deferred topics explicit; the evidence does not currently justify a broader feature-strategy amendment. | M |

## Counts

Baseline classifications before approved corrections:

| Classification | Count |
|---|---:|
| stale | 1 |
| missing | 1 |
| orphaned | 0 |
| aspirational | 0 |
| unverifiable | 2 |
| accurate | 4 |

After DOC-001 and DOC-002 were resolved by PR #45:

| Classification | Count |
|---|---:|
| stale | 0 |
| missing | 1 |
| orphaned | 0 |
| aspirational | 0 |
| unverifiable | 1 |
| accurate | 6 |

After DOC-007 and DOC-008 were resolved by PR #47:

| Classification | Count |
|---|---:|
| stale | 0 |
| missing | 0 |
| orphaned | 0 |
| aspirational | 0 |
| unverifiable | 0 |
| accurate | 8 |

Continuation re-audit before resolving DOC-009:

| Classification | Count |
|---|---:|
| stale | 1 |
| missing | 0 |
| orphaned | 0 |
| aspirational | 0 |
| unverifiable | 0 |
| accurate | 8 |

After DOC-009 is resolved by replacing the obsolete future-work statement with the normative ownership map:

| Classification | Count |
|---|---:|
| stale | 0 |
| missing | 0 |
| orphaned | 0 |
| aspirational | 0 |
| unverifiable | 0 |
| accurate | 9 |

Post-PR #49 state (current; prior tables remain historical snapshots):

| Classification | Count |
|---|---:|
| stale | 0 |
| missing | 0 |
| orphaned | 0 |
| aspirational | 0 |
| unverifiable | 0 |
| accurate | 10 |

PR #49 resolved DOC-010 by accepting ADR-0010, recording `EVID-RM-FEATURES-2026-09-02`, and adding `ATLAS-RWC-0140` through `ATLAS-RWC-0200`. The current registry contains 337 requirement IDs, and the ADR inventory contains 10 files with 10 index entries. The Rusty Mill trigger is resolved; its bounded evidence does not currently justify a broader feature-strategy amendment.

## Mechanical Checks

- Baseline `tools/validate_docs.py`: passed — 31 files, 330 unique requirement IDs.
- Post-correction `tools/validate_docs.py`: passed — 33 files, 330 unique requirement IDs.
- Issue #46 validator unit tests: passed, including duplicate, punctuation/Unicode, percent-encoded, explicit-anchor, file-only, and missing-fragment cases.
- Issue #46 anchor-aware `tools/validate_docs.py`: passed against the full repository.
- PR #47 mdBook `0.5.4` build: passed in required CI using the official release asset and published SHA-256 digest.
- DOC-009 ownership map: checked against the current ATLAS-001 requirement headings and text.
- Pre-PR #49 ADR inventory snapshot: 9 files, 9 index entries.
- README status table: matches volume metadata.
- Docs-loop reference scan: no confirmed broken relative Markdown file links; unresolved inline-code candidates were examples or external-repository paths, not broken Atlas links.
- `mdbook serve`: not executed because mdBook was unavailable on the audit host.
- Post-PR #49 `tools/validate_docs.py`: passed — 34 Markdown files, 337 unique registered requirement IDs.
- Post-PR #49 ADR inventory: 10 files, 10 index entries.
- Post-PR #49 required CI: Validate docs run 33672685856 passed, including “Install pinned mdBook release” and “Build documentation book.” The local audit host separately received HTTP 403 while downloading the pinned, digest-verified release asset, so it did not repeat the mdBook build locally.

## Intentional Incompleteness

Atlas is not a finished universal standards catalog. Three volumes remain Seed and Draft volumes retain approximately 40 explicit deferred topics. That is conforming behavior under `ATLAS-GOV-STD-0001`, not documentation drift. Completion means every fired trigger is addressed and every unfired trigger remains explicit—not that speculative chapters are filled in.

## Approval Boundary

DOC-001 and DOC-002 were documentation corrections approved and merged in PR #45. DOC-007 and DOC-008 were separated into Issue #46 because docs-loop does not edit validation code or silently expand automation policy; Issue #46 now owns their tested tooling and CI resolution.

DOC-010's trigger was resolved by PR #49 within the approved evidence boundary: ADR-0010 and `EVID-RM-FEATURES-2026-09-02` support the bounded `ATLAS-RWC-0140` through `ATLAS-RWC-0200` amendment. No normative, ADR, evidence, registry, validation, CI, or unrelated finding change is part of this reconciliation, and no broader feature-strategy amendment is currently justified.
