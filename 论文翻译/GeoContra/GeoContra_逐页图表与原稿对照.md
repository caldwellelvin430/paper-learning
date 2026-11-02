# GeoContra：逐页图表、算法与原文图像对照

> PDF 共 **19 页**；本文档按照 PDF 物理页码逐页列出所有检测到的 Figure、Table、Algorithm、Listing。下面的每张图片均是从上传 PDF 直接渲染或裁切，没有重绘或更改数值。


## 原稿第 1 页

**整页原稿截图（第 1 页，含该页全部文字与图表）：**

![PDF第1页](./source_pages/page-001.jpg)


## 原稿第 2 页

**整页原稿截图（第 2 页，含该页全部文字与图表）：**

![PDF第2页](./source_pages/page-002.jpg)


## 原稿第 3 页

**整页原稿截图（第 3 页，含该页全部文字与图表）：**

![PDF第3页](./source_pages/page-003.jpg)


## 原稿第 4 页

**整页原稿截图（第 4 页，含该页全部文字与图表）：**

![PDF第4页](./source_pages/page-004.jpg)


## 原稿第 5 页

### 图 1：GeoContra 的整体框架与地理契约驱动的修复循环

![原稿图1](./images/figure-1-p05.png)

> 原文标题：Figure 1: Overview of GeoContra. The pipeline begins with a natural-language GIS task and local geospatial data, constructs a geography-grounded task contract containing dataset schemas, CRS information, expected outputs, topology and metric constraints, spatial-relation semantics, expected GIS operations, and forbidden shortcuts, then asks an LLM to generate Python GIS code. The generated program

**整页原稿截图（第 5 页，含该页全部文字与图表）：**

![PDF第5页](./source_pages/page-005.jpg)


## 原稿第 6 页

### 算法 1：构建 GeoContra-Real 数据集的算法

![原稿算法1](./images/algorithm-1-p06.png)

> 原文标题：Algorithm 1. Constructing GeoContra-Real

**整页原稿截图（第 6 页，含该页全部文字与图表）：**

![PDF第6页](./source_pages/page-006.jpg)


## 原稿第 7 页

### 图 2：静态、运行时和语义验证的详细修复引擎

![原稿图2](./images/figure-2-p07.png)

> 原文标题：Figure 2: Detailed verification and repair engine. The static checker inspects AST structure, CRS-unit handling, field-schema consistency, spatial predicate direction, topology-sensitive op- eration patterns, forbidden method patterns, and network shortcuts. The runtime checker exe- cutes the generated program and validates tracebacks, timeouts, output-file existence, readable CSV/GeoJSON artifact

**整页原稿截图（第 7 页，含该页全部文字与图表）：**

![PDF第7页](./source_pages/page-007.jpg)


## 原稿第 8 页

### 算法 2：验证器引导的程序生成与修复

![原稿算法2](./images/algorithm-2-p08.png)

> 原文标题：Algorithm 2. Verifier-Guided Generation and Repair

### 算法 3：静态检查器

![原稿算法3](./images/algorithm-3-p08.png)

> 原文标题：Algorithm 3. Static Checker

**整页原稿截图（第 8 页，含该页全部文字与图表）：**

![PDF第8页](./source_pages/page-008.jpg)


## 原稿第 9 页

### 算法 4：运行时检查器

![原稿算法4](./images/algorithm-4-p09.png)

> 原文标题：Algorithm 4. Runtime Checker

**整页原稿截图（第 9 页，含该页全部文字与图表）：**

![PDF第9页](./source_pages/page-009.jpg)


## 原稿第 10 页

### 算法 5：任务语义验证器

![原稿算法5](./images/algorithm-5-p10.png)

> 原文标题：Algorithm 5. Semantic Verifier

### 算法 6：生成修复提示

![原稿算法6](./images/algorithm-6-p10.png)

> 原文标题：Algorithm 6. Repair Prompt Generation

**整页原稿截图（第 10 页，含该页全部文字与图表）：**

![PDF第10页](./source_pages/page-010.jpg)


## 原稿第 11 页

**整页原稿截图（第 11 页，含该页全部文字与图表）：**

![PDF第11页](./source_pages/page-011.jpg)


## 原稿第 12 页

### 表 1：GeoContra-Real 任务家族与难度组成

![原稿表1](./images/table-1-p12.png)

> 原文标题：Table 1: GeoContra-Real benchmark composition by task family and difficulty.

### 表 2：闭源模型整体实验结果

![原稿表2](./images/table-2-p12.png)

> 原文标题：Table 2: Closed-model overall results on 7,079 paired tasks per family.

**整页原稿截图（第 12 页，含该页全部文字与图表）：**

![PDF第12页](./source_pages/page-012.jpg)


## 原稿第 13 页

### 图 3：各任务族的空间正确率提升

![原稿图3](./images/figure-3-p13.png)

> 原文标题：Figure 3: Spatial-correctness gains by task family and closed-model family. Each cell is Geo- Contra minus LLM-only in percentage points.

**整页原稿截图（第 13 页，含该页全部文字与图表）：**

![PDF第13页](./source_pages/page-013.jpg)


## 原稿第 14 页

### 表 3：开源模型在 300 个任务上的空间正确率

![原稿表3](./images/table-3-p14.png)

> 原文标题：Table 3: Open-model spatial correctness on 300 formal tasks per setting.

### 图 4：11 个开源模型的空间正确率对比

![原稿图4](./images/figure-4-p14.png)

> 原文标题：Figure 4: Open-model spatial correctness. Each model has 300 LLM-only and 300 GeoContra runs.

**整页原稿截图（第 14 页，含该页全部文字与图表）：**

![PDF第14页](./source_pages/page-014.jpg)


## 原稿第 15 页

### 图 5：最终静态、运行时与语义违规数量

![原稿图5](./images/figure-5-p15.png)

> 原文标题：Figure 5: Average final violations per task after the last generation or repair round.

**整页原稿截图（第 15 页，含该页全部文字与图表）：**

![PDF第15页](./source_pages/page-015.jpg)


## 原稿第 16 页

### 表 4：失败与修复案例分析

![原稿表4](./images/table-4-p16.png)

> 原文标题：Table 4: Representative closed-model cases where LLM-only fails and GeoContra succeeds.

**整页原稿截图（第 16 页，含该页全部文字与图表）：**

![PDF第16页](./source_pages/page-016.jpg)


## 原稿第 17 页

**整页原稿截图（第 17 页，含该页全部文字与图表）：**

![PDF第17页](./source_pages/page-017.jpg)


## 原稿第 18 页

### 表 5：大波士顿 15 个研究区的数据多样性统计

![原稿表5](./images/table-5-p18.png)

> 原文标题：Table 5: Diversity statistics across the 15 Greater Boston study areas. Densities are normalized by area in square kilometers.

**整页原稿截图（第 18 页，含该页全部文字与图表）：**

![PDF第18页](./source_pages/page-018.jpg)


## 原稿第 19 页

**整页原稿截图（第 19 页，含该页全部文字与图表）：**

![PDF第19页](./source_pages/page-019.jpg)

