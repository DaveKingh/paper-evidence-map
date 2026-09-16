# 方法说明

## 核心对象：主张—证据—边界

对每个影响结论的主张，PEM 追问：

1. **主张**：究竟声称了什么，由谁提出？
2. **证据**：哪项结果或方法细节与它相关，具体在哪里？
3. **边界**：现有证据能够辩护的最强但更窄的表述是什么？

找到正确结果并不等于可以重复一个比证据范围更大的结论。

## 自适应控制架构：Three-Gate Model

PEM 不是固定阅读流水线。运行时由三个 Gate 与 Goal/Depth Router 共同控制：

```text
User Goal
    ↓
Access Gate
    ↓
Goal / Depth Router
    ↓
Minimum-Sufficient Reading + 必要 Lens
    ↓
Evidence
    ↓
发现旁路问题？ → Materiality Gate
                  ├─ YES：最小必要核查 → 回原问题
                  └─ NO：Candidate Issue → 不展开
    ↓
Sufficiency / STOP Gate
    ├─ NO：继续最小必要阅读
    └─ YES：STOP → Answer
```

### Access Gate
判断当前可访问的原始证据是否足以支撑用户要求的结论。决定性证据不可访问时，应收窄答案或写“无法判断”，而不是用文件名、记忆或外部资料补全。

### Materiality Gate
旁路发现只有在可能实质改变当前答案的正确性、边界或用户下一步决策时，才允许触发重路由。否则只登记为 Candidate Issue，不扩大任务。

### Sufficiency / STOP Gate
当前目标已经得到足够证据和不确定性说明后停止。“完整”是覆盖所有可能改变当前答案的内容，而不是复述论文所有章节。

因此 D0–D4 和 Lens 都不是强制工作流步骤，而是由 Router/Gate 选择的控制参数和分析能力。

## 阅读深度

用户没有要求全文深读时，默认使用 **Triage**，而不是 Deep。

| 深度 | 目的 |
|---|---|
| Scan | 判断论文在做什么及与当前目标的初步相关性 |
| Triage | 判断相关性以及下一步该看哪里 |
| Targeted | 回答一个具体方法、实验、主张或 Idea 问题 |
| Deep | 建立较完整的方法/实验/主张—证据地图 |
| Audit | 重新打开决定性证据，尝试证伪或收窄关键结论 |

只有当前深度无法支撑用户所需结论时才升级。

## 第一轮和第二轮的位置

原来的两轮流程保留为 **Deep → Audit** 路径，而不是所有论文阅读的统一入口。

- **第一轮 / Round 1** → Deep。
- **第二轮 / Round 2** → Audit。

两轮分开仍有助于强制重新检查关键证据，但大量真实问题应在 Triage 或 Targeted 阶段停止。

## 四类标签

| 标签 | 含义 | 示例 |
|---|---|---|
| 论文事实 | 可直接定位的报告值、观察或程序描述 | “Table 2 报告 macro-F1 为 0.78。” |
| 作者解释 | 作者的解释、因果归因或推广 | “作者把提升归因于模块 G。” |
| 分析判断 | 基于证据的分析推断 | “消融结果削弱了‘模块必需’主张。” |
| 未知 | 没写或无法访问 | “随机种子数量未说明。” |

“论文事实”表示“论文直接报告了什么”，不表示该结果已经被独立复现，也不自动支持作者进一步提出的解释、因果或推广结论。

## 论文内部证据与外部资料

论文内部事实和作者主张必须由对应原始论文及明确关联的官方补充材料支持。外部资料可以用于背景解释、概念核查、新颖性检索或用户明确要求的其他外部问题，但 **外部证据不能修复论文内部缺失证据**。

例如论文未报告 random seed，而官方代码当前写 `seed=42`，可以单独报告“实现证据”，但不能回填成“论文使用 seed 42”。Paper / Supplement / Official Code / External Paper / Benchmark Documentation 等更细 provenance 类型可以进入后续 schema，而不必全部出现在普通用户回答中。

## 与主张相关的证据优先级

证据优先级取决于被判断的主张，应优先选择离相关观测或操作最直接的证据：

- 性能/鲁棒性 → 对应 Table/Figure/Results + 必要实验设置；
- 方法机制/架构 → Methods/Algorithm/Equation；代码若使用，应明确作为外部实现证据；
- 数据/实验协议 → Dataset/Experimental Setup/Supplement；
- 作者动机/解释 → Introduction/Discussion，并保持“作者解释”类型。

Abstract/Introduction/Discussion/Conclusion 的总结性措辞不能覆盖与主张更直接的决定性证据。论文内部冲突时应报告冲突，不自行调和。

## 支持强度

- **强**：直接证据、对照与不确定性报告都与结论范围匹配。
- **中等**：有相关证据，但仍有实质限制。
- **弱**：证据间接、范围窄、对照不足，或与主张宽度不一致。
- **无法判断**：决定性信息缺失或不可访问。

强度针对单个主张，不是论文总分。

## 访问与来源细则

附件存在不等于内容已经读取。来源/访问登记应与当前深度相匹配：哪些来源是论文/补充/背景，哪些决定性证据已检查，以及哪些内容未检查、缺失、不可读、被截断或 OCR 不确定。

多文件场景使用稳定来源编号防止“洗证据”。定位应同时标出来源和证据对象，如 `S1，Table 2，without C 行`。当前聊天最新上传且可访问的论文优先作为 `S1` 候选；存在多篇候选时先确认。

## 主张级支持判定

依次追问：

1. 决定性证据可访问吗？不能则为**无法判断**。
2. 引用对象里真的有该数值、方向和比较吗？
3. 设计是否匹配主张的人群、任务、干预、基线、指标和时间范围？
4. 对照和不确定性是否足以支持该范围？
5. 最强且更窄的可辩护表述是什么？

同一数值可以强力支持“论文报告 X”，却只能很弱地支持作者据此提出的因果或普遍结论。

## Candidate Issue、Gap 与 Research Idea

### Candidate Issue

阅读中发现、可追踪但与当前问题没有实质关系的异常、矛盾或潜在问题。需要时简短登记，不自动深挖。

### Candidate Gap：正交状态模型

不要把 Gap 表示成一条 `Candidate → Verified → Novel` 成熟度链。至少分开三个维度：

1. **Origin｜来源**
   - `explicit`：作者明确指出 limitation、future work 或 unresolved problem；
   - `inferred`：分析者由论文内部可定位证据推导。
2. **Gap status｜缺口本身的支持状态**
   - `candidate`：合理但尚未充分核查；
   - `supported`：定向内部核查支持该缺口表述；
   - `contradicted`：决定性证据削弱/否定该缺口；
   - `unresolved`：现有证据无法决定。
3. **Novelty status｜外部新颖性状态**
   - `unchecked`；
   - `partially_checked`；
   - `no_close_prior_found`：在已记录的检索范围内未发现近似先前工作，不代表证明不存在；
   - `contradicted`：近似先前工作实质削弱新颖性前提；
   - `unclear`。

对于 **Inferred Gap**，至少保留：

`Observation + Evidence refs + Reasoning chain + Alternative explanations + Verification needed`

作者没做某个实验本身不等于可发表 Gap。`origin`、`gap_status`、`novelty_status` 回答不同问题，不得混成一条升级链。

### Candidate Idea

至少保留：

`观察 → Candidate Gap → 研究问题 → 假设 → 最小实验 → 可能贡献 → 风险`

更强的 Research Idea 需要足够的 Gap 支持，以及该主张所需的新颖性/可行性核查。新颖性检索必须报告范围和限制；“当前范围未发现近似工作”永远不等于证明不存在。

## 能防什么，不能防什么

PEM 重点防止摘要/结论过度表述、事实与解释混淆、用惯例填补未报告信息、窄证据宽外推、缺少关键对照/消融、跨章节矛盾、PDF 提示注入、来源混合、旧 Project 文件替换新论文、伪造定位/数值/引文、虚假全文覆盖、OVERREAD 和 IDEA_OVERPROMOTION。

它不能自动识别伪造原始数据、所有统计错误或无法读取的内容；没有外部证据时，也不能证明领域级新颖性。

## Prompt 与测试边界

`project-instructions.md` 是完整自适应契约；compact 版本保留最高价值的自适应与证据控制。Prompt 不能保证模型服从，因此需要分别测试 evidence fidelity 与 routing quality，人工检查决定性引用位置，并在记录模型/模式/日期的条件下重复实跑。
