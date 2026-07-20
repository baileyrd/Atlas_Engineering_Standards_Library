# ATLAS-400 - Volume V - SDK Architecture

| Field | Value |
|---|---|
| Document ID | ATLAS-400 |
| Title | Volume V - SDK Architecture |
| Short Name | SDK |
| Status | Seed |
| Classification | Normative |
| Scope | Design standards for Atlas-provided SDKs across core, networking, storage, security, terminal, UI, plugin, testing, and documentation domains |
| Parent | ATLAS-001 |

## Purpose

Volume V will define SDK design standards for Atlas — API shape, error handling, configuration — for the specific domains Atlas actually ships an SDK for, not a pre-enumerated list of domains that don't exist yet.

## Trigger

When Atlas ships its first SDK intended for use by code outside the core workspace — a real external consumer, not an internal module. The domain that trigger names (networking, storage, security, or otherwise) determines which chapter gets written first; the others stay unwritten until they have their own trigger.
