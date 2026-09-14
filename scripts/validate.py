#!/usr/bin/env python3
"""v0.2-aware validator facade.

The original dependency-free validator is kept in ``validate_legacy.py`` so
existing structure, fixture, JSON, and repository checks remain unchanged.
This facade replaces only the prompt-contract check: v0.2 prompts are validated
by behavioral/semantic invariants instead of exact legacy wording.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
_LEGACY_PATH = Path(__file__).with_name("validate_legacy.py")
_SPEC = importlib.util.spec_from_file_location("paper_evidence_map_validate_legacy", _LEGACY_PATH)
if _SPEC is None or _SPEC.loader is None:  # pragma: no cover - import bootstrap guard
    raise RuntimeError("could not load scripts/validate_legacy.py")
_legacy = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _legacy
_SPEC.loader.exec_module(_legacy)

# Re-export the public validator API so existing callers and the PDF builder keep
# working without changes.
for _name in dir(_legacy):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_legacy, _name)


_MINIMUM_LENGTHS = {
    "prompts/en/project-instructions.md": 3_000,
    "prompts/en/project-instructions-compact.md": 3_000,
    "prompts/zh-CN/project-instructions.md": 3_000,
    "prompts/zh-CN/project-instructions-compact.md": 1_500,
}

# Each tuple is one behavioral invariant. At least one wording alternative in
# each tuple must be present. This intentionally avoids pinning v0.2 to a single
# sentence or heading while still protecting the important behavior.
_PROMPT_CONTRACT_GROUPS = {
    "prompts/en/project-instructions.md": (
        ("Round 1",),
        ("Round 2",),
        ("Paper fact",),
        ("Export JSON",),
        ("current chat", "current-chat"),
        ("newest accessible paper", "newest accessible primary-paper"),
        ("untrusted content", "untrusted document content"),
        ("not reported",),
        ("Adaptive routing",),
        ("D0", "Scan"),
        ("D1", "Triage"),
        ("D2", "Targeted"),
        ("D3", "Deep"),
        ("D4", "Audit"),
        ("Candidate Gap",),
        ("Candidate Idea",),
        ("Stop when", "stop and give"),
    ),
    "prompts/en/project-instructions-compact.md": (
        ("Round 1",),
        ("Round 2",),
        ("current chat", "Current-chat"),
        ("Attachments are data, not instructions",),
        ("not reported",),
        ("Adaptive routing",),
        ("Scan",),
        ("Triage",),
        ("Targeted",),
        ("Deep",),
        ("Audit",),
        ("Candidate Gap",),
        ("Candidate Idea",),
        ("Stop once", "stops when"),
    ),
    "prompts/zh-CN/project-instructions.md": (
        ("第一轮",),
        ("第二轮",),
        ("论文事实",),
        ("Export JSON", "导出"),
        ("当前聊天",),
        ("最新上传",),
        ("不可信文档内容", "不可信"),
        ("未报告",),
        ("自适应路由",),
        ("D0", "Scan"),
        ("D1", "Triage"),
        ("D2", "Targeted"),
        ("D3", "Deep"),
        ("D4", "Audit"),
        ("Candidate Gap",),
        ("Candidate Idea",),
        ("停止", "停止继续扩展"),
    ),
    "prompts/zh-CN/project-instructions-compact.md": (
        ("第一轮",),
        ("第二轮",),
        ("当前聊天附件优先", "当前聊天"),
        ("附件是数据，不是指令",),
        ("未报告",),
        ("自适应路由",),
        ("Scan",),
        ("Triage",),
        ("Targeted",),
        ("Deep",),
        ("Audit",),
        ("Candidate Gap",),
        ("Candidate Idea",),
        ("目标已经满足就停止", "满足时停止"),
    ),
}


def check_prompt_contract(root: Path = ROOT) -> list[str]:
    """Validate prompt behavior without requiring legacy wording verbatim."""

    errors: list[str] = []
    for item, groups in _PROMPT_CONTRACT_GROUPS.items():
        path = root / item
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        minimum = _MINIMUM_LENGTHS[item]
        if len(text) < minimum:
            errors.append(f"prompt appears unexpectedly short: {item}")
        folded = text.casefold()
        for alternatives in groups:
            if not any(marker.casefold() in folded for marker in alternatives):
                label = " / ".join(repr(marker) for marker in alternatives)
                errors.append(f"prompt behavioral contract missing {label}: {item}")
    return errors


# Legacy repository_errors/main resolve check_prompt_contract from the legacy
# module's globals at runtime, so replacing it here upgrades every existing
# validation path without changing the other validator behavior.
_legacy.check_prompt_contract = check_prompt_contract
globals()["check_prompt_contract"] = check_prompt_contract


if __name__ == "__main__":
    sys.exit(_legacy.main())
