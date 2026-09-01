# ATLAS-300 - Volume IV - Rust Workspace and Cargo Architecture

| Field | Value |
|---|---|
| Document ID | ATLAS-300 |
| Title | Volume IV - Rust Workspace and Cargo Architecture |
| Short Name | RWC |
| Status | Draft 0.1 |
| Classification | Normative |
| Scope | Rust workspace coordination, Cargo manifest inheritance, dependency-graph policy, version expression, MSRV declaration, and lockfile reproducibility |
| Parent | ATLAS-001 |

## Purpose

Volume IV defines how Atlas uses Cargo workspaces and manifests once a Rust repository contains multiple cooperating packages. ATLAS-001 owns general dependency and reproducibility doctrine, ATLAS-100 owns architectural dependency direction, ATLAS-200 owns version-group semantics, and ATLAS-600 owns CI/toolchain workflow. This volume defines the Cargo-specific representation that keeps those decisions coherent across a real multi-crate workspace.

This first draft is intentionally narrower than the volume's eventual scope. The original Seed trigger has fired through exercised multi-crate workspace evidence recorded in ADR-0006, but feature strategy, build-profile policy, unsafe Rust, publishing, cross-compilation, native build integration, and exact toolchain pinning remain deferred until real work forces those decisions.

## Trigger Evidence

The Seed trigger is satisfied by a real Rust workspace containing applications, tools, and numerous cooperating crates. That workspace already makes concrete choices about explicit membership, a virtual-workspace resolver, inherited edition/license/MSRV metadata, shared third-party dependencies, local path dependencies, workspace-version inheritance, a committed lockfile, and automated Cargo dependency-boundary checks. See [ADR-0006](../decisions/0006-promote-atlas-300-from-exercised-rust-workspace-evidence.md).

## Relationship to Other Volumes

- ATLAS-100 determines which dependency directions and ownership boundaries are architecturally valid; this volume governs how Cargo manifests express and mechanically expose them.
- ATLAS-200 determines which crates belong to the same version group; this volume governs when Cargo workspace-version inheritance expresses that decision.
- ATLAS-600 determines how CI invokes Cargo and other tools; this volume defines the workspace and manifest properties those tools validate.

### Chapter 1 - Workspace Coordination Boundary

A Cargo workspace is a coordination boundary: packages inside it share dependency resolution, a lockfile, target output, root-level commands, and workspace metadata. It should therefore contain packages that are intentionally developed and validated together, not merely packages that happen to live in the same repository.

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

Cargo `rust-version` MUST be treated as a minimum compatibility floor, not as an exact developer or CI toolchain pin. Exact toolchain selection, when required, MUST be governed separately so that using a newer supported compiler does not falsely imply the declared MSRV has changed.

### Chapter 6 - Lockfile and Resolved Dependency State

A workspace that produces an application or repository-built release artifact needs a reviewable record of the exact dependency resolution used to build and test that artifact. Cargo's lockfile is that record; it is not a replacement for manifest compatibility constraints.

#### Requirements

##### ATLAS-RWC-0120 - Application Workspace Lockfile

A Cargo workspace that produces an application, executable tool, or other repository-built release artifact MUST track its root `Cargo.lock` in version control so the resolved dependency graph used by normal builds and validation is reviewable and reproducible. This requirement does not make a library consumer's resolution part of the library's public compatibility contract.

##### ATLAS-RWC-0130 - Lockfile Changes Are Deliberate

A `Cargo.lock` change MUST be attributable to an intended dependency-resolution change, manifest change, or tool-supported lockfile maintenance action. Unexplained or unrelated lockfile churn MUST NOT be accepted merely because the workspace still builds.

## Deferred

Per `ATLAS-GOV-STD-0001`, the following topics remain unwritten until exercised evidence requires a concrete rule:

| Topic | Trigger |
|---|---|
| Feature-flag architecture | Multiple supported feature combinations create real compatibility, dependency, or validation differences that require a shared policy |
| Build-profile policy | Measured release/debug behavior requires deliberate profile settings beyond Cargo defaults |
| Unsafe Rust policy | Nontrivial `unsafe` Rust or FFI enters an official Atlas implementation and requires ecosystem-wide review/containment rules |
| Cross-compilation and target matrices | A release must support more than one materially different Rust target or target-specific dependency graph |
| Crate publishing mechanics | An Atlas crate is actually published to crates.io or another registry and needs workspace publication rules |
| Native dependencies and build scripts | A release-critical package introduces `build.rs`, native linking, generated bindings, or system-library discovery |
| Exact toolchain pinning | Reproducibility or tool-specific behavior requires developers/CI to use an exact Rust toolchain; workflow ownership belongs with ATLAS-600 |
| Workspace build-profile sharing | Multiple packages need coordinated non-default Cargo profiles based on measured evidence |

The existence of a Cargo mechanism is not itself a trigger. Atlas standardizes it when a real workspace has demonstrated a policy decision that needs to remain coherent across packages or repositories.
