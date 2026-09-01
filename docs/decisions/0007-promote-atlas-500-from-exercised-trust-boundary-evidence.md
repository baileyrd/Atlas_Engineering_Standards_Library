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

The Seed trigger therefore no longer asks Atlas to speculate about security. A real architecture now contains identifiable protected assets, untrusted sources, Trust Boundaries, control paths, and exposure decisions that need durable cross-ecosystem rules.

NIST SP 800-207 supplies a mature external definition for the Zero Trust principle relevant to this evidence: trust is not granted implicitly merely because an asset, caller, or resource is inside a network boundary or organizationally owned. That principle maps cleanly onto the exercised architecture because loopback/locality reduces exposure but does not make learner/model/persisted data authoritative, and first-party component ownership does not remove the need for explicit admission and authority boundaries.

## Decision

Promote ATLAS-500 from `Seed` to `Draft 0.1`.

The first draft activates only two security subdomains:

1. `SEC-THREAT` — documented Threat Models, required Threat Model content, and review when the attack surface changes; and
2. `SEC-BOUNDARY` — untrusted-data authority, semantic validation, revalidation of data re-entering authority, trusted control configuration, enforced local-only exposure, secret separation, remote-egress review, and Zero Trust rules prohibiting implicit trust from location or ownership while keeping authority explicit and narrowly scoped.

Atlas adopts Zero Trust at the architectural-principle level consistent with NIST SP 800-207. A caller, component, asset, or data path does not become trusted solely because it is local, loopback-bound, first-party, in an internal network, or in the same Monorepo. Authority is established by the resource-owning policy through an explicit validation, admission, capability, or access decision and is scoped to the resource or operation for which it was established.

This decision does **not** claim that every Atlas system already implements a complete enterprise Zero Trust Architecture. NIST's identity/device authentication and authorization mechanisms become directly applicable when Atlas has real multi-principal, device, credential, or differentiated-access requirements; those mechanisms remain deferred to `SEC-IDENTITY` and `SEC-AUTH` until their own triggers fire.

ATLAS-001 remains authoritative for foundational security review, least privilege, defense in depth, fail-secure behavior, and sensitive observability. ATLAS-500 adds concrete architecture rules that make those tenets actionable at real Trust Boundaries.

The source system's technologies are evidence only. The draft does not standardize HTTP/WebSocket, SQLite, LM Studio, Tauri, Windows, or any other product-specific technology.

The existing reserved `SEC-IDENTITY`, `SEC-AUTH`, `SEC-CRYPTO`, `SEC-KEY`, and `SEC-SUPPLY` domains remain inactive. The first draft does not create account/role policy, choose a cryptographic scheme, define credential rotation, or prescribe supply-chain controls because those decisions have not yet been forced by equivalent supported surfaces.

## Consequences

- ATLAS-500 becomes an active security architecture standard grounded in a concrete attack surface.
- `SEC-THREAT` and `SEC-BOUNDARY` become active shared-family subdomains with permanent requirement IDs.
- Security review can now require explicit Threat Models and Trust Boundary reasoning rather than relying only on high-level tenets.
- Zero Trust becomes a governing Atlas security principle: locality, network position, organizational ownership, first-party status, Monorepo membership, and prior acceptance do not create implicit security authority.
- Untrusted content, model output, deserialized/persisted data, and remote-capable adapters are governed by explicit authority and exposure rules.
- Local-only architecture is treated as an enforceable exposure boundary that reduces attack surface, but not as proof that a caller or payload is trusted.
- Secret separation is standardized without prematurely specifying secret/key lifecycle machinery.
- Later security chapters must still satisfy their own evidence triggers rather than inheriting Draft status from this promotion.

## Alternatives Rejected

- **Keep ATLAS-500 Seed until credentials or cryptographic keys exist.** Rejected because the Seed trigger is disjunctive: handling real untrusted input is already sufficient to create a concrete security attack surface, and Nexa has explicit Trust Boundary decisions that need durable policy now.
- **Draft the full eventual security volume immediately.** Rejected under `ATLAS-GOV-STD-0001` and `ATLAS-PHIL-0102`; current evidence does not justify identity, authentication, cryptography, key lifecycle, or supply-chain requirements.
- **Put all concrete rules into ATLAS-001 Chapter 17.** Rejected because ATLAS-001 intentionally owns foundational tenets. Threat Model structure, Trust Boundary mechanics, and concrete Zero Trust application belong in the dedicated security volume once its trigger fires.
- **Copy Nexa's v1 technologies as security mandates.** Rejected because loopback HTTP/WebSocket, local SQLite, and a specific model adapter demonstrate the security problems but are not the only valid implementations.
- **Treat local or first-party as trusted.** Rejected because Zero Trust explicitly rejects implicit trust based solely on network/location/ownership, and the exercised architecture already demonstrates that local model output and persisted data still require admission or revalidation.
- **Require full enterprise Zero Trust identity infrastructure now.** Rejected because current evidence does not include the multi-principal/device authentication problem that would justify ecosystem-wide identity, credential, or policy-enforcement infrastructure.
- **Treat typed or parsed data as trusted.** Rejected because the exercised architecture explicitly distinguishes structural validity from authority and requires model/persisted content to pass owning admission or revalidation rules.
