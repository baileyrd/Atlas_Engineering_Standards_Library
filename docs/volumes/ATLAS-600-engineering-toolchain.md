# ATLAS-600 - Volume VII - Engineering Toolchain

| Field | Value |
|---|---|
| Document ID | ATLAS-600 |
| Title | Volume VII - Engineering Toolchain |
| Short Name | TOOL |
| Status | Draft 0.1 |
| Classification | Normative |
| Scope | Version control workflow (branching, commits, pull requests, review, merge) across Atlas repositories. Development environments, build systems, testing frameworks, static analysis, CI/CD, release automation, and compliance tooling remain Seed (see Deferred). |
| Parent | ATLAS-001 |

## Purpose

Volume VII defines the Atlas engineering toolchain - CI/CD, linting, release automation, artifact signing, and version control workflow. This draft covers only the latter: how Atlas repositories use git - branching, commits, pull requests, review, and merge mechanics. It exists as its own chapter group rather than waiting for the rest of the volume because it has its own fired trigger, independent of CI/CD, linting, release automation, or artifact signing.

## Trigger

This standards library's own `CONTRIBUTING.md`, branch protection on `main`, and the `validate-docs` CI check are already a real, working git workflow - not a plausible-sounding proposal. Per `ATLAS-AUTO-0010`, a second real instance of toolchain automation (branch protection enforcing the PR workflow, alongside the existing `validate-docs` check) is what promotes this slice from Seed to Draft: the pattern is being formalized because it has already been observed twice, not invented speculatively. This follows the same pattern ATLAS-200 used: transcribing a proven, argued policy rather than drafting one from a chapter list.

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

## Deferred

Per `ATLAS-GOV-STD-0001`, these stay unwritten until their own trigger fires, rather than being drafted speculatively now:

| Topic | Trigger |
|---|---|
| CI/CD pipeline standards | A second Atlas repository runs a CI pipeline beyond this library's `validate-docs` workflow, forcing a real choice about shared pipeline structure |
| Linting / static analysis tooling | Atlas has a real Rust crate whose lint configuration needs to be shared across repositories |
| Release automation | Atlas publishes a real release artifact (crate, binary) that needs a repeatable release process |
| Artifact signing | Atlas publishes a release artifact to a registry or distribution channel where provenance (`ATLAS-VAL-0022`) needs cryptographic verification, not just a statement |
| Development environment standards | A second Atlas repository exists with its own toolchain/environment setup to reconcile with this one |
