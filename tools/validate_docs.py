#!/usr/bin/env python3
"""Validate cross-cutting invariants across the Atlas Engineering Standards Library.

Checks:
  1. Every ATLAS-<PREFIX>-<NNNN> requirement identifier is unique.
  2. Every requirement identifier's prefix is registered in
     docs/reference/requirement-registry.md (skipped if that file is absent).
  3. Every Markdown file under docs/ (other than templates/ and decisions/,
     which are indexed via their own README rather than listed individually)
     is reachable from docs/SUMMARY.md. README.md and CONTRIBUTING.md are
     deliberately outside the mdBook (see docs/SUMMARY.md) and are excluded
     from this check.
  4. Every relative Markdown link in a tracked .md file resolves to a file
     that exists and, when present, to a rendered Markdown heading anchor.

Exits non-zero (and prints every violation) on any failure.
"""

import re
import sys
from collections import Counter
from html import unescape
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
REQUIREMENT_ID = re.compile(r"ATLAS-([A-Z]+(?:-[A-Z]+)*)-(\d{4})\b")
BACKTICK_TOKEN = re.compile(r"`([A-Z]+(?:-[A-Z]+)*)`")
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
SETEXT_UNDERLINE = re.compile(r"^ {0,3}(?:=+|-+)\s*$")
FENCED_CODE = re.compile(r"^\s*(`{3,}|~{3,})")
HTML_ANCHOR = re.compile(r"<(?:a\s+(?:name|id)|[^>]+\sid)=[\"']([^\"']+)[\"']", re.IGNORECASE)
INLINE_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
HTML_TAG = re.compile(r"<[^>]+>")
MARKDOWN_FORMATTING = re.compile(r"[*_~`]")

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
    summary_path = ROOT / "docs" / "SUMMARY.md"
    if not summary_path.exists():
        return [f"docs/SUMMARY.md not found at {summary_path}"]

    summary_text = summary_path.read_text(encoding="utf-8")
    referenced = set()
    for target in MD_LINK.findall(summary_text):
        target = target.split("#")[0].strip()
        if target:
            referenced.add((summary_path.parent / target).resolve())

    EXCLUDED_FROM_TOC = {"templates", "decisions"}
    must_be_reachable = {
        p for p in files
        if p != summary_path
        and "docs" in p.relative_to(ROOT).parts
        and not EXCLUDED_FROM_TOC & set(p.relative_to(ROOT).parts)
    }

    errors = []
    for path in sorted(must_be_reachable):
        if path.resolve() not in referenced:
            errors.append(f"{path.relative_to(ROOT)} is not linked from SUMMARY.md")
    return errors


def heading_slug(heading: str) -> str:
    """Return the GitHub/mdBook-compatible base anchor for a Markdown heading."""
    text = INLINE_LINK.sub(r"\1", heading)
    text = HTML_TAG.sub("", text)
    text = unescape(MARKDOWN_FORMATTING.sub("", text)).strip().lower()
    slug: list[str] = []
    for character in text:
        if character.isalnum() or character in {"_", "-"}:
            slug.append(character)
        elif character.isspace():
            slug.append("-")
    return "".join(slug)


def headings_and_explicit_anchors(path: Path) -> tuple[list[str], set[str]]:
    """Extract rendered headings and explicit HTML anchors outside fenced code blocks."""
    headings: list[str] = []
    explicit_anchors: set[str] = set()
    previous_line = ""
    fence_character: str | None = None
    fence_length = 0

    for line in path.read_text(encoding="utf-8").splitlines():
        fence = FENCED_CODE.match(line)
        if fence:
            marker = fence.group(1)
            if fence_character is None:
                fence_character = marker[0]
                fence_length = len(marker)
            elif marker[0] == fence_character and len(marker) >= fence_length:
                fence_character = None
                fence_length = 0
            previous_line = ""
            continue

        if fence_character is not None:
            continue

        explicit_anchors.update(HTML_ANCHOR.findall(line))
        atx_heading = MARKDOWN_HEADING.match(line)
        if atx_heading:
            headings.append(atx_heading.group(1))
            previous_line = ""
            continue

        if previous_line and SETEXT_UNDERLINE.match(line):
            headings.append(previous_line.strip())
            previous_line = ""
            continue

        previous_line = line if line.strip() else ""

    return headings, explicit_anchors


def anchors_for(path: Path) -> set[str]:
    """Collect generated heading anchors and explicit HTML anchors from a Markdown file."""
    headings, anchors = headings_and_explicit_anchors(path)
    generated_counts: Counter[str] = Counter()
    used_generated: set[str] = set()
    for heading in headings:
        base = heading_slug(heading)
        anchor = base
        while anchor in used_generated:
            generated_counts[base] += 1
            anchor = f"{base}-{generated_counts[base]}"
        used_generated.add(anchor)
        anchors.add(anchor)
    return anchors


def check_internal_links(files):
    errors = []
    anchor_cache: dict[Path, set[str]] = {}
    for path in files:
        text = path.read_text(encoding="utf-8")
        for target in MD_LINK.findall(text):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", target) or target.startswith("mailto:"):
                continue
            clean_target, separator, raw_fragment = target.partition("#")
            clean_target = clean_target.strip()
            resolved = (path.parent / clean_target).resolve() if clean_target else path.resolve()
            if not resolved.exists():
                errors.append(
                    f"{path.relative_to(ROOT)} links to '{target}', which does not resolve to an existing file"
                )
                continue

            if not separator or not raw_fragment or resolved.suffix.lower() != ".md":
                continue

            fragment = unquote(raw_fragment)
            if resolved not in anchor_cache:
                anchor_cache[resolved] = anchors_for(resolved)
            if fragment not in anchor_cache[resolved]:
                errors.append(
                    f"{path.relative_to(ROOT)} links to '{target}', but heading anchor "
                    f"'#{fragment}' does not exist in {resolved.relative_to(ROOT)}"
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
