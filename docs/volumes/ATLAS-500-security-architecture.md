# ATLAS-500 - Volume VI - Security Architecture

| Field | Value |
|---|---|
| Document ID | ATLAS-500 |
| Title | Volume VI - Security Architecture |
| Short Name | SEC |
| Status | Draft 0.1 |
| Classification | Normative |
| Scope | Evidence-backed threat modeling, zero-trust principles, and trust-boundary security for components handling untrusted data, local process/service exposure, trusted control configuration, secrets, and remote egress. Identity/authentication/authorization, cryptography, key lifecycle, supply-chain security, and broader secure-development-lifecycle policy remain deferred. |
| Parent | ATLAS-001 |

## Purpose

Volume VI defines concrete security architecture once an Atlas-aligned system has a real attack surface. ATLAS-001 Chapter 17 remains the foundational security authority: security-sensitive capabilities receive review, components use least privilege, designs use defense in depth where practical, and failures fail securely. This volume extends those tenets with the threat-model, Zero Trust, and Trust Boundary rules needed by an exercised system that accepts untrusted content and crosses process, persistence, configuration, and possible egress boundaries.

This first draft is intentionally narrow. The Seed trigger has fired for threat modeling and Trust Boundary security, not for every security domain named in the eventual volume scope. Identity, authentication, authorization, cryptography, key/secret lifecycle, supply-chain security, and broader secure-development-lifecycle rules remain unwritten until their own concrete surfaces require decisions.

Atlas adopts Zero Trust at the architectural-principle level consistent with [NIST SP 800-207](https://doi.org/10.6028/NIST.SP.800-207): trust MUST NOT be granted implicitly solely because a caller, component, asset, or data path is local, first-party, inside a repository/network boundary, or previously accepted. Atlas does not claim that every current system implements a complete enterprise Zero Trust Architecture; identity-, device-, and credential-specific enforcement remains governed by later security chapters when those real requirements exist.

## Trigger Evidence

The Seed trigger is satisfied by the exercised Nexa v1 architecture. That system accepts learner input, treats model output as untrusted until admission, persists authoritative local state, communicates across a same-machine process boundary, selects concrete adapter endpoints/processes from configuration, and explicitly requires local-only exposure, trust-boundary revalidation, least privilege, secret separation, and protection of sensitive diagnostics. See [ADR-0007](../decisions/0007-promote-atlas-500-from-exercised-trust-boundary-evidence.md).

The source technologies are evidence, not Atlas mandates. HTTP, WebSocket, SQLite, a particular model provider, desktop shell, or operating system are not required by this volume.

## Relationship to ATLAS-001

This volume assumes and extends the following foundational requirements rather than restating them:

- `ATLAS-SEC-FND-0001` — Security Design Review;
- `ATLAS-SEC-FND-0010` — Least Privilege;
- `ATLAS-SEC-FND-0020` — Defense in Depth;
- `ATLAS-SEC-FND-0030` — Fail Securely;
- `ATLAS-OBS-0020` — Sensitive Data Protection;
- `ATLAS-VAL-0050` through `ATLAS-VAL-0052` — security during design, explicit security documentation, and security controls that do not depend solely on developer discipline.

### Chapter 1 - Threat Modeling

A Threat Model turns a security review from a generic checklist into reasoning about a specific system. It identifies what must be protected, where trust changes, which inputs and actors are not trusted, what authority exists, how an attacker or failure could misuse the system, and which controls reduce that risk.

#### Requirements

##### ATLAS-SEC-THREAT-0001 - Threat Model Required for a Real Attack Surface

A security-sensitive capability that accepts untrusted input, crosses a Trust Boundary, handles credentials or secret material, exposes privileged operations, or protects sensitive data MUST have a documented Threat Model before stable adoption. The model MAY cover a component, workflow, deployment boundary, or bounded capability, but its scope MUST be explicit.

##### ATLAS-SEC-THREAT-0010 - Threat Model Minimum Content

A Threat Model MUST identify, as applicable to its scope: protected assets and data; Trust Boundaries; untrusted actors, sources, and entry points; privileges and control paths; sensitive-data ingress and egress; security-relevant assumptions and external dependencies; plausible abuse, compromise, and failure modes; controls or mitigations; and material residual risks or accepted limitations.

##### ATLAS-SEC-THREAT-0020 - Threat Model Evolves With the Attack Surface

A change that materially alters a Trust Boundary, exposure surface, privilege level, sensitive-data flow, external dependency, control path, or security assumption MUST review the applicable Threat Model and update it when the previous analysis no longer describes the changed system. A Threat Model MUST NOT remain nominally current while the attack surface it describes has materially changed.

### Chapter 2 - Trust Boundaries, Untrusted Data, and Zero Trust

Trust is an architectural property, not a data-format or location property. A value does not become trustworthy merely because it parsed successfully, arrived through a typed interface, originated on loopback, came from a first-party component, was produced by a model, or was previously persisted. Authority must come from an owning policy and an explicit validation, admission, capability, or access decision appropriate to the protected resource.

Zero Trust reinforces that model. Atlas protects resources and authority boundaries rather than assuming that an internal network, local process topology, monorepo, or organizational ownership creates a trusted zone. The mechanism used to establish authority MAY differ by system; where real principal authentication or differentiated authorization becomes necessary, the `SEC-IDENTITY` and `SEC-AUTH` triggers fire rather than being invented here.

#### Requirements

##### ATLAS-SEC-BOUNDARY-0001 - Untrusted Data Does Not Acquire Authority

Untrusted Data MUST NOT directly acquire host, platform, or domain authority merely by being accepted as content. In particular, untrusted input MUST NOT directly select privileged operations, filesystem or process authority, network destinations, authorization outcomes, policy versions, capability grants, tool execution, renderer/host primitives, or equivalent control decisions unless an authority-owning component explicitly validates and admits that use.

##### ATLAS-SEC-BOUNDARY-0010 - Semantic Validation at Trust Boundaries

Data crossing from a less-trusted source into a more-trusted authority boundary MUST be validated before it can influence privileged or irreversible side effects. Validation MUST cover the semantic invariants required by the receiving authority where parse or schema validity alone cannot establish safe meaning.

##### ATLAS-SEC-BOUNDARY-0020 - Revalidate Data Re-entering Authority

Persisted, cached, deserialized, replayed, migrated, or externally modifiable data MUST be revalidated when it re-enters an authority boundary if corruption, stale versions, partial migration, external modification, or changed invariants could make previously accepted data unsafe under the current contract. Prior acceptance MUST NOT be treated as permanent trust when the boundary conditions have changed.

##### ATLAS-SEC-BOUNDARY-0030 - Trusted Control Configuration

Configuration that selects privileged endpoints, processes, executable paths, filesystem locations, providers, authority modes, or equivalent host-control behavior MUST come from a documented trusted control path. Untrusted content or ordinary data-plane input MUST NOT silently become control-plane configuration.

##### ATLAS-SEC-BOUNDARY-0040 - Local-Only Exposure Is Enforced

A component or service whose governing architecture declares same-machine or local-only access MUST enforce that exposure boundary by default through its binding, IPC, or equivalent transport configuration. A wildcard or remotely reachable exposure MUST NOT be treated as equivalent to a local-only boundary. Enabling broader access is a security-significant Trust Boundary change and MUST receive the review required by `ATLAS-SEC-FND-0001` and `ATLAS-SEC-THREAT-0020`.

##### ATLAS-SEC-BOUNDARY-0050 - Secret Material Uses Dedicated Paths

Secret material MUST NOT be stored or propagated through ordinary domain content, normal event payloads, generic non-secret configuration, or routine diagnostics unless the governing component is explicitly a secret-management boundary. A component requiring secrets MUST obtain and retain them through a dedicated mechanism appropriate to its environment, and observability MUST continue to satisfy `ATLAS-OBS-0020`. Creation, rotation, revocation, cryptographic key policy, and secret-store architecture remain deferred to the `SEC-KEY` domain.

##### ATLAS-SEC-BOUNDARY-0060 - Remote Egress Is a Trust-Boundary Change

Protected or sensitive data MUST NOT cross a new remote Trust Boundary merely because a remote-capable adapter, provider contract, or transport is technically available. The governing specification MUST explicitly authorize the egress path, identify the permitted data classes and destination trust assumptions, and define the applicable transport/security policy before the path is treated as supported. Adding remote egress MUST trigger the Threat Model review required by `ATLAS-SEC-THREAT-0020`.

##### ATLAS-SEC-BOUNDARY-0070 - No Implicit Trust From Location or Ownership

A component, caller, asset, request, or data source MUST NOT receive security authority solely because it is on loopback, on the same host, inside an internal network, in the same Monorepo, first-party, or organizationally owned. Locality and ownership MAY reduce exposure or contribute evidence, but they MUST NOT substitute for the validation, admission, capability, or access decision required by the protected resource.

##### ATLAS-SEC-BOUNDARY-0080 - Authority Is Explicit and Narrowly Scoped

A security-relevant authority decision MUST be explicit and scoped to the resource, operation, capability, or workflow for which it was established. Authority established for one interaction or resource MUST NOT silently grant broader or transitive authority to adjacent components, operations, tools, or data. When material security context changes, the applicable authority or admission decision MUST be re-evaluated before additional privileged action proceeds.

## Deferred

Per `ATLAS-GOV-STD-0001`, these topics remain unwritten until their own concrete security surface fires a trigger:

| Topic | Trigger |
|---|---|
| Identity (`SEC-IDENTITY`) | A supported system must distinguish multiple real principals or external identities whose continuity or proof affects security decisions |
| Authentication / authorization (`SEC-AUTH`) | A supported capability requires proof of identity or differentiated access/privilege decisions between real actors or callers |
| Cryptography (`SEC-CRYPTO`) | A concrete confidentiality, integrity, authenticity, or non-repudiation requirement forces a cryptographic design choice rather than incidental hashing or library use |
| Key and secret lifecycle (`SEC-KEY`) | A supported system must provision, store, rotate, revoke, recover, or distribute real credentials or cryptographic keys beyond the separation rule in Chapter 2 |
| Supply-chain security (`SEC-SUPPLY`) | Release or distribution of real artifacts/dependencies requires ecosystem-wide provenance, dependency-integrity, signing, or compromise-response policy |
| Remote transport security | A supported service or provider crosses a host/network Trust Boundary and requires concrete transport authentication, confidentiality, exposure, or ingress policy |
| Sandboxing / untrusted code execution | A supported component executes dynamically supplied code, plugins, scripts, models, or tools whose authority must be contained |
| Broader secure development lifecycle | Repeated security-sensitive implementation and release work across multiple repositories requires a shared security workflow beyond the review/automation rules already in ATLAS-001 and ATLAS-600 |

A plausible future threat is not itself a trigger. Atlas deepens security policy when a real supported attack surface forces an architectural decision that must remain coherent.