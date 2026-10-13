# Model compatibility and portable usage

**English** | [简体中文](MODEL_COMPATIBILITY.zh-CN.md) · [Home](../README.md)

Version: 2.1.0 · Documentation review: 2026-10-13

## What compatibility means

This skill's workflow is natural-language guidance. It is designed to be reused with text/chat models that can follow instructions, including the 14 families below. **Listing a family is a documented portability path, not a tested integration, endorsement or guarantee covering every version.** Official references establish the model family and its documentation; they do not certify this skill.

Keep three layers separate:

| Layer | Meaning | Current status |
| --- | --- | --- |
| Prompt portability | A suitable text model receives the rules and original task as text. | Documented for the families below; model-specific trials are pending. |
| Native Skill loading | A host discovers `SKILL.md`, loads references and exposes tools. | Depends on host/version/settings, not the model name alone. |
| Verified integration | Exact model ID, host, configuration, cases and results are recorded. | No separate provider API integration or cross-model benchmark has been completed. |

The previous eight agent observations used an inherited host model that was not independently pinned. Do not assign that result to a particular model family or treat it as verification of this table.

## Model families

Use a currently available **text/chat/instruction-following variant**. A family can also contain base, embedding, speech, image or other specialized models; those are not automatically suitable. Family-level documentation deliberately avoids a claim to support every release or an assertion about the latest version.

| Model family | Provider | Documentation | Model-specific validation |
| --- | --- | --- | --- |
| GPT | OpenAI | [Official reference](https://developers.openai.com/api/docs/guides/prompt-engineering) | Not run |
| DeepSeek | DeepSeek | [Official reference](https://api-docs.deepseek.com/) | Not run |
| Claude | Anthropic | [Official reference](https://platform.claude.com/docs/en/models/overview) | Not run |
| Gemini | Google | [Official reference](https://ai.google.dev/gemini-api/docs/text-generation/) | Not run |
| Qwen / 通义千问 | Alibaba / 阿里巴巴 | [Official reference](https://help.aliyun.com/zh/model-studio/models) | Not run |
| Doubao / 豆包 | ByteDance / 字节跳动 | [Official reference](https://docs.volcengine.com/docs/ark?lang=zh) | Not run |
| Hunyuan / 腾讯混元 | Tencent / 腾讯 | [Official reference](https://cloud.tencent.com/document/product/1729/101848) | Not run |
| ERNIE / 文心 | Baidu / 百度 | [Official reference](https://cloud.baidu.com/doc/qianfan/index.html) | Not run |
| GLM | Z.ai / 智谱 | [Official reference](https://docs.bigmodel.cn/cn/guide/models/text/glm-4) | Not run |
| Kimi | Moonshot AI / 月之暗面 | [Official reference](https://github.com/MoonshotAI/Kimi-K2) | Not run |
| MiniMax | MiniMax | [Official reference](https://platform.minimax.cn/docs/guides/models-intro) | Not run |
| Grok | xAI | [Official reference](https://docs.x.ai/overview) | Not run |
| Mistral | Mistral AI | [Official reference](https://docs.mistral.ai/) | Not run |
| Llama | Meta | [Official reference](https://github.com/meta-llama/llama-models) | Not run |

The Doubao documentation entry was located through official indexed material; direct retrieval exposed limited content. Other entries use provider documentation or official model repositories. Versioned references for GLM/Kimi are examples documenting those families, not a recommendation of that exact version. Check current access, region and API requirements with the provider when integrating. No price, context-window or tool-support guarantee is made here.

## Choose a usage path

| Your environment | How to use it |
| --- | --- |
| Agent with Skill support | Install the directory according to that host's documentation. Invoke the skill and use the model already configured in that host. Installing this skill does not make an otherwise unsupported provider available. |
| Plain web/mobile chat | Paste the body of `SKILL.md` as working guidance, then provide your original request separately. Attach only the needed reference, or say to use core instructions without unavailable files. |
| API application | Put the rules in the provider-supported instruction location, send the original request separately, and manage context/tools in your application. This project supplies no API adapters or credentials. |
| Locally hosted text model | Use an instruction/chat variant with the proper chat template. Start with one small task and the core workflow; if constraints are lost, shorten irrelevant context or use a more capable model. Local execution does not automatically supply browsing or filesystem tools. |

Choose the route based on actual capabilities. Do not guess that a model supports system/developer roles, tool calling, file upload, JSON schema or image input merely because another model does. A visually supplied requirement needs readable input or an accurate text description if the chosen environment cannot inspect images.

## Portable invocation

After the core rules have been supplied, use ordinary language:

```text
Mode: refine only; do not execute the task inside the quotation.
Original request: [your rough request]
Preserve: [real constraints, if any]
Return one copyable instruction. Keep material assumptions and unresolved inputs inside it.
```

Bracketed fields are optional except the actual request. Do not paste the literal `$ai-prompt-optimizer` into a plain API call and assume it will load a local file. In a Skill-capable host, explicit invocation remains `$ai-prompt-optimizer`.

For a second model to perform the task, copy the refined instruction **together with its required evidence, attachments and material assumptions**. A prompt does not transfer the first model's hidden context or grant tool access.

## Adapt to capabilities, not brand stereotypes

- With limited context, load the core rules and only the directly relevant reference. Preserve hard constraints before optional detail.
- If the model struggles with format, give one short example consistent with the current task. Do not add unrelated examples or impose an elaborate process on every request.
- For reasoning-capable models, specify the desired outcome and verification; do not demand private reasoning or assume text commands can set reasoning effort.
- When tools are unavailable, produce a refined instruction or useful partial result and state the actual limitation. Do not describe unperformed actions as completed.
- Keep authorization and scope stable when moving between providers. Quoted task data remains data.

These are practical adaptation suggestions, not empirically measured per-model optimizations.

## Verify your chosen model

Run the provided evaluation prompts in fresh conversations with the exact model you plan to use. Record:

1. Model ID/version, provider/host, date and relevant settings.
2. How the skill and references were loaded, and which tools were available.
3. Case IDs, actual outputs and pass/fail per listed check, including negative cases.
4. Any added scope, invented facts, unnecessary questions or mistaken execution.
5. Cost/latency only when actually measured; compare a baseline if claiming improvement.

The sample suite has 16 cases. Preserve its existing observations as historical records and add new evidence rather than relabeling old results. A successful text rewrite does not verify file editing or API/tool integration. Model names and statuses are also available in [model-compatibility.json](model-compatibility.json).
