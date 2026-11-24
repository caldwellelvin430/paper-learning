<!-- 自动生成：仅修改 literature_catalog.yaml，再运行 scripts/generate_literature_navigation.py。 -->

# GeoAnalystBench：文献分类记录

| 字段 | 核查记录 |
|---|---|
| 完整英文标题 | GeoAnalystBench: A GeoAI Benchmark for Assessing Large Language Models for Spatial Analysis Workflow and Code Generation |
| 仓库短名称 | GeoAnalystBench |
| 实际 Benchmark 名称 | GeoAnalystBench |
| 年份与平台 | 2025；Transactions in GIS 29(7), e70135 |
| 原文网址 | [官方原文](https://doi.org/10.1111/tgis.70135) |
| 唯一主类别 | A |
| 阅读优先级 | P0 |
| 阅读优先级理由 | 用作工作流/代码相似度与真实地学正确性脱钩的核心对照。 |
| 分类理由 | 50项空间分析任务评价工作流和代码；虽侧重静态生成，按规范明确示例保留A，并标记与动态执行不同。 |
| 研究用途 | 直接审计对象：用作工作流/代码相似度与真实地学正确性脱钩的核心对照。 |
| 辅助标签 | 代码生成；工作流；代码相似度；参考代码；局部测量 |
| 主要测量对象 | 工作流有效性、长度/文本接近与代码表示相似 |
| 评价机制 | VR、MAD、MiniLM余弦TS、CodeBLEU(0.2/0.2/0.3/0.3)及4组件 |
| Ground Truth 类型 | GIS专家验证的人工/ModelBuilder工作流和Python代码 |
| 实证审计可行性 | RU |
| 可行性依据 | 官方dataset CSV与codes目录可访问，但完整评分器、人工VR规则和执行条件链未核实。 |
| 开源状态 | 部分声明/目录在Task02核查；官方dataset CSV与codes目录可访问，但完整评分器、人工VR规则和执行条件链未核实。未下载完整实验资产，未运行。 |
| 原文证据位置 | 摘要p1；构建§3 pp4–7；评价§4 pp7–8；表3 p10；局限§8 p16 |
| 核验状态 | 原文定向核验（分类所需章节）；非代码/实验复现 |
| 原文核验范围 | 英文摘要；方法/任务与数据构建；评价机制/指标；实验或系统案例；讨论、局限或结论边界 |
| 重点阅读章节 | §4.1人工有效性规则与欠说明参数；§4.2 AST/data-flow分含义；§5表3；候选是否真正执行。 |
| 局限与研究边界 | 线性工作流及任务覆盖、公开语料污染等限制；本地未取得独立Supporting Information，不声称附件全覆盖。 |
| 归档英文页数 | 18 |
| 核验日期 | 2026-11-24 |
| 实际目录 | [论文翻译/GeoAnalystBench](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench) |

## 阅读材料

| 材料 | 入口 / 状态 |
|---|---|
| 中文主入口及范围 | [章节中文译稿（未认定全文覆盖）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87_%E5%85%A8%E6%96%87.md) |
| 其他中文稿及范围 | [章节中文译稿（未认定全文覆盖）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87_%E5%85%A8%E6%96%87.md) |
| 英文原文 | [本地原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) · [官方](https://doi.org/10.1111/tgis.70135)；完整英文原文/逐页提取稿（以归档原文为准） |
| PDF | [PDF](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| 图表与原页 | [图表/原页](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench/%E5%9B%BE%E8%A1%A8%E7%B4%A2%E5%BC%95.md) |
| 核查报告 | [核查1](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench/QA_%E9%80%90%E9%A1%B5%E6%A0%B8%E6%9F%A5%E6%8A%A5%E5%91%8A.md) · [核查2](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench/%E9%80%90%E9%A1%B5%E5%9B%BE%E5%83%8F%E6%A0%A1%E5%AF%B9.md) |
| 阅读说明 | [阅读说明](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench/README_%E9%98%85%E8%AF%BB%E8%AF%B4%E6%98%8E.md) |
| 用于核验的本地原文 | [归档原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |

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
| 1 作者声明 | 原文有公开承诺或链接 |
| 2 提供链接 | https://github.com/GeoDS/GeoAnalystBench |
| 3 实际可访问 | 仅Task02记录范围；完整资产链未确认 |
| 4 文件已下载 | 未核查实验资产；本地论文存在不等于资产下载 |
| 5 已验证运行 | 未运行 |

## 译稿范围声明摘录

以下为现有中文稿开头，用于判断译稿范围，不用作英文研究结论的证据。

```text
# GeoAnalystBench：评估大语言模型空间分析工作流与代码生成能力的 GeoAI 基准

**作者：** Qianheng Zhang, Song Gao, Chen Wei, Yibo Zhao, Ying Nie, Ziru Chen, Shijie Chen, Yu Su, Huan Sun  
**机构：** 美国威斯康星大学麦迪逊分校地理系 GeoDS Lab；俄亥俄州立大学计算机科学与工程系  
**期刊：** *Transactions in GIS*，2025，29:e70135  
**DOI：** https://doi.org/10.1111/tgis.70135  
**收稿／修订／录用：** 2025-03-04／2025-08-25／2025-09-29  
**通讯作者：** Song Gao（song.gao@wisc.edu）  
**资助：** 美国国家科学基金会，项目号 2112606  
**开源数据：** https://github.com/GeoDS/GeoAnalystBench

> 术语采用“空间分析／地理处理（spatial analysis/geoprocessing）”“有效率（valid rate, VR）”“工作流长度平均绝对偏差（MAD）”“文本相似度（TS）”“领域知识（DK）”“数据集描述（DD）”“代码 BLEU（CodeBLEU）”等标准写法。此处保留英文论文原始数字、模型版本、代码、公式及图表，供交叉核对。

## 摘要

大语言模型（LLM）的进步推动了自动化地理空间分析和 GIS 工作流的研究，但模型的实际能力仍不确定。作者主张，在宣称实现全面 GIS 自动化之前，应当先用明确定义的地理处理任务进行严格评价。为此，本文提出 **GeoAnalystBench**：一个由 GIS 专家验证的基准，包含从真实世界地理空间问题提炼的 **50 项 Python 任务**。每个任务配有最低限度的交付成果，评估内容包括工作流有效性、结构一致性、语义相似度和代码质量（CodeBLEU）。研究测试了闭源与开源模型，发现显著差距：ChatGPT-4o-mini 等商业模型的工作流有效率可达 **95%**，CodeBLEU 为 **0.39**；DeepSeek-R1-7B 等较小开源模型经常生成不完整或不一致的工作流（有效率 **48.5%**，CodeBLEU **0.272**）。深度空间推理任务，例如空间关系判断和最优选址，对所有模型都最具挑战性。结果既展示了现阶段 LLM 在 GIS 自动化方面的潜力与局限，也为包含人类专家参与的 GeoAI 研究提供了可复现的评价框架。

**关键词：** 基准测试；GeoAI；语言智能体；大语言模型；空间分析。

## 1 引言

生成式
```

[返回文献总索引](../../%E6%96%87%E7%8C%AE%E6%80%BB%E7%B4%A2%E5%BC%95.md)
