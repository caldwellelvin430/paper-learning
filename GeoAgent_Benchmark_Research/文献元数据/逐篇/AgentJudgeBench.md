<!-- 自动生成：仅修改 literature_catalog.yaml，再运行 scripts/generate_literature_navigation.py。 -->

# AgentJudgeBench：文献分类记录

| 字段 | 核查记录 |
|---|---|
| 完整英文标题 | AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling |
| 仓库短名称 | AgentJudgeBench |
| 实际 Benchmark 名称 | AgentJudgeBench |
| 年份与平台 | 2026；arXiv预印本 v1 |
| 原文网址 | [官方原文](https://arxiv.org/abs/2608.26623v1) |
| 唯一主类别 | B |
| 阅读优先级 | P1 |
| 阅读优先级理由 | 借鉴固定GT、难度/拓扑分层、with/without-GT及programmatic与人工标签的多级校准。 |
| 分类理由 | 直接评价LLM裁判在工作流DAG上的可靠性，虽是Benchmark，主要测量对象是Judge而非Agent能力。 |
| 研究用途 | 方法借鉴；创新性对照：借鉴固定GT、难度/拓扑分层、with/without-GT及programmatic与人工标签的多级校准。 |
| 辅助标签 | LLM Judge；元评价；工作流DAG；评分稳定性；GT暴露 |
| 主要测量对象 | Judge对工具选择、参数键结构、位置顺序、query覆盖的alignment |
| 评价机制 | 3808合成记录；确定性四指标参考；LLM paired verdict；人工120记录验证与bootstrap |
| Ground Truth 类型 | schema/trace程序验证的参考；120条人工核对（非全部人标） |
| 实证审计可行性 | RU |
| 可行性依据 | 尚未核查任务、GT、评价器与必要环境的完整可用链，不凭论文公开声明评级 |
| 开源状态 | 代码、任务/数据、GT、评分器和环境的当前完整可用链尚未核查；RU或N/A不由论文链接自动升级；未运行。 |
| 原文证据位置 | 摘要p1；§3 pp4–6；§4 pp6–9；Limitations/附录A/G；格式附录W |
| 核验状态 | 原文定向核验（分类所需章节）；非代码/实验复现 |
| 原文核验范围 | 英文摘要；方法/任务与数据构建；评价机制/指标；实验或系统案例；讨论、局限或结论边界 |
| 重点阅读章节 | §3.1 GT验证与难度改写；§3.2四指标/空序列；§4 paired协议；Limitations及附录G。 |
| 局限与研究边界 | 合成静态记录不等于真实多轮执行；中等难度校准不充分；Judge-only重跑研究仍是未来工作。 |
| 归档英文页数 | 31 |
| 核验日期 | 2026-11-24 |
| 实际目录 | [论文翻译/AgentJudgeBench](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentJudgeBench) |

## 阅读材料

| 材料 | 入口 / 状态 |
|---|---|
| 中文主入口及范围 | [中文精读/核心译述（非全文）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentJudgeBench/AgentJudgeBench_%E4%B8%AD%E6%96%87%E7%B2%BE%E8%AF%BB%E4%B8%8E%E6%A0%B8%E5%BF%83%E5%86%85%E5%AE%B9%E8%AF%91%E8%BF%B0.md) |
| 其他中文稿及范围 | [中文精读/核心译述（非全文）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentJudgeBench/AgentJudgeBench_%E4%B8%AD%E6%96%87%E7%B2%BE%E8%AF%BB%E4%B8%8E%E6%A0%B8%E5%BF%83%E5%86%85%E5%AE%B9%E8%AF%91%E8%BF%B0.md) |
| 英文原文 | [本地原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentJudgeBench/AgentJudgeBench_%E8%8B%B1%E6%96%87%E5%85%A8%E6%96%87%E9%80%90%E9%A1%B5%E6%8F%90%E5%8F%96.md) · [官方](https://arxiv.org/abs/2608.26623v1)；完整英文原文/逐页提取稿（以归档原文为准） |
| PDF | 本地原始 PDF 缺失（见官方原文） |
| 图表与原页 | [图表/原页1](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentJudgeBench/images) · [图表/原页2](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentJudgeBench/source_pages) |
| 核查报告 | [核查](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentJudgeBench/QA_%E9%80%90%E9%A1%B5%E4%B8%8E%E5%9B%BE%E7%89%87%E5%BC%95%E7%94%A8%E6%A0%B8%E6%9F%A5.md) |
| 阅读说明 | [阅读说明](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentJudgeBench/README_%E5%85%88%E8%AF%BB.md) |
| 用于核验的本地原文 | [归档原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentJudgeBench/AgentJudgeBench_%E8%8B%B1%E6%96%87%E5%85%A8%E6%96%87%E9%80%90%E9%A1%B5%E6%8F%90%E5%8F%96.md) |

## 原文核验与研究判断

论文事实：标题、任务/Benchmark定位、测量对象、评价机制及 GT 摘要来自上列英文原文位置；测量对象字段概括评价操作，不把局部得分外推为完整地学能力。

研究判断：分类理由、研究用途、阅读优先级与阅读问题依据 v1.0 和当前研究方向确定；阅读问题用于后续核验，不表示已经发现评价缺陷。局限记录区分作者范围说明与本研究尚缺的证据。

## 实证条件分项检查

| 条件 | 实际核查状态 |
|---|---|
| 任务集 | 未核查 |
| GT | 未核查 |
| 参考轨迹 | 未核查 |
| 输出产物 | 未核查 |
| 评价器源码 | 未核查 |
| 执行环境 | 未核查 |
| API依赖 | 未核查 |
| 固定轨迹重复评分 | 未核查 |
| 对照样本构造 | 未核查 |
| 独立人工核验 | 未核查 |

## 开源证据阶段

| 阶段 | 状态 |
|---|---|
| 1 作者声明 | 原文给出资源入口，未独立确认所有资产可用 |
| 2 提供链接 | https://huggingface.co/datasets/ServiceNow-AI/AgentJudgeBench |
| 3 实际可访问 | 未核查 |
| 4 文件已下载 | 未核查实验资产；本地论文存在不等于资产下载 |
| 5 已验证运行 | 未运行 |

## 译稿范围声明摘录

以下为现有中文稿开头，用于判断译稿范围，不用作英文研究结论的证据。

```text
# AgentJudgeBench：面向智能体工具调用的多难度 LLM 评判器基准

**原题**：*AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling*  
**作者**：Abhigya Verma、Amit Kumar Saha、Seganrasan Subramanian、Sai Harshitha Aluru  
**机构**：ServiceNow AI  
**版本**：arXiv:2608.26623v1，2026-08-27  
**原稿页数**：31 页。

> **译稿性质**：下文包含摘要的完整中文翻译和论文正文、方法、关键实验、局限及附录的详尽中文学术译述，**并非每一页逐句完整翻译**。特别是附录中的全部数值表、评分提示词和英文参考文献，已在 `AgentJudgeBench_英文全文逐页提取.md` 中逐页保留，`source_pages/` 保存 31 页原稿图像，便于核对。所有模型名、函数、符号和原始数据不做推测性修正。

## 摘要（完整翻译）

大型语言模型（LLM）评判器已广泛用于评估智能体工具调用系统，但它们在**结构化、由依赖关系驱动的工作流**中的可靠性仍很少受到检验。本文提出 **AgentJudgeBench**，据作者所知，这是首个系统研究 LLM-as-a-judge 在工作流有向无环图（DAG）结构的智能体工具调用场景中可靠性的基准，其研究对象不同于开放式文本或偏好判断等更广义的 LLM-as-a-judge 任务。该基准包含 **3,808 个实例**，覆盖六种 DAG 拓扑结构与三个难度等级；评估涉及五个生成器（包括 3B–70B 的开放权重模型及 GPT-5.4）和六个评判器（从 20B 到前沿规模），并分别设置**提供与不提供 Ground Truth（GT）**的成对条件。评判器与程序化参考结果的一致性随任务难度增加而单调下降，且在没有 GT 时下降速度快 **1.5 倍**。对于困难任务，在不提供 GT 时，无论模型规模如何，所有六个评判器的一致性均收敛到狭窄的 **77%–82%** 区间，显示出一个主要由任务难度驱动、但对较弱生成器而言其高度也部分依赖提示词的结构性上限；仅扩大模型能力无法消除这一上限。暴露 GT 并非总是有益：GPT-5.4 的一致性下降 **1.5 个百分点**，Gemini-2.5-Pro 下降 **3.9 个百分点**，与过度锚定（over-anchoring）现象一致。缓解手段方面，思维链推理和评判器温度几乎没有影响；结构化评价细则最多可提高 **6.5 个百分点**，但这种收益不会稳定地推广到所有评判器—生成器组合。存在 GT
```

[返回文献总索引](../../%E6%96%87%E7%8C%AE%E6%80%BB%E7%B4%A2%E5%BC%95.md)
