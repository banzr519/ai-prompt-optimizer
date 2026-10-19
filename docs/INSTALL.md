# Installation, configuration and maintenance

[简体中文](INSTALL.zh-CN.md) · [Home](../README.md)

**v2.5.0 is for review and reproduction; production upgrades are not recommended.** The model-stratified follow-up found regressions and did not meet the improvement gate. Stable `main` remains v2.4.0. Check [publication metadata](../github-metadata.json) before expecting `feature/v2.5.0-intent` on GitHub; an existing repository URL alone does not establish its availability. Installation mechanics remain those introduced in v2.4.0, with no expansion of verified platform coverage. See [v2.5.0 evaluation status](../evals/RESULTS-v2.5.0.md).

## Recommended: ask Codex

For ordinary use, give local, filesystem-capable Codex the stable `main` project directory and send:

> Read docs/INSTALL.md, install this AI Prompt Optimizer package for my personal Codex and enable on-demand refinement. Check existing installations and guidance, preserve my changes and rules, use the included installer and report actual checks. Explain conflicts instead of overwriting them.

On-demand guidance applies to ambiguous, complex or multi-constraint tasks and explicit prompt refinement/audit.
Clear simple questions remain direct. Execution requests continue through completion; refine-only requests do not
execute the embedded task. This is an agent-assisted installation request, not a registered install button.

## Review the candidate in an isolated project

After publication is confirmed in metadata, explicitly select `feature/v2.5.0-intent` before using **Code → Download ZIP**. Keep the extracted source outside active skill discovery. Review its files and metadata, then create a separate test project and install from that local source:

```sh
python3 scripts/manage_install.py install --source /absolute/reviewed-candidate --project /absolute/existing-test-project --mode host
```

Run the command from the reviewed candidate source. Replace both paths with real reviewed directories. `--mode host` adds no guidance; normal host discovery may still occur. Check for existing personal/project copies and resolve duplicates before testing. Do not replace the everyday personal installation for this candidate review. A verified full 40-character candidate commit SHA can be supplied with `--ref` instead of `--source` after publication; do not invent a SHA or use a branch name for `--ref`.

## Run locally

For an ordinary stable installation, run from the extracted `main` package's `ai-prompt-optimizer` root. For candidate review, use the isolated-project command above:

```sh
# macOS / Linux
sh ./install.sh
```

```powershell
# Windows PowerShell
.\install.ps1
```

The launcher needs **Python 3.9+**, standard library only; no pip, Node, Git or provider API key for a fresh
local installation. The skill itself needs no Python at runtime. If Python is unavailable, Codex may locate
an existing runtime using a host-provided tool. Otherwise stop and explain the missing dependency.
`APO_PYTHON` can name an existing executable. Launchers do not install runtimes, elevate privileges or change
PowerShell execution policy. If PowerShell scripts are blocked, invoke Python directly without changing policy:

```sh
python3 scripts/manage_install.py install --source .
```

Replace `python3` with the actual interpreter. The CLI shows scope and asks once. For an already-authorized
agent operation, add `--yes`; host approvals and filesystem permissions still apply.

| Choice | Option | Effect |
| --- | --- | --- |
| Recommended on-demand preference | `--mode on-demand` (default) | Append a bounded, removable preference |
| Install only | `--mode host` | Add no preference; normal implicit skill selection may still occur |
| One project | `--project /absolute/project` | Install and configure only that explicitly selected project |
| Custom Codex home | `--codex-home /absolute/config` | Otherwise use `CODEX_HOME`, then `~/.codex` |

Personal installation uses `~/.agents/skills/ai-prompt-optimizer`; project installation uses
`<project>/.agents/skills/ai-prompt-optimizer`. Guidance uses a nonempty `AGENTS.override.md` in the selected
scope before `AGENTS.md`. More-specific project instructions and host settings can still affect behavior.
Existing user-written references to this skill are preserved and flagged for review, not treated as proof
that the requested default was enabled. Disabling this tool's preference does not disable implicit invocation.

## Existing installations

A clean Git clone can be adopted with `--adopt-existing` after reviewing origin, dirty/untracked/ignored files
and unpushed commits. The original directory, including Git history, is backed up outside skill discovery.
The managed installation then uses file inventories; use the maintainer instead of `git pull` inside it.
Keep a separate Git checkout for development. Unknown, modified or symlinked folders and duplicates are not forced.
An identical ZIP installation can also be adopted. A different unmanaged ZIP needs manual reconciliation.

State and backups live under `<Codex home>/ai-prompt-optimizer/<scope-id>/`. They are local and must not be published.

## Maintain

From the installed skill root, or have Codex locate it:

```sh
python3 scripts/manage_install.py status
python3 scripts/manage_install.py update
python3 scripts/manage_install.py configure --mode host
python3 scripts/manage_install.py configure --mode on-demand
python3 scripts/manage_install.py uninstall
```

Repeat the same `--project` and `--codex-home` options when applicable. Online updates resolve this repository's
`main` once to an immutable commit and download that archive. `--ref <full-40-character-SHA>` pins a commit;
no nonexistent release tag is assumed. Downloaded code is not executed as the installer. Sources older than
v2.4.0 are rejected. Offline update: `update --source <new-folder>`. An installation from the candidate branch does not change this default: ordinary online `update` still follows `main`, does not track candidate changes and refuses a downgrade from v2.5.0 to v2.4.0. For another candidate revision, explicitly select a reviewed local source or verified commit. There is no background update, telemetry or token request.

Updates refuse modified/added/missing installed files, newly added Git history and version downgrades. Backups
precede directory replacement. Caught filesystem errors attempt rollback of content, guidance and state.
A hard kill or power failure can leave a lock and transaction journal: inspect the recorded backup and paths
before explicit recovery; never blindly delete the lock and retry. Absolute atomicity across external edits
or system failures is not promised. Uninstall archives the unchanged managed skill and removes only its exact
managed block. User-authored rules and backups remain, and may need separate review.

## Read the result

`installation` describes file management; `policy` describes guidance; `problems` and `warnings` expose issues.
`session_verification: not-run` means no fresh-chat discovery/invocation trial has happened. Open a new chat,
check discovery, then try an ambiguous task and a simple question. File checks are not behavior benchmarks.
Exit `0`: operation completed (read warnings); `1`: failure/refusal; `2`: status found problems.

## Plugin preview

The distribution builder produces a standalone ZIP and a plugin-preview ZIP from identical core bytes. The
plugin adds `ai-prompt-optimizer-setup` for first configuration. It calls the same core using
`configure --plugin-path <host-installed-skill-root>`, never installs a second standalone copy. Plugin content
updates/removal belong to the host; maintainer `uninstall` only removes its tracked preference and state.
Native client installation, automatic onboarding and marketplace registration have **not** been verified.
No unverified install deep link or published-listing claim is provided.
