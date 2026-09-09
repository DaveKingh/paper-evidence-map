# Launch plan

No launch tactic guarantees stars. The goal is to earn attention with a useful result people can reproduce, then retain contributors by making failures improve the public test set.

## Release gate: do not publish claims before this passes

1. Confirm the owner is `DaveKingh`, the citation/copyright author is `Haochen Yang`, and no publication-critical `YOUR_USERNAME` placeholder remains.
2. Confirm that the README's primary path works in a clean ChatGPT session: create/open a Project, paste the instructions, start ordinary Chat, upload `examples/synthetic/paper.pdf`, and send the exact trigger.
3. Test the intended low-friction mode—including Instant if it is available on the test account—at least three times. Record the visible model/mode label, date, run count, manual rubric total, required findings caught, fabricated locators, and completion/review time.
4. Publish **all** comparable run scores, not the best screenshot. If results are inconsistent, label the project experimental and make the failure visible.
5. Run both local checks:

   ```bash
   python scripts/validate.py
   python scripts/validate.py --response examples/synthetic/expected-output.md --fixture synthetic
   ```

6. Ask 3–5 researchers from different disciplines to try one paper they already know well. Collect missing evidence, false confidence, inaccessible content, and time-to-use—not praise.
7. Upload the included [`assets/social-preview.png`](../assets/social-preview.png) as the 1280×640 social preview. The image and README say “no separate API key” without implying that no ChatGPT account is required.
8. Keep `v0.1.0` immutable. Create release `v0.1.1` from [`releases/v0.1.1.md`](releases/v0.1.1.md) only after the repository checks and repeated A9 live runs are complete.

## GitHub presentation

Recommended repository description:

> Evidence-first paper audit in ChatGPT: map claims to methods, experiments, figures, limitations, and uncertainty. Includes a reproducible synthetic test.

Recommended topics:

`chatgpt`, `chatgpt-prompts`, `research-papers`, `paper-reading`, `literature-review`, `prompt-engineering`, `evidence`, `reproducibility`, `academic-research`, `open-science`, `llm-evaluation`, `chinese`

Before launch:

- enable Issues and Discussions;
- add the social preview and repository description;
- create labels such as `fixture`, `prompt-regression`, `good-first-issue`, `documentation`, and `needs-reproduction`;
- pin a “Run the synthetic challenge and share your score” Discussion;
- pin a “Contribute a paper-reading failure case” Issue;
- seed 3–5 concrete, genuinely approachable issues rather than an empty board.

## The launch artifact

The strongest demonstration is not a feature list. It is one checkable miss:

```text
paper claim: “+8 points on both datasets”
Table 1:       Dataset A +8; Dataset B +4
evidence map:  narrows the claim and points to the conflict
```

Create a 60–90 second screen recording that shows:

1. the upload-ready synthetic PDF;
2. the exact `Round 1`/`第一轮` trigger;
3. the evidence matrix locating Table 1 and Table 2;
4. one limitation the workflow explicitly refuses to guess;
5. the public answer key and scoring rubric;
6. a closing invitation to report a missed finding.

Do not splice together different runs or hide failed outputs. Put the model/mode and run date in the caption.

## Launch sequence

### Day 0: credible seed

- Publish `v0.1.1`, the updated social preview, an unedited A9 demo run, and a compact table of all comparable runs.
- Invite the initial testers to critique a locator, boundary, or missing finding—not to post generic endorsements.
- Use the same canonical link and one-sentence positioning everywhere: **evidence-first single-paper audit, not another summarizer**.

### Days 1–3: demonstrate the miss

- Publish a before/after post built around the +8/+4 contradiction.
- Use channel-specific versions for Hacker News `Show HN`, relevant Reddit communities that permit project sharing, X/LinkedIn, and Chinese research/AI communities such as 知乎. Follow each community's self-promotion rules.
- Answer technical questions with the fixture, run conditions, and known limits. Avoid unsupported claims such as “eliminates hallucinations,” “reads every PDF,” or “works equally well on every model.”
- Ask readers to run the challenge before starring; this lowers shallow engagement but increases signal and useful feedback.

### Week 1: prove maintenance

- Reproduce and triage every actionable failure report.
- Convert at least one real-world miss into an anonymized synthetic fixture with permission-safe content.
- Ship one evidence-backed improvement release; disclose any regression.
- Publish aggregate multi-run results and a short “what it still misses” section.

### Month 1: create return value

- Add discipline packs only when a domain reviewer agrees to maintain them.
- Credit fixture authors and reviewers in release notes.
- Publish a monthly failure report with run conditions and unresolved cases.
- Submit to relevant awesome lists only after reading their contribution rules and showing sustained maintenance.
- Retire modes, screenshots, or product instructions that no longer match the live ChatGPT interface.

## Contribution flywheel

```text
user finds a miss
      ↓
minimal anonymized fixture + expected finding
      ↓
repeated before/after evaluation
      ↓
prompt, rubric, or parser improvement
      ↓
credited release + harder public challenge
```

Keep the unit small enough to review. Large prompt rewrites without repeat-run evidence should not merge.

## Metrics that matter

Track these before star count:

- README → prompt-open rate and challenge completion rate;
- time to first usable evidence map, including setup;
- required-finding recall on every run, not only averages;
- fabricated or invalid locator rate;
- manual-review time and inter-reviewer disagreement;
- issue-to-reproducible-fixture conversion rate;
- first response and resolution time for issues;
- returning contributors and release adoption.

Star count is a lagging, noisy signal. Never buy stars, automate starring, mass-tag people, manufacture testimonials, or imply independent validation that has not happened.

## Stop conditions for a claim

- If repeated runs miss a planted high-severity contradiction, remove any claim that the workflow reliably catches it.
- If the PDF upload path behaves differently from the Markdown fixture, report PDF results separately.
- If a model/mode label changes, update operating instructions but keep the core prompt model-neutral.
- If reviewers disagree on the answer key, resolve the fixture before using its score in promotion.
