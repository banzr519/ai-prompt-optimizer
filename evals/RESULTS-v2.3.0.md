# v2.3.0 language validation / 多语言验证

Date: 2026-10-14. [Language catalog](../docs/LANGUAGES.md) · [Previous behavior record](RESULTS-v2.2.0.md)

## Coverage delivered

30 language/locale entries: 2 existing primary full documentation sets; 27 additional localized introductions and getting-started guides; 1 experimental Pāli/English starter. Thus 28 locale entries were added, with 56 new localized Markdown pages. The catalog includes Chinese script variants and Portuguese regional variants; it is not a claim of 30 distinct natural languages or equal model proficiency.

Detailed research, publishing and historical evaluation materials remain English/Chinese where not translated. Fallback links identify those languages. The core SKILL.md remains one authoritative instruction set with explicit language-routing rules. This is not a website UI translation or an API language adapter.

## AI-assisted documentation review

Four independent reviewers inspected the following catalog groups and generated pages as needed:

| Group | Entries | Findings and applied corrections |
| --- | --- | --- |
| East/Southeast Asia | zh-Hant, ja, ko, vi, th, id, ms, fil | Corrected Indonesian wording so Simplified Chinese refers to the writing system rather than “simple Mandarin”. |
| Western/Southern Europe | de, es, fr, it, pt-BR, pt-PT, nl, sv, el | No material semantic defect reported; pt-BR/pt-PT remain distinct. |
| Eastern Europe/West Asia | ru, uk, pl, tr, ar, fa, he | Clarified Polish “client support” wording; added explicit left-to-right markup around RTL command-example blocks, matching the existing path wrappers. |
| South Asia/Africa/Pāli | hi, bn, sw, pi | Corrected Swahili agreement and variable terminology; clarified YAML frontmatter wording in Hindi/Bengali/Swahili; replaced uncertain Pāli technical headings with English. |

These were AI-assisted text/markup reviews, not professional native-speaker certification, not a complete linguistic audit and not a rendered GitHub browser inspection. The author checked and applied the specific corrections and regenerated affected pages. Revised translations were not submitted to a second professional or independent review. Pāli remains experimental and partly English by design.

## Five fresh behavior trials

Executors received only the installed skill path, relevant runtime references and a normal user request; they were not given checks, recorded outputs or locale documentation. They inherited the host model/settings and shared the filesystem. No separate provider API or model version was selected. The author reviewed their final responses.

| Case | Observed behavior |
| --- | --- |
| mixed-language-targets | Traditional Chinese explanation; English revised prompt instructing Spanish downstream output; exact two variables, slogan and 80-word constraint retained. No product description generated. |
| arabic-technical-identifiers | Arabic revision retained `{{source}}`, `price`, `null` and `ACME-01`; did not extract data or add JSON fields. |
| japanese-source-language | Japanese revision despite an English source prompt; retained price/name/button constraints and variable. No page created. |
| portuguese-locale-currency | European Portuguese wording retained the exact Brazilian-real price string and variable, with no conversion or task execution. |
| ukrainian-source-language | Ukrainian revision despite Russian source text; exact variable/name and three-item constraint retained. |

All five responses met their listed routing/constraint checks. This is a small behavior sample, not a success-rate estimate or proof of downstream output quality. In particular, the Spanish deliverable was not generated; it was only specified inside an English prompt. Outputs are in [observed-v2.3.0.jsonl](observed-v2.3.0.jsonl), inputs/checks in [cases-v2.3.0.jsonl](cases-v2.3.0.jsonl). Records preserve final responses, not full tool traces.

## Structural checks

Release preparation checks the skill structure, JSON/JSONL parsing, all 30 entry destinations, relative file links, required sections/commands, language-label uniqueness and source/generated-document consistency. `python3 scripts/build_localized_docs.py --check` verifies renderer consistency without writing. Code/identifiers contain no newly inserted bidi-control characters. Right-to-left code blocks have explicit LTR markup; visual rendering in GitHub remains untested.

Historical fixtures, license and earlier evaluation observations are preserved. No historical trial was rerun or relabeled as a new language test.

## Remaining limits / 尚未覆盖

- No professional native-speaker review of the new translations; no specialist Pāli review.
- No language-by-language provider API benchmark, automatic skill-selection benchmark or assurance of equal quality across the 30 entries.
- No end-to-end image/video execution, speech/pronunciation testing or complete GitHub visual QA.
- No measured token savings, success-rate gain or proof that translation improves task outcomes.

中文摘要：新增28套入口页面和入门指南，加上原有英／简中共30个语言及地区入口。完成4组AI文案审阅和5次独立上下文语言试用，发现的问题已修正；这不等同于母语专业审校或30种语言的跨模型测试。巴利语按实验双语入门处理。
