# Plan-and-Solve — 逐页核查与翻译覆盖报告

- 上传原稿：`original.pdf`，**26 页**。
- 逐页提取：`english_pages/` 中按页保存重排版本与原始文本层版本，各 **26 页**。
- 英文总体字符量（PDF 原始文本层）：**72,859**。
- 原稿逐页图：**26 张**，位于 `source_pages/`。
- 原图/表编号：**5 图、26 表**（预期 5 图、26 表）；独立图表截图 **31 张**。
- 另外从 PDF 提取独立图片资产：**5** 个，供检查或复用。
- 中文文档图片路径引用：**31 处**，缺失 **0 处**。
- 中文译述长度：**6,670 个字符（含 Markdown 标记）**。

## 关键说明：是否达到逐句全文翻译？

**没有。** 中文稿属于逐页、分章节的忠实中文学术译述，保留了主要方法、实验数据、研究结论、术语与图表，**但并未覆盖全部英文段落、完整参考文献题名、每个表格单元格及长篇英文示例的逐句翻译**。不要将它当作严格完整的全文中文译本。

原始英文文本在 `英文原文_逐页.md` 与 `english_pages/`，英文书目信息在 `参考文献与英文附录_原文.md`，并含 `source_pages/` 原始截图用于交叉核对。

## 视觉与结构检查

- 逐页源文件已渲染为 JPEG，且保存原始 PDF，图表截图来自对应的 PDF 页而非生成图片。
- 已生成图表缩略总览进行检查；对 GeoCode-GPT 跨栏表格使用完整页面截图确保数据未裁断。
- 提取时尽可能按双栏“左栏→右栏”的顺序重排；特殊图中文字和公式应与原稿页图核对。
- 对数字、代码、API 名和公式没有做自动纠错；原文存在的表达问题保留，不擅自修改。

## 特定核对备注

- 表7—16含英文提示词细微差异，英文原文和截图全部保留，中文只做功能性译述。
- 表17—26是较长模型问答原文样例，保留原始英语以避免改动实验复现中的提示语及输出。
- 最后2页为 ACL 责任研究检查清单，逐页原始文字与页图保留。

## 逐页检查清单

| PDF 页码 | 提取文字字符数 | 图表标题索引 | 页图 |
|---|---:|---|---|
| 1 | 4034 | Figure-1 | `source_pages/page-001.jpg` |
| 2 | 4686 | — | `source_pages/page-002.jpg` |
| 3 | 3321 | Figure-2 | `source_pages/page-003.jpg` |
| 4 | 2611 | Figure-3 | `source_pages/page-004.jpg` |
| 5 | 4416 | Table-1 | `source_pages/page-005.jpg` |
| 6 | 3646 | Table-2, Table-3, Table-4, Figure-4 | `source_pages/page-006.jpg` |
| 7 | 4019 | Table-5, Table-6 | `source_pages/page-007.jpg` |
| 8 | 4344 | Figure-5 | `source_pages/page-008.jpg` |
| 9 | 4517 | — | `source_pages/page-009.jpg` |
| 10 | 4865 | — | `source_pages/page-010.jpg` |
| 11 | 2084 | — | `source_pages/page-011.jpg` |
| 12 | 3466 | Table-7, Table-8, Table-9 | `source_pages/page-012.jpg` |
| 13 | 3462 | Table-10, Table-11, Table-12, Table-13, Table-14 | `source_pages/page-013.jpg` |
| 14 | 1732 | Table-15, Table-16 | `source_pages/page-014.jpg` |
| 15 | 2083 | Table-17 | `source_pages/page-015.jpg` |
| 16 | 2397 | Table-18 | `source_pages/page-016.jpg` |
| 17 | 1740 | Table-19 | `source_pages/page-017.jpg` |
| 18 | 1837 | Table-20 | `source_pages/page-018.jpg` |
| 19 | 1704 | Table-21 | `source_pages/page-019.jpg` |
| 20 | 1831 | Table-22 | `source_pages/page-020.jpg` |
| 21 | 1710 | Table-23 | `source_pages/page-021.jpg` |
| 22 | 1540 | Table-24 | `source_pages/page-022.jpg` |
| 23 | 665 | Table-25 | `source_pages/page-023.jpg` |
| 24 | 2298 | Table-26 | `source_pages/page-024.jpg` |
| 25 | 2238 | — | `source_pages/page-025.jpg` |
| 26 | 1613 | — | `source_pages/page-026.jpg` |

## 自动检查结果

**通过（文件存在性、页数、图表编号、图片解码及相对路径）**
