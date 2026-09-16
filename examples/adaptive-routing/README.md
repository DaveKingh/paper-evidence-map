# Adaptive Routing Fixture

This fixture tests **routing behavior**, not only factual correctness. Use the same paper across multiple fresh chats and vary only the user's goal.

Recommended source: `../synthetic/paper.pdf`.

The purpose is to verify that Paper Evidence Map chooses the minimum sufficient reading depth, does not over-read, and does not promote preliminary research ideas too strongly.

## Cases

| ID | User request | Expected depth | Required behavior | Forbidden behavior |
|---|---|---|---|---|
| R1 | `What is this paper about?` | Scan | Identify the task and core contribution concisely | Full experiment inventory or claim matrix |
| R2 | `Is this paper worth reading if I care about trustworthy model evaluation?` | Triage | Judge fit; identify the most relevant sections/tables and next reading step | Full Deep review by default |
| R3 | `Is Module C actually necessary?` | Targeted | Inspect the ablation evidence and give a bounded conclusion | Reconstruct unrelated sections of the whole paper |
| R4 | `Does the paper support its broad robustness claim?` | Targeted/Audit | Inspect robustness evidence; distinguish tested condition from broad claim | Accept broad robustness without boundary control |
| R5 | `Can this paper give me a research idea?` | Triage/Targeted | Surface a traceable Candidate Gap/Idea if justified | Claim verified novelty from the paper alone |
| R6 | `Read this paper deeply.` | Deep | Produce broad method/experiment/claim–evidence coverage | Stop at a superficial summary |
| R7 | `Strictly audit the most important conclusions.` | Audit | Re-open decisive evidence, seek alternatives, narrow claims | Merely restate a prior Deep pass |

## Failure classes

- `MISROUTE` — wrong depth/lenses for the user's goal.
- `OVERREAD` — substantially more analysis than the current goal requires.
- `UNDERREAD` — insufficient evidence inspection for the requested judgment.
- `NO_STOP` — continues into unrelated analysis after the current goal is satisfied.
- `EVIDENCE_BYPASS` — reaches a substantive judgment without inspecting decisive evidence.
- `IDEA_OVERPROMOTION` — presents a Candidate Gap/Idea as established novelty or a validated research direction without the necessary checks.

## How to run

Run every case in a fresh chat with the same prompt version, model/mode, and source paper. Save the raw outputs. Do not reuse a prior answer as evidence.

For each case record:

- expected depth;
- observed depth (inferred from behavior; the model does not need to print the internal label);
- relevant source objects inspected;
- whether the user's question was answered;
- whether any failure class occurred;
- approximate output length;
- notes on unnecessary sections or missing checks.

The goal is not to minimize token count at all costs. The goal is **minimum sufficient evidence work**.
