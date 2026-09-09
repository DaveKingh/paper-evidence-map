# TinyRank: Compact Document Classification with Dual Routing

> Synthetic evaluation fixture. This is not a real paper and contains deliberate inconsistencies and missing information.

## Abstract

We introduce TinyRank, a compact classifier with a global router (G) and a context gate (C). TinyRank improves macro-F1 by 8 percentage points over StrongBase on both evaluated datasets. Both proposed modules are essential to the gain. TinyRank is robust to input noise and generalizes across domains while using modest compute.

## 1. Introduction

Document classifiers often lose global topic information or overfit local token patterns. We ask whether combining a global routing module with a local context gate improves classification accuracy without high computational cost.

Our contributions are: (1) a dual-routing architecture combining G and C; (2) consistent 8-point improvements on two domains; (3) evidence that both modules are necessary; and (4) robustness to noisy input.

## 2. Data

Dataset A contains 120 labeled technical-support messages. Dataset B contains 90 labeled product reviews. We use an 80/20 train/test split for each dataset. Labels are balanced before splitting. No additional data is used.

## 3. Method

TinyRank encodes each document with a frozen 12-layer encoder. Module G computes a document-level routing vector from the mean token representation. Module C applies a sigmoid gate to each token. Their outputs are added and passed to a linear classifier.

The model is trained for 10 epochs with Adam and learning rate 0.001. We select the checkpoint with the best test-set macro-F1. Batch size, random seed, validation procedure, and stopping criterion are not reported.

## 4. Main results

Table 1 reports one run for each model. TinyRank performs best on both datasets.

**Table 1. Test macro-F1.**

| Model | Dataset A | Dataset B |
|---|---:|---:|
| SimpleBase | 0.66 | 0.70 |
| StrongBase | 0.70 | 0.74 |
| TinyRank | **0.78** | **0.78** |

These results confirm a consistent 8-point improvement and demonstrate that the architecture generalizes across domains.

## 5. Ablation

We ablate each module on Dataset A only.

**Table 2. Ablation on Dataset A.**

| Variant | Macro-F1 |
|---|---:|
| TinyRank | 0.78 |
| without G | 0.76 |
| without C | 0.78 |

Removing either component damages performance, showing that G and C are both essential.

## 6. Noise experiment

For Dataset A, we randomly delete 10% of tokens from each test message. TinyRank scores 0.71 macro-F1 and StrongBase scores 0.65. No other noise level or dataset is evaluated.

This confirms that TinyRank is broadly robust to noisy real-world text.

## 7. Efficiency

Training completed on a single GPU. We do not report the GPU model, wall-clock time, memory, parameter count, energy use, or a compute-matched baseline.

## 8. Conclusion

TinyRank delivers consistent 8-point gains across domains. Its two essential modules provide robust and compute-efficient document classification. Future work will evaluate more languages and larger datasets.
