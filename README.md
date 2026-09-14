# Paper Evidence Map

> **Don't just summarize a paper. Map what it actually proves — and only read as deeply as the current question requires.**

[简体中文](README.zh-CN.md) · [Quickstart](docs/quickstart.md) · [Adaptive reading](docs/adaptive-reading.md) · [Routing evaluation](docs/evaluation-adaptive.md) · [Method](docs/methodology.md) · [Known issues](docs/known-issues.md)

Paper Evidence Map is an adaptive, evidence-first ChatGPT workflow for research papers. Instead of forcing every paper through a full review, it first infers what you are trying to learn or decide, then uses the minimum reading depth needed to answer reliably.

Examples:

```text
“What is this paper about?”              → Scan
“Is it worth reading for my research?”   → Triage
“How does this module work?”             → Targeted
“Read this paper deeply.”                → Deep
“Strictly audit the main conclusions.”   → Audit
```

The evidence core stays the same at every depth:

```text
claim → evidence → support → defensible boundary
```

When useful, the workflow can also turn paper-internal anomalies into **Candidate Gaps** and **Candidate Ideas** without pretending they are already verified novelty.

It is designed for low-friction use in ordinary ChatGPT chats and Projects. It is not tied to a particular model, mode, plan, or usage allowance.

**What you need:** a ChatGPT account with file upload access. Projects are recommended but optional. The primary workflow needs no separate API key and no package install; optional local checks use Python 3.9+.

![Paper Evidence Map demo](assets/demo.svg)

## Why adaptive reading?

Researchers rarely need the same thing from every paper. Sometimes you only need to know whether a paper is relevant. Sometimes you need one method detail, one experiment, one disputed claim, or one possible research gap. A fixed full-paper template wastes time and output when the user's question is narrow.

PEM v0.2 therefore follows three rules:

1. **No user need → no analysis.**
2. **No evidence → no strong claim.**
3. **No verified gap → no strong research idea.**

The workflow stops when the current goal is satisfied and escalates only when a reliable answer requires more evidence.

## Five reading depths

| Depth | Use it for |
|---|---|
| **Scan** | Orientation: what is this paper about? |
| **Triage** | Is it relevant, worth reading, or useful for your research? |
| **Targeted** | One method, table, figure, claim, or question |
| **Deep** | Broad method/experiment/claim–evidence map |
| **Audit** | Skeptical re-check of decisive claims |

If you upload a paper without asking for a full deep read, the default is **Triage**.

## Setup once per Project

If you only want to use the workflow, you do not need to clone this repository.

1. Choose the [full prompt](prompts/en/project-instructions.md), or the [compact adaptive prompt](prompts/en/project-instructions-compact.md) for a shorter persistent instruction set.
2. Create a ChatGPT Project such as **Paper Evidence Map**.
3. Paste the selected prompt into Project instructions.
4. Start one chat per paper and upload the paper plus any clearly linked supplement.
5. Ask the real question directly. You do not need to start with `Round 1`.

Useful examples:

```text
Is this paper worth reading if I care about trustworthy evaluation?
Explain Section 3.2 and how the module actually works.
Does Table 4 really support the robustness claim?
Can this paper give me a research idea?
I need to present this paper tomorrow — what should I focus on?
```

Legacy triggers still work:

```text
Round 1  → Deep
Round 2  → Audit
Focus: X → Targeted
```

## See the difference on a checkable example

The included synthetic paper deliberately makes claims that its own tables do not support:

| What the paper says | What its primary evidence says | Defensible reading |
|---|---|---|
| “8-point gains on both datasets” | Table 1: +8 points on A, **+4** on B | The headline is overstated for B |
| “Both modules are essential” | Table 2: removing C changes **0.78 → 0.78** | Necessity of C is not demonstrated |
| “Broadly robust” | One corruption level on one dataset | Evidence supports only that tested condition |

Inspect the [upload-ready PDF](examples/synthetic/paper.pdf), [Markdown source](examples/synthetic/paper.md), [required findings](examples/synthetic/expected-findings.md), [reference evidence map](examples/synthetic/expected-output.md), and [reference JSON export](examples/synthetic/expected-output.json).

These artifacts make the method challengeable; they do **not** prove that every model run will catch every issue.

## Candidate Gaps and Candidate Ideas

PEM can surface an interesting paper-internal asymmetry or omission before a full audit. For example:

```text
observation
  ↓
Candidate Gap
  ↓
Targeted Evidence Check
  ↓
Candidate Idea
  ↓
external novelty / feasibility checks when needed
  ↓
Research Idea
```

A missing experiment alone is not enough to claim novelty.

## What PEM produces

The output depends on the user's goal.

A Triage answer may only contain:

- relevance to the user's current problem;
- the paper's core contribution;
- what to read first;
- what can wait;
- preliminary research leverage;
- one recommended next step.

A Deep/Audit answer may include:

- source and reading coverage;
- end-to-end method/module map;
- experiment inventory;
- claim → evidence → support → boundary matrix;
- cross-section contradictions and overclaims;
- unknown/risk register;
- prioritized re-checks.

Every important substantive statement should be traceable to a real source location or explicitly marked unknown/inaccessible.

## Try the reproducible evidence challenge

1. Upload [`examples/synthetic/paper.pdf`](examples/synthetic/paper.pdf).
2. Send `Round 1` to deliberately exercise the backward-compatible Deep path.
3. Compare with [required findings](examples/synthetic/expected-findings.md).
4. Score with the [100-point evidence rubric](docs/evaluation.md).
5. Optionally run:

```bash
python scripts/validate.py --response path/to/response.md --fixture synthetic
```

## Test adaptive routing

The new v0.2 behavior has its own fixture because a response can be factually correct yet still fail by reading too much, too little, or using the wrong analytical mode.

See [`examples/adaptive-routing/`](examples/adaptive-routing/README.md) and the [adaptive evaluation guide](docs/evaluation-adaptive.md).

Validate the routing fixture contract with:

```bash
python scripts/check_adaptive_routes.py
```

Routing failure classes include:

```text
OVERREAD
UNDERREAD
MISROUTE
NO_STOP
EVIDENCE_BYPASS
IDEA_OVERPROMOTION
```

The deterministic checker verifies the fixture definition, not model quality. Live routing behavior still requires repeated runs and human scoring.

## Where it fits

Paper Evidence Map is deliberately narrower than an end-to-end academic research platform.

| Need | Fit |
|---|---|
| Decide whether a paper is worth your time | **Yes** |
| Understand one method/module/experiment | **Yes** |
| Audit one paper's claims against its internal evidence | **Yes — core** |
| Find traceable Candidate Gaps/Ideas | **Yes, with status boundaries** |
| Create repeatable paper-reading notes | **Yes** |
| Search and rank an entire literature | No; use a literature-search workflow |
| Establish field-wide novelty from one paper | No |
| Re-run experiments or statistically replicate results | No |
| Full research → experiment → writing lifecycle | No; use a broader research suite |

A locator provides traceability, not truth. Human review remains necessary for consequential scientific decisions.

## Architecture

PEM v0.2 uses a thin router inspired by mature Skill architectures while keeping its own evidence model:

```text
SKILL.md
   ↓
manifest.yaml
   ↓
Goal Router + Depth Router
   ↓
selected Lens(es)
   ↓
source-grounded evidence work
   ↓
STOP when sufficient
```

See [design reference audit](docs/design-reference-audit.md) for what PEM borrows from Nature Skills and Academic Research Suite and what remains intentionally PEM-specific.

## Repository map

```text
paper-evidence-map/
├── SKILL.md                 # Thin skill router
├── manifest.yaml            # Loading and routing contract
├── static/core/             # Always-loaded principles/source/output rules
├── router/                  # Goal and depth routing
├── lenses/                  # Composable reading capabilities
├── prompts/                 # Paste-ready English and Chinese Project instructions
├── examples/                # Evidence, adversarial, access, precedence, routing fixtures
├── schemas/                 # Machine-readable evidence-map schema
├── scripts/                 # Repository, evidence, and routing checks
└── docs/                    # Method, quickstart, evaluation, design notes
```

## Maturity and limits

This is an early workflow and test harness, not a validated scientific instrument. The expected outputs and routing fixtures are evaluation artifacts, not model leaderboards.

Do not upload confidential, embargoed, personally identifying, peer-review, or otherwise restricted material unless your account and organization policies permit it. Scanned PDFs, long documents, equations, figures, and supplements may be incompletely accessible.

## Contribute a harder test

The most useful contribution is a reproducible failure case:

- evidence failure: missed contradiction, fabricated locator, boundary error;
- routing failure: over-reading, under-reading, wrong lens, failure to stop;
- idea failure: unverified omission promoted to novelty;
- source failure: paper/supplement/review mixing or prompt injection.

Read [CONTRIBUTING.md](CONTRIBUTING.md), run the repository checks, and keep each pull request focused.

## License and citation

MIT licensed; see [LICENSE](LICENSE). If the workflow materially supports published research or teaching, use [CITATION.cff](CITATION.cff).
