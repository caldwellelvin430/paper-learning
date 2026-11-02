# tau-bench：文件与逐页视觉核查报告

- 原始 PDF 文件：`Yao 等 - 2024 - τ-bench A Benchmark for Tool-Agent-User Interaction in Real-World Domains.pdf`
- 原稿页数：**50**；逐页截图：**50**
- 图表/算法/清单截图：**17**，分类：figure=7, table=4, listing=6
- PDF 逐页提取总字符数：**129,617**；空白文本页：[]
- Markdown 文件数量：**3**；图片相对路径引用数量：**134**
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
| 2 | figure | 1 | `images/figure-1-p02.png` | 工具—智能体—用户交互框架及航空领域示例轨迹 |
| 4 | figure | 2 | `images/figure-2-p04.png` | 数据库、API、政策、任务指令的模块化组成 |
| 5 | table | 1 | `images/table-1-p05.png` | 零售与航空两个领域的数据及任务规模 |
| 7 | table | 2 | `images/table-2-p07.png` | 不同模型的单次任务成功率 pass^1 |
| 7 | figure | 3 | `images/figure-3-p07.png` | 零售领域不同代理方法的成功率 |
| 7 | figure | 4 | `images/figure-4-p07.png` | 零售领域 pass^k 与 pass@k 的对比 |
| 7 | figure | 5 | `images/figure-5-p07.png` | 36 条失败轨迹的错误类型 |
| 8 | table | 3 | `images/table-3-p08.png` | 缺失领域政策时任务成功率的下降 |
| 8 | figure | 6 | `images/figure-6-p08.png` | 写入数据库动作次数与任务难度 |
| 13 | figure | 7 | `images/figure-7-p13.png` | 零售任务逐任务成功率分布 |
| 13 | table | 4 | `images/table-4-p13.png` | 两个业务领域的数据库与 API 清单 |
| 23 | listing | 1 | `images/listing-1-p23.png` | 零售用户数据库记录示例 |
| 23 | listing | 2 | `images/listing-2-p23.png` | 零售商品数据库记录示例 |
| 24 | listing | 3 | `images/listing-3-p24.png` | 零售订单数据库记录示例 |
| 43 | listing | 4 | `images/listing-4-p43.png` | 航空用户数据库记录示例 |
| 44 | listing | 5 | `images/listing-5-p44.png` | 航班数据库记录示例 |
| 45 | listing | 6 | `images/listing-6-p45.png` | 航空预订数据库记录示例 |
