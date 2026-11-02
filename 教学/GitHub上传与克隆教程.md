# GitHub 上传与克隆教程（Windows 实操）

示例仓库：[caldwellelvin430/paper-learning](https://github.com/caldwellelvin430/paper-learning)。本文的命令在 **PowerShell** 中运行。按小节依次执行，每一步成功后再继续；不要把所有命令一次性粘贴执行。

## 1. 先理解整个流程

```text
GitHub 远程仓库 ── clone（首次下载）──> 电脑上的本地仓库
本地仓库：复制/修改文件 → add（暂存）→ commit（本地记录）
本地提交 ── push（上传）──> GitHub
GitHub 新提交 ── pull（同步）──> 已有的本地仓库
```

- **仓库**存放文件和版本历史。本项目的文件位于“论文翻译”目录。
- **GitHub Projects** 是看板。例如 `/users/用户名/projects/1` 不是代码仓库，不能作为 `git clone` 的地址。
- **克隆**会下载文件和 `.git` 版本信息；网页的 Download ZIP 只下载文件，解压后不能直接在里面执行 `git push`。
- **commit** 只保存在电脑上，执行 **push** 后 GitHub 网页才会更新。
- 同一个仓库通常只需克隆一次，以后进入该目录同步即可。

## 2. 准备 Git 和登录方式

从 [Git 官方网站](https://git-scm.com/downloads/win)安装 Git for Windows。安装时保留 Git Credential Manager；安装完成后关闭并重新打开 PowerShell。

```powershell
git --version
```

能看到版本号即可。在这台电脑上首次使用 Git 时，配置提交署名：

```powershell
git config --global user.name "你的署名"
git config --global user.email "你的 GitHub 提交邮箱"
```

将引号中的两项替换为自己的信息。邮箱可以使用 GitHub → Settings → Emails 中提供的 noreply 邮箱。这是提交署名，不等于登录 GitHub，也不授予写入权限。

HTTPS 推送需要身份验证。Git Credential Manager 通常会引导浏览器登录；使用拥有该仓库写入权限的账户完成授权。GitHub 账户密码不能直接充当 HTTPS Git 密码。不要把令牌写进仓库文件或远程地址。

## 3. 第一次克隆这个仓库

选择一个存放项目的位置。以下示例使用你的文档目录下的 `GitProjects`：

```powershell
$projectRoot = Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'GitProjects'
New-Item -ItemType Directory -Path $projectRoot -Force | Out-Null
Set-Location -LiteralPath $projectRoot
git clone https://github.com/caldwellelvin430/paper-learning.git
```

克隆成功后进入本地仓库：

```powershell
Set-Location -LiteralPath (Join-Path $projectRoot 'paper-learning')
git remote -v
git status
```

`git remote -v` 应显示 `caldwellelvin430/paper-learning.git`；`git status` 应显示当前分支和工作区状态。`origin` 是远程仓库的默认别名。

如果这个目录已存在，先确认它是否就是之前克隆的仓库；不要再次在它里面嵌套克隆。进入已有仓库后执行下一节。

## 4. 每次上传前先同步

在本地 `paper-learning` 目录中运行：

```powershell
git status
git switch main
git pull --ff-only origin main
```

开始前最好让工作区保持干净。若已有未提交修改，先确认并提交自己的修改，再同步。`--ff-only` 在本地与远程各有独立提交时会停止，而不会自动合并；遇到这种情况见后面的排错说明。

## 5. 把论文文件放进“论文翻译”

已经上传到仓库的资料，克隆后就会自动下载，**不需要再解压上传一次**。本节用于你以后新增论文或更新资料。

建议目录如下：

```text
paper-learning/
├── README.md
├── 教学/
│   └── GitHub上传与克隆教程.md
└── 论文翻译/
    ├── README.md
    ├── GISAgentBench_中文译文/
    ├── GeoAgentBench/
    ├── AgentSuite/
    ├── tau-bench/
    ├── GeoContra/
    └── AgentJudgeBench/
```

最直观的做法：在资源管理器中解压压缩包，再把每篇论文的文件夹复制到本地仓库的“论文翻译”目录。保留 Markdown、`images`、`source_pages` 等原有层级，否则文中的相对图片链接可能失效。

也可以用 PowerShell。以下只适用于**新增且不与已有资料重名**的压缩包；将示例 ZIP 路径替换为实际文件路径：

```powershell
$zipPath = 'D:\下载\你的新论文合集.zip'
$reviewPath = Join-Path ([IO.Path]::GetTempPath()) ('paper-review-' + [Guid]::NewGuid().ToString('N'))
Expand-Archive -LiteralPath $zipPath -DestinationPath $reviewPath
Invoke-Item -LiteralPath $reviewPath
Invoke-Item -LiteralPath (Join-Path (Get-Location) '论文翻译')
```

这会打开临时解压目录和仓库目标目录。在资源管理器中检查后复制所需论文文件夹；如果提示同名文件，先比较内容再决定是否替换。不要直接把 ZIP 当作已解压的资料：只上传 ZIP，网页上就不能直接阅读里面的 Markdown。

编码文件名中的 `%E4%...` 不影响解压；`-LiteralPath` 配合引号可以处理空格、中文及这些字符。无需手工将它转换成中文文件名。

在“论文翻译/README.md”里添加阅读入口，例如：

```markdown
- [新论文中文稿](新论文/新论文_中文全文.md)
```

Git 不记录空目录。想让新文件夹在 GitHub 上出现，需要在其中加入 README 或其他实际文件。

## 6. 检查、提交并推送

先查看变化：

```powershell
git status --short
git diff --stat
```

`??` 表示新文件，`M` 表示已修改，`D` 表示删除。`git diff --stat` 默认不列出尚未跟踪的新文件，所以要结合 `git status` 看。如果出现意外的删除，先停下来核对。

只暂存这次需要上传的资料：

```powershell
git add -- "论文翻译"
git diff --cached --stat
git diff --cached --name-status
```

最后两条用于检查本次提交会包含哪些文件。确认无误再执行：

```powershell
git commit -m "添加新的论文中文精读和原文图表"
git push origin main
```

如果你修改的是教学文档，则暂存 `git add -- "教学"`；同时修改多个目录时，可以在 `git add --` 后写多个路径。相比直接 `git add .`，指定目录更容易控制上传范围。

如果发现文件不应该被暂存，可在提交前执行：

```powershell
git restore --staged -- "误暂存的文件路径"
```

这只取消暂存，保留本地文件。之后重新检查暂存列表，再提交。

## 7. 验证上传是否完成

```powershell
git status
git log -1 --oneline
```

推送成功且没有其他本地改动时，通常能看到 `working tree clean`。但这句话单独只能证明没有未提交修改，不能证明已经推送；还需确认 `git push` 成功，并打开 [仓库网页](https://github.com/caldwellelvin430/paper-learning)检查：

1. 分支选择为 `main`，最新提交说明与自己的提交一致。
2. “论文翻译”中能看到新论文文件夹。
3. 点击中文 Markdown，抽查图片是否正常显示。
4. 点击原文或原稿页面文件，确认没有遗漏。

## 8. 以后常用的最短流程

在已有的本地仓库里，先运行：

```powershell
git status
git pull --ff-only origin main
```

同步成功后，再复制或修改文件，然后：

```powershell
git add -- "论文翻译"
git diff --cached --stat
git commit -m "更新论文学习资料"
git push origin main
```

如果没有任何变化，`git commit` 会提示没有可提交的内容，这是正常情况。

## 9. 不用命令行：GitHub Desktop

如果更喜欢图形界面，可安装并登录 [GitHub Desktop](https://desktop.github.com/)。

1. 选择 **File → Clone repository**，在 URL 页粘贴 `https://github.com/caldwellelvin430/paper-learning.git`，选择本地目录并克隆。
2. 确认分支为 `main`，点击 **Fetch origin**；如有远程更新，点击 **Pull origin**。
3. 在资源管理器里打开这个本地仓库，将论文文件夹放入“论文翻译”。
4. 回到 Desktop，在 **Changes** 中核对文件，填写提交说明，提交到 `main`。
5. 点击 **Push origin**，再去 GitHub 网页核对结果。

Desktop 克隆出的目录本身也是 Git 仓库，可与命令行共用；不要为同一目录重复执行 `git init`。

## 10. 常见问题

| 提示或现象 | 原因与处理 |
| --- | --- |
| 找不到 `git` | 安装 Git 后重开 PowerShell；检查 Git 是否加入 PATH。 |
| `not a git repository` | 当前不在克隆后的仓库目录。进入 `paper-learning` 后用 `git status` 检查。 |
| 克隆时目标目录已存在且非空 | 如果那是已有仓库，直接进入并同步；否则选择一个新的本地目录。 |
| `Author identity unknown` | 配置第 2 节的 `user.name` 和 `user.email`。 |
| `Repository not found` 或 403 | 检查 `git remote -v`、仓库地址、当前登录账户及仓库权限。能看公开仓库不代表能写入它。 |
| 认证失败 | 使用 Credential Manager 重新认证正确账户；不要输入 GitHub 账户密码作为 Git 密码。 |
| `non-fast-forward` 或 `rejected` | 远程有新提交。先提交自己的修改，再 `git fetch origin`，用 `git log --oneline --graph --all -15` 比较；必要时 `git merge origin/main` 合并，检查后再推送。不要直接强制推送。 |
| 合并冲突 | 用 `git status` 找冲突文件，编辑保留正确内容并去掉冲突标记，`git add -- "冲突文件路径"` 后 `git commit`，再推送。若暂时无法处理，可在合并尚未结束时用 `git merge --abort` 退出本次合并，再检查状态。 |
| 图片没有显示 | 检查 Markdown 相对链接、目录层级和文件名大小写；确认对应图片也在提交中。 |
| 中文路径显示成转义字符 | 仅影响终端显示，可运行 `git -c core.quotepath=false status --short` 查看中文路径。 |
| 推送成功但网页没有变化 | 确认网页账户、仓库和分支正确；核对提交记录并刷新页面。 |

## 11. 文件大小和资料管理

GitHub 网页上传的单文件上限是 **25 MiB**；常规 Git 仓库阻止超过 **100 MiB** 的单文件，超过 **50 MiB** 时会警告。更大的文件应考虑 Git LFS 或 Releases，详见 [GitHub 大文件说明](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)。图片较多的论文包使用 Git/ Desktop 上传更合适。

提交前检查文件列表，避免把临时解压目录、账号凭据等无关文件一起加入。当前论文资料使用相对图片路径；移动论文文件时，应保持配套图片目录一起移动。

## 官方参考

- [克隆仓库](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- [从本地添加文件到 GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
- [使用 Git Credential Manager](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git)
- [GitHub Desktop 文档](https://docs.github.com/en/desktop)

文档编写日期：2026-11-02。界面名称可能随 GitHub 更新而变化，以官方文档为准。
