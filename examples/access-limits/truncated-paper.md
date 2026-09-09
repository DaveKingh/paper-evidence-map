# TinyRank: Compact Document Classification with Dual Routing

> Synthetic truncated export. Only the material below is available; the file ends before Methods and Results.

## Abstract

We introduce TinyRank, a compact classifier with a global router (G) and a context gate (C). TinyRank improves macro-F1 by 8 percentage points over StrongBase on both evaluated datasets. Both proposed modules are essential to the gain. TinyRank is robust to input noise and generalizes across domains while using modest compute.

## 1. Introduction

Document classifiers often lose global topic information or overfit local token patterns. We ask whether combining a global routing module with a local context gate improves classification accuracy without high computational cost.

Our contributions are: (1) a dual-routing architecture combining G and C; (2) consistent 8-point improvements on two domains; (3) evidence that both modules are necessary; and (4) robustness to noisy input.

## 2. Data

Dataset A contains 120 labeled technical-support messages. Dataset B contains 90 labeled product reviews. We use an 80/20 train/test split for each dataset. Labels are balanced before splitting. No additional data is used.

**Truncation notice:** The export ends here. Sections 3–8 and all result tables are unavailable.
