# Task02：地学Benchmark评价指标体系

日期：2026-11-24。依据已校验的paper-learning-local快照开展；仅新增此任务目录，未修改论文、Task01成果或原分类，没有git push。

覆盖9个对象，完成129条指标/统计记录：正式能力53条（主报告口径40，组件13），辅助诊断40，效率成本数据特征30，Benchmark元评价6。正式数量包含协议变体与组件，不是53个去重的新能力或可相加评分。

- [基础信息矩阵](01_Benchmark基础信息矩阵.csv)与[完整指标台账](02_完整评价指标汇总.csv)：筛选metric_class及metric_role后再统计。
- [指标定义与公式](03_评价指标定义与公式.md)与[分类规则](04_评价指标分类体系.md)：保留公式来源及未报告实现。
- [维度覆盖](05_Benchmark评价维度覆盖矩阵.csv)与[评价器机制](06_评价器类型对照矩阵.csv)：每格D/I/N/U旁有证据，不把U作N。
- [构念效度逐项分析](07_构念效度与测量对象分析.md)、[风险台账](08_候选评价缺陷与风险假设.csv)、[资源盘点](09_开源资源初步盘点.csv)。
- [研究发现与下一阶段建议](10_研究发现与下一阶段建议.md)回答指标、同名异义、覆盖缺口与审计队列；[验收报告](QA_Task02_验收报告.md)记录实际检查及未完成的复现范围。

## 逐篇入口

- [GeoAgentBench](Benchmark独立分析/GeoAgentBench.md)
- [GISAgentBench](Benchmark独立分析/GISAgentBench.md)
- [GeoNatureAgent](Benchmark独立分析/GeoNatureAgent.md)
- [GeoContra](Benchmark独立分析/GeoContra.md)
- [GeoBenchX](Benchmark独立分析/GeoBenchX.md)
- [GeoAnalystBench](Benchmark独立分析/GeoAnalystBench.md)
- [ThinkGeo](Benchmark独立分析/ThinkGeo.md)
- [GeoPlan-bench](Benchmark独立分析/GeoPlan-bench.md)
- [GeoLLM-Engine](Benchmark独立分析/GeoLLM-Engine.md)

## 批次验收

- [第一批](批次验收/第一批_QA.md)：GeoAgentBench、GISAgentBench、GeoNatureAgent。
- [第二批](批次验收/第二批_QA.md)：GeoContra、GeoBenchX、GeoAnalystBench。
- [第三批](批次验收/第三批_QA.md)：ThinkGeo、HTAM_EarthAgent中的GeoPlan-bench、GeoLLM-Engine。

## 证据与使用约定

`source_page`使用PDF物理页；GeoPlan补充重新从1编号，不能混用。部分论文没有本地PDF时，使用带原PDF页码及页面图像的英文逐页稿。所有论文事实可经每篇独立分析的相对链接回到原文；公式关键括号用原页图像核对。CSV为UTF-8 BOM，英文定义为转述，evidence为摘要/定位而非虚构逐字引文。

论文事实写在定义/来源；分类、构念解释与实验队列是本次分析；C级风险为待验证假设；A是作者陈述，不能当本研究已复现。B本次无独立验证条目。D是信息不足，不等于无缺陷或有缺陷。资源状态截至本日期：仅元数据/README低成本读取，无新任务资产或评分器安装运行。

前置阅读包括Task01八项交付，以及00_研究背景与目标、01_文献总索引、02_核心文献阅读顺序、03_文献分类调整记录和原研究框架README/验收。Task01的固定轨迹、独立标签、合法替代与Judge随机性分离方法在风险实验设计中沿用；不将其通用失败案例直接判为这9个地学实现的已有问题。
