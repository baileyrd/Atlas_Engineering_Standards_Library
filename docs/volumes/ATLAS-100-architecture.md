# ATLAS-100 - Volume II - Architecture

| Field | Value |
|---|---|
| Document ID | ATLAS-100 |
| Title | Volume II - Architecture |
| Short Name | ARCH |
| Status | Draft 0.1 |
| Classification | Normative |
| Scope | Runtime, communication, data, and platform architecture for Atlas components and services |
| Parent | ATLAS-001 |

## Purpose

Volume II defines concrete architectural rules that become necessary once real Atlas-aligned components must compose across crate, process, runtime, persistence, and platform boundaries. It extends ATLAS-001 Part IV rather than restating it: ATLAS-001 defines general layering, boundary, dependency, interface, state, and failure principles; this volume defines how those principles apply when a real system has domain components, orchestration, client/runtime communication, persistence, events, and concrete backends.

This first draft is intentionally narrow. Its original Seed trigger has fired through exercised architecture evidence captured in ADR-0005, but only the architectural decisions supported by that evidence are standardized here. Technology selections from the source system are evidence, not Atlas mandates.

## Trigger Evidence

The Seed trigger is satisfied: a real multi-crate Rust system now composes multiple domain and runtime components, exercises crate-to-crate dependencies, and has selected a cross-process business boundary plus explicit orchestration, persistence, event, and adapter ownership. See [ADR-0005](../decisions/0005-promote-atlas-100-from-exercised-architecture-evidence.md) for the evidence and promotion decision.

## Relationship to ATLAS-001

This volume assumes and does not duplicate these foundation requirements:

- `ATLAS-LAYER-0001` and `ATLAS-LAYER-0010` for directional dependency and substitutable layers;
- `ATLAS-BOUND-0001` and `ATLAS-BOUND-0010` for boundary ownership and failure contracts;
- `ATLAS-DEP-0001` and `ATLAS-DEP-0010` for dependency toward stability and the modular-monolith default;
- `ATLAS-IFACE-0001` and `ATLAS-IFACE-0010` for interface compatibility and minimal surface;
- `ATLAS-STATE-0001` for single responsibility for mutable-state consistency;
- `ATLAS-SPEC-0020` and `ATLAS-SPEC-0030` for parent-authority readiness and early vertical integration evidence.

The requirements below are therefore about **architectural ownership and composition**, not generic modularity.

### Chapter 1 - Runtime and Domain Authority

A composed system needs one place where each class of business meaning is authoritative. Presentation shells, adapters, persistence engines, and orchestration code may participate in a workflow without becoming alternate owners of domain semantics.

#### Requirements

##### ATLAS-ARCH-0001 - Domain Policy Ownership

Domain policy MUST remain owned by the component whose contract defines that policy. Presentation, orchestration, persistence, transport, and platform-adapter components MUST NOT reimplement the same policy as a parallel source of truth for convenience.

##### ATLAS-ARCH-0010 - No Parallel Business Authority

A presentation shell, platform shell, adapter, or transport boundary MUST NOT become a second authority for business behavior or mutable domain state already owned by another component. It MAY own lifecycle, presentation, transport, configuration, or platform concerns within its declared boundary.

### Chapter 2 - Orchestration Boundaries

Orchestration exists to coordinate work that crosses component boundaries. It is not a license to absorb the reasoning those components own.

#### Requirements

##### ATLAS-ARCH-0020 - Orchestration Coordinates, Domains Decide

An orchestration component MAY sequence and coordinate work across multiple domain components, but domain decisions MUST be delegated to the component that owns the applicable policy. The orchestrator MUST NOT duplicate that policy internally.

##### ATLAS-ARCH-0030 - Workflow Coordination Ownership

A workflow that crosses multiple component boundaries SHOULD have one declared coordination boundary responsible for the workflow's ordering, completion, cancellation, and recovery semantics. Splitting those responsibilities across unrelated components without an explicit higher-level contract SHOULD be avoided.

### Chapter 3 - Cross-Process Business Interfaces

A process boundary turns an internal call into a compatibility and failure boundary. Multiple clients or platform shells can still share one logical business contract even when their host mechanisms differ.

#### Requirements

##### ATLAS-ARCH-0040 - One Authoritative Logical Business Interface

When multiple clients, shells, or host environments expose the same business capability, they SHOULD converge on one authoritative logical business interface rather than maintain parallel business APIs with independently evolving semantics. Platform-specific IPC or shell commands MUST NOT silently become a second business contract.

##### ATLAS-ARCH-0050 - Cross-Process Interface Is a Compatibility Contract

A business interface that crosses a process boundary MUST define an explicit compatibility contract covering its request, response, event, failure, and lifecycle semantics. The concrete transport MAY vary; transport choice MUST NOT be used as a substitute for compatibility definition. Protocol-versioning mechanics belong to ATLAS-200.

### Chapter 4 - Data Ownership and Persistence

Persistence stores domain state; it does not define domain meaning. The storage implementation must preserve the identifiers, invariants, and atomicity owned by the domain model.

#### Requirements

##### ATLAS-ARCH-0060 - Persistence Preserves Domain Authority

A persistence adapter MUST preserve canonical domain identifiers, invariants, and ownership semantics. Database-generated identifiers, row structure, storage indexes, or vendor-specific types MUST NOT replace domain identity or become public domain contracts unless explicitly adopted by the governing domain specification.

##### ATLAS-ARCH-0070 - Transaction Boundary Follows Domain Atomicity

When one accepted domain operation changes multiple pieces of authoritative state, the persistence architecture MUST provide an atomic commit boundary that prevents observers from seeing a partially accepted operation. The storage technology MAY choose the mechanism, but it MUST preserve the domain operation's defined atomicity.

### Chapter 5 - Events and Durable Asynchrony

Events can represent authoritative facts or merely operational observations. Those roles must not be confused, and durable infrastructure should exist because a real consumer requires it rather than because event-driven architecture is fashionable.

#### Requirements

##### ATLAS-ARCH-0080 - Domain Facts and Telemetry Are Distinct

Operational logs, metrics, traces, and other telemetry MUST NOT silently become authoritative domain state. An event relied upon as a domain fact MUST have declared ownership, semantics, and durability expectations independent of any telemetry representation of that event.

##### ATLAS-ARCH-0090 - Durable Messaging Requires a Durable Need

A durable message broker, outbox, event store, or equivalent asynchronous durability mechanism SHOULD be introduced only when a real durable asynchronous consumer exists and loss of the relevant fact would violate a documented correctness or delivery requirement. Anticipated future consumers alone are not sufficient justification.

### Chapter 6 - Backend and Platform Adapters

Concrete technologies change more often than domain policy. Atlas architecture therefore isolates storage engines, model providers, renderers, speech engines, operating-system facilities, and similar backends behind owned adapter boundaries when the domain depends on the capability rather than the technology.

#### Requirements

##### ATLAS-ARCH-0100 - Concrete Backend Isolation

A concrete backend SHOULD be isolated behind an adapter boundary when callers depend on the capability it provides rather than on that backend's unique semantics. Provider-, platform-, or vendor-specific types and behavior SHOULD NOT leak across the adapter into domain contracts without explicit architectural justification.

##### ATLAS-ARCH-0110 - Adapter Responsibility Boundary

An adapter MAY own transport, endpoint or process configuration, provider-specific request/response mapping, technology-specific capacity behavior, and error normalization required to cross its boundary. It MUST NOT acquire domain policy authority merely because it performs the concrete integration.

## Deferred

Per `ATLAS-GOV-STD-0001`, the following topics remain unwritten until a real current system forces their architectural choices:

| Topic | Trigger |
|---|---|
| Multi-service deployment topology | A release-critical Atlas system requires independently deployed services rather than the modular-monolith default |
| Service discovery and load balancing | Multiple runtime instances must discover and route to each other dynamically |
| Distributed consistency and replication | Authoritative state must span multiple processes or nodes with real consistency tradeoffs |
| Durable event-broker topology | A real durable asynchronous consumer requires broker/outbox architecture beyond the requirement in Chapter 5 |
| Broad platform-service architecture | Multiple real systems require a shared platform service rather than project-local adapters |
| Multi-region / edge placement | Deployment geography becomes a real correctness, latency, or availability constraint |

The existence of a plausible future chapter is not a trigger. These topics remain deferred until evidence requires a decision.
