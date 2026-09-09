# Launch copy

Add the tested model/mode and date, and link the public multi-run results before publishing. Do not call the reference output a benchmark result.

## GitHub release / general post

I built **Paper Evidence Map** because “summarize this paper” often preserves the authors' confidence while dropping the limits of the evidence.

It is a copy-paste workflow for an ordinary ChatGPT chat, including Instant when available: add the prompt to a Project, upload one PDF, and send `Round 1`. The output separates paper facts, author interpretations, analyst judgments, and unknowns, then links major claims to their methods, experiments, figures, tables, and defensible boundaries.

The repository includes an upload-ready synthetic PDF with eight required findings, an auditable answer key, a 100-point manual rubric, and a zero-dependency repository/fixture checker. One example: the paper says “+8 points on both datasets,” while Table 1 reports +8 and +4.

It is an early workflow, not a guarantee of correctness. A ChatGPT account with file upload access is required; no separate API key or local package is needed for the main path.

Run the challenge before starring it—and report what it misses:
https://github.com/DaveKingh/paper-evidence-map

Tested: `[visible model/mode]`, `[date]`, `[n] runs`; results: `[link]`.

## Short post

“+8 points on both datasets,” says the paper. Its own Table 1 says +8 and +4.

Paper Evidence Map is a copy-paste ChatGPT workflow that maps claims to evidence and conclusion boundaries. It ships with a synthetic PDF, answer key, rubric, and checker—so you can test it rather than trust the demo.

Early project; no correctness guarantee. Run the challenge: https://github.com/DaveKingh/paper-evidence-map

## Show HN

Title:

> Show HN: Paper Evidence Map – audit a paper's claims against its own evidence

Opening paragraph:

> I made a small, testable alternative to “summarize this PDF.” You paste one prompt into a ChatGPT Project, upload a paper, and ask for a claim–evidence–boundary map. The repo includes a synthetic PDF whose prose conflicts with its tables, a public answer key, and a manual rubric. It requires a ChatGPT account but no separate API key or local install for the main workflow. I would especially value runs that miss a planted contradiction or invent a locator.

## 中文发布文案

我做了一个 **Paper Evidence Map｜论文证据地图**，因为“总结这篇论文”经常保留作者的自信，却丢掉证据真正能支持的范围。

它是一套可直接复制到 ChatGPT Project 的单篇论文审计工作流，账户提供 Instant 时也可以使用。上传 PDF，发送“`第一轮`”，输出会区分论文事实、作者解释、分析判断和未知项，并把重要主张连接到方法、实验、图表和结论边界。

仓库附有一份可直接上传的合成 PDF 和 8 个必找项；同时公开答案要点、100 分人工量表和零依赖仓库/案例检查器。比如论文声称“两个数据集都提升 8 个点”，但 Table 1 实际是 +8 和 +4。

这是早期工作流，不保证判断正确。需要可上传文件的 ChatGPT 账户；主流程不需要单独 API Key，也不需要本地安装。

建议先跑挑战，再决定是否 Star；更欢迎告诉我它漏掉或编造了什么：
https://github.com/DaveKingh/paper-evidence-map

测试条件：`[界面显示的模型/模式]`，`[日期]`，`[n 次运行]`；完整结果：`[链接]`。

## 中文短文案

论文说“两个数据集都 +8”，Table 1 却是 +8 和 +4。

我把“总结论文”改成了“主张 → 证据 → 边界”的可测试 ChatGPT 工作流，并附上合成 PDF、公开答案和评分量表。先别信演示，自己跑一次：
https://github.com/DaveKingh/paper-evidence-map

## Tester outreach

> I am testing an early evidence-first paper-reading workflow, not asking for an endorsement. Could you try it on one paper you know well and report one missed qualification, invalid locator, inaccessible item, or unnecessary step? Please include the visible model/mode, date, exact trigger, and whether the supplement was available. Do not send confidential or peer-review material.
