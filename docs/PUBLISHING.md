# GitHub publishing and discoverability

**English** | [简体中文](PUBLISHING.zh-CN.md) · [Home](../README.md)

This guide prepares a standalone public repository. The files alone do not create a GitHub repository, publish a release, or configure About/Topics. The verified owner is `banzr519`; [publication metadata](../github-metadata.json) records the publication status and, after publication, the verified repository URL.

## Naming decision

| Item | Value |
| --- | --- |
| Repository | `ai-prompt-optimizer` |
| English title | AI Prompt Optimizer |
| Chinese title | AI 提示词优化助手 |
| Skill identifier | `ai-prompt-optimizer` |
| Invocation | `$ai-prompt-optimizer` |
| Suggested release tag (only if separately authorized) | `v2.5.0` |
| Previous name | `clarify-intent` / 意图精炼器 |

The name uses recognizable category words—AI, prompt, optimizer—while the subtitle explains requirements clarification and faithful task instructions. This is a naming judgment based on the task and observed public naming, not a keyword-volume study. Other owners may use similar repository names; do not claim uniqueness or affiliation. Repository availability still depends on the chosen owner's namespace.

## Ready-to-copy About description

```text
AI prompt optimizer & prompt engineering skill. AI 提示词优化、需求澄清。Portable guidance for GPT, DeepSeek, Claude, Gemini, Qwen, Kimi, GLM, Doubao, Hunyuan, ERNIE, MiniMax, Grok, Mistral & Llama; integrations depend on the host.
```

The wording describes model reuse rather than claiming independently tested native integrations.

## Topics

Copy the relevant topics into the repository's About settings:

```text
prompt-optimizer
prompt-engineering
prompt-optimization
ai-prompts
agent-skills
codex
ai-tools
llm
gpt
deepseek
requirements-engineering
claude
gemini
qwen
kimi
glm
llama
mistral
multilingual
i18n
```

Do not add unsupported clients or unrelated trending topics. GitHub currently permits up to 20 topics, with lowercase letters, numbers and hyphens and a 50-character limit per topic. These 20 follow those rules. See [GitHub's topic documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics).

[github-metadata.json](../github-metadata.json) stores the proposed name, description and topics for reuse. **GitHub does not automatically import that file.** Apply the settings in GitHub's UI or through your own authorized API workflow.

## Publish the standalone directory

For this v2.5.0 candidate, follow the [candidate checks](#v250-intent-fidelity-candidate-checks) below: update the existing repository through a review branch and draft pull request while keeping stable `main` unchanged. The general instructions below also cover a fresh standalone publication.

1. Obtain **only this skill's directory**. Place its contents at the new repository root so `SKILL.md`, `README.md`, `README.zh-CN.md` and `LICENSE` are direct children. A managed export may use an internal folder ID; use `ai-prompt-optimizer` for the public/local folder name. Keep the relative layout, references and existing icon. Do not copy the parent Skills workspace, its Git history, unrelated skills or account metadata.
2. Create a repository named `ai-prompt-optimizer` under your own account or organization. Choose public visibility only for the reviewed standalone contents. If initializing a fresh local repository, do not add a second conflicting README/license remotely.
3. Both user guides use the verified owner `banzr519`; update the owner if publishing a fork. If you choose a different repository slug, update clone URLs and naming instructions consistently; the skill identifier can remain `ai-prompt-optimizer`.
4. Upload the standalone files or push a clean standalone repository. Do not add the public GitHub remote to the private managed Skills workspace.
5. Set the About description and Topics above. Leave Website blank unless a real project site exists. Update `publication_status` in `github-metadata.json` only after the repository is actually public, and record its verified URL if useful.
6. Open the root README and click **简体中文 → English**. Repeat for both user guides and publishing guides. Test installation from the public source in a clean temporary environment and invoke the new skill name.
7. If separately authorized to publish a Release, use `v2.5.0` for the verified commit. Describe the Python requirement, actually tested platforms, plugin-preview status and on-demand configuration boundaries. Preserve the earlier 30-entry language coverage and historical trial limits; installation checks are not cross-model benchmarks.

The repository root is already an installable skill directory; no build process is needed. `evals/fixtures/label.py` intentionally retains a bug for regression evaluation—it is not runtime production code. Keep the original MIT copyright notice.

## Bilingual navigation

- `README.md`: English landing page, with a Chinese subtitle/summary and a link to `README.zh-CN.md`.
- `README.zh-CN.md`: full Chinese landing page, linking back to English.
- `docs/USER_GUIDE.md` ↔ `docs/USER_GUIDE.zh-CN.md`: paired detailed guides.
- `docs/PUBLISHING.md` ↔ `docs/PUBLISHING.zh-CN.md`: paired maintainer instructions.

Use relative links so forks and local previews still work. Keep scope, version, commands and compatibility claims aligned in both languages. This is document navigation, not an interactive language widget or automatic translation. Do not rely on GitHub to select a translation automatically. The runtime core remains one file; the agent follows the user's response language.

## What search can and cannot do

GitHub documents repository-name, description, topic and README search. Without an `in:` qualifier, its repository search covers name, description and topics; README search can be requested explicitly with `in:readme`. This is why relevant terms belong naturally in the name and About text, rather than only in a long guide. See [repository search syntax](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories).

After publication, use these diagnostic searches:

```text
ai-prompt-optimizer in:name
prompt-optimizer topic:agent-skills
提示词优化 in:description
prompt optimization in:readme
```

Discovery tests are not ranking guarantees; indexing may not be immediate and relevance varies. Do not infer exact keyword search volumes from a few returned repositories. Do not stuff repeated keywords into the skill's runtime instructions. Preserve concise, useful documentation and real examples.

## Release checks

- Confirm owner/clone URLs and both language links.
- Confirm the current invocation and migration notes are consistent.
- Preserve LICENSE, existing source attribution and evaluation limitations.
- Confirm all promised files are present and local reference links resolve.
- Distinguish “ready to publish” from “published”, and “designed for reuse” from “tested integration”.

Sources checked on 2026-10-13: [GitHub README documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), the search/topic documentation above and [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills).

## v2.3.0 multilingual release checks

Run `python3 scripts/build_localized_docs.py --check` and check all 30 entries and relative links. Distinguish primary full documents, localized starter guides and the experimental bilingual Pāli entry. Do not claim full translation of every document, professional native review or tested support in every model. Preserve technical identifiers.


## v2.4.0 installation distribution checks

For v2.4.0, run `python3 -B -m unittest discover -s tests -v`, the documentation check and `python3 scripts/build_distribution.py --output <new-directory-outside-repo>`. Verify both ZIPs and SHA256SUMS; keep native plugin integration labeled untested. Preserve historical evaluations and disclose Python requirements and platform coverage. Update this version’s publication_status only after verified publication; builds do not create tags or Releases.

## v2.5.0 intent-fidelity candidate checks

The model-stratified numbers below describe the original candidate; the 2026-10-27 R3 section at the end records the current revision.

Run the existing installation/distribution and localization checks as regression checks. Review actual-deliverable routing, clarification value, continuing-task constraints and semantic scope against the [v2.5.0 evaluation record](../evals/RESULTS-v2.5.0.md). Separate deterministic file checks from observed model behavior and from held-out version comparisons. Do not claim a clear precision gain without supporting comparative evidence, or extend a limited result to all tasks, languages or model families. The inherited-host case sets showed no version difference, but the model-stratified follow-up observed Luna medium at 15/16 → 14/16 (1 recovery, 2 regressions, no candidate critical errors) and Sol medium at 16/16 → 13/16 (0 recoveries, 3 regressions, 2 candidate critical errors). This did not meet the improvement gate. Keep stable `main` at v2.4.0 and the active installation unchanged; publish only the `feature/v2.5.0-intent` review branch and a draft pull request, not a production upgrade.

Keep `publication_status` as `prepared-not-published` until the candidate branch is actually public and verified; an existing repository URL is not evidence that the candidate is available there. After verification, record the actual repository URL, candidate branch/ref and review status; public candidate availability does not mean stable acceptance. Review remote changes before a normal push; do not force-push or overwrite unknown changes. No candidate build or documentation update automatically authorizes a tag or GitHub Release. Installation examples must distinguish stable `main` from an explicitly selected candidate: use a reviewed local `--source` or verified full-SHA `--ref`; ordinary online `update` follows `main` and never automatically tracks the candidate branch.

For a claim about a particular model, require a version comparison within that explicitly recorded model/effort configuration. Inherited host runs do not establish lower-capability model performance. Keep direct skill use and optimizer-to-executor handoff evaluations distinct, retain exposed datasets as diagnostic/regression material, and do not pool model groups to satisfy a gain gate. This follow-up reused 16 tasks per configuration, with 64 new responses and no reruns; it is not a fresh independent holdout or a model capability ranking. The original blinded reviewers agreed on verdict and critical-error flags for 63/64 responses; blind reconciliation resolved the remaining disagreement. See the [model-stratified follow-up protocol](../evals/v2.5.0/model-strata/PROTOCOL.md) and the [results](../evals/RESULTS-v2.5.0.md).


## 2026-10-27 repair revision

R3 follows the preserved failed original candidate and R2. See [the current evidence](../evals/v2.5.0/revision-20261027/README.md): Sol/medium meets the bounded repair gate, Luna/medium does not. Keep both strata and repetitions visible; no stable promotion is justified. Update the existing review branch and draft PR only after deterministic checks. Reset the current revision publication status to `prepared-not-published` before upload; mark it `published` only after verifying the public archive against the exact source commit. Retain prior publication identifiers separately. Neither candidate publication nor the installer smoke test establishes new-chat discovery or native plugin onboarding.
