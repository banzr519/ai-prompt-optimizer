# 安装、配置与维护

[English](INSTALL.md) · [首页](../README.zh-CN.md) · [设计与验证边界](INSTALLATION-DESIGN.zh-CN.md)

**v2.4.0 本地候选版。** 当前文件包可用于安装与验证；是否已公开发布以
[发布元数据](../github-metadata.json)为准。已有仓库地址不代表本版本已发布。

## 推荐：交给 Codex 安装

把本文件包或源代码目录提供给支持本地文件操作的 Codex，然后发送：

> 请阅读这个项目的 docs/INSTALL.zh-CN.md，为我的个人 Codex 安装 AI Prompt Optimizer，并启用按需优化。先检查已有安装和配置，保留本地修改与用户规则，使用项目自带安装器；完成后报告实际检查结果。遇到冲突先说明，不覆盖。

默认个人级安装；只希望当前项目使用时，在请求中明确指定项目目录。
这是交给 Codex 的安装请求，不是网页按钮、无条件自动运行的命令或云端安装接口。

“按需优化”只处理模糊、复杂、多约束任务或明确的提示词优化／审核请求；简单问答直接处理。
要求完成任务时会继续执行，要求“只优化”时只交付提示词。不会每轮展示完整优化过程。

## 直接运行

在解压后的 `ai-prompt-optimizer` 根目录运行：

macOS / Linux：

```sh
sh ./install.sh
```

Windows PowerShell：

```powershell
.\install.ps1
```

启动器查找 Python 3.9+，不需要 pip、Node、Git或模型 API Key。**安装器需要 Python；技能本身不需要。**
若没有找到运行时，可让 Codex 使用宿主提供的运行时定位工具；没有可用工具或运行时时会停止并说明。
`APO_PYTHON` 可指定已有 Python 可执行文件。程序不会自动安装 Python、提权或修改 PowerShell 执行策略。
如果系统禁止运行 PowerShell 文件，使用可用的 Python 直接执行下面的核心命令，不更改系统策略。

直接调用核心（将 `python3` 替换为实际 Python 3.9+ 可执行文件）：

```sh
python3 scripts/manage_install.py install --source .
```

CLI 会显示操作范围并询问一次。由 Codex 在用户已明确授权后执行时可加 `--yes`。
它不会绕过宿主自身的审批和文件访问限制。

| 选择 | 参数 | 结果 |
| --- | --- | --- |
| 按需优化，推荐 | `--mode on-demand`，默认 | 在实际生效的指导文件中追加一小段可撤销规则 |
| 仅安装 | `--mode host` | 不添加默认规则；宿主仍可能根据技能描述自动选择 |
| 仅当前项目 | `--project /absolute/project` | 安装在该项目，配置该项目的指导文件 |
| 自定义配置目录 | `--codex-home /absolute/codex-home` | 否则遵循 `CODEX_HOME`，再回退到个人 `.codex` |

“仅安装”和“关闭默认规则”不等于禁止宿主隐式调用，也不会改写原有 `allow_implicit_invocation`。

## 位置、旧版与既有偏好

个人技能安装到 `~/.agents/skills/ai-prompt-optimizer/`；项目安装到指定项目的
`.agents/skills/ai-prompt-optimizer/`。配置优先选取该范围内非空的 `AGENTS.override.md`，否则是 `AGENTS.md`。
项目自己的更深层规则、其他个人偏好以及宿主配置仍可能改变最终行为，文件检查不会证明每轮都调用。

如果指导文件已有提及本技能的用户规则，安装器保留原文并报告 `existing-user-guidance-review-needed`，
由 Codex 阅读原规则判断是否符合用户目标。它不会自动认定“启用成功”，也不会删除已有自定义规则。

旧 Git 安装先检查来源、未提交修改、未推送提交和被忽略的个人文件。检查通过后，使用
`install --source <新版源目录> --adopt-existing`。原目录和 Git 历史会完整备份，新的安装由文件清单维护。
不再在受管理的安装目录内执行 `git pull`；开发仓库仍可保留 Git 工作流。

未知 ZIP、不同内容的目录、符号链接路径、重复副本或本地定制会被保留并要求先处理，不提供强制覆盖选项。
与待安装版本完全一致的 ZIP 目录可以采用 `--adopt-existing` 接管。状态和备份保存在
`<Codex配置目录>/ai-prompt-optimizer/<范围标识>/`，位于技能发现目录之外。

## 检查、更新、关闭与卸载

在已安装技能根目录运行，或让 Codex 找到该目录执行：

```sh
python3 scripts/manage_install.py status
python3 scripts/manage_install.py update
python3 scripts/manage_install.py configure --mode host
python3 scripts/manage_install.py configure --mode on-demand
python3 scripts/manage_install.py uninstall
```

项目安装和自定义配置目录在每次维护时使用相同的 `--project` / `--codex-home` 参数。

在线更新只访问本项目 GitHub，先把 `main` 解析为一个具体提交，再下载该提交的归档；也可用
`--ref <完整40位提交SHA>` 固定来源。下载内容不会作为安装器代码直接执行。不要使用不存在的版本标签。
在 v2.4.0 尚未发布时，在线源可能仍为旧版，安装器会拒绝不含维护程序或版本更低的来源。
离线更新使用 `update --source <新版目录>`。没有后台自动更新或遥测，也不会索取令牌。

更新前检查已安装文件是否与安装记录一致；有改动、额外文件、丢失文件或后来添加的 Git 历史则停止。
程序会保存备份，先准备完整新版本，再替换目录。发生可捕获的写入异常时尝试恢复旧技能、规则和状态。
关机、进程被强制终止等硬中断可能留下锁和事务记录：不要直接删锁后重试；先核对事务日志、备份及相关文件，
再由用户或 Codex 完成明确的恢复。跨进程编辑、系统故障不能承诺绝对原子性。

卸载移走受管理且未被改动的技能，仅删除原样保留的托管规则块。其他用户规则及备份继续保留。
旧的用户自写优化规则不会被删除，必要时需单独审核调整。

## 如何判断成功

- `installation`：文件安装／管理状态。
- `policy`：托管规则、宿主默认选择，或已有规则仍待审核。
- `problems` / `warnings`：冲突或待处理事项；不是每次安装成功都等于启用成功。
- `session_verification: not-run`：尚未验证新会话发现与调用。

新建聊天，先确认技能被发现，再用一个普通的模糊任务验证按需行为，同时用一个简单问题检查不过度触发。
不要把文件完整性检查当作模型行为测试。退出码 `0` 表示操作完成（仍需阅读 warnings），`1` 表示失败／拒绝，
`2` 表示状态检查发现问题。

## 原生插件预览

发布构建可生成独立技能 ZIP 和插件预览 ZIP，技能内容来自同一份源码。插件包含
`ai-prompt-optimizer` 与只负责首次配置的 `ai-prompt-optimizer-setup`。
插件设置调用同一个配置核心，使用 `configure --plugin-path <宿主已安装的技能目录>`；不会复制第二份技能。
插件更新和移除由宿主管理，维护脚本的 `uninstall` 只撤销其配置记录和规则。

**尚未验证客户端原生安装、自动首次引导或插件市场注册。** 因此本版不提供未经验证的“一键安装”深链接，
也不宣称插件已上架。预览包是下一步客户端集成验证的输入。
