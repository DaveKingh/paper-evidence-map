# Paper Evidence Map

> **Don't just summarize a paper. Read what matters, then map what it actually proves.**

[简体中文](README.zh-CN.md) · [Adaptive reading](docs/adaptive-reading.md) · [Quickstart](docs/quickstart.md) · [Synthetic challenge](#try-the-reproducible-challenge) · [Method](docs/methodology.md) · [Evaluation](docs/evaluation.md)

Paper Evidence Map (PEM) is an adaptive, evidence-first workflow for reading one research paper at a time. It does **not** assume that every paper deserves a full deep read. It first infers what you need from the paper, chooses the minimum useful reading depth, and then connects important claims to methods, experiments, figures, tables, limitations, and defensible boundaries.

The core idea is simple:

```text
user goal
   ↓
reading depth
   ↓
relevant paper evidence
   ↓
claim → evidence → defensible boundary
   ↓
optional gap / idea formation
```

PEM is designed for ordinary ChatGPT use, including Projects. It is model-neutral in design and does not require an API key for the primary workflow.

## Why adaptive reading

A researcher often starts with questions like:

- Is this paper worth reading for my current problem?
- Which section matters most to me?
- I only want to understand this module—how does it work?
- Does this table really support the author's claim?
- Is there a research idea hidden in this design choice?
- I need to present this paper tomorrow—what should I focus on?

A fixed full-paper template creates unnecessary work and output. PEM instead uses five reading depths:

| Depth | Use |
|---|---|
| **Scan** | What is this paper about? |
| **Triage** | Is it relevant / worth reading / useful for ideas? |
| **Targeted** | Answer one method, experiment, figure, table, or claim question |
| **Deep** | Build a broad evidence map |
| **Audit** | Skeptically re-check consequential claims |

**Triage is the default**, not Deep.

## Three core rules

1. **No user need → no analysis.**
2. **No evidence → no strong claim.**
3. **No verified gap → no strong research idea.**

This means PEM should stop when the current question is answered instead of automatically generating every possible section.

## Setup once per Project

If you only want to use the workflow, you do not need to clone this repository.

1. Copy the [full English Project instructions](prompts/en/project-instructions.md) or the [Chinese version](prompts/zh-CN/project-instructions.md).
2. Paste them into a ChatGPT Project's instructions.
3. Upload a paper and ask your actual question naturally.

Examples:

```text
Is this paper worth reading for my current research direction?
```

```text
I mainly care about scenario mining. Which parts of this paper should I read first?
```

```text
Why did the authors fine-tune BLIP2 instead of the strongest zero-shot model?
```

```text
Does Table 4 really support the paper's robustness claim?
```

```text
Can this paper give me any candidate research ideas?
```

You no longer need to start every paper with `Round 1`.

Legacy shortcuts still work:

| Send | Result |
|---|---|
| `Round 1` / `第一轮` | Deep evidence map |
| `Round 2` / `第二轮` | Skeptical audit |
| `Focus: <question>` | Targeted reading |
| `Reading status` | Coverage only |
| `Export JSON` | Structured evidence-map export |

## What PEM preserves from the original workflow

Adaptive routing changes **when** analysis is performed, not the evidence standard.

PEM still requires:

- source and access provenance;
- paper fact / author interpretation / analyst judgment / unknown separation;
- precise evidence locators where possible;
- claim-local support strength;
- explicit unknowns and inaccessible content;
- claim boundary control;
- counterevidence and alternative explanations in audit mode;
- no field-wide novelty claim from one paper alone.

The core scientific object remains:

```text
Claim → Evidence → Boundary
```

See [Methodology](docs/methodology.md).

## Candidate gaps and research ideas

PEM may surface interesting anomalies before a full audit, but it does not automatically call them research gaps.

```text
observation
  ↓
Candidate Gap
  ↓
targeted evidence check
  ↓
Candidate Idea
  ↓
novelty / feasibility checks when needed
  ↓
Research Idea
```

A missing experiment alone is **not** automatically a publishable gap.

## See the difference on a checkable example

The included synthetic paper deliberately makes claims that its own tables do not support:

| What the paper says | What its primary evidence says | Defensible reading |
|---|---|---|
| “8-point gains on both datasets” | Table 1: +8 points on A, **+4** on B | The headline is overstated for B |
| “Both modules are essential” | Table 2: removing C changes **0.78 → 0.78** | Necessity of C is not demonstrated |
| “Broadly robust” | One corruption level on one dataset | Evidence supports only that tested condition |

Inspect the [upload-ready PDF](examples/synthetic/paper.pdf), [Markdown source](examples/synthetic/paper.md), [expected findings](examples/synthetic/expected-findings.md), [reference evidence map](examples/synthetic/expected-output.md), and [reference JSON](examples/synthetic/expected-output.json).

## Try the reproducible challenge

### Evidence fidelity test

Upload [`examples/synthetic/paper.pdf`](examples/synthetic/paper.pdf) and send:

```text
Round 1
```

Then compare the result against the [required findings](examples/synthetic/expected-findings.md) and [evaluation rubric](docs/evaluation.md).

### Adaptive routing tests

Use a fresh chat for each question with the same synthetic paper:

```text
Is this paper worth reading if I mainly care about robust classification?
```

Expected: **Triage**, not a full evidence map.

```text
Explain whether Module C is actually necessary.
```

Expected: **Targeted + Evidence/Critical**, focused on the relevant ablation.

```text
Can this paper give me a research idea?
```

Expected: candidate gap/idea language, not an unqualified novelty claim.

The point of PEM v0.2 is therefore testable: it should not only read carefully; it should also choose **how much reading is appropriate**.

## Architecture

PEM v0.2 uses a thin, manifest-driven skill structure inspired by progressive-loading systems:

```text
SKILL.md
  ↓
manifest.yaml
  ├── always-load core
  ├── goal router
  ├── depth router
  ├── on-demand lenses
  └── on-demand references
```

See [design reference audit](docs/design-reference-audit.md) for what PEM borrows from Nature Skills and Academic Research Suite, and what it intentionally keeps different.

## Where it fits

| Need | Fit |
|---|---|
| Decide whether one paper is worth reading | **Yes—core use case** |
| Understand one method/module/result | **Yes—core use case** |
| Audit one paper's claims against its evidence | **Yes—core use case** |
| Find traceable candidate gaps / ideas | **Yes, with explicit uncertainty** |
| Search and rank an entire literature | No |
| Establish field-wide novelty from one paper | No |
| Replace replication or peer review | No |

A locator provides traceability, not truth. Human review remains necessary for consequential scientific decisions.

## Repository map

```text
paper-evidence-map/
├── SKILL.md
├── manifest.yaml
├── static/core/             # always-loaded principles, source gate, output contract
├── router/                  # goal and depth routing
├── lenses/                  # composable analysis capabilities
├── prompts/                 # paste-ready English and Chinese Project instructions
├── examples/                # synthetic/adversarial/access fixtures
├── schemas/                 # machine-readable evidence-map schema
├── scripts/validate.py      # deterministic repository/response checks
└── docs/                    # methodology, adaptive model, evaluation, design notes
```

## Maturity

PEM remains an early workflow and test harness, not a validated scientific instrument. Structural validation is not the same as semantic reading accuracy. Prompt revisions should be compared with repeated live runs under recorded conditions.

MIT licensed; see [LICENSE](LICENSE).
