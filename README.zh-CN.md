# Paper Evidence Map｜论文证据地图

> **不要只总结论文，要画出它究竟证明了什么。**

[English](README.md) · [快速开始](docs/quickstart.zh-CN.md) · [运行合成论文挑战](#运行可复现挑战) · [证据地图示例](examples/synthetic/expected-output.md) · [方法说明](docs/methodology.zh-CN.md) · [评测方法](docs/evaluation.zh-CN.md) · [已知问题](docs/known-issues.md)

Paper Evidence Map 是一套可复用的 ChatGPT 论文深读提示词与可测试、证据优先的单篇论文工作流。把提示词放进 ChatGPT Project，上传论文，只发送“`第一轮`”；它会要求 ChatGPT 把重要主张连接到方法、实验、图表、限制与可辩护的结论边界，而不只是生成一份流畅摘要。

它面向低门槛的普通 Chat 使用，**在账户提供 Instant 时也可以使用**，但不绑定、也不保证依赖某个模型、模式、套餐或额度规则。

**使用条件：**需要可上传文件的 ChatGPT 账户；推荐但不强制使用 Project。主要工作流**不需要单独的 API Key，也不需要安装软件包**；可选本地检查器需要 Python 3.9+。

![论文证据地图演示](assets/demo.svg)

## 先看一个可以核对的差异

仓库内的合成论文故意让正文主张与原始表格发生冲突：

| 论文怎么说 | 原始证据怎么说 | 可辩护的解读 |
|---|---|---|
| “两个数据集都提升 8 个点” | Table 1：A +8，B **只有 +4** | B 上的标题式结论被夸大 |
| “两个模块都必不可少” | Table 2：移除 C 后 **0.78 → 0.78** | C 的必要性没有得到证明 |
| “具有广泛鲁棒性” | 只在一个数据集测试一种扰动强度 | 证据只支持该测试条件 |

你可以检查 [可直接上传的 PDF](examples/synthetic/paper.pdf)、[便于审阅的 Markdown 源文](examples/synthetic/paper.md)、应被识别的 [8 个必找项](examples/synthetic/expected-findings.md)、[参考证据地图](examples/synthetic/expected-output.md) 和对应的 [JSON 参考导出](examples/synthetic/expected-output.json)。这些材料让方法可以被挑战，但**不能证明每次模型运行都会找全问题**。

## 每个 Project 只设置一次

如果你只想使用工作流，不需要克隆本仓库。

1. 需要全部功能时选择[完整版提示词](prompts/zh-CN/project-instructions.md)，只需要较短的两轮核心流程时选择[精简版提示词](prompts/zh-CN/project-instructions-compact.md)。完整复制其中一个文件，并在 ChatGPT 新建 Project，例如“论文深度阅读”。
2. 打开 Project settings，把提示词粘贴到 Project instructions，然后在该 Project 中新建普通 **Chat**。
3. 上传一篇论文 PDF；有补充材料时一并上传。等待附件可用后发送：**`第一轮`**。
4. 先确认来源清单把本聊天刚上传的论文列为 S1；如果它选中了旧 Project 文件，先使用[恢复指令](prompts/zh-CN/chat-triggers.md)，不要直接相信后续分析。
5. 先读“访问限制”和“未知项”，再看结论；发送 **`第二轮`** 复核最关键的主张。

```text
一次设置 Project → 上传一篇论文 → 第一轮 → 证据地图 → 第二轮 → 有边界的结论
```

如果不使用 Project，可以在普通聊天开头粘贴完整提示词，再上传论文；每个新聊天都需要重新粘贴。

OpenAI 官方文档说明，Project 会集中管理相关聊天、文件、指令和来源，同一个 Project 可以包含由 Chat 或 ChatGPT Work 发起的聊天。本仓库推荐普通 Chat，不要求使用 Work、Codex 或 API。参见 [Projects and chats](https://learn.chatgpt.com/docs/projects)。界面名称、文件限制、模型可用性与额度规则会因账户而异，也可能随时间变化。

## 工作流会生成什么

```text
论文 + 补充材料
        │
        ▼
第一轮：建立证据地图
研究问题 → 技术路线 → 实验 → 主张/证据/边界矩阵
        │
        ▼
第二轮：怀疑式复核
重查原始证据 → 寻找反证 → 收窄结论
        │
        ├── Markdown 研究笔记
        └── 可选 JSON 证据地图
```

默认输出包括：

- 实际阅读覆盖和无法访问的材料；
- 完整技术路线与模块依赖；
- 实验清单和影响结论的缺失信息；
- 主张 → 证据 → 支持强度 → 边界矩阵；
- Abstract、正文、图表和附录之间的冲突；
- 未知项、风险和下一步核查优先级。

每条重要陈述会被标为论文事实、作者解释、分析判断或未知。每个主要结论必须给出真实位置；无法定位时必须明确说明。

## 运行可复现挑战

1. 先**不要看答案**。上传 [`examples/synthetic/paper.pdf`](examples/synthetic/paper.pdf)，发送“`第一轮`”；只有需要审阅测试材料源码时，才打开 [`paper.md`](examples/synthetic/paper.md)。
2. 与 [8 个必找项](examples/synthetic/expected-findings.md) 对照。
3. 用 [100 分人工量表](docs/evaluation.zh-CN.md) 评估证据忠实度。
4. 可选：把回答保存为 Markdown，再运行结构冒烟测试：

```bash
python scripts/validate.py
python scripts/validate.py --response path/to/response.md --fixture synthetic
```

脚本检查仓库完整性、回答结构，以及合成案例的 8 项确定性断言；它仍不能判断所有科研解读是否正确。比较 Prompt 版本时，应在相同条件下至少运行三次并公布全部结果，而不是只展示最好的一次。

基础案例通过后，再运行[多文件对抗案例](examples/adversarial/README.md)，检查来源混用和附件内提示注入；运行[访问限制案例](examples/access-limits/README.md)，检查没有证据或只有部分证据时是否拒绝臆测；最后运行[当前聊天附件优先案例](examples/current-chat-precedence/README.md)，检查新上传论文是否优先于旧 Project 文件。

## 它适合什么，不适合什么

Paper Evidence Map 适合对已经拿到的单篇论文做严谨初审。它刻意不做成一个大而全的研究平台：

| 需求 | 是否适合 |
|---|---|
| 核对单篇论文的主张是否得到内部证据支持 | **是，核心场景** |
| 不写代码，生成结构一致的阅读笔记 | **是** |
| 搜索、筛选并排序整个领域的文献 | 否，应使用文献检索或 RAG 工具 |
| 证明论文具有领域级新颖性 | 否，需要外部文献检索 |
| 复算统计、运行代码或复现实验 | 否，需要统计审查与复现流程 |
| 对扫描件和复杂视觉内容做可靠 OCR | 不保证，必须披露不可访问内容 |

能够定位只代表可追溯，不代表证据一定真实或充分。涉及科研、临床、法律或财务决策时，仍需人工复核。

## 触发词

| 发送内容 | 结果 |
|---|---|
| `第一轮` | 完整证据地图 |
| `第二轮` | 对关键结论进行怀疑式复核 |
| `聚焦：<问题>` | 只围绕一个问题或决策建立地图 |
| `导出 JSON` | 按仓库内 JSON Schema 输出 |
| `阅读状态` | 已检查、未检查和无法访问的内容 |

## 仓库结构

```text
paper-evidence-map/
├── prompts/                 # 可直接粘贴的中英文指令
├── examples/                # 基础、对抗、访问限制和来源优先级夹具
├── schemas/                 # 可选的机器可读证据地图格式
├── scripts/validate.py      # 零依赖仓库/回答检查
├── docs/                    # 快速开始、方法、评测、FAQ 和调研
└── .github/                 # CI、Issue 表单和 PR 模板
```

## 当前成熟度与边界

这是早期工作流与测试框架，不是经过验证的科研测量工具。仓库中的 expected output 是参考材料，不是模型排行榜。只有在记录运行条件并重复测试后，才应发布跨模型或跨学科成绩。请先阅读[已知问题](docs/known-issues.md)，尤其是依赖产品环境的附件选择问题。

除非账户与组织政策允许，否则不要上传机密、未公开、含个人信息、同行评审材料或其他受限制内容。扫描版 PDF、长文档、复杂公式、图表和补充材料可能无法被完整读取。

## 贡献一个更难的测试

最有价值的贡献，是别人可以复现的小型失败案例：

- **最快参与：**运行合成论文挑战，报告遗漏或伪造的位置。
- **高杠杆贡献：**提交一篇原创对抗性迷你论文及答案要点。
- **修改 Prompt：**提供至少三次可比运行的前后成绩，并披露退化项。

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，运行 `python scripts/validate.py`，并让每个 PR 聚焦一个问题。范围内计划见 [ROADMAP.md](ROADMAP.md)。

## License 与引用

采用 MIT License，见 [LICENSE](LICENSE)。如果工作流实质性支持了论文或教学，可使用 [CITATION.cff](CITATION.cff) 引用。

**先运行合成论文挑战。如果它找到了普通摘要遗漏的问题，欢迎 Star；如果它失败了，请提交 Issue——失败案例比掌声更有价值。**
