# AI Prompt Optimizer · Pāli

[English](README.md) · [简体中文](README.zh-CN.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)

**v2.5.0 · MIT · pi**

**Atthaṃ rakkha. Vacanaṃ pākaṭaṃ karohi. / Preserve the meaning. Make the wording clear.**

Experimental Pāli–English starter using Latin transliteration. The skill refines a request while preserving facts and constraints. It executes the underlying task only when explicitly asked. Technical explanations remain in English to avoid presenting invented terminology as established Pāli.

**Install, update and verify / 安装、更新与验证:** [English](docs/INSTALL.md) · [简体中文](docs/INSTALL.zh-CN.md) · [Candidate evidence / 候选验证](evals/v2.5.0/revision-20261027/README.md)

## Patiṭṭhāpana / Installation

Download and extract the whole project. Name the folder ai-prompt-optimizer and place it in exactly one skill directory below. SKILL.md must be directly inside it. Start a fresh conversation.

```text
~/.agents/skills/ai-prompt-optimizer/
<project>/.agents/skills/ai-prompt-optimizer/
%USERPROFILE%\.agents\skills\ai-prompt-optimizer\
```

## Tayo nayā / Three modes

- Vacanaṃ sodhehi. / Refine the instruction only; do not execute the embedded task.
- Clarify and execute: perform authorized work only when explicitly requested.
- Vīmaṃsa. / Review important conflicts and gaps, then propose a minimal revision.

## Udāharaṇa / Example

```text
$ai-prompt-optimizer Vacanaṃ sodhehi; atthaṃ rakkha. Refine only; do not execute the task. Preserve {{source}} and all numbers. Use Pāli in Latin script; if a technical term is uncertain, mark it and retain an English gloss.
```

[Upayogavivaraṇa / Starter guide](docs/USER_GUIDE.pi.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)

## Sīmā / Limits

Experimental and AI-authored; not reviewed by a Pāli specialist. These short Pāli phrases and English explanations are a bilingual starter, not a full Pāli translation. Model proficiency is unverified. Request specialist review for consequential work; do not assume native-level accuracy.

[MIT](LICENSE)
