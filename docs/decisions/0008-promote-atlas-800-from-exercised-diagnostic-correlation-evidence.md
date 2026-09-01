# 0008 - Promote ATLAS-800 from Exercised Diagnostic-Correlation Evidence

**Status:** Accepted

## Context

ATLAS-800 was intentionally left as a Seed until two or more real components needed to agree on a cross-cutting convention to interoperate. General logging, metrics, configuration, error, serialization, testing, accessibility, and similar conventions were therefore deferred rather than copied from common industry practice without an Atlas need.

That trigger is now satisfied narrowly by the approved Nexa v1 architecture. One primary learner interaction crosses multiple independently owned components and boundaries, including the client boundary, local runtime/orchestrator, model adapter, learning/domain components, persistence, and operational evidence path. The architecture requires every primary interaction to be correlated through canonical session, workflow, model, and relevant domain identities and constrains normal diagnostics to content-safe classes such as identifiers, versions, hashes/replay anchors, outcome/error classifications, timings/counts, and lifecycle transitions.

This is a real interoperability requirement between components: evidence from one component is insufficient to diagnose the end-to-end workflow unless participating components preserve compatible correlation semantics.

## Decision

Promote ATLAS-800 from `Seed` to `Draft 0.1`, but activate only one subdomain: `STD-DIAG` for Diagnostic Correlation.

The first chapter standardizes the semantic contract needed across participating components:

- stable correlation context for multi-component workflows;
- use of canonical workflow/domain identities where they already exist;
- propagation of correlation context across participating synchronous, asynchronous, process, and adapter boundaries;
- explicit causal-parent relationships when a new scope is started and that relationship matters;
- separation of Operational Telemetry from authoritative domain facts;
- stable cross-component diagnostic semantic classes without mandating a logging/tracing implementation;
- machine-readable outcome/error classification when cross-component interpretation is required;
- content-safe correlation metadata governed by ATLAS-001 and ATLAS-500; and
- preservation of minimum required evidence when sampling/filtering/retention reduces diagnostic volume.

The source system's technologies are evidence only. This decision does not standardize OpenTelemetry, Rust `tracing`, JSON, any exact field names, log sinks, metrics backends, transport, or storage product.

General logging schemas, metrics conventions, error schemas beyond diagnostic classification, configuration, serialization, networking, documentation, internationalization, accessibility, testing, and naming remain deferred until their own interoperability triggers fire.

## Consequences

- ATLAS-800 becomes an active Draft standard grounded in a concrete multi-component interoperability need.
- `STD-DIAG` becomes an active requirement subdomain with permanent identifiers.
- Participating components can use different diagnostic implementations while preserving a coherent semantic correlation contract.
- Canonical domain/workflow identities become the preferred anchors for diagnosis instead of disconnected diagnostic-only IDs when authoritative identities already exist.
- Operational telemetry remains explicitly non-authoritative; diagnostics cannot become a shadow event store or business truth merely because they carry domain IDs.
- Sensitive content remains excluded from correlation metadata unless independently authorized by the governing security/privacy rules.
- Later ATLAS-800 chapters still require independent trigger evidence.

## Alternatives Rejected

- **Keep ATLAS-800 Seed until a universal log schema is needed.** Rejected because the Seed trigger is already satisfied by the cross-component correlation semantics required for diagnosis; a serialized log schema is a narrower implementation concern whose own trigger has not fired.
- **Standardize OpenTelemetry or one tracing/logging library.** Rejected because the evidence requires shared semantics, not one implementation technology.
- **Create a generic logging chapter containing every common best practice.** Rejected under `ATLAS-GOV-STD-0001`; current evidence only justifies correlation behavior and content-safe diagnostic semantics.
- **Use diagnostic-only correlation IDs everywhere.** Rejected because canonical workflow/domain identities already exist and provide a durable reconciliation path to governed state. Diagnostic-only causal IDs remain permitted when no authoritative identity represents the required scope.
- **Treat logs/traces as durable domain evidence.** Rejected because operational telemetry and authoritative domain facts have different ownership, retention, correctness, replay, and lifecycle semantics.
