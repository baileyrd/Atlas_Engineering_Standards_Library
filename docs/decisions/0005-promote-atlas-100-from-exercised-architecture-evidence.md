# 0005 - Promote ATLAS-100 from Exercised Architecture Evidence

**Status:** Accepted

## Context

ATLAS-100 was intentionally left as a Seed. Its trigger required real components to depend on each other across crate, process, service, or comparable public boundaries strongly enough to force architectural choices beyond the general rules already present in ATLAS-001 Part IV. Drafting runtime, communication, data, or platform architecture before then would have been speculative duplication.

That condition is now satisfied by Nexa, the concrete Rust system that already supplied the program-integrity lessons incorporated into ATLAS-001. The relevant evidence is not a hypothetical architecture narrative:

- the repository contains a multi-crate Rust workspace with real internal composition;
- `apps/nexa-headless` composes domain, knowledge, labs, orchestration, speech, tutor, and runtime crates;
- `nexa-orchestrator-runtime` depends on the orchestrator contract rather than absorbing it;
- the approved v1 architecture selects one logical cross-process business boundary between shared clients and a local Rust runtime;
- the architecture explicitly separates domain policy, orchestration, persistence, model/provider integration, rendering, speech, and platform concerns;
- the approved implementation baseline makes concrete decisions about persistence authority, transaction atomicity, event durability, platform adapters, and when durable asynchronous infrastructure is not justified;
- G1 evidence was executed and accepted for the selected shared-client / cross-process boundary, while the project deliberately did not promote disposable evidence into production maturity.

The trigger therefore no longer asks Atlas to predict how a composed system might behave. A real system has already forced choices about ownership, communication, persistence, and adapter boundaries.

## Decision

Promote ATLAS-100 from `Seed` to `Draft 0.1`.

The initial draft will standardize only architectural rules directly supported by the exercised evidence:

1. domain policy remains owned by domain components rather than being duplicated in presentation, orchestration, persistence, or adapters;
2. orchestration coordinates workflows without absorbing domain reasoning;
3. multiple clients or platform shells exposing the same capability converge on one authoritative logical business interface;
4. a cross-process business interface is an explicit compatibility contract, while its protocol-versioning mechanics remain owned by ATLAS-200;
5. persistence preserves domain identifiers, invariants, ownership, and atomicity rather than redefining them;
6. authoritative domain facts remain distinct from operational telemetry;
7. durable messaging infrastructure is justified by a real durable asynchronous consumer and correctness need;
8. concrete providers, platforms, storage engines, renderers, speech engines, and similar technologies remain behind owned adapter boundaries when the domain depends on the capability rather than the technology.

The source system's technologies are not standardized. React, Tauri, HTTP/WebSocket, SQLite, LM Studio, Sherpa-ONNX, Rive, and other Nexa choices demonstrate the architectural problem and solution shape; they are not Atlas-wide mandates.

The initial draft will continue to defer multi-service deployment topology, service discovery, distributed consistency, broker topology, broad platform-service architecture, multi-region placement, and other unexercised areas until their own evidence fires a trigger.

## Consequences

- ATLAS-100 becomes the first dedicated architecture volume with normative content grounded in an actual multi-component system.
- ATLAS-001 remains the owner of general architecture principles. ATLAS-100 must add concrete composition rules rather than duplicate `LAYER`, `BOUND`, `DEP`, `IFACE`, or `STATE` requirements under new identifiers.
- The `ARCH` prefix moves from the Seed reservation table into the active requirement registry.
- Future architecture requirements need evidence from real systems and should be added to the owning chapter rather than filling a pre-imagined table of contents.
- A real versioned cross-process business boundary now also satisfies ATLAS-200's deferred trigger for protocol versioning. That is a separate follow-up because versioning mechanics belong to ATLAS-200, not this promotion.
- A single system can supply evidence for an architectural rule when multiple real components within that system force the decision; the trigger did not require multiple independent products.

## Alternatives Rejected

- **Keep ATLAS-100 as Seed until another independent product exists.** Rejected because the Seed trigger is about real component interaction, not a product count. Nexa already contains multiple implemented and composed boundaries and has forced architecture decisions that ATLAS-001 alone does not specify concretely.
- **Draft the full eventual architecture volume now.** Rejected under `ATLAS-GOV-STD-0001` and `ATLAS-PHIL-0102`. Evidence exists for runtime ownership, orchestration, communication, persistence, events, and adapters; it does not yet exist for every distributed-systems or platform-services topic.
- **Copy Nexa's v1 architecture as the Atlas standard.** Rejected because Atlas standardizes durable engineering rules, not one product's technology stack. The evidence must be generalized without turning source-specific selections into ecosystem policy.
- **Put the new rules into ATLAS-001 instead.** Rejected because ATLAS-001 already defines the general architecture doctrine. The trigger for ATLAS-100 exists specifically for the concrete runtime/data/communication patterns that emerge once real components compose.
