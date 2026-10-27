# 安装、配置与维护

[English](INSTALL.md) · [首页](../README.zh-CN.md) · [设计与验证边界](INSTALLATION-DESIGN.zh-CN.md)

**v2.5.0 仍是审阅候选版。** 2026-10-27 的 R3 检查通过了 Sol/medium 的限定修复门槛，Luna/medium 未通过，不建议用于生产升级。稳定 `main` 保持 v2.4.0。下载前先核对[发布元数据](../github-metadata.json)中的当前修订。安装维护机制仍沿用 v2.4.0，详见 [R3 语义与安装验证](../evals/v2.5.0/revision-20261027/README.md)。

## 推荐：交给 Codex 安装

| 当前情况 | 最短路径 |
| --- | --- |
| 第一次使用 | 提供稳定 `main` 目录，复制下面的安装请求 |
| 已安装，想更新 | 使用下方更新请求，维护现有副本 |
| 只检查是否生效 | 运行 `status`，再做[调用检查](#如何判断成功) |
| 复现候选版 | 使用[隔离项目步骤](#在隔离项目中审阅候选版)，保留日常稳定安装 |

日常使用请把稳定 `main` 分支的文件包或源代码目录提供给支持本地文件操作的 Codex，然后发送：

> 请阅读这个项目的 docs/INSTALL.zh-CN.md，为我的个人 Codex 安装 AI Prompt Optimizer，并启用按需优化。先检查已有安装和配置，保留本地修改与用户规则，使用项目自带安装器；完成后报告实际检查结果。遇到冲突先说明，不覆盖。

默认个人级安装；只希望当前项目使用时，在请求中明确指定项目目录。
这是交给 Codex 的安装请求，不是网页按钮、无条件自动运行的命令或云端安装接口。

“按需优化”只处理模糊、复杂、多约束任务或明确的提示词优化／审核请求；简单问答直接处理。
要求完成任务时会继续执行，要求“只优化”时只交付提示词。不会每轮展示完整优化过程。

已有安装时，不必先下载另一份，直接发送：

> 请找到我已安装的 AI Prompt Optimizer，阅读它的安装维护说明，先运行 status，再使用现有维护程序从稳定 main 更新。保留已有模式、用户规则和本地修改；遇到重复副本、未知目录或降级限制时停止并说明。报告版本、路径、规则状态与新会话验证状态，不要额外安装第二份。

离线更新时提供已审核的新版目录，将“从稳定 main 更新”改为“从这个本地目录更新”。个人／项目范围不明确时先检查现有安装，不自行扩大范围。

## 在隔离项目中审阅候选版

发布元数据确认公开后，先显式选择 `feature/v2.5.0-intent`，再使用 **Code → Download ZIP**。将解压后的源目录放在正在使用的技能发现目录之外。审核文件与元数据后，另建测试项目，从本地来源安装：

```sh
python3 scripts/manage_install.py install --source /absolute/reviewed-candidate --project /absolute/existing-test-project --mode host
```

从已审核的候选源目录执行，将两个路径替换为实际已审核且存在的目录。`--mode host` 不添加默认规则，但宿主仍可能正常发现技能。测试前检查个人／项目已有副本并处理重名冲突，不为审阅候选版替换日常个人安装。公开后也可用 `--ref` 指定已核实的完整 40 位候选提交 SHA，代替 `--source`；不要编造 SHA，也不要向 `--ref` 传入分支名。

## 直接运行

日常稳定版安装，从解压后的 `main` 文件包的 `ai-prompt-optimizer` 根目录运行。候选版审阅使用上面的隔离项目命令：

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
安装器会拒绝不含维护程序的旧版来源，以及比当前托管安装版本更低的来源。
离线更新使用 `update --source <新版目录>`。安装过候选版不会改变默认来源：普通在线 `update` 仍跟随 `main`，不会持续跟踪候选分支，并会拒绝从 v2.5.0 降级到 v2.4.0。复现另一份候选修订时，应明确指定已审核的本地来源或已核实的提交。没有后台自动更新或遥测，也不会索取令牌。

更新前检查已安装文件是否与安装记录一致；有改动、额外文件、丢失文件或后来添加的 Git 历史则停止。
程序会保存备份，先准备完整新版本，再替换目录。发生可捕获的写入异常时尝试恢复旧技能、规则和状态。
关机、进程被强制终止等硬中断可能留下锁和事务记录：不要直接删锁后重试；先核对事务日志、备份及相关文件，
再由用户或 Codex 完成明确的恢复。跨进程编辑、系统故障不能承诺绝对原子性。

卸载移走受管理且未被改动的技能，仅删除原样保留的托管规则块。其他用户规则及备份继续保留。
旧的用户自写优化规则不会被删除，必要时需单独审核调整。

## 如何判断成功

- `version` / `path`：实际受管理的版本与位置；未受管理的旧目录可能没有版本字段。
- `installation`：文件安装／管理状态。
- `policy`：托管规则、宿主默认选择，或已有规则仍待审核。
- `problems` / `warnings`：冲突或待处理事项；不是每次安装成功都等于启用成功。
- `session_verification: not-run`：尚未验证新会话发现与调用。

新建聊天，先确认技能被发现，再用一个普通的模糊任务验证按需行为，同时用一个简单问题检查不过度触发。
不要把文件完整性检查当作模型行为测试。退出码 `0` 表示操作完成（仍需阅读 warnings），`1` 表示失败／拒绝，
`2` 表示状态检查发现问题。

只读检查可以直接说：“请检查 AI Prompt Optimizer 的实际版本、位置、重复副本、规则状态和待处理事项，先不要更新或改配置。”

新会话先显式调用 `$ai-prompt-optimizer`，要求“只优化：把邮件写得清楚一些，保留事实，不新增承诺”；应得到可复用指令，不应编造或发送邮件。再用一个简单问题检查是否直接回答。不点名技能的按需选择需要另行观察。以上是本机试用步骤，不是已经完成的模型测试。

| 状态 | 下一步 |
| --- | --- |
| `not-installed` | 按推荐入口安装；下载目录不等于已安装 |
| `unmanaged` | 检查来源与本地修改，再按迁移步骤处理 |
| `existing-user-guidance-review-needed` | 保留并审阅原有规则，不能只凭退出码宣称按需设置生效 |
| `duplicate-installations` | 识别副本来源与定制，不直接删除或覆盖 |
| `session_verification: not-run` 且无文件问题 | 新建聊天验证发现与调用，无需反复重装 |

## 原生插件预览

发布构建可生成独立技能 ZIP 和插件预览 ZIP，技能内容来自同一份源码。插件包含
`ai-prompt-optimizer` 与只负责首次配置的 `ai-prompt-optimizer-setup`。
插件设置调用同一个配置核心，使用 `configure --plugin-path <宿主已安装的技能目录>`；不会复制第二份技能。
插件更新和移除由宿主管理，维护脚本的 `uninstall` 只撤销其配置记录和规则。

**尚未验证客户端原生安装、自动首次引导或插件市场注册。** 因此本版不提供未经验证的“一键安装”深链接，
也不宣称插件已上架。预览包是下一步客户端集成验证的输入。


宿主发现路径与显式／隐式调用说明于 2026-10-27 对照了 [Codex 官方技能文档](https://developers.openai.com/codex/skills)。文档核对不等于本用户会话已完成实际调用验证。
