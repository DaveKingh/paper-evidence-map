# Paper Evidence Map

> **Don't just summarize a paper. Map what it actually proves.**

[简体中文](README.zh-CN.md) · [Quickstart](docs/quickstart.md) · [Run the synthetic challenge](#try-the-reproducible-challenge) · [Example evidence map](examples/synthetic/expected-output.md) · [Method](docs/methodology.md) · [Evaluation](docs/evaluation.md) · [Known issues](docs/known-issues.md)

Paper Evidence Map is a reusable ChatGPT paper-reading prompt plus a testable, evidence-first workflow for one research paper at a time. Put the prompt in a ChatGPT Project, upload a paper, and send `Round 1`. It instructs ChatGPT to connect each major claim to a method, experiment, figure, table, limitation, and defensible boundary—instead of merely producing a fluent summary.

It is designed for low-friction use, including **Instant when that option is available**, but it is not tied to or guaranteed by any particular model, mode, plan, or usage allowance.

**What you need:** a ChatGPT account with file upload access. Projects are recommended but optional. The primary workflow needs **no separate API key and no package install**; the optional local checker requires Python 3.9+.

![Paper Evidence Map demo](assets/demo.svg)

## See the difference on a checkable example

The included synthetic paper deliberately makes claims that its own tables do not support:

| What the paper says | What its primary evidence says | Defensible reading |
|---|---|---|
| “8-point gains on both datasets” | Table 1: +8 points on A, **+4** on B | The headline is overstated for B |
| “Both modules are essential” | Table 2: removing C changes **0.78 → 0.78** | Necessity of C is not demonstrated |
| “Broadly robust” | One corruption level on one dataset | Evidence supports only that tested condition |

Inspect the [upload-ready PDF](examples/synthetic/paper.pdf), its [reviewable Markdown source](examples/synthetic/paper.md), the [eight required findings](examples/synthetic/expected-findings.md), a [reference evidence map](examples/synthetic/expected-output.md), and the matching [reference JSON export](examples/synthetic/expected-output.json). These artifacts make the method challengeable; they do **not** prove that every model run will catch every issue.

## Setup once per Project

If you only want to use the workflow, you do not need to clone this repository.

1. Choose the [full prompt](prompts/en/project-instructions.md) for all features, or the [compact prompt](prompts/en/project-instructions-compact.md) for the shorter Round 1/2 core. Copy one complete file and create a ChatGPT Project such as **Paper Deep Reading**.
2. Open the Project settings, paste the prompt into Project instructions, then start a new **Chat** in that Project.
3. Upload one paper PDF and its supplement, if available. Wait until the attachment is available, then send **`Round 1`**.
4. Verify that the source ledger names the paper uploaded in this chat as S1. If it selects an older Project file, use the [recovery trigger](prompts/en/chat-triggers.md) before trusting the analysis.
5. Read the access limits and unknowns before the verdict. Send **`Round 2`** to re-check the most consequential claims.

```text
one-time Project setup → upload one paper → Round 1 → evidence map → Round 2 → bounded verdict
```

Without Projects, paste the complete prompt into a normal chat before uploading the paper. You will need to paste it again in each new chat.

OpenAI's documentation says Projects keep related chats, files, instructions, and sources together, and that one Project can contain chats started with either Chat or ChatGPT Work. This repository recommends ordinary Chat; it does not require Work, Codex, or the API. See [Projects and chats](https://learn.chatgpt.com/docs/projects). Interface labels, file limits, model availability, and usage rules can vary by account and change over time.

## What the workflow produces

```text
paper + supplement
        │
        ▼
Round 1: evidence map
question → method → experiments → claim/evidence/boundary matrix
        │
        ▼
Round 2: skeptical audit
re-open primary evidence → seek counterevidence → narrow conclusions
        │
        ├── Markdown research note
        └── optional JSON evidence map
```

The default output includes:

- reading coverage and inaccessible material;
- an end-to-end method and module map;
- an experiment inventory, including consequential omissions;
- a claim → evidence → support → boundary matrix;
- contradictions across abstract, prose, tables, figures, and appendices;
- an uncertainty register and prioritized next checks.

Each important statement is labeled as paper fact, author interpretation, analyst judgment, or unknown. Every major conclusion needs a real locator—or an explicit statement that it could not be located.

## Try the reproducible challenge

1. Do **not** read the answer key yet. Upload [`examples/synthetic/paper.pdf`](examples/synthetic/paper.pdf) and send `Round 1`. Use [`paper.md`](examples/synthetic/paper.md) only when you want to audit the fixture source.
2. Compare the result with the [required findings](examples/synthetic/expected-findings.md).
3. Score evidence fidelity with the [100-point manual rubric](docs/evaluation.md).
4. Optionally save the response as Markdown and run the structural smoke test:

```bash
python scripts/validate.py
python scripts/validate.py --response path/to/response.md --fixture synthetic
```

The checker validates repository integrity, response structure, and eight deterministic assertions for this synthetic fixture. It cannot determine whether every scientific interpretation is correct. For prompt comparisons, run the same conditions at least three times and report every run—not only the best one.

After the basic case, use the [adversarial multi-file fixture](examples/adversarial/README.md) to test source mixing and document prompt injection, the [access-limit fixtures](examples/access-limits/README.md) to test refusal under missing or partial evidence, and the [current-chat precedence fixture](examples/current-chat-precedence/README.md) to test whether a new upload outranks older Project files.

## Where it fits

Use Paper Evidence Map when you need a careful first-pass audit of a paper you already have. It is deliberately smaller than a research platform:

| Need | Fit |
|---|---|
| Audit one paper's claims against its internal evidence | **Yes—core use case** |
| Create repeatable reading notes without writing code | **Yes** |
| Search and rank an entire literature | No; use a literature-search or RAG tool |
| Establish field-wide novelty | No; requires external literature review |
| Verify statistics, rerun code, or replicate experiments | No; use statistical review and reproduction workflows |
| Reliably OCR complex scans or inspect every visual detail | Not guaranteed; disclose inaccessible content |

A locator provides traceability, not truth. Human review remains necessary for decisions with scientific, clinical, legal, or financial consequences.

## Triggers

| Send | Result |
|---|---|
| `Round 1` | Full evidence map |
| `Round 2` | Skeptical re-check of consequential claims |
| `Focus: <question>` | Evidence map scoped to one decision or question |
| `Export JSON` | Output against the included JSON schema |
| `Reading status` | Inspected, uninspected, and inaccessible content |

Chinese triggers are in the [full Chinese prompt](prompts/zh-CN/project-instructions.md) and its [compact version](prompts/zh-CN/project-instructions-compact.md).

## Repository map

```text
paper-evidence-map/
├── prompts/                 # Paste-ready English and Chinese instructions
├── examples/                # Basic, adversarial, access-limit, and source-precedence fixtures
├── schemas/                 # Optional machine-readable evidence-map schema
├── scripts/validate.py      # Zero-dependency repository/response checks
├── docs/                    # Quickstart, method, evaluation, FAQ, and research
└── .github/                 # CI, issue forms, and pull-request template
```

## Maturity and limits

This is an early workflow and test harness, not a validated scientific instrument. The included expected output is a reference artifact, not a model leaderboard. Cross-model and cross-discipline baselines should be published only after repeat runs under recorded conditions. Read the [known issues](docs/known-issues.md), especially the product-dependent attachment-selection case.

Do not upload confidential, embargoed, personally identifying, peer-review, or otherwise restricted material unless your account and organization policies permit it. Scanned PDFs, long documents, equations, figures, and supplements may be incompletely accessible.

## Contribute a harder test

The most useful contribution is a small failure case that others can reproduce:

- **Quick:** run the synthetic challenge and report a missed or fabricated finding.
- **High leverage:** contribute an original adversarial mini-paper plus expected findings.
- **Prompt change:** include before/after scores from at least three comparable runs and disclose regressions.

Read [CONTRIBUTING.md](CONTRIBUTING.md), run `python scripts/validate.py`, and keep each pull request focused. See the [roadmap](ROADMAP.md) for work in scope.

## License and citation

MIT licensed; see [LICENSE](LICENSE). If the workflow materially supports published research or teaching, use [CITATION.cff](CITATION.cff).

**Run the synthetic challenge first. If it catches something your usual summary missed, star the repository. If it fails, open an issue—the failure is more valuable than applause.**
