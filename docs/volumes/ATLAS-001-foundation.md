# ATLAS-001 - Volume I - Foundation

| Field | Value |
|---|---|
| Document ID | ATLAS-001 |
| Title | Volume I - Foundation |
| Short Name | FND |
| Status | Draft 0.1 |
| Classification | Normative |
| Scope | Entire Atlas Ecosystem |
| Parent | ATLAS-000 |

## Purpose

Volume I defines the fundamental engineering philosophy that governs Atlas. It establishes architectural expectations, engineering priorities, design principles, development practices, governance expectations, and quality standards.

Later volumes must remain consistent with Volume I unless a conflict is explicitly resolved by amending Volume I or the Foundation Charter.

## Table of Contents

### Part I - Introduction

```text
Chapter 1 Purpose
Chapter 2 Vision
Chapter 3 Mission
Chapter 4 Scope
Chapter 5 Audience
```

### Part II - Philosophy

```text
Chapter 6 Engineering Philosophy
Chapter 7 Core Values
Chapter 8 Design Goals
Chapter 9 Non-Goals
```

### Part III - Engineering Tenets

```text
Chapter 10 Correctness
Chapter 11 Clarity
Chapter 12 Explicitness
Chapter 13 Modularity
Chapter 14 Composability
Chapter 15 Determinism
Chapter 16 Observability
Chapter 17 Security
Chapter 18 Performance
Chapter 19 Maintainability
Chapter 20 Evolvability
```

### Part IV - Architectural Principles

```text
Chapter 21 Layered Architecture
Chapter 22 Boundary Design
Chapter 23 Dependency Direction
Chapter 24 Interface Design
Chapter 25 State Management
Chapter 26 Failure Handling
Chapter 27 Resource Management
```

### Part V - Ecosystem Principles

```text
Chapter 28 Specification-Driven Development
Chapter 29 Automation
Chapter 30 Validation
Chapter 31 Compatibility
Chapter 32 Lifecycle Management
Chapter 33 Knowledge Preservation
```

### Part VI - Governance

```text
Chapter 34 Standards Process
Chapter 35 RFC Process
Chapter 36 Architecture Decision Records
Chapter 37 Change Management
Chapter 38 Review Process
```

### Part VII - Reference

```text
Chapter 39 Requirement Language
Chapter 40 Terminology
Chapter 41 Document Conventions
Chapter 42 Future Evolution
```

## Part I - Introduction

### Chapter 1 - Purpose

Atlas exists to provide a coherent, principled, and technically rigorous software platform built around Rust. It governs libraries, applications, services, SDKs, protocols, plugins, build systems, documentation, tooling, specifications, release engineering, and governance.

#### Requirements

##### ATLAS-FND-0001 - Specification Authority

All major Atlas behavior MUST be defined by a governing specification before becoming an official ecosystem capability.

##### ATLAS-FND-0002 - Implementation Independence

Specifications MUST define externally observable behavior and MUST NOT require a specific implementation strategy unless explicitly documented.

##### ATLAS-FND-0003 - Traceability

Major architectural decisions MUST be traceable from implementation back to governing specifications, accepted RFCs, or architecture decision records.

##### ATLAS-FND-0004 - Standards Library Scope

The Atlas Engineering Standards Library MUST govern engineering standards for official Atlas specifications, implementations, tools, artifacts, and release processes.

### Chapter 2 - Vision

Atlas seeks to become the reference architecture for building reliable, secure, maintainable Rust software ecosystems.

The vision is not merely a collection of crates. Atlas is a complete ecosystem model: specifications, compatibility rules, build discipline, release governance, SDK design, plugin architecture, operational standards, and long-lived engineering knowledge.

#### Requirements

##### ATLAS-FND-0010 - Reference Architecture

Atlas SHOULD define reusable architectural patterns that can guide multiple implementations.

##### ATLAS-FND-0011 - Rust Alignment

Atlas standards SHOULD align with Rust ecosystem conventions where those conventions support correctness, clarity, safety, and maintainability.

##### ATLAS-FND-0012 - Ecosystem Coherence

Atlas standards MUST consider ecosystem-wide coherence rather than optimizing individual components in isolation.

### Chapter 3 - Mission

The Atlas mission is to make high-quality engineering easier to sustain over long periods of time. Atlas does this by converting judgment into standards, standards into requirements, requirements into verification, and verification into repeatable practice.

#### Requirements

##### ATLAS-FND-0020 - Durable Engineering Knowledge

Important engineering knowledge MUST be preserved in durable, discoverable artifacts.

##### ATLAS-FND-0021 - Automation Readiness

Atlas standards SHOULD be written so that tooling can validate them where practical.

##### ATLAS-FND-0022 - Maintainer Continuity

Atlas designs SHOULD be understandable by maintainers who were not present for the original design.

### Chapter 4 - Scope

Volume I applies to all official Atlas work, including specifications, Rust crates, applications, services, SDKs, plugins, protocols, schemas, build tooling, documentation, release artifacts, and governance processes.

#### In Scope

- Engineering philosophy.
- Architecture principles.
- Normative requirement conventions.
- Governance expectations.
- Compatibility and lifecycle philosophy.
- Documentation and knowledge preservation.

#### Out of Scope

- Detailed cargo rules, defined in ATLAS-300.
- Detailed versioning rules, defined in ATLAS-200.
- Detailed security controls, defined in ATLAS-500.
- Detailed plugin architecture, defined in ATLAS-700.

### Chapter 5 - Audience

This volume is intended for specification authors, architects, maintainers, library authors, application engineers, security reviewers, release engineers, tool authors, SDK authors, and contributors.

## Part II - Philosophy

### Chapter 6 - Engineering Philosophy

Atlas treats software as a long-lived system and a set of contracts. Behavior becomes part of an ecosystem once users, tools, artifacts, or other components begin relying on it. Therefore, behavior must be specified intentionally and must not become stable accidentally.

Atlas favors:

- Correctness before convenience.
- Explicit behavior before inferred behavior.
- Stable contracts before rapid churn.
- Architecture before optimization.
- Automation before manual process.
- Durable records before institutional memory.
- Security and observability as design inputs.

#### Requirements

##### ATLAS-PHIL-0001 - Long-Term Maintenance

Atlas components MUST be designed with consideration for long-term maintenance.

##### ATLAS-PHIL-0002 - Observable Behavior as Contract

All externally observable behavior MUST be treated as a contract.

##### ATLAS-PHIL-0003 - Contract Ownership

Contracts MUST have defined ownership, lifecycle, and compatibility expectations.

##### ATLAS-PHIL-0010 - Specification Before Adoption

New ecosystem capabilities MUST have a documented specification before official adoption.

##### ATLAS-PHIL-0020 - Accidental Behavior

Accidental implementation behavior MUST NOT become a public contract without explicit adoption.

##### ATLAS-PHIL-0030 - Complexity Management

Atlas designs SHOULD minimize accidental and hidden complexity.

##### ATLAS-PHIL-0040 - Long-Term Consequences

Architectural decisions MUST consider long-term consequences in addition to immediate benefits.

##### ATLAS-PHIL-0050 - Rust Strengths

Atlas designs SHOULD leverage Rust strengths without becoming unnecessarily coupled to language-specific limitations.

##### ATLAS-PHIL-0060 - Developer Comprehension

Atlas components SHOULD optimize for developer comprehension as well as runtime behavior.

##### ATLAS-PHIL-0070 - Knowledge Preservation (Retired)

Retired; superseded by `ATLAS-FND-0020`, which states the same requirement. This identifier remains reserved and MUST NOT be reused (`ATLAS-CHARTER-0006`).

##### ATLAS-PHIL-0080 - No-Surprise Interfaces

Public Atlas interfaces SHOULD minimize surprising behavior.

##### ATLAS-PHIL-0090 - Predictable Infrastructure

Infrastructure components SHOULD prioritize reliability and predictability over unnecessary novelty.

#### Unix Design Heritage

Atlas's engineering philosophy is a direct descendant of Unix design philosophy: Doug McIlroy's "do one thing and do it well," composability through narrow interfaces, "silence is golden," and "mechanism, not policy." ATLAS-000 Article III names Composability and Economy as foundational principles for this reason — they are not additions borrowed from elsewhere, they are load-bearing.

The practical consequence: a specification-driven ecosystem can drift toward the opposite of this heritage if left unchecked, accumulating process and ceremony because a "complete" specification seems to call for it rather than because a real need justifies it. This subsection exists to make that failure mode checkable, not just aspirational.

##### ATLAS-PHIL-0100 - Single Responsibility

Components SHOULD have one clearly stated purpose. New capability SHOULD become a new component composed with existing ones rather than accreted onto an existing component's scope.

##### ATLAS-PHIL-0101 - Mechanism Over Policy

Atlas components SHOULD provide capability and leave policy decisions to the caller, per ATLAS-000 Doctrine D11.

##### ATLAS-PHIL-0102 - Justified Complexity

New process, tooling, or abstraction MUST be justified by a demonstrated, current need. Introducing it speculatively, or because a specification's structure implies it should exist, is not sufficient justification.

##### ATLAS-PHIL-0103 - Quiet Success

Components and tools SHOULD produce output only when reporting a requested result or an error. Success that has nothing further to report SHOULD remain silent.

### Chapter 7 - Core Values

This chapter derives its ordering from the co-equal principles in ATLAS-000 Article III — it is the one place that ordering is stated, so later documents cite this chapter rather than inventing their own. Atlas values are ordered: lower values matter, but they must not casually override higher values. Composability and Economy sit above raw Convenience because they are about total, long-term engineering cost; Convenience is short-term implementer ease, which is deliberately the tiebreaker of last resort.

| Rank | Value | Purpose | Where it's covered |
|---|---|---|---|
| 1 | Correctness | Build systems that behave according to specification | Chapter 10; `ATLAS-VAL-0001`-`0003` |
| 2 | Security | Protect users, data, and systems from harm | Chapter 17; `ATLAS-VAL-0050`-`0052` |
| 3 | Clarity | Make behavior, intent, and rationale understandable | Chapter 11; `ATLAS-VAL-0010`-`0022` |
| 4 | Composability | Prefer small, focused parts that combine over monolithic ones | Chapter 14 |
| 5 | Economy | Spend engineering time on demonstrated need, not speculative generality | `ATLAS-VAL-0030`-`0031`, `0070`-`0071` |
| 6 | Stability | Treat public contracts as commitments | Chapter 20; `ATLAS-VAL-0090` |
| 7 | Maintainability | Design for the engineer who maintains this after you | Chapter 19; `ATLAS-VAL-0040`-`0041`, `0060`-`0061` |
| 8 | Performance | Be efficient, but only once correct | Chapter 18; `ATLAS-VAL-0080`-`0081` |
| 9 | Convenience | Short-term ease matters least when it conflicts with the above | — |

#### Requirements

##### ATLAS-VAL-0001 - Specification Correctness

Atlas components MUST implement their documented specifications correctly.

##### ATLAS-VAL-0002 - Undefined Behavior

Undefined behavior MUST NOT be relied upon as part of a supported design.

##### ATLAS-VAL-0003 - Correctness Defects

Correctness failures MUST be treated as priority defects.

##### ATLAS-VAL-0010 - Explainable Decisions

Atlas decisions MUST be explainable through documented reasoning.

##### ATLAS-VAL-0011 - Architectural Shortcuts

Architectural shortcuts MUST be explicitly acknowledged.

##### ATLAS-VAL-0020 - Documented Rationale

Significant design decisions MUST have documented rationale.

##### ATLAS-VAL-0021 - Discoverable Public Documentation

Public interfaces MUST have discoverable documentation.

##### ATLAS-VAL-0022 - Artifact Provenance

Release artifacts MUST provide provenance information.

##### ATLAS-VAL-0030 - Ecosystem Conventions

Atlas components SHOULD follow established ecosystem conventions.

##### ATLAS-VAL-0031 - New Convention Justification

New conventions MUST have documented justification.

##### ATLAS-VAL-0040 - Maintenance Cost

Designs MUST consider long-term maintenance cost.

##### ATLAS-VAL-0041 - Technical Debt

Technical debt MUST be intentionally managed.

##### ATLAS-VAL-0050 - Security During Design

Security considerations MUST be addressed during design.

##### ATLAS-VAL-0051 - Security Documentation

Security-sensitive behavior MUST be explicitly documented.

##### ATLAS-VAL-0052 - Security Automation

Security controls MUST NOT depend solely on developer discipline.

##### ATLAS-VAL-0060 - Downstream Impact

Contributors MUST consider downstream impact.

##### ATLAS-VAL-0061 - Existing Users

Changes affecting public contracts MUST consider existing users.

##### ATLAS-VAL-0070 - Practice Improvement

Atlas SHOULD continuously improve engineering practices.

##### ATLAS-VAL-0071 - Quality Preference

Quality improvements SHOULD be preferred over unnecessary feature growth.

##### ATLAS-VAL-0080 - Total System Cost

Performance decisions MUST consider total system cost.

##### ATLAS-VAL-0081 - Measured Optimization

Optimization SHOULD be guided by measurement.

##### ATLAS-VAL-0090 - Evolution Strategy

All major evolving components MUST define an evolution strategy.

##### ATLAS-VAL-0091 - Migration Paths (Retired)

Retired; superseded by `ATLAS-CHARTER-0007`, which states the same requirement at charter authority. This identifier remains reserved and MUST NOT be reused (`ATLAS-CHARTER-0006`).

### Chapter 8 - Design Goals

Atlas design goals provide evaluation criteria for specifications and implementations.

| Category | Evaluation Question |
|---|---|
| Correctness | Does it behave correctly? |
| Security | Does it reduce risk? |
| Reliability | Does it fail safely? |
| Maintainability | Can future engineers understand it? |
| Performance | Is it efficient based on evidence? |
| Interoperability | Can it evolve with other systems? |
| Scalability | Can it grow? |
| Observability | Can we understand what happened? |
| Automation | Can tools enforce it? |
| Reproducibility | Can we recreate it? |
| Developer Experience | Is it usable and learnable? |
| Longevity | Will it age well? |

#### Requirements

##### ATLAS-GOAL-0001 - Specified Public Behavior

Public behavior MUST be specified before being relied upon.

##### ATLAS-GOAL-0002 - Invalid State Prevention

Invalid states SHOULD be prevented where practical.

##### ATLAS-GOAL-0003 - Diagnostic Errors

Errors SHOULD provide sufficient context for diagnosis.

##### ATLAS-GOAL-0010 - Explicit Authorization

Security-sensitive operations MUST require explicit authorization.

##### ATLAS-GOAL-0011 - Secret Logging

Secrets MUST NOT be exposed through normal logging mechanisms.

##### ATLAS-GOAL-0012 - Security Assumptions

Security assumptions MUST be documented.

##### ATLAS-GOAL-0020 - Failure Behavior

Critical components MUST define failure behavior.

##### ATLAS-GOAL-0021 - Observable Failure Modes

Failure modes SHOULD be observable.

##### ATLAS-GOAL-0030 - Architectural Intent

Complex components MUST document architectural intent.

##### ATLAS-GOAL-0031 - Subsystem Boundaries

Subsystem boundaries SHOULD be clearly defined.

##### ATLAS-GOAL-0040 - Performance Claims

Performance claims MUST be supported by measurement.

##### ATLAS-GOAL-0041 - Correctness Over Performance

Performance improvements MUST NOT compromise correctness.

##### ATLAS-GOAL-0050 - Interoperability Interfaces

Interoperability interfaces MUST be explicitly specified.

##### ATLAS-GOAL-0051 - Protocol Documentation

Protocol behavior MUST NOT depend on undocumented implementation details.

##### ATLAS-GOAL-0060 - Independent Scaling

Architecture SHOULD avoid unnecessary coupling that prevents independent scaling.

##### ATLAS-GOAL-0070 - Operational Diagnostics

Production components SHOULD expose operational diagnostics.

##### ATLAS-GOAL-0071 - Diagnostic Protection

Diagnostics MUST avoid exposing protected information.

##### ATLAS-GOAL-0080 - Repeatable Automation

Repeatable processes SHOULD be automated.

##### ATLAS-GOAL-0081 - Machine-Readable Results

Automation SHOULD produce machine-readable results.

##### ATLAS-GOAL-0090 - Source Provenance

Release artifacts MUST identify their source provenance.

##### ATLAS-GOAL-0091 - Reproducible Builds

Build processes SHOULD produce reproducible outputs.

##### ATLAS-GOAL-0100 - Common Workflows

Common development workflows SHOULD require minimal special knowledge.

##### ATLAS-GOAL-0101 - Actionable Tooling

Tooling SHOULD provide actionable feedback.

##### ATLAS-GOAL-0110 - Future Evolution

Architectural decisions MUST consider future evolution.

##### ATLAS-GOAL-0111 - Temporary Solutions

Temporary solutions SHOULD have explicit expiration criteria.

### Chapter 9 - Non-Goals

Atlas intentionally avoids feature maximization, trend-driven architecture, unlimited compatibility, premature abstraction, implementation-first decisions, performance obsession, unmanaged complexity, fear of evolution, undocumented knowledge, and unnecessary tooling.

#### Requirements

##### ATLAS-NONGOAL-0001 - Feature Cost

Features MUST justify their long-term maintenance cost.

##### ATLAS-NONGOAL-0002 - Popularity

Feature requests SHOULD be evaluated against ecosystem goals rather than popularity alone.

##### ATLAS-NONGOAL-0010 - Technology Adoption

Technology adoption MUST be justified by architectural benefit.

##### ATLAS-NONGOAL-0011 - External Trends

External trends MUST NOT override ecosystem principles.

##### ATLAS-NONGOAL-0020 - Intentional Compatibility

Compatibility commitments MUST be intentional.

##### ATLAS-NONGOAL-0021 - Legacy Compatibility

Legacy compatibility SHOULD require demonstrated value.

##### ATLAS-NONGOAL-0030 - Emergent Abstractions

Abstractions SHOULD emerge from demonstrated patterns.

##### ATLAS-NONGOAL-0031 - Abstraction Cost

Abstractions MUST justify their complexity.

##### ATLAS-NONGOAL-0040 - Ecosystem Impact

Architecture decisions MUST consider ecosystem-wide impact.

##### ATLAS-NONGOAL-0041 - Convenience Limits

Short-term implementation convenience MUST NOT override architectural principles without documented justification.

##### ATLAS-NONGOAL-0050 - Performance Tradeoffs

Performance improvements MUST consider correctness and maintainability.

##### ATLAS-NONGOAL-0060 - Managed Complexity

Complexity SHOULD be managed, isolated, and documented.

##### ATLAS-NONGOAL-0070 - Managed Breaking Changes (Retired)

Retired; superseded by `ATLAS-CHARTER-0007`, which states the same requirement at charter authority. This identifier remains reserved and MUST NOT be reused (`ATLAS-CHARTER-0006`).

##### ATLAS-NONGOAL-0071 - Breaking Change Migration (Retired)

Retired; superseded by `ATLAS-CHARTER-0007`, which states the same requirement at charter authority. This identifier remains reserved and MUST NOT be reused (`ATLAS-CHARTER-0006`).

##### ATLAS-NONGOAL-0080 - Durable Knowledge (Retired)

Retired; superseded by `ATLAS-FND-0020`, which states the same requirement. This identifier remains reserved and MUST NOT be reused (`ATLAS-CHARTER-0006`).

##### ATLAS-NONGOAL-0090 - Purposeful Tooling

Tools SHOULD exist to solve recurring ecosystem problems.

## Part III - Engineering Tenets

### Chapter 10 - Correctness

Correctness is the property that a system produces behavior consistent with its defined specification under all supported conditions. Correctness applies from individual functions through modules, libraries, services, protocols, and the ecosystem.

#### Correctness Dimensions

- Functional correctness.
- Behavioral correctness.
- Data correctness.
- Temporal correctness.
- Security correctness.
- Compatibility correctness.

#### Correctness Hierarchy

```text
Specification Correctness
Architectural Correctness
Implementation Correctness
Operational Correctness
```

#### Rust Design Example

Less preferred:

```rust
struct User {
    authenticated: bool,
    token: Option<String>,
}
```

Preferred:

```rust
struct AuthenticatedUser {
    identity: IdentityToken,
}
```

The preferred design makes invalid states harder to represent. Atlas Rust code should use the type system to encode important invariants where doing so improves clarity and correctness.

#### Requirements

##### ATLAS-CORR-0001 - Invalid State Prevention

Designs SHOULD prevent invalid states through architecture and type systems where practical.

##### ATLAS-CORR-0010 - External Input Validation

External input MUST be validated before entering trusted system boundaries.

##### ATLAS-CORR-0020 - Explicit Failures

Failures MUST be represented explicitly.

##### ATLAS-CORR-0030 - Documented Invariants

Critical invariants MUST be documented.

##### ATLAS-CORR-0031 - Invariant Preservation

Implementations MUST NOT violate defined invariants.

##### ATLAS-CORR-0040 - Rust Type System

Atlas Rust implementations SHOULD use the type system to enforce correctness where practical.

##### ATLAS-CORR-0050 - Automated Validation

Critical behavior MUST have automated validation.

##### ATLAS-CORR-0060 - Formal Methods

Systems with high correctness requirements SHOULD consider formal verification techniques.

##### ATLAS-CORR-0070 - Complexity Risk

Designs SHOULD minimize unnecessary complexity that increases correctness risk.

### Chapter 11 - Clarity

Clarity is the property that a design can be understood by its intended maintainers, users, reviewers, and operators. A clear system communicates intent through structure, naming, documentation, contracts, and diagnostics.

#### Requirements

##### ATLAS-CLAR-0001 - Intentional Naming

Public names SHOULD communicate domain meaning rather than implementation trivia.

##### ATLAS-CLAR-0002 - Discoverable Intent

Important design intent MUST be discoverable from specifications, code, or architecture records.

##### ATLAS-CLAR-0010 - Ambiguity Reduction

Specifications MUST resolve behavior that would otherwise be ambiguous to implementers or consumers.

##### ATLAS-CLAR-0020 - Local Reasoning

Components SHOULD be designed so that common behavior can be understood without inspecting unrelated subsystems.

### Chapter 12 - Explicitness

Explicitness reduces hidden coupling and unexpected behavior. Atlas prefers visible configuration, declared dependencies, documented capabilities, and stable contracts.

#### Requirements

##### ATLAS-EXPL-0001 - Explicit Configuration

Configuration that affects externally observable behavior MUST be documented.

##### ATLAS-EXPL-0010 - Declared Dependencies

Components MUST declare their required dependencies and compatibility expectations.

##### ATLAS-EXPL-0020 - Capability Declaration

Optional capabilities SHOULD be declared in machine-readable metadata where practical.

##### ATLAS-EXPL-0030 - Hidden Global State

Designs SHOULD avoid hidden global state that changes behavior across unrelated components.

### Chapter 13 - Modularity

Modularity is the practice of dividing a system into cohesive parts with explicit boundaries. Modules exist to protect reasoning, ownership, testing, replacement, and evolution.

#### Requirements

##### ATLAS-MOD-0001 - Cohesive Components

Components SHOULD group responsibilities that change together.

##### ATLAS-MOD-0010 - Explicit Boundaries

Component boundaries MUST be documented when the component is public, shared, or safety-critical.

##### ATLAS-MOD-0020 - Boundary Leakage

Components SHOULD NOT expose internal implementation details as public contracts.

### Chapter 14 - Composability

Composability allows independently useful parts to work together through stable, simple, and well-documented contracts.

#### Requirements

##### ATLAS-COMP-0001 - Stable Composition Contracts

Composition points MUST define their accepted inputs, outputs, failure modes, and lifecycle expectations.

##### ATLAS-COMP-0010 - Narrow Interfaces

Interfaces SHOULD expose the minimum surface necessary for intended composition.

##### ATLAS-COMP-0020 - Feature Interaction

Specifications SHOULD document meaningful interactions between optional features.

### Chapter 15 - Determinism

Determinism supports reproducibility, testing, debugging, and trust. Atlas systems should make nondeterminism explicit and controlled.

#### Requirements

##### ATLAS-DET-0001 - Reproducible Behavior

Given identical supported inputs, configuration, and environment, Atlas systems SHOULD produce identical outputs where practical.

##### ATLAS-DET-0010 - Explicit Nondeterminism

Sources of nondeterminism SHOULD be explicit and documented.

##### ATLAS-DET-0020 - Deterministic Tests

Automated tests MUST NOT depend on uncontrolled nondeterminism.

### Chapter 16 - Observability

Observability is required for diagnosis, operations, security review, and long-term support.

#### Requirements

##### ATLAS-OBS-0001 - Operational Visibility

Production components SHOULD expose logs, metrics, traces, health signals, or equivalent diagnostics appropriate to their role.

##### ATLAS-OBS-0010 - Structured Diagnostics

Diagnostics SHOULD be structured where practical.

##### ATLAS-OBS-0020 - Sensitive Data Protection

Observability mechanisms MUST protect secrets and sensitive data.

##### ATLAS-OBS-0030 - Correlation

Distributed or multi-component workflows SHOULD support correlation across component boundaries.

### Chapter 17 - Security

Security is a foundational engineering concern. Atlas treats security properties as explicit architecture and specification work.

#### Requirements

##### ATLAS-SEC-FND-0001 - Security Design Review

Security-sensitive capabilities MUST receive security review before stable adoption.

##### ATLAS-SEC-FND-0010 - Least Privilege

Components SHOULD operate with the least privilege required for their responsibilities.

##### ATLAS-SEC-FND-0020 - Defense in Depth

Security-sensitive designs SHOULD use layered controls where practical.

##### ATLAS-SEC-FND-0030 - Fail Securely

Security-sensitive failures MUST fail securely unless a documented exception is approved.

### Chapter 18 - Performance

Performance matters, but it is not a license to discard correctness, security, clarity, or maintainability.

#### Requirements

##### ATLAS-PERF-0001 - Measurement

Performance claims MUST be supported by measurement.

##### ATLAS-PERF-0010 - Tradeoff Documentation

Performance-driven tradeoffs that affect public behavior, safety, or maintainability MUST be documented.

##### ATLAS-PERF-0020 - Efficient Defaults

Atlas components SHOULD provide efficient defaults appropriate to their domain.

### Chapter 19 - Maintainability

Maintainability is the ability to understand, repair, evolve, test, and operate a system over time.

#### Requirements

##### ATLAS-MAINT-0001 - Future Maintainer Principle

Designs MUST consider engineers who will maintain the system after the original authors are gone.

##### ATLAS-MAINT-0010 - Change Locality

Components SHOULD be designed so common changes remain localized.

##### ATLAS-MAINT-0020 - Technical Debt Records

Known significant technical debt SHOULD be recorded with ownership and remediation expectations.

### Chapter 20 - Evolvability

Evolvability is the ability to change without fragmentation. Atlas evolves through compatibility rules, lifecycle states, deprecation policy, migration paths, and versioned contracts.

#### Requirements

##### ATLAS-EVOL-0001 - Evolution Strategy (Retired)

Retired; superseded by `ATLAS-VAL-0090`, which states the same requirement. This identifier remains reserved and MUST NOT be reused (`ATLAS-CHARTER-0006`).

##### ATLAS-EVOL-0010 - Deprecation Path

Deprecated capabilities SHOULD include replacement guidance.

##### ATLAS-EVOL-0020 - Migration Support (Retired)

Retired; superseded by `ATLAS-CHARTER-0007`, which states the same requirement at charter authority and controlling strength (`MUST` vs. this requirement's weaker `SHOULD`). This identifier remains reserved and MUST NOT be reused (`ATLAS-CHARTER-0006`).

## Part IV - Architectural Principles

Part III states properties every Atlas design should have (correctness, clarity, modularity, and so on). Part IV is narrower: it states how Atlas systems are structured to get those properties. Where a requirement here would just restate a Part III tenet under a new prefix, it doesn't exist — this part cross-references Part III instead of duplicating it.

### Chapter 21 - Layered Architecture

Atlas systems SHOULD be organized into layers with directional dependency: domain logic depends on ports (interfaces), adapters implement ports, and platform-specific backends implement adapters where a platform distinction exists. Nothing above a layer depends on that layer's implementation detail — only on what it declares.

This is not aspirational; it already exists in practice. A `platform` crate can define traits (the port) while `platform-linux`/`platform-windows`/`platform-mock` implement them (the adapters) — everything above depends on the trait alone, never on a specific backend.

#### Requirements

##### ATLAS-LAYER-0001 - Directional Dependency

Higher architectural layers MUST depend on lower layers only through the lower layer's declared interface, never through its implementation detail.

##### ATLAS-LAYER-0010 - Layer Substitutability

A layer's implementation SHOULD be substitutable without changes to the layers that depend on it, provided the interface contract is preserved.

### Chapter 22 - Boundary Design

A boundary is where trusted, internally-consistent state meets something Atlas doesn't control: external input, another process, another crate's public surface, the filesystem, the network. `ATLAS-CORR-0010` already requires validating input at a boundary; this chapter's concern is different — who owns a boundary, and what it must declare, not the act of validating.

#### Requirements

##### ATLAS-BOUND-0001 - Boundary Ownership

Every trust boundary MUST have exactly one component responsible for translating across it. Responsibility MUST NOT be split silently across multiple components.

##### ATLAS-BOUND-0010 - Boundary Failure Contract

A boundary's failure behavior — what happens when translation across it fails — MUST be part of its declared interface, not left to caller inference.

### Chapter 23 - Dependency Direction

Atlas defaults to a modular monolith with clear internal module boundaries. Extracting a separate service or process requires a concrete forcing function — independent scaling, a team or language boundary, or hard fault isolation — not speculative future need; the distributed-systems tax is not paid without one.

#### Requirements

##### ATLAS-DEP-0001 - Dependency Toward Stability

Components SHOULD depend on more stable abstractions (ports, traits) rather than on more volatile concrete implementations.

##### ATLAS-DEP-0010 - Modular Monolith Default

Atlas SHOULD default to a modular monolith with narrow, explicit module boundaries. Extracting a separate service MUST be justified by a concrete forcing function (independent scaling, a team or language boundary, or hard fault isolation), not speculative future need.

### Chapter 24 - Interface Design

A public trait is consumed on two sides: callers and implementers. A change that is additive for callers can still be breaking for implementers — a trait gaining a required method compiles for every existing caller but breaks every existing implementation that doesn't yet have that method. Interface design in Atlas MUST account for both sides, not just the caller's.

#### Requirements

##### ATLAS-IFACE-0001 - Two-Sided Trait Contracts

A public trait's compatibility MUST be evaluated from both the caller's and the implementer's perspective before being classified as additive or breaking.

##### ATLAS-IFACE-0010 - Minimal Surface

Public interfaces SHOULD expose the minimum set of methods and types necessary for their stated purpose.

### Chapter 25 - State Management

#### Requirements

##### ATLAS-STATE-0001 - Single Ownership

Mutable state SHOULD have exactly one component responsible for its consistency at any time. Introducing shared mutable state MUST include an explicit synchronization strategy.

##### ATLAS-STATE-0010 - Immutability Default

Atlas designs SHOULD default to immutable data and explicit, narrow mutation points rather than broadly mutable shared state.

### Chapter 26 - Failure Handling

`ATLAS-CORR-0020` requires that failures be represented explicitly; this chapter states the Rust-specific mechanism for doing so.

#### Requirements

##### ATLAS-FAIL-0001 - Result Over Panic

Atlas Rust library code MUST return `Result` for recoverable failure rather than panicking. `unwrap()`/`expect()` MUST NOT appear outside tests and throwaway prototypes.

##### ATLAS-FAIL-0010 - Error Context

Errors MUST be propagated with enough context to diagnose the failure. An error MUST NOT be silently swallowed or flattened to an opaque type that discards its cause.

### Chapter 27 - Resource Management

#### Requirements

##### ATLAS-RES-0001 - RAII Ownership

External resources (file descriptors, sockets, handles, processes) MUST be owned by a type whose destructor releases them. Manual, non-RAII cleanup MUST NOT be the primary release mechanism.

##### ATLAS-RES-0010 - Ownership Transfer Explicitness

Where a resource's ownership can transfer between components, the transfer point and the post-transfer responsibility MUST be explicit in the interface, not inferred from convention.

## Part V - Ecosystem Principles

### Chapter 28 - Specification-Driven Development

`ATLAS-FND-0001` requires a governing specification to exist before a capability becomes official. This chapter states what that specification must actually contain, and what happens when it and the implementation disagree.

#### Requirements

##### ATLAS-SPEC-0001 - Specification Minimum Content

A governing specification MUST state the capability's externally observable behavior, error conditions, and compatibility expectations. A placeholder document is not a specification for the purposes of `ATLAS-FND-0001`.

##### ATLAS-SPEC-0010 - Specification Authority Over Implementation

Where a specification and its implementation disagree, the specification is authoritative until formally amended. The implementation MUST be corrected, not the specification silently reinterpreted to match it.

### Chapter 29 - Automation

#### Requirements

##### ATLAS-AUTO-0001 - Minimum Structural Enforcement

A published Atlas document set MUST have at least one automated check enforcing its own structural rules (identifier uniqueness, internal link validity, and similar), per ATLAS-000 Doctrine D5, rather than relying on review alone.

##### ATLAS-AUTO-0010 - Automation Proportionality

Automation SHOULD be added once a rule has demonstrably needed repeated manual checking, not speculatively before it has been checked by hand even once, per `ATLAS-PHIL-0102`.

### Chapter 30 - Validation

#### Requirements

##### ATLAS-VERIFY-0001 - Verification Method Stated

A normative requirement SHOULD state how its satisfaction can be verified. "Trust" is not a verification method.

##### ATLAS-VERIFY-0010 - Verification Method Taxonomy

Atlas recognizes four verification methods, in increasing order of assurance and cost: automated check, test, review, and formal proof. A requirement SHOULD use the cheapest method sufficient for its risk.

### Chapter 31 - Compatibility

#### Requirements

##### ATLAS-COMPAT-0001 - Compatibility Surface Classification

A component MUST classify each of its public surfaces (API, ABI, protocol, schema, configuration) independently. A change compatible on one surface MAY be breaking on another.

##### ATLAS-COMPAT-0010 - Two-Sided Compatibility

Compatibility classification MUST consider every consumer role a surface has, per `ATLAS-IFACE-0001`, not only the most common one.

### Chapter 32 - Lifecycle Management

Atlas has three independent lifecycle vocabularies, deliberately not conflated: a governing *document's* `Status` field (see `docs/templates/volume-template.md`), an individual *requirement's* `Status` field (see `docs/templates/requirement-template.md`), and — defined here — a shipped *artifact's* lifecycle state. A crate can be `Released` while the specification governing it is still `Draft`; the two track different things.

```text
Planning
Development
Preview
Released
Maintained
Security Fixes
Deprecated
Retired
Archived
```

#### Requirements

##### ATLAS-LIFE-0001 - Lifecycle State Declaration

A released Atlas artifact (crate, service, protocol, schema) MUST declare its current lifecycle state from the set: Planning, Development, Preview, Released, Maintained, Security Fixes, Deprecated, Retired, Archived.

##### ATLAS-LIFE-0010 - Lifecycle Distinctness

An artifact's lifecycle state, its governing document's `Status`, and any individual requirement's `Status` are independent and MUST NOT be conflated.

### Chapter 33 - Knowledge Preservation

`ATLAS-FND-0020` requires important knowledge to be preserved in durable artifacts. This chapter states the two concrete forms that takes.

#### Requirements

##### ATLAS-KNOW-0001 - Decision Records

Significant, non-obvious engineering decisions MUST be recorded as an Architecture Decision Record per Chapter 36, not left to commit messages or memory.

##### ATLAS-KNOW-0010 - Learning Notes

Debugging discoveries and hard-won operational lessons SHOULD be recorded as short, numbered, standalone notes discoverable independently of the code that prompted them, not buried in a pull request description.

## Part VI - Governance

Chapters 34 through 38 are reserved for detailed expansion. They will define the standards process, RFC process, architecture decision records, change management, and review process.

## Part VII - Reference

Chapters 39 through 42 are reserved for detailed expansion. They will define requirement language, terminology, document conventions, and future evolution.

