# Round 1 evidence map

## 0. Source ledger, reading coverage, and one-sentence verdict

**Sources:** S1 = `paper.pdf`, synthetic primary paper.

**Inspected:** S1 Abstract; Sections 1–8; Tables 1–2. No figures, equations, appendix, or supplement are identified in S1.

**Uninspected:** None.

**Missing/inaccessible:** Exact split counts, encoder identity, validation protocol, batch size, random seed, stopping rule, repeated runs, statistical tests, and detailed compute are **not specified in the paper**.

**Verdict:** [Analyst judgment] TinyRank outperforms StrongBase in one reported run on two small datasets, but the paper overstates the Dataset B gain, contradicts its own ablation for Module C, and does not substantiate broad robustness or compute efficiency.

## 1. Research question and promises

The paper asks whether global routing G plus context gate C improves document classification without high compute (S1, Section 1). It promises consistent 8-point gains, necessity of both modules, broad robustness, cross-domain generalization, and modest compute (S1, Abstract; Sections 1 and 8). The experiments only partially address these promises.

## 2. End-to-end method map

`document → frozen 12-layer encoder → G mean-token router + C token gate → addition → linear classifier → 10-epoch Adam training → macro-F1`

- **G:** [Paper fact] creates a document-level routing vector (S1, Section 3). Removing it lowers Dataset A macro-F1 from 0.78 to 0.76 (S1, Table 2), a small single-run ablation.
- **C:** [Paper fact] gates tokens with a sigmoid (S1, Section 3). Removing it leaves reported Dataset A macro-F1 unchanged at 0.78 (S1, Table 2), so necessity is not demonstrated.
- **Training:** [Unknown] the checkpoint is selected by best test macro-F1; no validation procedure is reported (S1, Section 3), creating leakage/selection-bias risk.

## 3. Innovation-claim map

| Author claim | Internal method | Linked experiment | Current evidence | Internal credibility | External novelty |
|---|---|---|---|---|---|
| Dual-routing architecture | G plus C | S1, Tables 1–2 | Architecture is described, but C adds no measured gain in the only ablation | Weak for necessity | Not checked |
| Consistent 8-point gain | Full model | S1, Table 1 | +8 points on A; +4 on B | Weak; numerically contradicted | Not checked |
| Both modules essential | G and C | S1, Table 2 | G removal: −2 points; C removal: 0 | Weak; C claim contradicted | Not checked |
| Robustness | Full model | S1, Section 6 | One 10% deletion condition on A | Weak outside that condition | Not checked |

## 4. Experiment map

| Item | Reported information | Gap |
|---|---|---|
| Data | A: 120 support messages; B: 90 reviews; 80/20 split; balanced before split (S1, Section 2) | Exact counts and balancing procedure not specified |
| Baselines | SimpleBase, StrongBase (S1, Table 1) | Architecture and tuning not specified |
| Metric | Test macro-F1 | No class-level results or uncertainty |
| Training | 10 epochs, Adam, LR 0.001 (S1, Section 3) | Seed, batch size, validation, stopping rule not specified |
| Runs/statistics | One run per model (S1, Section 4) | No repeats, variation, confidence interval, or test |
| Robustness | 10% token deletion on A (S1, Section 6) | One noise type, level, and dataset |
| Compute | Single GPU (S1, Section 7) | Model, time, memory, parameters, energy, matched baseline not specified |

## 5. Core claim–evidence matrix

| ID | Core claim | Type | Evidence location | What the evidence shows | Support | Boundary/gap |
|---|---|---|---|---|---|---|
| C1 | TinyRank improves by 8 points on both datasets | [Author interpretation] | S1, Abstract; Table 1 | +0.08 on A, +0.04 on B | Weak | Claim is false for B |
| C2 | Both modules are essential | [Author interpretation] | S1, Section 5; Table 2 | Without G: 0.76; without C: 0.78; full: 0.78 | Weak | C has no observed contribution; A only; one run |
| C3 | TinyRank generalizes across domains | [Author interpretation] | S1, Section 4; Table 1 | Separate within-dataset results on two domains | Weak | No cross-domain transfer; tiny samples; one run |
| C4 | TinyRank is broadly robust | [Author interpretation] | S1, Section 6 | Under 10% token deletion on A, 0.71 vs 0.65 | Weak | Supports one corruption condition only |
| C5 | TinyRank is compute-efficient | [Author interpretation] | S1, Section 7 | Training used one unspecified GPU | Cannot judge | No cost measurement or matched comparison |
| C6 | TinyRank exceeds StrongBase in reported runs | [Paper fact] | S1, Table 1 | A: 0.78 vs 0.70; B: 0.78 vs 0.74 | Moderate | Direct result, but one run and test-selected checkpoint |

## 6. Cross-section consistency audit

- **High:** S1 Abstract, Sections 1, 4, and 8 claim an 8-point gain on both datasets; S1 Table 1 shows only 4 points on B. This changes a headline claim.
- **High:** S1 Section 5 says removing either module damages performance; S1 Table 2 shows no change without C. This directly undermines the “both essential” claim.
- **Medium:** Broad robustness language in S1 Abstract/Section 6 exceeds one token-deletion test on A.
- **Medium:** “Generalizes across domains” in S1 Sections 4 and 8 is stronger than separate in-domain evaluation on two datasets.
- **Medium:** “Compute-efficient” in S1 Section 8 lacks a measured efficiency result in S1 Section 7.

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
