# ATLAS-200 - Volume III - Ecosystem Versioning Standard

| Field | Value |
|---|---|
| Document ID | ATLAS-200 |
| Title | Volume III - Ecosystem Versioning Standard |
| Short Name | EVS |
| Status | Planned |
| Classification | Normative |
| Scope | Version domains, compatibility rules, and lifecycle policy for specifications, crates, components, APIs, ABIs, protocols, schemas, and artifacts |
| Parent | ATLAS-001 |

## Purpose

Volume III defines the Atlas versioning model for a Rust-based ecosystem. Semantic versioning remains useful at the crate level, but Atlas requires a broader compatibility and lifecycle system for specifications, workspaces, components, APIs, ABIs, protocols, schemas, configurations, plugins, artifacts, and documentation.

## Version Domains

Atlas expects independent version domains for:

- Ecosystem releases.
- Specifications.
- Rust crates.
- Workspaces.
- Components.
- Services.
- APIs.
- ABIs.
- Protocols.
- Schemas.
- Configuration formats.
- Features and capabilities.
- SDKs.
- Toolchains.
- Build artifacts.
- Documentation.

## Proposed Table of Contents

```text
Chapter 1 Versioning Philosophy
Chapter 2 Version Domains
Chapter 3 Semantic Versioning Extension
Chapter 4 Component Versions
Chapter 5 API Versions
Chapter 6 Protocol Versions
Chapter 7 Schema Versions
Chapter 8 Configuration Versions
Chapter 9 ABI Versions
Chapter 10 Compatibility Rules
Chapter 11 Capability Negotiation
Chapter 12 Deprecation
Chapter 13 Migration
Chapter 14 Release Channels
Chapter 15 Long-Term Support
Chapter 16 Breaking Changes
Chapter 17 Version Validation
Chapter 18 Release Certification
```

## Initial Manifest Sketch

```toml
[ecosystem]
name = "Atlas"
version = "0.1"
workspace = "2026.1"
release = "Draft"

[component]
name = "example-component"
version = "0.1.0"
api = 1
abi = 0
protocol = 0
schema = 1
minimum_ecosystem = "0.1"
minimum_rust = "1.92"
```

