# 0011 - Activate Dependency-Role, Artifact-Reachability, and Native Build-Input Governance

**Status:** Accepted

## Context

ATLAS-300 deferred native dependencies and build scripts until a release-critical package introduced build scripts, native linking, generated bindings, or system-library discovery. That trigger has fired in the Rusty Mill workspace at immutable revision `77df1d62e0d328a86f54dedb226e5204a0e42fad`, recorded as [EVID-RM-DEPS-2026-09-03](../reference/evidence-provenance.md#evid-rm-deps-2026-09-03).

At that revision, the root workspace declared approximately 183 members and the repository tracked 199 Cargo manifests. The manifests and resolved lockfile distinguish normal, development, and build dependencies and include registry and git sources. Multiple tracked `build.rs` files and resolved packages expose native-library linking, generated bindings, and system integration. These roles do not have identical production reachability: a development dependency can be a non-shipping test oracle, while a build dependency can materially affect a shipped artifact without becoming a runtime library dependency.

The evidence also exposes a claim boundary. One workspace lockfile records resolution for a coordination boundary containing many packages and targets; it does not prove that every output ships or executes every resolved package. A meaningful dependency-free or dependency-footprint claim consequently needs a named package or product, target, supported feature profile, relevant dependency roles, and artifact boundary.

Rusty Mill additionally states a project-specific dependency-sovereignty objective and enforces detectable source restrictions in required CI. The objective is evidence that such a policy needs explicit scope and mechanical enforcement, not evidence that every Atlas project should adopt the same policy.

## Decision

Activate one bounded ATLAS-300 chapter, “Cargo Dependency Roles, Artifact Reachability, and Native Build Inputs,” with requirements `ATLAS-RWC-0210` through `ATLAS-RWC-0250`.

The chapter requires dependency roles to remain distinct when material to claims; bounds artifact dependency claims by package or product, target, supported feature profile, and roles; makes project-selected dependency restrictions explicit and mechanically enforced where detectable; and makes release-critical native and generated build inputs discoverable and reproducible.

These are technology-neutral outcomes. A conforming project selects mechanisms appropriate to its graph and validation environment. Atlas does not universally prohibit external dependencies: external packages can be deliberate, reviewable implementation inputs, and development-only dependencies can provide useful independent test oracles without shipping in an artifact. Any project choosing stricter provenance, sovereignty, or source constraints must state and enforce its own bounded policy.

ATLAS-500 supply-chain security remains separate and deferred. Inventory and build realization establish what inputs apply and how they can be reviewed; they do not establish ecosystem-wide integrity verification, signing, provenance attestations, vulnerability response, or compromise handling. Those security controls require their own future trigger and evidence.

## Consequences

- Dependency inventories and architectural assertions require role-aware interpretation rather than one undifferentiated count.
- Artifact-footprint and dependency-free claims become narrower but reviewable and reproducible.
- Project-specific dependency restrictions require declared scope, exceptions, artifact profiles, and automatic enforcement of detectable violations in required validation.
- Supported artifacts that depend on build scripts, generated bindings, native libraries, system discovery, or target-specific tooling incur documentation and reproducibility obligations.
- Whole-workspace lockfiles and all-features graphs remain valuable resolution and stress evidence but cannot be relabeled as every artifact's shipping graph.
- Build profiles, unsafe Rust, publishing, cross-compilation, and workspace profile sharing remain deferred, and no ATLAS-500 requirement is activated.

## Alternatives Rejected

- **Leave native/build-input governance deferred.** Rejected because the documented trigger has fired in exercised, release-relevant workspace evidence.
- **Universally prohibit external dependencies.** Rejected because dependency acceptability is an artifact- and project-specific architectural decision; external development dependencies may also be intentionally non-shipping test oracles.
- **Mandate `cargo-deny`, `cargo-audit`, `cargo-vet`, or another named tool.** Rejected because the durable requirement is automatic enforcement and reviewable evidence, not one implementation. No single named tool proves every dependency role, artifact graph, native input, policy, or security property.
- **Mandate one workspace directory layout.** Rejected because filesystem organization does not itself establish dependency role, reachability, provenance, or reproducibility.
- **Require exhaustive feature combinations.** Rejected because combinatorial enumeration may be infeasible and may include unsupported graphs. Chapter 7 already governs explicit supported profiles and graph-representative validation.
- **Treat the lockfile as every artifact's bill of materials.** Rejected because a whole-workspace resolution can contain dependencies unreachable from a particular package, target, feature profile, or production role.
- **Activate ATLAS-500 supply-chain security simultaneously.** Rejected because this evidence supports dependency and build-input governance, not a complete Atlas-wide provenance, integrity, signing, vulnerability, or compromise-response policy.
