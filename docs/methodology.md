# Methodology

## Core object: the claim–evidence–boundary triple

For every consequential claim, the workflow asks three questions:

1. **Claim** — What exactly is being asserted, and by whom?
2. **Evidence** — What result or method detail bears on it, and where is it?
3. **Boundary** — What is the strongest narrower statement that the evidence can defend?

The third question prevents a common failure: correctly finding a result but repeating a broader conclusion than that result warrants.

## Why two rounds

Round 1 optimizes coverage. It reconstructs the paper and exposes missing links. Round 2 optimizes falsification: it re-opens the most important evidence, seeks alternative explanations, and revises the claim rather than merely adding more prose.

The rounds should be separate because a single long answer can give the appearance of depth without actually re-checking decisive evidence.

## Evidence labels

| Label | Meaning | Example |
|---|---|---|
| Paper fact | Explicit and locatable report | “Table 2 reports 0.78 macro-F1.” |
| Author interpretation | Explanation or generalization made by authors | “The authors attribute the gain to Module G.” |
| Analyst judgment | Inference from internal evidence | “The ablation weakens the necessity claim.” |
| Unknown | Missing or inaccessible | “The number of random seeds is not specified.” |

## Support levels

- **Strong:** direct, well-matched evidence with appropriate comparisons and uncertainty reporting supports the stated scope.
- **Moderate:** relevant evidence exists but a material limitation remains.
- **Weak:** evidence is indirect, narrow, under-controlled, or inconsistent with the claim's breadth.
- **Cannot judge:** decisive information is missing or inaccessible.

These labels are local to a claim. They are not an overall quality ranking.

## Threat model

The workflow explicitly addresses:

- abstract and conclusion overstatement;
- result/interpretation conflation;
- unreported details filled in from convention;
- one-condition evidence generalized broadly;
- missing ablations for “essential” modules;
- inconsistent values across text and tables;
- document-embedded prompt injection;
- false claims of full-document coverage.

It does not solve fabricated source data, sophisticated statistical errors, inaccessible content, or field-wide novelty without external evidence.

