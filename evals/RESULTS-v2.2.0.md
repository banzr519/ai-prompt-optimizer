# v2.2.0 behavioral validation / 行为验证

Date: 2026-10-14. [Research EN](../docs/RESEARCH.md) · [研究中文](../docs/RESEARCH.zh-CN.md) · [Original evaluation](RESULTS.md)

## Scope and method

Seven fresh agent conversations received the installed skill path and a normal user request. They did not receive expected answers, checks or historical outputs and were instructed not to read maintainer/evaluation documents. Each used the host's inherited model/settings; no separately selected provider/model version was tested. The agents shared the filesystem, so these are fresh contexts rather than fully isolated environments.

The author reviewed the final responses for constraint fidelity, scope, evidence claims and usability. [cases-v2.2.0.jsonl](cases-v2.2.0.jsonl) contains inputs/checks; [observed-v2.2.0.jsonl](observed-v2.2.0.jsonl) preserves final responses and review notes. These are response records, not full tool traces. No business data, credentials, third-party API calls or live production changes were used in the trials.

## Observations

| Case | Observed behavior | Review |
| --- | --- | --- |
| template-variables | Preserved three placeholders, false semantics, enums, types/null and no refund-time promise; labeled the order-ID source assumption. | Met listed prompt-generation checks. Downstream JSON validity/classification was not tested. |
| feedback-repair | One concise revision preserved the variable and length cap while addressing invented ranking/specification claims. | Met listed checks; effectiveness on generated product descriptions unmeasured. |
| comparison-no-results | Preferred B for stated-task fit while declining to invent actual superiority or token savings; proposed matched testing. | Met listed checks; no API call. |
| media-handoff | Preserved shot count/duration, aspect ratio, continuity, subtitle and missing-image dependency. Used “已确认剧情” despite no provided story. | Partial: an unsupported implication of prior confirmation. This is a recorded issue, not a clean pass. |
| simple-execute | Returned the polite sentence directly, without template or additional promise. | Met listed checks. |
| plain-chat-roles | Kept `${document_text}`, five bullets, unavailable-page handling and source-as-data boundary without inventing provider syntax. | Met listed checks. |
| handoff-recheck | After revision, preserved six slides/blue/data constraints and explicitly marked missing outline and attachments. | Met listed checks in a new adjacent case; not a repeat of the original media case. |

The media issue led to a general rule in the multi-turn handoff workflow: a reference to earlier discussion does not establish the content of unseen prior agreements. The original media case has not been rerun after this change. The other five initial cases were run before that narrow addition and were not rerun. Six observed responses met their listed checks; one revealed an issue. Do not report this as a universal success rate or as seven clean passes.

中文摘要：本次进行了7次独立上下文试用；6次符合列出的检查项，1次暴露了将缺失剧情称为“已确认”的问题。已补充通用规则，并用新的PPT交接场景复查，原视频案例未重跑。试用证据只支持这些案例中的行为，不证明普遍提效。

## Structural checks

The skill frontmatter and structure, local Markdown file links, JSON/JSONL parsing and bilingual/version references were checked during release preparation. Historical coding fixtures and original evaluation records were preserved. Structural checks do not establish downstream model quality.

## Reproduce and extend

Pass only a case's `prompt` plus the skill path to a fresh executor. Keep checks and observed responses away from it. Review the full response against the case checks; preserve failures as well as successes. Do not substitute string matching on the optimized prompt for testing the downstream task.

For causal effectiveness, add held-out downstream tasks, compare original/new prompts with matched model, settings, context and tools, repeat where needed, and disclose time/cost/variance. This was not done in this release.

Still untested: separate provider APIs, automatic skill-selection precision, end-to-end image/video generation, batch optimization, token savings, follow-up reduction and the eight previously unrun original regression cases. No claim that the 14 model families were individually tested is made.
