# 发布到 GitHub

## 1. 发布前只需替换两类信息

在仓库根目录搜索 `YOUR_USERNAME`，替换成你的 GitHub 用户名；再按需要把 `LICENSE` 和 `CITATION.cff` 中的作者改成你的姓名或组织名。

运行：

```bash
python scripts/validate.py
python scripts/validate.py --response examples/synthetic/expected-output.md
```

两条命令都应显示 `PASS`。替换完成后，不应再出现 `YOUR_USERNAME` 提示。

## 2. 用 GitHub 网页发布（最适合第一次）

1. 在 GitHub 点击 **New repository**。
2. Repository name 填 `paper-evidence-map`。
3. Description 使用 `docs/launch-plan.md` 中的推荐文案。
4. 选择 **Public**。
5. 不要让 GitHub额外生成 README、`.gitignore` 或 License，本仓库已经包含这些文件。
6. 创建后按 GitHub 页面提示上传仓库全部内容，保留 `.github` 等以点开头的目录。
7. 在 Settings → General → Social preview 上传由 `assets/demo.svg` 导出的 1280×640 PNG。
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
5. 发布后逐项测试 README 中的链接和下载后的两条验证命令。

## 5. 真正的下载复测

用另一个临时目录重新克隆公开仓库：

```bash
git clone https://github.com/YOUR_USERNAME/paper-evidence-map.git
cd paper-evidence-map
python scripts/validate.py
python scripts/validate.py --response examples/synthetic/expected-output.md
```

然后从 GitHub 页面直接打开中文 Prompt，复制到一个全新的 ChatGPT Project，上传合成论文并发送“第一轮”。只有“重新下载 + 新 Project”都成功，首个版本才算真正可复现。

