# Adaptive Routing Evaluation

PEM v0.2 adds a new behavior that must be tested separately from evidence fidelity: **does the workflow choose an appropriate reading scope for the user's current goal?**

A model can be scientifically careful yet still fail v0.2 by producing a full evidence map when the user only asked whether the paper is worth reading.

## Evaluation dimensions

Score each live run on four routing dimensions before applying the existing evidence-fidelity rubric where relevant.

| Dimension | Pass condition |
|---|---|
| Goal fit | The response addresses the user's actual decision/question rather than a generic paper template. |
| Depth fit | The response uses no more depth than necessary for a reliable answer. |
| Lens discipline | Only relevant analytical capabilities appear; unrelated inventories are omitted. |
| Stop behavior | The response stops after satisfying the current goal and does not automatically continue into deeper analysis. |

A routing failure is recorded even if the extra analysis is factually correct.

## Required live routing matrix

Use a fresh chat for each case. Attach the same `examples/synthetic/paper.pdf` unless another fixture is specified.

| ID | User request | Expected route | Required behavior | Failure examples |
|---|---|---|---|---|
| R1 | “What is this paper about?” | Scan | Short orientation: problem, contribution, paper type; no claim matrix. | Full experiment inventory; deep audit. |
| R2 | “Is this worth reading if I mainly care about robust classification?” | Triage | Fit judgment, useful sections/evidence, what to read next, one next action. | Outputs all datasets/ablations/claims regardless of relevance. |
| R3 | “Explain whether Module C is actually necessary.” | Targeted + Method/Evidence/Critical | Inspect Module C description plus decisive ablation; give bounded answer. | Reconstructs whole paper before answering. |
| R4 | “Does the broadly robust claim hold?” | Targeted -> Audit if needed | Re-open robustness evidence; narrow claim to tested condition. | Gives generic limitation list without checking decisive evidence. |
| R5 | “Can this paper give me a research idea?” | Triage + Gap/Idea, optionally Targeted | Surface Candidate Gap/Idea with uncertainty; identify what must be checked next. | Calls an unverified omission a novel research direction. |
| R6 | “Read this paper deeply.” | Deep | Broad method/experiment/claim/evidence map with provenance and boundaries. | Only gives a short summary. |
| R7 | “Strictly audit the main conclusions.” | Audit | Re-open decisive evidence, seek counterevidence, narrow/withdraw claims. | Merely repeats a Deep response. |
| R8 | “I need to present this paper tomorrow.” | Targeted/Deep + Presentation | Prioritize motivation, method flow, decisive result, limitation, likely questions. | Produces a reviewer-style audit with no presentation prioritization. |
| R9 | “What should I learn before I can understand Section 3?” | Triage/Targeted + Learning | Minimal prerequisite path tied to the section. | Generic textbook syllabus unrelated to the paper. |
| R10 | Upload paper with no further goal, ask “take a look” | Triage | Brief paper fit/value map and suggested reading paths; do not assume Deep. | Automatically executes Round 1. |

## Legacy compatibility matrix

These cases ensure v0.2 does not break v0.1 workflows.

| ID | Trigger | Expected behavior |
|---|---|---|
| L1 | `Round 1` / `第一轮` | Deep evidence map. |
| L2 | `Round 2` / `第二轮` after L1 | Audit with re-inspection rather than paraphrase. |
| L3 | `Focus: Module C` / `聚焦 Module C` | Targeted reading, not mandatory whole-paper reconstruction. |
| L4 | `Export JSON` | Existing schema-compatible behavior remains available. |

## Candidate Gap / Idea checks

For every idea-oriented case, verify:

1. The observation has a real paper locator or is marked uncertain.
2. The gap is phrased as an unresolved question, not automatically as novelty.
3. The Candidate Idea includes a testable research question or minimal experiment.
4. External novelty is explicitly `Not checked` unless literature search was actually performed.
5. A missing experiment alone is not treated as sufficient evidence of publishable novelty.

## Routing failure classes

Use these labels in evaluation notes:

- `OVERREAD` — analysis depth exceeds user need without justification.
- `UNDERREAD` — insufficient evidence inspected for the requested conclusion.
- `MISROUTE` — wrong goal/lens selected.
- `NO_STOP` — useful answer is followed by unnecessary deep expansion.
- `IDEA_OVERPROMOTION` — Candidate Gap/Idea is presented as established novelty or a strong research direction without required checks.
- `EVIDENCE_BYPASS` — routing is correct but the answer skips necessary source evidence.

## Reporting prompt revisions

For a prompt/version comparison, report both:

```text
Evidence fidelity score
+
Routing outcome (pass/fail + failure class)
```

Do not allow a high evidence-fidelity score to hide systematic over-reading, and do not allow concise routing behavior to excuse weak evidence grounding.

For meaningful comparisons, run each routing case multiple times under the same model/mode/date conditions and report all runs rather than selecting the best output.
