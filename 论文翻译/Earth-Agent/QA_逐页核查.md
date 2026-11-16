# Earth-Agent：逐页校验及翻译覆盖说明

- 原始 PDF：**65 页**。
- 原稿逐页截图：**65/65 页**。
- 每页提取到英文文本：**65/65 页**（无空白文本页）。
- 原始独立图：**42 幅**；原始表格：**17 张**。
- 图片文件总数：**66 个**（含跨页续表）。
- 中文 Markdown 图片引用：**66 处**；无失效路径。
- 图片文件可打开：**全部通过**。

## 中文翻译范围（务必阅读）

摘要及第 1–6 节进行了较详细的中文译写；附录 A–G 的结构、关键方法、全部图表标题和案例图索引已汉化；大量长代码、API 工具表原文、案例图内英文和参考文献尚未逐句翻译。

**说明：此版本虽然有完整英文提取稿和逐页图表，但并未达到“每一个英文段落、代码注释、表格单元格与参考文献都逐句汉化”的严格全译标准。** 请勿将此校验表当作逐句翻译通过证明。

## 视觉检验方法

1. 逐页截图由原 PDF 的渲染结果生成，供核对分页、图表是否跨页。
2. 按 PDF 内图号和表号定位，并分别裁取原稿图表。跨页表格另附续页截图。
3. 对全部截图运行图片文件完整性验证；检查 `中文译文.md` 中全部图片引用的相对路径均存在。
4. 抽样人工检查典型图表的内容边界，如工具表、模型结果表和架构示意图。
5. 表格截图可能包含所在页面的正文，原因是需要保证跨栏或紧邻正文的表格数据不被裁掉；无法凭截图检查所有公式转写精度时，请参照 PDF。

## 逐页核对表

| PDF 页 | 英文字符数 | 图 / 表所在页 | 原稿截图 |
|---:|---:|---|---|
| 1 | 4684 | 图1 | [原稿第1页](./source_pages/page-001.jpg) |
| 2 | 4871 | — | [原稿第2页](./source_pages/page-002.jpg) |
| 3 | 4825 | 图2 | [原稿第3页](./source_pages/page-003.jpg) |
| 4 | 4636 | — | [原稿第4页](./source_pages/page-004.jpg) |
| 5 | 3712 | 图3 | [原稿第5页](./source_pages/page-005.jpg) |
| 6 | 4106 | 图4 | [原稿第6页](./source_pages/page-006.jpg) |
| 7 | 4273 | 图5 | [原稿第7页](./source_pages/page-007.jpg) |
| 8 | 4426 | 表1 | [原稿第8页](./source_pages/page-008.jpg) |
| 9 | 3816 | 表2、表3 | [原稿第9页](./source_pages/page-009.jpg) |
| 10 | 3642 | — | [原稿第10页](./source_pages/page-010.jpg) |
| 11 | 3919 | — | [原稿第11页](./source_pages/page-011.jpg) |
| 12 | 3799 | — | [原稿第12页](./source_pages/page-012.jpg) |
| 13 | 3557 | — | [原稿第13页](./source_pages/page-013.jpg) |
| 14 | 3298 | — | [原稿第14页](./source_pages/page-014.jpg) |
| 15 | 3589 | — | [原稿第15页](./source_pages/page-015.jpg) |
| 16 | 3775 | — | [原稿第16页](./source_pages/page-016.jpg) |
| 17 | 1820 | 表4、表5 | [原稿第17页](./source_pages/page-017.jpg) |
| 18 | 2592 | 表6 | [原稿第18页](./source_pages/page-018.jpg) |
| 19 | 2565 | 图6 | [原稿第19页](./source_pages/page-019.jpg) |
| 20 | 2511 | 表7 | [原稿第20页](./source_pages/page-020.jpg) |
| 21 | 2651 | — | [原稿第21页](./source_pages/page-021.jpg) |
| 22 | 4554 | 表8、表9 | [原稿第22页](./source_pages/page-022.jpg) |
| 23 | 4045 | 表10 | [原稿第23页](./source_pages/page-023.jpg) |
| 24 | 1721 | 图7 | [原稿第24页](./source_pages/page-024.jpg) |
| 25 | 2918 | 表11 | [原稿第25页](./source_pages/page-025.jpg) |
| 26 | 2383 | 表12 | [原稿第26页](./source_pages/page-026.jpg) |
| 27 | 557 | 图8、图9 | [原稿第27页](./source_pages/page-027.jpg) |
| 28 | 1983 | 图10、表13 | [原稿第28页](./source_pages/page-028.jpg) |
| 29 | 2614 | 表14 | [原稿第29页](./source_pages/page-029.jpg) |
| 30 | 2485 | — | [原稿第30页](./source_pages/page-030.jpg) |
| 31 | 2183 | 表15 | [原稿第31页](./source_pages/page-031.jpg) |
| 32 | 2629 | — | [原稿第32页](./source_pages/page-032.jpg) |
| 33 | 2681 | 表16 | [原稿第33页](./source_pages/page-033.jpg) |
| 34 | 2832 | 表17 | [原稿第34页](./source_pages/page-034.jpg) |
| 35 | 2484 | — | [原稿第35页](./source_pages/page-035.jpg) |
| 36 | 2465 | — | [原稿第36页](./source_pages/page-036.jpg) |
| 37 | 2262 | — | [原稿第37页](./source_pages/page-037.jpg) |
| 38 | 2057 | 图11 | [原稿第38页](./source_pages/page-038.jpg) |
| 39 | 2243 | 图12 | [原稿第39页](./source_pages/page-039.jpg) |
| 40 | 2257 | 图13 | [原稿第40页](./source_pages/page-040.jpg) |
| 41 | 2396 | 图14 | [原稿第41页](./source_pages/page-041.jpg) |
| 42 | 144 | 图15 | [原稿第42页](./source_pages/page-042.jpg) |
| 43 | 153 | 图16 | [原稿第43页](./source_pages/page-043.jpg) |
| 44 | 1467 | 图17 | [原稿第44页](./source_pages/page-044.jpg) |
| 45 | 1574 | 图18 | [原稿第45页](./source_pages/page-045.jpg) |
| 46 | 1954 | 图19 | [原稿第46页](./source_pages/page-046.jpg) |
| 47 | 2222 | 图20 | [原稿第47页](./source_pages/page-047.jpg) |
| 48 | 2547 | 图21 | [原稿第48页](./source_pages/page-048.jpg) |
| 49 | 2655 | 图22 | [原稿第49页](./source_pages/page-049.jpg) |
| 50 | 1766 | 图23 | [原稿第50页](./source_pages/page-050.jpg) |
| 51 | 1972 | 图24 | [原稿第51页](./source_pages/page-051.jpg) |
| 52 | 2292 | 图25 | [原稿第52页](./source_pages/page-052.jpg) |
| 53 | 1943 | 图26 | [原稿第53页](./source_pages/page-053.jpg) |
| 54 | 1996 | 图27 | [原稿第54页](./source_pages/page-054.jpg) |
| 55 | 133 | 图28 | [原稿第55页](./source_pages/page-055.jpg) |
| 56 | 141 | 图29 | [原稿第56页](./source_pages/page-056.jpg) |
| 57 | 131 | 图30 | [原稿第57页](./source_pages/page-057.jpg) |
| 58 | 139 | 图31 | [原稿第58页](./source_pages/page-058.jpg) |
| 59 | 126 | 图32 | [原稿第59页](./source_pages/page-059.jpg) |
| 60 | 1416 | 图33 | [原稿第60页](./source_pages/page-060.jpg) |
| 61 | 133 | 图34 | [原稿第61页](./source_pages/page-061.jpg) |
| 62 | 141 | 图35 | [原稿第62页](./source_pages/page-062.jpg) |
| 63 | 1657 | 图36、图37、图38 | [原稿第63页](./source_pages/page-063.jpg) |
| 64 | 1471 | 图39、图40 | [原稿第64页](./source_pages/page-064.jpg) |
| 65 | 634 | 图41、图42 | [原稿第65页](./source_pages/page-065.jpg) |

## 原始资料与再核查路径

- `原始论文.pdf`：上传 PDF 的逐字节副本。
- `英文全文_逐页提取.md`：含全部原文页序及页面截图。
- `英文原文_纯文本.txt`：便于全文搜索与差异检查。
- `原稿逐页对照.md`：每页完整英文文本和整页图像。
- `图表索引.md`：所有截图的原文图题与对应 PDF 页数。
- `assets/图表索引.json`：机器可读的图表文件及裁切坐标清单。
- `images/`：原文图表截图。
- `source_pages/`：全部原稿整页截图。

**原稿 SHA-256：** `97228beb0798bb021f70d9c973ba5dc13d31667bef71ca1c282099bfb7e0694f`
