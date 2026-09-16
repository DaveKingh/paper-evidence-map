# Adaptive Routing Evaluation

PEM v0.2 adds a behavior that must be tested separately from evidence fidelity: **does the workflow choose an appropriate reading scope for the user's current goal?**

A model can be scientifically careful yet still fail v0.2 by producing a full evidence map when the user only asked whether the paper is worth reading.

The canonical routing fixture is under [`examples/adaptive-routing/`](../examples/adaptive-routing/README.md). Its machine-readable contract is [`expected-routes.json`](../examples/adaptive-routing/expected-routes.json).

Before live testing, validate the fixture contract:

```bash
python scripts/check_adaptive_routes.py
```

This deterministic check verifies the routing test matrix itself; it does **not** score model behavior.

## Evaluation dimensions

Score each live run on four routing dimensions before applying the existing evidence-fidelity rubric where relevant.

| Dimension | Pass condition |
|---|---|
| Goal fit | The response addresses the user's actual decision/question rather than a generic paper template. |
| Depth fit | The response uses no more depth than necessary for a reliable answer. |
| Lens discipline | Only relevant analytical capabilities appear; unrelated inventories are omitted. |
| Stop behavior | The response stops after satisfying the current goal and does not automatically continue into deeper analysis. |

A routing failure is recorded even if the extra analysis is factually correct.

**Required signals are semantic, not formatting requirements.** For example, an R5 response can satisfy `gap_origin_if_present`, `gap_status_if_present`, and `novelty_status_if_present` through clear natural-language wording; it does not need to print raw schema field names unless structured status is itself requested.

## Core routing fixture

Use a fresh chat for every case with the same prompt version, model/mode, and `examples/synthetic/paper.pdf`. The seven canonical cases R1–R7 are defined machine-readably in the fixture.

| ID | User request | Expected route | Required behavior | Failure examples |
|---|---|---|---|---|
| R1 | “What is this paper about?” | Scan | Short orientation: problem and core contribution; no claim matrix. | Full experiment inventory or deep audit. |
| R2 | “Is this worth reading if I care about trustworthy model evaluation?” | Triage | Fit judgment, priority sections/evidence, and next reading step. Research Gap/Idea content is optional and should not be manufactured merely to fill Triage. | Full Deep review by default or unnecessary Gap/Idea expansion. |
| R3 | “Is Module C actually necessary?” | Targeted + Evidence/Critical | Inspect decisive ablation and give a bounded conclusion. | Reconstruct unrelated sections first. |
| R4 | “Does the paper support its broad robustness claim?” | Targeted/Audit | Inspect robustness evidence and narrow to tested scope. | Accept broad robustness without boundary control. |
| R5 | “Can this paper give me a research idea?” | Triage/Targeted + Gap/Idea | Surface a Candidate Gap/Idea if justified, communicate origin/internal support/external novelty status semantically, and give the next check. | Claim verified novelty from the paper alone. |
| R6 | “Read this paper deeply.” | Deep | Broad method/experiment/claim–evidence coverage over all major evidence that could materially affect comprehensive understanding. | Stop at a superficial summary, or mechanically dump low-value inventory without synthesis. |
| R7 | “Strictly audit the most important conclusions.” | Audit | Re-open decisive evidence, seek alternatives/counterevidence, narrow claims. | Merely restate a prior Deep pass. |

## Extended routing cases

These are valuable live tests but are intentionally kept outside the minimal machine-readable fixture so the fixture stays small and stable.

| ID | User request | Expected route | Required behavior |
|---|---|---|---|
| R8 | “I need to present this paper tomorrow.” | Targeted/Deep + Presentation | Prioritize motivation, method flow, decisive result, limitation, likely questions. Deep may govern evidence coverage, but the output should remain presentation-shaped rather than exposing a full Deep evidence map. |
| R9 | “What should I learn before I can understand Section 3?” | Triage/Targeted + Learning | Minimal prerequisite path tied to that section. |
| R10 | Upload paper and say “take a look.” | Triage | Brief fit/value map and suggested reading paths; do not assume Deep or manufacture research ideas. |
| R11 | Context: “I am reading papers mainly to find new research ideas.” Then ask: “Is this one worth reading?” | Triage + Relevance + Contribution + Gap + Idea | Inherit the established idea-seeking goal; research leverage is required. Decide whether a paper-supported hook exists, surface a Candidate Gap/Idea if justified, and stop before full Gap Mining. | Treat the question as generic relevance-only Triage, ask the user to repeat the already established goal, or omit research leverage. |

R11 is specifically a **goal-carryover** test: short follow-up wording must not erase a stable research purpose already established in the conversation. At the same time, the inherited goal does not justify automatic Deep/Audit behavior; the Minimum-Sufficient and STOP rules still apply.

## Legacy compatibility matrix

These cases ensure v0.2 does not break v0.1 workflows.

| ID | Trigger | Expected behavior |
|---|---|---|
| L1 | `Round 1` / `第一轮` | Deep evidence map. |
| L2 | `Round 2` / `第二轮` after L1 | Audit with re-inspection rather than paraphrase. |
| L3 | `Focus: Module C` / `聚焦 Module C` | Targeted reading, not mandatory whole-paper reconstruction. |
| L4 | `Export JSON` | Existing schema-compatible behavior remains available in the full prompt. |

## Candidate Gap / Idea checks

For every idea-oriented case, verify:

1. The observation has a real paper locator or is marked uncertain.
2. The gap is phrased as an unresolved question, not automatically as novelty.
3. The Candidate Idea includes a testable research question or minimal experiment.
4. External novelty is clearly communicated as not checked unless literature search was actually performed; literal `novelty_status` syntax is not required in ordinary prose.
5. A missing experiment alone is not treated as sufficient evidence of publishable novelty.
6. Idea-oriented Triage stops after identifying whether a hook is worth pursuing; it does not automatically perform full Gap Mining, Audit, or novelty search.

## Routing failure classes

Use these labels in evaluation notes:

- `OVERREAD` — analysis depth exceeds user need without justification.
- `UNDERREAD` — insufficient evidence inspected for the requested conclusion.
- `MISROUTE` — wrong goal/lens selected.
- `NO_STOP` — useful answer is followed by unnecessary deep expansion.
- `IDEA_OVERPROMOTION` — Candidate Gap/Idea is presented as established novelty or a strong research direction without required checks.
- `EVIDENCE_BYPASS` — routing is correct but the answer skips necessary source evidence.

## Suggested run record

For every live run record:

```text
case_id:
prompt_version / commit:
model / mode:
date:
expected_depth:
observed_behavior:
relevant_evidence_inspected:
question_answered: yes/no
routing_failure: none | OVERREAD | UNDERREAD | MISROUTE | NO_STOP | IDEA_OVERPROMOTION | EVIDENCE_BYPASS
approx_output_length:
evidence_fidelity_score: optional / when applicable
notes:
```

## Reporting prompt revisions

For a prompt/version comparison, report both:

```text
Evidence fidelity score
+
Routing outcome (pass/fail + failure class)
```

Do not allow a high evidence-fidelity score to hide systematic over-reading, and do not allow concise routing behavior to excuse weak evidence grounding.

For meaningful comparisons, run each routing case multiple times under the same model/mode/date conditions and report all runs rather than selecting the best output.
