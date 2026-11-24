# GeoPlan-bench：独立分析

核查日期：2026-11-24。本文件基于[本地英文原文](../../../论文翻译/HTAM_EarthAgent/原始论文.pdf)。中文稿只用于术语辅助；所有论文事实按下列原文节页追溯。

## 对象定位与基本信息

- **定位**：HTAM为框架；EarthAgent为系统；GeoPlan-bench为规划Benchmark；不另计三次。
- **声称能力**：关键工具选择、规划结构与逻辑完整性。
- **任务**：遥感7领域；简单561、中等441、复杂242。
- **规模**：1907初始→1244保留；主评996（排除AFlow训练248）。
- **工具**：领域工具依赖图；评测使用mock工具返回。
- **执行**：规划序列评分，不要求真实工具成功；实际演示系统与主评区分。
- **输入**：生成任务、参数和参考依赖/调用路径。
- **输出**：工具调用计划；主评不以真实遥感产物为结果。
- **GT构建**：Gemini2.5-Pro依赖图→GPT4o-mini参数与反向查询→领域/复杂性/去重过滤。
- **GT形式**：Sgt工具路径、LLM识别关键集、聚合依赖图中心性。
- **参考轨迹**：有；规划参考路径。
- **真实产物**：主评不依赖；补充11系统演示不能替代主评产物GT。
- **评价器**：LLM关键工具集；加权编辑距离/嵌入；成对LLM Judge及Elo。
- **评分流程**：关键召回/精确/F1→加权路径相似度→全部成对比较Elo完整性。
- **作者局限**：补充7.2：领域依赖与层次设计、抽象与回退限制；规划分不覆盖真实工具成功（补充8.2明示）。

上述基础信息出处：§5.1；补充7.2、8.1–8.2、10.3，PDF物理页7、12–15、61。

## 正式评价指标与组件

| ID | 原文名称/缩写 | 实际测量对象 | 判分规则与分母 | 来源 |
| --- | --- | --- | --- | --- |
| M096 | Key tool recall / Recall_key（primary） | 参考关键工具覆盖 | LLM先识别GT关键集合；与候选全路径交；任务/复杂度/领域/模型；Elo跨对战更新 | §5.1；补充8.2 式6–15 PDF7、14–15 |
| M097 | Key tool precision / Precision_key（primary） | 候选关键工具相关性 | LLM先识别候选关键集合；与参考全路径交；不是普通同集合precision；任务/复杂度/领域/模型；Elo跨对战更新 | §5.1；补充8.2 式6–15 PDF7、14–15 |
| M098 | Key tool F1 / F1_key（primary） | 双向关键工具选择 | 两套不同关键集合的P/R调和；任务/复杂度/领域/模型；Elo跨对战更新 | §5.1；补充8.2 式6–15 PDF7、14–15 |
| M099 | Path similarity / Structural score / PathSimilarity（primary） | 参考规划序列的结构接近 | 增删成本来自图中心性；替换成本1−embedding cosine；MaxPossibleCost启发式；任务/复杂度/领域/模型；Elo跨对战更新 | §5.1；补充8.2 式6–15 PDF7、14–15 |
| M100 | Completeness score / Elo / Elo（primary） | 相对于参评Agent的逻辑完整性偏好 | 同任务两两计划对比；win1/draw.5/loss0；Elo在线更新；任务/复杂度/领域/模型；Elo跨对战更新 | §5.1；补充8.2 式6–15 PDF7、14–15 |

完整公式、变量、阈值与未报告细节见[03_评价指标定义与公式](../03_评价指标定义与公式.md)。逐项能力结论边界见[07_构念效度](../07_构念效度与测量对象分析.md)。

## 非正式能力统计的分流

| ID | 统计 | 类型 | 规则/来源 |
| --- | --- | --- | --- |
| M101 | Out-degree centrality | 3_效率成本数据特征 | 全局工具图重要性，不是Agent成功指标；补充10.3 式20–23 PDF61 |
| M102 | PageRank centrality | 3_效率成本数据特征 | 阻尼/归一参数未完整报告；补充10.3 式20–23 PDF61 |
| M103 | Out-degree edit cost | 3_效率成本数据特征 | 式21；补充10.3 式20–23 PDF61 |
| M104 | PageRank edit cost | 3_效率成本数据特征 | 式22；补充10.3 式20–23 PDF61 |
| M105 | Composite importance | 3_效率成本数据特征 | 式23附近；工具图统计；补充10.3 式20–23 PDF61 |
| M106 | Composite cost | 3_效率成本数据特征 | 式23；与段落文字简写不完全同义，保留公式口径；补充10.3 式20–23 PDF61 |

## 原文核查中的定位修订

1244任务中248用于AFlow训练，主评996。本文69物理页与补充印刷页码不一致，引用一律用PDF物理页。补充11真实系统展示不改变补充8.2“planning only”的主评分定义。

## 下一轮可检验风险

| 风险 | 证据等级与依据 | 检验方式 |
| --- | --- | --- |
| R21：两次关键集LLM提取可改变分母 | C；GT与候选各自key set；未给固定缓存/复现协议；补充8.2.1 PDF14 | 冻结path与工具说明，多次提key；再冻结key仅重算指标，分解来源 |
| R22：中心性与归一上界参数欠明 | D；α与MaxPossibleCost启发式未完整给；补充8.2.2 PDF14–15；10.3 PDF61 | 核代码成本/边界/中心性归一；用相同path只改一个编辑操作验证 |
| R23：参评集合与顺序、Judge偏好混合 | C；Elo逐场更新；K/初值/对战顺序未完全报告；补充8.2.3 PDF15 | 固定成对胜负表先置换更新顺序；另固定计划重复Judge，分开两种波动 |
| R24：规划分被外推为真实地学执行成功 | C；补充8.2明确不依赖工具执行；mock环境；§5.1 p7；补充8.2 PDF14 | 不需先大规模运行；抽小样本计划在可控真实工具环境执行，单列运行失败来源 |

## 资源与优先级

阅读优先级：已完成：第三批。实验优先级（本次分析建议）：高：独立GeoPlan代码已可访问；Elo与关键集优先；不需EarthAgent私有代码。

| 资源 | 官方入口 | 已完成检查 | 下载/运行 |
| --- | --- | --- | --- |
| 代码 | [代码](https://github.com/earth-insights/GeoPlan-bench) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| 数据/任务集 | [数据/任务集](https://github.com/earth-insights/GeoPlan-bench/tree/main/data) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| GT/参考 | [GT/参考](https://github.com/earth-insights/GeoPlan-bench/tree/main/data/test_tasks) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| 评价器 | [评价器](https://github.com/earth-insights/GeoPlan-bench/tree/main/geoplan_bench/evaluation) | 已确认geoplan_bench目录列出evaluation；未独立请求子目录 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| 所属EarthAgent系统代码 | [所属EarthAgent系统代码](https://github.com/earth-insights/EarthAgent) | 是；根目录仅README.md | 仅README响应已保存；系统源码未取得；否 |

## 后续记录规则

本次未运行新Agent或官方评价器。后续审计记录必须写明任务/轨迹ID、数据与环境版本、scorer commit、rubric、模型配置、原分数、独立标签与争议裁决。新增实证结果单独追加，不把本文件的C级假设改写成既成事实。
