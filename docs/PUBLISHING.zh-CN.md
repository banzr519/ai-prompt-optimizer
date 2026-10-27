# GitHub 发布与搜索配置

[English](PUBLISHING.md) | **简体中文** · [返回首页](../README.zh-CN.md)

本指南用于准备独立公共仓库。文件本身不会创建 GitHub 仓库、发布版本或设置 About/Topics；已核实所有者为 `banzr519`；[发布元数据](../github-metadata.json)记录发布状态，公开成功后再记录已核实的仓库地址。

## 命名方案

| 项目 | 内容 |
| --- | --- |
| 仓库名称 | `ai-prompt-optimizer` |
| 英文名称 | AI Prompt Optimizer |
| 中文名称 | AI 提示词优化助手 |
| 技能标识 | `ai-prompt-optimizer` |
| 调用方式 | `$ai-prompt-optimizer` |
| 建议版本标签（仅另获授权时） | `v2.5.0` |
| 旧名称 | `clarify-intent` / 意图精炼器 |

名称使用容易理解的类别词 AI、Prompt、Optimizer，副标题再说明需求澄清和任务指令优化。这是结合用途与公开项目命名作出的判断，不是搜索量研究。其他所有者也可能使用类似仓库名，不声称独占或关联关系；能否创建还要看你所选账号下是否已有同名仓库。

## 可以直接复制的仓库简介

```text
AI prompt optimizer & prompt engineering skill. AI 提示词优化、需求澄清。Portable guidance for GPT, DeepSeek, Claude, Gemini, Qwen, Kimi, GLM, Doubao, Hunyuan, ERNIE, MiniMax, Grok, Mistral & Llama; integrations depend on the host.
```

这里区分了“模型可复用的规则”和“已经单独验证的原生集成”，避免误导使用者。

## Topics 标签

在仓库 About 设置中填写这些相关标签：

```text
prompt-optimizer
prompt-engineering
prompt-optimization
ai-prompts
agent-skills
codex
ai-tools
llm
gpt
deepseek
requirements-engineering
claude
gemini
qwen
kimi
glm
llama
mistral
multilingual
i18n
```

不要加入未支持客户端或无关热门词。GitHub 当前允许最多20个 Topic，每个最多50个字符，使用小写字母、数字与连字符；这里的20个标签符合规则。见 [GitHub Topics 官方说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)。

[github-metadata.json](../github-metadata.json) 保存了推荐仓库名、简介和标签，方便复制。**GitHub 不会自动读取该文件设置 About 或 Topics**，需要在界面或你授权的 API 流程中应用。

## 发布独立仓库

本次 v2.5.0 候选版按下方[候选版检查](#v250-意图保真候选版检查)执行：在已有仓库中通过审阅分支与草稿 PR 交付，稳定 `main` 保持不变。以下通用步骤同时适用于首次发布独立仓库。

1. 获取**这个技能自身的目录**，将里面的内容作为新仓库根目录，确保 `SKILL.md`、`README.md`、`README.zh-CN.md` 和 `LICENSE` 直接位于根目录。托管导出可能使用内部编号命名，公开及本地安装时用 `ai-prompt-optimizer`。保留相对目录、参考资料和现有图标；不要带上整个私人技能工作区、原 Git 历史、其他技能或账号元数据。
2. 在自己的 GitHub 账号或组织下创建 `ai-prompt-optimizer` 仓库，确认独立目录内容后选择 Public。若从全新本地仓库推送，不要在远端重复生成有冲突的 README 或许可证。
3. 两份用户指南使用已核实的所有者 `banzr519`；发布 Fork 时应更新为对应所有者。若换了仓库名，一并更新克隆地址和对应说明；技能标识本身可以保持 `ai-prompt-optimizer`。
4. 上传独立文件，或从全新独立仓库推送。不要把公共 GitHub remote 加到私人托管 Skills 工作区上。
5. 在 About 中填入上面的简介和 Topics；没有真实项目网站时，Website 留空。公开成功后，再更新 `github-metadata.json` 中的 `publication_status`，需要时记录已核实的真实地址。
6. 打开首页，点击 **简体中文 → English** 检查双向切换；对使用指南、发布指南也各检查一次。在干净临时环境从公开源安装并调用新技能名。
7. 如另获授权发布 Release，可对已验证的提交使用 `v2.5.0` 标签。说明安装器的 Python 依赖、实际测试平台、原生插件预览状态以及按需配置边界。保留此前30个语言／地区入口和历史试用的范围说明，不将本次安装检查称为跨模型测试。

仓库根目录本身就是技能目录，无需编译。`evals/fixtures/label.py` 特意保留了用于评测的原始 Bug，不属于运行时业务代码。保留 MIT 原有版权声明。

## 中英文切换如何实现

- `README.md`：英文首页，保留中文副标题/摘要，链接到 `README.zh-CN.md`。
- `README.zh-CN.md`：完整中文首页，链接回英文。
- `docs/USER_GUIDE.md` ↔ `docs/USER_GUIDE.zh-CN.md`：双语详细使用指南。
- `docs/PUBLISHING.md` ↔ `docs/PUBLISHING.zh-CN.md`：双语维护与发布指南。

采用相对链接，方便 Fork 与本地预览。两种语言中的范围、版本、命令和兼容性声明保持一致。这是文档页面切换，不是交互式语言组件或自动翻译，也不依赖 GitHub 根据浏览器语言自动选择文档。技能核心维护一份，实际回答跟随用户语言。

## 搜索发现的实际边界

GitHub 官方说明，仓库搜索可以针对名称、简介、Topics 和 README。未加 `in:` 限定时，搜索范围是名称、简介和 Topics；搜索 README 可使用 `in:readme`。因此将相关词自然写入仓库名与 About，比只藏在长文档里更有意义。见[仓库搜索语法](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)。

公开后可以用这些查询检查发现情况：

```text
ai-prompt-optimizer in:name
prompt-optimizer topic:agent-skills
提示词优化 in:description
prompt optimization in:readme
```

这些检查不保证排名；收录可能有延迟，相关性也会变化。不能根据几个搜索结果推断准确搜索量。不要为了堆关键词而膨胀技能运行时指令，重点保持清楚的用途与真实示例。

## 发布检查

- 确认真实账号、克隆链接与双语切换链接。
- 确认新调用名与迁移说明一致。
- 保留许可证、原有来源归属和评测局限。
- 确认承诺的文件均存在、相对链接可用。
- 明确区分“已准备发布”和“已经发布”、“按可复用设计”和“已验证集成”。

资料核对日期：2026-10-13。来源包括 [GitHub README 文档](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)、上述搜索和 Topics 文档，以及 [Codex 技能文档](https://learn.chatgpt.com/docs/build-skills)。

## v2.3.0 多语言发布检查

运行 `python3 scripts/build_localized_docs.py --check`，检查30个入口及相对链接。发布说明要区分完整主维护文档、本地化入门指南和巴利语实验双语入口。不要声称所有文档均全文翻译、母语审校或所有模型均已实测。不要修改语言目录中的技术标识符。


## v2.4.0 安装分发检查

发布 v2.4.0 前运行 `python3 -B -m unittest discover -s tests -v`、文档生成检查和 `python3 scripts/build_distribution.py --output <仓库外的新目录>`。核验两个 ZIP 与 SHA256SUMS；插件仍标为原生客户端未验证。保留此前评测原文，明确 Python 依赖与平台测试范围。公开成功后再更新本版 publication_status；本次构建不自动创建标签或 Release。

## v2.5.0 意图保真候选版检查

继续运行已有安装、分发和本地化检查作为回归检查。下文分层补测数字是首次候选版的历史记录，当前 R3 另见本页末尾。依据 [v2.5.0 评测记录](../evals/RESULTS-v2.5.0.md)，核对实际交付物路由、澄清价值、多轮有效约束和语义范围。区分确定性的文件检查、实际模型行为观察，以及未参与调试任务的版本对照。缺少对照证据支持时不得宣称精准度已明显提升，也不得把有限结果外推到所有任务、语言或模型系列。继承宿主配置的两组题未观察到版本差异，但按模型分层补测中，Luna medium 为 15/16 → 14/16（恢复 1、回退 2、候选关键错误 0），Sol medium 为 16/16 → 13/16（恢复 0、回退 3、候选关键错误 2），未达到提升门槛。稳定 `main` 保持 v2.4.0，实际启用的技能不替换；仅公开 `feature/v2.5.0-intent` 审阅分支并创建草稿 PR，不作为生产升级。

候选分支实际公开并核验前，`publication_status` 保持 `prepared-not-published`；已有仓库地址不能证明候选版已上传。核验后记录实际仓库地址、候选分支／提交与审阅状态；候选版公开不代表已被接纳为稳定版。正常推送前检查远端改动，不强推或覆盖不明改动。构建候选包或更新文档不会自动授权创建标签或 GitHub Release。安装说明必须区分稳定 `main` 与显式选择的候选版：使用已审核的本地 `--source` 或已核实完整 SHA 的 `--ref`；普通在线 `update` 跟随 `main`，不会自动跟踪候选分支。

若宣称某模型上的收益，需要该模型及推理档位内的明确版本对照。继承宿主配置的测试不能代表较弱模型。区分直接使用技能与优化器向执行器交接提示词两条路径；已暴露题集继续作为诊断／回归材料，不将不同模型的数据合并以凑足提升门槛。本次每种配置复用 16 题，共 64 个新响应、无重跑，不是新的独立保留题或模型能力排行。原始盲评在 63/64 个响应的总判与关键错误标志上一致，剩余分歧经盲态复核达成一致。见[按模型分层的补测协议](../evals/v2.5.0/model-strata/PROTOCOL.md)及[结果](../evals/RESULTS-v2.5.0.md)。


## 2026-10-27 修订记录

R3 保留首次失败候选版与 R2 的完整记录。[本轮证据](../evals/v2.5.0/revision-20261027/README.md)显示 Sol/medium 通过限定修复门槛，Luna/medium 未通过。分别保留模型与轮次结果，不升级稳定版。完成确定性检查后更新现有审阅分支与草稿 PR；本地新修订先将发布状态重置为 `prepared-not-published`，实际公开且逐文件核验对应提交后才写为 `published`，此前发布标识另行保留。候选分支公开和安装维护测试均不能替代新会话发现、调用或原生插件引导验证。
