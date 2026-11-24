<!-- 自动生成：仅修改 literature_catalog.yaml，再运行 scripts/generate_literature_navigation.py。 -->

# HTAM_EarthAgent：文献分类记录

| 字段 | 核查记录 |
|---|---|
| 完整英文标题 | Designing Domain-Specific Agents via Hierarchical Task Abstraction Mechanism |
| 仓库短名称 | HTAM_EarthAgent |
| 实际 Benchmark 名称 | GeoPlan-bench |
| 年份与平台 | 2025；arXiv预印本 v1 |
| 原文网址 | [官方原文](https://arxiv.org/abs/2511.17198v1) |
| 唯一主类别 | A |
| 阅读优先级 | P0 |
| 阅读优先级理由 | 审计关键工具集、语义加权编辑距离和Elo；限制结论为规划质量。 |
| 分类理由 | HTAM是框架、EarthAgent是系统，GeoPlan-bench是独立规划任务集；规划基准符合规范A纳入标准。 |
| 研究用途 | 直接审计对象：审计关键工具集、语义加权编辑距离和Elo；限制结论为规划质量。 |
| 辅助标签 | 规划路径；LLM Judge；轨迹匹配；模拟执行；Agent系统 |
| 主要测量对象 | 关键工具选择、参考计划结构、相对逻辑完整性 |
| 评价机制 | 关键P/R/F1、PathSimilarity/Structural、LLM成对比较Elo；mock返回 |
| Ground Truth 类型 | 生成/筛选参考路径、LLM关键集与全局工具依赖图 |
| 实证审计可行性 | R1 |
| 可行性依据 | 独立GeoPlan-bench测试目录、含ground_truth_tool_flow的样例JSON与correctness.py已取回；依赖、Judge和完整重放尚未测试。 |
| 开源状态 | GeoPlan-bench任务/GT和metrics源码可访问；EarthAgent母仓库仅说明并推迟系统代码，二者不混同。 |
| 原文证据位置 | 摘要p1；§5 pp7–8；补充7.2/8.1–2 PDF12–15；10.3 PDF61 |
| 核验状态 | 原文定向核验（分类所需章节）；非代码/实验复现 |
| 原文核验范围 | 英文摘要；方法/任务与数据构建；评价机制/指标；实验或系统案例；讨论、局限或结论边界 |
| 重点阅读章节 | 补充8.2关键P/R两个分母；归一上界/中心性；Elo初值/K/顺序；主评996与训练248。 |
| 局限与研究边界 | 主评不依赖真实工具成功；真实系统演示不等于基准产物验证；启发式归一与Elo配置未完全给定。 |
| 归档英文页数 | 69 |
| 核验日期 | 2026-11-24 |
| 实际目录 | [论文翻译/HTAM_EarthAgent](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent) |

## 阅读材料

| 材料 | 入口 / 状态 |
|---|---|
| 中文主入口及范围 | [摘要与章节译述（非逐句全文）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87_%E4%B8%BB%E6%96%87.md) |
| 其他中文稿及范围 | [补充材料译述（非逐句全文）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/%E4%B8%AD%E6%96%87%E5%AD%A6%E6%9C%AF%E8%AF%91%E7%A8%BF_%E4%B8%BB%E6%96%87%E4%B8%8E%E8%A1%A5%E5%85%85%E6%9D%90%E6%96%99.md) · [摘要与章节译述（非逐句全文）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87_%E4%B8%BB%E6%96%87.md) · [补充材料译述（非逐句全文）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87_%E8%A1%A5%E5%85%85%E6%9D%90%E6%96%99.md) |
| 英文原文 | [本地原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) · [官方](https://arxiv.org/abs/2511.17198v1)；完整英文原文/逐页提取稿（以归档原文为准） |
| PDF | [PDF](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| 图表与原页 | [图表/原页](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/%E5%9B%BE%E8%A1%A8%E7%B4%A2%E5%BC%95.md) |
| 核查报告 | [核查1](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/QA_%E9%80%90%E9%A1%B5%E6%A0%B8%E6%9F%A5%E6%8A%A5%E5%91%8A.md) · [核查2](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/%E9%80%90%E9%A1%B5%E5%9B%BE%E5%83%8F%E6%A0%A1%E5%AF%B9.md) |
| 阅读说明 | [阅读说明](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/README_%E9%98%85%E8%AF%BB%E8%AF%B4%E6%98%8E.md) |
| 用于核验的本地原文 | [归档原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |

## 原文核验与研究判断

论文事实：标题、任务/Benchmark定位、测量对象、评价机制及 GT 摘要来自上列英文原文位置；测量对象字段概括评价操作，不把局部得分外推为完整地学能力。

研究判断：分类理由、研究用途、阅读优先级与阅读问题依据 v1.0 和当前研究方向确定；阅读问题用于后续核验，不表示已经发现评价缺陷。局限记录区分作者范围说明与本研究尚缺的证据。

## 实证条件分项检查

| 条件 | 实际核查状态 |
|---|---|
| 任务集 | test_tasks实际目录可访问 |
| GT | 读取样例JSON的ground_truth_tool_flow |
| 参考轨迹 | 样例含参考工具flow；主评是规划 |
| 输出产物 | 未核查 |
| 评价器源码 | metrics/correctness.py已取回；structural/holistic文件目录可见 |
| 执行环境 | 未安装依赖；mock规划，不是真实遥感执行 |
| API依赖 | LLM关键集/Judge依赖未验证 |
| 固定轨迹重复评分 | 未核查 |
| 对照样本构造 | 未核查 |
| 独立人工核验 | 未核查 |

## 开源证据阶段

| 阶段 | 状态 |
|---|---|
| 1 作者声明 | 项目说明指向独立GeoPlan-bench库 |
| 2 提供链接 | https://github.com/earth-insights/GeoPlan-bench |
| 3 实际可访问 | 任务目录、样例GT和评价模块已实际请求 |
| 4 文件已下载 | 小型样例与源码保存于工作缓存；未下载全库 |
| 5 已验证运行 | 未运行 |

## 译稿范围声明摘录

以下为现有中文稿开头，用于判断译稿范围，不用作英文研究结论的证据。

```text
# 通过层次化任务抽象机制设计领域专用智能体

**英文题名：** Designing Domain-Specific Agents via Hierarchical Task Abstraction Mechanism  
**作者：** Kaiyu Li, Jiayu Wang, Zhi Wang, Hui Qiao, Weizhan Zhang, Deyu Meng, Xiangyong Cao  
**机构：** 西安交通大学；中国电信陕西分公司  
**预印本：** arXiv:2511.17198v1（2025 年 11 月 21 日）  
**项目：** https://earth-insights.github.io/EarthAgent  
**通讯作者：** Xiangyong Cao（caoxiangyong@mail.xjtu.edu.cn）

> 本文提出的 **EarthAgent** 与另一篇《Earth-Agent: Unlocking the Full Landscape of Earth Observation with Agents》是不同的系统，作者在原论文补充材料第12节专门解释同名差异。**HTAM** = Hierarchical Task Abstraction Mechanism（层次化任务抽象机制）；**GeoPlan-bench** 是本文用于规划能力比较的基准；全文“工具调用路径”不等同于真实工具执行轨迹。

## 摘要

由大语言模型驱动的智能体，尤其是采用 ReAct 等通用框架或模拟人类社会角色协作的架构，在需要严格结构化流程的专门领域往往表现不佳。例如遥感分析既需要辐射校正、光谱指数计算等专业工具，也涉及多个中间产物、可选步骤和复杂的先后次序，对通用智能体提出很大挑战。为弥合这一差距，作者提出以**层次化任务抽象机制（HTAM）**为核心的新型智能体设计框架。HTAM 不再按照人类职业角色组织协作，而是依据目标领域本身的任务依赖图，将多智能体组织为符合问题求解逻辑的层级架构。复杂问题被拆为若干依次衔接的功能层，上层依赖下层处理结果，从结构上约束过程正确性。

作者将该方法实现为面向复杂地理空间分析的多智能体系统 **EarthAgent**，并提出 **GeoPlan-bench**，以真实的多步骤地理空间规划问题检验智能体对任务的分解与规划能力。论文设计了工具选择正确性、路径结构相似度和逻辑完整性等多维指标，比较了多种单智能体与多智能体架构。结果显示，EarthAgent 在多个评测维度上显著优于基线系统。研究强调：**让智能体架构与专业领域固有的任务结构相匹配，是构建稳健、可靠的专用自治系统的重要条件**。

## 1 引言

近年来，大语言模型在推理、规划和工具交互方面的进步推动了自治智能
```

[返回文献总索引](../../%E6%96%87%E7%8C%AE%E6%80%BB%E7%B4%A2%E5%BC%95.md)
