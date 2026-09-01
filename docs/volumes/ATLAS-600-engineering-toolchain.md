# ATLAS-600 - Volume VII - Engineering Toolchain

| Field | Value |
|---|---|
| Document ID | ATLAS-600 |
| Title | Volume VII - Engineering Toolchain |
| Short Name | TOOL |
| Status | Draft 0.1 |
| Classification | Normative |
| Scope | Version-control workflow, evidence-backed CI validation, and development-environment setup policy across Atlas repositories. Lint/static-analysis policy, exact toolchain pinning, release automation, artifact signing, and broader compliance tooling remain deferred (see Deferred). |
| Parent | ATLAS-001 |

## Purpose

Volume VII defines the Atlas engineering toolchain where real repository workflows have already forced durable policy. The initial draft standardized version-control workflow, then added cross-repository CI validation once a second exercised pipeline created a real reconciliation need. A second repository now also provides a materially different local development environment, so this draft defines the portable setup rules common to both without requiring identical tools.

The volume does not prescribe a universal CI provider, editor, development-container technology, Rust lint configuration, exact compiler pin, release system, or signing mechanism. Those remain implementation choices or separate concerns whose own triggers must fire before becoming normative.

## Trigger Evidence

The version-control chapters are grounded in this standards library's own protected-branch and pull-request workflow. The CI chapter is grounded in two exercised repositories with distinct validation needs:

- this standards library validates requirement identifiers, documentation reachability, and internal links on pull requests and on the default branch; and
- the Nexa Rust repository validates its coordinated workspace through build/test gates plus repository-specific dependency-boundary enforcement, also on pull requests and on the default branch.

The two pipelines use different languages and checks but share the same engineering shape: governing rules have machine-checkable evidence, pull requests cannot rely on manual review alone, and repository-specific structural checks are first-class CI inputs rather than optional local conventions.

The development-environment chapter is grounded in the same two repositories having different but real setup models. The standards library documents Python-based local validation and mdBook usage without requiring a container. Nexa documents Rust/Cargo validation and also carries repository-owned development-container configuration. The shared policy is therefore that setup prerequisites and validation capability are durable and reproducible; a particular editor, container provider, or language toolchain is not an Atlas-wide requirement merely because one repository uses it.

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

## Deferred

Per `ATLAS-GOV-STD-0001`, these stay unwritten until their own trigger fires, rather than being drafted speculatively now:

| Topic | Trigger |
|---|---|
| Linting / static analysis tooling | Atlas has a real Rust crate whose lint configuration needs to be shared across repositories — trigger review tracked in Issue #30 |
| Exact toolchain pinning | Reproducibility or tool behavior demonstrates that a repository must use an exact toolchain rather than a documented compatibility floor |
| Release automation | Atlas publishes a real release artifact (crate, binary) that needs a repeatable release process |
| Artifact signing | Atlas publishes a release artifact to a registry or distribution channel where provenance (`ATLAS-VAL-0022`) needs cryptographic verification, not just a statement |

The existence of a tool, editor extension, environment file, CI feature, or provider capability is not itself a trigger for another toolchain chapter. Atlas standardizes additional tooling when real repository evidence requires a shared policy decision.
