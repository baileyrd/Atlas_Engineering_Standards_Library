# ATLAS-300 - Volume IV - Rust Workspace and Cargo Architecture

| Field | Value |
|---|---|
| Document ID | ATLAS-300 |
| Title | Volume IV - Rust Workspace and Cargo Architecture |
| Short Name | RWC |
| Status | Draft 0.1 |
| Classification | Normative |
| Scope | Rust workspace coordination, Cargo manifest inheritance, dependency-graph and artifact-reachability policy, version expression, MSRV declaration, lockfile reproducibility, and native/build-input governance |
| Parent | ATLAS-001 |

## Purpose

Volume IV defines how Atlas uses Cargo workspaces and manifests once a Rust repository contains multiple cooperating packages. ATLAS-001 owns general dependency and reproducibility doctrine, ATLAS-100 owns architectural dependency direction, ATLAS-200 owns version-group semantics, and ATLAS-600 owns repository/monorepo and CI/toolchain workflow. This volume defines the Cargo-specific representation that keeps those decisions coherent across a real multi-crate workspace.

A Cargo workspace and a Monorepo are related but distinct coordination boundaries. A Monorepo is the repository-level governance boundary defined by ATLAS-600; one Monorepo MAY contain one Cargo workspace, multiple Cargo workspaces, non-Cargo projects, governed documentation/assets, or other independently built areas where justified. This volume MUST NOT be read as requiring every first-party area in one repository to share a single Cargo workspace.

This draft is intentionally narrower than the volume's eventual scope. The original Seed trigger fired through exercised multi-crate workspace evidence recorded in ADR-0006. Cargo feature strategy is active through [ADR-0010](../decisions/0010-activate-cargo-feature-strategy-from-unified-workspace-evidence.md). Dependency-role, artifact-reachability, and native/build-input governance are now active through [ADR-0011](../decisions/0011-activate-dependency-role-artifact-reachability-and-native-build-input-governance.md). Build-profile policy, unsafe Rust, publishing, cross-compilation, and workspace profile sharing remain deferred. Exact developer and CI toolchain selection is active under ATLAS-600 Chapter 10; this volume retains Cargo and MSRV ownership as described below.

## Trigger Evidence

The Seed trigger is satisfied by a real Rust workspace containing applications, tools, and numerous cooperating crates. That workspace already makes concrete choices about explicit membership, a virtual-workspace resolver, inherited edition/license/MSRV metadata, shared third-party dependencies, local path dependencies, workspace-version inheritance, a committed lockfile, and automated Cargo dependency-boundary checks. See [ADR-0006](../decisions/0006-promote-atlas-300-from-exercised-rust-workspace-evidence.md).

The previously deferred native-dependency and build-script trigger has also fired. Rusty Mill's immutable exercised evidence contains materially different normal, development, and build dependency roles; release-relevant build scripts; registry, git, native-library, generated-binding, and system-integration dependencies; and a repository-specific dependency-sovereignty objective backed by required automation. Its whole-workspace lockfile also demonstrates why workspace inventory is not automatically an artifact's shipping graph. See [ADR-0011](../decisions/0011-activate-dependency-role-artifact-reachability-and-native-build-input-governance.md) and [EVID-RM-DEPS-2026-09-03](../reference/evidence-provenance.md#evid-rm-deps-2026-09-03).

## Relationship to Other Volumes

- ATLAS-100 determines which dependency directions and ownership boundaries are architecturally valid; this volume governs how Cargo manifests express and mechanically expose them.
- ATLAS-200 determines which crates belong to the same version group; this volume governs when Cargo workspace-version inheritance expresses that decision.
- ATLAS-600 determines repository/Monorepo coordination and how CI invokes Cargo and other tools; this volume defines the workspace and manifest properties those repository-level rules validate.

### Chapter 1 - Workspace Coordination Boundary

A Cargo workspace is a build and dependency-resolution coordination boundary: packages inside it share dependency resolution, a lockfile, target output, root-level commands, and workspace metadata. It should therefore contain packages that are intentionally developed and validated together, not merely packages that happen to live in the same Monorepo. Monorepo membership alone is not sufficient reason to place a package in a Cargo workspace.

#### Requirements

##### ATLAS-RWC-0001 - Explicit Workspace Coordination Boundary

A repository containing multiple first-party Rust packages that are developed and validated as one coordinated system MUST define an explicit Cargo workspace containing those packages. A package intentionally kept outside that workspace MUST have a documented reason for independent build, release, dependency-resolution, or ownership behavior.

##### ATLAS-RWC-0010 - Intended Membership Is Explicit

Every first-party package intended to participate in a workspace's coordinated build and dependency resolution MUST be explicitly covered by the workspace's `members` declaration. A package under the workspace root that is intentionally not a member MUST be excluded or otherwise separated deliberately rather than relying on accidental Cargo discovery behavior.

##### ATLAS-RWC-0020 - Virtual Workspace Resolver Is Explicit

A virtual Cargo workspace — a workspace root with no root `[package]` — MUST declare its Cargo feature resolver explicitly. The resolver choice MUST be compatible with the workspace's supported Rust/Cargo baseline rather than inferred from a package edition that the virtual root does not have.

### Chapter 2 - Shared Manifest Policy

A workspace should centralize policy that is genuinely shared while leaving real package differences visible. Inheritance is useful when it removes drift; it is harmful when it hides independent compatibility or dependency requirements.

#### Requirements

##### ATLAS-RWC-0030 - Shared Package Metadata

Package metadata that is intentionally common across workspace members — including Rust edition, license, and MSRV where applicable — SHOULD be declared once under `[workspace.package]` and inherited by members. A member whose value differs for a real compatibility or release reason MUST declare that difference explicitly rather than silently inheriting an incorrect shared value.

##### ATLAS-RWC-0040 - Shared Third-Party Dependency Policy

When multiple workspace members intentionally share the same third-party dependency source and version baseline, the dependency SHOULD be declared under `[workspace.dependencies]` and inherited by those members. A member MAY add member-specific features or other compatible dependency options at its own declaration. A member that requires a different source, incompatible version baseline, or otherwise independent compatibility policy SHOULD declare that requirement locally instead of distorting the workspace-wide baseline for unrelated members.

##### ATLAS-RWC-0050 - Workspace-Local First-Party Resolution

A normal dependency on another package in the same Cargo workspace MUST resolve to that workspace-local package during workspace development, directly through a path dependency or an equivalent workspace dependency that resolves locally. A registry or git copy of the same first-party workspace package MUST NOT silently substitute for the local member in the normal workspace dependency graph.

### Chapter 3 - Cargo Dependency Graph and Architecture

Cargo manifests are executable architecture. A source-level module boundary does not preserve dependency direction if a manifest can add an implementation dependency around it.

#### Requirements

##### ATLAS-RWC-0060 - Normal Dependency Edges Follow Architecture

Normal dependency edges between first-party workspace members MUST conform to the governing architectural dependency direction defined by ATLAS-100 and the applicable component specifications. Dev-only dependencies MAY cross a production dependency layer for test fixtures or conformance support only when they do not enter the normal build graph or create a second production authority.

##### ATLAS-RWC-0070 - Machine-Checkable Dependency Boundaries

When a prohibited Cargo dependency edge would still compile successfully while violating a normative architecture boundary, the repository MUST enforce that critical boundary with an automated check based on Cargo metadata, `cargo tree`, manifest inspection, or an equivalent machine-readable dependency graph. Review alone MUST NOT be the only protection against a mechanically detectable forbidden edge.

### Chapter 4 - Cargo Expression of Version Groups

ATLAS-200 owns the decision about which packages version together. Cargo's workspace version inheritance is an implementation of that decision, not a reason to place unrelated packages into lockstep.

#### Requirements

##### ATLAS-RWC-0080 - Workspace Version Inheritance Means Shared Version Group

A package using `version.workspace = true` MUST belong to the version group represented by the workspace-level version under ATLAS-200. Workspace version inheritance MUST NOT be used merely to avoid writing an independently governed package version in its own manifest.

##### ATLAS-RWC-0090 - Independently Versioned Packages Declare Their Version

A workspace member governed as an independent version domain under ATLAS-200 MUST declare its own package version rather than inherit the workspace package version. Changing version-group membership MUST be a deliberate versioning decision, not an incidental Cargo-manifest cleanup.

### Chapter 5 - Rust Compatibility Baseline

Cargo's `rust-version` expresses a minimum supported Rust version. It does not select the exact compiler used by every developer or CI run, so Atlas keeps compatibility-floor policy separate from toolchain-selection policy.

#### Requirements

##### ATLAS-RWC-0100 - Explicit MSRV

An official multi-package Atlas Rust workspace MUST declare the minimum supported Rust version for packages it governs. Where members share one MSRV, it SHOULD be declared under `[workspace.package]` and inherited. A member requiring a higher MSRV MUST declare that difference explicitly and treat the change as a compatibility consideration for its consumers.

##### ATLAS-RWC-0110 - MSRV Is Not a Toolchain Pin

Cargo `rust-version` MUST be treated as a minimum compatibility floor, not as an exact developer or CI toolchain pin. Exact developer and CI toolchain selection, when required, MUST be governed by ATLAS-600 Chapter 10 so that using a newer supported compiler does not falsely imply the declared MSRV has changed.

### Chapter 6 - Lockfile and Resolved Dependency State

A workspace that produces an application or repository-built release artifact needs a reviewable record of the exact dependency resolution used to build and test that artifact. Cargo's lockfile is that record; it is not a replacement for manifest compatibility constraints.

#### Requirements

##### ATLAS-RWC-0120 - Application Workspace Lockfile

A Cargo workspace that produces an application, executable tool, or other repository-built release artifact MUST track its root `Cargo.lock` in version control so the resolved dependency graph used by normal builds and validation is reviewable and reproducible. This requirement does not make a library consumer's resolution part of the library's public compatibility contract.

##### ATLAS-RWC-0130 - Lockfile Changes Are Deliberate

A `Cargo.lock` change MUST be attributable to an intended dependency-resolution change, manifest change, or tool-supported lockfile maintenance action. Unexplained or unrelated lockfile churn MUST NOT be accepted merely because the workspace still builds.

### Chapter 7 - Cargo Feature Architecture

Cargo features participate in dependency resolution across a graph. Their effective behavior can therefore differ between an isolated package command and a supported workspace or cross-package composition. A maximal feature combination is valuable stress evidence, but support commitments belong to explicitly defined profiles and their compatibility and runtime preconditions. This chapter defines those Cargo-specific invariants; ATLAS-100 remains authoritative for architectural boundaries, ATLAS-200 for version and compatibility domains, and ATLAS-600 for CI orchestration and validation workflow.

#### Requirements

##### ATLAS-RWC-0140 - Effective Features Are Graph-Resolved

The effective feature set for a Cargo build MUST be determined from the resolved dependency graph for the applicable build context. It MUST NOT be inferred solely from a consumer's or dependency's local manifest, because other graph participants can enable additional features through feature unification.

##### ATLAS-RWC-0150 - Supported Feature Profiles Are Explicit

Materially distinct feature profiles that a package, workspace, or product supports MUST be explicitly identified. Each such profile MUST document its compatibility expectations and any runtime, configuration, platform, provider, or integration preconditions needed for correct operation.

##### ATLAS-RWC-0160 - All-Features Evidence Is Bounded

Validation with Cargo's `--all-features` option MAY be designated as a stress profile, but MUST NOT be treated as proof of every supported feature profile unless those profiles are demonstrably equivalent. An all-features check MUST NOT replace validation required for default, minimal, or other explicitly supported profiles.

##### ATLAS-RWC-0170 - Behavior-Changing Features Affect Compatibility

A feature that changes runtime or executor assumptions, I/O traits, provider selection, serialization, wire behavior, persistence, or a comparable operating precondition MUST be documented as affecting the applicable compatibility surface. Ownership and versioning of that surface MUST follow ATLAS-100 and the applicable ATLAS-200 compatibility domain rather than being hidden as a manifest-only implementation detail.

##### ATLAS-RWC-0180 - Unified Supported Graphs Are Validated

When feature unification can produce a supported cross-package graph with materially different behavior, required validation MUST exercise that resolved graph or enforce an equivalent automated incompatibility check. Validation of an isolated package graph MUST NOT substitute for the materially different supported graph.

##### ATLAS-RWC-0190 - Impact Analysis Uses Compatible Feature Assumptions

Impact-aware package selection and the validation selected from it MUST use compatible feature-graph assumptions. If impact calculation uses a broader or different feature graph than the selected validation, the repository MUST document and enforce why that difference cannot omit affected behavior.

##### ATLAS-RWC-0200 - Incompatible Assumptions Fail Clearly

Incompatible feature and runtime assumptions MUST produce a clear failure. Compile-time or configuration-time rejection SHOULD be used where practical; otherwise the required adapter, bridge, or runtime precondition MUST be documented and automatically tested in every supported graph that depends on it.

### Chapter 8 - Cargo Dependency Roles, Artifact Reachability, and Native Build Inputs

Cargo records several kinds of dependency edges, while a workspace may produce many artifacts from different packages, targets, and feature profiles. Reviewable dependency claims must therefore describe the applicable artifact graph rather than transfer whole-workspace inventory to every output. Build scripts, generated code, native libraries, system discovery, and target-specific inputs are part of the supported build realization when an artifact relies on them. This chapter governs their discoverability and reproducibility without prescribing a dependency vendor, directory layout, or named validation tool.

#### Requirements

##### ATLAS-RWC-0210 - Dependency Roles Are Distinguished

Dependency policy, inventory, and evidence MUST distinguish normal, development, and build dependencies when that distinction affects production reachability, validation, distribution, or architectural claims.

##### ATLAS-RWC-0220 - Artifact Dependency Claims Are Bounded

A claim about an artifact's dependency footprint MUST identify the applicable package or product, target, supported feature profile, and dependency roles. A complete workspace lockfile or all-features graph MUST NOT be represented as the dependency footprint of every produced artifact.

##### ATLAS-RWC-0230 - Dependency Constraints Are Explicit and Enforced

When a project imposes dependency-source, provenance, sovereignty, or external-dependency restrictions, it MUST define the scope, permitted exceptions, and affected artifact profiles. Mechanically detectable violations MUST be enforced automatically in the required validation path.

##### ATLAS-RWC-0240 - Native and Build Inputs Are Discoverable

Release-critical build scripts, native libraries, generated bindings, system-library discovery, required tools, and target-specific build inputs MUST be discoverable for every supported artifact to which they apply.

##### ATLAS-RWC-0250 - Generated and Native Build Realization Is Reproducible

Generated or native build behavior required for a supported artifact MUST identify its controlled inputs, tools, target assumptions, and required environment sufficiently to reproduce and review the supported build.

## Deferred

Per `ATLAS-GOV-STD-0001`, the following topics remain unwritten until exercised evidence requires a concrete rule:

| Topic | Trigger |
|---|---|
| Build-profile policy | Measured release/debug behavior requires deliberate profile settings beyond Cargo defaults |
| Unsafe Rust policy | Nontrivial `unsafe` Rust or FFI enters an official Atlas implementation and requires ecosystem-wide review/containment rules |
| Cross-compilation and target matrices | A release must support more than one materially different Rust target or target-specific dependency graph |
| Crate publishing mechanics | An Atlas crate is actually published to crates.io or another registry and needs workspace publication rules |
| Workspace build-profile sharing | Multiple packages need coordinated non-default Cargo profiles based on measured evidence |

Native dependencies and build scripts are no longer deferred: Chapter 8 owns their Cargo dependency-role, artifact-reachability, discoverability, and reproducible-build-input semantics. Exact developer and CI toolchain selection is also no longer deferred: ATLAS-600 Chapter 10 owns that activated workflow and environment policy. This volume continues to own Cargo `rust-version`, MSRV, workspace metadata, dependency resolution, and Cargo-specific compatibility semantics.

The existence of a Cargo mechanism is not itself a trigger. Atlas standardizes it when a real workspace has demonstrated a policy decision that needs to remain coherent across packages or repositories.
