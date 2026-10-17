# v2.4.0 installation validation / 安装验证

Date: 2026-10-17. Scope: local installation tooling and packaging; no new model/provider benchmark.

## Automated filesystem checks

`python3 -B -m unittest discover -s tests -v` passed 35 tests on macOS with Python 3.13.
Tests use temporary home/config/project directories and do not alter the real installed skill or global rules.

Coverage includes first/repeated installation, CRLF preservation, user/project scope, custom Codex home,
nonempty override precedence and later override migration, existing user guidance, install-only/host mode,
configuration changes, clean Git adoption and history backup, unknown/modified/extra files, ignored personal
files, newly added Git history, downgrade prevention, missing runtime references, duplicate/symlink refusal,
archive traversal/symlink/case collisions, commit resolution with mocked network responses, network failure,
rollback after an injected state-write error, stale locks/journals, plugin preference setup/removal and a
removed plugin. File tests do not establish real client discovery or implicit invocation.

## Independent forward check

An independent agent performed 16 CLI operations plus four additional fault/configuration scenarios using
isolated macOS home/config directories and local source. Install, repeat, update, disable, enable, uninstall,
project scope, edited-file preservation, override handling, state-write rollback, pending-transaction refusal
and plugin-content preservation passed. It did not edit project source or real user configuration.

One reporting issue was found: existing user-written guidance could prohibit automatic use, while the result
only exposed a policy field and an otherwise generic next step. The final implementation adds an explicit
warning that the requested default is not verified, and directs review of the existing rule. A regression
check verifies the warning and action. The independent checker also repeated the original conflicting-rule scenario after the fix and confirmed both the explicit warning and byte-preserved user guidance. This is a reporting correction, not a new language trial.

## Structural and package checks

Skill structure, Python syntax, shell syntax, JSON/JSONL and local documentation links are checked locally.
The localization renderer reports `30 locales; 0 changed; check passed`. Original license, deliberately buggy
fixtures and historical evaluation records are preserved. Generated installation links explicitly use
English/Simplified Chinese fallback; translations have not acquired new professional review status.

The distribution builder checks that plugin core bytes equal the standalone source. It uses deterministic
ZIP member order, timestamps and permissions and writes SHA256SUMS. A plugin archive is a packaging preview,
not proof of native client installation, automatic onboarding or marketplace registration.

An extracted standalone archive also passed shell-launcher install, status, update, disable and uninstall
under an isolated home containing spaces/non-ASCII text. The extracted plugin core passed preference setup
and removal without deleting plugin files; the setup skill passed structural validation. Two independent
builds produced byte-identical archives. These are package/filesystem checks, not native client installation.

## Pre-publication network verification

On 2026-10-17, the initial real GitHub download exposed a macOS temporary-directory issue:
`/var` is a system alias, and source validation rejected the installer’s own downloaded temporary path.
The installer now canonicalizes only its internally created download directory. User-supplied symlink
sources and archive symlinks remain refused. A regression test covers a symlinked system temp root.

Candidate commit `e667c5b` then passed six CLI operations using anonymous GitHub archive downloads in
an isolated home with spaces and non-ASCII characters: install pinned to the full commit, status, online
update to that commit, configure host mode, configure on-demand mode and uninstall. After installation,
the subsequent operations used the downloaded installer. The recorded source commit matched the requested
commit; the installed directory and managed guidance were removed on uninstall. No GitHub token was used
by the installer. This is a real macOS transport/filesystem check, not a model behavior trial.

The local Codex CLI could not start because its platform runtime dependency was missing, so no new
client discovery/invocation result is claimed. Docker was present but its daemon was unavailable;
Windows/Linux native execution remains outside this run.

## Public-main verification

After fast-forward publication of commit `108a8c8` on 2026-10-17, anonymous GitHub API and archive
requests confirmed the public owner/repository, main commit and byte equality of all 105 tracked files.
The repository description and 20 topics matched `github-metadata.json`; Website remained empty.
A fresh isolated home then passed install, status, update, configure host mode and uninstall using the
public main source. Install/update resolved main through the real GitHub API; the recorded source commit
matched the published commit. Subsequent operations ran the downloaded installer. Publication metadata
was changed to `published` only after these public checks. No tag or GitHub Release was created.

## Remaining limits

- Windows PowerShell and Linux have not been executed on their native platforms; launchers are supplied for review.
- Python 3.9 is the minimum intended runtime; this run used Python 3.13, not a Python-version compatibility matrix.
- Real GitHub archive download/update passed on macOS as described above; power loss/SIGKILL recovery and adversarial concurrent external edits remain unverified.
- No fresh Codex client discovery/implicit invocation or native plugin onboarding test was run.
- No new provider API comparison, language performance trial, native-speaker review or measured user-effort reduction.
- No automatic GitHub publication, tag or Release is performed by the build. Publication status is recorded separately after public verification.

中文摘要：本版验证安装与配置行为，不新增模型效果结论。35 项自动化检查通过，独立检查者完成
16 次 CLI 操作及 4 个补充场景。发现并修正“已有用户规则需审核”的结果提示及 macOS 在线下载临时路径误判；真实 GitHub 固定提交下载的 6 项安装维护操作通过。Windows、Linux、
真实客户端发现和原生插件安装等范围仍待验证；历史语言试用和故意错误样例未重跑或修复。

公开主分支核验：匿名读取确认 105 个文件一致，简介与 20 个 Topics 匹配，Website 为空；
从公开 main 自动解析提交的 5 项安装维护操作通过，随后才记录 published 状态。未创建标签或 Release。
