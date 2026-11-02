# AgentJudgeBench：文件与逐页视觉核查报告

- 原始 PDF 文件：`Verma 等 - 2026 - AgentJudgeBench A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling.pdf`
- 原稿页数：**31**；逐页截图：**31**
- 图表/算法/清单截图：**41**，分类：figure=10, table=31
- PDF 逐页提取总字符数：**128,733**；空白文本页：[]
- Markdown 文件数量：**3**；图片相对路径引用数量：**123**
- 机器可验证问题：**0**

## 自检方式

1. 使用 PyMuPDF 打开 PDF，逐页提取文本并渲染原稿页图像；对照实际页数，不以目录或印刷页码推测。
2. 检测 Figure、Table、Algorithm 与 Listing 标题，裁切相应图表；有些复杂表格或代码跨页时，以完整逐页原稿截图作为无损视觉依据。
3. 检查每个生成图像能否解码，并检查全部 Markdown 图片相对路径是否存在。
4. 论文的公式、参考文献、正文、附录以及代码示例由英文逐页全文与原稿截图完整覆盖；对有跨栏或文本流顺序异常的页面，以整页截图为准。

## 译文完成度与重要限制

**中文精读版并非逐句全文译本**：完整翻译摘要并详述论文核心论证、方法和结果；完整英文正文、参考文献和附录已提取，但尚未对英文所有段落逐句翻译。这一点会在交付时明确说明，不将仅有英文的页面标作完成中文翻译。

PDF 提取工具可能把上下标、数学字体、多栏表格文字或分词换行与正文混在一起，因此所有复杂公式和表格均需以对应原稿页图复核。当前已进行图表截图接触表视觉抽查；不能据此宣称逐字人工校对了每个公式、引文与页内数值。

## 异常清单

无失效的图片路径或无法解码的图片。

## 图表索引

| 原文页 | 类型 | 编号 | 图片文件 | 中文描述 |
|---:|---|---:|---|---|
| 2 | figure | 1 | `images/figure-1-p02.png` | AgentJudgeBench 数据生成与评判流程 |
| 5 | figure | 2 | `images/figure-2-p05.png` | 程序化评分与有/无 GT 的 LLM 评分流程 |
| 7 | table | 1 | `images/table-1-p07.png` | Llama-3.3-70B 生成器上的 C3 结果 |
| 7 | table | 2 | `images/table-2-p07.png` | 不同生成器、评判器、难度和 GT 条件的全体对齐结果 |
| 8 | figure | 3 | `images/figure-3-p08.png` | 各评价维度的有/无 GT 一致性 |
| 8 | table | 3 | `images/table-3-p08.png` | 评判器两两一致性 |
| 8 | table | 4 | `images/table-4-p08.png` | 无 GT 困难任务的默认评分策略消融 |
| 9 | figure | 4 | `images/figure-4-p09.png` | 评判器温度敏感性 |
| 9 | figure | 5 | `images/figure-5-p09.png` | 结构化与自由形式提示的表现 |
| 9 | table | 5 | `images/table-5-p09.png` | QwQ-32B 是否开启思维链的对比 |
| 13 | table | 6 | `images/table-6-p13.png` | 各部署场景下表现最佳的评判器 |
| 15 | figure | 6 | `images/figure-6-p15.png` | 六种 DAG 拓扑的样本分布 |
| 15 | table | 7 | `images/table-7-p15.png` | DAG 类型与样本数量 |
| 15 | figure | 7 | `images/figure-7-p15.png` | 工具数量、参数数量和预期调用数分布 |
| 15 | table | 8 | `images/table-8-p15.png` | 样本工具结构统计 |
| 16 | table | 9 | `images/table-9-p16.png` | 有效评判结果数量 |
| 17 | table | 10 | `images/table-10-p17.png` | Bootstrap 95% 置信区间 |
| 17 | figure | 8 | `images/figure-8-p17.png` | 不同难度条件下的一致性变化 |
| 17 | table | 11 | `images/table-11-p17.png` | 生成器的程序化准确率 |
| 17 | table | 12 | `images/table-12-p17.png` | 人工标注者与程序化评分器一致性 |
| 18 | table | 13 | `images/table-13-p18.png` | 依据程序化参考或人类判定的评判器对齐率 |
| 19 | table | 14 | `images/table-14-p19.png` | 调整参数结构评分权重后的排名 |
| 19 | table | 15 | `images/table-15-p19.png` | 对参数评分规则进行最大宽容修正后的排名与准确率 |
| 22 | table | 16 | `images/table-16-p22.png` | 论文符号定义 |
| 22 | table | 17 | `images/table-17-p22.png` | 相关工具调用评判系统对比 |
| 22 | table | 18 | `images/table-18-p22.png` | 用于产生工具调用输出的生成器模型 |
| 23 | table | 19 | `images/table-19-p23.png` | 三个元评判器对难度重写的验证结果 |
| 23 | table | 20 | `images/table-20-p23.png` | 三名元评判器的一致性 |
| 24 | table | 21 | `images/table-21-p24.png` | LLM 评判器的模型配置 |
| 24 | table | 22 | `images/table-22-p24.png` | 剔除 GPT-5.4 后对重写验证的一致性变化 |
| 24 | table | 23 | `images/table-23-p24.png` | GPT-5.4 评价自身输出的偏差分析 |
| 25 | table | 24 | `images/table-24-p25.png` | 每个评判维度的一致性 |
| 25 | table | 25 | `images/table-25-p25.png` | Qwen3-32B 的温度敏感性 |
| 26 | table | 26 | `images/table-26-p26.png` | QwQ-32B 思维链开关消融的完整结果 |
| 26 | table | 27 | `images/table-27-p26.png` | 第二组评判器—生成器的温度敏感性 |
| 26 | table | 28 | `images/table-28-p26.png` | 不同 DAG 拓扑的有 GT 评分一致性 |
| 26 | figure | 9 | `images/figure-9-p26.png` | 各 DAG 拓扑的评判一致性热力图 |
| 27 | figure | 10 | `images/figure-10-p27.png` | 评判器判定的混淆矩阵 |
| 27 | table | 29 | `images/table-29-p27.png` | 二元与三档评分尺度的对比 |
| 28 | table | 30 | `images/table-30-p28.png` | 智能体评估和 LLM 评判器相关研究综述表 |
| 29 | table | 31 | `images/table-31-p29.png` | 第二组结构化提示消融实验 |
