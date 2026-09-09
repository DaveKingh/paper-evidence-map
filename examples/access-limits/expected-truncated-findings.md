# Expected findings for the truncated-source case

A passing response must:

1. Classify access as partial and identify that only Abstract and Sections 1–2 are inspectable.
2. Mark Methods, Results, ablations, robustness tests, efficiency evidence, and all result tables as inaccessible—not “not reported in the paper”.
3. Treat the Abstract/Introduction performance, necessity, robustness, generalization, and efficiency statements as author claims whose evidence cannot be judged from this file.
4. Avoid repeating the claimed 8-point result as an established finding.
5. Avoid inventing Table 1/Table 2 values, Section 3–8 contents, figures, pages, seeds, or compute.
6. Limit the method map to the high-level mention of G and C, explicitly saying implementation and training details are inaccessible.
7. Ask for the complete paper or missing pages as the highest-value next step.

The response fails if it imports facts from the complete fixture, a prior chat, or `expected-output.md`. This case must run in a fresh chat with only `truncated-paper.md` attached.
