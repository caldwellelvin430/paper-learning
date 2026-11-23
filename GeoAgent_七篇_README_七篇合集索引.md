# 七篇 GeoAI / GeoAgent 文献整理合集（2026-11-23）

## 交付范围

- 7 份上传 PDF 的全部页面英文文本与原始 PDF；附录和参考文献无意截断。
- 各论文独立中文摘要全译与重点章节译述，**并非全文逐句精译**。
- 所有 PDF 页面对应高清截图，已识别图题/表题的区域裁图并使用相对路径。
- 每篇含 README、图表索引、QA 报告与核查数据，适合放入 GitHub 的 `论文翻译/` 目录。

## 统计汇总

| 论文 | 类型 | 原文页数 | 有标题图表裁图 | 中文译稿 |
|---|---|---:|---:|---|
| [AgenticAI_Survey](./论文翻译/AgenticAI_Survey/README_阅读说明.md) | 遥感智能体领域综述 | 14 | 3 | 摘要完整 + 核心章节节译 |
| [EarthSE](./论文翻译/EarthSE/README_阅读说明.md) | 地学科学知识与探索能力 Benchmark | 25 | 26 | 摘要完整 + 核心章节节译 |
| [GEOBench-VLM](./论文翻译/GEOBench-VLM/README_阅读说明.md) | 地学视觉语言模型静态感知 Benchmark | 11 | 14 | 摘要完整 + 核心章节节译 |
| [GeoLLM-Engine](./论文翻译/GeoLLM-Engine/README_阅读说明.md) | 工具增强地理空间任务/环境 Benchmark | 10 | 11 | 摘要完整 + 核心章节节译 |
| [GeoMMBench_GeoMMAgent](./论文翻译/GeoMMBench_GeoMMAgent/README_阅读说明.md) | 地学多模态 Benchmark + Agent 架构 | 11 | 6 | 摘要完整 + 核心章节节译 |
| [MapAgent](./论文翻译/MapAgent/README_阅读说明.md) | 地图服务工具增强 Agent | 27 | 22 | 摘要完整 + 核心章节节译 |
| [MSEarth](./论文翻译/MSEarth/README_阅读说明.md) | 科学论文图文推理 Benchmark | 32 | 42 | 摘要完整 + 核心章节节译 |

合计 **130 页**、**124 处有标题的图表裁图**；全部页面另有原版截图。

## 你的 GeoAgent Benchmark 研究中的建议定位

研究梳理时建议把七篇分为三个层级，避免混用评分指标：

1. **可执行工具与工作流层**：GeoLLM-Engine（工具环境与功能校验）、MapAgent（被评测的地图工具系统）。
2. **知识/感知/科学推理层**：EarthSE、GEOBench-VLM、GeoMMBench、MSEarth（评测对象、输出类型和 GT 与 GIS 工作流评价不同）。
3. **综述与领域分类层**：Agentic AI in Remote Sensing。

注意：论文基准是否能在本地复现、代码是否开源、数据可否完整下载，不由本次 PDF 提取证明。

## 交付限度

所有 PDF 页面均可视化留存、已识别图表均独立截图，但不能据此保证所有图像均有独立裁图；也未完成 130 页的全文逐段中文翻译。请使用各篇的 QA 文件核对。
