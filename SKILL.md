---
name: paper-evidence-map
description: Adaptive, evidence-grounded reading for a single research paper. Use when the user wants to decide whether a paper is worth reading, understand a method or experiment, check whether a claim is supported, prepare a presentation, or turn a paper-internal observation into a candidate research gap or idea.
metadata:
  version: "0.2.0"
---

# Paper Evidence Map — Router

Paper Evidence Map should answer the user's current research need with the minimum sufficient reading depth. It is not a fixed two-round pipeline.

## Routing protocol

1. Read `manifest.yaml`.
2. Load every file under `always_load`.
3. Infer the user's immediate goal using `router/goal-router.md`.
4. Select the minimum useful reading depth using `router/depth-router.md`.
5. Load only the lens guidance required by the selected goal(s). Do not load every lens by default.
6. Inspect only the source material needed to answer the current question reliably.
7. Stop when the user's immediate goal is satisfied; escalate depth only when decisive uncertainty remains.

## Default behavior

If the user supplies a paper without asking for a full deep read, default to **Triage**, not a full evidence map. Explain what the paper is useful for, what to read first, and any promising candidate gap/idea hooks that are already visible. Do not automatically generate a complete method map, experiment inventory, claim matrix, and limitation audit.

Follow-up questions should reuse already established source/evidence locations when available. Do not rebuild the whole paper analysis for a narrow follow-up.

## Backward compatibility

- `Round 1` / `第一轮` -> Deep evidence-map reading.
- `Round 2` / `第二轮` -> skeptical Audit of consequential claims.
- `Focus: <question>` / `聚焦 <问题>` -> Targeted reading.
- `Export JSON` -> structured export using the repository schema when available.

These triggers are shortcuts, not the required interface. Natural-language research goals take precedence.

## On-demand references

Use detailed evidence methodology, schemas, and evaluation rules only when the current task needs them, as declared in `manifest.yaml`. The existing Project prompts remain compatibility/runtime surfaces; they are not a reason to load the entire workflow into context for every request.
