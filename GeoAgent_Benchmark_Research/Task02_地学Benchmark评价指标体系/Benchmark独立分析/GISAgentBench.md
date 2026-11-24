# GISAgentBench：独立分析

核查日期：2026-11-24。本文件基于[本地英文原文](../../../论文翻译/GISAgentBench/GISAgentBench_英文原文_逐页提取.md)。中文稿只用于术语辅助；所有论文事实按下列原文节页追溯。

## 对象定位与基本信息

- **定位**：实践任务Benchmark；不是Agent架构。
- **声称能力**：现实多步GIS任务完成与结果正确性。
- **任务**：空间连接/地理编码96；叠加93；地形63；空间模式52；遥感45。
- **规模**：349任务；6 AOI；92输入文件；128 API；参考轨迹2–43步，均值11.7。
- **工具**：QGIS/GDAL CLI及GeoPandas/Rasterio/Shapely等。
- **执行**：ReAct真实执行；50次调用预算。
- **输入**：5个美国地区+荷兰Randstad公开GIS数据。
- **输出**：文件产物、API轨迹、文本与运行记录。
- **GT构建**：Claude生成候选参考→独立Python交叉核对→3位GIS专家逐步与产物审核；歧义任务移除。
- **GT形式**：可执行参考轨迹、任务输出契约、精确GT文件及容差。
- **参考轨迹**：有；headline不以参考轨迹匹配计分。
- **真实产物**：有；GT与Agent文件。
- **评价器**：确定性结构、行集、数值与实体几何检查；不使用LLM Judge。
- **评分流程**：执行→结构与容差全通过得TSR→QCS连续接近度；轨迹仅诊断。
- **作者局限**：§4：地理集中、工具栈有限；开放答案/制图难用当前确定性评分；附录F.5承认角色集合忽略次数、参数与大部分顺序。

上述基础信息出处：§2–4；附录E、F、G、H，PDF物理页3–7、21–24。

## 正式评价指标与组件

| ID | 原文名称/缩写 | 实际测量对象 | 判分规则与分母 | 来源 |
| --- | --- | --- | --- | --- |
| M009 | Strict Task Success Rate / TSR（primary） | 容差意义下最终任务产物全通过 | CRS/类型/维度/NoData/列等全通过且匹配值容差内；二元任务成功率；无部分分 | §3.1；F.1 PDF5、23 |
| M010 | Quantitative Closeness Score / QCS（primary） | 产物部分接近程度及覆盖 | 数值1−sMAPE；类别weighted F1；实体F1；缺产物0；coverage-weighted product；完整跨类型/列/任务权重未报告 | §3.1；F.2–F.4 PDF5、23 |

完整公式、变量、阈值与未报告细节见[03_评价指标定义与公式](../03_评价指标定义与公式.md)。逐项能力结论边界见[07_构念效度](../07_构念效度与测量对象分析.md)。

## 非正式能力统计的分流

| ID | 统计 | 类型 | 规则/来源 |
| --- | --- | --- | --- |
| M011 | Row-set precision | 2_辅助诊断 | 契约ID→geometry key→唯一列→最优值配对；匹配输出行/输出行；F.2–F.4 PDF23 |
| M012 | Row coverage / recall | 2_辅助诊断 | 匹配参考行/参考行；F.2–F.4 PDF23 |
| M013 | Row-set F1 | 2_辅助诊断 | 行匹配P与R调和平均；F.2–F.4 PDF23 |
| M014 | Symmetric percentage-error closeness | 2_辅助诊断 | 1减对称百分误差并截断；sMAPE常数/零处理未完整给；F.2–F.4 PDF23 |
| M015 | Mean-normalized RMSE | 2_辅助诊断 | RMSE按参考均值归一；绝对值/零均值处理未报告；F.2–F.4 PDF23 |
| M016 | Weighted MAPE | 2_辅助诊断 | 底层记录保留；公式与零处理未报告；F.2–F.4 PDF23 |
| M017 | Correlation-based agreement | 2_辅助诊断 | 底层记录保留；具体相关系数与转换未报告；F.2–F.4 PDF23 |
| M018 | Fraction of cells within tolerance | 2_辅助诊断 | 容差内单元格比例；容差组合实现待查；F.2–F.4 PDF23 |
| M019 | Categorical weighted F1 | 2_辅助诊断 | 仅匹配行；排除参考单类别列；weighted F1；F.2–F.4 PDF23 |
| M020 | Entity precision | 2_辅助诊断 | 满足IoU≥0.5或点线距离ε的输出实体/输出实体；F.2–F.4 PDF23 |
| M021 | Entity recall | 2_辅助诊断 | 被匹配参考实体/参考实体；F.2–F.4 PDF23 |
| M022 | Entity F1 | 2_辅助诊断 | 实体级P/R调和；分别报多点/多线/多面；F.2–F.4 PDF23 |
| M023 | Trajectory closeness | 2_辅助诊断 | 只计非只读、无error角色；任务级去除被成功替代的要求；8空集不评分；F.5 PDF23–24 |
| M024 | Tool-call error rate | 2_辅助诊断 | 错误调用数/所有调用数；F.6 PDF24 |
| M025 | Failure-mechanism frequency | 2_辅助诊断 | 各标签占失败尝试比；总和可超过1；§3失败分析 PDF7 |
| M026 | Trajectory length | 3_效率成本数据特征 | 调用次数；F.6、G、H PDF24 |
| M027 | Model inference time | 3_效率成本数据特征 | 与harness GIS执行时间分开；F.6、G、H PDF24 |
| M028 | Harness time | 3_效率成本数据特征 | 不含等待模型端点；F.6、G、H PDF24 |
| M029 | Token consumption | 3_效率成本数据特征 | 按任务/族报告；F.6、G、H PDF24 |
| M030 | Role-map adjusted Rand index | 4_Benchmark元评价 | ARI=.27；68争议对经裁决修5处；F.5 PDF23 |
| M031 | Trajectory–TSR correlation | 4_Benchmark元评价 | point-biserial heldout .440/calibration .420；pooled .424；model .977；F.5 PDF24 |

## 原文核查中的定位修订

F.5开头说headline不比较轨迹，而后提供TC角色集合诊断，两者不矛盾。角色集不包含有序轨迹比较。F.2乐观匹配上界和F.5忽略参数都是作者主动限定。

## 下一轮可检验风险

| 风险 | 证据等级与依据 | 检验方式 |
| --- | --- | --- |
| R05：容差组合与QCS完整聚合缺少重现细节 | D；F.1给atol/rtol但无组合式；F.3只说明coverage product；F.1–F.4 p23 | 拿到scorer后对容差边界、空表、零均值、部分覆盖运行单变量例 |
| R06：不辨重复角色、错误参数与大部分顺序 | A；作者F.5明确；只作诊断；F.5 p24 | 固定工具集合改变层/参数/顺序；验证TC不变且TSR变化；不把预期局部性当bug |
| R07：最优值配对的乐观上界可能遮盖实体错配 | A；F.2作者明确last resort optimistic upper bound；F.2 p23 | 去掉ID且置换实体属性，记录fallback调用并比独立空间匹配 |
| R08：要求角色删除依赖已参评成功模型 | C；156任务375 role drops；any successful model证据门；F.5 pp23–24 | 冻结GT、角色map、成功池；增量加入模型后比较要求集与分数 |

## 资源与优先级

阅读优先级：已完成：第一批。实验优先级（本次分析建议）：高研究价值，待核实官方发布入口，不能把论文承诺当可运行资源。

| 资源 | 官方入口 | 已完成检查 | 下载/运行 |
| --- | --- | --- | --- |
| 代码 | 论文承诺公开但未定位到明确官方仓库URL | U：名称搜索无结果不代表未公开或不存在 | 否；否 |
| 数据/任务集 | 论文承诺公开但未定位到明确官方仓库URL | U：名称搜索无结果不代表未公开或不存在 | 否；否 |
| GT/参考 | 论文承诺公开但未定位到明确官方仓库URL | U：名称搜索无结果不代表未公开或不存在 | 否；否 |
| 评价器 | 论文承诺公开但未定位到明确官方仓库URL | U：名称搜索无结果不代表未公开或不存在 | 否；否 |

## 后续记录规则

本次未运行新Agent或官方评价器。后续审计记录必须写明任务/轨迹ID、数据与环境版本、scorer commit、rubric、模型配置、原分数、独立标签与争议裁决。新增实证结果单独追加，不把本文件的C级假设改写成既成事实。
