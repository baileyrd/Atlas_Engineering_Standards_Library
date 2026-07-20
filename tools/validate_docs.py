#!/usr/bin/env python3
"""Validate cross-cutting invariants across the Atlas Engineering Standards Library.

Checks:
  1. Every ATLAS-<PREFIX>-<NNNN> requirement identifier is unique.
  2. Every requirement identifier's prefix is registered in
     docs/reference/requirement-registry.md (skipped if that file is absent).
  3. Every Markdown file under docs/, plus README.md and CONTRIBUTING.md, is
     reachable from SUMMARY.md.
  4. Every relative Markdown link in a tracked .md file resolves to a file
     that exists.

Exits non-zero (and prints every violation) on any failure.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIREMENT_ID = re.compile(r"ATLAS-([A-Z]+(?:-[A-Z]+)*)-(\d{4})\b")
BACKTICK_TOKEN = re.compile(r"`([A-Z]+(?:-[A-Z]+)*)`")
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

EXCLUDED_DIRS = {".git", ".github", ".claude", ".agents", "book", "node_modules"}


def tracked_markdown_files():
    files = []
    for path in ROOT.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts):
            continue
        files.append(path)
    return sorted(files)


HEADING_LINE = re.compile(r"^#{2,6}\s+ATLAS-")


def check_requirement_ids(files):
    """Only heading lines (## ATLAS-FOO-0001 - Title) count as *definitions*.

    Prose mentions elsewhere (citations, rationale, illustrative examples in
    README.md) are references, not redefinitions, and must not trip this check.
    """
    errors = []
    seen = {}
    for path in files:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not HEADING_LINE.match(line):
                continue
            match = REQUIREMENT_ID.search(line)
            if not match:
                continue
            req_id = match.group(0)
            if req_id in seen and seen[req_id] != path:
                errors.append(
                    f"Duplicate requirement ID {req_id}: defined in "
                    f"{seen[req_id].relative_to(ROOT)} and {path.relative_to(ROOT)}"
                )
            else:
                seen[req_id] = path
    return errors, seen


def check_registered_prefixes(seen):
    registry_path = ROOT / "docs" / "reference" / "requirement-registry.md"
    if not registry_path.exists():
        print("NOTICE: docs/reference/requirement-registry.md not found; skipping prefix-registration check.")
        return []

    registry_text = registry_path.read_text(encoding="utf-8")
    known_prefixes = set(BACKTICK_TOKEN.findall(registry_text))

    errors = []
    for req_id, path in seen.items():
        match = REQUIREMENT_ID.match(req_id)
        prefix = match.group(1)
        if prefix not in known_prefixes:
            errors.append(
                f"{req_id} in {path.relative_to(ROOT)} uses prefix '{prefix}', "
                f"which is not registered in docs/reference/requirement-registry.md"
            )
    return errors


def check_summary_reachability(files):
    summary_path = ROOT / "SUMMARY.md"
    if not summary_path.exists():
        return [f"SUMMARY.md not found at {summary_path}"]

    summary_text = summary_path.read_text(encoding="utf-8")
    referenced = set()
    for target in MD_LINK.findall(summary_text):
        target = target.split("#")[0].strip()
        if target:
            referenced.add((summary_path.parent / target).resolve())

    must_be_reachable = {
        p for p in files
        if p != summary_path
        and p.name not in {"requirement-template.md", "volume-template.md"}
        and "templates" not in p.relative_to(ROOT).parts
    }

    errors = []
    for path in sorted(must_be_reachable):
        if path.resolve() not in referenced:
            errors.append(f"{path.relative_to(ROOT)} is not linked from SUMMARY.md")
    return errors


def check_internal_links(files):
    errors = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for target in MD_LINK.findall(text):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", target) or target.startswith("mailto:"):
                continue
            clean_target = target.split("#")[0].strip()
            if not clean_target:
                continue
            resolved = (path.parent / clean_target).resolve()
            if not resolved.exists():
                errors.append(
                    f"{path.relative_to(ROOT)} links to '{target}', which does not resolve to an existing file"
                )
    return errors


def main():
    files = tracked_markdown_files()

    id_errors, seen = check_requirement_ids(files)
    prefix_errors = check_registered_prefixes(seen)
    reachability_errors = check_summary_reachability(files)
    link_errors = check_internal_links(files)

    all_errors = id_errors + prefix_errors + reachability_errors + link_errors

    if all_errors:
        print(f"validate_docs.py found {len(all_errors)} issue(s):\n")
        for error in all_errors:
            print(f"  - {error}")
        sys.exit(1)

    print(f"validate_docs.py: OK ({len(files)} files, {len(seen)} unique requirement IDs)")


if __name__ == "__main__":
    main()
