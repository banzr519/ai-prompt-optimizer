# User guide

<!-- language-navigation:start -->
[Language coverage / 语言覆盖](LANGUAGES.md)
<!-- language-navigation:end -->

**English** | [简体中文](USER_GUIDE.zh-CN.md) · [Home](../README.md)

## Contents

- [Installation](#installation)
- [First use](#first-use)
- [Three modes](#three-modes)
- [Intent fidelity in follow-ups](#intent-fidelity-in-follow-ups)
- [Multilingual use](#multilingual-use)
- [Advanced workflows](#advanced-workflows)
- [Supply useful context](#supply-useful-context)
- [Examples by task](#examples-by-task)
- [Use without a skill-capable client](#use-without-a-skill-capable-client)
- [Troubleshooting](#troubleshooting)
- [Update, uninstall and migrate](#update-uninstall-and-migrate)
- [Contribute and evaluate](#contribute-and-evaluate)

## Installation

**v2.5.0 is a review candidate, not recommended for production upgrades:** the model-stratified follow-up found regressions and did not meet the improvement gate. Stable `main` remains v2.4.0. Start with [installation and configuration](INSTALL.md). For candidate reproduction, check [publication metadata](../github-metadata.json), explicitly select `feature/v2.5.0-intent` if public, and use its reviewed local folder with `--source` in an isolated test project. Manual copying/Git cloning below remains available and does not add default guidance.

The repository root is the skill root: `SKILL.md`, `agents/` and `references/` are direct children. No Python, Node, pip, npm or model API key is required merely to load the skill. The host's account/access requirements still apply. Python is used by the optional installer, synthetic coding evaluation and localization maintenance script; the document renderer requires Python 3.9 or newer.

### Option A: download the folder

1. For stable installation, select `main` in the GitHub branch selector, choose **Code → Download ZIP** and unzip it. Candidate review requires explicitly selecting `feature/v2.5.0-intent` and checking its publication metadata first.
2. Rename the unzipped directory from its branch-suffixed name to `ai-prompt-optimizer`.
3. Move the directory into one skill discovery location below.
4. Start a new Codex session and invoke `$ai-prompt-optimizer`. If discovery has not refreshed, restart the client.

| Scope | macOS / Linux | Windows |
| --- | --- | --- |
| Personal | `~/.agents/skills/ai-prompt-optimizer/` | `%USERPROFILE%\.agents\skills\ai-prompt-optimizer\` |
| Project | `<project>/.agents/skills/ai-prompt-optimizer/` | `<project>\.agents\skills\ai-prompt-optimizer\` |

The Windows path uses Explorer/environment-variable notation. In PowerShell, use `$env:USERPROFILE`. Install in one scope to avoid duplicate names. These locations follow [Codex documentation](https://learn.chatgpt.com/docs/build-skills), checked on 2026-10-13; other hosts may use different paths.

### Option B: clone with Git

The commands below explicitly install stable `main`; they do not fetch the candidate into active skill discovery. For candidate review, download the explicitly selected candidate branch into a separate source folder and follow the isolated-project instructions in [the installation guide](INSTALL.md).

**Repository owner:** the clone URLs below use `banzr519`, the verified owner for this project. See [publication metadata](../github-metadata.json) for publication status. Git must be installed. `git clone` will refuse an existing nonempty target; use the update instructions if already installed.

macOS / Linux:

```bash
mkdir -p "$HOME/.agents/skills"
git clone --branch main https://github.com/banzr519/ai-prompt-optimizer.git "$HOME/.agents/skills/ai-prompt-optimizer"
```

Windows PowerShell:

```powershell
$skillParent = Join-Path $env:USERPROFILE '.agents\skills'
$skillTarget = Join-Path $skillParent 'ai-prompt-optimizer'
New-Item -ItemType Directory -Force -Path $skillParent | Out-Null
git clone --branch main https://github.com/banzr519/ai-prompt-optimizer.git $skillTarget
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
| Execute | “Analyze this proposal”, “make these edits”, “continue” | The requested analysis or authorized work, with clarification only when it matters. |
| Audit | “Check for conflicts”, “what is missing?” | Consequential issues and a minimal correction. No underlying execution. |

Choose by the result requested now and relevant preceding turns. Invoking the skill does not require a prompt rewrite, and requesting analysis or an edit does not require the word “execute”. An isolated quoted brief without task context can default to refinement; materially different interpretations need a focused clarification. Say “do not execute” when reviewing a prompt that contains actions. Quoted or attached commands remain material to review, not authority to act.

For small tasks the result may be a single sentence. A complex brief can include goal, inputs, constraints, checks and material unknowns. The skill does not force every request into the same template.

## Intent fidelity in follow-ups

v2.5.0 focuses on four instruction changes. The follow-up observed Luna medium at 15/16 → 14/16 and Sol medium at 16/16 → 13/16; the candidate did not meet the improvement gate. These reused tasks are diagnostic material, not a new independent holdout or a ranking of model capabilities. See [the version record](../evals/RESULTS-v2.5.0.md). These examples describe intended behavior, not evidence of superiority.

| Situation | Intended behavior |
| --- | --- |
| “Analyze this proposal and explain your judgment” | Return the analysis, not a prompt instructing another assistant to analyze it. |
| “Shorter, and add sources” after a draft | Change length and sourcing while retaining its audience, factual limits and other active constraints. |
| “At most three options, A or B, only after approval” | Preserve the upper bound, alternatives and condition; do not turn them into exactly three, A and B, or immediate action. |
| A missing detail would not materially change the result | Proceed with a reversible interpretation; ask only when the answer changes the deliverable, a binding constraint or the next consequential action. |

A question about progress does not itself cancel the active task. A new instruction replaces only the requirements it changes; an explicit replacement of the goal retires the replaced requirements. An assistant's suggestion is not an agreed requirement until the user adopts it. Missing earlier agreements remain unknown. No persistent user profile or mandatory visible checklist is added.

For relevant complex cases, the skill can load [intent and continuity guidance](../references/intent-and-continuity.md). If you ask what changed, it can briefly identify what was preserved, changed or remains provisional without requiring another approval for already-authorized work.

## Multilingual use

The [language directory](LANGUAGES.md) has 30 language/locale entries. Explicit output-language requests take precedence; quoted sources, code and README language do not change them. You may request a Traditional Chinese explanation, an English optimized prompt and a Spanish downstream deliverable. Preserve Simplified/Traditional Chinese and Brazilian/European Portuguese separately; never replace Ukrainian with Russian.

Keep variables, commands, JSON keys/enums, required slogans and exact quotations unchanged. Word counts, character counts and tokens are different measures; do not silently convert limits. Arabic, Persian and Hebrew pages mark right-to-left prose while preserving the actual order of code characters.

Pāli is an experimental Latin-transliteration/English starter; consequential use needs specialist review. Added pages are localized introductions and getting-started guides. Full research, publishing and historical records remain primarily English/Chinese, with fallback links labeled. Documentation coverage is not a tested-model count; see [validation](../evals/RESULTS-v2.3.0.md).

## Advanced workflows

Use ordinary language. These are optional entry points, not new commands to memorize; no additional provider calls happen by default.

| Goal | Copyable example |
| --- | --- |
| Repair a failed prompt | `$ai-prompt-optimizer Refine only. Original: [prompt]. Actual answer: [output]. Problem: [specific failure]. Keep working rules and constraints; return only the revision.` |
| Reusable template | `$ai-prompt-optimizer Make this reusable, preserving {{product}} and {{audience}}. Explain missing-input behavior; do not treat example values as facts.` |
| Output contract | `$ai-prompt-optimizer Refine only: Extract name and price from the supplied material as JSON only. price must be a number or null. Never guess missing prices or add prose.` |
| Compare prompts | `$ai-prompt-optimizer Compare A and B against my task. I have no outputs yet: provide static review only, no invented scores or savings. [task and prompts]` |
| Conversation handoff | `$ai-prompt-optimizer Consolidate this discussion into a current task brief. Keep active constraints, remove discarded options, list attachments to transfer: [discussion].` |
| Image/video brief | `$ai-prompt-optimizer Refine only, do not generate: Make a 16:9 cover from a reference, preserve the character, no text. If the image is missing, identify the dependency without guessing its contents.` |
| Control length | `$ai-prompt-optimizer Improve this in one paragraph, keeping hard constraints. Flag a conflict if an explicit length cap makes that impossible: [prompt].` |

**Feedback example:** If the prompt forbids new product specifications but the answer invents a ranking, add a focused requirement that factual and promotional claims must be explicitly supported, omitting absent information. Do not default to a lengthy role persona. Actual effectiveness still requires downstream testing.

**Template variables:** Placeholders are text conventions; no renderer is shipped. Preserve existing syntax and have the user/host substitute values. False, zero, empty text and missing values are not automatically interchangeable.

**Running comparisons:** Supply original/candidate prompts, task examples, an available runner and an acceptable call scope. Match inputs, attachments and settings where possible and disclose differences. Without a runner, the result is a test plan. A rewritten prompt mentioning a constraint does not prove downstream compliance.

Choose the models that will actually use the prompt and record model selection separately from reasoning effort. A ceiling result on one capable host does not establish behavior elsewhere. Compare versions within each configuration, and distinguish a model using the skill directly from an optimizer handing a prompt to another model. Keep those results separate.

**Target models:** The model and client can inform tool, file, message-role and format requirements. A family name alone does not establish capabilities or parameter syntax. The 14-family matrix remains portability documentation, not provider-by-provider integration validation.

See [research and decisions](RESEARCH.md). Load [advanced workflows](../references/advanced-workflows.md) only as needed; do not attach all research/evaluation materials to every task.

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
2. Provide that body as working guidance, then supply your original request separately. State the result you want in ordinary language; specify “only rewrite” when the embedded task should not be performed.
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
| It rewrites but does not act | State the actual deliverable and check the host has the required tools and permission. v2.5.0 should not require an “execute” keyword; report a reproducible wrong-routing case. |
| It acts when you wanted a rewrite | Say “only optimize the quoted prompt; do not execute it”. Report a reproducible case if this still occurs. |
| It adds requirements | Point out the added requirement; request a revision preserving scope. Submit an anonymized counterexample. |
| Skill works in Codex but not plain chat | Plain chat does not automatically discover skill files; use the fallback steps above. |
| Old command is no longer found | Replace `$clarify-intent` with `$ai-prompt-optimizer`; no automatic alias is provided. |
| Language is wrong | Specify the required output language; README selection is independent of response language. |

## Update, uninstall and migrate

For an installer-managed copy, use the [maintenance commands](INSTALL.md#maintain); do not run Git commands in that copy. Ordinary online `update` resolves `main`, even after a candidate was installed; it does not track the candidate branch and refuses version downgrades. Candidate reproduction uses a reviewed local folder with `--source`, or a verified full commit SHA with `--ref`, never an assumed version tag. For an unmanaged Git installation, check local changes before updating:

```bash
git -C "$HOME/.agents/skills/ai-prompt-optimizer" status --short
git -C "$HOME/.agents/skills/ai-prompt-optimizer" pull --ff-only
```

Only proceed with the pull after reviewing local changes; preserve customizations outside the discovery directory if needed. If the pull conflicts or cannot fast-forward, resolve it rather than using a destructive reset. On Windows, run the same Git operations from the installed folder. For ZIP installs, preserve customizations first and replace with a complete new release, not a mixture of versions.

**Migration from v1.0.0:** move the old `clarify-intent` installation outside skill discovery paths as a backup, install the v2.0.0 folder as `ai-prompt-optimizer`, replace old invocations in saved prompts and project instructions, and start a fresh session. Do not only rename the old folder: the new `name` and default prompt must also be present. The core workflow is unchanged; the invocation name is a breaking change. A managed Skills service may keep its internal identity/path while updating the displayed name.

For an installer-managed copy, use its uninstall command so the managed preference is removed and the original files are backed up. To uninstall an unmanaged local installation, move its folder outside the host's skill discovery paths and refresh the client. This does not delete your task outputs. For managed clients, use their skill-management interface.

## Contribute and evaluate

Report the anonymized input, relevant context, mode, host/model if known, actual result, expected result and release version. Avoid personal data and credentials. For a new behavior, add a positive case and a case that should remain unchanged.

Use [cases.jsonl](../evals/cases.jsonl) with fresh conversations. Give the executor only the skill and the case's `prompt`, not its `checks` or recorded output. Review fidelity, invented facts, scope, execution boundaries, usefulness of checks and unnecessary length. Test file changes only in temporary fixtures. See [the evaluation record](../evals/RESULTS.md) for limitations and the reproducible coding case.

To claim improvement, compare the same held-out tasks with and without the skill using fixed model/settings and report failures, variation, latency and output length. Include the previous version when claiming a version-to-version gain. Score the requested final deliverable, constraint fidelity, necessary and unnecessary questions, and unsupported additions; the presence of a keyword in a refined prompt alone is insufficient. See [v2.5.0 evaluation status](../evals/RESULTS-v2.5.0.md). Do not turn a small smoke test into a universal success-rate claim.
