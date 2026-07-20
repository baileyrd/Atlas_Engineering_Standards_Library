# ATLAS-700 - Volume VIII - Plugin and Extension Architecture

| Field | Value |
|---|---|
| Document ID | ATLAS-700 |
| Title | Volume VIII - Plugin and Extension Architecture |
| Short Name | PLUG |
| Status | Seed |
| Classification | Normative |
| Scope | Plugin lifecycle, discovery, loading, communication, ABI, sandboxing, permissions, and marketplace architecture |
| Parent | ATLAS-001 |

## Purpose

Volume VIII will define the Atlas extension model — plugin lifecycle, ABI, sandboxing, permissions — once a real plugin exists to design the model around, rather than guessing at an ABI no consumer has tested yet.

## Trigger

When Atlas has a first real plugin or extension point that a component outside the core workspace needs to load dynamically. Plugin ABI design decided speculatively, before any real dynamic-loading case exists, is exactly the kind of unjustified complexity `ATLAS-PHIL-0102` exists to prevent — it would need to be redesigned anyway once a real case arrived.
