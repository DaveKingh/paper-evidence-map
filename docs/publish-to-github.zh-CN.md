# 发布到 GitHub

## 当前仓库维护者：发布 v0.1.1

`DaveKingh/paper-evidence-map` 的 `v0.1.0` 已经发布，不要删除、移动或重新创建该 Tag。后续更新应从当前 `main` 建分支，通过 PR 合并后创建新版本：

```bash
git switch main
git pull --ff-only
git switch -c release/v0.1.1
```

合并内容后运行本文下面的完整发布门禁，并在 ChatGPT 中把 A9 当前聊天附件优先案例至少重复三次。PR 的必需检查名继续保持为 `repository`；Python 3.9 兼容任务作为额外检查运行。

PR 合并且 CI 通过后，创建 `v0.1.1` Tag，Release notes 使用 [`docs/releases/v0.1.1.md`](releases/v0.1.1.md)。原有 [`v0.1.0`](releases/v0.1.0.md) Release notes 保持不变。

以下第 1–5 节保留为新建仓库或 Fork 首次发布时的通用参考。

## 1. 发布前只需替换两类信息

在仓库根目录搜索 `YOUR_USERNAME`，替换成你的 GitHub 用户名；再按需要把 `LICENSE` 和 `CITATION.cff` 中的作者改成你的姓名或组织名。

需要 Python 3.9 或更高版本。在仓库根目录运行完整发布门禁：

```bash
python -m unittest discover -s scripts/tests -v
python scripts/build_fixture_pdf.py --check
python scripts/validate.py
python scripts/validate.py --response examples/synthetic/expected-output.md --fixture synthetic
python scripts/validate.py --json examples/synthetic/expected-output.json --fixture synthetic
python scripts/validate.py --strict-publish
```

以上命令都应通过。`--response` 的 100 分只检查结构，`--fixture synthetic` 另外检查合成论文的 8 个已知事实，`--json` 检查 Schema 与跨字段约束。它们都不代替人工科学判断。替换完成后，`--strict-publish` 不应再报告 `YOUR_USERNAME`。

Windows 通常使用 `python`；如果 macOS/Linux 上命令名是 `python3`，将上面所有 `python` 换成 `python3`。

## 2. 用 GitHub 网页发布（最适合第一次）

1. 在 GitHub 点击 **New repository**。
2. Repository name 填 `paper-evidence-map`。
3. Description 使用 `docs/launch-plan.md` 中的推荐文案。
4. 选择 **Public**。
5. 不要让 GitHub额外生成 README、`.gitignore` 或 License，本仓库已经包含这些文件。
6. 创建后按 GitHub 页面提示上传仓库全部内容，保留 `.github` 等以点开头的目录。
7. 在 Settings → General → Social preview 上传仓库自带的 [`assets/social-preview.png`](../assets/social-preview.png)（1280×640）。
8. 开启 Issues、Discussions，并按 `docs/publishing-checklist.md` 完成其余设置。

## 3. 用命令行发布

在解压后的仓库目录运行：

```bash
git init
git add .
git commit -m "feat: release Paper Evidence Map v0.1.0"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/paper-evidence-map.git
git push -u origin main
```

其中 `YOUR_USERNAME` 必须替换为你的用户名，并且 GitHub 上要先创建同名空仓库。若使用 GitHub CLI，也可以在本目录运行：

```bash
gh repo create paper-evidence-map --public --source=. --remote=origin --push
```

## 4. 创建首个 Release

1. 打开仓库的 Releases → Draft a new release。
2. Tag 填 `v0.1.0`，target 选择 `main`。
3. 标题填 `Paper Evidence Map v0.1.0 — reproducible first release`。
4. 正文复制 `docs/releases/v0.1.0.md`。
5. 发布后逐项测试 README 中的链接和下载后的完整发布门禁。

## 5. 真正的下载复测

用另一个临时目录重新克隆公开仓库：

```bash
git clone https://github.com/YOUR_USERNAME/paper-evidence-map.git
cd paper-evidence-map
python -m unittest discover -s scripts/tests -v
python scripts/build_fixture_pdf.py --check
python scripts/validate.py
python scripts/validate.py --response examples/synthetic/expected-output.md --fixture synthetic
python scripts/validate.py --json examples/synthetic/expected-output.json --fixture synthetic
```

还要从仓库页面选择 **Code → Download ZIP**，解压到另一个新目录，在该目录重复以上命令。确认 ZIP 中保留 `.github`、`.gitignore`、`examples/synthetic/paper.pdf`、`expected-output.json`、Schema 和测试文件。

最后从 GitHub 页面直接打开中文 Prompt，复制到一个全新的 ChatGPT Project，上传 `examples/synthetic/paper.pdf` 并发送“第一轮”。只有“全新 clone + 全新 ZIP 解压 + 新 Project”都成功，首个版本才算真正可复现。
