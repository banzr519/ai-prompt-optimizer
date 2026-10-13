# AI Prompt Optimizer

**English** | [简体中文](README.zh-CN.md)

**Turn vague requests into clear, actionable AI instructions—while preserving what you meant.**

AI Prompt Optimizer is a **prompt optimization and requirements clarification Agent Skill**. Use it to improve prompts, audit conflicting instructions, or clarify a task before an AI agent executes it. It covers coding, design, writing, analysis and planning.

AI 提示词优化助手：优化 Prompt、澄清需求、明确任务边界与验收标准，保留原意。

**v2.1.0 · MIT · Instruction-only · No API key required by the skill**

[Get started](#quick-start) · [User guide](docs/USER_GUIDE.md) · [中文使用指南](docs/USER_GUIDE.zh-CN.md) · [Evaluation record](evals/RESULTS.md) · [Publishing guide](docs/PUBLISHING.md)

## Before and after

**Your request**

> Make this product page feel more premium. Keep all text, prices and button behavior unchanged. It should look good on mobile too.

**A clarified instruction**

> Improve the existing product page's visual presentation while preserving all text, prices and button behavior, including labels and destinations. Provisionally interpret “premium” as clear hierarchy, consistent typography, balanced spacing and restrained styling aligned with the existing brand. Check mobile layouts for overflow, overlap, readability and usable controls. Compare the result against the original content and behavior. Do not add new modules or redesign the brand.

This is an illustrative translation, not a fixed template or performance claim.

## What it helps you do

| Your situation | What the skill adds |
| --- | --- |
| “Make it professional” | Context-specific structure, tone or visual criteria. |
| “Be comprehensive” | The relevant workflow, evidence and consequential exceptions. |
| “Make it faster” | A measurable baseline and comparable verification, without invented targets. |
| “Don't ask me lots of questions” | Reversible assumptions for small details; explicit handling of material unknowns. |
| “Just improve my prompt” | A copyable instruction without executing the embedded task. |
| “Clarify it and do it” | Minimal clarification followed by authorized execution. |

The skill preserves numbers, names, exclusions and scope. It separates known information from assumptions, detects conflicting requirements and keeps already-clear tasks short. It includes 34 semantic patterns, 10 domain guides and 8 teaching examples, loaded only when useful.

## Quick start

### 1. Install

Download this repository using GitHub's **Code → Download ZIP**, unzip it, and name the resulting skill folder `ai-prompt-optimizer`.

Place it in **one** of these Codex locations:

| Scope | Folder |
| --- | --- |
| Your local account | `~/.agents/skills/ai-prompt-optimizer/` |
| One project | `<project-root>/.agents/skills/ai-prompt-optimizer/` |

The folder must directly contain `SKILL.md`, `agents/`, and `references/`; avoid an extra nested folder. If it is already installed, follow the [update instructions](docs/USER_GUIDE.md#update-uninstall-and-migrate) instead of overwriting local changes. For Git-based installation and Windows paths, see the [user guide](docs/USER_GUIDE.md#installation).

### 2. Invoke

In Codex CLI or IDE, invoke the skill by name:

```text
$ai-prompt-optimizer Improve this prompt only: Make my report more professional without changing the facts.
```

If your client provides a skill picker, select **AI Prompt Optimizer**. If it does not appear, start a new session or restart the client. Automatic selection depends on the host and task; explicit invocation is the most predictable way to use it.

### 3. Choose the outcome in ordinary language

| Mode | Example |
| --- | --- |
| Refine only | `$ai-prompt-optimizer Rewrite this as a clear task instruction. Do not execute: …` |
| Clarify and execute | `$ai-prompt-optimizer Clarify and then carry out this task: …` |
| Audit | `$ai-prompt-optimizer Check this prompt for conflicts and missing essentials: …` |

No special command parser is required. If execution is not requested, the skill defaults to refinement.

## Compatibility

**Documented model families:** GPT, DeepSeek, Claude, Gemini, Qwen, Doubao, Hunyuan, ERNIE, GLM, Kimi, MiniMax, Grok, Mistral and Llama. The shared instruction workflow is designed for their suitable text/chat variants; individual model integrations have not been tested. See the [14-family usage matrix](docs/MODEL_COMPATIBILITY.md) for official references, usage paths and validation status.

| Environment | What is supported by this project |
| --- | --- |
| Codex skill-capable environments | Standard `SKILL.md` structure with optional UI metadata. Local discovery paths follow the official documentation linked in the user guide. |
| Other Agent Skills hosts | Portable Markdown instructions. Check that host's discovery paths, metadata support and available tools. Not separately integration-tested. |
| Listed model families through a suitable client or API | Reusable natural-language guidance. The client must provide context and any tools. Separate model API comparisons have not been run. |
| Plain chat without Skills | Paste the `SKILL.md` body as guidance, provide the original request separately, and attach only relevant reference material. See the [fallback workflow](docs/USER_GUIDE.md#use-without-a-skill-capable-client). |

This is a skill, not a hosted web app, model, browser extension or automatic model-settings switch. It cannot create missing tools, bypass permissions, guarantee correctness or eliminate every clarification round.

## Documentation

| English | 简体中文 |
| --- | --- |
| [Model compatibility and usage](docs/MODEL_COMPATIBILITY.md) | [大模型适用与使用方法](docs/MODEL_COMPATIBILITY.zh-CN.md) |
| [Detailed user guide](docs/USER_GUIDE.md) | [详细使用指南](docs/USER_GUIDE.zh-CN.md) |
| [GitHub publishing and discovery](docs/PUBLISHING.md) | [GitHub 发布与搜索配置](docs/PUBLISHING.zh-CN.md) |

The language links switch between maintained Markdown documents. They do not change GitHub's interface language or automatically translate content. Core skill instructions are maintained in one file to avoid behavior drift; output follows the user's language.

## Validation and limitations

Eight independent agent tasks were observed in v1.0.0, including a real repair of a synthetic Python function with four existing tests. The core workflow is unchanged through v2.1.0. v2.0.0 renamed the skill; v2.1.0 adds model-family portability documentation without new API integrations. See [validation details and limitations](evals/RESULTS.md). Sixteen evaluation cases are included; eight remain unrun. These are not cross-model benchmarks or proof of reduced cost or follow-up count.

## Upgrading from Clarify Intent

This project was previously named `clarify-intent` / 意图精炼器. **v2.0.0 changes the invocation to `$ai-prompt-optimizer`.** No automatic alias is installed for the old command. Update saved prompts and local folder names; keep only one active copy. See [migration instructions](docs/USER_GUIDE.md#update-uninstall-and-migrate).

## Contributing and license

Contribute a concrete input, expected behavior and a counterexample. Do not include private data or credentials. See the [contribution and evaluation workflow](docs/USER_GUIDE.md#contribute-and-evaluate).

[MIT License](LICENSE). The original copyright notice is retained. This project is independent and is not an official product of any listed model provider.
