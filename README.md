# Atlas Engineering Standards Library

The Atlas Engineering Standards Library is a normative standards library for a Rust-based software ecosystem. It defines the philosophy, architecture, versioning model, cargo and workspace rules, SDK expectations, security architecture, toolchain policy, plugin model, ecosystem standards, and reference architectures for Atlas.

Atlas treats engineering standards as first-class artifacts. A standard is not merely explanatory documentation; it is a durable contract that can guide design, implementation, review, automation, testing, release engineering, and long-term maintenance.

## Library Status

| Document | Title | Status |
|---|---|---|
| [ATLAS-000](docs/ATLAS-000-foundation-charter.md) | Foundation Charter | Draft 0.1 |
| [ATLAS-001](docs/volumes/ATLAS-001-foundation.md) | Volume I - Foundation | Draft 0.1 |
| [ATLAS-100](docs/volumes/ATLAS-100-architecture.md) | Volume II - Architecture | Draft 0.1 |
| [ATLAS-200](docs/volumes/ATLAS-200-versioning.md) | Volume III - Ecosystem Versioning Standard | Draft 0.1 |
| [ATLAS-300](docs/volumes/ATLAS-300-rust-workspace-cargo.md) | Volume IV - Rust Workspace and Cargo Architecture | Draft 0.1 |
| [ATLAS-400](docs/volumes/ATLAS-400-sdk-architecture.md) | Volume V - SDK Architecture | Seed |
| [ATLAS-500](docs/volumes/ATLAS-500-security-architecture.md) | Volume VI - Security Architecture | Seed |
| [ATLAS-600](docs/volumes/ATLAS-600-engineering-toolchain.md) | Volume VII - Engineering Toolchain | Draft 0.1 |
| [ATLAS-700](docs/volumes/ATLAS-700-plugin-extension-architecture.md) | Volume VIII - Plugin and Extension Architecture | Seed |
| [ATLAS-800](docs/volumes/ATLAS-800-ecosystem-standards.md) | Volume IX - Ecosystem Standards | Seed |
| [ATLAS-900](docs/volumes/ATLAS-900-reference-architectures.md) | Volume X - Reference Architectures | Seed |

## Document Hierarchy

```text
Library
    Volume
        Part
            Chapter
                Section
                    Requirement
```

## Requirement Identifiers

Every normative requirement receives a permanent identifier.

```text
ATLAS-FND-0001
ATLAS-PHIL-0010
ATLAS-CORR-0050
ATLAS-EVS-API-0107
ATLAS-SEC-CRYPTO-0182
```

Requirement identifiers are never reused. If a requirement is removed, its identifier remains reserved and its retirement is recorded in the relevant document history.

## Normative Language

Atlas uses RFC-style requirement language:

- `MUST` indicates an absolute requirement.
- `MUST NOT` indicates an absolute prohibition.
- `SHOULD` indicates a strong recommendation with valid exceptions.
- `SHOULD NOT` indicates a discouraged practice with possible exceptions.
- `MAY` indicates an explicitly permitted option.

## Documentation Site

[`docs/SUMMARY.md`](docs/SUMMARY.md) is an [mdBook](https://rust-lang.github.io/mdBook/) table of contents covering everything under `docs/`. Preview it locally with:

```sh
mdbook serve
```

`book.toml` points `src` at `docs/` specifically (not the repo root) so the build only ever touches library content — this README and CONTRIBUTING.md are intentionally outside the book and stay as plain GitHub-rendered docs. The build output (`book/`) is gitignored and not currently published anywhere.

## Working Model

Atlas evolves from specification to implementation:

```text
Vision
Principles
Architecture
Standards
Requirements
Tests
Code
Artifacts
Deployments
Operations
```

No official ecosystem capability should become stable without a governing specification, an ownership model, compatibility expectations, lifecycle status, and verification strategy.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the PR workflow and authoring conventions.

## License

This library is licensed under [CC BY 4.0](LICENSE) (Creative Commons Attribution 4.0 International). You may use, adapt, and redistribute these standards, including commercially, as long as you give appropriate credit to Atlas.
