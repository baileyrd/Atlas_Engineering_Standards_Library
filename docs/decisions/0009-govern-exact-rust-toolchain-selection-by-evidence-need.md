# 0009 - Govern Exact Rust Toolchain Selection by Evidence Need

**Status:** Accepted

## Context

ATLAS-300 and ATLAS-600 deliberately deferred exact Rust toolchain selection until exercised evidence showed that a moving compatible compiler was insufficient. That trigger is now satisfied by the bounded `rusty_data_os` EXP-0001 evidence contract. The experiment freezes Rust `1.89.0`, the `rustfmt` and Clippy components, and target `x86_64-unknown-linux-gnu`; rejects tracking moving `stable`; requires CI to identify the exact compiler and tools used; and treats a selection change as a reviewable change to its reproducibility authorization.

The version and target are evidence from one bounded experiment, not an Atlas-wide mandate. Nexa provides the useful counterexample: it validly follows stable. Atlas therefore needs a conditional policy that distinguishes a justified exact selection from a compatibility floor and from a preference for uniformity.

Cargo `rust-version` already has a separate meaning under ATLAS-300: it states a minimum supported Rust version. Conflating that floor with the developer/CI selection would make compatibility claims and evidence identity ambiguous.

## Decision

Activate ATLAS-600 Chapter 10 for exact Rust toolchain selection and assign permanent requirements `ATLAS-TOOL-0310` through `ATLAS-TOOL-0380`.

An exact selection is required only when a documented reproducibility, compatibility, validation, or tool-behavior requirement makes a moving compatible toolchain insufficient. When required, the authoritative selection is repository-owned and machine-readable where practical; required components and targets are durably specified; required local and CI validation use and identify the governed selection; and changes to the selection revisit the evidence basis through review.

Atlas does not standardize Rust `1.89.0`, `rustup`, `rust-toolchain.toml` as the only realization mechanism, or universal exact pinning. A repository without a forcing exact-version requirement may use moving stable or another compatible selection.

ATLAS-600 owns developer/CI selection, environment identity, reproducible invocation, and selection change control. ATLAS-300 retains ownership of Cargo `rust-version`, MSRV semantics, workspace metadata, dependency resolution, and Cargo-specific compatibility rules. Exact selection does not establish platform, target, performance, runtime, or portability evidence beyond what was actually exercised.

## Consequences

- Repositories with a real evidence need have a durable way to bind developer and CI validation to one reviewable Rust toolchain identity.
- Repositories without that need are not forced into version churn or false uniformity.
- Compatibility-floor claims remain independent from the compiler selected to produce a particular validation result.
- Toolchain components and targets that affect reproducibility become part of the governed selection instead of undocumented machine state.
- CI results under an exact-selection contract carry enough identity to audit the evidence basis.
- Toolchain changes become substantive evidence changes while still allowing automation to propose reviewed updates.
- Exact compiler identity cannot be used to overstate which platforms, targets, or behaviors were validated.

## Alternatives Rejected

- **Pin every Atlas Rust repository to one exact version.** Rejected because the evidence includes a valid moving-stable strategy and does not justify ecosystem-wide lockstep.
- **Standardize the experiment's Rust `1.89.0` selection.** Rejected because it is bounded source evidence, not a universal compatibility or release decision.
- **Treat Cargo `rust-version` as the exact selection.** Rejected because an MSRV is a compatibility floor and may intentionally differ from the compiler used for normal developer and CI validation.
- **Require `rustup` and `rust-toolchain.toml`.** Rejected because Atlas needs a faithfully realized, repository-owned selection, not one installer or distribution mechanism.
- **Allow automated advancement without review.** Rejected because changing the compiler, required components, or targets changes the basis of reproducibility evidence.
- **Infer platform or behavior coverage from the pin.** Rejected because toolchain identity records the environment used; it does not prove unexecuted acceptance criteria.
