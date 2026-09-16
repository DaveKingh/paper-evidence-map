"""Regression tests for the dependency-free repository validator."""

from __future__ import annotations

import copy
import importlib.util
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "paper_evidence_map_validate", REPOSITORY_ROOT / "scripts" / "validate.py"
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover - import bootstrap guard
    raise RuntimeError("could not load scripts/validate.py")
validate = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validate
SPEC.loader.exec_module(validate)

BUILD_SPEC = importlib.util.spec_from_file_location(
    "paper_evidence_map_pdf_builder", REPOSITORY_ROOT / "scripts" / "build_fixture_pdf.py"
)
if BUILD_SPEC is None or BUILD_SPEC.loader is None:  # pragma: no cover
    raise RuntimeError("could not load scripts/build_fixture_pdf.py")
sys.modules["validate"] = validate
pdf_builder = importlib.util.module_from_spec(BUILD_SPEC)
sys.modules[BUILD_SPEC.name] = pdf_builder
BUILD_SPEC.loader.exec_module(pdf_builder)


class RepositoryChecksTest(unittest.TestCase):
    def test_repository_integrity(self) -> None:
        self.assertEqual(validate.repository_errors(REPOSITORY_ROOT), [])

    def test_v02_prompt_behavior_contract_is_bilingual(self) -> None:
        """Protect v0.2 capabilities, not one legacy sentence spelling."""
        self.assertEqual(validate.check_prompt_contract(REPOSITORY_ROOT), [])
        for relative_path in (
            "prompts/en/project-instructions.md",
            "prompts/en/project-instructions-compact.md",
            "prompts/zh-CN/project-instructions.md",
            "prompts/zh-CN/project-instructions-compact.md",
        ):
            with self.subTest(path=relative_path):
                text = (REPOSITORY_ROOT / relative_path).read_text(encoding="utf-8")
                for marker in ("Scan", "Triage", "Targeted", "Deep", "Audit", "Candidate Gap", "Candidate Idea"):
                    self.assertIn(marker, text)

    def test_prompt_contract_accepts_reworded_current_chat_rule(self) -> None:
        """Regression: semantic-equivalent v0.2 wording must not fail CI."""
        original = validate._PROMPT_CONTRACT_GROUPS["prompts/en/project-instructions.md"]
        self.assertIn(("current chat", "current-chat"), original)
        self.assertNotIn(("Current-chat attachment precedence",), original)

    def test_prompt_contract_protects_open_request_triage_and_config_binding(self) -> None:
        """Regression: vague requests stay Triage and cross-table values stay config-bound."""
        for relative_path in (
            "prompts/en/project-instructions.md",
            "prompts/en/project-instructions-compact.md",
        ):
            groups = validate._PROMPT_CONTRACT_GROUPS[relative_path]
            self.assertIn(("take a look", "help me read this", "what do you think of this paper"), groups)
            self.assertIn(("not directly comparable",), groups)

        for relative_path in (
            "prompts/zh-CN/project-instructions.md",
            "prompts/zh-CN/project-instructions-compact.md",
        ):
            groups = validate._PROMPT_CONTRACT_GROUPS[relative_path]
            self.assertIn(("看一下", "帮我读读", "这篇怎么样"), groups)
            self.assertIn(("不可直接比较",), groups)

    def test_prompt_contract_accepts_reworded_chinese_stop_rule(self) -> None:
        """Regression: equivalent Chinese STOP wording must not fail CI."""
        alternatives = validate._PROMPT_CONTRACT_GROUPS[
            "prompts/zh-CN/project-instructions-compact.md"
        ][-1]
        self.assertIn("当前目标满足就停止", alternatives)

    def test_markdown_image_and_html_image_are_checked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "![missing](assets/nope.svg)\n<img src=\"assets/also-nope.png\">\n",
                encoding="utf-8",
            )
            errors = validate.check_markdown_links(root)
            self.assertEqual(sum("broken local link" in item for item in errors), 2)

    def test_links_in_code_blocks_are_not_treated_as_repository_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "```markdown\n[illustrative](not-a-real-file.md)\n```\n",
                encoding="utf-8",
            )
            self.assertEqual(validate.check_markdown_links(root), [])

    def test_pdf_fixture_has_basic_integrity(self) -> None:
        self.assertEqual(validate.check_pdf_fixture(REPOSITORY_ROOT), [])

    def test_pdf_builder_is_deterministic_and_extractable(self) -> None:
        source = (REPOSITORY_ROOT / "examples" / "synthetic" / "paper.md").read_bytes()
        first = pdf_builder.make_pdf(source)
        second = pdf_builder.make_pdf(source)
        self.assertEqual(first, second)
        self.assertEqual(len(re.findall(rb"/Type\s*/Page\b", first)), 2)
        extracted = validate.extract_pdf_text_basic(first)
        self.assertIn("TinyRank: Compact Document Classification", extracted)
        self.assertIn("without C", extracted)


class StructuralScoringTest(unittest.TestCase):
    def test_reference_output_passes(self) -> None:
        report = validate.score_response(
            REPOSITORY_ROOT / "examples" / "synthetic" / "expected-output.md"
        )
        self.assertGreaterEqual(report.score, 90)

    def test_input_paper_does_not_masquerade_as_response(self) -> None:
        report = validate.score_response(REPOSITORY_ROOT / "examples" / "synthetic" / "paper.md")
        self.assertLess(report.score, 75)

    def test_keyword_stuffing_does_not_pass(self) -> None:
        text = """# Reading coverage
Inspected; missing/inaccessible; not specified in the paper.
## Research question
## Method map
## Innovation
## Experiment map
## Claim-evidence
## Consistency
## Unknown risk register
[Paper fact] [Author interpretation] [Analyst judgment] [Unknown]
Section 1; Section 2; Table 1; Table 2.
""" + ("filler words without an evidence matrix " * 30)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stuffed.md"
            path.write_text(text, encoding="utf-8")
            self.assertLess(validate.score_response(path).score, 75)

    def test_strongbase_is_not_a_support_label(self) -> None:
        rows = [["C1", "StrongBase result", "Section 1"]]
        support_values = {"strong", "moderate", "weak", "cannot judge"}
        valid_rows = sum(any(cell.casefold() in support_values for cell in row) for row in rows)
        self.assertEqual(valid_rows, 0)


class SyntheticAssertionsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.reference_text = (
            REPOSITORY_ROOT / "examples" / "synthetic" / "expected-output.md"
        ).read_text(encoding="utf-8")

    def test_reference_output_hits_fixture_contract(self) -> None:
        report = validate.check_synthetic_fixture(self.reference_text)
        self.assertTrue(report.passed, report)
        self.assertGreaterEqual(len(report.hits), 7)

    def test_fabricated_locator_fails_fixture(self) -> None:
        report = validate.check_synthetic_fixture(self.reference_text + "\nFigure 9 proves the claim.\n")
        self.assertFalse(report.passed)
        self.assertIn("Figure 9", report.fabricated_locators)

    def test_invented_detail_fails_fixture(self) -> None:
        report = validate.check_synthetic_fixture(self.reference_text + "\nRandom seed = 42.\n")
        self.assertFalse(report.passed)
        self.assertIn("invented numeric seed", report.fabricated_details)

    def test_missing_critical_numeric_correction_fails(self) -> None:
        stripped = re.sub(r"\+?0\.04|\+4 points|only 4 points", "unclear", self.reference_text)
        report = validate.check_synthetic_fixture(stripped)
        self.assertFalse(report.passed)
        self.assertTrue(any(item.startswith("F1 ") for item in report.misses))


class JsonExportTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.path = REPOSITORY_ROOT / "examples" / "synthetic" / "expected-output.json"
        cls.instance = json.loads(cls.path.read_text(encoding="utf-8"))
        cls.schema = json.loads(
            (REPOSITORY_ROOT / "schemas" / "evidence-map.schema.json").read_text(encoding="utf-8")
        )

    def test_reference_export_matches_schema_and_semantics(self) -> None:
        _, errors = validate.load_and_validate_export(self.path, REPOSITORY_ROOT)
        self.assertEqual(errors, [])

    def test_additional_property_is_rejected(self) -> None:
        instance = copy.deepcopy(self.instance)
        instance["unexpected"] = True
        errors = validate.validate_json_schema(instance, self.schema)
        self.assertTrue(any("additional property" in item for item in errors), errors)

    def test_duplicate_claim_ids_are_rejected(self) -> None:
        instance = copy.deepcopy(self.instance)
        instance["claims"].append(copy.deepcopy(self.instance["claims"][0]))
        errors = validate.evidence_map_semantic_errors(instance)
        self.assertTrue(any("duplicate claim" in item for item in errors), errors)

    def test_false_full_read_is_rejected(self) -> None:
        instance = copy.deepcopy(self.instance)
        instance["coverage"]["claimed_full_read"] = True
        instance["coverage"]["inaccessible"] = ["Supplement"]
        errors = validate.evidence_map_semantic_errors(instance)
        self.assertTrue(any("claimed_full_read" in item for item in errors), errors)

    def test_located_evidence_required_for_moderate_support(self) -> None:
        instance = copy.deepcopy(self.instance)
        instance["claims"][0]["support"] = "moderate"
        instance["claims"][0]["evidence"] = []
        errors = validate.validate_json_schema(instance, self.schema)
        errors.extend(validate.evidence_map_semantic_errors(instance))
        self.assertTrue(any("locator" in item or "at least 1" in item for item in errors), errors)

    def test_json_strings_can_be_checked_against_fixture(self) -> None:
        report = validate.check_synthetic_fixture(validate.flatten_strings(self.instance))
        self.assertTrue(report.passed, report)


if __name__ == "__main__":
    unittest.main()
