# AgentJudgeBench：逐页图表、算法与原文图像对照

> PDF 共 **31 页**；本文档按照 PDF 物理页码逐页列出所有检测到的 Figure、Table、Algorithm、Listing。下面的每张图片均是从上传 PDF 直接渲染或裁切，没有重绘或更改数值。


## 原稿第 1 页

**整页原稿截图（第 1 页，含该页全部文字与图表）：**

![PDF第1页](./source_pages/page-001.jpg)


## 原稿第 2 页

### 图 1：AgentJudgeBench 数据生成与评判流程

![原稿图1](./images/figure-1-p02.png)

> 原文标题：Figure 1: Overall pipeline of AgentJudgeBench. Each BFCL-style Agentic record undergoes difficulty-controlled rewriting, generator inference, and parallel scoring by a programmatic judge and LLM judges (with/without GT), followed by alignment with the programmatic reference.

**整页原稿截图（第 2 页，含该页全部文字与图表）：**

![PDF第2页](./source_pages/page-002.jpg)


## 原稿第 3 页

**整页原稿截图（第 3 页，含该页全部文字与图表）：**

![PDF第3页](./source_pages/page-003.jpg)


## 原稿第 4 页

**整页原稿截图（第 4 页，含该页全部文字与图表）：**

![PDF第4页](./source_pages/page-004.jpg)


## 原稿第 5 页

### 图 2：程序化评分与有/无 GT 的 LLM 评分流程

![原稿图2](./images/figure-2-p05.png)

> 原文标题：Figure 2: Evaluation pipeline of AgentJudgeBench. Records expand into three difficulty tiers, LLM judges (with/without GT) and programmatic judge score the generated tool-call predictions.

**整页原稿截图（第 5 页，含该页全部文字与图表）：**

![PDF第5页](./source_pages/page-005.jpg)


## 原稿第 6 页

**整页原稿截图（第 6 页，含该页全部文字与图表）：**

![PDF第6页](./source_pages/page-006.jpg)


## 原稿第 7 页

### 表 1：Llama-3.3-70B 生成器上的 C3 结果

![原稿表1](./images/table-1-p07.png)

> 原文标题：Table 1: Full C3 results on Llama-3.3-70B generator. All values are mean alignment (%) over 3,764–3,771 records per cell. cGT: corrupted-GT condition. Gemini: Gemini 2.5 Pro. ∆cGT-GT: corrupted-GT minus standard GT. ∆cGT-noGT: corrupted-GT minus without GT.

### 表 2：不同生成器、评判器、难度和 GT 条件的全体对齐结果

![原稿表2](./images/table-2-p07.png)

> 原文标题：Table 2: LLM–judge alignment (%) with the program- matic reference across generators, judges, difficulty, and GT condition. Bold = column-wise maximum within each generator block among the six main judges. Prom2 = Prometheus-2, a judge-specialised baseline (Limita- tions); shown for reference and not counted toward bold column-wise maxima or six-judge statistics. full breakdowns are in Appendices

**整页原稿截图（第 7 页，含该页全部文字与图表）：**

![PDF第7页](./source_pages/page-007.jpg)


## 原稿第 8 页

### 图 3：各评价维度的有/无 GT 一致性

![原稿图3](./images/figure-3-p08.png)

> 原文标题：Figure 3: Per-metric alignment (with and without GT) across the six main judges, plus Prometheus-2 (judge- specialised baseline; Limitations), shown for reference.

### 表 3：评判器两两一致性

![原稿表3](./images/table-3-p08.png)

> 原文标题：Table 3: Pairwise inter-judge agreement under the with GT condition. Upper triangle : exact metric-level

### 表 4：无 GT 困难任务的默认评分策略消融

![原稿表4](./images/table-4-p08.png)

> 原文标题：Table 4: Hard without GT alignment (%) under the standard 1.0-default and the recalibrated 0.5-default prompts, averaged across six judges per generator. ∆= (0.5-default) −(1.0-default).

**整页原稿截图（第 8 页，含该页全部文字与图表）：**

![PDF第8页](./source_pages/page-008.jpg)


## 原稿第 9 页

### 图 4：评判器温度敏感性

![原稿图4](./images/figure-4-p09.png)

> 原文标题：Figure 4: Judge temperature sensitivity. Qwen3-32B alignment at T ∈{0.3, 0.7, 1.0} on Llama-3.3-70B. All three difficulty curves are near-flat; maximum spread ≤0.6 pp.

### 图 5：结构化与自由形式提示的表现

![原稿图5](./images/figure-5-p09.png)

> 原文标题：Figure 5: Prompt structure vs. alignment. Structured JSON prompt vs. free-form for Qwen3-32B on Llama- 3.3-70B. The per-metric rubric adds +4.8-+6.5 pp with GT across all difficulty levels.

### 表 5：QwQ-32B 是否开启思维链的对比

![原稿表5](./images/table-5-p09.png)

> 原文标题：Table 5: Chain-of-thought reasoning in the QwQ-32B judge: alignment (%) with thinking on vs. off across four open-weight generators. ∆= thinking-on − thinking-off (pp).

**整页原稿截图（第 9 页，含该页全部文字与图表）：**

![PDF第9页](./source_pages/page-009.jpg)


## 原稿第 10 页

**整页原稿截图（第 10 页，含该页全部文字与图表）：**

![PDF第10页](./source_pages/page-010.jpg)


## 原稿第 11 页

**整页原稿截图（第 11 页，含该页全部文字与图表）：**

![PDF第11页](./source_pages/page-011.jpg)


## 原稿第 12 页

**整页原稿截图（第 12 页，含该页全部文字与图表）：**

![PDF第12页](./source_pages/page-012.jpg)


## 原稿第 13 页

### 表 6：各部署场景下表现最佳的评判器

![原稿表6](./images/table-6-p13.png)

> 原文标题：Table 6: Best judge per deployment scenario. The with- out GT rows reflect the common deployment setting where ground-truth tool calls are unavailable. GT = ground-truth tool calls available; without GT = judge uses only query and tool schemas. Alignment (%) is unweighted mean over five generators.

**整页原稿截图（第 13 页，含该页全部文字与图表）：**

![PDF第13页](./source_pages/page-013.jpg)


## 原稿第 14 页

**整页原稿截图（第 14 页，含该页全部文字与图表）：**

![PDF第14页](./source_pages/page-014.jpg)


## 原稿第 15 页

### 图 6：六种 DAG 拓扑的样本分布

![原稿图6](./images/figure-6-p15.png)

> 原文标题：Figure 6: DAG topology distribution across the 3,808 unique records (left: proportional pie, right: absolute counts). Fan-in accounts for over a quarter of all records; loop-like is the rarest at 5.9%.

### 表 7：DAG 类型与样本数量

![原稿表7](./images/table-7-p15.png)

> 原文标题：Table 7: Record counts by DAG topology. Counts reflect unique records; each record has three difficulty variants (easy / medium / hard), giving 3,808×3 = 11,424 total rows in the full dataset.

### 图 7：工具数量、参数数量和预期调用数分布

![原稿图7](./images/figure-7-p15.png)

> 原文标题：Figure 7: Frequency distributions of (left) available tools per record, (centre) parameters per tool, and (right) expected tool calls per record. Dashed vertical lines mark the mean of each distribution. Tool inventory is tightly concentrated around 13 (range 8-19); parameter counts are right-skewed with a median of 2; expected call-sequence length ranges from 2 to 5.

### 表 8：样本工具结构统计

![原稿表8](./images/table-8-p15.png)

> 原文标题：Table 8: Structural statistics of the 3,808 Agent- JudgeBench records. All quantities are computed over unique records (collapsing difficulty variants). Avail- able tools is the size of the tool inventory exposed to the generator per record. Parameters per tool counts typed argument fields in each tool’s JSON schema. Expected tool calls is the length of the ground-truth execution trace.

**整页原稿截图（第 15 页，含该页全部文字与图表）：**

![PDF第15页](./source_pages/page-015.jpg)


## 原稿第 16 页

### 表 9：有效评判结果数量

![原稿表9](./images/table-9-p16.png)

> 原文标题：Table 9: Number of records with valid LLM-judge ver- dicts per generator and difficulty tier. Theoretical max per generator is 3,808 × 3 = 11,424 (three difficulty variants of each base record). Judged records are iden- tical across all six LLM judges for a given (genera- tor, difficulty) cell. Multiplying the Total column by 6 judges × 2 conditions yields the full evaluation in- stance count per

**整页原稿截图（第 16 页，含该页全部文字与图表）：**

![PDF第16页](./source_pages/page-016.jpg)


## 原稿第 17 页

### 表 10：Bootstrap 95% 置信区间

![原稿表10](./images/table-10-p17.png)

> 原文标题：Table 10: Bootstrap 95% confidence intervals for alignment (%) on the Llama-3.3-70B-Instruct generator. Format: mean [lo, hi].

### 图 8：不同难度条件下的一致性变化

![原稿图8](./images/figure-8-p17.png)

> 原文标题：Figure 8: Mean judge alignment as a function of query difficulty, averaged across all six judges and five gen- erators. The without GT degradation slope is roughly 1.5× steeper than the GT slope across all generators.

### 表 11：生成器的程序化准确率

![原稿表11](./images/table-11-p17.png)

> 原文标题：Table 11: Generator programmatic accuracy ¯p (%) on AgentJudgeBench, averaged across the four metrics and six DAG topologies. Generators are ranked by hard- difficulty accuracy.

### 表 12：人工标注者与程序化评分器一致性

![原稿表12](./images/table-12-p17.png)

> 原文标题：Table 12: Human annotator agreement with the program- matic scorer across 120 hard-difficulty records (n=480 metric-level verdicts), stratified at 20 records per DAG topology.

**整页原稿截图（第 17 页，含该页全部文字与图表）：**

![PDF第17页](./source_pages/page-017.jpg)


## 原稿第 18 页

### 表 13：依据程序化参考或人类判定的评判器对齐率

![原稿表13](./images/table-13-p18.png)

> 原文标题：Table 13: Judge alignment (%, with GT) on 120 hard records: vs. programmatic reference and vs. human verdicts (35 corrected). ∆= human −programmatic. Smaller |∆| is better.

**整页原稿截图（第 18 页，含该页全部文字与图表）：**

![PDF第18页](./source_pages/page-018.jpg)


## 原稿第 19 页

### 表 14：调整参数结构评分权重后的排名

![原稿表14](./images/table-14-p19.png)

> 原文标题：Table 14: With-GT judge ranking (programmatic ref- erence) under alternative weightings of the parameter- structure metric. The full six-judge ranking is identical across all three weightings.

### 表 15：对参数评分规则进行最大宽容修正后的排名与准确率

![原稿表15](./images/table-15-p19.png)

> 原文标题：Table 15: With-GT alignment (%) under the current parameter-structure rule vs. the maximally generous upper-bound correction, record-weighted across the full corpus. Judges’ own verdicts are held fixed; only the programmatic reference’s parameter-structure score changes. Ranking order is identical to the current one in both columns.

**整页原稿截图（第 19 页，含该页全部文字与图表）：**

![PDF第19页](./source_pages/page-019.jpg)


## 原稿第 20 页

**整页原稿截图（第 20 页，含该页全部文字与图表）：**

![PDF第20页](./source_pages/page-020.jpg)


## 原稿第 21 页

**整页原稿截图（第 21 页，含该页全部文字与图表）：**

![PDF第21页](./source_pages/page-021.jpg)


## 原稿第 22 页

### 表 16：论文符号定义

![原稿表16](./images/table-16-p22.png)

> 原文标题：Table 16: Notation used in the paper.

### 表 17：相关工具调用评判系统对比

![原稿表17](./images/table-17-p22.png)

> 原文标题：Table 17: Comparison of systems that deploy LLM judges for agentic tool-calling evaluation. Judge Model: LLM used as judge. Per-Metric: whether evaluation is decomposed into fine-grained dimensions. Difficulty: whether tasks span multiple difficulty tiers. GT Abl.: whether the effect of ground-truth availability is studied. Prog. Ref.: whether a deterministic evaluator is used as a bias-free basel

### 表 18：用于产生工具调用输出的生成器模型

![原稿表18](./images/table-18-p22.png)

> 原文标题：Table 18: Generator models used to produce tool-calling outputs. All generators use temperature = 0 with their native function-calling prompt.

**整页原稿截图（第 22 页，含该页全部文字与图表）：**

![PDF第22页](./source_pages/page-022.jpg)


## 原稿第 23 页

### 表 19：三个元评判器对难度重写的验证结果

![原稿表19](./images/table-19-p23.png)

> 原文标题：Table 19: Per-judge “yes”-rate on the rewrite-validation criteria over n = 198 stratified triplets.

### 表 20：三名元评判器的一致性

![原稿表20](./images/table-20-p23.png)

> 原文标题：Table 20: Unanimity of the three meta-judges on each criterion (n = 198).

**整页原稿截图（第 23 页，含该页全部文字与图表）：**

![PDF第23页](./source_pages/page-023.jpg)


## 原稿第 24 页

### 表 21：LLM 评判器的模型配置

![原稿表21](./images/table-21-p24.png)

> 原文标题：Table 21: LLM judge configurations evaluated in this paper. All judges consume the same prompt scaffold (Appendix W) and produce the same JSON output schema.

### 表 22：剔除 GPT-5.4 后对重写验证的一致性变化

![原稿表22](./images/table-22-p24.png)

> 原文标题：Table 22: Unanimous-agreement rate on each rewrite- validation criterion, Claude Sonnet 4.5 + Gemini-2.5- Pro only (n = 198), versus the published three-meta- judge rate. ∆= 2-judge −3-judge.

### 表 23：GPT-5.4 评价自身输出的偏差分析

![原稿表23](./images/table-23-p24.png)

> 原文标题：Table 23: Judge=GPT-5.4 bias (llm_accuracy − programmatic_accuracy) by generator, averaged over all difficulty tiers. ∗GPT-5.4 judging its own genera- tions.

**整页原稿截图（第 24 页，含该页全部文字与图表）：**

![PDF第24页](./source_pages/page-024.jpg)


## 原稿第 25 页

### 表 24：每个评判维度的一致性

![原稿表24](./images/table-24-p25.png)

> 原文标题：Table 24: Per-metric match score µm j,r,c × 100, av- eraged across all (g, d) configurations. Bold marks the best value per column among the six main judges. Prometheus-2 (all five generators, both GT conditions) is shown for reference below the rule and excluded from bold column-wise maxima; under GT it trails the six- judge range by 20-45 pp on parameter structure and query coverage specifically

### 表 25：Qwen3-32B 的温度敏感性

![原稿表25](./images/table-25-p25.png)

> 原文标题：Table 25: Judge temperature sensitivity: per-difficulty alignment (%) for Qwen3-32B on Llama-3.3-70B.

**整页原稿截图（第 25 页，含该页全部文字与图表）：**

![PDF第25页](./source_pages/page-025.jpg)


## 原稿第 26 页

### 表 26：QwQ-32B 思维链开关消融的完整结果

![原稿表26](./images/table-26-p26.png)

> 原文标题：Table 26: Chain-of-thought reasoning study: full per-generator alignment (%) for QwQ-32B with thinking on vs. off. ∆rows show thinking-on minus thinking-off in percentage points.

### 表 27：第二组评判器—生成器的温度敏感性

![原稿表27](./images/table-27-p26.png)

> 原文标题：Table 27: Judge temperature sensitivity, second pairing: with-GT alignment (%) for GPT-OSS-120B on Llama- 3.1-8B-Instruct. Maximum spread (0.25 pp) is even tighter than the original (Qwen3-32B, Llama-3.3-70B) pairing in Table 25 (≤0.6 pp), confirming temperature insensitivity generalises beyond the original test-bed cell.

### 表 28：不同 DAG 拓扑的有 GT 评分一致性

![原稿表28](./images/table-28-p26.png)

> 原文标题：Table 28: Judge alignment (with GT, %) by DAG topol- ogy. Bold marks the best judge per topology.

### 图 9：各 DAG 拓扑的评判一致性热力图

![原稿图9](./images/figure-9-p26.png)

> 原文标题：Figure 9: Judge alignment (%) by DAG topology (with GT), visualised as a heatmap. Fan-out consistently achieves the highest alignment across all judges; fan-in and loop-like are the hardest. The ordering is judge- independent, indicating that DAG structural complexity is an intrinsic difficulty signal.

**整页原稿截图（第 26 页，含该页全部文字与图表）：**

![PDF第26页](./source_pages/page-026.jpg)


## 原稿第 27 页

### 图 10：评判器判定的混淆矩阵

![原稿图10](./images/figure-10-p27.png)

> 原文标题：Figure 10: Verdict-level confusion matrices (% of N). Rows = judge 1, columns = judge 2. Diagonal entries are shaded.

### 表 29：二元与三档评分尺度的对比

![原稿表29](./images/table-29-p27.png)

> 原文标题：Table 29: Binary vs. {0, 0.5, 1} verdict scale: mean GT alignment (%) and judge rankings averaged over 15 (generator, difficulty) cells. ∆= Binary −Standard.

**整页原稿截图（第 27 页，含该页全部文字与图表）：**

![PDF第27页](./source_pages/page-027.jpg)


## 原稿第 28 页

### 表 30：智能体评估和 LLM 评判器相关研究综述表

![原稿表30](./images/table-30-p28.png)

> 原文标题：Table 30: Representative works across agentic benchmarks, LLM-as-judge methods, and LLM judges for tool- calling evaluation.

**整页原稿截图（第 28 页，含该页全部文字与图表）：**

![PDF第28页](./source_pages/page-028.jpg)


## 原稿第 29 页

### 表 31：第二组结构化提示消融实验

![原稿表31](./images/table-31-p29.png)

> 原文标题：Table 31: Prompt format ablation, second pairing: with- GT alignment (%) for QwQ-32B on SmolLM3-3B, structured per-metric prompt vs. free-form. Compare to the original (Qwen3-32B, Llama-3.3-70B) pairing’s +4.8-+6.5 pp (Figure 5): the effect is smaller here and reverses sign on hard queries.

**整页原稿截图（第 29 页，含该页全部文字与图表）：**

![PDF第29页](./source_pages/page-029.jpg)


## 原稿第 30 页

**整页原稿截图（第 30 页，含该页全部文字与图表）：**

![PDF第30页](./source_pages/page-030.jpg)


## 原稿第 31 页

**整页原稿截图（第 31 页，含该页全部文字与图表）：**

![PDF第31页](./source_pages/page-031.jpg)

