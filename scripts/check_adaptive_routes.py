#!/usr/bin/env python3
"""Validate the machine-readable adaptive-routing fixture contract.

This checker does not score model behavior. It ensures the routing test matrix is
complete, internally consistent, and suitable for repeated live evaluations.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples" / "adaptive-routing" / "expected-routes.json"

ALLOWED_DEPTHS = {
    "scan",
    "triage",
    "targeted",
    "targeted_or_audit",
    "triage_or_targeted",
    "deep",
    "audit",
}
EXPECTED_IDS = {f"R{i}" for i in range(1, 8)}
EXPECTED_FAILURES = {
    "MISROUTE",
    "OVERREAD",
    "UNDERREAD",
    "NO_STOP",
    "EVIDENCE_BYPASS",
    "IDEA_OVERPROMOTION",
}


def main() -> int:
    errors: list[str] = []
    try:
        data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    except Exception as exc:  # deliberate standalone diagnostic
        print(f"FAIL: cannot parse {FIXTURE.relative_to(ROOT)}: {exc}")
        return 1

    if data.get("fixture") != "adaptive-routing-v0.2":
        errors.append("fixture id must be 'adaptive-routing-v0.2'")

    source = data.get("source")
    if not isinstance(source, str) or not (ROOT / source).is_file():
        errors.append("source must point to an existing repository file")

    cases = data.get("cases")
    if not isinstance(cases, list):
        errors.append("cases must be an array")
        cases = []

    ids = [case.get("id") for case in cases if isinstance(case, dict)]
    if set(ids) != EXPECTED_IDS or len(ids) != len(EXPECTED_IDS):
        errors.append("cases must contain exactly R1 through R7 once each")

    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"cases[{index}] must be an object")
            continue
        cid = case.get("id", f"index-{index}")
        request = case.get("request")
        if not isinstance(request, str) or not request.strip():
            errors.append(f"{cid}: request must be a non-empty string")
        depth = case.get("expected_depth")
        if depth not in ALLOWED_DEPTHS:
            errors.append(f"{cid}: invalid expected_depth {depth!r}")
        for key in ("required_signals", "forbidden_signals"):
            value = case.get(key)
            if not isinstance(value, list) or not value or not all(
                isinstance(item, str) and item.strip() for item in value
            ):
                errors.append(f"{cid}: {key} must be a non-empty string array")
            elif len(value) != len(set(value)):
                errors.append(f"{cid}: {key} contains duplicates")

    failures = data.get("failure_classes")
    if not isinstance(failures, list) or set(failures) != EXPECTED_FAILURES:
        errors.append("failure_classes must match the v0.2 routing failure taxonomy")

    if errors:
        print("Adaptive routing fixture: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Adaptive routing fixture: PASS")
    print(f"- {len(cases)} routing cases")
    print(f"- {len(failures)} failure classes")
    print("- live model behavior still requires manual/repeated evaluation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
