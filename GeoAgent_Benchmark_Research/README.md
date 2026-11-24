<!-- 自动生成：仅修改 literature_catalog.yaml，再运行 scripts/generate_literature_navigation.py。 -->

# GeoAgent Benchmark 科研文献导航

以系统性综述为基础的地学Agent Benchmark评价有效性审计与评价方法研究。分类记录服务于研究设计、精读顺序与审计对象筛选；不将文献相关性视为可复现证据。

## 文献统计与分类

共 **61 篇论文**，对应 61 个论文目录；分类与优先级统计由统一 YAML 自动生成。最近核验：2026-11-24。

| 统计项 | 分布 |
|---|---|
| 主类别 | A：9；B：15；C：11；D：6；E：9；F：5；G：6 |
| 阅读优先级 | P0：21；P1：16；P2：16；P3：8 |
| 实证可行性（与阅读优先级独立） | R0：0；R1：3；R2：1；RU：35；N/A：22 |

原文核验指面向分类的摘要、方法、评价、实验及局限定向核验；不等于全部附录或源码已审计。中文入口注明译稿范围；文件名中的“全文”不作为全文覆盖证明。

| 类别 | 论文数量 | 研究用途 | 分类入口 |
|---|---|---|---|
| A｜核心地学 Benchmark | 9 | 直接提取工具、参数、工作流、执行及空间结果指标，建立核心审计对象池 | [分类与精读记录](A_%E6%A0%B8%E5%BF%83%E5%9C%B0%E5%AD%A6%20Benchmark/README.md) |
| B｜Benchmark 审计与方法论 | 15 | 借鉴构念效度、评价器审计、独立真值、故障注入与质量检查方法 | [分类与精读记录](B_Benchmark%20%E5%AE%A1%E8%AE%A1%E4%B8%8E%E7%A0%94%E7%A9%B6%E6%96%B9%E6%B3%95%E8%AE%BA/README.md) |
| C｜地学专项 Agent Benchmark | 11 | 补充灾害、地球观测、气候和天气任务，验证方法的领域适用范围 | [分类与精读记录](C_%E5%9C%B0%E5%AD%A6%E4%B8%93%E9%A1%B9%20Agent%20Benchmark/README.md) |
| D｜地学知识、感知与代码评测 | 6 | 区分静态知识、感知和代码生成能力与动态Agent工作流能力 | [分类与精读记录](D_%E5%9C%B0%E5%AD%A6%E7%9F%A5%E8%AF%86%E3%80%81%E6%84%9F%E7%9F%A5%E4%B8%8E%E4%BB%A3%E7%A0%81%E7%94%9F%E6%88%90%20Benchmark/README.md) |
| E｜通用 Agent Benchmark 与评分机制 | 9 | 借鉴状态、里程碑、部分得分、功能测试与重复试验评分机制 | [分类与精读记录](E_%E9%80%9A%E7%94%A8%20Agent%20Benchmark%20%E4%B8%8E%E8%AF%84%E4%BB%B7%E6%9C%BA%E5%88%B6/README.md) |
| F｜地学 Agent 系统与综述 | 5 | 整理系统架构、应用需求、研究背景及地学工具使用场景 | [分类与精读记录](F_%E5%9C%B0%E5%AD%A6%20Agent%20%E7%B3%BB%E7%BB%9F%E4%B8%8E%E7%BB%BC%E8%BF%B0/README.md) |
| G｜AI 与 Agent 基础文献 | 6 | 理解基础模型、推理行动循环、规划、记忆与感知工具 | [分类与精读记录](G_AI%20%E4%B8%8E%20Agent%20%E5%9F%BA%E7%A1%80%E6%96%87%E7%8C%AE/README.md) |

## 核心研究文献

| 论文名称 | 年份 | 阅读优先级 | 研究价值 | 中文译稿 | 英文原文 | PDF |
|---|---|---|---|---|---|---|
| [GeoAgentBench](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/GeoAgentBench.md) | 2026 | P0 | 比较参数末次尝试对齐、参考路径与地图VLM的测量边界。 | [正文译稿（代码/参考文献等保留英文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAgentBench/GeoAgentBench_%E4%B8%AD%E6%96%87%E5%85%A8%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAgentBench/GeoAgentBench_%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) · [官方](https://arxiv.org/abs/2604.13888v1) | 本地原始 PDF 缺失（见官方原文） |
| [GISAgentBench](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/GISAgentBench.md) | 2026 | P0 | 优先审查严格成功、部分接近度、容差与实体/行配对，而非按论文承诺认定可运行。 | [章节中文译稿（未认定全文覆盖）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GISAgentBench/GISAgentBench_%E4%B8%AD%E6%96%87%E5%85%A8%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GISAgentBench/GISAgentBench_%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E6%8F%90%E5%8F%96.md) · [官方](https://arxiv.org/abs/2608.01645v1) | 本地原始 PDF 缺失（见官方原文） |
| [GeoNatureAgent](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/GeoNatureAgent.md) | 2026 | P0 | 可冻结JSON、工具日志和答案，检查子串、数值窗口与v5/v6预算豁免。 | [章节中文译稿（未认定全文覆盖）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%AE%8C%E6%95%B4%E6%8F%90%E5%8F%96.md) · [官方](https://arxiv.org/abs/2610.09112v1) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [GeoContra](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/GeoContra.md) | 2026 | P0 | 明确“执行且过契约”与完整地学真值的差别，建立空间约束审计参照。 | [中文精读/核心译述（非全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoContra/GeoContra_%E4%B8%AD%E6%96%87%E7%B2%BE%E8%AF%BB%E4%B8%8E%E6%A0%B8%E5%BF%83%E5%86%85%E5%AE%B9%E8%AF%91%E8%BF%B0.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoContra/GeoContra_%E8%8B%B1%E6%96%87%E5%85%A8%E6%96%87%E9%80%90%E9%A1%B5%E6%8F%90%E5%8F%96.md) · [官方](https://arxiv.org/abs/2605.00782v1) | 本地原始 PDF 缺失（见官方原文） |
| [GeoBenchX](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/GeoBenchX.md) | 2025 | P0 | 审查拒绝任务、三Judge频率聚合、方案与最终交付之间的构念差别。 | [章节中文译稿（未认定全文覆盖）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoBenchX/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87_%E5%85%A8%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoBenchX/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) · [官方](https://doi.org/10.1145/3764915.3770721) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoBenchX/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [GeoAnalystBench](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/GeoAnalystBench.md) | 2025 | P0 | 用作工作流/代码相似度与真实地学正确性脱钩的核心对照。 | [章节中文译稿（未认定全文覆盖）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87_%E5%85%A8%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) · [官方](https://doi.org/10.1111/tgis.70135) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAnalystBench/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [ThinkGeo](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/ThinkGeo.md) | 2025 | P0 | 区分教师上下文局部accuracy、自由执行、答案Judge与图像grounding。 | [摘要与章节译述（非逐句全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ThinkGeo/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ThinkGeo/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) · [官方](https://arxiv.org/abs/2505.23752v3) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ThinkGeo/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [HTAM_EarthAgent](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/HTAM_EarthAgent.md) | 2025 | P0 | 审计关键工具集、语义加权编辑距离和Elo；限制结论为规划质量。 | [摘要与章节译述（非逐句全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87_%E4%B8%BB%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) · [官方](https://arxiv.org/abs/2511.17198v1) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/HTAM_EarthAgent/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [GeoLLM-Engine](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/GeoLLM-Engine.md) | 2024 | P0 | 比较调用正确率与最终成功，检查状态过约束和GT共识构建。 | [摘要全译＋主要章节译述（非全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoLLM-Engine/%E4%B8%AD%E6%96%87%E5%AD%A6%E6%9C%AF%E8%AF%91%E7%A8%BF_%E6%91%98%E8%A6%81%E4%B8%8E%E6%A0%B8%E5%BF%83%E7%AB%A0%E8%8A%82.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoLLM-Engine/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%85%A8%E6%96%87.md) · [官方](https://arxiv.org/abs/2404.15500) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoLLM-Engine/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |

## Benchmark 审计方法

核心对标：[Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/Benchmarking%20the%20Benchmarks.md)。

| 论文名称 | 年份 | 阅读优先级 | 研究价值 | 中文译稿 | 英文原文 | PDF |
|---|---|---|---|---|---|---|
| [Benchmarking the Benchmarks](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/Benchmarking%20the%20Benchmarks.md) | 2026 | P0 | 复用独立人工判据、固定轨迹重评分、失败归因与修复验证设计；先区分研究创新边界。 | [摘要与章节译述（非逐句全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Benchmarking%20the%20Benchmarks/%E4%B8%AD%E6%96%87%E5%85%A8%E6%96%87_%E4%B8%BB%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Benchmarking%20the%20Benchmarks/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) · [官方](https://arxiv.org/abs/2607.02577v1) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Benchmarking%20the%20Benchmarks/%E8%8B%B1%E6%96%87%E5%8E%9F%E8%AE%BA%E6%96%87.pdf) |
| [Measuring What Matters](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/Measuring%20What%20Matters.md) | 2025 | P0 | 用于建立提取codebook、双人核查和结论支持范围；不把局部指标直接判无效。 | [摘要与章节译述（非逐句全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Measuring%20What%20Matters/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Measuring%20What%20Matters/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%AE%8C%E6%95%B4%E6%8F%90%E5%8F%96.md) · [官方](https://arxiv.org/abs/2511.04703) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Measuring%20What%20Matters/original.pdf) |
| [Oracle Failures](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/Oracle%20Failures.md) | 2026 | P0 | 优先迁移状态污染/重置检查与固定结果离线重放，避免把语言配置效应误当普遍能力。 | [摘要与章节译述（非逐句全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Oracle%20Failures/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Oracle%20Failures/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%AE%8C%E6%95%B4%E6%8F%90%E5%8F%96.md) · [官方](https://arxiv.org/abs/2610.16067v2) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Oracle%20Failures/original.pdf) |
| [AgentSuite](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/AgentSuite.md) | 2026 | P0 | 为地学任务的组件化记录、规则+语义审查及误报复核提供直接方法对照。 | [章节中文译稿（未认定全文覆盖）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentSuite/AgentSuite_%E4%B8%AD%E6%96%87%E5%85%A8%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentSuite/AgentSuite_%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) · [官方](https://proceedings.mlr.press/v306/suh26a.html) | 本地原始 PDF 缺失（见官方原文） |
| [Beyond the Final Answer](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/Beyond%20the%20Final%20Answer.md) | 2026 | P0 | 研究无唯一参考路径时如何审计过程；区分reference-free运行评分与有标签元评价。 | [中文精读/核心译述（非全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Beyond%20the%20Final%20Answer/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87%E4%B8%8E%E7%B2%BE%E8%AF%BB.md) | [本地摘要](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Beyond%20the%20Final%20Answer/%E8%8B%B1%E6%96%87%E6%91%98%E8%A6%81_%E5%8E%9F%E6%96%87.md) · [官方](https://proceedings.mlr.press/v306/kim26bg.html) | 本地原始 PDF 缺失（见官方原文） |
| [ABC](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/ABC.md) | 2025 | P0 | 把任务能否代表能力与正评分能否代表任务成功分开；借鉴known-answer/测试完整性对照。 | [摘要与章节译述（非逐句全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ABC/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ABC/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%AE%8C%E6%95%B4%E6%8F%90%E5%8F%96.md) · [官方](https://arxiv.org/abs/2507.02825) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ABC/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [Agent-as-a-Judge](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/Agent-as-a-Judge.md) | 2025 | P0 | 借鉴工作区取证、依赖要求和人类共识对照；比较聚合Judge Shift与逐要求Alignment，关注类别不平衡导致的解释边界。 | [摘要全译＋关键段落节译（非全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Agent-as-a-Judge/%E4%B8%AD%E6%96%87%E8%AF%91%E7%A8%BF_%E6%91%98%E8%A6%81%E5%85%A8%E8%AF%91%E4%B8%8E%E5%85%B3%E9%94%AE%E6%AE%B5%E8%90%BD%E8%8A%82%E8%AF%91.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Agent-as-a-Judge/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%85%A8%E6%96%87%E4%B8%8E%E9%85%8D%E5%9B%BE.md) · [官方](https://proceedings.mlr.press/v267/zhuge25a.html) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Agent-as-a-Judge/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [AgentProcessBench](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/AgentProcessBench.md) | 2026 | P0 | 借鉴中性探索标签、首错定位和双人标注；核查微平均步骤一致率与轨迹级首错准确率的不同权重及fail-fast偏差。 | [摘要全译＋关键段落节译（非全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentProcessBench/%E4%B8%AD%E6%96%87%E8%AF%91%E7%A8%BF_%E6%91%98%E8%A6%81%E5%85%A8%E8%AF%91%E4%B8%8E%E5%85%B3%E9%94%AE%E6%AE%B5%E8%90%BD%E8%8A%82%E8%AF%91.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentProcessBench/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%85%A8%E6%96%87%E4%B8%8E%E9%85%8D%E5%9B%BE.md) · [官方](https://doi.org/10.1145/3770855.3817494) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentProcessBench/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [RuVerBench](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/RuVerBench.md) | 2026 | P0 | 借鉴先固定被评输出、再比较prompt/batch/voting的设计；用分类平衡准确率处理正负标签不平衡，记录排除歧义rubric后的适用范围。 | [摘要全译＋关键段落节译（非全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/RuVerBench/%E4%B8%AD%E6%96%87%E8%AF%91%E7%A8%BF_%E6%91%98%E8%A6%81%E5%85%A8%E8%AF%91%E4%B8%8E%E5%85%B3%E9%94%AE%E6%AE%B5%E8%90%BD%E8%8A%82%E8%AF%91.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/RuVerBench/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%85%A8%E6%96%87%E4%B8%8E%E9%85%8D%E5%9B%BE.md) · [官方](https://aclanthology.org/2026.emnlp-main.2192/) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/RuVerBench/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [Protocol_Validity_HackDetect](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/Protocol_Validity_HackDetect.md) | 2026 | P0 | 借鉴Expose→Exploit→Mislead可归因证据链及成对分数比较，防止把可疑动作直接标成作弊；区分预选可疑样本与总体缺陷率。 | [摘要全译＋关键段落节译（非全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Protocol_Validity_HackDetect/%E4%B8%AD%E6%96%87%E8%AF%91%E7%A8%BF_%E6%91%98%E8%A6%81%E5%85%A8%E8%AF%91%E4%B8%8E%E5%85%B3%E9%94%AE%E6%AE%B5%E8%90%BD%E8%8A%82%E8%AF%91.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Protocol_Validity_HackDetect/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%85%A8%E6%96%87%E4%B8%8E%E9%85%8D%E5%9B%BE.md) · [官方](https://arxiv.org/abs/2607.22368) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Protocol_Validity_HackDetect/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [SCIRIGOR](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/SCIRIGOR.md) | 2026 | P0 | 比较“自己的结果与自己的主张一致”与“独立科学目标正确”；借鉴替代完整路径、独立数值oracle及最早断链定位，避免把流畅解释当作正确证据。 | [摘要全译＋关键段落节译（非全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/SCIRIGOR/%E4%B8%AD%E6%96%87%E8%AF%91%E7%A8%BF_%E6%91%98%E8%A6%81%E5%85%A8%E8%AF%91%E4%B8%8E%E5%85%B3%E9%94%AE%E6%AE%B5%E8%90%BD%E8%8A%82%E8%AF%91.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/SCIRIGOR/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%85%A8%E6%96%87%E4%B8%8E%E9%85%8D%E5%9B%BE.md) · [官方](https://arxiv.org/abs/2609.06192) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/SCIRIGOR/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [Double_Measurement_Confound](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/Double_Measurement_Confound.md) | 2026 | P0 | 借鉴同任务2×2干预、正确/伪造/空提交探针与固定种子重放；学习如何区分确认性空结果、探索性跟进及资源配额耦合，限制外推。 | [摘要全译＋关键段落节译（非全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Double_Measurement_Confound/%E4%B8%AD%E6%96%87%E8%AF%91%E7%A8%BF_%E6%91%98%E8%A6%81%E5%85%A8%E8%AF%91%E4%B8%8E%E5%85%B3%E9%94%AE%E6%AE%B5%E8%90%BD%E8%8A%82%E8%AF%91.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Double_Measurement_Confound/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%85%A8%E6%96%87%E4%B8%8E%E9%85%8D%E5%9B%BE.md) · [官方](https://arxiv.org/abs/2609.09218) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Double_Measurement_Confound/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [AgentJudgeBench](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/AgentJudgeBench.md) | 2026 | P1 | 借鉴固定GT、难度/拓扑分层、with/without-GT及programmatic与人工标签的多级校准。 | [中文精读/核心译述（非全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentJudgeBench/AgentJudgeBench_%E4%B8%AD%E6%96%87%E7%B2%BE%E8%AF%BB%E4%B8%8E%E6%A0%B8%E5%BF%83%E5%86%85%E5%AE%B9%E8%AF%91%E8%BF%B0.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/AgentJudgeBench/AgentJudgeBench_%E8%8B%B1%E6%96%87%E5%85%A8%E6%96%87%E9%80%90%E9%A1%B5%E6%8F%90%E5%8F%96.md) · [官方](https://arxiv.org/abs/2608.26623v1) | 本地原始 PDF 缺失（见官方原文） |
| [BetterBench](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/BetterBench.md) | 2024 | P1 | 支持Benchmark选择指南与资源/文档检查；质量分不自动代表评价器语义正确。 | [摘要与章节译述（非逐句全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/BetterBench/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/BetterBench/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) · [官方](https://arxiv.org/abs/2411.12990) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/BetterBench/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| [Fantastic Bugs](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/%E9%80%90%E7%AF%87/Fantastic%20Bugs.md) | 2025 | P1 | 在已有多模型结果充分时探索低成本抽样审计；先核单维潜构念假设，避免异常即错题。 | [摘要与章节译述（非逐句全文）](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Fantastic%20Bugs/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) | [本地原文](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Fantastic%20Bugs/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%AE%8C%E6%95%B4%E6%8F%90%E5%8F%96.md) · [官方](https://arxiv.org/abs/2511.16842) | [PDF](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Fantastic%20Bugs/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |

## 阅读优先级

| 优先级 | 数量 | 阅读要求 | 清单 |
|---|---|---|---|
| P0 | 21 | 直接影响核心研究问题/审计对象/方法/创新性边界，精读 | [P0 阅读清单](%E9%98%85%E8%AF%BB%E4%BC%98%E5%85%88%E7%BA%A7/P0.md) |
| P1 | 16 | 补充评价机制、方法、对象或跨基准验证，针对性精读 | [P1 阅读清单](%E9%98%85%E8%AF%BB%E4%BC%98%E5%85%88%E7%BA%A7/P1.md) |
| P2 | 16 | 相关工作/边界/补充指标或专项背景，按需深读 | [P2 阅读清单](%E9%98%85%E8%AF%BB%E4%BC%98%E5%85%88%E7%BA%A7/P2.md) |
| P3 | 8 | 基础背景或关联较弱，归档按需查阅 | [P3 阅读清单](%E9%98%85%E8%AF%BB%E4%BC%98%E5%85%88%E7%BA%A7/P3.md) |

## 实证审计与评价指标 / Ground Truth

实证可行性单独记录任务、GT、轨迹、产物、评价器、环境/API及独立核验条件。R1 不表示已运行；RU 不表示资源不存在。

- [Benchmark 可行性矩阵](%E5%AE%9E%E8%AF%81%E5%AE%A1%E8%AE%A1%E5%8F%AF%E8%A1%8C%E6%80%A7/Benchmark%E5%8F%AF%E8%A1%8C%E6%80%A7%E7%9F%A9%E9%98%B5.md)
- [Task01：核心对标论文拆解与审计方法](Task01_%E6%A0%B8%E5%BF%83%E5%AF%B9%E6%A0%87%E8%AE%BA%E6%96%87%E6%8B%86%E8%A7%A3/QA_Task01_%E9%AA%8C%E6%94%B6%E6%8A%A5%E5%91%8A.md)
- [Task02：评价指标、测量对象与 GT 研究](Task02_%E5%9C%B0%E5%AD%A6Benchmark%E8%AF%84%E4%BB%B7%E6%8C%87%E6%A0%87%E4%BD%93%E7%B3%BB/README.md)
- [Task02：指标完整汇总](Task02_%E5%9C%B0%E5%AD%A6Benchmark%E8%AF%84%E4%BB%B7%E6%8C%87%E6%A0%87%E4%BD%93%E7%B3%BB/02_%E5%AE%8C%E6%95%B4%E8%AF%84%E4%BB%B7%E6%8C%87%E6%A0%87%E6%B1%87%E6%80%BB.csv)

## 分类规范与维护

- [文献总索引](%E6%96%87%E7%8C%AE%E6%80%BB%E7%B4%A2%E5%BC%95.md)
- [Benchmark 实证审计可行性矩阵](%E5%AE%9E%E8%AF%81%E5%AE%A1%E8%AE%A1%E5%8F%AF%E8%A1%8C%E6%80%A7/Benchmark%E5%8F%AF%E8%A1%8C%E6%80%A7%E7%9F%A9%E9%98%B5.md)
- [分类规范 v1.0（原始规范）](%E6%96%87%E7%8C%AE%E5%88%86%E7%B1%BB%E4%B8%8E%E4%BC%98%E5%85%88%E7%BA%A7%E8%A7%84%E8%8C%83.md)
- [YAML 元数据（唯一数据源）](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/literature_catalog.yaml)
- [CSV 元数据（自动导出）](%E6%96%87%E7%8C%AE%E5%85%83%E6%95%B0%E6%8D%AE/literature_catalog.csv)
- [分类维护说明](%E5%88%86%E7%B1%BB%E7%BB%B4%E6%8A%A4%E8%AF%B4%E6%98%8E.md)
- [本次分类整改验收报告](QA_%E6%96%87%E7%8C%AE%E5%88%86%E7%B1%BB%E6%95%B4%E6%94%B9%E9%AA%8C%E6%94%B6%E6%8A%A5%E5%91%8A.md)

统一数据源为 YAML；CSV、三个 README、类别与优先级索引和逐篇记录由脚本生成。未来新增文献先核实原文并更新 YAML，再生成和检查。原始论文目录保持原位。论文目录内随包保存的文献分类记录.yaml属于历史初步记录，不参与当前导航生成。

## 原有研究材料

Task01、Task02 成果及研究分析矩阵保留。早期矩阵属于阶段性研究记录，分类与阅读优先级以本次 YAML 为准。

- [研究背景与目标](00_%E7%A0%94%E7%A9%B6%E8%83%8C%E6%99%AF%E4%B8%8E%E7%9B%AE%E6%A0%87.md)
- [原有研究分析矩阵](%E7%A0%94%E7%A9%B6%E5%88%86%E6%9E%90%E7%9F%A9%E9%98%B5)
- [分类核验与变更记录](03_%E6%96%87%E7%8C%AE%E5%88%86%E7%B1%BB%E8%B0%83%E6%95%B4%E8%AE%B0%E5%BD%95.md)
- [论文阅读与图表导航](../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/README.md)
- [GitHub 上传与克隆教程](../%E6%95%99%E5%AD%A6/GitHub%E4%B8%8A%E4%BC%A0%E4%B8%8E%E5%85%8B%E9%9A%86%E6%95%99%E7%A8%8B.md)
