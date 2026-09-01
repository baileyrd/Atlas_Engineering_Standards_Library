# 0004 - Program-Integrity Governance Scales by Responsibility, Not Headcount

**Status:** Accepted

## Context

The Nexa tactical-pause assessment exposed a governance gap that ordinary pull-request review does not close. A project can remain locally correct — accepted ADRs, green CI, deterministic tests, disciplined implementation — while the overall program stops converging on a finite release outcome. The follow-up in Issue #20 therefore requires parent-specification maturity gates, capability-maturity reporting, a thin vertical walking skeleton, controlled deferrals, periodic architecture rebaseline, explicit program-integrity authority, and traceability to a first-release definition.

Those controls create a second problem if written carelessly: they can imply an organization with separate architects, implementers, reviewers, release managers, and committees. Atlas must also govern work performed by one developer. Requiring fictional organizational separation would add ceremony without adding assurance, directly conflicting with `ATLAS-PHIL-0102` (Justified Complexity). At the same time, treating a solo developer's self-review as if it were independent peer review would misstate the evidence available.

The design therefore has to preserve two things at once:

- governance responsibilities and deliberate decision gates must remain real even when one person performs all of them; and
- review mechanisms with materially different independence and assurance must not be conflated.

## Decision

Atlas will define governance roles as **responsibilities and decision authorities, not mandatory headcount**. One individual may hold implementation, architecture, project-ownership, and review responsibilities simultaneously unless law, regulation, contract, or a documented risk control requires separation of duties.

Atlas will distinguish four review mechanisms rather than calling all of them "review":

- **Author self-review** — the author deliberately checks the work against governing requirements and acceptance criteria.
- **Automated verification** — tools check mechanically verifiable properties.
- **Program-integrity review** — a deliberate whole-system rebaseline performed independently of the normal implementation/change-review cadence. The independence is procedural and does not by itself require a different person.
- **Independent human review** — a separate person supplies a genuinely independent judgment.

Program-integrity review will be required at defined rebaseline triggers and will produce an explicit `Continue`, `Redirect`, or `Tactical Pause` disposition. Every project will assign an Architecture Authority responsible for program integrity and empowered to require that rebaseline. The same individual may be the implementer on a solo project.

Where independent human review is unavailable and no external or risk-driven separation-of-duties requirement applies, Atlas will require the absence of independent review to be stated rather than disguised. Self-review, automated evidence, and program-integrity review remain required according to their own triggers.

The associated normative requirements are placed in the chapters that already own their subject matter: Chapter 19 for controlled deferrals, Chapter 28 for parent maturity and the walking skeleton, Chapter 32 for capability maturity and release convergence, and Chapter 38 for program-integrity review and role composition. No parallel program-governance hierarchy or new requirement prefix is introduced.

## Consequences

- A one-person Atlas project can comply without inventing committees, duplicate approvals, or fictional peer review.
- A larger organization can separate roles naturally, and can impose stronger separation of duties where risk or external obligations require it.
- Architecture rebaseline remains independent from day-to-day implementation even when performed by the same person, because the required inputs, questions, and disposition are distinct from ordinary change review.
- Status reporting becomes more conservative: contract/conformance completion cannot be reported as runtime integration, system verification, user acceptance, or release readiness without evidence for those later states.
- The Architecture Authority becomes explicitly accountable for system convergence, not only local architecture consistency.
- The standard accepts that a solo project has less independent human assurance than a multi-reviewer project. It records that limitation rather than pretending it does not exist.

## Alternatives Rejected

- **Require a different person for architecture rebaseline.** Rejected because it makes the governance model unusable for legitimate single-developer projects and turns headcount into a prerequisite for engineering discipline.
- **Treat self-review as equivalent to peer review.** Rejected because the mechanisms have different independence and failure modes. Calling them equivalent would corrupt the evidence Atlas is trying to preserve.
- **Make program-integrity review optional for solo projects.** Rejected because the Nexa failure pattern is about perspective and cadence, not team size. A single developer can drift into horizontal depth or specification/implementation mismatch just as a large team can.
- **Create a separate program-governance volume or requirement family.** Rejected because the controls extend existing specification, lifecycle, maintainability, and review responsibilities. A parallel hierarchy would duplicate ownership and violate the library's preference for requirements to live where engineers already look for them.
- **Require independent human review for every substantive change.** Rejected as disproportionate and incompatible with single-maintainer work. Independent review remains desirable or mandatory where risk and external obligations justify it, rather than being universal ceremony.
