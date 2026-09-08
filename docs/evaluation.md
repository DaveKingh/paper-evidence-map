# Evaluation

Evaluate responses on evidence fidelity, not eloquence. Use the synthetic paper first, then add domain-specific papers whose decisive findings you can verify.

## 100-point manual rubric

| Dimension | Points | Full-credit behavior |
|---|---:|---|
| Coverage honesty | 10 | States what was and was not accessible; does not falsely claim full coverage. |
| Claim separation | 15 | Consistently separates paper facts, author interpretations, analyst judgments, and unknowns. |
| Evidence localization | 20 | Every major claim has a valid section/table/figure/appendix locator. |
| Evidence fidelity | 20 | Describes what the cited evidence actually shows without numerical or directional errors. |
| Boundary control | 15 | Narrows causality, generality, robustness, stability, and novelty to tested scope. |
| Missing information | 10 | Surfaces consequential unreported details without inventing defaults. |
| Counterevidence | 10 | Finds the strongest inconsistency, negative result, or alternative explanation. |

Interpretation: 90–100 excellent; 75–89 useful with review; 60–74 incomplete; below 60 unreliable for decision support.

## Synthetic-paper required findings

Use [`examples/synthetic/expected-findings.md`](../examples/synthetic/expected-findings.md). Score each required finding as:

- 2: found, correctly located, and bounded;
- 1: found but vague, mislocated, or insufficiently bounded;
- 0: missed or contradicted.

## Structural smoke test

```bash
python scripts/validate.py --response response.md
```

This checks headings, locators, support labels, uncertainty markers, and claim-type labels. It deliberately does not call an LLM and cannot judge substantive truth.

## Comparing prompt revisions

Run the same paper and user trigger at least three times per prompt version. Keep the chat conditions comparable. Record:

- rubric total and per-dimension scores;
- required findings caught;
- fabricated locators;
- completion time and manual review time;
- model/mode and date, because product behavior changes.

Do not publish a single best run as representative. Report the number of runs and failures.

