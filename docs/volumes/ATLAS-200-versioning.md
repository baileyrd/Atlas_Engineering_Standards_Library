# ATLAS-200 - Volume III - Ecosystem Versioning Standard

| Field | Value |
|---|---|
| Document ID | ATLAS-200 |
| Title | Volume III - Ecosystem Versioning Standard |
| Short Name | EVS |
| Status | Draft 0.1 |
| Classification | Normative |
| Scope | Version domains, cross-crate grouping, the pre-1.0 semantic versioning rule, and cross-repository pinning for Atlas crates and workspaces |
| Parent | ATLAS-001 |

## Purpose

Volume III defines how versioning works across an Atlas ecosystem made of multiple crates, workspaces, and sibling repositories. Unlike the rest of the seeded volumes (ATLAS-100, ATLAS-300 through ATLAS-900), this volume has a real, current trigger: a proven, argued versioning policy already exists for a sibling Rust ecosystem and is transcribed here rather than invented speculatively.

This draft deliberately does not cover every version domain in the volume's eventual scope. API, ABI, protocol, schema, and configuration versioning, release channels, long-term support, and capability negotiation are real future chapters — but nothing in the ecosystem yet exercises them the way crate and workspace versioning already have been exercised. Per `ATLAS-GOV-STD-0001`, they stay unwritten until their own trigger fires; see [Deferred](#deferred) below rather than a plausible-sounding chapter list for them.

### Chapter 1 - Versioning Philosophy

Atlas treats compatibility as multi-dimensional. A crate's version, a workspace's coordinated snapshot, and a downstream consumer's pinned dependency each answer a different question — "can I upgrade this crate," "does this snapshot cohere," "does what I depend on still work" — and collapsing them into one number answers none of them precisely.

#### Requirements

##### ATLAS-EVS-0001 - No Ecosystem-Wide Version

Atlas MUST NOT define a single ecosystem-wide version number. Each consumer's own dependency resolution (lockfile, pinned revision) is the combination of the versions it depends on, computed independently per consumer — not a shared number every component is forced onto. A version shared by components with no real dependency on each other is coupling expressed as a number instead of code, which `ATLAS-PHIL-0102` already prohibits in code.

##### ATLAS-EVS-0002 - Version Domain Independence

A change in one version domain MUST NOT force a version bump in another domain unless a real dependency exists between them.

### Chapter 2 - Version Domains

#### Requirements

##### ATLAS-EVS-0010 - Recognized Domains

Atlas recognizes two version domains by default: the **crate** (a single publishable unit) and the **workspace** (a coordinated snapshot of multiple crates at a point in time, used for internal coordination — not published as a single artifact, per `ATLAS-EVS-0001`). Additional domains (API, ABI, protocol, schema) MAY be introduced once the volume covering them has a fired trigger (`ATLAS-GOV-STD-0001`); see Deferred.

### Chapter 3 - Grouping by Coupling

Not every crate in a workspace needs the same versioning treatment, and neither full lockstep (one version for everything) nor full independence (a separate version for every crate) is the default. The grouping follows evidence of actual coupling, not a rule picked in advance.

#### Requirements

##### ATLAS-EVS-0020 - Group by Demonstrated Coupling

Crates that provably change together in the same pull requests (a trait and every backend that must implement it in lockstep to keep compiling) SHOULD share one version. Crates with independently demonstrated lifecycles SHOULD version independently.

##### ATLAS-EVS-0021 - Grouping Is Revisable

A crate's version-group membership MAY change if its actual coupling pattern changes. The initial grouping is a starting hypothesis based on observed behavior, not a permanent commitment.

### Chapter 4 - The Pre-1.0 Surface Rule

Standard SemVer's `0.y.z` leaves the actual convention ambiguous — some treat `y` as breaking-only, others bump it for any public change. Atlas picks one, explicitly, rather than leaving it to individual judgment every time.

> **At `0.y.z`: any change to the public API surface — additive or breaking — bumps `y`. `z` is reserved for changes that touch no public item's shape at all** (a fix inside an existing function's body, a doc correction, an internal refactor, a test-only change).

The reason this is stricter than the common "additive changes are patch-level" reading: a public trait is consumed on two sides. Adding a method to a trait is additive for every existing *caller*, but breaking for every existing *implementer* — it won't compile until they add the new method too. A crate whose public surface is mostly traits doesn't get to assume additive means safe the way a struct-and-functions crate can.

#### Worked Example

| Change | Bump | Why |
|---|---|---|
| New public trait added | `0.1.0` → `0.2.0` | new public surface |
| Existing trait gains a required method | `0.2.0` → `0.3.0` | breaking for implementers, even though additive for callers |
| Bug fix inside an existing function, no signature change | *no bump* | touches no public item's shape |
| Internal refactor, public surface unchanged | *no bump* | same |

#### Requirements

##### ATLAS-EVS-0030 - Pre-1.0 Surface Rule

While a crate is at `0.y.z`, any change to its public API surface — additive or breaking — MUST bump `y`. `z` is reserved for changes touching no public item's shape.

##### ATLAS-EVS-0031 - Two-Sided Surface Evaluation

Whether a change is additive MUST be evaluated per `ATLAS-IFACE-0001` from every consumer role a surface has. A public trait gaining a required method is additive for callers and breaking for implementers, and MUST be treated as a `y` bump.

##### ATLAS-EVS-0032 - 1.0 Is a Decision, Not a Schedule

Moving a crate to `1.0` MUST be a deliberate decision justified by the surface having stabilized — no capability-driven growth for a meaningful period — not a default triggered by elapsed time or version count.

### Chapter 5 - Cross-Repository Pinning

A git dependency on a sibling Atlas repository is a real trust boundary (`ATLAS-BOUND-0001`): the dependent has no signal about compatibility unless the dependency is pinned.

#### Requirements

##### ATLAS-EVS-0040 - Pin, Never Track

A dependency on a sibling Atlas repository MUST pin a specific commit (`rev`) or tag. It MUST NOT track a branch.

##### ATLAS-EVS-0041 - Consumer-Triggered Tagging

A tag SHOULD be cut when an external consumer is actually about to pin against that state, not speculatively on every merge, per `ATLAS-PHIL-0102`.

##### ATLAS-EVS-0042 - Deliberate Pin Bumps

Bumping an existing pin MUST be a reviewable, deliberate diff, not an incidental side effect of an unrelated dependency resolution.

### Chapter 6 - Release Mechanics

#### Requirements

##### ATLAS-EVS-0050 - Bump With the Change

A version bump MUST land in the same pull request as the public-surface change that requires it, per `ATLAS-GOV-CHANGE-0010`, not deferred to a separate release pull request.

##### ATLAS-EVS-0051 - Changelog Per Bump

A crate or version group with independent versioning MUST maintain a changelog recording what triggered each bump.

## Deferred

Per `ATLAS-GOV-STD-0001`, these stay unwritten until their own trigger fires, rather than being drafted speculatively now:

| Topic | Trigger |
|---|---|
| API / ABI versioning | A component ships a dynamically-loaded or FFI surface (ties to ATLAS-700's own trigger) |
| Protocol versioning | Atlas components communicate over a real wire protocol between processes |
| Schema versioning | Atlas serializes data with a schema that must evolve across versions in production |
| Configuration versioning | A configuration format needs to remain readable across incompatible Atlas versions |
| Release channels / LTS | Atlas has real external users who need a stability guarantee beyond "whatever's on `main`" |
| Capability negotiation | Two Atlas components need to negotiate which optional features they both support at runtime |
