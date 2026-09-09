# Expected findings for the synthetic paper

This is a content-level answer key, not an exact response template. Use `paper.pdf` for the real attachment test; `paper.md` is its human-reviewable source. A good `Round 1` should catch all required findings and preserve their scope.

## Required findings

1. **The “8 points on both datasets” claim is false.** Table 1 shows +0.08 on Dataset A (0.78 vs 0.70) but only +0.04 on Dataset B (0.78 vs 0.74). This conflicts with the Abstract, Introduction contribution 2, Results prose, and Conclusion.
2. **Module C is not shown to be essential.** Table 2 reports 0.78 both for full TinyRank and “without C”. The statement below Table 2 says removing either component damages performance, which directly conflicts with the table.
3. **The generalization claim is too broad.** Results cover two small datasets and one run per model. Cross-domain transfer was not tested; training and testing occurred within each dataset.
4. **The robustness claim is too broad.** Section 6 tests one token-deletion level on Dataset A only. It does support better performance than StrongBase under that one condition, but not broad real-world robustness.
5. **The compute-efficiency claim is unsupported.** Section 7 reports only “a single GPU” and omits hardware, time, memory, parameters, energy, and compute-matched comparison.
6. **Checkpoint selection risks test-set leakage.** Section 3 says the best test-set macro-F1 checkpoint is selected. There is no reported validation procedure.
7. **Uncertainty and reproducibility are weak.** Results are one run; seed, batch size, validation procedure, stopping rule, statistical tests, and variation are not reported.
8. **Ablation coverage is narrow.** Ablations are on Dataset A only, so they cannot establish module necessity on Dataset B.

## Bonus findings

- Dataset sizes imply test sets of about 24 and 18 under an exact 80/20 split, but rounding and realized split counts are not reported; do not invent them as facts.
- Label balancing “before splitting” is ambiguous and could involve resampling or leakage, but the method is not described.
- “No additional data” sits uneasily with an unspecified frozen 12-layer encoder if the claim is meant to cover pretraining; the paper does not identify the encoder or clarify this boundary.
- Macro-F1 alone may not establish real-world utility; class-level performance is absent.

## Failure conditions

A response should not receive a high score if it:

- repeats the 8-point claim for Dataset B;
- describes C as validated or essential;
- invents seeds, p-values, test counts, GPU type, or validation data;
- calls the method compute-efficient as a fact;
- says the paper tested cross-domain transfer;
- claims to have checked figures or appendices that do not exist.
