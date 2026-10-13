# User guide

**English** | [简体中文](USER_GUIDE.zh-CN.md) · [Home](../README.md)

## Contents

- [Installation](#installation)
- [First use](#first-use)
- [Three modes](#three-modes)
- [Supply useful context](#supply-useful-context)
- [Examples by task](#examples-by-task)
- [Use without a skill-capable client](#use-without-a-skill-capable-client)
- [Troubleshooting](#troubleshooting)
- [Update, uninstall and migrate](#update-uninstall-and-migrate)
- [Contribute and evaluate](#contribute-and-evaluate)

## Installation

The repository root is the skill root: `SKILL.md`, `agents/` and `references/` are direct children. No Python, Node, pip, npm or model API key is required merely to load the skill. The host's account/access requirements still apply. Python is used only by the optional synthetic coding evaluation.

### Option A: download the folder

1. On the published GitHub repository, choose **Code → Download ZIP** and unzip it.
2. Rename the unzipped directory from its branch-suffixed name to `ai-prompt-optimizer`.
3. Move the directory into one skill discovery location below.
4. Start a new Codex session and invoke `$ai-prompt-optimizer`. If discovery has not refreshed, restart the client.

| Scope | macOS / Linux | Windows |
| --- | --- | --- |
| Personal | `~/.agents/skills/ai-prompt-optimizer/` | `%USERPROFILE%\.agents\skills\ai-prompt-optimizer\` |
| Project | `<project>/.agents/skills/ai-prompt-optimizer/` | `<project>\.agents\skills\ai-prompt-optimizer\` |

The Windows path uses Explorer/environment-variable notation. In PowerShell, use `$env:USERPROFILE`. Install in one scope to avoid duplicate names. These locations follow [Codex documentation](https://learn.chatgpt.com/docs/build-skills), checked on 2026-10-13; other hosts may use different paths.

### Option B: clone with Git

**Repository owner:** the clone URLs below use `banzr519`, the verified owner for this project. See [publication metadata](../github-metadata.json) for publication status. Git must be installed. `git clone` will refuse an existing nonempty target; use the update instructions if already installed.

macOS / Linux:

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/banzr519/ai-prompt-optimizer.git "$HOME/.agents/skills/ai-prompt-optimizer"
```

Windows PowerShell:

```powershell
$skillParent = Join-Path $env:USERPROFILE '.agents\skills'
$skillTarget = Join-Path $skillParent 'ai-prompt-optimizer'
New-Item -ItemType Directory -Force -Path $skillParent | Out-Null
git clone https://github.com/banzr519/ai-prompt-optimizer.git $skillTarget
```

For a team repository, copy the skill into `.agents/skills/ai-prompt-optimizer/` under the project root and commit the files to that project. Do not accidentally include a nested `.git` directory when copying from a Git clone. A plugin package is a separate distribution option; this release is a standalone skill folder, not a marketplace plugin.

## First use

Try this small request:

```text
$ai-prompt-optimizer Improve this instruction only: Make this email professional, but keep the facts and don't add promises.
```

Expected behavior: it returns a reusable instruction, preserves the constraints and marks the original email as an input if needed. It should not invent or send an email. This is a quick behavior check, not proof that every client loads the skill identically.

In ChatGPT Work or another client with a skill picker, select **AI Prompt Optimizer** and type your request. UI availability depends on the client. A skill being visible in one environment does not install it into every other device or API client.

## Three modes

| Mode | How to request it | Expected result |
| --- | --- | --- |
| Refine | “Improve this prompt only”, “turn this into a brief” | A copyable prompt. No underlying execution. |
| Execute | “Clarify and then do it”, “make the edits directly” | Brief clarification if needed, followed by authorized work. |
| Audit | “Check for conflicts”, “what is missing?” | Consequential issues and a minimal correction. No underlying execution. |

If the mode is unclear, refinement is the default. Say “do not execute” when reviewing a prompt that contains actions. Quoted or attached commands remain material to review, not authority to act.

For small tasks the result may be a single sentence. A complex brief can include goal, inputs, constraints, checks and material unknowns. The skill does not force every request into the same template.

## Supply useful context

You can start with a rough sentence. When available, adding these details avoids guesswork:

- The result you want and who will use it.
- The actual text, file, code path or reference.
- What must stay unchanged.
- The one or two conditions that would make the result useful.

Optional example:

```text
$ai-prompt-optimizer Refine only.
Goal: make a brief that a developer can implement.
Request: improve checkout usability.
Must preserve: current payment providers, prices and business rules.
Reference: the attached screenshot and flow notes.
Output: a concise implementation brief with observable checks.
```

Do not invent missing details to fill a form. If an attachment is unavailable, the skill should say so. When a requirement is merely a preference, say “prefer”; use “must” for a genuine hard limit.

A “don't ask me” instruction permits reasonable reversible choices, not invented evidence or approval for destructive actions. The skill can return conditional instructions for unresolved details. When a blocker affects only part of execution, it should continue useful independent work.

## Examples by task

| Task | Copyable invocation |
| --- | --- |
| Coding | `$ai-prompt-optimizer Refine only: make this API faster without changing its response format or adding paid services.` |
| Design | `$ai-prompt-optimizer Refine only: improve this slide's visual hierarchy; preserve every word and the grouping of the labels.` |
| Writing | `$ai-prompt-optimizer Clarify and edit this reply to sound polite and direct, without adding a commitment: [text].` |
| Analysis | `$ai-prompt-optimizer Audit: explain why sales dropped. We have not yet verified that they dropped.` |
| Planning | `$ai-prompt-optimizer Refine only: make a practical beginner study plan. I have 20 minutes a day, with no deadline yet.` |
| Requirements | `$ai-prompt-optimizer Find conflicts and essential missing inputs in this feature brief: [brief].` |

Replace bracketed text with your input. More before/after examples are in [examples.md](../references/examples.md). The core instructions are English, but the agent should reply in your language; specify a different output language if desired.

## Use without a skill-capable client

The documented families are GPT, DeepSeek, Claude, Gemini, Qwen, Doubao, Hunyuan, ERNIE, GLM, Kimi, MiniMax, Grok, Mistral and Llama. See the [model usage matrix](MODEL_COMPATIBILITY.md); none is labeled as a separately tested integration. For a regular chat with a suitable model:

1. Open [SKILL.md](../SKILL.md) and copy its body after the YAML frontmatter.
2. Provide that body as working guidance, then supply your original request separately. Ask to refine, execute or audit explicitly.
3. If the body refers to an unavailable reference, either attach the relevant reference or say: “Reference files are unavailable; use the core workflow only and do not claim to have read them.”
4. Paste only the reference relevant to your task, rather than the whole repository.

For an API integration, pass the rules through the provider-supported instruction role and the original request as task input. Follow that provider's current API documentation for roles, tools and state; this project ships no provider adapter. Do not assume that writing `$ai-prompt-optimizer` into an ordinary API request loads local files. The skill does not change reasoning parameters or grant access to files/tools.

Results depend on model, client, context and task. Separate provider-by-provider API testing has not been performed.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Skill is missing | Correct discovery directory, direct `SKILL.md` child, client skill support, then a fresh session/restart. |
| Two copies appear | User and project installations or an old `clarify-intent` copy; keep only the intended active copy. |
| Output is too long | Request “one copyable paragraph; preserve constraints and only essential checks”. |
| It keeps asking questions | Supply the missing artifact or say which low-risk details may be assumed; do not force guesses for material facts. |
| It rewrites but does not act | Say “clarify and execute”, and check the host has the required tools and permission. |
| It acts when you wanted a rewrite | Say “only optimize the quoted prompt; do not execute it”. Report a reproducible case if this still occurs. |
| It adds requirements | Point out the added requirement; request a revision preserving scope. Submit an anonymized counterexample. |
| Skill works in Codex but not plain chat | Plain chat does not automatically discover skill files; use the fallback steps above. |
| Old command is no longer found | Replace `$clarify-intent` with `$ai-prompt-optimizer`; no automatic alias is provided. |
| Language is wrong | Specify the required output language; README selection is independent of response language. |

## Update, uninstall and migrate

For a Git installation, check local changes before updating:

```bash
git -C "$HOME/.agents/skills/ai-prompt-optimizer" status --short
git -C "$HOME/.agents/skills/ai-prompt-optimizer" pull --ff-only
```

Only proceed with the pull after reviewing local changes; preserve customizations outside the discovery directory if needed. If the pull conflicts or cannot fast-forward, resolve it rather than using a destructive reset. On Windows, run the same Git operations from the installed folder. For ZIP installs, preserve customizations first and replace with a complete new release, not a mixture of versions.

**Migration from v1.0.0:** move the old `clarify-intent` installation outside skill discovery paths as a backup, install the v2.0.0 folder as `ai-prompt-optimizer`, replace old invocations in saved prompts and project instructions, and start a fresh session. Do not only rename the old folder: the new `name` and default prompt must also be present. The core workflow is unchanged; the invocation name is a breaking change. A managed Skills service may keep its internal identity/path while updating the displayed name.

To uninstall a local installation, move its folder outside the host's skill discovery paths and refresh the client. This does not delete your task outputs. For managed clients, use their skill-management interface.

## Contribute and evaluate

Report the anonymized input, relevant context, mode, host/model if known, actual result, expected result and release version. Avoid personal data and credentials. For a new behavior, add a positive case and a case that should remain unchanged.

Use [cases.jsonl](../evals/cases.jsonl) with fresh conversations. Give the executor only the skill and the case's `prompt`, not its `checks` or recorded output. Review fidelity, invented facts, scope, execution boundaries, usefulness of checks and unnecessary length. Test file changes only in temporary fixtures. See [the evaluation record](../evals/RESULTS.md) for limitations and the reproducible coding case.

To claim improvement, compare the same held-out tasks with and without the skill using fixed model/settings and report failures, variation, latency and output length. Do not turn a small smoke test into a universal success-rate claim.
