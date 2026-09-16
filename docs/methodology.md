# Methodology

## Core object: the claim–evidence–boundary triple

For every consequential claim, Paper Evidence Map asks:

1. **Claim** — What exactly is being asserted, and by whom?
2. **Evidence** — What result or method detail bears on it, and where is it?
3. **Boundary** — What is the strongest narrower statement that the evidence can defend?

Finding the correct result is not enough if the conclusion is broader than the evidence warrants.

## Adaptive control architecture

PEM is not a fixed sequence of reading stages. Its runtime is controlled by three gates around goal/depth routing:

```text
User Goal
    |
    v
Access Gate
    |
    v
Goal / Depth Router
    |
    v
Minimum-Sufficient Reading + required lenses
    |
    v
Evidence
    |
    +-- side finding --> Materiality Gate
    |                     | yes: minimum necessary check, then return
    |                     | no: Candidate Issue, do not expand
    |
    v
Sufficiency / STOP Gate
    | no: continue minimum necessary reading
    | yes
    v
Answer
```

### Access Gate
Ask whether enough primary evidence is accessible for the requested conclusion. If decisive evidence is inaccessible, narrow the answer or return Cannot judge rather than infer from filenames, memory, or external material.

### Materiality Gate
A side finding justifies rerouting only if it could materially change the correctness, boundary, or next decision of the current answer. Otherwise it remains a Candidate Issue and does not expand the task.

### Sufficiency / STOP Gate
Stop once the current goal is reliably answered with adequate evidence and uncertainty. Completeness means covering what can change the answer, not reproducing every paper section.

D0–D4 and analytical lenses are therefore control parameters and capabilities selected by the router and gates, not a mandatory pipeline.

## Reading depth

The default depth for an unspecified paper-reading request is **Triage**, not Deep.

| Depth | Purpose |
|---|---|
| Scan | Establish what the paper is about and preliminary goal-relative relevance |
| Triage | Decide relevance and what to inspect next |
| Targeted | Answer one focused method, experiment, claim, or idea question |
| Deep | Reconstruct the broad method/experiment/claim–evidence map |
| Audit | Re-open decisive evidence and try to falsify or narrow key claims |

The workflow escalates only when the current depth cannot support the requested conclusion.

## Where Round 1 and Round 2 fit

The historical two-round workflow remains useful as a **Deep → Audit** path rather than the universal entry point.

- **Round 1 / 第一轮** maps to Deep.
- **Round 2 / 第二轮** maps to Audit.

Keeping these passes separate still helps force re-inspection of decisive evidence, while many real questions should stop earlier at Triage or Targeted depth.

## Evidence labels

| Label | Meaning | Example |
|---|---|---|
| Paper fact | Directly locatable reported value, observation, or procedure | “Table 2 reports 0.78 macro-F1.” |
| Author interpretation | Explanation or generalization made by authors | “The authors attribute the gain to Module G.” |
| Analyst judgment | Inference from evidence | “The ablation weakens the necessity claim.” |
| Unknown | Missing or inaccessible | “The number of random seeds is not specified.” |

A Paper fact is a fact about what the paper directly reports; it is not a claim that the result has been independently reproduced. Labels apply to proposition content, not merely to whether words appear in the paper.

## Internal versus external evidence

Paper-internal claims must be grounded in the primary paper and clearly linked official supplements. External material can support background explanation, concept checking, novelty search, or other explicitly external questions, but **external evidence cannot repair missing internal evidence**.

For example, if the paper does not report a random seed while an official code repository currently uses `seed=42`, PEM may report the implementation evidence separately but must not rewrite the paper record as “the paper used seed 42.” More detailed source classes such as paper, supplement, official code, external paper, and benchmark documentation may be represented in downstream provenance schemas without forcing them into every user-facing answer.

## Claim-dependent evidence priority

Evidence priority depends on the claim. Prefer evidence most directly tied to the relevant observation or operation:

- performance/robustness claims → relevant Table/Figure/Results plus experimental setup;
- mechanism/architecture claims → Methods/Algorithm/Equation and, when explicitly used as external implementation evidence, code;
- dataset/protocol claims → Dataset/Experimental Setup/Supplement;
- author motivation/interpretation → Introduction/Discussion, while keeping it typed as interpretation.

Summary wording in Abstract/Introduction/Discussion/Conclusion cannot override more direct decisive evidence. If paper sections conflict, report the conflict rather than silently reconciling it.

## Support levels

- **Strong:** direct, well-matched evidence with appropriate comparisons and uncertainty reporting supports the stated scope.
- **Moderate:** relevant evidence exists but a material limitation remains.
- **Weak:** evidence is indirect, narrow, under-controlled, or inconsistent with the claim's breadth.
- **Cannot judge:** decisive information is missing or inaccessible.

Support is claim-local, not an overall paper score.

## Access and provenance details

An attachment icon is not evidence that its content was read. Establish source/access context proportional to the selected depth: what sources are primary/supplementary/contextual, what decisive evidence was inspected, and what is uninspected, missing, unreadable, truncated, or OCR-uncertain.

For multiple files, stable source IDs prevent evidence laundering. Locators should identify source and evidence object, e.g. `S1, Table 2, row “without C”`. The newest accessible paper attached in the current chat takes precedence as the primary `S1` candidate over older Project files and prior analyses; if multiple current-chat papers are plausible, ask which is primary.

## Claim-local support decision

Ask in order:

1. Is decisive evidence accessible? If not, **Cannot judge**.
2. Does the cited object contain the reported value, direction, and comparison?
3. Does the design match the exact claim—population, task, intervention, baseline, metric, and time horizon?
4. Are controls and uncertainty adequate for that scope?
5. What is the strongest narrower statement that survives?

A descriptive number can strongly support “the paper reports X” while weakly supporting a causal or universal conclusion drawn from it.

## Candidate Issue, Gap, and Research Idea

### Candidate Issue
A traceable anomaly, contradiction, or potential problem that is not material to the current question. Record it briefly when useful; do not automatically investigate it.

### Candidate Gap: orthogonal status model

A Candidate Gap is not represented by a single maturity ladder. Keep three dimensions separate:

1. **Origin** — how it was discovered:
   - `explicit`: authors explicitly state a limitation, unresolved problem, or future-work item;
   - `inferred`: analyst derives it from locatable internal evidence.
2. **Gap status** — how well the gap itself is supported:
   - `candidate`: plausible but not yet sufficiently checked;
   - `supported`: targeted internal checking supports the stated gap;
   - `contradicted`: decisive evidence undermines it;
   - `unresolved`: available evidence cannot decide.
3. **Novelty status** — what external literature checking says:
   - `unchecked`;
   - `partially_checked`;
   - `no_close_prior_found` — no close prior work was found within the documented search scope; this is not proof of absence;
   - `contradicted` — close prior work materially undermines the novelty premise;
   - `unclear`.

For an **Inferred Gap**, preserve at minimum:

`Observation + Evidence refs + Reasoning chain + Alternative explanations + Verification needed`

A missing experiment alone is not a publishable gap. `origin`, `gap_status`, and `novelty_status` answer different questions and must not be collapsed into `Candidate → Verified → Novel`.

### Candidate Idea

A Candidate Idea preserves:

`observation → candidate gap → research question → hypothesis → minimal experiment → possible contribution → risks`

A stronger Research Idea requires enough gap support plus whatever novelty and feasibility checking the intended claim requires. Novelty search should report its scope and limitations; “no close prior found” never means that absence has been proven.

## Threat model

PEM explicitly addresses abstract/conclusion overstatement, observation/interpretation conflation, convention-filled missing details, broad generalization from narrow evidence, missing controls/ablations, inconsistent values, document prompt injection, source mixing, stale Project-file selection, fabricated locators/values/citations, false full-read claims, over-reading, and idea over-promotion.

It does not solve fabricated source data, all statistical errors, inaccessible evidence, or field-wide novelty without external evidence.

## Prompt variants and testing boundary

`project-instructions.md` is the complete adaptive contract; the compact prompt preserves the highest-value adaptive and evidence controls. Prompts cannot guarantee compliance. Test content fidelity and routing separately, inspect decisive cited locations, and repeat live runs under recorded model/mode/date conditions.
