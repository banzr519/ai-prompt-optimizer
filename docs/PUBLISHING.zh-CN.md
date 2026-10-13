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
| 建议版本标签 | `v2.1.0` |
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
```

不要加入未支持客户端或无关热门词。GitHub 当前允许最多20个 Topic，每个最多50个字符，使用小写字母、数字与连字符；这里的18个标签符合规则。见 [GitHub Topics 官方说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)。

[github-metadata.json](../github-metadata.json) 保存了推荐仓库名、简介和标签，方便复制。**GitHub 不会自动读取该文件设置 About 或 Topics**，需要在界面或你授权的 API 流程中应用。

## 发布独立仓库

1. 获取**这个技能自身的目录**，将里面的内容作为新仓库根目录，确保 `SKILL.md`、`README.md`、`README.zh-CN.md` 和 `LICENSE` 直接位于根目录。托管导出可能使用内部编号命名，公开及本地安装时用 `ai-prompt-optimizer`。保留相对目录、参考资料和现有图标；不要带上整个私人技能工作区、原 Git 历史、其他技能或账号元数据。
2. 在自己的 GitHub 账号或组织下创建 `ai-prompt-optimizer` 仓库，确认独立目录内容后选择 Public。若从全新本地仓库推送，不要在远端重复生成有冲突的 README 或许可证。
3. 两份用户指南使用已核实的所有者 `banzr519`；发布 Fork 时应更新为对应所有者。若换了仓库名，一并更新克隆地址和对应说明；技能标识本身可以保持 `ai-prompt-optimizer`。
4. 上传独立文件，或从全新独立仓库推送。不要把公共 GitHub remote 加到私人托管 Skills 工作区上。
5. 在 About 中填入上面的简介和 Topics；没有真实项目网站时，Website 留空。公开成功后，再更新 `github-metadata.json` 中的 `publication_status`，需要时记录已核实的真实地址。
6. 打开首页，点击 **简体中文 → English** 检查双向切换；对使用指南、发布指南也各检查一次。在干净临时环境从公开源安装并调用新技能名。
7. 如需发布 Release，给已验证的提交添加 `v2.1.0` 标签，说明新增的模型复用文档，以及调用名此前从 `$clarify-intent` 改为 `$ai-prompt-optimizer`、核心流程未变，以及未开展独立的模型 API 对照测试。

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
