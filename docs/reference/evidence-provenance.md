# Evidence Provenance

This ledger records immutable source snapshots used to verify exercised evidence cited by Atlas standards and ADRs. It makes the evidence reviewable without turning source-system technologies into Atlas mandates.

An entry establishes that the linked source artifacts existed at the recorded revision and support the stated Atlas decision. It does not expand the scope of that decision, prove behavior outside the linked artifacts, or make later source changes normative. When later evidence changes an Atlas decision, Atlas records that change through its normal RFC and ADR process rather than silently advancing this ledger entry.

## Evidence Records

### EVID-NEXA-2026-09-01

| Field | Value |
|---|---|
| Source repository | [`baileyrd/nexa`](https://github.com/baileyrd/nexa) |
| Immutable revision | [`f7925682d9eb11d2444b8ca41cbd0347aa9a8808`](https://github.com/baileyrd/nexa/tree/f7925682d9eb11d2444b8ca41cbd0347aa9a8808) |
| Verified | 2026-09-01 |
| Atlas decisions supported | ADR-0004 through ADR-0008; exercised evidence used by ATLAS-100, ATLAS-300, ATLAS-500, ATLAS-600, and ATLAS-800 |

Authoritative source artifacts reviewed at that revision:

- [Approved v1 release architecture](https://github.com/baileyrd/nexa/blob/f7925682d9eb11d2444b8ca41cbd0347aa9a8808/docs/architecture/NEXA-ARCH-002-V1-RELEASE-ARCHITECTURE.md) — runtime/domain authority, orchestration, process boundaries, persistence, events, adapters, trust boundaries, and diagnostic-correlation semantics.
- [Root Cargo workspace manifest](https://github.com/baileyrd/nexa/blob/f7925682d9eb11d2444b8ca41cbd0347aa9a8808/Cargo.toml) and [lockfile](https://github.com/baileyrd/nexa/blob/f7925682d9eb11d2444b8ca41cbd0347aa9a8808/Cargo.lock) — workspace membership, resolver, shared package metadata, MSRV, shared dependencies, and resolved dependency state.
- [Required Rust CI workflow](https://github.com/baileyrd/nexa/blob/f7925682d9eb11d2444b8ca41cbd0347aa9a8808/.github/workflows/ci.yml) — moving stable toolchain selection, `rustfmt`, Clippy with warnings denied, workspace build/test coverage, and dependency-boundary enforcement.
- [Current-state assessment](https://github.com/baileyrd/nexa/blob/f7925682d9eb11d2444b8ca41cbd0347aa9a8808/docs/architecture/NEXA-CURRENT-STATE-ASSESSMENT.md), [rebaseline gates](https://github.com/baileyrd/nexa/blob/f7925682d9eb11d2444b8ca41cbd0347aa9a8808/docs/governance/ARCHITECTURE-REBASELINE-GATES.md), and [v1 definition](https://github.com/baileyrd/nexa/blob/f7925682d9eb11d2444b8ca41cbd0347aa9a8808/docs/architecture/NEXA-V1-DEFINITION.md) — the program-integrity and finite-release governance evidence generalized by ADR-0004 and ATLAS-001.

Limitations: this snapshot verifies repository-recorded architecture, workspace, workflow, and governance evidence. It does not independently certify runtime deployment, performance, external-provider behavior, user acceptance, or any later source revision.

### EVID-RDO-EXP0001-2026-09-01

| Field | Value |
|---|---|
| Source repository | [`baileyrd/rusty_data_os`](https://github.com/baileyrd/rusty_data_os) |
| Immutable revision | [`d76fe6027e87d1c22c64aaa5c84d895fadae1a05`](https://github.com/baileyrd/rusty_data_os/tree/d76fe6027e87d1c22c64aaa5c84d895fadae1a05) |
| Verified | 2026-09-01 |
| Atlas decisions supported | ADR-0009; exercised repository evidence used by ATLAS-600 Chapters 8-10 and the monorepo-management chapter |

Authoritative source artifacts reviewed at that revision:

- [EXP-0001 R9 authorization](https://github.com/baileyrd/rusty_data_os/blob/d76fe6027e87d1c22c64aaa5c84d895fadae1a05/docs/experiments/EXP-0001/R9-WORKSPACE-HARNESS-CI-AND-SLICE-A-AUTHORIZATION.md) — exact-toolchain rationale, component/target freeze, CI identity reporting, evidence limits, and review requirements for selection changes.
- [Exact toolchain declaration](https://github.com/baileyrd/rusty_data_os/blob/d76fe6027e87d1c22c64aaa5c84d895fadae1a05/experiments/exp-0001/rust-toolchain.toml) — Rust `1.89.0`, minimal profile, `rustfmt`, Clippy, and `x86_64-unknown-linux-gnu`.
- [Required EXP-0001 workflow](https://github.com/baileyrd/rusty_data_os/blob/d76fe6027e87d1c22c64aaa5c84d895fadae1a05/.github/workflows/exp0001-slice-a.yml) — exact installation, tool-version disclosure, locked/offline validation, formatting, lint, and test commands.
- [Experiment workspace manifest](https://github.com/baileyrd/rusty_data_os/blob/d76fe6027e87d1c22c64aaa5c84d895fadae1a05/experiments/exp-0001/Cargo.toml) and [lockfile](https://github.com/baileyrd/rusty_data_os/blob/d76fe6027e87d1c22c64aaa5c84d895fadae1a05/experiments/exp-0001/Cargo.lock) — bounded workspace configuration and resolved state.
- [Repository README](https://github.com/baileyrd/rusty_data_os/blob/d76fe6027e87d1c22c64aaa5c84d895fadae1a05/README.md) and [conceptual architecture](https://github.com/baileyrd/rusty_data_os/blob/d76fe6027e87d1c22c64aaa5c84d895fadae1a05/docs/ARCHITECTURE.md) — separation of research, experiments, reusable code, and explicitly unresolved product architecture.

Limitations: Rust `1.89.0`, the named target, EXP-0001 boundaries, and its workflow are source evidence only. They are not Atlas-wide version, platform, installer, database, or release mandates. The snapshot does not convert validation into benchmark, durability, portability, or production-readiness evidence.

### EVID-RM-FEATURES-2026-09-02

| Field | Value |
|---|---|
| Source repository | [`Rusty-Mill/rusty_mill`](https://github.com/Rusty-Mill/rusty_mill) |
| Immutable revision | [`06ca8669f38f80291a63308de7563bfea43caab5`](https://github.com/Rusty-Mill/rusty_mill/tree/06ca8669f38f80291a63308de7563bfea43caab5) |
| Verified | 2026-09-02 |
| Atlas decision and chapters supported | ADR-0010; exercised feature-graph evidence used by ATLAS-300 Chapter 7, at its boundaries with ATLAS-100 compatibility architecture, ATLAS-200 version/compatibility domains, and ATLAS-600 validation |

Authoritative source artifacts reviewed at that revision:

- [Root Cargo workspace manifest](https://github.com/Rusty-Mill/rusty_mill/blob/06ca8669f38f80291a63308de7563bfea43caab5/Cargo.toml) — the 174-member workspace and its Cargo resolution boundary.
- [CI workflow](https://github.com/Rusty-Mill/rusty_mill/blob/06ca8669f38f80291a63308de7563bfea43caab5/.github/workflows/ci.yml) — scoped and workspace-wide validation, including all-features use.
- [Affected-crate analysis](https://github.com/Rusty-Mill/rusty_mill/blob/06ca8669f38f80291a63308de7563bfea43caab5/.github/scripts/affected_crates.py) — transitive-dependent calculation using `cargo metadata --all-features`.
- [Architecture](https://github.com/Rusty-Mill/rusty_mill/blob/06ca8669f38f80291a63308de7563bfea43caab5/ARCHITECTURE.md) and [workspace ADR](https://github.com/Rusty-Mill/rusty_mill/blob/06ca8669f38f80291a63308de7563bfea43caab5/docs/adr/0001-consolidate-crates-into-workspace.md) — component boundaries, workspace consolidation, and validation context.
- [Feature-unification decision request](https://github.com/Rusty-Mill/rusty_mill/blob/06ca8669f38f80291a63308de7563bfea43caab5/crates/rusty_tokio/docs/decision-request-real-tokio-interop-bridge.md) — the optional `rusty_request` behavior, unified all-features graph, scoped-graph difference, reactor panic, capability-manifest boundary, and proposed bridge whose correctness remains undecided.

The related [workspace migration PR](https://github.com/Rusty-Mill/rusty_mill/pull/131) and [decision-request PR](https://github.com/Rusty-Mill/rusty_mill/pull/132) supplied review history; the immutable revision and blob links above are the evidence snapshot used for the Atlas decision.

Limitations: this evidence does not certify every Rusty Mill crate or target. It does not make Rusty Mill, Tokio, `rusty_tokio`, `--all-features`, GitHub Actions, or Rusty Mill's CI design mandatory for Atlas. It does not prove that the proposed bridge is correct. It does not turn capability-manifest closure into runtime, system, user-acceptance, or release-readiness evidence.

### EVID-RM-DEPS-2026-09-03

| Field | Value |
|---|---|
| Source repository | [`Rusty-Mill/rusty_mill`](https://github.com/Rusty-Mill/rusty_mill) |
| Immutable revision | [`77df1d62e0d328a86f54dedb226e5204a0e42fad`](https://github.com/Rusty-Mill/rusty_mill/tree/77df1d62e0d328a86f54dedb226e5204a0e42fad) |
| Verified | 2026-09-03 |
| Atlas decision and chapter supported | ADR-0011; exercised dependency-role, artifact-reachability, and native/build-input evidence used by ATLAS-300 Chapter 8 |

Authoritative source artifacts reviewed at that revision:

- [Immutable repository tree](https://github.com/Rusty-Mill/rusty_mill/tree/77df1d62e0d328a86f54dedb226e5204a0e42fad), [root Cargo workspace manifest](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/Cargo.toml), and the exact path-qualified `Cargo.toml` files in that tree, including [`rusty_request`](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/crates/rusty_request/Cargo.toml) and [`rusty_tokio`](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/crates/rusty_tokio/Cargo.toml) — 199 tracked manifests and manifest-level normal, development, build, source, target, and feature distinctions. The root manifest combines explicit member entries with glob patterns; an exact member count would require expanding those patterns against the immutable tree, which this review did not independently reproduce, so no workspace-member count is asserted. The immutable tree is the authoritative enumeration of all 199 exact manifest paths rather than a moving search result.
- [Root lockfile](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/Cargo.lock) — the whole-workspace resolved state, including registry and git sources and packages associated with native libraries, generated bindings, and system integration. Its breadth supports inventory analysis but not a claim that every artifact reaches every package.
- The five tracked build scripts, cited at exact immutable paths: [`crates/rusty_a2a/build.rs`](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/crates/rusty_a2a/build.rs), [`crates/rusty_inventrory/crates/inventory-tauri/build.rs`](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/crates/rusty_inventrory/crates/inventory-tauri/build.rs), [`crates/rusty_key/desktop/src-tauri/build.rs`](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/crates/rusty_key/desktop/src-tauri/build.rs), [`crates/rusty_yirp/crates/sessionmgr-daemon/build.rs`](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/crates/rusty_yirp/crates/sessionmgr-daemon/build.rs), and [`crates/rusty_yirp/crates/sessionmgr-desktop/src-tauri/build.rs`](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/crates/rusty_yirp/crates/sessionmgr-desktop/src-tauri/build.rs). Their manifest associations and source make their build-time behavior inspectable; presence alone does not classify each script or package as release-critical.
- The [`sessionmgr-daemon` manifest](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/crates/rusty_yirp/crates/sessionmgr-daemon/Cargo.toml) declares that the package ships the `sessionmgr` binary, while its [build script](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/crates/rusty_yirp/crates/sessionmgr-daemon/build.rs) embeds the Windows manifest into that artifact. This manifest-to-script relationship is the release-critical build-script trigger; the other four scripts are treated only according to their immutable manifests and source.
- [Repository CI workflow](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/.github/workflows/ci.yml) and [affected-crate analysis](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/.github/scripts/affected_crates.py) — graph-aware affected-package selection and validation. These artifacts do not mechanically enforce the project's dependency-source restrictions and do not establish that the workflow was required by branch protection.
- [Architecture](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/ARCHITECTURE.md), [repository README](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/README.md), [workspace ADR](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/docs/adr/0001-consolidate-crates-into-workspace.md), and [`rusty_tokio` feature decision request](https://github.com/Rusty-Mill/rusty_mill/blob/77df1d62e0d328a86f54dedb226e5204a0e42fad/crates/rusty_tokio/docs/decision-request-real-tokio-interop-bridge.md) — component and artifact boundaries, workspace intent, dependency-sovereignty context, and why graph-wide evidence requires a bounded interpretation.

Independent review counted tracked manifest and build-script paths from the immutable tree, classified dependency tables in those manifests, and compared those static declarations with source kinds and package metadata in the lockfile and repository CI path. It did not independently expand the root manifest's member glob patterns into an exact workspace-member count.

Limitations: static dependency evidence is not runtime or release certification. The workspace lockfile does not prove every artifact ships every package. Rusty Mill's dependency-sovereignty objective and detectable source-policy gaps show why a scoped policy needs mechanical enforcement; they do not prove that the cited workflow supplies that enforcement, and the immutable repository artifacts do not prove required-branch status. Counts are revision-specific, and no workspace-member count is asserted without independently expanding the root manifest's patterns. External development dependencies may serve as non-shipping test oracles. This record does not certify native tool availability, generated output correctness, platform portability, vulnerability status, or supply-chain integrity, and it does not activate ATLAS-500.

## Maintenance

- Evidence links MUST use immutable revisions rather than moving branches.
- A source snapshot MUST identify the Atlas decision or chapter it supports and the limits of that support.
- A later source revision does not silently replace an existing record. Add a new dated evidence record when a later Atlas decision relies on materially changed evidence.
- Source artifacts remain owned by their source repository. This ledger records provenance; it does not duplicate or take ownership of their specifications.
