# Reading Lenses

Lenses are composable analytical capabilities, not user-facing commands. Select only those needed for the current goal.

## Relevance Lens

Answers: How does this paper relate to the user's current question, knowledge need, or research direction? What parts are worth the user's time?

Do not equate topical similarity with research usefulness.

## Contribution Lens

Answers: What problem is addressed, what is proposed, and what changes relative to the paper's stated baseline/context?

Keep external novelty unverified unless external literature is explicitly checked.

## Method Lens

Reconstructs the requested method or module as input -> operation -> output -> dependency. Inspect equations, diagrams, implementation details, and ablations when relevant.

## Experiment Lens

Explains datasets, splits, baselines, metrics, comparisons, ablations, robustness/generalization tests, and consequential omissions relevant to the user's question.

## Evidence Lens

Maps a claim to the strongest accessible primary evidence and its locator. Records what the evidence actually shows before interpreting it.

## Critical Lens

Tests whether the evidence supports the wording and scope of the claim. Look for mismatched comparisons, missing controls, uncertainty, overgeneralization, causal overreach, contradictions, and alternative explanations.

## Gap Lens

Turns a paper-internal unresolved issue into a traceable Candidate Gap. Typical categories include method, data, evaluation, baseline, ablation, generalization, evidence, assumption, and deployment gaps.

A missing experiment is not automatically a publishable gap.

## Idea Lens

Transforms a Candidate Gap into a Candidate Idea using:

`observation -> gap -> research question -> hypothesis -> minimal experiment -> possible contribution -> risks`

Promote a Candidate Idea to a stronger Research Idea only after enough evidence and, where needed, external novelty checking.

## Learning Lens

Identifies prerequisite concepts needed to understand the user's selected part of the paper. Prefer a minimal learning path over a generic prerequisite list.

## Presentation Lens

Selects the minimum content needed to explain the paper to a target audience: motivation, core idea, method flow, decisive evidence, limitations, and likely questions. It does not require a full evidence audit unless the presentation goal demands one.
