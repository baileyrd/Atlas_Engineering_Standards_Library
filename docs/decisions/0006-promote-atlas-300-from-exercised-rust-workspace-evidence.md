# 0006 - Promote ATLAS-300 from Exercised Rust Workspace Evidence

**Status:** Accepted

## Context

ATLAS-300 was intentionally left as a Seed until a real Rust repository contained enough cooperating packages to force choices about workspace layout, shared manifest policy, dependency grouping, and Cargo-level coordination. A single crate does not need a standard for workspace membership, shared package metadata, local path dependencies, or version inheritance.

That condition is now satisfied by Nexa, the same concrete Rust system that supplied the architecture and program-integrity evidence already incorporated into Atlas. Its root Cargo workspace contains applications, tools, and numerous cooperating first-party crates. The exercised workspace makes specific choices that are no longer hypothetical:

- the repository has one explicit root Cargo workspace for coordinated packages;
- the virtual workspace declares its resolver explicitly;
- edition, license, and MSRV are centralized under `[workspace.package]` and inherited by many members;
- shared third-party dependency baselines are centralized under `[workspace.dependencies]`;
- first-party crate dependencies resolve through workspace-local paths;
- some packages inherit the workspace version while Cargo also permits explicit package versions, making the expression of ATLAS-200 version-group decisions a real concern;
- the repository tracks a root `Cargo.lock` while producing applications and tools;
- architecture-critical dependency rules are enforced from `cargo metadata`, `cargo tree`, manifest/source inspection, and workspace-wide Cargo commands rather than review alone;
- the declared `rust-version` is an MSRV compatibility floor while CI currently uses a newer stable toolchain, demonstrating that MSRV and exact toolchain selection are distinct concerns.

The trigger therefore no longer asks Atlas to invent a preferred Cargo layout. A real multi-package system has already demonstrated which workspace decisions must stay coherent.

## Decision

Promote ATLAS-300 from `Seed` to `Draft 0.1`.

The initial draft standardizes only the Cargo/workspace rules supported by exercised evidence:

1. coordinated first-party Rust packages use an explicit Cargo workspace boundary and intended membership is deliberate;
2. virtual workspaces declare their feature resolver explicitly;
3. genuinely shared package metadata is centralized and inherited while real differences stay visible;
4. genuinely shared third-party dependency policy is centralized under workspace dependencies;
5. dependencies on first-party members resolve to workspace-local packages during workspace development;
6. normal Cargo dependency edges follow governing architecture and critical mechanically detectable boundary violations are automatically checked;
7. Cargo workspace-version inheritance expresses an ATLAS-200 version-group decision rather than creating one;
8. official packages declare an MSRV, with shared floors inherited where appropriate, and MSRV remains distinct from exact toolchain selection;
9. application/repository-built artifact workspaces track the root lockfile and treat lockfile changes as deliberate resolved-dependency changes.

The initial draft does not standardize the source repository's crate names, `apps/`/`crates/`/`tools/` directory naming, product metadata, exact Rust edition, exact MSRV number, dependency versions, or CI provider.

Feature-flag architecture, build-profile tuning, unsafe Rust policy, cross-compilation, registry publishing, native build scripts, and exact toolchain pinning remain deferred until their own evidence creates a real decision.

## Consequences

- ATLAS-300 becomes an active Cargo/workspace standard grounded in a real multi-package Rust system.
- `RWC` moves from the Seed reservation table into the active requirement registry.
- ATLAS-100 remains authoritative for architecture. ATLAS-300 may require Cargo dependency edges and automated graph checks to preserve that architecture, but it does not redefine the architecture itself.
- ATLAS-200 remains authoritative for version grouping. `version.workspace = true` is treated as Cargo expression of a version-group decision, not as evidence that every workspace member should version in lockstep.
- ATLAS-600 remains authoritative for CI and developer-tool workflow. ATLAS-300 defines Cargo structures and invariants that CI can inspect but does not prescribe pipeline structure.
- The Nexa CI evidence separately fires ATLAS-600's deferred CI/CD trigger; that follow-up should be handled independently rather than bundled into this promotion.

## Alternatives Rejected

- **Keep ATLAS-300 as Seed until Atlas itself hosts multiple Rust crates.** Rejected because the standards library has already adopted real sibling-system evidence as a valid trigger source for ATLAS-100 and ATLAS-200. The relevant question is whether the engineering decision has been exercised, not which repository owns the source code.
- **Copy the Nexa workspace layout literally.** Rejected because directory names and crate names are product organization, not durable Cargo policy.
- **Require every workspace member to inherit one version.** Rejected because ATLAS-200 explicitly groups by demonstrated coupling; Cargo workspace version inheritance must follow that decision rather than override it.
- **Put CI commands such as `cargo clippy` and `cargo test` in this volume.** Rejected because pipeline and tool invocation are ATLAS-600 concerns. This volume owns the Cargo workspace and manifest semantics those tools operate on.
- **Draft feature, profile, unsafe, publishing, cross-target, and build-script rules now.** Rejected under `ATLAS-GOV-STD-0001` and `ATLAS-PHIL-0102`; the current evidence does not justify pretending those decisions have been exercised.
