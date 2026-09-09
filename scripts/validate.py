#!/usr/bin/env python3
"""Validate the repository, evidence-map responses, and JSON exports.

The checker deliberately has no third-party dependencies. It reports three
different layers separately: repository integrity, generic response structure,
and content assertions for the bundled synthetic fixture.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
import sys
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    ".gitattributes",
    ".github/ISSUE_TEMPLATE/bug-report.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/fixture-request.yml",
    ".github/ISSUE_TEMPLATE/prompt-improvement.yml",
    ".github/pull_request_template.md",
    ".github/workflows/validate.yml",
    "CHANGELOG.md",
    "CITATION.cff",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.md",
    "README.zh-CN.md",
    "ROADMAP.md",
    "SECURITY.md",
    "SUPPORT.md",
    "assets/social-preview.png",
    "docs/evaluation.md",
    "docs/evaluation.zh-CN.md",
    "docs/methodology.md",
    "docs/methodology.zh-CN.md",
    "docs/known-issues.md",
    "docs/publishing-checklist.md",
    "docs/quickstart.md",
    "docs/quickstart.zh-CN.md",
    "docs/releases/v0.1.1.md",
    "examples/current-chat-precedence/README.md",
    "examples/current-chat-precedence/expected-findings.md",
    "examples/current-chat-precedence/new-chat-paper.md",
    "examples/current-chat-precedence/old-project-paper.md",
    "examples/synthetic/expected-findings.md",
    "examples/synthetic/expected-output.json",
    "examples/synthetic/expected-output.md",
    "examples/synthetic/paper.md",
    "examples/synthetic/paper.pdf",
    "prompts/en/chat-triggers.md",
    "prompts/en/project-instructions-compact.md",
    "prompts/en/project-instructions.md",
    "prompts/zh-CN/chat-triggers.md",
    "prompts/zh-CN/project-instructions-compact.md",
    "prompts/zh-CN/project-instructions.md",
    "schemas/evidence-map.schema.json",
    "scripts/build_fixture_pdf.py",
    "scripts/tests/test_validate.py",
)

# Publishing instructions are deliberately excluded: they explain this token.
PUBLISH_PLACEHOLDER_FILES = (
    ".github/ISSUE_TEMPLATE/config.yml",
    "CITATION.cff",
    "docs/social-copy.md",
)

MARKDOWN_LINK = re.compile(
    r"!?\[[^\]\n]*\]\(\s*(?P<target><[^>]+>|[^\s)]+)(?:\s+[\"'][^\"']*[\"'])?\s*\)"
)
HTML_LINK = re.compile(
    r"<(?:a|img)\b[^>]*?\b(?:href|src)\s*=\s*[\"'](?P<target>[^\"']+)[\"']",
    flags=re.IGNORECASE,
)
FENCED_CODE = re.compile(r"^[ \t]*(```|~~~).*?^[ \t]*\1[ \t]*$", re.MULTILINE | re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")
CONFLICT_MARKER = re.compile(r"^(?:<{7}|={7}|>{7})(?:\s|$)", re.MULTILINE)


@dataclass(frozen=True)
class StructuralReport:
    score: int
    notes: tuple[str, ...]


@dataclass(frozen=True)
class FixtureReport:
    passed: bool
    hits: tuple[str, ...]
    misses: tuple[str, ...]
    fabricated_locators: tuple[str, ...]
    fabricated_details: tuple[str, ...]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def relative(path: Path, root: Path = ROOT) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def check_required_files(root: Path = ROOT) -> list[str]:
    return [
        f"missing required file: {item}"
        for item in REQUIRED_FILES
        if not (root / item).is_file()
    ]


def check_conflict_markers(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    suffixes = {".cff", ".json", ".md", ".py", ".yaml", ".yml"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.casefold() not in suffixes:
            continue
        try:
            text = read_text(path)
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"unreadable text file: {relative(path, root)}: {exc}")
            continue
        if CONFLICT_MARKER.search(text):
            errors.append(f"unresolved merge-conflict marker: {relative(path, root)}")
    return errors


def check_json_files(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*.json"):
        try:
            json.loads(read_text(path))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON: {relative(path, root)}: {exc}")
    return errors


def strip_code(text: str) -> str:
    """Remove code spans/blocks so documentation examples are not links."""

    return INLINE_CODE.sub("", FENCED_CODE.sub("", text))


def local_link_target(raw: str) -> str | None:
    target = unquote(raw.strip().strip("<>"))
    if not target or target.startswith("#"):
        return None
    parsed = urlsplit(target)
    if parsed.scheme or target.startswith("//"):
        return None
    return parsed.path


def exact_case_exists(root: Path, resolved: Path) -> bool:
    """Detect links that work locally but break on case-sensitive CI."""

    try:
        parts = resolved.relative_to(root).parts
    except ValueError:
        return False
    current = root
    for part in parts:
        try:
            names = {child.name for child in current.iterdir()}
        except OSError:
            return False
        if part not in names:
            return False
        current /= part
    return current.exists()


def check_markdown_links(root: Path = ROOT) -> list[str]:
    """Check Markdown and HTML links/images that resolve inside the repository."""

    errors: list[str] = []
    for path in root.rglob("*.md"):
        try:
            text = strip_code(read_text(path))
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"unreadable Markdown: {relative(path, root)}: {exc}")
            continue
        raw_targets = [match.group("target") for match in MARKDOWN_LINK.finditer(text)]
        raw_targets.extend(match.group("target") for match in HTML_LINK.finditer(text))
        for raw in raw_targets:
            target = local_link_target(raw)
            if target is None:
                continue
            if target.startswith(("/", "\\")) or re.match(r"^[A-Za-z]:[\\/]", target):
                errors.append(f"absolute local link: {relative(path, root)} -> {raw}")
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"link escapes repository: {relative(path, root)} -> {raw}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link: {relative(path, root)} -> {raw}")
            elif not exact_case_exists(root.resolve(), resolved):
                errors.append(f"case-mismatched local link: {relative(path, root)} -> {raw}")
    return errors


def check_prompt_contract(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    minimum_lengths = {
        "prompts/en/project-instructions.md": 3_000,
        "prompts/en/project-instructions-compact.md": 3_000,
        "prompts/zh-CN/project-instructions.md": 3_000,
        # Chinese conveys the same contract in substantially fewer characters.
        "prompts/zh-CN/project-instructions-compact.md": 1_500,
    }
    contracts = {
        "prompts/en/project-instructions.md": (
            "Round 1",
            "Round 2",
            "Paper fact",
            "not specified in the paper",
            "Export JSON",
            "untrusted document content",
            "Current-chat attachment precedence",
        ),
        "prompts/en/project-instructions-compact.md": (
            "Round 1",
            "Round 2",
            "Current-chat attachment precedence",
        ),
        "prompts/zh-CN/project-instructions.md": (
            "第一轮",
            "第二轮",
            "论文事实",
            "论文未明确说明",
            "导出 JSON",
            "不可信",
            "当前聊天附件优先",
        ),
        "prompts/zh-CN/project-instructions-compact.md": (
            "第一轮",
            "第二轮",
            "当前聊天附件优先",
        ),
    }
    for item, terms in contracts.items():
        path = root / item
        if not path.is_file():
            continue
        text = read_text(path)
        if len(text) < minimum_lengths[item]:
            errors.append(f"prompt appears unexpectedly short: {item}")
        for term in terms:
            if term not in text:
                errors.append(f"prompt contract missing {term!r}: {item}")
    return errors


def check_github_templates(root: Path = ROOT) -> list[str]:
    """Check key GitHub YAML invariants without requiring a YAML dependency."""

    errors: list[str] = []
    issue_dir = root / ".github" / "ISSUE_TEMPLATE"
    for path in issue_dir.glob("*.yml"):
        text = read_text(path)
        if "\t" in text:
            errors.append(f"tabs are not valid YAML indentation: {relative(path, root)}")
        if path.name == "config.yml":
            if "blank_issues_enabled:" not in text or "contact_links:" not in text:
                errors.append(f"incomplete issue-template config: {relative(path, root)}")
            continue
        for key in ("name:", "description:", "body:"):
            if not re.search(rf"^{re.escape(key)}", text, flags=re.MULTILINE):
                errors.append(f"issue form missing {key[:-1]!r}: {relative(path, root)}")
        ids = re.findall(r"^[ \t]+id:\s*([A-Za-z][A-Za-z0-9_-]*)\s*$", text, flags=re.MULTILINE)
        duplicates = sorted({item for item in ids if ids.count(item) > 1})
        if duplicates:
            errors.append(
                f"duplicate issue-form id(s) in {relative(path, root)}: {', '.join(duplicates)}"
            )
        types = re.findall(r"^[ \t]*-[ \t]+type:\s*(\S+)", text, flags=re.MULTILINE)
        invalid = [
            item
            for item in types
            if item not in {"checkboxes", "dropdown", "input", "markdown", "textarea"}
        ]
        if invalid:
            errors.append(
                f"unsupported issue-form type(s) in {relative(path, root)}: {', '.join(invalid)}"
            )

    workflow = root / ".github" / "workflows" / "validate.yml"
    if workflow.is_file():
        text = read_text(workflow)
        for token in (
            "on:",
            "permissions:",
            "jobs:",
            "actions/checkout@",
            "python -m unittest",
            "scripts/build_fixture_pdf.py --check",
            "scripts/validate.py",
            "--fixture synthetic",
            "--json examples/synthetic/expected-output.json",
        ):
            if token not in text:
                errors.append(f"validation workflow missing {token!r}")
        if re.search(r"^\s*contents:\s*write\s*$", text, flags=re.MULTILINE):
            errors.append("validation workflow requests unnecessary contents: write permission")
    return errors


def check_citation(root: Path = ROOT) -> list[str]:
    path = root / "CITATION.cff"
    if not path.is_file():
        return []
    text = read_text(path)
    errors: list[str] = []
    for key in ("cff-version", "message", "title", "type", "authors", "license"):
        if not re.search(rf"^{re.escape(key)}:", text, flags=re.MULTILINE):
            errors.append(f"CITATION.cff missing top-level key: {key}")
    for key in ("cff-version", "message", "title", "type", "license"):
        if re.search(rf"^{re.escape(key)}:\s*$", text, flags=re.MULTILINE):
            errors.append(f"CITATION.cff has empty scalar: {key}")
    if not re.search(r"^cff-version:\s*[\"']?1\.2\.0[\"']?\s*$", text, flags=re.MULTILINE):
        errors.append("CITATION.cff must declare cff-version 1.2.0")
    if not re.search(r"^authors:\s*\n\s+-\s+", text, flags=re.MULTILINE):
        errors.append("CITATION.cff must contain at least one author entry")
    return errors


def _decode_pdf_string(value: bytes) -> str:
    """Decode a literal PDF string sufficiently for the bundled fixture."""

    output = bytearray()
    index = 0
    escapes = {ord("n"): 10, ord("r"): 13, ord("t"): 9, ord("b"): 8, ord("f"): 12}
    while index < len(value):
        current = value[index]
        if current != 92:  # backslash
            output.append(current)
            index += 1
            continue
        index += 1
        if index >= len(value):
            break
        escaped = value[index]
        if escaped in escapes:
            output.append(escapes[escaped])
            index += 1
        elif escaped in b"()\\":
            output.append(escaped)
            index += 1
        elif 48 <= escaped <= 55:
            digits = bytes([escaped])
            index += 1
            while index < len(value) and len(digits) < 3 and 48 <= value[index] <= 55:
                digits += bytes([value[index]])
                index += 1
            output.append(int(digits, 8))
        elif escaped in b"\r\n":
            if escaped == 13 and index + 1 < len(value) and value[index + 1] == 10:
                index += 1
            index += 1
        else:
            output.append(escaped)
            index += 1
    return output.decode("latin-1", errors="replace")


def extract_pdf_text_basic(data: bytes) -> str:
    """Extract literal text from plain or ReportLab-compressed content streams."""

    chunks: list[str] = []
    for stream in re.finditer(rb"stream\r?\n(.*?)endstream", data, flags=re.DOTALL):
        payload = stream.group(1).strip()
        dictionary = data[max(0, stream.start() - 500) : stream.start()]
        try:
            if b"/ASCII85Decode" in dictionary:
                payload = base64.a85decode(payload, adobe=True)
            if b"/FlateDecode" in dictionary:
                payload = zlib.decompress(payload)
        except (ValueError, zlib.error):
            continue
        for literal in re.finditer(rb"\(((?:\\.|[^\\()])*)\)\s*Tj\b", payload):
            chunks.append(_decode_pdf_string(literal.group(1)))
    return "\n".join(chunks)


def check_pdf_fixture(root: Path = ROOT) -> list[str]:
    """Perform dependency-free corruption and key-content checks."""

    path = root / "examples" / "synthetic" / "paper.pdf"
    if not path.is_file():
        return []
    try:
        data = path.read_bytes()
    except OSError as exc:
        return [f"cannot read synthetic PDF: {exc}"]
    errors: list[str] = []
    if not data.startswith(b"%PDF-"):
        errors.append("examples/synthetic/paper.pdf: missing PDF header")
    if b"%%EOF" not in data[-1024:]:
        errors.append("examples/synthetic/paper.pdf: missing terminal EOF marker")
    if len(data) < 1_000:
        errors.append("examples/synthetic/paper.pdf: unexpectedly small (<1000 bytes)")
    page_count = len(re.findall(rb"/Type\s*/Page\b", data))
    if page_count != 2:
        errors.append(f"examples/synthetic/paper.pdf: expected 2 pages; found {page_count}")
    extracted = extract_pdf_text_basic(data)
    for phrase in (
        "TinyRank: Compact Document Classification",
        "8 percentage points",
        "best test-set macro-F1",
        "Table 1",
        "Table 2",
        "without C",
        "single GPU",
    ):
        if phrase not in extracted:
            errors.append(f"examples/synthetic/paper.pdf: key text not extractable: {phrase!r}")
    hash_match = re.search(rb"Canonical source SHA-256:\s*([0-9a-f]{64})", data)
    if hash_match:
        source = root / "examples" / "synthetic" / "paper.md"
        expected_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        embedded_hash = hash_match.group(1).decode("ascii")
        if embedded_hash != expected_hash:
            errors.append("examples/synthetic/paper.pdf: embedded source hash does not match paper.md")
    return errors


def publication_warnings(root: Path = ROOT) -> list[str]:
    warnings: list[str] = []
    for item in PUBLISH_PLACEHOLDER_FILES:
        path = root / item
        if path.is_file() and "YOUR_USERNAME" in read_text(path):
            warnings.append(f"replace YOUR_USERNAME before publishing: {item}")
    return warnings


def _json_type_matches(value: Any, expected: str) -> bool:
    mapping = {
        "array": lambda item: isinstance(item, list),
        "boolean": lambda item: isinstance(item, bool),
        "integer": lambda item: isinstance(item, int) and not isinstance(item, bool),
        "null": lambda item: item is None,
        "number": lambda item: isinstance(item, (int, float)) and not isinstance(item, bool),
        "object": lambda item: isinstance(item, dict),
        "string": lambda item: isinstance(item, str),
    }
    return expected in mapping and mapping[expected](value)


def validate_json_schema(instance: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    """Validate the JSON-Schema subset used by this repository."""

    errors: list[str] = []
    expected = schema.get("type")
    if expected is not None:
        expected_types = [expected] if isinstance(expected, str) else expected
        if not isinstance(expected_types, list) or not all(isinstance(item, str) for item in expected_types):
            return [f"{path}: schema has invalid type declaration"]
        if not any(_json_type_matches(instance, item) for item in expected_types):
            names = ", ".join(expected_types)
            return [f"{path}: expected type {names}; got {type(instance).__name__}"]

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} is not in enum {schema['enum']!r}")
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                errors.append(f"{path}: missing required property {key!r}")
        properties = schema.get("properties", {})
        for key, value in instance.items():
            child_path = f"{path}.{key}"
            if key in properties:
                errors.extend(validate_json_schema(value, properties[key], child_path))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{child_path}: additional property is not allowed")

    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            errors.append(f"{path}: expected at least {schema['minItems']} item(s)")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append(f"{path}: expected at most {schema['maxItems']} item(s)")
        if schema.get("uniqueItems"):
            serialized = [json.dumps(item, sort_keys=True, ensure_ascii=False) for item in instance]
            if len(serialized) != len(set(serialized)):
                errors.append(f"{path}: array items must be unique")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, value in enumerate(instance):
                errors.extend(validate_json_schema(value, item_schema, f"{path}[{index}]"))
        if "contains" in schema:
            matches = sum(not validate_json_schema(value, schema["contains"], path) for value in instance)
            minimum = schema.get("minContains", 1)
            if matches < minimum:
                errors.append(f"{path}: expected at least {minimum} item(s) matching contains")

    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            errors.append(f"{path}: string is shorter than minLength {schema['minLength']}")
        pattern = schema.get("pattern")
        if pattern and not re.search(pattern, instance):
            errors.append(f"{path}: string does not match pattern {pattern!r}")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: value is less than minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: value is greater than maximum {schema['maximum']}")

    for subschema in schema.get("allOf", []):
        errors.extend(validate_json_schema(instance, subschema, path))
    condition = schema.get("if")
    if isinstance(condition, dict) and not validate_json_schema(instance, condition, path):
        branch = schema.get("then")
        if isinstance(branch, dict):
            errors.extend(validate_json_schema(instance, branch, path))
    return errors


def evidence_map_semantic_errors(instance: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(instance, dict):
        return errors
    coverage = instance.get("coverage")
    if isinstance(coverage, dict) and coverage.get("claimed_full_read") is True:
        if coverage.get("uninspected") or coverage.get("inaccessible"):
            errors.append(
                "$.coverage: claimed_full_read cannot be true when uninspected or inaccessible is non-empty"
            )
    claims = instance.get("claims")
    if isinstance(claims, list):
        ids = [claim.get("id") for claim in claims if isinstance(claim, dict)]
        duplicates = sorted({item for item in ids if item is not None and ids.count(item) > 1})
        if duplicates:
            errors.append(f"$.claims: duplicate claim id(s): {', '.join(map(str, duplicates))}")
        for index, claim in enumerate(claims):
            if not isinstance(claim, dict):
                continue
            if claim.get("support") in {"strong", "moderate"}:
                evidence = claim.get("evidence")
                located = isinstance(evidence, list) and any(
                    isinstance(item, dict)
                    and isinstance(item.get("locator"), str)
                    and item["locator"].strip()
                    for item in evidence
                )
                if not located:
                    errors.append(
                        f"$.claims[{index}]: strong/moderate support requires a non-empty locator"
                    )
    return errors


def load_and_validate_export(path: Path, root: Path = ROOT) -> tuple[Any | None, list[str]]:
    try:
        instance = json.loads(read_text(path))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return None, [f"invalid JSON export: {path}: {exc}"]
    schema_path = root / "schemas" / "evidence-map.schema.json"
    try:
        schema = json.loads(read_text(schema_path))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return instance, [f"cannot load evidence-map schema: {exc}"]
    errors = validate_json_schema(instance, schema)
    errors.extend(evidence_map_semantic_errors(instance))
    return instance, errors


def check_example_exports(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for path in root.glob("examples/**/expected-output.json"):
        _, found = load_and_validate_export(path, root)
        errors.extend(f"{relative(path, root)}: {item}" for item in found)
    return errors


def _headings(text: str) -> list[str]:
    return [match.group(1).strip() for match in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.MULTILINE)]


def _contains_any(text: str, patterns: Iterable[str]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL) for pattern in patterns)


def _claim_table_rows(text: str) -> list[list[str]]:
    lines = text.splitlines()
    for index, line in enumerate(lines[:-1]):
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip().casefold() for cell in line.strip().strip("|").split("|")]
        header_is_claim_map = (
            any(re.search(r"core claim|claim|结论|主张", cell) for cell in cells)
            and any(re.search(r"evidence|证据", cell) for cell in cells)
            and any(re.search(r"support|支持", cell) for cell in cells)
            and any(re.search(r"boundary|gap|边界|缺口", cell) for cell in cells)
        )
        if not header_is_claim_map or index + 1 >= len(lines):
            continue
        separator = lines[index + 1]
        if not separator.lstrip().startswith("|") or not re.search(r"-{3,}", separator):
            continue
        rows: list[list[str]] = []
        for candidate in lines[index + 2 :]:
            if not candidate.lstrip().startswith("|"):
                break
            rows.append([cell.strip() for cell in candidate.strip().strip("|").split("|")])
        return rows
    return []


def _locators(text: str) -> set[str]:
    patterns = (
        r"\b(?:sections?|figures?|figs?\.?|tables?|equations?|appendices?|appendix)\s*[A-Za-z]?\d+(?:\.\d+)*(?:\s*[–—-]\s*[A-Za-z]?\d+(?:\.\d+)*)?",
        r"(?:第\s*)?\d+(?:\.\d+)?\s*节",
        r"(?:图|表|公式|附录)\s*[A-Za-z0-9一二三四五六七八九十]+",
    )
    found: set[str] = set()
    for pattern in patterns:
        found.update(match.group(0).casefold() for match in re.finditer(pattern, text, re.IGNORECASE))
    return found


def score_response(path: Path) -> StructuralReport:
    text = read_text(path)
    headings = "\n".join(_headings(text))
    notes: list[str] = []

    section_groups = (
        (r"reading coverage|coverage|access limit|阅读覆盖|覆盖范围|访问限制",),
        (r"research question|research problem|研究问题",),
        (r"method map|method chain|technical route|技术路线|方法地图",),
        (r"innovation|novelty|创新",),
        (r"experiment map|experiment inventory|实验地图|实验清单",),
        (r"claim.{0,3}evidence|evidence matrix|结论.{0,3}证据|主张.{0,3}证据",),
        (r"consistency|一致性",),
        (r"unknown|risk register|未知|风险",),
    )
    found_sections = sum(_contains_any(headings, group) for group in section_groups)
    section_score = found_sections * 4
    notes.append(f"required headings: {found_sections}/8 ({section_score}/32)")

    rows = _claim_table_rows(text)
    table_score = (8 if rows else 0) + min(12, len(rows) * 4)
    notes.append(f"claim/evidence table rows: {len(rows)} ({table_score}/20)")

    locators = _locators(text)
    locator_score = min(16, len(locators) * 4)
    notes.append(f"unique evidence locators: {len(locators)} ({locator_score}/16)")

    type_patterns = (
        r"\[paper fact\]|\[论文事实\]",
        r"\[author interpretation\]|\[作者解释\]",
        r"\[analyst judgment\]|\[分析判断\]",
        r"\[unknown\]|\[未知\]",
    )
    found_types = sum(_contains_any(text, (pattern,)) for pattern in type_patterns)
    type_score = found_types * 3
    notes.append(f"exact claim-type labels: {found_types}/4 ({type_score}/12)")

    support_values = {
        "strong",
        "moderate",
        "weak",
        "cannot judge",
        "强",
        "中等",
        "弱",
        "无法判断",
    }
    valid_support_rows = sum(
        any(cell.strip().casefold() in support_values for cell in row) for row in rows
    )
    support_score = 8 if valid_support_rows >= 3 else valid_support_rows * 2
    notes.append(f"claim rows with valid support label: {valid_support_rows} ({support_score}/8)")

    unknown_score = 6 if _contains_any(
        text, (r"not specified in the paper", r"论文未明确说明")
    ) else 0
    notes.append(f"explicit unknown marker: {unknown_score}/6")

    coverage_signals = sum(
        _contains_any(text, patterns)
        for patterns in (
            (r"\binspected\b", r"已检查|已阅读"),
            (r"missing.{0,2}inaccessible|\binaccessible\b|未检查|不可访问|缺失",),
        )
    )
    coverage_score = coverage_signals * 3
    notes.append(f"coverage signals: {coverage_signals}/2 ({coverage_score}/6)")

    score = section_score + table_score + locator_score + type_score + support_score + unknown_score + coverage_score
    if len(text.strip()) < 800:
        score = min(score, 60)
        notes.append("short-response cap applied (<800 characters)")
    return StructuralReport(score=score, notes=tuple(notes))


def flatten_strings(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(flatten_strings(item) for item in value)
    if isinstance(value, dict):
        return "\n".join(flatten_strings(item) for item in value.values())
    return "" if value is None else str(value)


SYNTHETIC_FINDINGS: tuple[tuple[str, tuple[tuple[str, ...], ...]], ...] = (
    (
        "F1 Dataset B gain is four, not eight, percentage points",
        (
            (r"dataset\s*b|数据集\s*b",),
            (r"\+?0\.0?4\b|\b4\s*(?:percentage\s*)?points?\b|4\s*个?百分点",),
            (r"false|contradict|not\s+(?:an?\s+)?8|only|overstat|错误|不符|矛盾|仅|只有|夸大",),
        ),
    ),
    (
        "F2 Module C is not shown to be essential",
        (
            (r"without\s+c\b|remov(?:e|ing)\s+(?:module\s+)?c\b|移除\s*c|去掉\s*c",),
            (r"\b0\.78\b",),
            (r"unchanged|no\s+(?:observed\s+)?(?:gain|change|contribution)|not\s+(?:shown|demonstrated|supported)|contradict|不变|没有.*(?:变化|贡献)|未.*(?:证明|支持)|矛盾",),
        ),
    ),
    (
        "F3 cross-domain generalization was not tested",
        (
            (r"cross[- ]domain|generaliz|跨域|跨领域|泛化",),
            (r"not\s+test|no\s+cross[- ]domain|within[- ]dataset|separate\s+in[- ]domain|too\s+broad|未.*测试|没有.*(?:迁移|跨域)|各自.*数据集|过度|过宽",),
        ),
    ),
    (
        "F4 robustness evidence covers one deletion condition on Dataset A",
        (
            (r"robust|鲁棒",),
            (r"10\s*%",),
            (r"dataset\s*a|数据集\s*a",),
            (r"only|one\s+(?:condition|corruption|level)|too\s+broad|仅|只|单一|一种",),
        ),
    ),
    (
        "F5 compute-efficiency claim is unsupported",
        (
            (r"compute|efficien|hardware|计算|效率|硬件",),
            (r"unsupported|cannot\s+judge|no\s+(?:cost|measurement|hardware|comparison)|not\s+(?:measured|specified)|未报告|无法判断|缺少|未测量|不支持",),
        ),
    ),
    (
        "F6 test-set checkpoint selection creates leakage/selection risk",
        (
            (r"checkpoint|检查点",),
            (r"test[- ]set|test\s+(?:macro|f1)|测试集",),
            (r"leak|selection\s+bias|optimis|泄漏|选择偏差|乐观",),
        ),
    ),
    (
        "F7 single-run results and reproducibility/statistical details are missing",
        (
            (r"one\s+run|single[- ]run|one\s+reported\s+run|一次运行|单次运行|仅.*一次",),
            (r"seed|random|repeat|variation|confidence|statistical|种子|重复|方差|置信|统计",),
            (r"not\s+(?:reported|specified)|no\s+(?:repeat|variation|confidence|test)|missing|未报告|未明确|没有|缺少",),
        ),
    ),
    (
        "F8 ablations are limited to Dataset A",
        (
            (r"ablation|消融",),
            (r"dataset\s*a|数据集\s*a",),
            (r"only|limited|not.*dataset\s*b|仅|只|局限|未.*数据集\s*b",),
        ),
    ),
)


def _fabricated_synthetic_locators(text: str) -> list[str]:
    fabricated: list[str] = []
    pattern = re.compile(
        r"\b(?:(?P<numbered>section|table|figure|fig\.?|equation)\s*"
        r"(?P<numbered_label>[A-Za-z]?\d+(?:\.\d+)*)|"
        r"(?P<appendix>appendix)\s*(?P<appendix_label>[A-Za-z]|\d+(?:\.\d+)*))",
        flags=re.IGNORECASE,
    )
    for match in pattern.finditer(text):
        context = text[max(0, match.start() - 70) : min(len(text), match.end() + 70)]
        if _contains_any(
            context,
            (
                r"\b(?:no|none|absent|missing|not\s+present|inaccessible)\b",
                r"不存在|没有|缺失|未提供|不可访问",
            ),
        ):
            continue
        kind = (match.group("numbered") or match.group("appendix")).rstrip(".").casefold()
        label = match.group("numbered_label") or match.group("appendix_label")
        allowed = False
        if kind == "section" and label[0].isdigit():
            allowed = 1 <= int(label.split(".", 1)[0]) <= 8
        elif kind == "table" and label.isdigit():
            allowed = int(label) in {1, 2}
        if not allowed:
            fabricated.append(match.group(0))

    chinese_pattern = re.compile(
        r"(?P<kind>第|图|表|公式|附录)\s*(?P<label>\d+(?:\.\d+)?|[A-Za-z])(?:\s*节)?"
    )
    for match in chinese_pattern.finditer(text):
        context = text[max(0, match.start() - 70) : min(len(text), match.end() + 70)]
        if _contains_any(context, (r"不存在|没有|缺失|未提供|不可访问", r"\bno\b")):
            continue
        kind, label = match.group("kind"), match.group("label")
        allowed = (
            kind == "第" and label[0].isdigit() and 1 <= int(label.split(".")[0]) <= 8
        ) or (kind == "表" and label.isdigit() and int(label) in {1, 2})
        if not allowed:
            fabricated.append(match.group(0))
    return sorted(set(fabricated), key=str.casefold)


def _fabricated_synthetic_details(text: str) -> list[str]:
    details: list[str] = []
    patterns = {
        "invented numeric seed": r"(?:random\s+)?seed\s*(?:=|:|was|is)?\s*\d+|随机种子\s*(?:为|=|:)?\s*\d+",
        "invented p-value": r"\bp\s*[<=>]\s*0?\.\d+",
        "invented GPU model": r"\b(?:A100|H100|V100|RTX\s*\d{3,4})\b",
    }
    for label, pattern in patterns.items():
        if re.search(pattern, text, flags=re.IGNORECASE):
            details.append(label)
    return details


def check_synthetic_fixture(text: str) -> FixtureReport:
    hits: list[str] = []
    misses: list[str] = []
    for name, groups in SYNTHETIC_FINDINGS:
        if all(_contains_any(text, patterns) for patterns in groups):
            hits.append(name)
        else:
            misses.append(name)
    fabricated_locators = _fabricated_synthetic_locators(text)
    fabricated_details = _fabricated_synthetic_details(text)
    critical = {SYNTHETIC_FINDINGS[0][0], SYNTHETIC_FINDINGS[1][0]}
    passed = (
        len(hits) >= 7
        and critical.issubset(hits)
        and not fabricated_locators
        and not fabricated_details
    )
    return FixtureReport(
        passed=passed,
        hits=tuple(hits),
        misses=tuple(misses),
        fabricated_locators=tuple(fabricated_locators),
        fabricated_details=tuple(fabricated_details),
    )


def repository_errors(root: Path = ROOT) -> list[str]:
    return (
        check_required_files(root)
        + check_conflict_markers(root)
        + check_json_files(root)
        + check_markdown_links(root)
        + check_prompt_contract(root)
        + check_github_templates(root)
        + check_citation(root)
        + check_pdf_fixture(root)
        + check_example_exports(root)
    )


def print_repository_result(errors: list[str], warnings: list[str]) -> None:
    print(f"Repository validation: {'FAIL' if errors else 'PASS'}")
    for error in errors:
        print(f"  ERROR: {error}")
    for warning in warnings:
        print(f"  NOTE: {warning}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python scripts/validate.py\n"
            "  python scripts/validate.py --response response.md\n"
            "  python scripts/validate.py --response response.md --fixture synthetic\n"
            "  python scripts/validate.py --json evidence-map.json --fixture synthetic\n"
            "  python scripts/validate.py --strict-publish"
        ),
    )
    parser.add_argument("--response", type=Path, help="Markdown response to structurally smoke-test")
    parser.add_argument("--json", dest="json_export", type=Path, help="JSON evidence map to validate")
    parser.add_argument(
        "--fixture",
        choices=("synthetic",),
        help="also check response/export against a bundled fixture's content assertions",
    )
    parser.add_argument(
        "--strict-publish",
        action="store_true",
        help="treat unresolved owner placeholders as errors",
    )
    args = parser.parse_args(argv)

    if args.fixture and not (args.response or args.json_export):
        parser.error("--fixture requires --response or --json")

    errors = repository_errors()
    warnings = publication_warnings()
    if args.strict_publish:
        errors.extend(
            f"publishing placeholder unresolved: {item.rsplit(': ', 1)[-1]}"
            for item in warnings
        )
        warnings = []
    print_repository_result(errors, warnings)

    fixture_texts: list[tuple[str, str]] = []
    if args.response:
        response = args.response.resolve()
        if not response.is_file():
            errors.append(f"response file not found: {response}")
            print(f"Response structural smoke test: FAIL\n  ERROR: file not found: {response}")
        else:
            report = score_response(response)
            passed = report.score >= 75
            print(f"Response structural smoke test: {'PASS' if passed else 'FAIL'} ({report.score}/100)")
            for note in report.notes:
                print(f"  {note}")
            print("  Scope: structure only; this score does not establish scientific correctness.")
            if not passed:
                errors.append(f"response structural score below 75: {report.score}")
            fixture_texts.append((str(response), read_text(response)))

    if args.json_export:
        export = args.json_export.resolve()
        if not export.is_file():
            errors.append(f"JSON export file not found: {export}")
            print(f"JSON export validation: FAIL\n  ERROR: file not found: {export}")
        else:
            instance, export_errors = load_and_validate_export(export)
            print(f"JSON export validation: {'FAIL' if export_errors else 'PASS'}")
            for error in export_errors:
                print(f"  ERROR: {error}")
            errors.extend(f"JSON export: {item}" for item in export_errors)
            if instance is not None:
                fixture_texts.append((str(export), flatten_strings(instance)))

    if args.fixture == "synthetic":
        for label, text in fixture_texts:
            report = check_synthetic_fixture(text)
            print(
                f"Synthetic fixture assertions ({label}): "
                f"{'PASS' if report.passed else 'FAIL'} ({len(report.hits)}/8 findings)"
            )
            for hit in report.hits:
                print(f"  HIT: {hit}")
            for miss in report.misses:
                print(f"  MISS: {miss}")
            for locator in report.fabricated_locators:
                print(f"  ERROR: possible fabricated locator: {locator}")
            for detail in report.fabricated_details:
                print(f"  ERROR: possible {detail}")
            print("  Scope: deterministic fixture assertions; manual evidence review is still required.")
            if not report.passed:
                errors.append(f"synthetic fixture assertions failed for {label}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
