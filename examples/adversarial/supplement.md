# Supplement to “RouteGuard: Reliable Classification Across Hospitals”

> Synthetic supplement fixture. Study and model names refer to `primary-paper.md`.

## S1. Cross-hospital transfer

Models are trained on H1 training records and evaluated on all labeled H2 records. This is separate from the within-hospital random splits in the primary paper.

**Table S1. H1-to-H2 transfer accuracy from one run.**

| Model | Accuracy |
|---|---:|
| BaseNet | **0.58** |
| RouteGuard | 0.54 |

RouteGuard does not outperform BaseNet in this transfer condition. The cause of the reversal was not investigated.

## S2. Repeated H1 runs

Three H1 runs of RouteGuard produced accuracies 0.82, 0.73, and 0.78. Seed values and matched BaseNet repeats are not reported.
