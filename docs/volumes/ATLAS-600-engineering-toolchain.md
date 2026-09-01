# ATLAS-600 - Volume VII - Engineering Toolchain

| Field | Value |
|---|---|
| Document ID | ATLAS-600 |
| Title | Volume VII - Engineering Toolchain |
| Short Name | TOOL |
| Status | Draft 0.1 |
| Classification | Normative |
| Scope | Version-control workflow, evidence-backed CI validation, development-environment setup, Rust formatting/lint validation, and monorepo management policy across Atlas repositories. Exact toolchain pinning, release automation, artifact signing, and broader compliance tooling remain deferred (see Deferred). |
| Parent | ATLAS-001 |

## Purpose

Volume VII defines the Atlas engineering toolchain where real repository workflows have already forced durable policy. The draft now covers version-control workflow, cross-repository CI validation, portable development-environment setup, the Rust formatting/lint contract demonstrated independently by more than one real Rust repository, and monorepo management demonstrated by repositories containing multiple governed first-party areas under one review and authority boundary.

The volume does not prescribe a universal CI provider, editor, development-container technology, exact compiler pin, release system, signing mechanism, third-party static-analysis suite, directory layout, CODEOWNERS implementation, or monorepo product. Those remain implementation choices or separate concerns whose own triggers must fire before becoming normative.

## Trigger Evidence

The version-control chapters are grounded in this standards library's own protected-branch and pull-request workflow. The CI chapter is grounded in exercised repositories with distinct validation needs: this standards library validates documentation structure and identifiers, while the Nexa Rust repository validates a coordinated Rust workspace plus repository-specific dependency boundaries.

The development-environment chapter is grounded in the standards library and Nexa having different but real setup models. The shared policy is that prerequisites and validation capability are durable and reproducible; a particular editor, container provider, or language toolchain is not an Atlas-wide requirement merely because one repository uses it.

The Rust formatting/lint chapter is grounded in two independent Rust repositories, Nexa and `rusty_data_os`. Both use `rustfmt` in check mode and Clippy over their governed package/target scope, and both reject Clippy warnings in required validation. Their toolchain strategies differ — one follows stable while the other uses a frozen compiler — demonstrating that the lint contract is independent from exact toolchain selection under `ATLAS-TOOL-0150`.

The monorepo chapter is grounded in those same two repositories as repository-management evidence rather than only Cargo evidence. Nexa governs applications, reusable crates, tools, content, assets, documentation, scripts, and spikes in one repository with explicit component boundaries, authority entry points, root validation, and focused-change rules. `rusty_data_os` separately governs experiments, reusable crates, tools, documentation, research evidence, and authority artifacts in one repository, with explicit graduation and synchronization rules between those areas. Both demonstrate that repository co-location is useful only when component authority, change impact, and evidence boundaries remain explicit.

### Chapter 1 - Repository and Branching Model

Atlas repositories use trunk-based development: short-lived branches cut from the default branch, merged back through review, and deleted. This is what `CONTRIBUTING.md` already describes for this repository - this chapter generalizes it across Atlas.

#### Requirements

##### ATLAS-TOOL-0001 - Trunk-Based Development

An Atlas repository MUST develop against a single long-lived default branch. It MUST NOT maintain additional long-lived integration branches (e.g. `develop`, `release/*`) unless a concrete forcing function is documented, per `ATLAS-DEP-0010`'s reasoning applied to branch topology rather than service extraction.

##### ATLAS-TOOL-0002 - Branch Naming

A working branch SHOULD be named `<scope>/<short-description>`, where `<scope>` identifies the affected area (e.g. a volume identifier, a crate name, or `fix`/`docs` for non-scoped changes). The name SHOULD let a reviewer infer what changed before opening the diff.

##### ATLAS-TOOL-0003 - Single-Purpose Branches

A branch SHOULD correspond to one coherent unit of work. Unrelated changes across unconnected scopes SHOULD NOT be bundled onto one branch, per the PR scope rule in `CONTRIBUTING.md`.

### Chapter 2 - Branch Protection

#### Requirements

##### ATLAS-TOOL-0010 - Protected Default Branch

The default branch of an Atlas repository MUST be protected: direct pushes MUST be blocked, force-pushes MUST be blocked, and branch deletion MUST be blocked. This is the repository-level mechanism that enforces `ATLAS-GOV-REVIEW-0001`.

##### ATLAS-TOOL-0011 - Required Status Checks

Merging into the default branch MUST require any automated checks defined for that repository under `ATLAS-AUTO-0001` to pass first. A failing required check MUST block merge.

##### ATLAS-TOOL-0012 - No Undocumented Bypass

An administrative override of branch protection (a force-push to the default branch, a merge with failing required checks) MUST NOT occur without a documented reason in the triggering pull request or an ADR, per `ATLAS-VAL-0011`.

### Chapter 3 - Commit Conventions

#### Requirements

##### ATLAS-TOOL-0020 - Intent-Describing Commit Messages

A commit message MUST describe the change's intent - why it was made - not merely restate what lines changed. A message such as `update file` or `fix` with no further context does not satisfy this requirement.

##### ATLAS-TOOL-0021 - Atomic Commits

A commit SHOULD represent one logical change. Unrelated changes SHOULD NOT be bundled into a single commit where splitting them would preserve reviewability.

##### ATLAS-TOOL-0022 - No Secrets in History

A commit MUST NOT introduce credentials, tokens, or other secrets into repository history. If a secret is committed, it MUST be rotated at the source - removing it in a follow-up commit alone does NOT satisfy this requirement, since history still contains it.

### Chapter 4 - Pull Request and Review Workflow

#### Requirements

##### ATLAS-TOOL-0030 - Pull Request Required

Every change to an Atlas repository's default branch MUST land through a pull request, per `ATLAS-GOV-REVIEW-0001`.

##### ATLAS-TOOL-0031 - Pull Request Rationale

A pull request description MUST state what changed and why - per ATLAS-000 Article V - especially for any substantive change under `ATLAS-GOV-CHANGE-0001`.

##### ATLAS-TOOL-0032 - Review Depth Proportional to Classification

Review depth SHOULD scale with the change classification from `ATLAS-GOV-CHANGE-0001`, per `ATLAS-GOV-REVIEW-0010`. This applies to every Atlas repository, not only the standards library.

##### ATLAS-TOOL-0033 - Focused Pull Request Scope

A pull request SHOULD be scoped to a single coherent change. Unrelated changes SHOULD be split into separate pull requests rather than bundled for convenience, per `ATLAS-NONGOAL-0041`.

### Chapter 5 - Merge and Cleanup

#### Requirements

##### ATLAS-TOOL-0040 - Declared Merge Strategy

An Atlas repository MUST declare one default merge strategy (squash, merge commit, or rebase) and apply it consistently rather than mixing strategies ad hoc per pull request.

##### ATLAS-TOOL-0041 - Branch Cleanup After Merge

A merged branch's remote copy SHOULD be deleted after merge so the repository's branch list remains actionable.

##### ATLAS-TOOL-0042 - No Rewriting Merged History

Commits already merged into the default branch MUST NOT be rewritten (force-pushed over, rebased away) except to remediate a leaked secret or a critical incident, and only as a documented exception under `ATLAS-TOOL-0012`.

### Chapter 6 - Continuous Integration Validation

CI is the repository-level execution environment for mechanically verifiable requirements. It does not own the architecture, Cargo model, documentation structure, or test semantics being checked; it provides repeatable evidence that the repository's applicable automated gates ran on the change being reviewed.

Different repositories legitimately require different commands. A documentation standards repository and a multi-crate Rust system should not have identical pipelines merely for consistency. The shared standard is therefore about **coverage, failure semantics, privilege, reproducibility, and governance of the validation pipeline**, not a universal command list or provider.

#### Requirements

##### ATLAS-TOOL-0050 - Pull Request Validation Pipeline

An Atlas repository with mechanically verifiable governing requirements MUST run an automated validation pipeline for pull requests targeting its default branch. The pipeline's required result MUST participate in the merge gate through `ATLAS-TOOL-0011`; manual review MUST NOT substitute for required machine-checkable evidence.

##### ATLAS-TOOL-0060 - Governing Validation Coverage

The required CI pipeline MUST execute the repository-wide automated checks needed to support its governing requirements and acceptance criteria, not merely a convenience smoke test of one component. A repository MAY split validation across multiple jobs or platforms, but the required merge result MUST reflect the applicable governing checks for the proposed change.

##### ATLAS-TOOL-0070 - Repository-Specific Enforcement Runs in CI

When another Atlas requirement relies on an automated repository-specific enforcement mechanism — including structural validation, architecture/dependency-boundary checks, generated-artifact validation, or equivalent machine-checkable policy — that enforcement MUST run in the required CI path for changes that can affect the governed property. Defining the check without executing it in the merge-validation path does not satisfy the automation requirement.

##### ATLAS-TOOL-0080 - Required Validation Fails Closed

A failed required CI validation MUST produce a failing required result and MUST NOT be converted to success, ignored, or silently skipped in order to permit merge. A conditional check MAY be skipped only when its applicability rule is explicit and the changed work is demonstrably outside that rule's scope; an unexpected execution failure MUST NOT be treated as an inapplicable skip.

##### ATLAS-TOOL-0090 - Least-Privilege Validation

CI validation jobs SHOULD receive only the repository, token, network, secret, and write permissions required to perform their validation. A validation job that requires write access, privileged credentials, or other elevated authority SHOULD document why the validation cannot be performed with narrower permissions. CI-provider-specific permission syntax is implementation detail.

##### ATLAS-TOOL-0100 - Locally Reproducible Validation

The substantive checks required by CI SHOULD be invocable locally through documented commands, repository scripts, or an equivalent reproducible procedure so a contributor can validate the same governed properties before requesting merge. Provider orchestration MAY differ locally; the repository MUST NOT make ordinary correctness evidence depend solely on opaque CI-only behavior when an equivalent local execution is practical.

##### ATLAS-TOOL-0110 - Default-Branch Revalidation

A repository SHOULD run its governing validation pipeline, or the applicable equivalent, after changes land on the default branch when doing so can detect event-path, merge-result, environment, or integration differences not represented by the pull-request run. Post-merge validation is detection evidence; it MUST NOT be used to justify merging a change that failed its required pre-merge validation.

##### ATLAS-TOOL-0120 - Validation-Control Changes Are Reviewable

A change that removes, disables, bypasses, or materially weakens a required CI validation MUST state which assurance is being removed and what, if anything, replaces it. Such a change MUST be reviewed as a substantive toolchain/governance change rather than treated as routine pipeline maintenance.

### Chapter 7 - Development Environment and Toolchain Setup

A development environment is successful when a maintainer can establish the prerequisites needed to build, inspect, and validate the repository from durable project information. Atlas does not require every repository to use the same editor, container, operating system, or language toolchain; repositories have different legitimate needs.

Environment automation is therefore a portability aid, not a ceremony requirement. A repository may use a development container, bootstrap script, package manager manifest, toolchain file, manual prerequisite list, or a combination. The governing requirement is that the setup model is explicit enough to reproduce the repository's required validation and does not hide compatibility assumptions in one maintainer's machine.

#### Requirements

##### ATLAS-TOOL-0130 - Documented Development Prerequisites

An Atlas repository MUST document the tools, runtimes, platform prerequisites, and setup steps required to perform its normal local build and required validation. Version constraints or compatibility floors that affect whether the repository can be built or validated correctly MUST be discoverable from repository documentation or version-controlled configuration.

##### ATLAS-TOOL-0140 - Clean-Checkout Validation Path

A repository MUST document a path from a clean checkout on a supported development platform to an environment capable of running the substantive local validation required by `ATLAS-TOOL-0100`. The path MAY contain manual steps, but it MUST NOT depend on undocumented institutional knowledge or machine-local configuration known only to an existing maintainer.

##### ATLAS-TOOL-0150 - Compatibility Floor Is Distinct From Toolchain Selection

A language or package compatibility floor, such as Cargo `rust-version`, MUST NOT be represented as an exact developer-toolchain selection unless the project deliberately makes those concerns identical. Requiring an exact toolchain version SHOULD have a documented reproducibility, compatibility, or tool-behavior reason; otherwise a toolchain satisfying the documented compatibility requirements MAY be used.

##### ATLAS-TOOL-0160 - Repository-Owned Environment Automation

Development-environment automation such as a container definition, bootstrap script, package-manager environment, or toolchain manifest MAY be provided when it reduces setup drift. If such automation is required for normal development or validation, its authoritative configuration MUST be version-controlled and the repository MUST document that it is required. Optional automation MUST NOT be presented as the only supported setup path unless the project has explicitly chosen it as a required environment boundary.

##### ATLAS-TOOL-0170 - Environment Configuration Does Not Embed Secrets

Repository-owned development-environment configuration MUST NOT embed credentials, access tokens, private keys, or machine-specific secret values. A workflow requiring a secret MUST obtain it through a documented external injection or credential mechanism rather than committing the secret as environment setup data.

##### ATLAS-TOOL-0180 - Platform-Specific Evidence Is Explicit

When a required validation or acceptance result can be produced only on a particular operating system, architecture, device class, or other environment, the repository MUST document that prerequisite and distinguish the platform-specific evidence from checks that can run in a general development environment. Passing a portable local or CI setup MUST NOT be represented as evidence for an unexecuted platform-specific requirement.

### Chapter 8 - Rust Formatting and Lint Validation

Atlas is a Rust-based ecosystem, so repeated Rust repository evidence can justify a shared Rust quality gate without requiring identical toolchain versions. `rustfmt` and Clippy are the exercised baseline: formatting is checked rather than mutated during validation, lint coverage follows the governed package/target scope, and accepted warnings do not silently accumulate.

This chapter owns the shared formatter/lint execution policy. It does not replace ATLAS-300's Cargo architecture, Chapter 6's CI semantics, or Chapter 7's toolchain-selection rules.

#### Requirements

##### ATLAS-TOOL-0190 - Rustfmt Is the Canonical Rust Formatter

An official Atlas Rust repository MUST use `rustfmt` as the canonical formatter for governed Rust source and MUST include a non-mutating formatting check in required validation. CI MUST report formatting drift as a failure rather than silently rewriting source and accepting the rewritten result.

##### ATLAS-TOOL-0200 - Clippy Covers the Governed Rust Scope

An official Atlas Rust repository MUST run Clippy in required validation across the workspace or other governed first-party package set and across all targets applicable to that validation environment. Linting only one convenience crate or target MUST NOT substitute for the governed repository scope.

##### ATLAS-TOOL-0210 - Clippy Warnings Fail Required Validation

Clippy warnings in the governed validation scope MUST fail required validation. A project MAY intentionally allow or configure a specific lint, but the exception MUST be explicit in version-controlled source or configuration rather than implemented by ignoring the required lint result in CI.

##### ATLAS-TOOL-0220 - Lint Scope Exceptions Are Explicit

A package or target MAY be excluded from the general Clippy gate when it genuinely requires a different platform, toolchain, generated-code treatment, or other separately governed validation environment. The exclusion and its required alternate evidence MUST be documented; a silently omitted package or target MUST NOT be treated as lint-validated. Platform-specific exclusions MUST remain consistent with `ATLAS-TOOL-0180`.

### Chapter 9 - Monorepo Management

A Monorepo is a repository coordination boundary, not an architectural promise that every contained component shares one owner, version, release cadence, build graph, or lifecycle. Co-location is valuable when it makes related changes atomic, repository authority discoverable, shared policy maintainable, and cross-component validation practical. It becomes harmful when physical proximity is allowed to erase component contracts or create accidental lockstep.

ATLAS-600 owns repository-level monorepo management. ATLAS-300 owns Cargo-workspace mechanics inside Rust monorepos; ATLAS-100 owns architectural boundaries and dependency direction; ATLAS-200 owns version domains and version groups.

#### Requirements

##### ATLAS-TOOL-0230 - Monorepo Is a Deliberate Coordination Boundary

A Monorepo MUST define what classes of first-party artifacts or components are intentionally coordinated through the repository and what important lifecycle, architecture, versioning, build, or release concerns remain independently governed. Repository co-location MUST NOT by itself be treated as evidence that all contained components share one version, release, deployment, owner, or Cargo workspace.

##### ATLAS-TOOL-0240 - Repository Map and Authority Entry Points

A Monorepo MUST provide a durable, discoverable map of its major first-party areas and the governing authority or starting documents a maintainer should consult before changing them. The map MAY be implemented through a README, contributor/agent guide, specification registry, generated catalog, or equivalent repository-owned artifact; a particular directory naming scheme is not required.

##### ATLAS-TOOL-0250 - Component Responsibility Boundaries Remain Explicit

Significant components or governed areas within a Monorepo MUST have explicit responsibility boundaries sufficient to determine which contract, specification, or project authority governs a proposed change. A single person MAY hold multiple responsibilities; this requirement does not mandate CODEOWNERS, separate teams, or separation of duties unless another requirement does.

##### ATLAS-TOOL-0260 - Cross-Component Contract Changes Are Atomic When Coordinated

When a contract change requires coordinated updates to multiple in-repository producers, consumers, tests, specifications, or traceability artifacts for the repository to remain coherent, those required updates SHOULD land in one reviewable change. Splitting a required coordinated update across separate merges MUST have a documented reason and MUST NOT leave the default branch knowingly inconsistent with the governing contract.

##### ATLAS-TOOL-0270 - Shared Policy Without False Uniformity

Repository-level policy, tooling, configuration, or metadata that is genuinely shared across multiple Monorepo areas SHOULD have one authoritative version-controlled source. A component with a real independent requirement MAY diverge, but the divergence MUST remain explicit rather than forcing unrelated components into a false common baseline or silently overriding the shared policy.

##### ATLAS-TOOL-0280 - Monorepo Validation Preserves Evidence Boundaries

Repository-level validation MUST preserve the applicability and evidence boundaries of the components it covers. A green root pipeline MUST NOT be represented as evidence for an excluded platform, component, lifecycle state, or separately governed acceptance gate that did not run. Impact-aware or path-scoped validation MAY be used, but skipped validation MUST satisfy the explicit applicability and fail-closed rules of `ATLAS-TOOL-0080` and applicable platform-evidence rules such as `ATLAS-TOOL-0180`.

##### ATLAS-TOOL-0290 - Repository Extraction Requires a Forcing Function

Moving a component out of a Monorepo, or creating a separately governed repository for a component that could remain inside it, SHOULD have a documented forcing function such as an independent release or dependency-resolution lifecycle, access/security boundary, ownership boundary, operational isolation need, external distribution boundary, or materially different toolchain/build governance. Repository separation SHOULD NOT be introduced solely for aesthetic directory organization or speculative future independence.

##### ATLAS-TOOL-0300 - Monorepo Topology Changes Are Substantive

A change that materially alters Monorepo component ownership, repository split/join boundaries, major dependency boundaries, validation authority, or release coordination MUST be reviewed as a substantive architecture/toolchain change. The review MUST identify the affected ATLAS-100 architecture, ATLAS-200 versioning, ATLAS-300 workspace, and ATLAS-600 workflow requirements that remain applicable after the topology change.

## Deferred

Per `ATLAS-GOV-STD-0001`, these stay unwritten until their own trigger fires, rather than being drafted speculatively now:

| Topic | Trigger |
|---|---|
| Exact toolchain pinning | Reproducibility or tool behavior demonstrates that a repository must use an exact toolchain rather than a documented compatibility floor |
| Release automation | Atlas publishes a real release artifact (crate, binary) that needs a repeatable release process |
| Artifact signing | Atlas publishes a release artifact to a registry or distribution channel where provenance (`ATLAS-VAL-0022`) needs cryptographic verification, not just a statement |
| Additional static analyzers | Two or more real repositories require the same analyzer beyond compiler/Clippy diagnostics, forcing a shared configuration or suppression policy |

The existence of a tool, editor extension, environment file, CI feature, provider capability, or monorepo product is not itself a trigger for another toolchain chapter. Atlas standardizes additional tooling when real repository evidence requires a shared policy decision.
