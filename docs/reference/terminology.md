# Terminology

This reference defines initial Atlas terms. Later volumes may extend this glossary within their own domains.

`Architecture`: The structure of a system, including boundaries, responsibilities, dependencies, communication patterns, and evolution constraints.

`Architecture Authority`: The project responsibility accountable for architecture coherence and program integrity, including authority to require a rebaseline or tactical pause. It is a responsibility and decision authority, not a mandatory job title or separate person.

`Architecture Decision Record (ADR)`: A durable record of a significant architectural decision, including the context, the options considered, and the rationale for the choice made.

`Artifact`: A produced output such as a binary, crate, container image, SBOM, document, schema, generated SDK, test report, or release bundle.

`Author Self-Review`: Deliberate review of a change by the same individual who authored it, against its governing requirements and acceptance criteria. It is not independent human review.

`Capability Maturity`: An evidence-backed state describing how far a capability has progressed from concept through architecture, specification, implementation, integration, verification, acceptance, and release readiness. It is distinct from artifact lifecycle, document status, and requirement status.

`Chapter`: A numbered subdivision of a Part within a Volume, typically the unit at which requirements are grouped.

`Compatibility`: The degree to which a consumer can continue to use a provider across changes without modification.

`Component`: A cohesive subsystem with defined ownership, contracts, dependencies, lifecycle, and versioning.

`Contract`: A documented commitment about externally observable behavior.

`Diagnostic Correlation Context`: Operational metadata propagated across participating components so diagnostics from one governed workflow or causal operation can be associated using applicable canonical identities, causal relationships, classifications, versions, or other content-safe references. It is not authoritative domain state.

`Ecosystem`: The complete system of standards, code, tools, processes, artifacts, registries, documentation, and governance.

`First Release Definition`: The finite system or artifact boundary, observable acceptance outcomes, required capability maturity, explicitly deferred scope, and evidence required to decide that a first release is ready.

`Independent Human Review`: Review performed by a person other than the author who is sufficiently independent of the work to provide a separate judgment. It is distinct from author self-review, automated verification, and program-integrity review.

`Lifecycle State`: The current release or support state of a shipped artifact, as defined by ATLAS-001 Chapter 32. It is distinct from capability maturity and from document or requirement status.

`Monorepo`: A single version-control repository used as a deliberate coordination boundary for multiple first-party components, packages, tools, applications, documents, assets, experiments, or other governed areas. Monorepo membership does not by itself imply shared architecture, ownership, versioning, release cadence, deployment, lifecycle, or build/workspace membership.

`Normative`: Binding for official Atlas work.

`Operational Telemetry`: Non-authoritative diagnostic or operational evidence such as logs, traces, metrics, health signals, timings, counts, lifecycle observations, and related metadata. Operational Telemetry may describe domain activity but does not become authoritative domain state unless a governing domain contract explicitly records the fact through its authoritative path.

`Part`: A numbered subdivision of a Volume that groups related Chapters (e.g. "Part II - Philosophy").

`Program Integrity`: The degree to which current specifications, architecture, implementation, deferrals, verification, and roadmap still converge on the project's defined release outcome rather than only remaining locally correct within individual changes.

`Program-Integrity Review`: A deliberate whole-system architecture and convergence review performed independently of the normal implementation/change-review cadence. Independence here is procedural; the review does not require a different person unless another requirement or external obligation requires separation of duties.

`Protocol Compatibility`: The defined relation under which peers using identified Protocol Versions can interact correctly for the applicable request, response, event or stream, and failure semantics.

`Protocol Version`: An explicit identifier for one revision of a cross-process business protocol contract. It is distinct from the version of the transport, framework, executable, package, or library carrying or implementing that protocol unless the governing specification explicitly defines them as one version domain.

`Public Interface`: An interface intended for use outside its defining component, crate, process, service, or administrative boundary.

`Requirement`: A specific statement that constrains or permits behavior.

`RFC (Request for Comments)`: A proposal document used to solicit review and reach consensus on a significant change before it is adopted into a specification.

`Seed`: A volume's status before it has a real, current consumer need. A Seed states purpose and trigger only — no chapters, no requirements — until `ATLAS-GOV-STD-0001`'s trigger condition promotes it to Draft.

`Specification`: A document that defines behavior, structure, interfaces, processes, or governance rules.

`Threat Model`: A documented security analysis of a bounded system or capability that identifies protected assets, Trust Boundaries, untrusted actors or inputs, privileges, assumptions, plausible abuse or failure modes, controls, and residual risks.

`Traceability`: The ability to connect requirements, decisions, implementations, tests, artifacts, and releases.

`Trust Boundary`: A boundary at which the security assumptions, authority, privilege, provenance, or validation requirements applicable to data, callers, components, or resources change. Crossing a Trust Boundary requires the receiving authority to apply the security decision appropriate to the protected resource rather than inheriting trust from the source location.

`Untrusted Data`: Data or content whose provenance, correctness, intent, or authority is insufficient to permit it to directly control privileged, irreversible, or policy-owning behavior without explicit validation or admission by the receiving authority. Untrusted does not necessarily mean malicious.

`Walking Skeleton`: A thin end-to-end implementation path through the release-critical system boundaries, using concrete dependencies where practical, whose purpose is to validate architecture and integration assumptions before substantial horizontal hardening.

`Zero Trust`: A security principle, used by Atlas consistently with NIST SP 800-207, under which trust is not granted implicitly solely because a caller, component, asset, or data path is local, first-party, internally networked, organizationally owned, or previously accepted. Security authority is explicitly evaluated for the protected resource and narrowly scoped to the operation or capability being granted.

`Volume`: A top-level, independently numbered division of the Atlas Engineering Standards Library (e.g. ATLAS-001 Volume I - Foundation), composed of Parts and Chapters.
