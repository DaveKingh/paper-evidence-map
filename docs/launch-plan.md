# Launch plan

Stars are an outcome of recurring utility and trust. This plan optimizes for people who can reproduce a useful result in five minutes.

## Before publishing

1. Replace every `DaveKingh` and maintainer placeholder.
2. Add a 1280脳640 social preview derived from `assets/demo.svg`.
3. Run `python scripts/validate.py` on Windows, macOS, or Linux.
4. Test the synthetic paper in a fresh ChatGPT Project at least three times; publish all scores, not only the best.
5. Ask 3鈥? researchers from different fields to test one real paper and report missing evidence.
6. Turn on GitHub Discussions and choose the repository topics listed below.
7. Create release `v0.1.0` using [`docs/releases/v0.1.0.md`](releases/v0.1.0.md).

Recommended description:

> Evidence-first deep reading for research papers in ChatGPT: map claims to methods, experiments, figures, limitations, and uncertainty.

Recommended topics:

`chatgpt`, `research-papers`, `literature-review`, `prompt-engineering`, `evidence`, `reproducibility`, `academic-research`, `open-science`, `llm-evaluation`, `chinese`

## Launch sequence

### Day 0: credible seed

- Publish the repository, release, social preview, and a 60鈥?0 second screen recording.
- Pin one issue: 鈥淪hare a paper-reading failure case.鈥?
- Share with the initial testers and ask for critique or fixtures, not generic promotion.

### Days 1鈥?: demonstrate the miss

- Publish a before/after example: ordinary summary misses the synthetic contradictions; evidence map catches them.
- Post concise versions to GitHub, X/LinkedIn, Reddit communities that allow project sharing, Hacker News `Show HN`, and Chinese research/AI communities such as 鐭ヤ箮 or灏忕孩涔?where appropriate.
- Adapt the explanation to each community; do not cross-post identical promotional copy everywhere.

### Week 1: close the loop

- Triage every reproducible issue.
- Ship one improvement release based on user failures.
- Add one new fixture from a different discipline.
- Publish aggregate multi-run scores and known failures.

### Month 1: build return value

- Add discipline packs only when maintained by domain users.
- Highlight contributors in release notes.
- Publish a monthly 鈥渨hat the workflow still misses鈥?report.
- Submit to relevant awesome lists only after meeting their contribution rules and demonstrating sustained maintenance.

## Demo script

1. Show a normal one-paragraph summary of the synthetic paper.
2. Highlight the abstract claim: 鈥? points on both datasets.鈥?
3. Run `Round 1`.
4. Zoom into the evidence matrix: Table 1 shows only +4 points on Dataset B.
5. Show Table 2: Module C has no measured effect despite being called essential.
6. End on: 鈥淭raceable does not mean true鈥攂ut untraceable is harder to challenge.鈥?

## Metrics that matter

- quickstart completion rate;
- percentage of testers who catch all planted findings;
- false or fabricated locator rate;
- time to first useful evidence map;
- issue-to-fixture conversion rate;
- returning contributors and release adoption.

Star count is a lagging signal. Do not buy stars, automate starring, or use misleading claims.


