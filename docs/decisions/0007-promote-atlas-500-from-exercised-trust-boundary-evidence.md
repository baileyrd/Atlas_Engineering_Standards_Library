# 0007 - Promote ATLAS-500 from Exercised Trust-Boundary Evidence

**Status:** Accepted

## Context

ATLAS-500 was intentionally left as a Seed until an Atlas-aligned component had a real security attack surface. ATLAS-001 already provides foundational security tenets—security review, least privilege, defense in depth, and fail-secure behavior—but deeper security architecture was deferred so Atlas would not invent identity, authentication, cryptography, key management, or supply-chain machinery in the absence of concrete threats.

That condition is now satisfied by Nexa's approved v1 architecture. The system has several explicit trust-boundary decisions that are no longer hypothetical:

- learner input enters an authoritative application/runtime workflow;
- model output is untrusted until explicit admission and quality checks succeed;
- authoritative state is persisted and later re-enters domain authority;
- two clients communicate with one local runtime across a same-machine process boundary;
- model endpoints/process configuration is control-plane state rather than content authority;
- the local model server is loopback-bound by default;
- model, knowledge, and learner content cannot acquire host structural authority;
- secrets are separated from normal domain persistence and diagnostics;
- remote disclosure is not enabled merely because provider-neutral remote contracts exist;
- least-privilege process/filesystem behavior and sensitive diagnostic constraints are explicit architecture requirements.

The Seed trigger therefore no longer asks Atlas to speculate about security. A real architecture now contains identifiable protected assets, untrusted sources, trust boundaries, control paths, and exposure decisions that need durable cross-ecosystem rules.

## Decision

Promote ATLAS-500 from `Seed` to `Draft 0.1`.

The first draft activates only two security subdomains:

1. `SEC-THREAT` — documented threat models, required threat-model content, and review when the attack surface changes; and
2. `SEC-BOUNDARY` — untrusted-data authority, semantic validation, revalidation of data re-entering authority, trusted control configuration, enforced local-only exposure, secret separation, and remote-egress review.

ATLAS-001 remains authoritative for foundational security review, least privilege, defense in depth, fail-secure behavior, and sensitive observability. ATLAS-500 adds concrete architecture rules that make those tenets actionable at real trust boundaries.

The source system's technologies are evidence only. The draft does not standardize HTTP/WebSocket, SQLite, LM Studio, Tauri, Windows, or any other product-specific technology.

The existing reserved `SEC-IDENTITY`, `SEC-AUTH`, `SEC-CRYPTO`, `SEC-KEY`, and `SEC-SUPPLY` domains remain inactive. The first draft does not create account/role policy, choose a cryptographic scheme, define credential rotation, or prescribe supply-chain controls because those decisions have not yet been forced by equivalent supported surfaces.

## Consequences

- ATLAS-500 becomes an active security architecture standard grounded in a concrete attack surface.
- `SEC-THREAT` and `SEC-BOUNDARY` become active shared-family subdomains with permanent requirement IDs.
- Security review can now require explicit threat models and trust-boundary reasoning rather than relying only on high-level tenets.
- Untrusted content, model output, deserialized/persisted data, and remote-capable adapters are governed by explicit authority and exposure rules.
- Local-only architecture is treated as an enforceable security boundary, not descriptive deployment prose.
- Secret separation is standardized without prematurely specifying secret/key lifecycle machinery.
- Later security chapters must still satisfy their own evidence triggers rather than inheriting Draft status from this promotion.

## Alternatives Rejected

- **Keep ATLAS-500 Seed until credentials or cryptographic keys exist.** Rejected because the Seed trigger is disjunctive: handling real untrusted input is already sufficient to create a concrete security attack surface, and Nexa has explicit trust-boundary decisions that need durable policy now.
- **Draft the full eventual security volume immediately.** Rejected under `ATLAS-GOV-STD-0001` and `ATLAS-PHIL-0102`; current evidence does not justify identity, authentication, cryptography, key lifecycle, or supply-chain requirements.
- **Put all concrete rules into ATLAS-001 Chapter 17.** Rejected because ATLAS-001 intentionally owns foundational tenets. Threat-model structure and trust-boundary mechanics belong in the dedicated security volume once its trigger fires.
- **Copy Nexa's v1 technologies as security mandates.** Rejected because loopback HTTP/WebSocket, local SQLite, and a specific model adapter demonstrate the security problems but are not the only valid implementations.
- **Treat typed or parsed data as trusted.** Rejected because the exercised architecture explicitly distinguishes structural validity from authority and requires model/persisted content to pass owning admission or revalidation rules.
