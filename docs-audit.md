# Documentation Audit

Audit date: 2026-09-01
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
| DOC-007 | Documentation validation | Whole repository | Heading fragments and prose claims are protected from drift | missing | Before Issue #46, `tools/validate_docs.py` checked target files but not Markdown heading fragments or semantic claims | Issue #46 adds tested anchor validation; semantic prose remains review-owned | M |
| DOC-008 | `README.md` | Documentation Site | `mdbook serve` is the local preview path | unverifiable | Before Issue #46, `book.toml` was coherent but CI did not build the book | Issue #46 pins mdBook `0.5.4`, verifies its release digest, and builds the book in required CI | M |

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

After DOC-007 and DOC-008 are resolved by Issue #46:

| Classification | Count |
|---|---:|
| stale | 0 |
| missing | 0 |
| orphaned | 0 |
| aspirational | 0 |
| unverifiable | 0 |
| accurate | 8 |

## Mechanical Checks

- Baseline `tools/validate_docs.py`: passed — 31 files, 330 unique requirement IDs.
- Post-correction `tools/validate_docs.py`: passed — 33 files, 330 unique requirement IDs.
- Issue #46 validator unit tests: passed, including duplicate, punctuation/Unicode, percent-encoded, explicit-anchor, file-only, and missing-fragment cases.
- Issue #46 anchor-aware `tools/validate_docs.py`: passed against the full repository.
- Issue #46 mdBook `0.5.4` build: required in CI using the official release asset and published SHA-256 digest.
- ADR inventory: 9 files, 9 index entries.
- README status table: matches volume metadata.
- Docs-loop reference scan: no confirmed broken relative Markdown file links; unresolved inline-code candidates were examples or external-repository paths, not broken Atlas links.
- `mdbook serve`: not executed because mdBook was unavailable on the audit host.

## Intentional Incompleteness

Atlas is not a finished universal standards catalog. Three volumes remain Seed and Draft volumes retain approximately 40 explicit deferred topics. That is conforming behavior under `ATLAS-GOV-STD-0001`, not documentation drift. Completion means every fired trigger is addressed and every unfired trigger remains explicit—not that speculative chapters are filled in.

## Approval Boundary

DOC-001 and DOC-002 were documentation corrections approved and merged in PR #45. DOC-007 and DOC-008 were separated into Issue #46 because docs-loop does not edit validation code or silently expand automation policy; Issue #46 now owns their tested tooling and CI resolution.
