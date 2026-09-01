"""Tests for Atlas documentation validation."""

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "validate_docs.py"
SPEC = importlib.util.spec_from_file_location("validate_docs", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load validator from {MODULE_PATH}")
validate_docs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_docs)


class HeadingAnchorTests(unittest.TestCase):
    """Verify heading normalization and duplicate-anchor behavior."""

    def test_normalizes_punctuation_unicode_and_inline_markup(self) -> None:
        self.assertEqual(
            validate_docs.heading_slug("Café & `Rust`: [API](guide.md) — v1.0!"),
            "café--rust-api--v10",
        )

    def test_matches_mdbook_upstream_normalization_examples(self) -> None:
        self.assertEqual(
            validate_docs.heading_slug("Method-call 🐙 expressions 👼"),
            "method-call--expressions-",
        )
        self.assertEqual(validate_docs.heading_slug("中文標題 CJK title"), "中文標題-cjk-title")

    def test_decodes_html_entities_like_rendered_markdown(self) -> None:
        self.assertEqual(validate_docs.heading_slug("Rust &amp; Python"), "rust--python")

    def test_duplicate_headings_receive_numeric_suffixes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "duplicate.md"
            path.write_text("# Repeat\n\n## Repeat\n\n## Repeat\n", encoding="utf-8")

            self.assertEqual(
                validate_docs.anchors_for(path),
                {"repeat", "repeat-1", "repeat-2"},
            )

    def test_cross_base_duplicate_collision_remains_unique(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "collision.md"
            path.write_text("# Repeat\n\n## Repeat\n\n## Repeat-1\n", encoding="utf-8")

            self.assertEqual(
                validate_docs.anchors_for(path),
                {"repeat", "repeat-1", "repeat-1-1"},
            )

    def test_supports_setext_and_ignores_fenced_headings(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "forms.md"
            path.write_text(
                "Setext Title\n============\n\n"
                "```md\n# Not Rendered\n<a id=\"also-not-rendered\"></a>\n```\n",
                encoding="utf-8",
            )

            self.assertEqual(validate_docs.anchors_for(path), {"setext-title"})


class InternalLinkTests(unittest.TestCase):
    """Verify file and fragment validation against temporary Markdown files."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.original_root = validate_docs.ROOT
        validate_docs.ROOT = self.root

    def tearDown(self) -> None:
        validate_docs.ROOT = self.original_root
        self.temp_dir.cleanup()

    def test_accepts_percent_encoded_duplicate_and_file_only_links(self) -> None:
        target = self.root / "target.md"
        source = self.root / "source.md"
        target.write_text("# Café Guide\n\n## Repeat\n\n## Repeat\n", encoding="utf-8")
        source.write_text(
            "[Unicode](target.md#caf%C3%A9-guide)\n"
            "[Duplicate](target.md#repeat-1)\n"
            "[File only](target.md)\n",
            encoding="utf-8",
        )

        self.assertEqual(validate_docs.check_internal_links([source, target]), [])

    def test_rejects_missing_fragment(self) -> None:
        target = self.root / "target.md"
        source = self.root / "source.md"
        target.write_text("# Present\n", encoding="utf-8")
        source.write_text("[Missing](target.md#absent)\n", encoding="utf-8")

        errors = validate_docs.check_internal_links([source, target])

        self.assertEqual(len(errors), 1)
        self.assertIn("heading anchor '#absent' does not exist", errors[0])

    def test_accepts_explicit_html_anchor(self) -> None:
        target = self.root / "target.md"
        source = self.root / "source.md"
        target.write_text('<a id="stable-contract"></a>\n', encoding="utf-8")
        source.write_text("[Explicit](target.md#stable-contract)\n", encoding="utf-8")

        self.assertEqual(validate_docs.check_internal_links([source, target]), [])


if __name__ == "__main__":
    unittest.main()
