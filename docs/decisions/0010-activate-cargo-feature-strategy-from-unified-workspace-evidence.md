# 0010 - Activate Cargo Feature Strategy from Unified Workspace Evidence

**Status:** Accepted

## Context

ATLAS-300 deferred feature-flag architecture until multiple supported feature combinations created real compatibility, dependency, or validation differences requiring shared policy. That trigger has fired in the Rusty Mill workspace at immutable revision `06ca8669f38f80291a63308de7563bfea43caab5`, recorded as [EVID-RM-FEATURES-2026-09-02](../reference/evidence-provenance.md#evid-rm-features-2026-09-02).

The 174-member workspace demonstrated that Cargo features are resolved graph behavior, not isolated switches owned only by the package whose manifest declares them. `rusty_request` has an optional feature that selects real-Tokio behavior. Workspace-wide `--all-features` enabled that feature in the unified graph; consumers executing under `rusty_tokio` then encountered real-Tokio reactor panics. Scoped package testing resolved a different graph and therefore did not represent the failing composition. Rusty Mill's affected-crate planner already acknowledges the same graph property by calculating transitive dependents from `cargo metadata --all-features`.

The incident also demonstrates an evidence boundary. An all-features run can expose combinations that narrower profiles miss, but maximal feature union is not automatically a promised product configuration. Conversely, passing a package's default or locally scoped tests cannot establish a supported unified workspace graph. A 436/436 capability manifest showed declared capability closure but did not establish runtime integration; this is consistent with Atlas's rule that maturity and validation evidence do not transfer transitively into stronger runtime, system, user-acceptance, or release-readiness claims.

The source system uses Tokio, `rusty_tokio`, particular repository scripts, and GitHub Actions. Those mechanisms explain the observed failure but are not the durable decision. Atlas needs technology-neutral Cargo requirements for explicit supported profiles, graph-representative validation, compatibility-affecting feature behavior, runtime preconditions, and impact-aware selection.

## Decision

Activate ATLAS-300's Cargo feature architecture topic and add Chapter 7 requirements `ATLAS-RWC-0140` through `ATLAS-RWC-0200`.

The chapter establishes that:

1. effective features are determined from the applicable resolved dependency graph, not inferred from one manifest;
2. materially distinct supported profiles and their compatibility and runtime preconditions are explicit;
3. `--all-features` can supply bounded stress evidence but does not replace default, minimal, or other supported-profile evidence;
4. features that alter runtime, executor, I/O, provider, serialization, wire, persistence, or comparable assumptions affect a compatibility surface;
5. a supported cross-package graph materially changed by feature unification is exercised or rejected by an equivalent automated incompatibility check;
6. impact analysis and the validation it selects use compatible feature-graph assumptions; and
7. incompatible feature/runtime assumptions fail clearly, preferably before runtime where practical, or rely on a documented and tested adapter, bridge, or precondition.

These are outcome requirements, not a universal feature layout. Atlas does not prescribe feature names, a runtime, an integration bridge, a CI provider, or one command for every workspace.

ATLAS-100 remains authoritative for architectural ownership and compatibility boundaries exposed by changed behavior. ATLAS-200 remains authoritative for version and compatibility domains and any evolution obligations on those surfaces. ATLAS-600 remains authoritative for CI orchestration and validation workflow; ATLAS-300 defines the Cargo graph and profile assumptions that such validation must represent.

## Consequences

- ATLAS-300's previously documented feature-strategy trigger is satisfied, while its other deferred topics remain deferred.
- Supported configurations require more explicit documentation and may require additional graph-aware validation or an automated incompatibility check.
- Teams must distinguish stress evidence from product support evidence and must state what each validation result establishes.
- Impact-aware CI can remain selective, but its dependency analysis and selected checks cannot silently reason from incompatible feature graphs.
- Behavior-changing features become visible compatibility concerns rather than manifest-local implementation details.
- Existing integrations may need earlier failure, profile-specific tests, or a documented and tested adapter or runtime precondition. This decision does not approve the proposed real-Tokio bridge or establish that any particular bridge is correct.

## Alternatives Rejected

- **Leave feature strategy deferred.** Rejected because the documented trigger has fired: a real unified workspace graph produced a material runtime and validation difference across packages.
- **Universally require only `--all-features`.** Rejected because maximal union is useful stress evidence but may be unsupported, mutually inconsistent, or unlike default, minimal, and other supported product profiles.
- **Treat a package's local manifest as proof of its effective resolved features.** Rejected because Cargo feature unification permits other graph participants to enable features, and the exercised scoped and workspace graphs differed materially.
- **Ban Cargo features.** Rejected because features remain a legitimate Cargo composition mechanism; the demonstrated problem is unstated support and graph assumptions, not the existence of the mechanism.
- **Standardize the proposed Tokio bridge as an Atlas-wide solution.** Rejected because its correctness is not established by this evidence and because Tokio, `rusty_tokio`, and the proposed bridge are source-system mechanisms rather than Atlas-wide architecture.
- **Move feature-graph rules into ATLAS-600.** Rejected because CI orchestration belongs there, while Cargo resolution, feature profiles, and graph semantics belong in ATLAS-300. The two volumes must agree at their boundary without transferring ownership.
