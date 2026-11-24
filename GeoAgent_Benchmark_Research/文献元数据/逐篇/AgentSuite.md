<!-- 自动生成：仅修改 literature_catalog.yaml，再运行 scripts/generate_literature_navigation.py。 -->

# AgentSuite：文献分类记录

| 字段 | 核查记录 |
|---|---|
| 完整英文标题 | AgentSuite: Toward More Reliable Agent Evaluation with a Component-Based Benchmark Auditing Pipeline |
| 仓库短名称 | AgentSuite |
| 实际 Benchmark 名称 | N/A（COBA审计管线与AgentSuite运行平台） |
| 年份与平台 | 2026；ICML 2026, PMLR 306 |
| 原文网址 | [官方原文](https://proceedings.mlr.press/v306/suh26a.html) |
| 唯一主类别 | B |
| 阅读优先级 | P0 |
| 阅读优先级理由 | 为地学任务的组件化记录、规则+语义审查及误报复核提供直接方法对照。 |
| 分类理由 | 把任务分成User/Environment/GT/Evaluation并检测组件间缺陷，主贡献是评价审计方法。 |
| 研究用途 | 方法借鉴；创新性对照：为地学任务的组件化记录、规则+语义审查及误报复核提供直接方法对照。 |
| 辅助标签 | 元评价；组件审计；LLM Judge；人工审计；创新性对照 |
| 主要测量对象 | 任务组件缺陷检出及与专家标签一致性 |
| 评价机制 | COBA结构过滤+taxonomy-guided LLM+可选adversarial rebuttal；P/R/F1与后验复核 |
| Ground Truth 类型 | 专家三人独立标注和裁决；基准原任务组件/参考轨迹 |
| 实证审计可行性 | N/A |
| 可行性依据 | 方法或系统背景文献，当前不作为独立实证审计对象 |
| 开源状态 | 代码、任务/数据、GT、评分器和环境的当前完整可用链尚未核查；RU或N/A不由论文链接自动升级；未运行。 |
| 原文证据位置 | 摘要p1；§2 pp2–3；§3 pp3–5；§4 pp5–8；局限p9 |
| 核验状态 | 原文定向核验（分类所需章节）；非代码/实验复现 |
| 原文核验范围 | 英文摘要；方法/任务与数据构建；评价机制/指标；实验或系统案例；讨论、局限或结论边界 |
| 重点阅读章节 | §3四组件映射；§4.1平衡子集与全量flag复核的分母；§4.3未见基准泛化；附录Judge消融。 |
| 局限与研究边界 | 作者承认taxonomy不穷尽、LLM偏差与清理后任务非无错保证；结构规则不在人工alignment评估分母。 |
| 归档英文页数 | 20 |
| 核验日期 | 2026-11-24 |
| 实际目录 | [论文翻译/AgentSuite](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentSuite) |

## 阅读材料

| 材料 | 入口 / 状态 |
|---|---|
| 中文主入口及范围 | [章节中文译稿（未认定全文覆盖）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentSuite/AgentSuite_%E4%B8%AD%E6%96%87%E5%85%A8%E6%96%87.md) |
| 其他中文稿及范围 | [章节中文译稿（未认定全文覆盖）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentSuite/AgentSuite_%E4%B8%AD%E6%96%87%E5%85%A8%E6%96%87.md) |
| 英文原文 | [本地原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentSuite/AgentSuite_%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) · [官方](https://proceedings.mlr.press/v306/suh26a.html)；完整英文原文/逐页提取稿（以归档原文为准） |
| PDF | 本地原始 PDF 缺失（见官方原文） |
| 图表与原页 | [图表/原页1](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentSuite/images) · [图表/原页2](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentSuite/source_pages) |
| 核查报告 | [核查](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentSuite/QA_%E6%A0%B8%E6%9F%A5%E6%8A%A5%E5%91%8A.md) |
| 阅读说明 | [阅读说明](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentSuite/README.md) |
| 用于核验的本地原文 | [归档原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentSuite/AgentSuite_%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) |

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
| 2 提供链接 | https://github.com/Agent-Suite/AgentSuite |
| 3 实际可访问 | 未核查 |
| 4 文件已下载 | 未核查实验资产；本地论文存在不等于资产下载 |
| 5 已验证运行 | 未运行 |

## 译稿范围声明摘录

以下为现有中文稿开头，用于判断译稿范围，不用作英文研究结论的证据。

```text
# AgentSuite：利用基于组件的基准审计流水线实现更可靠的智能体评估

**原题**：*AgentSuite: Toward More Reliable Agent Evaluation with a Component-Based Benchmark Auditing Pipeline*  
**作者**：Hyewon Suh、Binfei Ji、Seojune Lee、Rishi Khare、Basit Khan、Hyunjun Kim、Tianyi Zhang、Venkat Krishna Srinivasan、Peter Belcak、Shizhe Diao、Pavlo Molchanov、Yingyan (Celine) Lin、Zhen Dong  
**机构**：佐治亚理工学院；NVIDIA；加州大学圣巴巴拉分校  
**会议**：第 43 届国际机器学习大会（ICML 2026），PMLR 第 306 卷，首尔  
**通讯作者**：Zhen Dong（zhend@nvidia.com；zhend@ucsb.edu）  
**项目**：https://github.com/Agent-Suite/AgentSuite

> **阅读与排版说明**：忠实保留论文中的组件缩写、评估公式、代码与接口、表中数值。引用文献的书目元数据以原文为准。所有图表均为原 PDF 裁切，必要时参见 `source_pages/` 中的 20 张逐页原稿截图及同目录的完整英文提取稿。

## 摘要

大语言模型（LLM）智能体能否得到可靠评价，在很大程度上取决于基准的**有效性**（benchmark validity）。然而，现代智能体基准常含有由用户指令、环境、工具、真实值轨迹和评估协议之间的交互引起的隐蔽缺陷。这些问题将模型自身错误与基准构造缺陷混淆，削弱了基于排行榜的模型比较的可信度。

本文提出 **COBA（COmponent-based Benchmark Auditing，基于组件的基准审计）**，一种自动化诊断与过滤智能体基准有效性问题的流水线。COBA 将智能体任务拆解为四个标准化组件：**用户（User）**、**环境（Environment）**、**真实值（Ground Truth）**和**评估（Evaluation）**，并结合基于规则的检测器与分类体系指导的 LLM 判断，将组件级问题分类体系落实为可执行的审计机制。在六个广泛使用的智能体基准上，COBA 与专家判断高度一致，F1 分数达到 **0.791–0.874**。它补充了对 τ²-bench 的人工核查，发现因基准复杂性而被人工遗漏的问题，并且只需极少调整即可泛化到此前未见过的基准。研究表明，基准缺陷广泛存在，并对评价结果产生实质影响，因此组件化审计为更可靠、可解释的
```

[返回文献总索引](../../%E6%96%87%E7%8C%AE%E6%80%BB%E7%B4%A2%E5%BC%95.md)
