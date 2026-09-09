# FAQ

## Is this only for ChatGPT Instant?

It is optimized for a low-friction ChatGPT Project chat and can be used with Instant when that option is available. It is prompt-based rather than model-locked. Availability, naming, behavior, and usage limits can change; check the current product interface and official documentation.

## Does a Project automatically read every page?

No assumption of complete access is safe. The prompt requires a coverage statement and asks the assistant to disclose inaccessible scans, figures, appendices, or supplements.

## What if it selects an older Project file instead of my new upload?

Stop that run and use the [S1 recovery trigger](../prompts/en/chat-triggers.md), explicitly naming the paper uploaded in the current chat. Do not trust an evidence map whose source ledger names the wrong primary paper. This product-dependent behavior and its manual regression fixture are documented in [Known issues](known-issues.md).

## Can it prove a paper is correct?

No. It can improve traceability and expose internal gaps. It cannot validate source data, rerun statistics, reproduce experiments, or replace expert review.

## Can it judge novelty?

Not from one attached paper. Internal contribution claims can be mapped, but field-wide novelty requires a separate literature search with external sources.

## Why not ask for a summary first?

You can derive a summary from an evidence map. The reverse is unreliable because a summary often removes caveats and provenance.

## What if the paper is very long?

Ask for `Reading status`, then use `Focus: <question>` for the decision you care about. Include supplementary files explicitly.

## Can I use it with another AI assistant?

Usually, yes: paste the prompt as persistent/custom instructions where supported. Interface-specific steps and document-access behavior will differ, so re-run the included evaluation.

## Does the validator grade scientific correctness?

No. It catches missing structural signals and broken repository links. Use the manual rubric and expected findings for content evaluation.
