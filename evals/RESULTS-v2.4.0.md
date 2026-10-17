# v2.4.0 installation validation / 安装验证

Date: 2026-10-17. Scope: local installation tooling and packaging; no new model/provider benchmark.

## Automated filesystem checks

`python3 -B -m unittest discover -s tests -v` passed 34 tests on macOS with Python 3.13.
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

## Remaining limits

- Windows PowerShell and Linux have not been executed on their native platforms; launchers are supplied for review.
- Python 3.9 is the minimum intended runtime; this run used Python 3.13, not a Python-version compatibility matrix.
- Real GitHub download/update transport, power loss/SIGKILL recovery and adversarial concurrent external edits are not certified.
- No fresh Codex client discovery/implicit invocation or native plugin onboarding test was run.
- No new provider API comparison, language performance trial, native-speaker review or measured user-effort reduction.
- No automatic GitHub publication, tag or Release is performed by the build. Publication status stays prepared until separately verified.

中文摘要：本版验证安装与配置行为，不新增模型效果结论。34 项自动化检查通过，独立检查者完成
16 次 CLI 操作及 4 个补充场景。发现并修正一处“已有用户规则需审核”的结果提示。Windows、Linux、
真实客户端发现和原生插件安装等范围仍待验证；历史语言试用和故意错误样例未重跑或修复。
