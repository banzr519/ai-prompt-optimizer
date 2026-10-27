# AI Prompt Optimizer

<!-- language-navigation:start -->
[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md)

[Русский](README.ru.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md)

[Українська](README.uk.md) · [Polski](README.pl.md) · [Português (Brasil)](README.pt-BR.md) · [Pāli](README.pi.md) · [Bahasa Indonesia](README.id.md) · [Italiano](README.it.md)

[Ελληνικά](README.el.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [বাংলা](README.bn.md) · [فارسی](README.fa.md) · [עברית](README.he.md)

[Nederlands](README.nl.md) · [Svenska](README.sv.md) · [Português (Portugal)](README.pt-PT.md) · [Bahasa Melayu](README.ms.md) · [Filipino](README.fil.md) · [Kiswahili](README.sw.md)

[Language coverage / 语言覆盖](docs/LANGUAGES.md)
<!-- language-navigation:end -->

**Turn vague requests into clear, actionable AI instructions—while preserving what you meant.**

AI Prompt Optimizer is a **prompt optimization and requirements clarification Agent Skill**. Use it to improve prompts, audit conflicting instructions, or clarify a task before an AI agent executes it. It covers coding, design, writing, analysis and planning.

AI 提示词优化助手：优化 Prompt、澄清需求、明确任务边界与验收标准，保留原意。

**v2.5.0 candidate · MIT · Instruction-based skill + optional installer · No API key required by the skill**

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

## New in v2.5.0: intent fidelity

The candidate sharpens how the skill selects the actual deliverable: analysis, an edit or a continuation stays actual work; a rewritten prompt is returned when that is what you ask for. Clarification is limited to answers that change the result or a consequential action. Follow-ups preserve unaffected constraints, and semantic checks keep negation, alternatives, bounds, uncertainty and conditional permissions attached to their meaning.

**Review candidate; not recommended for production upgrades.** The 2026-10-27 R3 repair check still fails the Luna/medium gate; Sol/medium passes its bounded check.

| Requested configuration | Exposed 4: stable → R3, repetitions 1 / 2 | Fresh 8: stable → R3, repetitions 1 / 2 |
| --- | --- | --- |
| GPT-5.6 Luna, medium | 3/4 → 3/4; 3/4 → 2/4 | 7/8 → 8/8; 7/8 → 8/8 |
| GPT-5.6 Sol, medium | 3/4 → 4/4; 4/4 → 4/4 | 8/8 → 8/8; 8/8 → 8/8 |

R3 adds targeted rules for active-context preservation, unknown facts, present-versus-future output contracts and required placement. Luna still omits necessary final-date clarification in both repetitions, with one additional tone-requirement omission. The fresh cases show no paired regression, but do not cancel the exposed-case failures. The run contains 96 responses in 8 batch sessions, with two anonymous AI reviews agreeing on all 96 verdicts; it is not 96 independent sessions, a general improvement claim or a model ranking. See [R3 evidence and limitations](evals/v2.5.0/revision-20261027/README.md).

The original follow-up (Luna 15/16 → 14/16; Sol 16/16 → 13/16) and [R2 repair attempt](evals/v2.5.0/revision-20261026/README.md) remain unchanged. Earlier inherited-host ceiling results also remain in the [original v2.5.0 record](evals/RESULTS-v2.5.0.md); those results do not establish performance on other configurations.

Stable `main` remains v2.4.0. Current candidate publication is tracked in [metadata](github-metadata.json) and [draft PR #1](https://github.com/banzr519/ai-prompt-optimizer/pull/1); an existing repository URL does not prove that a local revision has been uploaded. Candidate publication does not mean acceptance as a stable upgrade.

## New in v2.3.0: languages

30 language/locale entries with clickable README and getting-started guides. Added language rules distinguish the explanation, optimized prompt and downstream output; preserve scripts, variables and exact constraints. Pāli has an experimental bilingual starter. Added translations are AI-authored and not professionally native-reviewed; documentation coverage is not a model-quality guarantee.

[Language directory and coverage](docs/LANGUAGES.md) · [Language validation](evals/RESULTS-v2.3.0.md)

## New in v2.2.0

Repair prompts from failed outputs; preserve reusable variables and output contracts; compare evidence without inventing scores; consolidate multi-turn context; refine image/video briefs. Simple requests remain short, and provider calls are not added by default. Use natural language—no new command syntax.

[Advanced usage](docs/USER_GUIDE.md#advanced-workflows) · [Research and decisions](docs/RESEARCH.md) · [New validation record](evals/RESULTS-v2.2.0.md)

## New in v2.4.0: installation and setup

Deterministic personal/project installation, optional on-demand guidance, status checks, safe updates and backed-up removal. Ask local Codex to install the supplied package. The installer requires Python 3.9+; everyday skill use does not. Native plugin packaging is an unverified preview.

[Recommended installation and maintenance](docs/INSTALL.md) · [Validation and platform limits](evals/RESULTS-v2.4.0.md)

## Quick start

### 1. Install or update

For ordinary use, give Codex the stable `main` package and send:

> Read docs/INSTALL.md, install AI Prompt Optimizer for my personal Codex and enable on-demand refinement. Use the included installer, preserve existing configuration and local edits, and report actual verification.

**Already installed?** Ask Codex to maintain that copy instead of copying another folder:

> Check my installed AI Prompt Optimizer and use its included maintenance program to update from stable main. Preserve my current on-demand setting, local edits and user rules. Stop and explain conflicts or a refused downgrade. Report the actual version, installation location and anything still unverified.

To review or reproduce this candidate, explicitly select `feature/v2.5.0-intent` only after checking its [publication status](github-metadata.json), then use the reviewed local folder with `--source` in an isolated test project. Default cloning, ZIP download from `main` and ordinary online `update` do not select or track the candidate. For requirements, source selection, old-version migration and install-only mode, see the [installation guide](docs/INSTALL.md).

<details>
<summary>Manual and Git installation</summary>

Download ZIP, extract and name the skill directory `ai-prompt-optimizer`, then place it in `~/.agents/skills/` or the project's `.agents/skills/`. It must directly contain `SKILL.md`, `agents/` and `references/`. Manual copying does not configure a default preference. See [Git/Windows instructions](docs/USER_GUIDE.md#installation) and [existing-installation migration](docs/INSTALL.md#existing-installations).

</details>

### 2. Invoke

In Codex CLI or IDE, invoke the skill by name:

```text
$ai-prompt-optimizer Improve this prompt only: Make my report more professional without changing the facts.
```

If your client provides a skill picker, select **AI Prompt Optimizer**. If it does not appear, start a new session or restart the client. Automatic selection depends on the host and task; explicit invocation is the most predictable way to use it.

Installation reporting should distinguish **file version/location, guidance state and new-chat invocation**. `session_verification: not-run` means the last item has not been checked, not that installation failed. See [how to verify success](docs/INSTALL.md#read-the-result).

### 3. Choose the outcome in ordinary language

| Mode | Example |
| --- | --- |
| Refine only | `$ai-prompt-optimizer Rewrite this as a clear task instruction. Do not execute: …` |
| Actual work | `$ai-prompt-optimizer Analyze this proposal and give your reasons: …` or `Make these edits: …` |
| Audit | `$ai-prompt-optimizer Check this prompt for conflicts and missing essentials: …` |

No special command parser or “execute” keyword is required. The requested result determines the mode; invoking the skill does not automatically turn an analysis or edit into a prompt rewrite. A quoted brief without task context can default to refinement. Explicit “only rewrite” still prevents embedded execution.

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

v2.5.0 remains a review candidate. [R3](evals/v2.5.0/revision-20261027/README.md) meets the bounded repair gate for Sol/medium but not Luna/medium; stable v2.4.0 remains the everyday version. No general accuracy, cost or cross-model improvement is claimed.

Eight independent agent tasks were observed in v1.0.0, including a real repair of a synthetic Python function with four existing tests. The core workflow is unchanged through v2.1.0. v2.0.0 renamed the skill; v2.1.0 adds model-family portability documentation without new API integrations. See [validation details and limitations](evals/RESULTS.md). The original record contains sixteen cases, eight then unrun. New v2.5.0 reruns are recorded separately in [the v2.5.0 evaluation](evals/RESULTS-v2.5.0.md); the native implicit-invocation check remains unverified. New v2.2.0 behavior cases and their actual observations are recorded separately in [the new evaluation record](evals/RESULTS-v2.2.0.md). These are not cross-model benchmarks or proof of reduced cost or follow-up count.

## Upgrading from Clarify Intent

This project was previously named `clarify-intent` / 意图精炼器. **v2.0.0 changes the invocation to `$ai-prompt-optimizer`.** No automatic alias is installed for the old command. Update saved prompts and local folder names; keep only one active copy. See [migration instructions](docs/USER_GUIDE.md#update-uninstall-and-migrate).

## Contributing and license

Contribute a concrete input, expected behavior and a counterexample. Do not include private data or credentials. See the [contribution and evaluation workflow](docs/USER_GUIDE.md#contribute-and-evaluate).

[MIT License](LICENSE). The original copyright notice is retained. This project is independent and is not an official product of any listed model provider.
