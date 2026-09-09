# Design research: what high-star repositories actually teach us

Snapshot date: **2026-09-09**. Star counts below are rounded snapshots from public GitHub repository pages or the GitHub API. They change continuously and are adoption signals—not proof that a README pattern caused growth or that a project is technically superior.

## Broad open-source exemplars

| Project | Stars at snapshot | Observable repository pattern | What transfers here |
|---|---:|---|---|
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | 181.4k | Defines one job in the first paragraph, shows concrete supported inputs, puts security boundaries and runnable usage close to the top. | State the single-paper audit job, show a concrete contradiction, disclose file-access and privacy limits. |
| [f/prompts.chat](https://github.com/f/prompts.chat) | 169.7k | Turns prompts into a browsable/copyable product, supports community submissions, and offers multiple surfaces such as web, CLI, self-hosting, and integrations. | Make the prompt directly copyable, keep bilingual entry points, and turn failure reports into reviewable contributions. |
| [astral-sh/uv](https://github.com/astral-sh/uv) | 89.6k | Leads with a narrow measurable promise, then demonstrates real commands and outputs before deep documentation. | Put the shortest successful path and an inspectable result before architecture; avoid speed claims that have not been measured. |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 78.1k | Combines a repository with maintained learning material, multiple languages, releases, a web presence, and citation guidance. | Pair the prompt with method/evaluation docs, English and Chinese parity, changelog, and citation metadata. |
| [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | 43.9k | Uses a memorable philosophy plus named, reusable task patterns rather than presenting an undifferentiated prompt collection. | Keep “claim → evidence → boundary” as the memorable unit and use stable triggers such as `Round 1`. |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 24.9k | Treats prompts as testable artifacts, provides a fast quickstart, repeatable evaluations, CI integration, and explicit capabilities. | Ship adversarial fixtures, an answer key, a rubric, a structural checker, and evidence requirements for prompt changes. |

## Adjacent research-paper tools

These projects clarify the category boundary better than generic prompt repositories do.

| Project | Stars at snapshot | Core value | Positioning implication |
|---|---:|---|---|
| [binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic) | 71.3k | A broad academic LLM application with many models, plugins, translation, summarization, code analysis, GUI, and deployment paths. | Do not compete on feature breadth. Paper Evidence Map should win on zero-code setup, a narrow audit job, and inspectable tests. |
| [Future-House/paper-qa](https://github.com/future-house/paper-qa) | 9.2k | Programmatic scientific-document RAG with grounded answers, indexing, metadata, CLI/library APIs, and published research. | Do not imply equivalent retrieval or benchmark rigor. Position this project as a lightweight single-paper workflow for users who already have ChatGPT. |

## What the README must accomplish

The landing page should answer these questions without requiring the reader to open another file:

1. **What is the output?** A claim–evidence–boundary map for one paper.
2. **What does it catch?** Show one numerical contradiction and one unsupported module claim from the synthetic fixture.
3. **What do I need?** A ChatGPT account with file upload access; Projects are recommended. No separate API key or local package is required for the primary workflow.
4. **What is the shortest path?** Copy the prompt, paste it into Project instructions, upload a PDF, send `Round 1`.
5. **What proves it?** An upload-ready synthetic PDF, auditable source, public answer key, manual rubric, and structural checker.
6. **What does it not do?** Literature search, novelty verification, statistical reanalysis, replication, or guaranteed PDF/OCR coverage.
7. **How can I help?** Report a reproducible miss or add a small adversarial fixture.

The previous “30-second quickstart” label was too precise: setup time depends on account state, file upload, and response generation. “No API key” also needed qualification because the workflow still requires a ChatGPT account. The README now uses “no separate API key” and avoids a promised completion time.

## Positioning decision

“AI paper summarizer” is crowded and weakly differentiated. The sharper category is **evidence-first single-paper audit**. The memorable object is not a better summary; it is a traceable triple:

```text
claim → primary evidence → defensible boundary
```

The defensible promise is improved structure, traceability, and challengeability. It is **not** guaranteed correctness, hallucination elimination, full-PDF coverage, field-wide novelty judgment, or equal performance across ChatGPT models and modes.

The workflow can be used in ordinary Chat, including Instant when available, but the repository should not be named or architected around a volatile model label. Mentioning Instant once in descriptive copy serves the intended low-friction use case and search intent; all operating instructions remain mode-neutral/explainable if product labels change.

## Why the synthetic demo matters

A generic screenshot proves that an output looks polished. It does not prove that the output finds a contradiction. The synthetic fixture provides:

- an upload-ready PDF that exercises the real file path;
- a Markdown source that maintainers can audit line by line;
- planted contradictions and omissions with known locations;
- a public content-level answer key;
- a 100-point manual rubric plus separate structural and deterministic fixture checks.

The expected output is intentionally described as a **reference artifact**, not a model benchmark; it is a review aid. Credible performance claims require repeated live ChatGPT runs under recorded model, mode, and date conditions.

## README and conversion design

The revised README follows a proof-first path:

```text
specific promise → visible contradiction → requirements → copy/use path
→ reproducible challenge → scope limits → contribution CTA
```

This prioritizes first-use conversion without hiding caveats. The primary CTA is “run the synthetic challenge,” not “star the repository.” The final CTA earns the star request only after a result and treats failures as valuable contributions.

## Contribution and retention loop

The scalable contribution unit is not a large prompt rewrite. It is a compact fixture:

```text
real-world miss → anonymized synthetic case → expected finding
→ repeatable evaluation → prompt or rubric change → credited release
```

This loop gives users a reason to return: each substantive release should add a new failure mode, discipline pack, language improvement, or measured prompt change. Cosmetic version bumps do not add return value.

## Distribution hypothesis

Distribution should demonstrate a miss, not announce “another prompt repository.” The strongest launch asset is a short before/after showing the synthetic paper's “+8 on both datasets” claim versus Table 1's +8/+4 result, with the public fixture and answer key linked. Channel-specific posts should lead to the challenge and disclose early-project status.

Potential high Star does not come from copying surface features of large repositories. It depends on repeated utility, a credible proof artifact, fast issue response, visible maintenance, and a contribution unit that compounds the test set.

## Primary sources

- [MarkItDown repository](https://github.com/microsoft/markitdown)
- [prompts.chat repository](https://github.com/f/prompts.chat)
- [uv repository](https://github.com/astral-sh/uv)
- [Prompt Engineering Guide repository](https://github.com/dair-ai/Prompt-Engineering-Guide)
- [Fabric repository](https://github.com/danielmiessler/Fabric)
- [Promptfoo repository](https://github.com/promptfoo/promptfoo)
- [GPT Academic repository](https://github.com/binary-husky/gpt_academic)
- [PaperQA2 repository](https://github.com/Future-House/paper-qa)
- [Official OpenAI documentation: Projects and chats](https://learn.chatgpt.com/docs/projects)
