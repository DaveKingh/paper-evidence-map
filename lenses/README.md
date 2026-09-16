# Reading Lenses

Lenses are composable analytical capabilities, not user-facing commands. Select only those needed for the current goal, and activate an additional lens only when the Materiality Gate says it could change the current answer.

## Relevance Lens

Answers: How does this paper relate to the user's current question, knowledge need, or research direction? What parts are worth the user's time for that goal?

Always make relevance goal-relative. Do not equate topical similarity or high relevance with deep-read value, the existence of a research gap, or a recommended research direction.

## Contribution Lens

Answers: What problem is addressed, what is proposed, and what changes relative to the paper's stated baseline/context?

Keep external novelty unchecked unless external literature is explicitly searched.

## Method Lens

Reconstructs the requested method or module as input -> operation -> output -> dependency. Inspect equations, diagrams, implementation details, and ablations when relevant. Prefer evidence directly tied to the claimed mechanism.

## Experiment Lens

Explains datasets, splits, baselines, metrics, comparisons, ablations, robustness/generalization tests, and consequential omissions relevant to the user's question.

## Evidence Lens

Maps a claim to the strongest accessible primary evidence and its locator. Records what the evidence actually shows before interpreting it. Evidence priority is claim-dependent: prefer the source object most directly tied to the observation or operation being judged.

External information must remain distinct from paper-internal evidence and cannot repair information the paper did not report.

## Critical Lens

Tests whether the evidence supports the wording and scope of the claim. Look for mismatched comparisons, missing controls, uncertainty, overgeneralization, causal overreach, contradictions, and alternative explanations. Summary rhetoric cannot override conflicting decisive evidence.

## Gap Lens

Turns a paper-internal unresolved issue into a traceable Candidate Gap. Typical categories include method, data, evaluation, baseline, ablation, generalization, evidence, assumption, and deployment gaps.

Keep three dimensions separate when structured detail is needed:

- `origin`: explicit or inferred;
- `gap_status`: candidate / supported / contradicted / unresolved;
- `novelty_status`: unchecked / partially_checked / no_close_prior_found / contradicted / unclear.

For an inferred gap preserve `Observation + Evidence refs + Reasoning chain + Alternative explanations + Verification needed`. A missing experiment is not automatically a publishable gap, and internal support is not the same as external novelty.

## Idea Lens

Transforms a Candidate Gap into a Candidate Idea using:

`observation -> gap -> research question -> hypothesis -> minimal experiment -> possible contribution -> risks`

Promote a Candidate Idea to a stronger Research Idea only after enough internal gap support and the novelty/feasibility checks required by the intended claim. “No close prior found” within a documented search scope is not proof of absence.

## Learning Lens

Identifies prerequisite concepts needed to understand the user's selected part of the paper. Prefer a minimal learning path over a generic prerequisite list.

## Presentation Lens

Selects the minimum content needed to explain the paper to a target audience: motivation, core idea, method flow, decisive evidence, limitations, and likely questions. It does not require a full evidence audit unless the presentation goal demands one.
