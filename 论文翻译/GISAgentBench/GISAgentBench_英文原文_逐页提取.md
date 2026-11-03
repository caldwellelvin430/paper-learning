# GISAgentBench — 英文原文逐页提取

> 对照来源：`GISAgentBench.pdf`；总页数 29。此文件是 PDF 的全文文本提取，保留原有的 API 标识、公式符号、参考文献及附录内容；复杂图表以中文版文档中的原图截图为准。


---

## PDF 第 1 / 29 页

```text
GISAgentBench: A Practitioner-Sourced Benchmark for Evaluating LLM Agents
on GIS Tasks
Abhinav Pothuri1
, Zhe Jiang1∗
, Zelin Xu1
, Di Yang2
1
Department of Computer & Information Science & Engineering, University of Florida
2
Department of Geography, University of Florida
Abstract
Geographic Information System (GIS) professionals rely on
multi-step spatial analysis workflows to support decision-
making in urban planning, disaster response, and environ-
mental monitoring. The process is tedious, time-consuming,
and error-prone. While recent large language model (LLM)
agents equipped with external tools have the potential to auto-
mate geospatial analysis, their ability to perform realistic GIS
workflows remains largely unexplored. Existing GIS agent
benchmarking datasets are mostly drawn from textbooks, tu-
torials, or LLM-generated seeds, and remain limited in size
and trajectory depth. More importantly, none provides ground
truth outputs. They therefore rely on surrogate signals such as
code similarity, trajectory matching, or LLM and VLM judges,
which can conflate workflow resemblance with task correct-
ness. To address this gap, we introduce GISAgentBench, a
benchmark of 349 multi-step GIS tasks curated from GIS
Stack Exchange and instantiated on real public data across
six selected geographic areas of interest. Each task ships with
an executable reference trajectory and an exact ground truth
output file, enabling strict, deterministic, tolerance-aware out-
put matching beyond LLM judging. Evaluations of six LLM
models reveal that realistic GIS workflows remain challeng-
ing: the best agent completes only 32.7% of tasks under strict
tolerance-aware scoring, although most models produce out-
puts that are close to the ground truth.
1 Introduction
A geographic information system (GIS) is a software sys-
tem for storing, managing, analyzing, and visualizing spa-
tially referenced data. It plays a crucial role in addressing
grand societal challenges such as disaster management, ur-
ban planning, land administration, climate adaptation, and
precision agriculture (Goodchild 2010). For example, the
Federal Emergency Management Agency delineates flood
hazard zones by analyzing terrain, hydrography, and par-
cel data in GIS, producing the maps that underpin the Na-
tional Flood Insurance Program and its $1.3 trillion of cov-
erage (Federal Emergency Management Agency 2026). Yet
such products are rarely the result of a single operation. Even
a well-defined task, such as identifying census tracts within
a floodplain and computing their demographic overlap, re-
quires an analyst to gather heterogeneous datasets, reconcile
∗
Contact author: Zhe Jiang zhe.jiang@ufl.edu
their coordinate systems and schemas, select and parameter-
ize operations from toolboxes and libraries of hundreds of
primitives, and execute a long chain of geoprocessing steps.
Today, such analyses are performed daily by a large profes-
sional workforce of GIS analysts and technicians, working
either through graphical map interfaces or scripted geopro-
cessing pipelines (U.S. Bureau of Labor Statistics 2026).
Unfortunately, professional GIS work remains tedious, time-
consuming, and error-prone. Recently, large language mod-
els (LLMs) capable of tool use (Schick et al. 2024) and
multi-step reasoning (Yao et al. 2023; Wei et al. 2022) have
provided a promising alternative that could drive a major
paradigm shift. Given a natural-language request, an LLM
agent can in principle decompose the task into spatial oper-
ations, invoke GIS tools to execute the workflow, and return
the final spatial product. Early systems that generate and
execute GIS code or spatial queries demonstrate this poten-
tial (Li and Ning 2024; Zhang et al. 2023; Chen et al. 2024b).
An agent that performed such workflows reliably would both
automate routine geospatial labor and make advanced spatial
analysis accessible to non-specialists.
However, GIS tasks are uniquely challenging for
LLM agents. Professional GIS work is inherently cross-
disciplinary, drawing simultaneously on geospatial infor-
mation science, spatial databases, GIS software, machine
learning, statistics, and remote sensing. This interdisci-
plinary character produces failure modes largely absent from
general-purpose code generation and agent benchmarks.
First, an undetected coordinate reference system (CRS) mis-
match silently invalidates every distance, area, and intersec-
tion computed downstream. Second, practitioner requests are
often underspecified, leaving the intended spatial predicate,
measurement unit, or attribute schema to be inferred. A re-
quest for features inside a boundary, for example, does not
say whether features touching that boundary should be re-
tained. Third, real spatial data are imperfect. Rasters carry
NoData masks, and vector layers contain invalid, overlap-
ping, or multipart geometries. Fourth, GIS analyses are long
chains of interdependent operations, so an error introduced
early propagates through every subsequent step. A workflow
can therefore run to completion without a single error and
still be spatially wrong. Finally, evaluation is itself difficult,
because correct outputs may legitimately differ in geometric
representation or fall within numerical tolerances. This raises
arXiv:2608.01645v1
[cs.AI]
3
Aug
2026
```

---

## PDF 第 2 / 29 页

```text
Table 1: Comparison of existing GIS agent benchmarks.
Benchmark # Tasks Source # Tools Traj. Length Evaluation Method Challenge Tags
GeoAnalystBench 50 Textbook & Tutorials unknown Avg 6; Max 10 CodeBLEU to match
code
–
GeoBenchX 202 LLM-generated from
a few industry seeds
23 Avg 5; Max 14 LLM judge to match
trajectory
Post hoc error
analysis
GeoAgentBench 53 Textbook & Tutorials 117 Avg 7; Max 17 Trajectory match + VLM
judge on map appearance
–
GISAgentBench 349 GIS Stack Exchange 128 Avg 12; Max 43 Tolerance-aware output
matching + traj. match
Pre-identified
human pitfalls
a fundamental open question: how reliably can frontier LLM
agents solve the multi-step GIS tasks that practitioners face
in real-world settings?
Existing benchmarks cannot answer this question. Systems
that apply LLMs to GIS code generation, spatial database
querying, urban analytics, and map understanding (Li and
Ning 2024; Zhang et al. 2023; Li et al. 2024; Feng et al.
2024) are largely demonstrations on small handcrafted ex-
amples rather than standardized evaluations. General agent
and code benchmarks (Liu et al. 2024; Mialon et al. 2023;
Yao et al. 2022; Qin et al. 2023; Chen et al. 2021b; Lai
et al. 2023; Jimenez et al. 2024) define correctness over
text answers, web interactions, or unit tests, none of which
capture spatial outputs, and evaluations of geospatial code
generation (Gramacki, Martins, and Szymanski 2024; Hou
et al. 2025) measure code synthesis rather than the full loop
of planning, tool selection, geoprocessing, and output val-
idation. Spatial reasoning benchmarks (Chen et al. 2021a;
Huang et al. 2019; Chen et al. 2024a; Xu et al. 2025) assess
geographic knowledge or map interpretation without tool-
mediated geoprocessing. The closest works are GeoAnalyst-
Bench (Zhang et al. 2025), GeoBenchX (Krechetova and
Kochedykov 2025), and GeoAgentBench (Yu et al. 2025),
which evaluate tool-calling agents on multi-step geospatial
tasks (Table 1). However, their tasks are drawn from text-
books, tutorials, or LLM-generated seeds rather than from
practice, and remain limited in size (50 to 202 tasks) and
depth (reference trajectories of 5 to 7 tool calls on average, at
most 17). More importantly, none of them provides an exe-
cutable ground truth output. They therefore rely on surrogate
signals such as code similarity, trajectory matching, or LLM
and VLM judges, which can conflate workflow resemblance
with task correctness. In addition, none of them identifies in
advance where a task is prone to error.
To fill this gap, we introduce GISAgentBench, a bench-
mark of 349 multi-step GIS tasks curated from GIS Stack
Exchange (Stack Exchange, Inc. 2026), the largest public
question-and-answer forum for GIS practitioners, and instan-
tiated on real public datasets across six geographic areas of
interest. To our knowledge, it is the first GIS agent benchmark
built from community-generated practitioner questions and
scored against exact ground truth outputs. Practitioner-based
sourcing gives our benchmark five distinguishing features.
First, the tasks are real-world problems posed by working
analysts, rather than textbook or tutorial exercises. Second,
each task is paired with an executable reference solution
and an exact ground truth output file, so that agents are
scored by strict, deterministic, tolerance-aware output match-
ing. Third, we also evaluate agent trajectories alongside final
outputs, which separates planning failures from execution
failures. Fourth, our benchmark is substantially larger and
deeper than related work, with 349 tasks whose reference
solutions require up to 43 API calls (11.7 on average), com-
pared with around 100 tasks and far shorter trajectories in
prior work. Finally, and most importantly, we annotate each
task in advance with practical caveats, namely the CRS, unit,
NoData, boundary, and geometry pitfalls drawn from the
practical experience of GIS professionals. These conditions
are highly error-prone even for human experts, and anno-
tating them allows us to evaluate whether LLM agents fall
into the same traps as human practitioners in failture mode
analysis. Using this benchmark, we evaluate six LLM agents
under a standardized framework with a fixed harness of 128
GIS APIs, deterministic tolerance-aware output matching,
and trajectory-level diagnostics. The results show that real-
istic GIS workflows remain far beyond the current capability
frontier, with the best agent solving only 32.7% of tasks un-
der strict scoring. A quantitative closeness analysis further
reveals that agents recover geometry far more reliably than
numeric attributes and complete row sets, and that our pre-
annotated pitfalls are predictive of failure, with geometry
and topology errors and CRS misalignment the most damag-
ing. The complete task set, reference trajectories, and ground
truth outputs will be released publicly.
2 GIS Agent Benchmark
GISAgentBench is a benchmark of 349 multi-step GIS tasks
sourced from practitioner questions on GIS Stack Exchange
and instantiated on real public spatial data across six geo-
graphic areas of interest. Each task pairs a practitioner-style
problem statement with its input datasets, an output contract
specifying the required file and how it will be scored, an exe-
cutable reference trajectory, and expert annotations recording
which task family the problem belongs to and which practical
pitfalls it exercises.
Tasks are organized into five families:
• Spatial Joining & Geocoding (SJ&G): associating
```

---

## PDF 第 3 / 29 页

```text
SPATIAL JOINING &
GEOCODING
For each NYC address point,
find the borough polygon that
contains it and attach the
borough's ID.
address points
borough boundaries
points tagged with borough
ID
SPATIAL OVERLAY &
SUITABILITY
Buffer each NYC census tract
by 400 m and compute the
percent of the buffered area
covered by parks.
census tracts
parks
% covered by parks
TERRAIN & HYDROLOGICAL
ANALYSIS
From elevation data, extract
polygons of contiguous area
where slope is under 5%
inside city limits.
elevation
city boundary
low-slope area
SPATIAL PATTERN ANALYSIS
For each hospital, intersect a
1 km buffer with its bounded
Voronoi cell within
neighborhood limits.
hospitals
neighborhoods
clipped service buffers
REMOTE SENSING &
IMAGE ANALYSIS
Compute mean NDVI from
aerial-imagery pixels that fall
within each municipality
polygon.
aerial imagery
municipalities
mean NDVI by municipality
TASK FAMILY
TASK
DESCRIPTION
INPUT DATA
REFERENCE
TRAJECTORY
OUTPUT DATA
CRS Reproject → … →
Join by Location (point-in-
polygon) → … → Export to CSV
CRS Reproject → … → Buffer
(400 m) → Dissolve → Intersect
→ Statistics Table → …
CRS Reproject → Slope → … →
Clip Raster → Raster Calculator
(threshold) → Polygonize Raster
→ …
CRS Reproject → … → Voronoi
Polygons → Clip Features →
Buffer (1 km) → Intersect → …
CRS Reproject → Rearrange
Bands → Raster Calculator
(NDVI) → … → Zonal Statistics
(mean) → Join by Field → …
Figure 1: Illustrative examples of GISAgentBench tasks.
records, coordinates, or features across spatial and tab-
ular datasets (96 tasks).
• Spatial Overlay & Suitability Analysis (SO&SA): com-
bining layers through predicates, buffers, intersections, or
selection criteria to identify areas satisfying spatial con-
straints (93 tasks).
• Terrain Modeling & Hydrological Analysis
(TM&HA): deriving products from elevation data,
such as slope, drainage, watershed, and flow-related
outputs (63 tasks).
• Spatial Pattern Analysis (SPA): measuring geometric,
topological, or distributional structure, including cluster-
ing, proximity patterns, thinning, and morphology (52
tasks).
• Remote Sensing & Image Analysis (RS&IA): process-
ing raster imagery or derived indices through masking,
classification, pixel-level computation, or zonal summa-
rization (45 tasks).
Figure 1 shows one example from each family, which
makes the shape of a task concrete. An agent receives a re-
quest phrased as an analyst would pose it, together with a set
of data files, and must return a specific file whose columns,
coordinate system, and numeric tolerances are fixed in ad-
vance. Solving it means composing named geoprocessing
operations, each of which reads one or more layers—tables
whose rows carry a geometry—and writes a new one. Some
operations relate layers by position, such as finding which
points fall inside which polygons. Others construct new ge-
ometry, such as the zone within a fixed distance of a feature.
Others summarize a grid of pixels into one value per re-
gion. Because each call consumes the file the previous call
produced, a task is a dependent chain rather than a set of in-
dependent queries, and what is scored is a spatial file rather
than a string.
GIS API harness: Agents interact with spatial data exclu-
sively through a fixed harness of 128 GIS APIs, backed
by QGIS through its command-line interface, including its
GDAL-backed algorithms, together with GeoPandas, Raste-
rio, Shapely, pandas/NumPy, and SciPy. Every API is ex-
posed through a uniform interface with typed arguments and
a documented return contract, and the set is identical across
all evaluated models. Table 2 summarizes its functional cov-
erage. Appendix C lists all 128 with descriptions and param-
eters. This fixed-harness design is central to our evaluation:
every task is verified to be solvable with the provided APIs,
so tool availability is never a confounding factor; and hold-
ing the harness constant isolates an agent’s ability to select,
parameterize, and sequence GIS operations from differences
in what harness it can reach.
```

---

## PDF 第 4 / 29 页

```text
Table 2: Functional coverage of the 128-API harness.
Category # Category #
Geometry construction 22 Spatial join 6
Attribute & table ops 15 Inspection 6
Raster processing 15 Zonal statistics 5
Raster–vector 11 CRS & reprojection 4
Buffers & proximity 10 Network analysis 4
Terrain & hydrology 9 Density surfaces 3
Vector overlay 8 Input/output 3
Geometry cleaning 7 Total 128
GIS Stack Exchange
~110,000 threads
1
Coarse Filter
→ ~27,000
2
LLM Refinement
→ ~6,000 → ~2,000
3
TASK CONSTRUCTION
Task Template
Recast to 6 AOIs
→ ~1,000
4
Reference Solutions
2–43 calls · mean 11.7 calls
5
Deduplication & QC
→ 349 tasks
6
Ground Truth Output Files
Expert Verification loop
→ tables · geometry · rasters
Figure 2: GISAgentBench construction pipeline.
2.1 Task Set Selection and Construction
GISAgentBench is built from GIS Stack Exchange, the largest
public question-and-answer forum for GIS practitioners. Un-
like benchmarks that rely on textbook, tutorial, or synthetic
tasks, it is grounded in problems encountered during opera-
tional geospatial analysis: questions are posed organically by
working analysts, reflecting authentic analytical needs and
workflow complexity, while community-vetted answers pro-
vide a foundation for constructing reference solutions.
Figure 2 summarizes the construction pipeline. From ap-
proximately 110,000 crawled threads, a deterministic filter
retains roughly 27,000 by scoring each thread on GIS ter-
minology, workflow verbs, and data context, and rejecting
posts that are too short, that concern software setup or map
display rather than spatial analysis, or that repeat an earlier
post. Two LLM screening passes with GPT-5-mini follow: a
lightweight triage discards threads without a concrete spatial
goal, leaving about 6,000, and a stricter pass retains only
problems that require more than a single operation, are re-
producible from fixed inputs, and can be moved to new data
without altering the underlying question, leaving roughly
2,000 candidates. Both screening prompts were developed
iteratively rather than written once: a GIS expert reviewed
initial batches of 50–100 threads against each draft of the cri-
teria, and recurring errors were folded back into the prompts
until the retained set matched expert judgment. Each retained
thread is then cast into a common benchmark task template: a
practitioner-style prompt, the input data in a selected area of
interest, the task parameters, and an output contract naming
the required file, columns, spatial reference, and tolerances.
After recasting the task description into a fixed set of areas
of interest (Section 2.2) and generating reference trajectories
(Section 2.3), we remove tasks whose reference cannot be
Table 3: Task family by practitioner caveat.
CRS Bound. Geom. NoData Unit none Tasks
SJ&G 86 68 44 3 13 1 96
SO&SA 71 47 30 12 19 4 93
SPA 31 21 20 10 8 3 52
RS&IA 16 22 6 28 3 4 45
TM&HA 40 22 13 37 4 4 63
Total 244 180 113 90 47 16 349
produced from the declared inputs, whose trajectories are
duplicated, or whose trajectories prove too short to require
multi-step reasoning. We finally collapse tasks that reduce to
the same ordered sequence of operations, leaving a final set of
349 tasks. Appendix B gives the complete keyword dictio-
naries, filter thresholds, and screening and drafting prompts.
Each task is also tagged by GIS experts with the caveats
it exercises: CRS misalignment (244 tasks), boundary am-
biguity (180), geometry and topology errors (113), NoData
values (90), and unit mismatch (47). Annotating pitfalls in
advance lets us ask whether LLM agents fall into the same
traps as human experts. Table 3 cross-tabulates the two anno-
tations, and the caveat profile follows the data model rather
than being uniform. The vector families are dominated by
coordinate-system and geometry problems: 90% of Spatial
Joining & Geocoding tasks carry a CRS caveat and 46% a
geometry one, while NoData is almost absent from them (3
of 96). The raster families invert this, with NoData in 59%
of Terrain Modeling and 62% of Remote Sensing tasks.
2.2 Geographic Recasting into Selected Areas of
Interest
Because the source threads are public, their accepted answers
are indexed on the web and may sit in any model’s pretraining
data. Geographic recasting mitigates that leakage: an agent
receives the problem posed over data the original thread never
used, so no published answer exists for it. Schema normal-
ization on import extends the same protection to field names.
In this process, we preserve a task’s analytical objective, spa-
tial predicates, and data roles while changing the geography,
datasets, schemas, and resulting numbers.
This demands target geographies that are individually rich
and collectively diverse. The six areas of interest (Table 4)
were chosen to span the task families rather than repeat
one layer stack: dense urban-coastal and cadastral settings
for joins, overlays, and topology repair; a mountain front
and a low-relief floodplain for terrain, hydrology, and least-
cost analysis; an engineered water-control landscape for con-
strained routing; and a nationally standardized European en-
vironment that tests the same operations outside U.S. data
conventions. Each area draws on public national, municipal,
and European open-data portals at operational scale, span-
ning vector, raster, and tabular layers. To ensure that a task
retains the caveat (pitfall) tagged in its source GIS Stack
Exchange post, a few input datasets are slightly modified.
Appendix D lists every data source, the principal layers with
exact feature counts, and every raster with its full character-
```

---

## PDF 第 5 / 29 页

```text
Table 4: The six areas of interest. Appendix D details their
datasets and per-family task counts.
Area of interest Landscape Tasks
San Francisco
Bay Area
Dense urban coastal; bay
shoreline, terrain, imagery
99
Randstad,
Netherlands
Low-lying delta; nationally
standardized registries
91
New York City Dense urban; parcel- and
address-rich cadastre
51
Denver Front
Range
Mountain front; wildland–urban
interface, hazards
40
Houston–Harris Flat coastal plain; floodplain and
drainage network
40
South Florida Engineered water control;
low-relief coastal wetland
28
istics.
2.3 Ground Truth Reference Trajectory and
Output Generation
Each task ships with an executable reference trajectory and
the output file it produces, which are generated and verified
by the Claude Fable 5 model (a current frontier model that is
deliberately not among our evaluated agents). The released
trajectory is expressed entirely in the same 128-API harness
the agents are given, and is executed inside that harness to
materialize the ground truth output file. In order to cross-
check these outputs, we also provide Fable 5 direct access
to the input data and to free-form Python for deriving and
checking what the correct result should be. Across the bench-
mark these trajectories range from 2 to 43 API calls (mean
11.7) over 92 distinct input files, reflecting the compositional
depth of real practitioner workflows.
Quality assurance proceeds in two steps. First, an auto-
mated recheck statically validates every reference step against
the real API signatures, catching fake tools, misspelled argu-
ments, and unbound intermediate outputs. Second, and more
importantly, three GIS experts (in our author list) reviewed
the reference trajectories directly. Trajectories were not ac-
cepted merely because a model produced them or because
a command sequence ran to completion: they were hand-
traced step by step, with manual inspection of intermediate
outputs and visual checks of the resulting spatial outputs.
Expert review is what surfaced the defect classes that auto-
mated checks cannot see, such as a field calculation bound
to a column the upstream operation never produced, a slope
computed on an unprojected elevation model, or an output
contract keyed on a column the prompt never promised. Tasks
whose descriptions proved ambiguous, or whose specifica-
tion required revision to be solvable, were removed rather
than repaired in place. Appendix E documents the details.
3 Experimental Evaluation
3.1 Experimental Setup
Framework: We evaluate every model as a tool-using agent
in a single ReAct (Yao et al. 2023) loop implemented with
LangChain. Each of the 128 GIS APIs (Section 2) is regis-
tered as a typed tool, so every model sees the same interface.
The agent alternates between reasoning and acting until it
declares completion or exhausts its step budget, and every
tool call, argument, return value, and error is logged.
Metrics: For model output errors, we use strict Task Success
Rate (TSR), the fraction of tasks whose outputs match the
ground truth within a small tolerance threshold, and Quanti-
tative Closeness Score (QCS), which aggregates closeness
across both non-spatial and spatial attributes, with a miss-
ing output scoring 0. Non-spatial attributes include qualita-
tive (weighted F1) and quantitative (1 − sMAPE, symmet-
ric mean absolute percentage error). Rows are matched by
the output contract’s identifier columns rather than by posi-
tion, and attribute scores are computed over matched rows
only. Spatial attributes include raster grids and multi-point,
multi-polyline, and multi-polygon geometries, which is mea-
sured by instance F1 within an intersection-over-union (IoU)
threshold for areal outputs or a distance threshold for point
and line outputs. We additionally report trajectory close-
ness, which measures the similarity of key API calls at a
coarse functional category level. We also record trajectory
length and tool-call error rate. Appendix F gives full defini-
tions.
Infrastructure: Agent execution and all geoprocessing run
in a reproducible container on one node with 32 CPU cores
and 512 GB of memory. No GPUs are used: all six models
are accessed as hosted API services. Appendix A reports
the software environment, decoding parameters, and model
routing.
Models: We evaluate six agents—three closed-source
models (Gemini-3.1-Pro, Claude-4.6-Opus, GPT-5.4) and
three open-source models (DeepSeek-V4-Pro, Qwen3.6-
27B, GPT-OSS-120B)—on all 349 tasks. All six run under
the same harness, prompts, and 50-call budget with greedy
decoding, so measured differences reflect the models rather
than their scaffolding.
3.2 Overall Output Accuracy Analysis
Table 5 summarizes overall model performance and output
accuracy across the benchmark. No agent solves a third of
the tasks: Gemini-3.1-Pro leads at 0.327 strict TSR against
a six-model mean of 0.238, the three closed-source models
form a clear tier, and the open-source models reach roughly
half their success rate. Quantitative closeness preserves that
ranking but is two to three times higher throughout (0.380–
0.663), so a typical failed run recovers much of the intended
result rather than producing nothing.
Difficulty is driven by workflow type rather than model-
specific strengths: the family ranking is consistent across
all six models. Spatial Overlay & Suitability Analysis is
most tractable and Spatial Pattern Analysis hardest under
both metrics, its low closeness score indicating genuinely
wrong outputs rather than near misses. Terrain Modeling
inverts this—the second-lowest TSR but the highest quanti-
tative closeness of any family—because long raster pipelines
run to completion and land just outside tolerance.
Numeric closeness and categorical agreement are uni-
formly high and separate the models weakly (Tables 6 and 7);
```

---

## PDF 第 6 / 29 页

```text
Table 5: Model performance on tasks measured in strict TSR and quantitative closeness, overall and by task family.
Strict Task Success Rate (TSR) Quantitative Closeness Score (QCS)
Model All SJ&G SO&SA SPA RS&IA TM&HA All SJ&G SO&SA SPA RS&IA TM&HA
Gemini-3.1-Pro 0.327 0.385 0.383 0.231 0.378 0.190 0.663 0.676 0.680 0.623 0.703 0.628
Claude-4.6-Opus 0.295 0.302 0.344 0.231 0.333 0.238 0.606 0.569 0.640 0.570 0.546 0.688
DeepSeek-V4-Pro 0.275 0.312 0.277 0.212 0.244 0.286 0.595 0.571 0.620 0.483 0.636 0.658
GPT-5.4 0.229 0.188 0.309 0.173 0.200 0.238 0.538 0.515 0.606 0.381 0.524 0.619
Qwen3.6-27B 0.178 0.188 0.213 0.135 0.156 0.159 0.436 0.429 0.484 0.360 0.483 0.414
GPT-OSS-120B 0.123 0.125 0.138 0.115 0.133 0.095 0.380 0.365 0.377 0.346 0.361 0.437
Table 6: Non-spatial output accuracy.
Numerical Categorical Row
Model 1−sMAPE Weighted F1 Coverage
Gemini-3.1-Pro 0.903 0.980 0.871
Claude-4.6-Opus 0.859 0.983 0.866
DeepSeek-V4-Pro 0.888 0.984 0.890
GPT-5.4 0.878 0.945 0.868
Qwen3.6-27B 0.885 0.970 0.844
GPT-OSS-120B 0.880 0.963 0.833
Table 7: Spatial output accuracy by entity-level matching.
All spatial entities F1 by geometry type
Model Prec. Rec. F1 Point Line Polygon
Gemini-3.1-Pro 0.886 0.889 0.876 0.886 0.995 0.868
Claude-4.6-Opus 0.899 0.900 0.882 0.928 0.857 0.873
DeepSeek-V4-Pro 0.901 0.899 0.888 0.925 0.662 0.895
GPT-5.4 0.821 0.797 0.797 0.723 0.800 0.806
Qwen3.6-27B 0.883 0.847 0.855 0.835 1.000 0.843
GPT-OSS-120B 0.762 0.786 0.771 0.781 0.750 0.762
the discriminative signals are row coverage and geometry.
Spatial quality is comparatively strong—entity F1 reaches
0.76–0.89—so agents recover shapes far more reliably than
they recover complete, correctly valued row sets. Strict fail-
ures are therefore predominantly attribute- and coverage-
level rather than geometric.
3.3 Agentic Trajectory Evaluation
Figure 3 plots trajectory closeness against strict TSR. The two
are consistent with each other: models that perform more of
the required operations generally solve more tasks, and the
same three models lead on both measures (r = 0.99). They
nevertheless sit on very different scales, with agents covering
68–83% of the required operations while solving 12–33% of
tasks.
We report trajectory closeness as a diagnostic rather than
as a headline metric, and retain output error analysis as our
primary measure: scoring a produced output against an exact
ground truth is what distinguishes this benchmark from prior
work that can only compare trajectories. A formal trajectory
metric would need more than a correct reference trajectory,
since a task admits many equally valid trajectories that differ
in the order of independent steps and in the choice among
70 75 80 85
Trajectory closeness (%)
0.10
0.15
0.20
0.25
0.30
0.35
Strict
TSR
Gemini
Claude
DeepSeek
GPT-5.4
Qwen3.6
GPT-OSS
r = 0.99
Figure 3: Strict TSR against trajectory closeness. Agents
cover most required operations but convert few of them into
exactly correct outputs.
interchangeable operations. Defining equivalence over that
space is left to future work.
Execution statistics of model trajectories are given in Ta-
ble 8. Average trajectory length (number of tool calls) ranges
from 13.6 to 28.5. Qwen3.6027B has bigger tool call error
rates, likely due to a smaller model size. The rankings of tool
call error rate is also consistent with output errors.
3.4 Computational Cost of API Calls
Figure 4 shows how long each task takes to execute inside the
harness. We exclude the LLM API time costs due to inconsis-
tency of cloud API providers. The results show that task API
time cost is heavy-tailed: it spans four orders of magnitude,
from sub-second attribute edits to a 2,633 s spatial join over
939,821 address points, so the slowest 5% of runs consume
38% of all execution time and the mean sits at roughly twice
the median. Models differ only modestly in the execution
they trigger, from a median of 52 s per task for Claude-4.6-
Table 8: Execution statistics: mean tool calls per task and the
fraction of tool calls returning an error.
Model Mean tool calls Tool call error rate
Gemini-3.1-Pro 25.5 2.9%
Claude-4.6-Opus 15.8 3.1%
DeepSeek-V4-Pro 28.5 4.3%
GPT-5.4 13.6 4.0%
Qwen3.6-27B 22.4 12.0%
GPT-OSS-120B 22.1 9.5%
```

---

## PDF 第 7 / 29 页

```text
1 10 100 1000
Harness time per task (s, log scale)
Gemini
Claude
DeepSeek
GPT-5.4
Qwen3.6
GPT-OSS
Figure 4: Per-task harness time by model, log scale. Bars
mark the interquartile range, dots the median.
Opus to 72 s for Gemini-3.1-Pro, a spread of 1.38×. We also
measure the token consumption of different models, from
275k per task for GPT-5.4 to 829k for DeepSeek-V4-Pro.
Appendix G and H give the per-family breakdowns.
3.5 Failure Analysis
Each incorrect run with a trajectory carries a written diagnos-
tic note from scoring. We labelled those 1,381 notes against
a fixed set of mechanisms, allowing more than one label per
run; Table 9 reports how often each appears.
Failures are concentrated in the plan rather than in the in-
dividual call. A required operation is missing from 28.3% of
runs, and another 18.4% perform the right operations in the
wrong order, most often resampling a raster after computing
a slope from it rather than before. Wrong tool substitution
(13.4%) is similar in kind: the agent picks an operation that
sounds right but computes something else, typically a plain
spatial join where one that aggregates was needed, and a fur-
ther 14.4% repeat or undo steps without converging. Errors
inside a single call are rarer, at 7.8%, while 9.9% of runs
compute much of the answer but never write the required
file.
Three rows describe the limits of the analysis rather than
agent behaviour. Complete but unexplained (14.1%) covers
runs that perform every required operation in a valid order
yet still produce a wrong output, with no cause visible in the
sequence of tool names; shared task-level ceiling (13.8%)
covers tasks every model fails alike, which points at the
task rather than the agent; and 16.8% of notes could not be
assigned to any mechanism.
Performance by caveat. The data-integrity caveats are the
most damaging: pooled TSR falls to 0.152 on tasks tagged
with geometry and topology errors and 0.220 under CRS
misalignment, against 0.241 for NoData handling and 0.269–
0.277 for the language-level caveats (boundary ambiguity
and unit mismatch). Underspecified predicates produce syn-
tactically valid but semantically wrong outputs rather than
failed calls, so they cost accuracy without raising the error
rate.
Table 9: Failure mechanisms across 1,381 wrong-but-
attempted runs, pooled over all six models.
Failure mechanism Runs %
Missing required operation 391 28.3
Operation order violation 254 18.4
Redundant rework 199 14.4
Complete but unexplained 195 14.1
Shared task-level ceiling 190 13.8
Wrong tool substitution 185 13.4
Output never delivered 137 9.9
Parameter or formula error 108 7.8
Unrecovered tool failure 47 3.4
Native identifier violation 38 2.8
CRS / reprojection gap 38 2.8
Premature or unsorted delivery 26 1.9
Not specified 232 16.8
3.6 Case Studies
We conducted case studies for representative success and
failure examples for each task family, with map visualizations
of agent and reference outputs. Due to space limit, they are
provided in Appendix I.
4 Conclusion and Future Work
We introduced GISAgentBench, a benchmark for evaluat-
ing LLM agents on the multi-step spatial analysis that GIS
professionals perform in practice. Its 349 tasks come from
questions working analysts asked on a practitioner forum, re-
cast onto new geography so that no published answer exists
for any of them, and each ships with real spatial data, an
executable reference solution, a ground truth output file, and
expert annotations marking the pitfalls that cost practitioners
hours of debugging. Agents work through a fixed harness
of 128 GIS APIs and are scored deterministically against
the reference within task-declared tolerances, with no model
in the loop. Across six LLM agents, the strongest solves
32.7% of tasks fully, and failures are dominated by omitted
and mis-ordered operations rather than malformed calls, ev-
idence that capability is limited by workflow planning rather
than by access to GIS functionality.
Future work will extend the harness beyond open-source
libraries to commercial GIS libraries such as ArcGIS Tool-
box, which reach operations our present API set does not. We
will broaden geographic coverage beyond the predominantly
U.S. areas of interest used here. We will also evaluate new
frontier models as they are released, so that the benchmark
tracks the capability frontier rather than a single snapshot of
it. Evaluating open-ended and purely cartographic products,
which deterministic ground truth output matching cannot
score, remains open.
References
Chen, B.; Xu, Z.; Kirmani, S.; Ichter, B.; Driess, D.; Florence,
P.; Sadigh, D.; Guibas, L.; and Xia, F. 2024a. SpatialVLM:
Endowing Vision-Language Models with Spatial Reasoning
Capabilities. arXiv preprint arXiv:2406.13537.
```

---

## PDF 第 8 / 29 页

```text
Chen, J.; Tang, J.; Qin, J.; Liang, X.; Liu, L.; Xing, E.; and
Lin, L. 2021a. GeoQA: A Geometric Question Answering
Benchmark Towards Multimodal Numerical Reasoning. In
Findings of the Association for Computational Linguistics:
ACL-IJCNLP.
Chen, M.; Tworek, J.; Jun, H.; Yuan, Q.; Pinto, H. P. d. O.;
Kaplan, J.; Edwards, H.; Burda, Y.; Joseph, N.; Brockman,
G.; et al. 2021b. Evaluating Large Language Models Trained
on Code. arXiv preprint arXiv:2107.03374.
Chen, Y.; Wang, W.; Lobry, S.; and Kurtz, C. 2024b. An
LLM Agent for Automatic Geospatial Data Analysis. arXiv
preprint arXiv:2410.18792.
City and County of Denver. 2026. Denver Open Data. https:
//opendata-geospatialdenver.hub.arcgis.com.
City and County of San Francisco. 2026. San Francisco Open
Data. https://data.sfgov.org.
City of New York. 2026. NYC Open Data. https://data.
cityofnewyork.us.
Colorado Department of Public Health and Environment.
2026. Colorado Geospatial Open Data. https://data-cdphe.
opendata.arcgis.com.
Federal Emergency Management Agency. 2026. FEMA
National Flood Hazard Layer. https://hazards.fema.gov/gis/
nfhl/rest/services/public/NFHL/MapServer.
Feng, J.; Liu, T.; Du, Y.; Guo, S.; Lin, Y.; and Li, Y. 2024.
CityGPT: Empowering Urban Spatial Cognition of Large
Language Models. arXiv preprint arXiv:2406.13948.
Goodchild, M. F. 2010. Towards Geodesign: Repurposing
Geography for the Design Professions. ESRI Press.
Gramacki, P.; Martins, B.; and Szymanski, B. 2024. Eval-
uation of Code LLMs on Geospatial Code Generation. In
Proceedings of the ACM SIGSPATIAL International Work-
shop on Advances in Resilient and Intelligent Cities.
Harris County, Texas. 2026. Harris County Open Data. https:
//geo-harriscounty.opendata.arcgis.com.
Hou, S.; Shen, Z.; Zhao, A.; Liang, J.; Gui, Z.; Guan, X.;
Li, R.; and Wu, H. 2025. GeoCode-GPT: A Large Language
Model for Geospatial Code Generation Tasks. International
Journal of Applied Earth Observation and Geoinformation.
Huang,Z.; Shen,Y.;Li, X.;Wei, Y.;Cheng,G.; Zhou,L.;Dai,
X.; and Qu, Y. 2019. GeoSQA: A Benchmark for Scenario-
based Question Answering in the Geography Domain at High
School Level. In Proceedings of the Conference on Empirical
Methods in Natural Language Processing and the Interna-
tional Joint Conference on Natural Language Processing,
5866–5871.
Jimenez, C. E.; Yang, J.; Wettig, A.; Yao, S.; Pei, K.; Press,
O.; and Narasimhan, K. 2024. SWE-bench: Can Language
Models Resolve Real-World GitHub Issues? arXiv preprint
arXiv:2310.06770.
Krechetova, V.; and Kochedykov, D. 2025. GeoBenchX:
Benchmarking LLMs in Agent Solving Multistep Geospatial
Tasks. In Proceedings of the ACM SIGSPATIAL Interna-
tional Workshop on Generative and Agentic AI for Multi-
Modality Space-Time Intelligence, 27–35.
Lai, Y.; Li, C.; Wang, Y.; Zhang, T.; Zhong, R.; Zettlemoyer,
L.; Yih, W.-t.; Fried, D.; Wang, S.; and Yu, T. 2023. DS-1000:
A Natural and Reliable Benchmark for Data Science Code
Generation. In Proceedings of the International Conference
on Machine Learning.
Li, Z.; and Ning, H. 2024. LLM-Geo: Autonomous GIS with
Large Language Models. Transactions in GIS.
Li, Z.; Xia, L.; Tang, J.; Xu, Y.; Shi, L.; Xia, L.; Yin, D.;
and Huang, C. 2024. UrbanGPT: Spatio-Temporal Large
Language Models. In Proceedings of the ACM SIGKDD
International Conference on Knowledge Discovery and Data
Mining.
Liu, X.; Yu, H.; Zhang, H.; Xu, Y.; Lei, X.; Lai, H.; Gu, Y.;
Ding, H.; Men, K.; Yang, K.; et al. 2024. AgentBench: Eval-
uating LLMs as Agents. In Proceedings of the International
Conference on Learning Representations.
Mialon, G.; Dessì, R.; Lomeli, M.; Nalmpantis, C.; Pasunuru,
R.; Raileanu, R.; Rozière, B.; Schick, T.; Dwivedi-Yu, J.; Ce-
likyilmaz, A.; et al. 2023. GAIA: A Benchmark for General
AI Assistants. arXiv preprint arXiv:2311.12983.
Miami-Dade County. 2026. Miami-Dade Open Data. https:
//gis-mdc.opendata.arcgis.com.
OpenStreetMap contributors. 2026. OpenStreetMap. https:
//overpass-api.de.
Publieke Dienstverlening Op de Kaart. 2026. Publieke Di-
enstverlening Op de Kaart (PDOK). https://api.pdok.nl.
Qin, Y.; Liang, S.; Ye, Y.; Zhu, K.; Yan, L.; Lu, Y.; Lin,
Y.; Cong, X.; Tang, X.; Qian, B.; et al. 2023. ToolBench:
Facilitating Large Language Models to Master 16000+ Real-
World APIs. arXiv preprint arXiv:2307.16789.
Schick, T.; Dwivedi-Yu, J.; Dessì, R.; Raileanu, R.; Lomeli,
M.; Zettlemoyer, L.; Cancedda, N.; and Scialom, T. 2024.
Toolformer: Language Models Can Teach Themselves to Use
Tools. Advances in Neural Information Processing Systems,
36.
South Florida Water Management District. 2026. South
Florida Water Management District Geodata. https://
geodata.sfwmd.gov.
Stack Exchange, Inc. 2026. GIS Stack Exchange. https:
//gis.stackexchange.com.
Statistics Netherlands. 2026. Statistics Netherlands (CBS)
Open Data. https://opendata.cbs.nl.
U.S. Bureau of Labor Statistics. 2026. Occupational Out-
look Handbook: Cartographers and Photogrammetrists, Sur-
veyors, and Surveying and Mapping Technicians. https:
//www.bls.gov/ooh/architecture-and-engineering/.
U.S. Census Bureau. 2026. US Census TIGER/Line Shape-
files. https://www.census.gov/geographies/mapping-files/
time-series/geo/tiger-line-file.html.
U.S. Geological Survey. 2026. USGS National Map. https:
//tnmaccess.nationalmap.gov/api/v1/products.
Wei, J.; Wang, X.; Schuurmans, D.; Bosma, M.; Xia, F.; Chi,
E.; Le, Q. V.; and Zhou, D. 2022. Chain-of-Thought Prompt-
ing Elicits Reasoning in Large Language Models. Advances
in Neural Information Processing Systems, 35.
```

---

## PDF 第 9 / 29 页

```text
Xu, Z.; Zhang, Y.; Adhikari, S.; Islam, S.; Xiao, T.; Liu, Z.;
Chen, S.; Yan, D.; and Jiang, Z. 2025. EarthSpatialBench:
Benchmarking Spatial Reasoning Capabilities of Multimodal
LLMs on Earth Imagery. arXiv preprint arXiv:2602.15918.
Yao, S.; Chen, H.; Yang, J.; and Narasimhan, K. 2022. Web-
Shop: Towards Scalable Real-World Web Interaction with
Grounded Language Agents. In Advances in Neural Infor-
mation Processing Systems, volume 35.
Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan, K.;
and Cao, Y. 2023. ReAct: Synergizing Reasoning and Acting
in Language Models. In Proceedings of the International
Conference on Learning Representations.
Yu, B.; Yang, C.; Hou, D.; Liu, C.; Liu, J.; Wang, C.; Zhang,
Z.; Li, H.; and Yang, W. 2025. GeoAgentBench: Benchmark-
ing LLM Agents for Geospatial Tasks. arXiv preprint.
Zhang, Q.; Gao, S.; Wei, C.; Zhao, Y.; Nie, Y.; Chen, Z.;
Chen, S.; Su, Y.; and Sun, H. 2025. GeoAnalystBench: A
GeoAI Benchmark for Assessing Large Language Models
for Spatial Analysis Workflow and Code Generation. Trans-
actions in GIS, 29.
Zhang, Y.; Wei, C.; Wu, S.; He, Z.; and Yu, W.
2023. GeoGPT: Understanding and Processing Geospa-
tial Tasks through an Autonomous GPT. arXiv preprint
arXiv:2307.07930.
```

---

## PDF 第 10 / 29 页

```text
Table A1: Final parameter values, applied identically to all
six models. No hyperparameter search was performed.
Parameter Value
Temperature 0 (greedy)
Top-p, top-k, penalties provider default
Random seed not exposed by providers
Max tool calls per task 50
Max tool-result characters 4,000
Runs per task per model 1
Agent loop ReAct (Yao et al. 2023)
Toolset size 128 primitives
Appendices
The appendices below record the implementation and exper-
imental details needed to reproduce our results, together with
extended tables and analyses for which there was no room in
the main text.
A Reproducibility Details
A.1 Model Access and Decoding
All six evaluated models are accessed as hosted API services;
none is served on local hardware, so no GPU resources are
used for inference. Gemini-3.1-Pro, Claude-4.6-Opus, GPT-
5.4, and GPT-OSS-120B are reached through an institutional
API gateway that proxies vendor endpoints, while DeepSeek-
V4-Pro and Qwen3.6-27B are reached through OpenRouter.
All runs reported in the paper were executed in July 2026.
Table A1 lists every parameter used. Decoding is greedy:
temperature is set explicitly to 0 for all six models, and no
other sampling parameter (top-p, top-k, or repetition penalty)
is overridden, so provider defaults apply. We do not set a
random seed, because the hosted endpoints do not expose
seed control; temperature-0 decoding is the only determin-
ism mechanism available to us. Exact bitwise replication is
therefore not guaranteed for hosted models, and providers
may additionally update model versions behind a fixed end-
point name. We perform one run per task per model, so all
reported numbers are single-run values rather than averages
over repetitions.
A.2 Software and Hardware Environment
Agent execution and all geoprocessing run inside a repro-
ducible container on a single compute node with 32 CPU
cores and 512 GB of memory; no GPUs are used. The soft-
ware environment is Ubuntu 25.10 with Python 3.11.15,
QGIS 4.0.2, GDAL/OGR 3.10.3, PROJ 9.6.0, GEOS 3.13.1,
GeoPandas 1.1.3, Rasterio 1.4.4, Shapely 2.1.2, and PyProj
3.7.2. Because every benchmark task is scored by determin-
istic output matching against a stored ground truth file, eval-
uation is fully reproducible given a fixed set of agent trajec-
tories, independent of the model endpoints used to generate
them.
B Task Set Construction Details
This appendix records the concrete filtering criteria and
prompts behind the pipeline summarized in Section 2.1 of
the main paper.
B.1 Source and Crawl
Threads are collected from GIS Stack Exchange through the
Stack Exchange API, retaining the question title, body, tags,
and answer bodies. The crawler also implements a scraper
for a second practitioner forum, which we did not use for this
release; every task in GISAgentBench originates from GIS
Stack Exchange.
B.2 Deterministic Pre-Filter
The first stage uses no language model. Each thread is scored
against seven positive term dictionaries and eight blacklist
families, all compiled as word-boundary regular expressions.
The dictionaries are reproduced in full below, exactly as they
appear in the pipeline source.
Positive dictionaries.
GIS core terminology (53). arcgis, arcgis pro, arcmap, arcpy, ar-
cpy.analysis, arcpy.conversion, arcpy.da, arcpy.management,
arcpy.mp, arcpy.na, arcpy.sa, contour, coordinate system, crs,
datum, datum transformation, dem, epsg, feature class, feature
layer, featureclass, file geodatabase, geodatabase, geographic
coordinate system, geometry, geoprocess, geoprocessing, geo-
tiff, gis, hydrology, image analyst, lidar, map algebra, nad83,
network analyst, parcel, point, polygon, polyline, projected co-
ordinate system, projection, raster, shapefile, spatial analyst,
spatial reference, tin, topology, utm, vector, watershed, web
mercator, wgs84, wkid.
Workflow verbs (54). add field, append, aspect, buffer, calculate
field, clip, contour, copy features, cost distance, cost path, de-
fine projection, dissolve, erase, euclidean distance, extract by
mask, extract values to points, feature class to feature class, flow
accumulation, flow direction, focal statistics, generate near ta-
ble, idw, intersect, join field, kernel density, kriging, least cost
path, make feature layer, make xy event layer, merge, mosaic to
new raster, near, pairwise buffer, pairwise clip, pairwise erase,
pairwise intersect, point density, project raster, raster calcula-
tor, reclassify, reproject, sample, select layer by attribute, select
layer by location, slope, snap raster, spatial join, stream order,
summarize within, table to table, tabulate intersection, union,
viewshed, zonal statistics.
Network analysis (19). add locations, closest facility, impedance,
location allocation, make closest facility analysis layer, make
closest facility layer, make od cost matrix analysis layer, make
route analysis layer, make service area layer, network dataset,
od cost matrix, origin destination cost matrix, route, routing,
service area, shortest path, solve tool, travel mode, turn restric-
tion.
GIS API terms (21). addfield, arcpy.describe, arcpy.exists, ar-
cpy.getcount, arcpy.listfeatureclasses, arcpy.listfields, ar-
cpy.management.getcount, calculatefield, copyfeatures, get-
count, insertcursor, listdatasets, listfeatureclasses, listfields,
listtables, makefeaturelayer, searchcursor, selectlayerbyat-
tribute, selectlayerbylocation, spatialreference, updatecursor.
Data context (27). .csv, .gdb, .geojson, .gpkg, .img, .shp, .tif, .tiff,
address, addresses, attribute table, building footprint, field
name, field names, latitude, line layer, longitude, objectid, point
layer, polygon layer, road network, shape@, shape@xy, sql,
street centerline, timestamp, where clause.
```

---

## PDF 第 11 / 29 页

```text
Task-signal verbs (28). aggregate, buffer, calculate, classify, clip,
compute, convert, create, derive, estimate, extract, find,
geocode, identify, intersect, join, overlay, produce, project, re-
pair, reverse geocode, route, sample, segment, summarize, tab-
ulate, transform, validate.
Result-signal terms (18). classification, count, csv, density, fea-
ture class, feature layer, hot spot, layer, mean, output, point,
polygon, polyline, raster, result, route, summary, table.
Blacklist families.
Not a task (21). account, announcement, career, community
guidelines, enhancement, feature request, hiring, idea, intern-
ship, job posting, license, licensing, login, moderator, pricing,
release notes, roadmap, server outage, service issue, status
page, subscription.
Interface only (19). display, export format, hatch fill, html margin,
icon, label, labeling, layout, legend, panel, pop up, popup, print
layout, render, ribbon, style only, styling, symbology, toolbar.
Environment and installation (14). cannot load, conda, corrupt
package, dependency, environment, failed to load, install, in-
stallation, package, packages, pip, plugin, upgrade, version.
Online services (12). access denied, arcgis online, geoserver, not
running, permission, portal, publish, publishing, refresh, ser-
vice unavailable, submitted but not running, sync.
Software recommendation (10). basemap provider, best soft-
ware, best tool, imagery provider, recommend a, recommend
software, recommendation, tile provider, what software, which
software.
General questions (5). general question, is there a way, what is
better, what is the difference, why does.
Weak help requests (10). any ideas, can anyone help, can some-
one help, does anyone know, i am stuck, i need help, not sure
why, please help, thanks in advance, what am i doing wrong.
Code errors (10). attributeerror, exception:, indexerror, keyer-
ror, runtimeerror, stack trace, syntaxerror, traceback, typeer-
ror, valueerror.
A thread’s keyword score sums its dictionary hits and the
number of task-category families it matches, where a family
matches when the thread contains at least two of its subject
terms, or at least one subject and one action term. Threads
are rejected when the problem statement is shorter than 420
characters, when the keyword score falls below 4, when no
task family matches and the thread lacks both a workflow
signal and two or more data-context terms, when no task
signal or result signal is present, or when fewer than two
data-context terms appear. Near-duplicates are removed by
a SHA-256 signature over the lowercased title and the first
1,200 characters of the statement.
B.3 LLM Screening
Two GPT-5-mini screening passes follow. The first is a cheap
triage that emits a keep/reject decision against these criteria,
quoted verbatim from the pipeline:
Reject a thread if any line below fits it. (1) It is not a GIS
work problem. (2) It is mainly about accounts, licenses, ac-
cess, setup, installs, packages, plugins, or versions. (3) It is
mainly about display, colors, labels, legends, layouts, pop-
ups, forms, styling, settings, or map appearance. (4) It is
mainly about code syntax, SQL syntax, API syntax, script
bugs, or tool settings instead of the GIS result. (5) It is mainly
about file import/export, file format quirks, metadata, stor-
age, or docs. (6) It asks for general advice or explanation,
not a concrete GIS output. (7) It is only a tiny one-step con-
version, lookup, report, extract, or cleanup. (8) It is mainly
about speed, hardware, compression, parallel work, or ren-
dering. (9) The GIS goal is not clear.
The second pass is stricter and decides whether a surviving
thread can become a benchmark seed:
Keep only threads that can become strong GIS benchmark
seeds. Keep when all lines below are true: (1) The post has a
real GIS task, not just a bug, UI issue, or software question.
(2) The task has a clear spatial goal and a clear final result.
(3) The task can be written so the same inputs always lead to
the same output. (4) The task can be moved to local GIS files
without changing the real problem. (5) The work is more
than one tiny tool call. (6) The post or answer gives enough
detail to write a GIS solution later. Reject if a later task
writer would need to invent a different goal, guess missing
facts, or turn the post into a new problem.
This pass returns structured output rather than a bare la-
bel: booleans recording whether the thread states a complete
problem, whether its original meaning can be preserved un-
der recasting, and whether a short reference trajectory is
plausible; together with integer ratings on complexity, us-
ability, reproducibility, ambiguity, and reference clarity.
B.4 Task Drafting
Retained threads are cast into the benchmark task template:
a task identifier, a practitioner-style prompt with title, objec-
tive, inputs, required outputs and constraints, the input roles
bound to concrete files in a selected area of interest, task
parameters, and an output contract naming the file kind, re-
quired columns, spatial reference, and tolerances. The draft-
ing stage preserves the original analytical objective and is
explicitly barred from inventing a different question; drafts
that would require doing so are rejected rather than repaired.
Every draft is then reviewed by a second model pass before
entering reference generation.
The drafting instruction is quoted verbatim:
Create one local GIS benchmark task from one GIS forum
thread. Return status=ready only when the task is clear,
local, checkable, and still the same real problem as the
source post. Reject if the task needs missing data, guessed
input columns, made-up raster class meanings, made-up
selected features, fake row pairs, fake ObjectID matches,
unsupported network work, manual choices, or a different
GIS problem. Return exactly one JSON object matching the
schema.
A draft that fails schema or style validation is passed to
a repair prompt, which may correct fields but is held to the
same prohibition on inventing a different question.
C Complete GIS API Harness
Table C2 lists all 128 APIs available to the agent, grouped
by function. Descriptions are the first line of each API’s doc-
string, which is verbatim the description the agent receives at
inference time, so the table reflects the harness exactly as the
models see it. Of these, 111 appear in at least one released
```

---

## PDF 第 12 / 29 页

```text
reference trajectory; the remainder are available to agents but
not required by any task.
APIs are backed by QGIS through the qgis_process
command-line interface, including its GDAL-backed algo-
rithms, together with GeoPandas, Rasterio, Shapely, pan-
das/NumPy, and SciPy. Roughly two thirds dispatch to a
QGIS processing algorithm; the remainder are implemented
directly against the Python geospatial stack, and a small num-
ber compose other APIs in the harness.
```

---

## PDF 第 13 / 29 页

```text
Table C2: The complete 128-API harness. For each API the parameter list is given beneath its name, with optional parameters in
brackets. Descriptions are the first line of each API’s docstring, which is verbatim what the agent receives as the tool description.
API and parameters Description
Inspection & metadata (read-only) (6)
describe_layer
INPUT
Return schema and spatial metadata for a vector layer or CSV.
describe_raster
INPUT
Return spatial metadata for a raster.
get_feature_count
INPUT
Return the total number of features (rows) in a vector layer or CSV.
get_field_unique_values
INPUT, FIELD, [MAX_VALUES]
Return the sorted unique non-null values of FIELD, capped at MAX_VALUES.
get_feature_id_field
INPUT
Return the QGIS expression string ’$id’. Pass the returned value as FORMULA
in calculate_attribute_field to materialize a 1-based sequential integer feature
identifier into a named\dots
get_raster_property
INPUT, PROPERTY_NAME
Return one scalar property of a raster dataset.
CRS & reprojection (4)
warp_reproject_raster
INPUT, TARGET_CRS, OUTPUT, [RESAMPLING],
[SOURCE_CRS], [TARGET_RESOLUTION],
[TARGET_EXTENT], [TARGET_EXTENT_CRS], [NODATA],
[DATA_TYPE], [MULTITHREADING], [EXTRA]
Reproject or resample a raster to TARGET_CRS using GDAL warp.
assign_projection
INPUT, CRS, OUTPUT
Assign CRS metadata to INPUT without reprojecting coordinates.
reproject_features
INPUT, TARGET_CRS, OUTPUT,
[CONVERT_CURVED_GEOMETRIES], [OPERATION]
Transform vector layer coordinates to TARGET_CRS (e.g. ’EPSG:28992’).
align_raster_to_template
INPUT, TEMPLATE, OUTPUT, [RESAMPLING], [DATA_TYPE],
[NODATA], [MULTITHREADING]
Resample INPUT to exactly match TEMPLATE’s CRS, origin, cell size, and
pixel dimensions.
Vector overlay (8)
intersection_overlay
INPUT, OVERLAY, OUTPUT, [INPUT_FIELDS],
[OVERLAY_FIELDS], [OVERLAY_FIELDS_PREFIX],
[GRID_SIZE]
Compute the geometric intersection of INPUT and OVERLAY, producing
output features with the intersecting geometry and attributes from both layers.
clip_features
INPUT, OVERLAY, OUTPUT
Clip INPUT geometries to the shape of the OVERLAY layer, discarding parts
that fall outside. INPUT attributes are preserved.
difference_overlay
INPUT, OVERLAY, OUTPUT, [GRID_SIZE]
Erase OVERLAY geometry from INPUT features, keeping only the parts of
INPUT that do not overlap OVERLAY. INPUT attributes are preserved.
line_intersections
INPUT, INTERSECT, OUTPUT, [INPUT_FIELDS],
[INTERSECT_FIELDS], [INTERSECT_FIELDS_PREFIX]
Find all crossing points between INPUT and INTERSECT line layers,
outputting point features with attributes from both.
union_overlay
INPUT, OUTPUT, [OVERLAY], [OVERLAY_FIELDS_PREFIX],
[GRID_SIZE]
Compute the geometric union of INPUT and OVERLAY, producing output
features that cover all areas of both layers with attributes from both. When
OVERLAY is omitted, dissolves INPUT into a\dots
multi_intersection_overlay
INPUT, OVERLAYS, OUTPUT, [OVERLAY_FIELDS_PREFIX]
Compute the geometric intersection of INPUT with every layer in OVERLAYS
sequentially, retaining attributes from all layers.
multi_union_overlay
INPUT, OVERLAYS, OUTPUT, [OVERLAY_FIELDS_PREFIX]
Compute the geometric union of INPUT with every layer in OVERLAYS,
retaining all features and attributes from all layers.
update_features
INPUT, UPDATE, OUTPUT, [KEEP_BORDERS],
[CLUSTER_TOLERANCE]
Replace INPUT areas overlapping UPDATE features with the UPDATE
features, then merge the remainder with UPDATE into a single output layer.
Buffers & proximity (10)
buffer_features
INPUT, DISTANCE, OUTPUT, [SEGMENTS],
[END_CAP_STYLE], [JOIN_STYLE], [MITER_LIMIT],
[DISSOLVE]
Create buffer polygons at radius DISTANCE around each input feature.
```

---

## PDF 第 14 / 29 页

```text
Table C3 continued from previous page
API and parameters Description
multi_ring_buffer
INPUT, DISTANCES, FIELD_NAME, OUTPUT,
[OUTSIDE_ONLY], [DISSOLVE]
Create concentric buffer polygons at each distance in DISTANCES from input
features, storing the ring distance in FIELD_NAME.
nearest_features_table
INPUT, NEAR, OUTPUT, [SEARCH_RADIUS], [LOCATION],
[ANGLE], [NEIGHBOR_LIMIT], [DISTANCE_METHOD],
[DROP_GEOMETRY], [INPUT_ID_FIELD], [NEAR_ID_FIELD]
Computes nearest-neighbor distances between INPUT and NEAR features and
writes a table to OUTPUT. Output columns: IN_FID (INPUT identifier),
NEAR_FID (NEAR identifier), NEAR_DIST\dots
nearest_feature_distance_layer
INPUT, NEAR, OUTPUT, [INPUT_ID_FIELD],
[NEAR_ID_FIELD], [OUTPUT_INPUT_ID_FIELD],
[OUTPUT_NEAR_ID_FIELD], [OUTPUT_DISTANCE_FIELD],
[ROUND_DECIMALS], [DISTANCE_MULTIPLIER],
[KEEP_FIELDS]
For each INPUT feature, finds the nearest NEAR feature and writes OUTPUT: a
spatial layer with INPUT geometry and three appended fields:
OUTPUT_INPUT_ID_FIELD (INPUT feature identifier),\dots
euclidean_distance_raster
SOURCE, OUTPUT, [MAXIMUM_DISTANCE], [CELL_SIZE]
Create a raster where each cell value is the planar Euclidean distance to the
nearest non-zero cell in SOURCE. SOURCE must be a raster with non-zero
cells marking the source locations.
buffer_polygon_area_perimeter_table
POINTS, POLYGONS, OUTPUT, [POINT_ID_FIELD],
[BUFFER_RADIUS], [OUTPUT_AREA_FIELD],
[OUTPUT_PERIMETER_FIELD], [OUTPUT_PERCENT_FIELD],
[ROUND_DECIMALS]
For each point, compute the intersection area, boundary length, and area
percentage of POLYGONS within a BUFFER_RADIUS circle. Output
columns: POINT_ID_FIELD, OUTPUT_AREA_FIELD (total\dots
polygon_max_interior_radius_table
INPUT, OUTPUT, [ID_FIELD], [OUTPUT_ID_FIELD],
[OUTPUT_RADIUS_FIELD], [TOLERANCE],
[ROUND_DECIMALS]
Compute the pole of inaccessibility radius (maximum inscribed circle radius)
for each polygon and write a table. Output columns: OUTPUT_ID_FIELD
(polygon identifier from ID_FIELD),\dots
clip_point_buffers_to_containing_
polygons
POINTS, POLYGONS, OUTPUT, [POINT_ID_FIELD],
[POLYGON_ID_FIELD], [BUFFER_RADIUS],
[OUTPUT_POINT_ID_FIELD],
[OUTPUT_POLYGON_ID_FIELD], [BUFFER_FIELD],
[BUFFER_VALUE], [TIE_BREAKER], [SEGMENTS]
For each point, create a BUFFER_RADIUS circle clipped to the POLYGONS
polygon that contains it. Output columns: OUTPUT_POINT_ID_FIELD (point
identifier), OUTPUT_POLYGON_ID_FIELD\dots
clip_geometry_buffers_to_
containing_polygons
INPUT, CONTAINERS, OUTPUT, [INPUT_ID_FIELD],
[CONTAINER_ID_FIELD], [BUFFER_DISTANCE],
[OUTPUT_INPUT_ID_FIELD],
[OUTPUT_CONTAINER_ID_FIELD], [BUFFER_FIELD],
[AREA_FIELD], [ROUND_DECIMALS],
[CONTAINER_TIE_BREAKER], [SEGMENTS]
Buffer each INPUT geometry by BUFFER_DISTANCE and clip the result to
the CONTAINERS polygon that contains it. Output columns:
OUTPUT_INPUT_ID_FIELD (INPUT identifier),\dots
voronoi_polygons
INPUT, OUTPUT, [BUFFER], [TOLERANCE],
[COPY_ATTRIBUTES]
Generate a Voronoi diagram (Thiessen polygons) from point features, one
polygon per input point.
Geometry construction & conversion (22)
minimum_bounding_geometry
INPUT, TYPE, OUTPUT, [FIELD]
Create a minimum bounding geometry for each feature or, when FIELD is
given, for each group of features.
multipart_to_singleparts
INPUT, OUTPUT
Explode multipart geometries into single-part features, one output feature per
part with duplicated attributes.
point_on_surface
INPUT, OUTPUT, [ANGLE_TOLERANCE]
Generate a guaranteed-interior representative point for each feature’s surface.
The output point is always inside or on the boundary of the feature, even for
concave shapes.
geometry_by_expression
INPUT, OUTPUT, EXPRESSION, [OUTPUT_GEOMETRY],
[WITH_Z], [WITH_M]
Replace each feature’s geometry with the result of evaluating the QGIS
geometry EXPRESSION.
extract_specific_vertices
INPUT, VERTICES, OUTPUT
Extract geometry vertices at the given 0-based positions, one output point per
matched vertex.
features_to_lines
INPUTS, OUTPUT, [ATTRIBUTES], [CLUSTER_TOLERANCE]
Split line and polygon boundary geometries from INPUTS at all intersection
points, producing a set of non-duplicate line segments covering all edges.
polygons_to_lines
INPUT, OUTPUT, [SPLIT_SHARED_BOUNDARIES]
Convert polygon boundaries to line features. When
SPLIT_SHARED_BOUNDARIES=True, shared edges between polygons
produce separate line features with LEFT_FID (polygon on the left) and\dots
```

---

## PDF 第 15 / 29 页

```text
Table C3 continued from previous page
API and parameters Description
centroid_points
INPUT, OUTPUT, [ALL_PARTS]
Replace each feature’s geometry with its centroid point.
convex_hull
INPUT, OUTPUT
Replace each feature’s geometry with its convex hull. Output appends two
columns: ’area’ (polygon area in CRS units) and ’perimeter’ (polygon perimeter
in CRS units).
extract_vertices
INPUT, OUTPUT
Extract every vertex of each input geometry as an individual point feature,
preserving source attributes.
create_point_layer_from_table
INPUT, XFIELD, YFIELD, TARGET_CRS, OUTPUT, [ZFIELD],
[MFIELD]
Create a point layer from coordinate columns in a table, assigning
TARGET_CRS to the output geometries.
points_along_lines
INPUT, OUTPUT, [PLACEMENT], [DISTANCE],
[PERCENTAGE], [INCLUDE_END_POINTS],
[ADD_CHAINAGE_FIELDS], [DISTANCE_FIELD]
Place points at a regular DISTANCE interval along each line. Output includes
all INPUT attributes. When ADD_CHAINAGE_FIELDS=True, output also
includes ORIG_FID (source line identifier),\dots
explode_lines
INPUT, OUTPUT
Split each line at every interior node, producing individual two-vertex line
segments with duplicated attributes.
create_grid
TYPE, EXTENT, HSPACING, VSPACING, CRS, OUTPUT,
[HOVERLAY], [VOVERLAY]
Create a regular vector grid covering EXTENT at HSPACING x VSPACING
cell size.
bounding_boxes
INPUT, OUTPUT
Replace each feature’s geometry with its axis-aligned bounding box (minimum
enclosing rectangle aligned to the CRS axes).
polygonize_lines
INPUT, OUTPUT, [KEEP_FIELDS]
Form polygons from closed line rings in a line network, filling every enclosed
area as a polygon feature.
indexed_fishnet
TEMPLATE, CELL_WIDTH, CELL_HEIGHT, OUTPUT,
[NUMBER_ROWS], [NUMBER_COLUMNS],
[GEOMETRY_TYPE], [CRS], [ROW_FIELD], [COL_FIELD],
[ID_FIELD], [ORIGIN_MODE], [ROW_ORDER]
Create a regular grid over the extent of TEMPLATE at CELL_WIDTH x
CELL_HEIGHT spacing. Output columns: ID_FIELD (1-based sequential cell
ID), ROW_FIELD (row index), COL_FIELD (column index).
snap_centered_square_boxes_to_
raster_grid
INPUT, RASTER, HALF_SIZE, OUTPUT, [ID_FIELD],
[OUTPUT_ID_FIELD], [BUFFER_FIELD], [BUFFER_VALUE],
[MODE_FIELD], [MODE_VALUE]
Create one square polygon per input point, snapped inward to the nearest
RASTER cell boundaries. The square is centered on the point with half-width
HALF_SIZE but the actual edges are\dots
add_xy_fields
INPUT, OUTPUT, [CRS], [PREFIX]
Append X and Y coordinate fields to each feature. Output field names are
PREFIX+’x’ and PREFIX+’y’.
centered_squares_from_points
INPUT, SIDE_LENGTHS, OUTPUT, [ID_FIELD],
[OUTPUT_ID_FIELD], [SIDE_FIELD]
Create one centered square polygon per input point per side length in
SIDE_LENGTHS; each square is centered on its source point. Output columns:
OUTPUT_ID_FIELD (source identifier),\dots
offset_points_by_bearings
INPUT, OUTPUT, DISTANCE, BEARINGS, [ORIGIN_ID_FIELD],
[OFFSET_INDEX_FIELD], [BEARING_FIELD],
[DISTANCE_FIELD]
Create one offset point per input point per bearing, translating each point by
DISTANCE in the given direction. Output columns: ORIGIN_ID_FIELD
(source feature identifier),\dots
translate_points_by_xy_offset
INPUT, DX, DY, OUTPUT, [ID_FIELD], [OUTPUT_ID_FIELD],
[X_FIELD], [Y_FIELD], [ROUND_DECIMALS]
Shift every point geometry by (DX, DY) in CRS units, appending
OUTPUT_ID_FIELD, X_FIELD (new X, rounded to ROUND_DECIMALS),
and Y_FIELD (new Y, rounded to ROUND_DECIMALS).
Geometry cleaning & dissolve (7)
delete_duplicates_by_attribute
INPUT, FIELDS, OUTPUT, [DUPLICATES]
Remove duplicate features by matching values in FIELDS, keeping the first
occurrence; optionally write removed duplicates to DUPLICATES.
find_identical_features
INPUT, FIELDS, OUTPUT, [XY_TOLERANCE],
[Z_TOLERANCE], [OUTPUT_RECORD_OPTION]
Find features with identical attribute values or geometry and write a table of
duplicates. Output columns: IN_FID (1-based feature ID), FEAT_SEQ (group
identifier; features in the same\dots
delete_duplicate_geometries
INPUT, OUTPUT
Remove features whose geometry is exactly duplicated by another feature,
keeping the first occurrence.
dissolve_features
INPUT, OUTPUT, [FIELD], [SEPARATE_DISJOINT]
Merge features into multipart geometries by grouping on FIELD values. All
features merge into one when FIELD is empty.
fix_geometries
INPUT, OUTPUT, [METHOD]
Repair topologically invalid vector geometries using GEOS algorithms.
delete_holes
INPUT, OUTPUT, [MIN_AREA]
Remove interior rings (holes) from polygon features. Holes with area strictly
less than MIN_AREA are removed; MIN_AREA=0.0 keeps all holes; pass a
large value (e.g., float(’inf’)) to\dots
simplify_geometries
INPUT, METHOD, TOLERANCE, OUTPUT
Reduce vertex count of geometries using a named simplification algorithm.
```

---

## PDF 第 16 / 29 页

```text
Table C3 continued from previous page
API and parameters Description
Attribute & table operations (15)
calculate_attribute_field
INPUT, FIELD_NAME, FORMULA, [OUTPUT], [FIELD_TYPE],
[FIELD_LENGTH], [FIELD_PRECISION], [NEW_FIELD]
Add or overwrite attribute field FIELD_NAME on each feature using a QGIS
field-calculator FORMULA expression.
join_table_by_field
INPUT, FIELD, INPUT_2, FIELD_2, [OUTPUT],
[FIELDS_TO_COPY], [METHOD],
[DISCARD_NONMATCHING], [PREFIX]
Join INPUT_2 attributes onto INPUT by matching FIELD = FIELD_2,
retaining INPUT geometry. Accepts ’$id’ as either FIELD or FIELD_2.
extract_features_by_expression
INPUT, EXPRESSION, OUTPUT, [FAIL_OUTPUT]
Extract features where the QGIS expression EXPRESSION evaluates to true,
writing matched features to OUTPUT.
sort_table_rows
INPUT, SORT_FIELDS, OUTPUT
Sort rows by one or more fields. SORT_FIELDS are applied in order, so the first
entry is the primary sort key.
statistics_table
INPUT, AGGREGATES, OUTPUT, [CASE_FIELDS]
Aggregate INPUT rows using AGGREGATES function definitions, optionally
grouped by CASE_FIELDS. Output columns: CASE_FIELDS columns (one
per group-by field) plus one column per AGGREGATES\dots
add_geometry_attributes
INPUT, [OUTPUT], [GEOMETRY_PROPERTIES], [AREA_UNIT],
[LENGTH_UNIT]
Append geometric measurement columns to each feature.
rename_field
INPUT, FIELD, NEW_NAME, OUTPUT
Rename attribute field FIELD to NEW_NAME in the output layer. The QGIS
expression ’$id’ is accepted for FIELD, which materializes the feature ID as a
real column named NEW_NAME.
add_attribute_field
INPUT, FIELD_NAME, FIELD_TYPE, OUTPUT,
[FIELD_LENGTH], [FIELD_PRECISION]
Add an empty attribute field FIELD_NAME of the given type to a vector layer,
initialized to NULL for all features.
retain_fields
INPUT, FIELDS, OUTPUT
Keep only the listed FIELDS attribute columns, dropping all others. Geometry
is always retained. An empty FIELDS list drops all attributes.
delete_columns
INPUT, COLUMN, OUTPUT
Remove the listed COLUMN attribute fields from the layer, keeping all other
fields and geometry. COLUMN accepts a list of field name strings.
statistics_by_categories
INPUT, CATEGORIES_FIELD_NAME, OUTPUT,
[VALUES_FIELD_NAME]
Compute descriptive statistics for VALUES_FIELD_NAME grouped by unique
combinations of CATEGORIES_FIELD_NAME. Output columns:
CATEGORIES_FIELD_NAME fields plus count, unique, min, max,\dots
join_attributes_by_field_value
INPUT, FIELD, INPUT_2, FIELD_2, OUTPUT,
[FIELDS_TO_COPY], [METHOD],
[DISCARD_NONMATCHING], [PREFIX], [NON_MATCHING]
Join INPUT_2 attributes onto INPUT by matching FIELD = FIELD_2,
retaining INPUT geometry.
frequency_table
INPUT, FIELDS, OUTPUT, [COUNT_FIELD]
Count the occurrences of each unique combination of FIELDS values. Output
columns: FIELDS columns plus COUNT_FIELD (integer occurrence count).
wide_table_to_long_table
INPUT, ID_FIELDS, [VARIABLE_FIELD], [VALUE_FIELD],
[OUTPUT], [WIDE_FIELDS], [WIDE_FIELD_PREFIX],
[ID_OUTPUT_FIELDS], [INCLUDE_ZERO],
[VARIABLE_FIELD_TYPE], [VALUE_FIELD_TYPE]
Reshape a wide table to long format. Output columns: ID_OUTPUT_FIELDS
(one per ID_FIELDS entry), VARIABLE_FIELD (column name stripped of
prefix), VALUE_FIELD (cell value).
add_autoincremental_field
INPUT, FIELD_NAME, OUTPUT, [START], [MODULUS],
[GROUP_FIELDS], [SORT_EXPRESSION],
[SORT_ASCENDING], [SORT_NULLS_FIRST]
Add an integer FIELD_NAME that increments by 1 for each feature starting at
START (default 0, so the first feature receives 0).
Spatial join & selection (6)
join_attributes_by_location
INPUT, JOIN, OUTPUT, [PREDICATE_CODES], [METHOD],
[DISCARD_NONMATCHING], [JOIN_FIELDS], [PREFIX],
[ADD_TARGET_FID], [ADD_JOIN_COUNT]
Join JOIN attributes onto INPUT features that satisfy the spatial predicates.
Optionally appends Join_Count (number of matching JOIN features per INPUT
feature).
join_attributes_by_location_summary
INPUT, JOIN, OUTPUT, [PREDICATE_CODES], [JOIN_FIELDS],
[SUMMARIES], [DISCARD_NONMATCHING], [PREFIX]
Aggregate JOIN feature attributes into per-INPUT-feature summary statistics
using spatial relationship. Output appends ’<field>_<stat>’ columns for each
JOIN_FIELDSxSUMMARIES combination.
extract_features_by_location
INPUT, INTERSECT, PREDICATE, OUTPUT
Extract INPUT features that satisfy at least one spatial predicate against the
INTERSECT layer.
point_polygon_layer_counts
POINTS, POLYGON_LAYERS, OUTPUT, [POINT_ID_FIELD],
[OUTPUT_COUNT_FIELDS], [PREDICATE], [SORT_BY_ID]
Count the number of polygon features from each POLYGON_LAYERS layer
that satisfy PREDICATE for each point. Output columns: POINT_ID_FIELD
plus one count column per layer in\dots
```

---

## PDF 第 17 / 29 页

```text
Table C3 continued from previous page
API and parameters Description
join_attributes_by_nearest
INPUT, INPUT_2, OUTPUT, [FIELDS_TO_COPY],
[DISCARD_NONMATCHING], [PREFIX], [NEIGHBORS],
[MAX_DISTANCE], [ADD_TARGET_FID]
Join INPUT_2 attributes onto each INPUT feature using nearest-neighbor
geometry matching, retaining INPUT geometry.
join_attributes_by_location_within_
distance
INPUT, JOIN, DISTANCE, OUTPUT, [METHOD],
[DISCARD_NONMATCHING], [JOIN_FIELDS], [PREFIX],
[ADD_JOIN_COUNT]
Join JOIN attributes onto INPUT features whose geometries lie within planar
DISTANCE, preserving INPUT geometry.
Raster processing (15)
clip_raster_by_mask
INPUT, MASK, OUTPUT, [SOURCE_CRS], [TARGET_CRS],
[NODATA], [ALPHA_BAND], [CROP_TO_CUTLINE],
[KEEP_RESOLUTION], [SET_RESOLUTION],
[X_RESOLUTION], [Y_RESOLUTION], [MULTITHREADING],
[OPTIONS], [DATA_TYPE], [EXTRA]
Clip a raster to the shape of vector MASK polygons using GDAL.
clip_raster_to_raster_extent
INPUT, REFERENCE_RASTER, OUTPUT, [NODATA],
[DATA_TYPE], [EXTRA]
Clip INPUT to the axis-aligned bounding box of REFERENCE_RASTER.
clip_raster_to_layer_extent
INPUT, REFERENCE_LAYER, OUTPUT, [NODATA],
[DATA_TYPE], [EXTRA]
Clip INPUT to the axis-aligned bounding box of REFERENCE_LAYER (vector
or raster).
clump_raster_regions
INPUT, OUTPUT, [DIAGONAL], [THRESHOLD], [TITLE],
[GRASS_REGION_PARAMETER],
[GRASS_REGION_CELLSIZE_PARAMETER]
Label connected raster regions of equal pixel value with a unique integer
component ID. Output is an Int32 raster where each distinct contiguous region
has a unique positive ID; 0\dots
rearrange_raster_bands
INPUT, BANDS, OUTPUT, [DATA_TYPE],
[CREATION_OPTIONS]
Reorder or subset raster bands; output has one band per entry in BANDS
(1-based band indices).
raster_calculator
LAYERS, FORMULA, OUTPUT, [RTYPE], [NO_DATA],
[EXTENT_OPT], [EXTRA]
Evaluate a pixel-wise arithmetic FORMULA across LAYERS, where each layer
is referenced as A, B, C, ... in LAYERS order (up to six layers).
focal_statistics_raster
INPUT, OUTPUT, [METHOD], [CIRCULAR],
[RADIUS_OR_WIDTH], [HEIGHT], [UNITS],
[IGNORE_NODATA], [WINDOW_MODE]
Compute a per-cell statistic over a moving neighborhood window, producing a
Float32 output raster.
reclassify_raster_by_table
INPUT_RASTER, TABLE, OUTPUT, [RASTER_BAND],
[NO_DATA], [RANGE_BOUNDARIES],
[NODATA_FOR_MISSING], [DATA_TYPE]
Reclassify raster values using a TABLE of [lower_bound, upper_bound,
new_value] rows. Each row maps cells whose values fall in the specified range
to new_value.
cell_statistics_raster
INPUT, STATISTIC, REF_LAYER, OUTPUT, [IGNORE_NODATA],
[OUTPUT_NO_DATA_VALUE], [CREATION_OPTIONS]
Compute a cell-by-cell statistic across a stack of aligned rasters, using
REF_LAYER to define the output grid. All INPUT rasters must share the same
CRS, origin, and cell size as\dots
merge_rasters
INPUT, OUTPUT, [PCT], [SEPARATE], [NODATA_INPUT],
[NODATA_OUTPUT], [DATA_TYPE], [OPTIONS], [EXTRA]
Mosaic multiple rasters into a single-band output by overlaying them in order
(last INPUT on top).
region_group_raster
INPUT, OUTPUT, [NEIGHBORS], [EXCLUDED_VALUE]
Label connected regions of equal-value raster cells with unique positive
integers. Produces an Int32 raster; 0 marks NoData or EXCLUDED_VALUE
cells. NEIGHBORS must be 4 or 8;\dots
aggregate_raster
INPUT, CELL_FACTOR, STATISTIC, OUTPUT,
[IGNORE_NODATA]
Reduce raster resolution by aggregating CELL_FACTOR x CELL_FACTOR
blocks into a single output cell using STATISTIC. The output grid origin aligns
with the input origin; each output cell\dots
translate_raster_format
INPUT, OUTPUT, [NODATA], [COPY_SUBDATASETS],
[CREATION_OPTIONS], [EXTRA], [DATA_TYPE]
Convert or copy a raster to a new file, optionally changing pixel data type.
raster_value_count_table
INPUT_RASTER, OUTPUT
Count pixel occurrences for each unique integer value in band 1 of
INPUT_RASTER. Output columns: value (pixel value), count (number of cells
with that value).
weighted_sum_raster
INPUTS, WEIGHTS, OUTPUT
Compute a pixel-wise weighted sum of already aligned rasters. Each INPUTS[i]
is multiplied by WEIGHTS[i] and the products are summed. All inputs must
share the same CRS, transform, and\dots
```

---

## PDF 第 18 / 29 页

```text
Table C3 continued from previous page
API and parameters Description
Raster–vector conversion & sampling (11)
polygonize_raster
INPUT, OUTPUT, [BAND], [FIELD],
[EIGHT_CONNECTEDNESS], [EXTRA]
Convert contiguous raster regions of equal pixel value in BAND into polygon
features, storing the pixel value in FIELD.
raster_max_points_by_polygon
POLYGONS, RASTER, OUTPUT, [POLYGON_ID_FIELD],
[OUTPUT_ID_FIELD], [OUTPUT_VALUE_FIELD],
[ROUND_DECIMALS], [INCLUDE_BOUNDARY]
Create one point feature per polygon at the raster cell center with the maximum
pixel value inside that polygon. Output columns: OUTPUT_ID_FIELD
(polygon identifier from\dots
raster_pixels_to_points
INPUT_RASTER, RASTER_BAND, FIELD_NAME, OUTPUT
Create one point at each valid raster cell center for RASTER_BAND, storing the
pixel value in FIELD_NAME. NoData cells produce no point.
sample_raster_values_to_points
INPUT, RASTER, COLUMN_PREFIX, OUTPUT
Sample RASTER cell values at each point location, appending columns
COLUMN_PREFIX1, COLUMN_PREFIX2, ... (one per band). NoData cells
produce NULL.
raster_domain_polygon
INPUT_RASTER, OUTPUT, [BAND]
Create polygon features covering all contiguous regions of valid (non-NoData,
finite) cells in BAND. Multiple disconnected regions produce multiple features;
output column gridcode=1 for\dots
polygon_to_raster
INPUT, FIELD, OUTPUT, CELL_SIZE, [ALL_TOUCHED],
[PRIORITY_FIELD], [DATA_TYPE], [EXTENT], [INIT],
[NODATA], [EXTRA], [EXTENT_BUFFER]
Burn vector polygon attribute FIELD into a raster grid at CELL_SIZE
resolution.
point_to_raster
INPUT, FIELD, OUTPUT, CELL_SIZE, [DATA_TYPE],
[EXTENT], [INIT], [NODATA], [EXTRA]
Burn point feature attribute FIELD into a raster grid at CELL_SIZE resolution.
polyline_to_raster
INPUT, FIELD, OUTPUT, CELL_SIZE, [ALL_TOUCHED],
[PRIORITY_FIELD], [DATA_TYPE], [EXTENT], [INIT],
[NODATA], [EXTRA]
Burn line feature attribute FIELD into a raster grid at CELL_SIZE resolution.
sample_multiple_rasters_at_points
RASTERS, LOCATIONS, OUTPUT, [COLUMN_PREFIX]
Sample values from each raster in RASTERS at LOCATIONS points, merging
RASTERS into a multi-band stack first. Output columns from LOCATIONS
plus COLUMN_PREFIX1, COLUMN_PREFIX2, ... (one\dots
raster_contour_lines
INPUT, OUTPUT, [BAND], [INTERVAL], [FIELD_NAME],
[CREATE_3D], [IGNORE_NODATA], [NODATA], [OFFSET],
[OPTIONS], [EXTRA]
Generate contour lines from raster BAND at a fixed elevation INTERVAL.
Output column FIELD_NAME stores the contour elevation value for each line.
raster_cells_to_polygons
INPUT_RASTER, OUTPUT, [INCLUDE_NODATA],
[ROW_FIELD], [COL_FIELD], [CELL_ID_FIELD],
[VALUE_FIELD]
Create one polygon per raster cell, one feature per valid pixel. Output columns:
ROW_FIELD (row index), COL_FIELD (column index), CELL_ID_FIELD
(sequential cell ID), VALUE_FIELD (pixel\dots
Zonal statistics & area tabulation (5)
tabulate_area_table
ZONES, ZONE_FIELD, CLASSES, [CLASS_FIELD],
[PROCESSING_CELL_SIZE], [OUTPUT]
Count cells of each CLASSES raster value within each ZONES polygon and
multiply by pixel area. Output columns: ZONE_FIELD (zone identifier) plus
one VALUE_<n> column per raster class\dots
zonal_statistics_as_table
ZONES, ZONE_FIELD, RASTER, STATISTICS,
COLUMN_PREFIX, [FIELD_RENAMES], [IGNORE_NODATA],
[OUTPUT]
Compute raster statistics for each polygon zone and write them as a table
(geometry dropped). Output columns: all ZONES attribute columns plus one
per STATISTICS entry named\dots
zonal_statistics_raster
ZONES, ZONE_FIELD, RASTER, [STATISTIC_FIELD],
[IGNORE_NODATA], [OUTPUT]
Compute zonal statistics of RASTER by ZONES and burn the
STATISTIC_FIELD value back onto a raster grid matching RASTER.
STATISTIC_FIELD must be MAX or COUNT (from zonal_statistics_as_table).
tabulate_intersection
ZONES, ZONE_FIELDS, CLASSES, [CLASS_FIELDS],
[SUM_FIELDS], [OUT_UNITS], [OUTPUT]
Intersect ZONES and CLASSES polygon layers and compute overlap areas.
Output columns: ZONE_FIELDS columns, CLASS_FIELDS columns, AREA
(intersection area in the squared CRS units of\dots
zonal_percentile_table
ZONES, ZONE_FIELD, RASTER, [PERCENTILE],
[INTERPOLATION], [IGNORE_NODATA], [OUTPUT]
Compute a raster percentile for each polygon zone and write a table. Output
columns: ZONE_FIELD (zone identifier), COUNT (valid cell count), AREA
(COUNT x pixel area in CRS units), PCTxx\dots
Density surfaces (3)
gaussian_kernel_from_points
POINTS, TEMPLATE_RASTER, OUTPUT, SIGMA, [NODATA],
[ROUND_DECIMALS]
Create a raster where each valid cell value is exp(-d^2 / (2*sigma^2)) where d is
the Euclidean distance to the nearest POINTS location. Output uses the same
grid as TEMPLATE_RASTER.
```

---

## PDF 第 19 / 29 页

```text
Table C3 continued from previous page
API and parameters Description
heatmap_kernel_density
INPUT, RADIUS, PIXEL_SIZE, OUTPUT, [WEIGHT_FIELD],
[RADIUS_FIELD], [KERNEL], [DECAY], [OUTPUT_VALUE]
Create a kernel density estimation raster from point features; each cell value is
the density contribution within RADIUS of the cell center.
point_density_raster
point_fc, output_path, [population_field], [cell_size],
[neighborhood_type], [neighborhood_radius],
[neighborhood_units], [area_unit_scale_factor]
Create a kernel density estimation raster from point features.
Terrain & hydrology (9)
slope_raster
INPUT, Z_FACTOR, OUTPUT
Compute a slope raster in degrees from an elevation model, using Z_FACTOR
to scale vertical units relative to horizontal units.
aspect_raster
INPUT, OUTPUT, [Z_FACTOR]
Compute an aspect raster (compass direction of steepest descent in degrees)
from an elevation model. Z_FACTOR scales vertical units relative to horizontal
units.
viewshed_raster
raster_path, observer_features, output_path, [z_factor],
[curvature_correction], [refractivity_coefficient]
Create a binary union viewshed from observer point features. Output is a raster
where each cell is 1 if visible from any observer and 0 otherwise.
hillshade_raster
INPUT, OUTPUT, [BAND], [Z_FACTOR], [SCALE], [AZIMUTH],
[ALTITUDE], [COMPUTE_EDGES], [ZEVENBERGEN],
[COMBINED], [MULTIDIRECTIONAL], [EXTRA],
[CREATION_OPTIONS]
Generate a hillshade raster from an elevation model. Z_FACTOR exaggerates
vertical scale; AZIMUTH is the light-source compass angle (0=north);
ALTITUDE is the sun elevation angle in\dots
fill_sinks
raster_path, output_path, [z_limit]
Fill topographic sinks in a DEM to produce continuous flow paths. z_limit:
maximum depth of sinks to fill; pass None or 0 for unlimited.
flow_direction_raster
surface_raster, output_path, [force_flow], [flow_direction_type]
Compute the downslope flow direction for each cell of a sink-filled DEM.
force_flow must be NORMAL; flow_direction_type must be D8.
flow_accumulation_raster
flow_direction_raster_path, output_path, [data_type],
[flow_direction_type]
Compute the number of upstream cells draining into each cell from a D8
flow-direction raster. flow_direction_type must be D8; data_type should be
FLOAT32 or FLOAT64 (passing FLOAT uses\dots
snap_pour_point_raster
pour_point_data, accumulation_raster, output_path, snap_distance,
pour_point_field
Rasterize pour-point features onto a grid matching accumulation_raster, burning
pour_point_field values into a Float32 raster aligned to the accumulation grid.
Cells with no pour point\dots
watershed_raster
flow_direction_raster_path, pour_point_data, output_path,
[pour_point_field]
Delineate drainage basins by assigning each valid cell to the nearest pour-point
label. pour_point_data must be a rasterized pour-point raster (from
snap_pour_point_raster) aligned to\dots
Network analysis & linear referencing (4)
create_routes
INPUT, ROUTE_ID_FIELD, OUTPUT, [MEASURE_FACTOR],
[MEASURE_OFFSET]
Prepare INPUT line features as routes for linear referencing. Measures are
derived from cumulative line length; MEASURE_FACTOR multiplies and
MEASURE_OFFSET shifts all measure values.\dots
locate_features_along_routes
FEATURES, ROUTES, ROUTE_ID_FIELD, TOLERANCE,
OUTPUT, [DISTANCE_FIELD], [ROUTE_LOCATIONS],
[INPUT_ID_FIELD]
Project FEATURES onto ROUTES by linear referencing. Output columns:
INPUTOID (FEATURES identifier), ROUTE_ID_FIELD (matched route
identifier), MEAS (linear distance along route from\dots
service_area_from_layer
NETWORK, START_POINTS, TRAVEL_COST, OUTPUT,
[STRATEGY], [DIRECTION_FIELD], [VALUE_FORWARD],
[VALUE_BACKWARD], [VALUE_BOTH], [SPEED_FIELD],
[DEFAULT_SPEED], [TOLERANCE]
Return network edges reachable within TRAVEL_COST (meters for
SHORTEST, minutes for FASTEST) from each START_POINT.
shortest_path_point_to_layer
NETWORK, START_POINTS, END_POINTS, OUTPUT,
[STRATEGY], [DIRECTION_FIELD], [VALUE_FORWARD],
[VALUE_BACKWARD], [VALUE_BOTH], [SPEED_FIELD],
[DEFAULT_SPEED], [TOLERANCE]
Compute the shortest/fastest network path from each START_POINT to its
nearest END_POINT.
Input/output & layer management (3)
export_table_to_csv
INPUT, OUTPUT, [FIELDS], [FIELD_RENAMES],
[EXPRESSION], [MAX_ROWS]
Write a table or vector layer to a CSV file at OUTPUT, dropping geometry.
save_features
INPUT, OUTPUT, [LAYER_NAME], [DATASOURCE_OPTIONS],
[LAYER_OPTIONS], [ACTION_ON_EXISTING_FILE]
Write a vector layer to a file, applying OGR format options and controlling
existing-file behavior.
```

---

## PDF 第 20 / 29 页

```text
Table C3 continued from previous page
API and parameters Description
merge_vector_layers
LAYERS, OUTPUT, [CRS], [ADD_SOURCE_FIELDS]
Stack multiple vector layers into a single output layer, combining all features.
```

---

## PDF 第 21 / 29 页

```text
D Area-of-Interest Data
Table D5 reports the principal vector layers per area of in-
terest with exact feature counts, and Table D6 reports ev-
ery raster with its dimensions and spatial reference. Feature
counts are measured from the shipped files rather than de-
clared in metadata.
Note that several rasters ship in geographic coordinate
systems while the analysis reference for their area of interest
is projected, and that filenames encoding a nominal resolu-
tion do not always match the shipped grid. Both conditions
are genuine properties of the released data and are among
the sources of the CRS Misalignment and Unit Mismatch
caveats.
D.1 Data Sources
Each area of interest is populated from public data portals: the
USGS National Map (U.S. Geological Survey 2026) (eleva-
tion and imagery), US Census TIGER/Line files (U.S. Cen-
sus Bureau 2026) (transportation and administrative bound-
aries), OpenStreetMap (OpenStreetMap contributors 2026)
(transportation, facilities, and hydrography), regional open-
data portals (City of New York 2026; City and County
of San Francisco 2026; City and County of Denver 2026;
Harris County, Texas 2026; Colorado Department of Public
Health and Environment 2026; Miami-Dade County 2026;
South Florida Water Management District 2026) (parcels,
flood hazards, and administrative datasets), the FEMA Na-
tional Flood Hazard Layer (Federal Emergency Management
Agency 2026), and the Dutch PDOK and CBS services (Pub-
lieke Dienstverlening Op de Kaart 2026; Statistics Nether-
lands 2026) (addresses, neighborhoods, municipalities, ele-
vation, and orthophotography).
D.2 Derived and Modified Layers
Most layers are ingested unmodified from their public source.
Three categories are derived so that data-quality caveats rest
on real conditions rather than hypothetical ones.
Controlled geometric defects. Clean cadastral layers are
perturbed by deterministic, seeded transformations to pro-
duce layers containing overlapping parcels (a small positive
buffer applied to a sampled subset, appended to the layer) and
narrow slivers (an inward buffer with the resulting ring re-
tained). Sampling uses fixed strides and fixed random seeds,
so the defects are identical on every regeneration. The re-
leased tasks exercise three such layers.
Derived raster products. Where no suitable public prod-
uct exists, a raster is computed from the elevation gradient
of the area’s digital elevation model and rescaled to a docu-
mented range, producing surface-cost and hazard rasters that
inherit the source grid exactly.
Schema normalization. Every ingested vector layer is
normalized on import, which adds stable identifier fields and,
for shapefile outputs, truncates field names to the format’s
ten-character limit. This is part of geographic recasting rather
than incidental: an agent cannot fall back on a field name
memorized from the source thread.
E Ground Truth Generation and Verification
E.1 Generation
Reference trajectories and their output files are generated and
verified with Claude Fable 5, a current frontier model that
is deliberately excluded from the set of evaluated agents so
that no evaluated model participates in authoring the ground
truth it is scored against.
Authoring runs in a deliberately privileged setting: the au-
thor is given direct access to the input data and to free-form
Python for deriving and cross-checking what the correct re-
sult should be, neither of which the evaluated agents receive.
The released trajectory, however, is expressed entirely in the
same 128-API harness the agents are given, and is executed
inside that harness to materialize the gold output file. The
intended answer is therefore established outside the harness,
while the output against which agents are scored is produced
inside it.
Reference trajectories are emitted as an ordered list of API
calls, each naming an API, its bound arguments, and a handle
for its output. The generation prompt constrains the author
to the published harness:
Use only tools from the provided parsed catalog. Do not as-
sume an unlisted tool, unlisted input field, external dataset,
manual edit, hidden preprocessing step, or alternate inter-
pretation of the task.
This constraint is enforced rather than merely requested:
the executor rejects any reference step naming a function
outside the set exposed to agents, so a reference that drifted
from the harness cannot be executed or released.
E.2 Automated Verification
Generated sequences pass through static validation before
execution. Argument names are checked against the real API
signatures, output handles are checked for binding, and unre-
solvable references are rejected. Sequences that fail are sent
to a verify-and-repair pass, which may rename APIs, cor-
rect arguments, or reorder steps, but may not change the task
being solved. The verification instruction is quoted verbatim:
Check a proposed ground-truth tool sequence for basic tool-
use problems. Check tool names, argument names, place-
holders, missing steps, and final output paths. Do not change
the task. If the tool list cannot support the task as written,
return reject. Return exactly one JSON object matching the
schema.
The instruction is deliberately narrow: the verifier is a tool-
use checker, not a second author. A sequence that cannot be
repaired within the published harness is rejected rather than
rewritten, which is why tasks leave the pipeline instead of
being weakened to fit it. Surviving sequences are executed
in the benchmark environment; a task is retained only if
execution yields a well-formed file conforming to its output
contract.
E.3 Expert Review
Automated checks establish that a trajectory is well formed
and runs to completion; they cannot establish that it computes
the intended quantity. Reference trajectories were therefore
```

---

## PDF 第 22 / 29 页

```text
Table D4: Areas of interest: landscape character, analysis CRS, and task counts by family. Analysis CRS is the projected
reference in which measurements are defined; several source products ship in geographic coordinates, which is one origin of
the CRS Misalignment caveat.
Area of interest Landscape Analysis CRS SJ&G SO&SA SPA TM&HA RS&IA Tasks
San Francisco Bay Area Dense urban coastal; bay
shoreline, terrain, imagery
EPSG:26910 28 31 14 19 7 99
Randstad, Netherlands Low-lying delta; nationally
standardized registries
EPSG:28992 27 23 10 4 27 91
New York City Dense urban; parcel- and
address-rich cadastre
EPSG:2263 18 17 10 4 2 51
Denver Front Range Mountain front; wildland–urban
interface, hazards
EPSG:26913 6 5 6 16 7 40
Houston–Harris Flat coastal plain; floodplain and
drainage network
EPSG:2278 4 12 5 17 2 40
South Florida Engineered water control;
low-relief coastal wetland
EPSG:2236 13 5 7 3 0 28
Total 96 93 52 63 45 349
Table D5: Principal vector layers by area of interest, with
exact feature counts.
Area of interest Layer Features
San Francisco Bay
police_incidents 494,975
parcels 236,300
buildings 177,023
roads_osm 27,605
New York City
address_point 500,000
buildings 142,257
pluto_lots 133,289
lion (street network) 66,234
South Florida
address_points 939,821
miami_parcels 592,689
street_network 115,981
Houston–Harris
harris_roads 365,800
hcad_parcels_clean 312,518
canals 3,957
Denver Front Range
building_footprints 988,345
census_tracts 324
lookouts 208
Randstad
roads_osm 55,346
address_points 5,500
cbs_buurten_2025 1,000
reviewed directly by three GIS experts among the authors,
hand-traced step by step, with manual inspection of interme-
diate outputs and visual inspection of the resulting spatial
outputs. Every released reference trajectory passed through
this review; a subset was additionally re-verified in a ded-
icated audit round, for which the per-task records are most
complete.
Expert review surfaced defect classes that automated val-
idation cannot detect, because in each case the trajectory
executes successfully and produces a plausible output:
• a field calculation bound to a column that the upstream
Table D6: Raster products by area of interest.
Area Raster Pixels CRS
Denver dem_81m 1164 × 889 4258
Denver friction_surface_01 1164 × 889 4258
Denver friction_surface_02 1164 × 889 4258
Denver wildfire_risk_2024 1152 × 886 4269
Denver topo_scan_1950 1152 × 886 4326
Houston dem_34m 3663 × 2428 4258
Houston naip_latest 4096 × 3732 2278
NYC dem_10m 5345 × 5287 2263
NYC dem_1m 4221 × 2871 4326
NYC nypl_map_scan_1924 11266 × 7777 4326
NYC nypl_map_scan_1951 4560 × 5657 4326
NYC naip_latest 4045 × 4090 2263
SF Bay dem_1m 1817 × 1390 4269
SF Bay naip_latest 4096 × 3841 26910
S. Florida dem_24m 4096 × 4096 4326
S. Florida naip_latest 3546 × 4105 2236
Randstad dem_open 918 × 619 4269
Randstad landcover_class 1949 × 1214 4326
Randstad orthophoto_cir 2448 × 1652 4269
Randstad orthophoto_rgb 2048 × 2048 28992
operation never produced, yielding an all-zero or null
reference;
• a measurement computed on data in geographic coordi-
nates, so that areas and distances are expressed in degree-
based units;
• slope or terrain derivatives computed on an unprojected
elevation model;
• an output contract keyed on a column name the prompt
never promised, or renamed during export;
• off-by-one and truncation errors in row matching;
• geometry measured before an invalid-geometry repair
step rather than after.
Tasks whose problem statement proved ambiguous on re-
view, or whose specification would have had to change to
```

---

## PDF 第 23 / 29 页

```text
become solvable, were removed from the release rather than
repaired in place.
F Evaluation Metric Definitions
This appendix gives the full definitions summarized in Sec-
tion 3.2 of the main paper. All scoring is deterministic: no
language model participates in judging, and no metric com-
pares an agent’s trajectory to the reference trajectory.
F.1 Strict Task Success Rate
A run is counted correct only when every structural check de-
clared by the task passes and every matched value lies within
the task’s declared tolerance. Structural checks cover the co-
ordinate reference system, geometry type, data type, raster
dimensions and NoData encoding, and the required output
columns. Tolerance is applied per task against a combined
absolute tolerance of 1e−6 and relative tolerance of 0.01%,
so scoring is tolerance-aware rather than byte-identical: a re-
sult differing only by floating-point noise passes, while one
differing by a genuine unit or projection error does not. Strict
TSR is binary per task and admits no partial credit.
F.2 Row-Set Agreement
Rows are matched as a set, never by position. The matcher
tries, in order: the contract identifier columns declared by the
task; a geometry key, pairing each row with a geometry entity;
a detected unique column; and, as a last resort, an optimal
assignment over values. The last fallback is optimistic—it
finds the most favourable pairing—so closeness computed
from those rows should be read as an upper bound. We report
precision, recall, and F1 over the resulting correspondence.
We refer to recall—the fraction of reference rows matched—
as row coverage, since it is the quantity that exposes a partial
output: a model that emits few rows but gets those rows right
scores high on closeness and low on coverage.
F.3 Non-Spatial Attributes
Numeric columns are scored as one minus a normalized
error, clipped to [0, 1]. We report symmetric percentage er-
ror closeness and root-mean-square error normalized by the
reference mean; the underlying record additionally retains
weighted mean absolute percentage error, correlation-based
agreement, and the fraction of cells within the task’s declared
tolerance.
Categorical columns are scored with weighted F1, re-
stricted to reference columns carrying more than one class.
Single-class columns are excluded because any output that
emits the constant value scores perfectly on them, which
inflates the aggregate.
Both families of metric are computed over matched rows
only. They must therefore be read together with row-set cov-
erage: a model that emits few rows but gets those rows
right scores high on closeness and low on coverage, and
the coverage-weighted product is the single number that pe-
nalizes partial outputs.
F.4 Spatial Attributes
Geometry is scored by entity-level matching. For each ref-
erence geometry we ask whether a corresponding output
geometry exists within tolerance: polygons must reach an
intersection-over-union of at least 0.5, while points and lines
must fall within a distance threshold ε. Entity recall is the
fraction of reference entities found, entity precision the frac-
tion of produced entities corresponding to a reference entity,
and we report entity F1 separately for multi-point, multi-
polyline, and multi-polygon outputs.
We prefer entity-level matching to a set-based intersection-
over-union for two reasons. First, set-based IoU is only com-
putable when the union of geometries is tractable, so it is eval-
uated on a self-selected subset of outputs: a model that emits
fewer or simpler outputs is scored on a smaller sample, and
raw IoU consequently misranks models unless weighted by
task coverage. Second, a set-based overlap can look healthy
while the number of distinct entities is wrong, which entity-
level matching detects and IoU does not.
F.5 Trajectory Closeness
Trajectory closeness measures how much of a task’s refer-
ence workflow an agent actually performed, independently
of whether its final output was correct. It is reported as a
diagnostic and is not part of either headline metric.
The comparison is made at a coarse functional level rather
than over exact API names. Several APIs in the harness
accomplish the same operation—two-layer and multi-layer
union, for instance, differ only in arity—so matching on ex-
act names would penalize an agent for choosing a legitimate
alternative to the one the reference happened to use. Group-
ing APIs by function first, and then comparing the resulting
sets, separates which operations were performed from which
particular call was used to perform them. Read-only inspec-
tion calls are excluded on both sides: describing a layer or
counting its features advances the workflow no further, so
what remains on each side are the calls that change state.
Roles. Each of the 128 harness APIs is mapped to a seman-
tic role through a fixed lookup table (128 tools, roughly 103
distinct roles); composite tools map to several roles at once.
The mapping is deterministic and applied mechanically, so
turning a trajectory into its coarse-grained role sequence in-
volves no model judgment.
The table was built in two independent passes and then
reconciled. The first grouped tools by the GIS operation they
perform; the second, constructed blind to the first, grouped
them by the underlying QGIS or GDAL processing algorithm
each one dispatches to. Agreement between the passes was
0.27 by adjusted Rand index—moderate, as expected for
two genuinely different constructs—and all 68 disagreeing
tool pairs were individually adjudicated, which surfaced and
corrected five real labeling errors in the first pass.
Score. A task’s required roles are the distinct roles appear-
ing in its own reference trajectory, after discarding read-only
inspection calls and deduplicating to a set. An agent’s roles
are obtained by the same mapping over its real trajectory, dis-
carding calls that returned an error, since a failed call did not
accomplish the operation. Writing R for the set of required
```

---

## PDF 第 24 / 29 页

```text
roles and A for the set of roles the agent performed, trajectory
closeness is |R ∩ A|/|R|, where a required role also counts
as satisfied if the agent performed a functionally equivalent
substitute for it. Operations beyond those the reference used
are recorded but never subtracted, so the measure is a recall
over required operations with no precision term.
Requirement set. The reference trajectory is treated as
a correct solution rather than the only one, and it is a hard
ceiling: no role is ever required beyond what the reference
itself used. A required role is additionally dropped when at
least one model that solved the task under strict TSR did
so without invoking that role or a substitute, which prevents
the metric from penalizing an agent for skipping a step that
is demonstrably not necessary. Dropping is evidence-gated
and applied task-wide: 156 of the 349 tasks have at least
one droppable role, for 375 role drops in total. Eight tasks
lose their entire requirement set this way and are reported as
ungradeable rather than scored, on the principle that a ratio
with an empty denominator is undefined.
Order. Order violations are checked only for a small set
of constraints that admit no counterexample in our data, and
harmful insertions only for a single gated case. Both are
recorded as informational flags and neither is subtracted from
the score, consistent with our practice of scoring leniently
wherever a convention is ambiguous.
Validation. Two areas of interest—South Florida and
Houston, 68 tasks—were held out entirely while the role map
was built. Agreement with strict correctness is comparable
on the held-out and calibration splits (row-level point-biserial
r = 0.440 versus 0.420), indicating the mapping is not fitted
to the tasks used to construct it. Pooled over all 349 tasks
the row-level correlation is r = 0.424 and the model-level
correlation is r = 0.977.
Limitations. Requirements are role sets, so a reference
that applies the same operation to two different layers con-
tributes one required role rather than two, and an agent that
applies it once receives full credit. The measure compares
operation identity only: it does not inspect arguments, so in-
voking the right operation on the wrong layer or with the
wrong parameters still counts as satisfied. These properties
are why we treat trajectory closeness as a diagnostic rather
than a scored metric, and why a formal trajectory-level metric
over the space of equally valid reference trajectories remains
open.
F.6 Trajectory Diagnostics
For every run we additionally record the trajectory length
(number of API calls issued), the tool call error rate (the
fraction of calls returning an error, capturing failures in pa-
rameter correctness, input validity, and spatial reference han-
dling), the wall-clock time spent in model inference, and the
number of tokens consumed.
G Per-Family Timing
Table G7 reports mean per-task harness time broken down by
task family, complementing the aggregate figures in the main
paper. Harness time is time spent executing GIS operations
inside the evaluation framework; it excludes time spent wait-
ing on the model endpoint, which is reported separately in
the main text because it is dominated by vendor and network
conditions rather than by task difficulty.
Table G7: Mean per-task harness time (seconds) by task
family.
Model SJ&G SO&SA SPA RS&IA TM&HA
Gemini-3.1-Pro 143 151 106 99 125
Claude-4.6-Opus 121 120 113 51 107
DeepSeek-V4-Pro 156 143 156 73 120
GPT-5.4 142 133 142 52 68
Qwen3.6-27B 240 175 122 67 126
GPT-OSS-120B 116 130 107 85 161
H Token Consumption by Task Family
Table H8 reports mean token consumption per task, overall
and broken down by task family, complementing the aggre-
gate figures quoted in Section 3. The raster-heavy families
are the most token-hungry for most models, while Spatial
Joining & Geocoding is generally the cheapest.
Table H8: Mean tokens consumed per task (×103
), overall
and by task family. Lowest value per column in bold.
Model All SJ&G SO&SA SPA RS&IA TM&HA
Gemini-3.1-Pro 520 407 564 540 657 521
Claude-4.6-Opus 581 495 612 593 612 637
DeepSeek-V4-Pro 829 817 807 778 862 898
GPT-5.4 275 256 284 233 314 301
Qwen3.6-27B 661 716 721 625 576 577
GPT-OSS-120B 448 432 474 350 494 483
I Case Studies
Section 3.6 of the main paper states that representative suc-
cess and failure cases for each task family, with map visual-
izations of agent and reference outputs, are provided here.
Each case gives the task as the agent received it, the output
contract it was scored against, the reference and agent trajec-
tories, a side-by-side rendering of the two outputs, and the
outcome. Scores are strict pass/fail and quantitative closeness
under the metrics of Appendix F. Trajectories are reproduced
exactly as executed, with tool names as exposed by the har-
ness.
I.1 Spatial Joining & Geocoding
Success: Nearest-destination counting Task counting_
destinations_within_one_mile_of_origins
Objective. For each Colorado Front Range origin point,
count the destination points within 1 mile (1609.344 m) of
it.
Constraints.
• Search radius is 1 mile = 1609.344 m; destination points exactly
at the boundary are included; measure in EPSG:26913.
• Attach DEST_CNT_1 (integer destination count) to each ori-
gin point and preserve original origin attributes. Output CRS:
EPSG:26913.
```

---

## PDF 第 25 / 29 页

```text
Output contract.
• origins_with_counts — feature class; geometry Point;
CRS EPSG:26913; required columns DEST_CNT_1.
Reference trajectory (11 steps).
reproject_features → reproject_features →
get_feature_id_field → calculate_attribute_
field → calculate_attribute_field →
calculate_attribute_field → nearest_
features_table → frequency_table → join_
table_by_field → calculate_attribute_field →
save_features
Agent trajectory. Gemini-3.1-Pro, 9 calls, 0 er-
rors – reprojects both layers, then collapses the
reference’s three-step count logic into a single
join_attributes_by_location_within_distance call, fol-
lowed by a field rename and cleanup. A shorter, structurally
different route to the same answer.
Outcome. Pass, quantitative closeness 1.00 (all 6 models
pass this task unanimously; Gemini-3.1-Pro shown as repre-
sentative).
Figure I1: Success case, Spatial Joining & Geocoding: refer-
ence output (left) against agent output (right).
Failure: Interior points from unprojected geometry
Task creating_interior_points_with_projected_
coordinates
Objective. For each SF Bay neighborhood polygon, produce
one interior point that is guaranteed to lie inside the polygon
and attach the polygon’s native FID and the point’s projected
coordinates.
Constraints.
• Each output point must lie inside its source polygon (not just on
the boundary); use EPSG:26910 for coordinate computation.
• Output point fields: POLY_FID (native polygon FID),
X_EPSG2691 (X coordinate in meters, rounded to 2 decimal
places), and Y_EPSG2691 (Y coordinate in meters, rounded to
2 decimal places); preserve original polygon attributes. Output
CRS: EPSG:26910.
Output contract.
• artifact_point_shapefile — feature class; geometry
Point; CRS EPSG:26910; required columns POLY_FID, X_
EPSG2691, Y_EPSG2691.
Reference trajectory (8 steps).
reproject_features → get_feature_id_field →
calculate_attribute_field → point_on_surface
→ add_geometry_attributes → calculate_
attribute_field → calculate_attribute_field
→ save_features
Agent trajectory. DeepSeek-V4-Pro, 14 calls, 0 errors – calls
point_on_surface before reprojecting, then reprojects after-
ward and derives coordinates with add_xy_fields instead of
add_geometry_attributes. Divergence point: step 1. Comput-
ing the interior point before projecting yields a different point
than computing it after — both points fall inside the same
poly
Outcome. Fail, quantitative closeness 0.00, 0 tool-call errors
— the run completes cleanly and produces a valid-looking
point layer that is simply the wrong point.
Figure I2: Failure case, Spatial Joining & Geocoding: refer-
ence output (left) against agent output (right).
I.2 Spatial Overlay & Suitability Analysis
Success:Inward countyboundary inset Task creating_
inland_county_boundary_inset
Objective. From the Harris County boundary polygon, pro-
duce the polygon representing an inward inset of 3,000 m.
Constraints.
• Inset the county polygon boundary 3,000 m inward; keep only
valid non-empty polygon parts; each resulting polygon part is a
separate output feature.
• Output fields: orig_fid (native county polygon FID) and inset_m
(= 3000 for all features). Output CRS: EPSG:26915.
Output contract.
• houston_county_inland_agent — feature class; ge-
ometry Polygon; CRS EPSG:26915; required columns orig_
fid, inset_m.
Reference trajectory (10 steps).
save_features → get_feature_id_field →
calculate_attribute_field → reproject_
features → buffer_features → fix_geometries →
multipart_to_singleparts → calculate_
attribute_field → add_geometry_attributes →
extract_features_by_expression
Agent trajectory. Claude-4.6-Opus, 8 calls, 0 errors –
reproject to buffer_features to multipart_to_singleparts to
compute columns to retain_fields — omits the reference’s
fix_geometries and final expression-based cleanup. A shorter
path that happens not to need the cleanup steps on this par-
ticular input, since the source boundary has no pre-existing
topology
```

---

## PDF 第 26 / 29 页

```text
Outcome. Pass, quantitative closeness 1.00 (all 6 models
pass unanimously; Claude-4.6-Opus shown as representa-
tive).
Figure I3: Success case, Spatial Overlay & Suitability Anal-
ysis: reference output (left) against agent output (right).
Failure: Shoreline clipping with a CRS-preservation trap
Task clipping_shoreline_to_boroughs
Objective. Clip the NYC shoreline lines to the borough poly-
gons and report the clipped length of each original shoreline
segment.
Constraints.
• Retain only shoreline geometry that falls inside borough poly-
gons; measure lengths in EPSG:2263.
• Output: clipped shoreline lines in the input shoreline CRS,
and a CSV with columns: source_fid (native shoreline FID)
and length_m (clipped length in meters, rounded to 2 decimal
places).
Output contract.
• clipped_shoreline_agent — feature class;
geometry Polyline; CRS Preserve the CRS of in-
put_dir/nyc_new_york/transport/shoreline.shp (output must
use the same CRS).
• clipped_lengths_csv — csv; required columns
source_fid, length_m.
Reference trajectory (10 steps).
reproject_features → reproject_features →
fix_geometries → fix_geometries → clip_
features → get_feature_id_field → calculate_
attribute_field → calculate_attribute_field
→ reproject_features → export_table_to_csv
Agent trajectory. Gemini-3.1-Pro, 34 calls, 1 tool-call error
– attempts a field calculation before reprojecting, then re-
projects and clips — this first clip_features call fails with a
real tool error (TopologyException: side location conflict, an
invalid-geometry symptom) because fix_geometries had not
yet been run. The agent recovers by fixing geometries and
re-clipping, then spend
Outcome. Fail, quantitative closeness 0.499 — among the
closest near-misses in this appendix; only DeepSeek-V4-Pro
(1/6) preserves the input CRS correctly on this task.
I.3 Terrain Modeling & Hydrological Analysis
Success: Canal network topology classification
Task classifying_multichannel_canal_segments
Figure I4: Failure case, Spatial Overlay & Suitability Analy-
sis: reference output (left) against agent output (right).
Objective. From the Houston canal line network, classify
each planarized segment as multichannel or single-channel
and report its length.
Constraints.
• Planarize the network by splitting lines at all intersections; an
’island polygon’ is any positive-area polygon enclosed by the
planarized linework.
• A segment is multichannel (is_multich = 1) when it intersects
any island polygon; otherwise it is single-channel (is_multich =
0).
• Output fields: ORIG_FID (native source line FID), is_multich
(0 or 1), and length_m (segment length in meters, measured
in EPSG:26915, rounded to 2 decimal places); output CRS:
EPSG:26915.
Output contract.
• classified_canals — feature class; geometry Poly-
line; CRS EPSG:26915; required columns ORIG_FID, is_
multich, length_m.
Reference trajectory (12 steps).
reproject_features → get_feature_id_field →
calculate_attribute_field → features_to_
lines → polygonize_lines → get_feature_id_
field → calculate_attribute_field → join_
attributes_by_location_summary → calculate_
attribute_field → calculate_attribute_field
→ retain_fields → save_features
Agent trajectory. Claude-4.6-Opus, 14 calls, 0
errors – follows the same planarization (fea-
tures_to_lines to polygonize_lines), then substitutes
a plain join_attributes_by_location plus its own
add_geometry_attributes / extract_features_by_expression
steps for the reference’s single aggregating
join_attributes_by_location_summary call — a mo
Outcome. Pass, quantitative closeness 1.00 (all 6 models
pass unanimously — the only Terrain Modeling task in this
benchmark with a clean sweep; Claude-4.6-Opus shown as
representative).
Failure: Steep-slope polygonization
Task polygonizing_steep_slope_areas
Objective. From the Colorado Front Range DEM, produce
polygons for contiguous areas where slope (on a 10 m grid)
is at least 20 percent.
Constraints.
```

---

## PDF 第 27 / 29 页

```text
Figure I5: Success case, Terrain Modeling & Hydrological
Analysis: reference output (left) against agent output (right).
• Slope in percent at 10 m analysis resolution; cells with slope >=
20% are steep; group contiguous steep cells.
• Output polygon fields: raster_value (class identifier), slope__pct
(maximum slope percent within the polygon, rounded to
2 decimal places), and area_m2 (area in m2, measured in
EPSG:26913, rounded to 2 decimal places); output CRS:
EPSG:26913.
Output contract.
• agent_shapefile — feature class; geometry Polygon;
CRS EPSG:26913; required columns raster_val, slope_
_pct, area_m2.
Reference trajectory (17 steps).
warp_reproject_raster → slope_raster →
raster_calculator → raster_calculator →
polygonize_raster → extract_features_by_
expression → reproject_features → get_
feature_id_field → calculate_attribute_field
→ zonal_statistics_as_table → join_table_by_
field → calculate_attribute_field →
calculate_attribute_field → add_geometry_
attributes → calculate_attribute_field →
retain_fields → save_features
Agent trajectory. Claude-4.6-Opus, 19 calls, 1 tool-call er-
ror – matches the reference up through slope thresholding,
but inserts an extra clump_raster_regions call before polygo-
nize_raster to pre-group contiguous cells — redundant with
what polygonize_raster already does on its own. Divergence
point: this inserted step. It changes the downstream file/ID
chain enoug
Outcome. Fail, quantitative closeness 0.00 (0/6 models pass;
four of six complete with 0–1 tool errors, so the miss is in
the final polygon set, not the process).
I.4 Spatial Pattern Analysis
Success: Park-overlap grid counting Task counting_
park_overlaps_in_grid_cells
Objective. Over the South Florida park extent, create a 1
km polygon grid and count how many distinct park polygons
intersect each cell.
Constraints.
• Grid cell size: 1,000 m; each input park feature contributes at
most 1 to a cell count regardless of how many polygons it has;
cells with no intersecting parks have park_count = 0.
Figure I6: Failure case, Terrain Modeling & Hydrological
Analysis: reference output (left) against agent output (right).
• Output grid polygon fields: grid_id (integer cell identifier) and
park_count; output CRS: EPSG:32617.
Output contract.
• richness_grid — feature class; geometry Polygon; CRS
EPSG:32617; required columns grid_id, park_count.
Reference trajectory (11 steps).
reproject_features → get_feature_id_field →
calculate_attribute_field → fix_geometries →
indexed_fishnet → intersection_overlay →
frequency_table → join_table_by_field →
calculate_attribute_field → save_features →
retain_fields
Agent trajectory. Claude-4.6-Opus, 10 calls, 0 er-
rors – builds the same grid, then collapses the refer-
ence’s three-step overlay-count-join sequence into a single
join_attributes_by_location_summary call — the same kind
of aggregating-join shortcut seen in the canal-classification
success case above.
Outcome. Pass, quantitative closeness 1.00 (4/6 models pass;
Claude-4.6-Opus shown as representative).
Figure I7: Success case, Spatial Pattern Analysis: reference
output (left) against agent output (right).
Failure: Voronoi-clipped hospital buffers Task sf_bay_
voronoi_clipped_hospital_buffers_1_km
```

---

## PDF 第 28 / 29 页

```text
Objective. For each SF Bay hospital, produce a polygon rep-
resenting the intersection of a 1,000 m circle around it and its
bounded Voronoi cell within the neighborhood boundaries.
Constraints.
• Voronoi cells are derived from hospital points, bounded by the
combined neighborhood extent; each hospital’s output polygon
is its 1,000 m circle intersected with its Voronoi cell; measure
in EPSG:26910.
• Output polygon fields: hospit_fid (native hospital FID) and
buffer_rad (= 1000); output CRS: EPSG:26910.
Output contract.
• agent_shp — feature class; geometry Polygon; CRS
EPSG:26910; required columns hospit_fid, buffer_
rad.
Reference trajectory (15 steps).
reproject_features → reproject_features →
get_feature_id_field → calculate_attribute_
field → voronoi_polygons → dissolve_features
→ clip_features → buffer_features → fix_
geometries → fix_geometries → intersection_
overlay → extract_features_by_expression →
calculate_attribute_field → retain_fields →
save_features
Agent trajectory. Gemini-3.1-Pro, 9 calls, 0 errors – re-
project, dissolve, Voronoi, clip — then substitutes a single
specialized clip_point_buffers_to_containing_polygons call
for the reference’s buffer/intersect/expression-filter combi-
nation, and skips both fix_geometries passes entirely. Diver-
gence point: this substitution. The composite tool does not
reproduce the reference’s
Outcome. Fail, quantitative closeness 0.00, 0 tool-call errors
— only Claude-4.6-Opus (1/6) solves this task; three chal-
lenge dimensions stacked at once make it one of the harder
cases in the benchmark. This is also the Spatial Pattern Anal-
ysis exemplar shown in Figure 1 of the main paper.
Figure I8: Failure case, Spatial Pattern Analysis: reference
output (left) against agent output (right).
I.5 Remote Sensing & Image Analysis
Success: NDVI from a color-infrared orthophoto
Task extract_ndvi_values_at_randstad_address_
points_from_cir_orthophoto
Objective. For each Randstad address point, compute NDVI
from the CIR orthophoto at the point location and attach it
to the point layer.
Constraints.
• NDVI (NIR band 1, R band 2); set NDVI to null when either
sampled band is NoData or when NIR + R = 0.
• NDVI field: Float32, rounded to 4 decimal places; preserve all
original address point attributes. Output CRS: EPSG:28992.
Output contract.
• agent_shapefile — feature class; geometry Point; CRS
EPSG:28992; required columns NDVI.
Reference trajectory (9 steps).
reproject_features → rearrange_raster_bands
→ rearrange_raster_bands → raster_calculator
→ sample_raster_values_to_points → rename_
field → calculate_attribute_field → delete_
columns → save_features
Agent trajectory. Claude-4.6-Opus, 8 calls, 0 errors – sam-
ples the raw orthophoto bands directly at the points first, then
computes NDVI as an attribute-field formula on the sampled
band values, reprojecting only at the very end. A different
order of operations — computing the index after sampling
rather than before — that lands on the same NDVI values for
this raster.
Outcome. Pass, quantitative closeness 1.00 (3/6 models pass
this task; Claude-4.6-Opus shown as representative).
Figure I9: Success case, Remote Sensing & Image Analysis:
reference output (left) against agent output (right).
Failure: Landcover raster polygonization with a skipped
reprojection Task vectorize_randstad_landcover_
raster_classes_into_polygons
Objective. Convert the Randstad landcover raster into vector
polygons, grouping 8-connected cells of the same value.
Constraints.
• 8-connected regions (including diagonals); one polygon per con-
nected region; raster_val field stores the integer pixel value.
• Output CRS: EPSG:28992.
Output contract.
• vector_shapefile — feature class; geometry Polygon;
CRS EPSG:28992; required columns raster_val.
```

---

## PDF 第 29 / 29 页

```text
Reference trajectory (5 steps).
warp_reproject_raster → polygonize_raster →
fix_geometries → calculate_attribute_field →
save_features
Agent trajectory. Claude-4.6-Opus, 1 call, 0 errors –
calls polygonize_raster directly on the raw raster and
submits the result. Divergence point: step 1. Skipping
warp_reproject_raster means the output inherits the source
raster’s native geographic CRS (EPSG:4326, degrees) in-
stead of the required EPSG:28992 (meters) — confirmed
directly from the two files’ CRS metadata. Once reproj
Outcome. Fail, quantitative closeness 0.00 (0/6 models pass
this no-caveat control task; every model completes with zero
or one tool-call error, so failure here reflects a specific missed
step rather than general raster-to-vector difficulty).
Figure I10: Failure case, Remote Sensing & Image Analysis:
reference output (left) against agent output (right).
```
