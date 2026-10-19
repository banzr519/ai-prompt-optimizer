# AI Prompt Optimizer · AI 提示词优化助手

<!-- language-navigation:start -->
[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md)

[Русский](README.ru.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md)

[Українська](README.uk.md) · [Polski](README.pl.md) · [Português (Brasil)](README.pt-BR.md) · [Pāli](README.pi.md) · [Bahasa Indonesia](README.id.md) · [Italiano](README.it.md)

[Ελληνικά](README.el.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [বাংলা](README.bn.md) · [فارسی](README.fa.md) · [עברית](README.he.md)

[Nederlands](README.nl.md) · [Svenska](README.sv.md) · [Português (Portugal)](README.pt-PT.md) · [Bahasa Melayu](README.ms.md) · [Filipino](README.fil.md) · [Kiswahili](README.sw.md)

[Language coverage / 语言覆盖](docs/LANGUAGES.md)
<!-- language-navigation:end -->

**把模糊描述转成明确、可执行的 AI 指令，同时保留你的原意。**

AI Prompt Optimizer 是一个用于 **AI 提示词优化、Prompt Engineering 和需求澄清的 Agent Skill**。你可以用它改进提示词、检查指令冲突，也可以让它先理清任务，再交给 AI 执行。覆盖开发、设计、写作、分析和日常规划。

**v2.5.0 候选版 · MIT 许可 · 指令技能与可选安装器 · 技能本身无需 API Key**

[快速开始](#快速开始) · [详细使用指南](docs/USER_GUIDE.zh-CN.md) · [English guide](docs/USER_GUIDE.md) · [评测记录](evals/RESULTS.md) · [GitHub 发布指南](docs/PUBLISHING.zh-CN.md)

## 使用前后

**你原来的表达**

> 把产品页做高级一点，原来的文字、价格和按钮功能都别动，手机也要好看。

**转译后的指令**

> 优化现有产品页的视觉呈现，保留全部文字、价格和按钮行为，包括按钮文案与跳转目标。暂按层级清晰、字体统一、间距协调和风格克制的方向理解“高级”，延续现有品牌规范。检查手机端是否存在溢出、重叠、文字难读和按钮难点击的问题。交付前对照原页面核对内容与行为，不新增模块或擅自更换品牌风格。

这是示范表达，不是每次都会套用的固定模板，也不代表效果承诺。

## 它能帮你做什么

| 你遇到的情况 | 技能如何处理 |
| --- | --- |
| “专业一点” | 结合场景明确结构、语气或视觉标准。 |
| “全面一点” | 补充相关流程、证据和重要异常，不无限扩展。 |
| “快一点” | 要求建立基线并用同条件验证，不编造性能目标。 |
| “不要总问我” | 小细节做可逆假设，关键未知信息明确处理。 |
| “只优化提示词” | 输出可复制的指令，不执行指令里的任务。 |
| “理解后直接做” | 最小化澄清，然后继续完成已授权工作。 |

它会保留数字、名称、否定条件和范围，区分事实与假设，识别矛盾要求，并让已经清楚的请求保持简短。包含34类语义模式、10类任务场景和8个教学示例，参考资料按需读取。

## v2.5.0：意图保真

本候选版明确按用户实际要的交付物选择行为：要求分析、修改或继续任务时完成实际工作，要求提示词时才输出可复用指令。只澄清会改变结果或重要行动的信息；承接修改时保留未被改变的限制，并检查否定、或／且、上下限、不确定性和条件授权的原意。

**本版仅供审阅与复现，不建议用于生产升级。** 按模型分层的补测未达到提升门槛：

| 请求的模型配置 | v2.4.0 基线 | v2.5.0 候选 | 恢复／回退 | 候选关键错误 |
| --- | --- | --- | --- | --- |
| GPT-5.6 Luna，medium | 15/16 | 14/16 | 1／2 | 0 |
| GPT-5.6 Sol，medium | 16/16 | 13/16 | 0／3 | 2 |

每种配置 16 对，共 64 个新响应，无重跑。补测复用了此前的补充题集，不是新的独立保留题、模型能力排行或通用兼容性保证。此前继承宿主配置的对照中，两版核心题均为 24/24、入口题均为 4/4、补充题均为 16/16；这些满分结果仅属于该配置的观察。详见 [v2.5.0 评测记录](evals/RESULTS-v2.5.0.md)。

计划仅通过 `feature/v2.5.0-intent` 审阅分支和草稿 PR 交付，稳定 `main` 保持 v2.4.0。实际公开状态与分支以[发布元数据](github-metadata.json)为准；已有仓库地址本身不能证明候选版已公开。

## v2.3.0：多语言

提供30个语言／地区入口，可切换到对应README和入门指南。新增规则分别处理说明、优化后提示词和下游产出的语言，保留简繁体、地区用语、变量及原有限制。巴利语为实验双语入门页。新增翻译由AI编写，尚未经母语专业审校；文档覆盖不代表模型语言能力保证。

[语言目录与覆盖范围](docs/LANGUAGES.md) · [语言验证记录](evals/RESULTS-v2.3.0.md)

## v2.2.0 新增

根据失败回答修订提示词；保留复用变量和输出格式；有依据地比较；整理长对话交接；转译图像与视频需求。简单任务保持简短，不默认增加模型调用，也不用记住新命令。

[进阶用法](docs/USER_GUIDE.zh-CN.md#进阶用法) · [开源研究与改进决策](docs/RESEARCH.zh-CN.md) · [本次验证记录](evals/RESULTS-v2.2.0.md)

## v2.4.0：安装与配置

新增确定性的安装维护程序：个人／项目安装、按需偏好、状态检查、安全更新与备份卸载。可将文件包交给 Codex 完成安装。安装器需要 Python 3.9+；技能日常使用不需要。原生插件包为待验证预览。

[推荐安装与维护](docs/INSTALL.zh-CN.md) · [本版验证及平台边界](evals/RESULTS-v2.4.0.md)

## 快速开始

### 1. 安装

日常使用请将稳定 `main` 分支的文件包提供给 Codex，并发送：

> 请阅读 docs/INSTALL.zh-CN.md，为我的个人 Codex 安装 AI Prompt Optimizer 并启用按需优化。使用项目自带安装器，保留已有配置与本地修改，完成后报告实际验证结果。

如需审阅或复现候选版，先核对[发布状态](github-metadata.json)，再显式选择 `feature/v2.5.0-intent`，通过 `--source` 使用已审核的本地目录，在隔离测试项目中安装。默认克隆、从 `main` 下载 ZIP 和普通在线 `update` 均不会选择或持续跟踪候选版。完整操作、来源选择、Python 要求、旧版迁移及仅安装选项见[安装指南](docs/INSTALL.zh-CN.md)。

<details>
<summary>手动安装与 Git 安装</summary>

下载 ZIP，解压并将技能目录命名为 `ai-prompt-optimizer`，放入 `~/.agents/skills/` 或项目的 `.agents/skills/`。目录直接包含 `SKILL.md`、`agents/` 和 `references/`。手动复制不会自动配置默认偏好。Git 命令及 Windows 路径见[详细指南](docs/USER_GUIDE.zh-CN.md#安装方式)。已有安装先阅读[更新说明](docs/INSTALL.zh-CN.md#位置旧版与既有偏好)。

</details>

### 2. 调用

在 Codex CLI 或 IDE 输入：

```text
$ai-prompt-optimizer 只优化下面这段提示词：把我的报告写得专业一点，但不能改变事实。
```

如果客户端提供技能选择器，选择 **AI Prompt Optimizer · 提示词优化助手**。没有出现时，新建会话或重启客户端。自动触发取决于宿主和当前任务，显式点名调用最容易确认是否生效。

### 3. 用普通语言说明要什么结果

| 用法 | 示例 |
| --- | --- |
| 只优化 | `$ai-prompt-optimizer 整理成清晰的任务指令，先不要执行：……` |
| 完成实际工作 | `$ai-prompt-optimizer 分析这份方案并说明依据：……` 或 `直接修改：……` |
| 检查已有提示词 | `$ai-prompt-optimizer 检查这段提示词的冲突与必要信息缺口：……` |

这些是自然语言用法，不要求专门说“执行”。实际要的结果决定处理方式，调用技能不会把分析或修改任务自动变成提示词改写。没有任务上下文、仅提供被引用需求时，可以默认只优化；“只改写，不执行”仍然阻止执行其中的任务。

## 适用环境

**已列入使用说明的模型系列：**GPT、DeepSeek、Claude、Gemini、Qwen/通义千问、Doubao/豆包、Hunyuan/腾讯混元、ERNIE/文心、GLM、Kimi、MiniMax、Grok、Mistral 和 Llama。通用指令流程面向其中合适的文本/对话版本设计，各模型集成尚未单独实测。详见[14个系列的使用与验证状态表](docs/MODEL_COMPATIBILITY.zh-CN.md)，内含官方资料和具体使用路径。

| 环境 | 本项目提供什么 |
| --- | --- |
| 支持技能的 Codex 环境 | 标准 `SKILL.md` 结构及可选界面元数据。详细指南中的本地目录已对照官方文档。 |
| 其他 Agent Skills 客户端 | 可迁移的 Markdown 指令；加载路径、元数据和工具支持以对应客户端为准，未逐一集成测试。 |
| 通过合适客户端或 API 使用所列模型系列 | 可复用的自然语言规则；上下文和工具由客户端提供，未开展各系列的独立 API 测试。 |
| 不支持 Skills 的普通聊天 | 将 `SKILL.md` 正文作为工作要求，再单独提供原始需求；仅附上必要参考资料。见[普通聊天用法](docs/USER_GUIDE.zh-CN.md#不支持-skills-时怎么用)。 |

它是技能文件，不是在线网站、模型、浏览器插件，也不会切换模型推理参数。它不能补出不存在的工具、绕过权限、保证零错误或消除所有澄清对话。

## 文档与语言切换

| 简体中文 | English |
| --- | --- |
| [大模型适用与使用方法](docs/MODEL_COMPATIBILITY.zh-CN.md) | [Model compatibility and usage](docs/MODEL_COMPATIBILITY.md) |
| [详细使用指南](docs/USER_GUIDE.zh-CN.md) | [Detailed user guide](docs/USER_GUIDE.md) |
| [GitHub 发布与搜索配置](docs/PUBLISHING.zh-CN.md) | [GitHub publishing and discovery](docs/PUBLISHING.md) |

页面顶部的语言链接切换到对应 Markdown 文档，不改变 GitHub 界面语言，也不依赖自动翻译。技能核心只维护一份，避免中英文规则不同步；回答语言跟随用户。

## 验证情况与边界

v2.5.0 增加交付物路由、澄清门槛和多轮承接规则；[按模型分层的补测](evals/RESULTS-v2.5.0.md)在两种已测配置中均发现回退，因此保留审阅候选状态，不替换稳定 v2.4.0。不宣称普遍的精准度提升、成本下降或跨模型验证通过。

v1.0.0 完成8个独立代理任务试用，包括一次合成 Python 代码的实际修复，现有4项测试通过。截至v2.1.0，核心流程保持不变。v2.0.0 调整名称；v2.1.0 补充模型系列的复用说明，未新增API集成。详见[评测记录与局限](evals/RESULTS.md)。原有记录包含16个用例，其中8个在当时未运行。v2.5.0 的新复跑单独记录于[本版评测](evals/RESULTS-v2.5.0.md)，原生客户端的隐式触发检查仍未验证。v2.2.0 新增行为案例及实际观察单独记录于[本次验证记录](evals/RESULTS-v2.2.0.md)。这些结果不等于跨模型基准，也不能证明固定比例的提效或成本下降。

## 从旧版升级

旧名称为 `clarify-intent` / 意图精炼器。**v2.0.0 的调用名称改为 `$ai-prompt-optimizer`**，没有为旧命令自动安装别名。请更新常用提示词与本地文件夹名称，只保留一个生效版本。详见[迁移步骤](docs/USER_GUIDE.zh-CN.md#更新卸载与旧版迁移)。

## 贡献与许可

欢迎提交具体输入、期望行为以及一个不应触发的反例。请勿提交隐私数据或密钥。见[贡献与评测方法](docs/USER_GUIDE.zh-CN.md#贡献与评测)。

采用 [MIT 许可证](LICENSE)，保留原有版权声明。本项目为独立项目，不是任何所列模型提供方的官方产品。
