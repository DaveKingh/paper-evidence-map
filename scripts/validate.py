#!/usr/bin/env python3
"""Validate repository integrity and optionally smoke-test a Markdown response.

Uses only the Python standard library. Structural checks are not a substitute
for the content-level rubric in docs/evaluation.md.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "SECURITY.md",
    "prompts/en/project-instructions.md",
    "prompts/zh-CN/project-instructions.md",
    "examples/synthetic/paper.md",
    "examples/synthetic/expected-findings.md",
    "examples/synthetic/expected-output.md",
    "schemas/evidence-map.schema.json",
    "docs/evaluation.md",
    ".github/workflows/validate.yml",
)

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def check_required_files() -> list[str]:
    return [f"missing required file: {relative}" for relative in REQUIRED_FILES if not (ROOT / relative).is_file()]


def check_json_files() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON: {path.relative_to(ROOT)}: {exc}")
    return errors


def normalize_link(raw: str) -> str:
    target = raw.strip().strip("<>")
    if " " in target and not target.startswith("#"):
        # Markdown links may contain an optional quoted title.
        target = target.split(" \"", 1)[0].split(" '", 1)[0]
    return unquote(target.split("#", 1)[0])


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw in MARKDOWN_LINK.findall(text):
            target = normalize_link(raw)
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"link escapes repository: {path.relative_to(ROOT)} -> {raw}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link: {path.relative_to(ROOT)} -> {raw}")
    return errors


def check_prompt_contract() -> list[str]:
    errors: list[str] = []
    contracts = {
        "prompts/en/project-instructions.md": (
            "Round 1",
            "Round 2",
            "Paper fact",
            "not specified in the paper",
            "Export JSON",
        ),
        "prompts/zh-CN/project-instructions.md": (
            "第一轮",
            "第二轮",
            "论文事实",
            "论文未明确说明",
            "导出 JSON",
        ),
    }
    for relative, terms in contracts.items():
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if len(text) < 3_000:
            errors.append(f"prompt appears unexpectedly short: {relative}")
        for term in terms:
            if term not in text:
                errors.append(f"prompt contract missing {term!r}: {relative}")
    return errors


def repository_warnings() -> list[str]:
    warnings: list[str] = []
    for relative in ("README.md", "README.zh-CN.md", "CITATION.cff", "docs/social-copy.md"):
        path = ROOT / relative
        if path.exists() and "YOUR_USERNAME" in path.read_text(encoding="utf-8"):
            warnings.append(f"replace YOUR_USERNAME before publishing: {relative}")
    return warnings


def contains_any(text: str, choices: tuple[str, ...]) -> bool:
    lowered = text.casefold()
    return any(choice.casefold() in lowered for choice in choices)


def score_response(path: Path) -> tuple[int, list[str]]:
    text = path.read_text(encoding="utf-8")
    notes: list[str] = []

    section_groups = (
        ("reading coverage", "阅读覆盖"),
        ("research question", "研究问题"),
        ("method map", "技术路线"),
        ("innovation", "创新点"),
        ("experiment map", "实验地图"),
        ("claim–evidence", "claim-evidence", "结论—证据", "结论-证据"),
        ("consistency", "一致性"),
        ("unknown", "未知"),
    )
    found_sections = sum(contains_any(text, group) for group in section_groups)
    section_score = round(30 * min(found_sections, 8) / 8)
    notes.append(f"sections: {found_sections}/8 ({section_score}/30)")

    locators = re.findall(
        r"\b(?:section|figure|fig\.?|table|equation|appendix)\s*[A-Za-z0-9.–-]+|(?:第\s*)?\d+(?:\.\d+)?\s*节|(?:图|表|公式|附录)\s*[A-Za-z0-9一二三四五六七八九十.–-]+",
        text,
        flags=re.IGNORECASE,
    )
    locator_score = min(20, len(locators) * 4)
    notes.append(f"evidence locators: {len(locators)} ({locator_score}/20)")

    type_groups = (
        ("[paper fact]", "[论文事实]"),
        ("[author interpretation]", "[作者解释]"),
        ("[analyst judgment]", "[分析判断]"),
        ("[unknown]", "[未知]"),
    )
    found_types = sum(contains_any(text, group) for group in type_groups)
    type_score = round(15 * min(found_types, 4) / 4)
    notes.append(f"claim-type labels: {found_types}/4 ({type_score}/15)")

    support_groups = (
        ("strong", "强"),
        ("moderate", "中等"),
        ("weak", "弱"),
        ("cannot judge", "无法判断"),
    )
    found_support = sum(contains_any(text, group) for group in support_groups)
    support_score = round(15 * min(found_support, 4) / 4)
    notes.append(f"support labels: {found_support}/4 ({support_score}/15)")

    unknown_score = 10 if contains_any(text, ("not specified in the paper", "论文未明确说明")) else 0
    notes.append(f"explicit unknown marker: {unknown_score}/10")

    boundary_score = 10 if contains_any(text, ("boundary/gap", "boundary", "narrow", "边界/缺口", "边界", "收窄")) else 0
    notes.append(f"claim-boundary signal: {boundary_score}/10")

    return section_score + locator_score + type_score + support_score + unknown_score + boundary_score, notes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--response", type=Path, help="optional Markdown response to smoke-test")
    args = parser.parse_args()

    errors = check_required_files() + check_json_files() + check_markdown_links() + check_prompt_contract()
    warnings = repository_warnings()

    if errors:
        print("Repository validation: FAIL")
        for error in errors:
            print(f"  ERROR: {error}")
    else:
        print("Repository validation: PASS")

    for warning in warnings:
        print(f"  NOTE: {warning}")

    if args.response:
        response = args.response.resolve()
        if not response.is_file():
            print(f"Response smoke test: FAIL\n  ERROR: file not found: {response}")
            return 1
        score, notes = score_response(response)
        print(f"Response structural score: {score}/100")
        for note in notes:
            print(f"  {note}")
        print("  Reminder: use docs/evaluation.md to score scientific correctness.")
        if score < 75:
            errors.append(f"response structural score below 75: {score}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

