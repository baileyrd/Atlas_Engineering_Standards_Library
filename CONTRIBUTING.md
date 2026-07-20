# Contributing to the Atlas Engineering Standards Library

Atlas standards are durable engineering artifacts. Changes to them should be deliberate, traceable, and reviewed — this document describes the workflow that enforces that in practice.

## Branch Protection

`main` is protected:

- Changes land only through pull requests. Direct pushes to `main` are blocked.
- Force-pushes and branch deletion are blocked on `main`.
- A `validate-docs` CI check runs on every PR (requirement-ID uniqueness and prefix registration, SUMMARY.md reachability, internal link validity — see `tools/validate_docs.py`) and **must pass before a PR can merge**.

## Workflow

1. **Branch from `main`.** Use a short, descriptive branch name, e.g. `atlas-500/crypto-requirements` or `fix/terminology-typo`.
2. **Make your change.** See [Authoring Conventions](#authoring-conventions) below for document- and requirement-level rules.
3. **Run `python tools/validate_docs.py` locally** before opening the PR — it catches duplicate/unregistered requirement IDs and broken internal links.
4. **Open a pull request into `main`.** Describe *what* changed and, per Article V (Governance Principles) of [ATLAS-000](docs/ATLAS-000-foundation-charter.md), the rationale — especially for anything touching a normative requirement.
5. **Review.** Changes to normative requirements require review for correctness, security, compatibility, maintainability, and ecosystem impact (ATLAS-000, Article V). For editorial or structural changes (typos, formatting, non-normative prose), a lighter pass is sufficient.
6. **Merge.** Squash or merge once the PR reflects the intended change and any review feedback is addressed. Delete the branch after merge.

## Authoring Conventions

- **Requirement identifiers are permanent.** Never reuse or renumber an existing identifier (ATLAS-CHARTER-0006). If a requirement is removed, retire it — record the retirement in the document rather than deleting the identifier.
- **New requirements** should follow the format in [docs/templates/requirement-template.md](docs/templates/requirement-template.md).
- **New requirement-ID prefixes or chapters** must be registered in [docs/reference/requirement-registry.md](docs/reference/requirement-registry.md) in the same PR — see that file for the numbering convention and shared domain families (e.g. `SEC-*`).
- **New volumes** should start from [docs/templates/volume-template.md](docs/templates/volume-template.md).
- **Use RFC-style normative language** (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`) as defined in [README.md](README.md#normative-language) — don't introduce ad hoc requirement phrasing.
- **Foundational changes** — anything touching [ATLAS-000](docs/ATLAS-000-foundation-charter.md) or the core doctrine in [ATLAS-001](docs/volumes/ATLAS-001-foundation.md) — require unusually strong justification (ATLAS-000, Article V) and should be flagged as such in the PR description.
- **Breaking changes to a public contract** must be intentional, documented, reviewed, versioned, and accompanied by migration guidance where practical (ATLAS-CHARTER-0007).
- Keep the status table in [README.md](README.md#library-status) in sync when a document's `Status` field changes.

## Scope of PRs

Keep pull requests focused on a single document, requirement set, or clearly related change. Avoid bundling unrelated edits across volumes — it makes review and traceability harder.
