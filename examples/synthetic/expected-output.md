# Round 1 evidence map

## 0. Reading coverage and one-sentence verdict

**Inspected:** Abstract; Sections 1–8; Tables 1–2. No figures, equations, appendix, or supplement are present in the supplied document.

**Missing/inaccessible:** Exact split counts, encoder identity, validation protocol, batch size, random seed, stopping rule, repeated runs, statistical tests, and detailed compute are **not specified in the paper**.

**Verdict:** [Analyst judgment] TinyRank outperforms StrongBase in one reported run on two small datasets, but the paper overstates the Dataset B gain, contradicts its own ablation for Module C, and does not substantiate broad robustness or compute efficiency.

## 1. Research question and promises

The paper asks whether global routing G plus context gate C improves document classification without high compute (Section 1). It promises consistent 8-point gains, necessity of both modules, broad robustness, cross-domain generalization, and modest compute (Abstract; Sections 1 and 8). The experiments only partially address these promises.

## 2. End-to-end method map

`document → frozen 12-layer encoder → G mean-token router + C token gate → addition → linear classifier → 10-epoch Adam training → macro-F1`

- **G:** [Paper fact] creates a document-level routing vector (Section 3). Removing it lowers Dataset A macro-F1 from 0.78 to 0.76 (Table 2), a small single-run ablation.
- **C:** [Paper fact] gates tokens with a sigmoid (Section 3). Removing it leaves reported Dataset A macro-F1 unchanged at 0.78 (Table 2), so necessity is not demonstrated.
- **Training:** [Unknown] the checkpoint is selected by best test macro-F1; no validation procedure is reported (Section 3), creating leakage/selection-bias risk.

## 3. Innovation-claim map

| Author claim | Internal method | Linked experiment | Current evidence | Internal credibility | External novelty |
|---|---|---|---|---|---|
| Dual-routing architecture | G plus C | Tables 1–2 | Architecture is described, but C adds no measured gain in the only ablation | Weak for necessity | Not checked |
| Consistent 8-point gain | Full model | Table 1 | +8 points on A; +4 on B | Weak; numerically contradicted | Not checked |
| Both modules essential | G and C | Table 2 | G removal: −2 points; C removal: 0 | Weak; C claim contradicted | Not checked |
| Robustness | Full model | Section 6 | One 10% deletion condition on A | Weak outside that condition | Not checked |

## 4. Experiment map

| Item | Reported information | Gap |
|---|---|---|
| Data | A: 120 support messages; B: 90 reviews; 80/20 split; balanced before split (Section 2) | Exact counts and balancing procedure not specified |
| Baselines | SimpleBase, StrongBase (Table 1) | Architecture and tuning not specified |
| Metric | Test macro-F1 | No class-level results or uncertainty |
| Training | 10 epochs, Adam, LR 0.001 (Section 3) | Seed, batch size, validation, stopping rule not specified |
| Runs/statistics | One run per model (Section 4) | No repeats, variation, confidence interval, or test |
| Robustness | 10% token deletion on A (Section 6) | One noise type, level, and dataset |
| Compute | Single GPU (Section 7) | Model, time, memory, parameters, energy, matched baseline not specified |

## 5. Core claim–evidence matrix

| ID | Core claim | Type | Evidence location | What the evidence shows | Support | Boundary/gap |
|---|---|---|---|---|---|---|
| C1 | TinyRank improves by 8 points on both datasets | [Author interpretation] | Abstract; Table 1 | +0.08 on A, +0.04 on B | Weak | Claim is false for B |
| C2 | Both modules are essential | [Author interpretation] | Section 5; Table 2 | Without G: 0.76; without C: 0.78; full: 0.78 | Weak | C has no observed contribution; A only; one run |
| C3 | TinyRank generalizes across domains | [Author interpretation] | Section 4; Table 1 | Separate within-dataset results on two domains | Weak | No cross-domain transfer; tiny samples; one run |
| C4 | TinyRank is broadly robust | [Author interpretation] | Section 6 | Under 10% token deletion on A, 0.71 vs 0.65 | Weak | Supports one corruption condition only |
| C5 | TinyRank is compute-efficient | [Author interpretation] | Section 7 | Training used one unspecified GPU | Cannot judge | No cost measurement or matched comparison |
| C6 | TinyRank exceeds StrongBase in reported runs | [Paper fact] | Table 1 | A: 0.78 vs 0.70; B: 0.78 vs 0.74 | Moderate | Direct result, but one run and test-selected checkpoint |

## 6. Cross-section consistency audit

- **High:** Abstract, Section 1, Section 4, and Section 8 claim an 8-point gain on both datasets; Table 1 shows only 4 points on B. This changes a headline claim.
- **High:** Section 5 says removing either module damages performance; Table 2 shows no change without C. This directly undermines the “both essential” claim.
- **Medium:** Broad robustness language in Abstract/Section 6 exceeds one token-deletion test on A.
- **Medium:** “Generalizes across domains” in Sections 4 and 8 is stronger than separate in-domain evaluation on two datasets.
- **Medium:** “Compute-efficient” in Section 8 lacks a measured efficiency result in Section 7.

## 7. Unknowns and risk register

- **Not specified:** seed, batch size, encoder identity, exact split counts, validation protocol, baseline details, repeated-run variance, statistical tests, compute measurements.
- **Inaccessible:** none beyond material absent from the supplied document.
- **Requires external sources:** whether the dual-routing architecture is novel.
- **Requires replication:** stability of gains; effect of C; robustness across corruptions and Dataset B.

## 8. Round 2 priorities

1. Recheck Table 1 against every 8-point claim; impact is high and contradiction is direct.
2. Recheck Table 2 and surrounding prose for Module C necessity.
3. Audit test-set checkpoint selection in Section 3 and quantify its possible optimism.
4. Narrow the robustness and generalization conclusions to actually tested conditions.
5. Determine what evidence would be required for compute efficiency.

