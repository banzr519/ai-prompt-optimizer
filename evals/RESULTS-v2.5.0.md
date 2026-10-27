# v2.5.0 intent fidelity evaluation / 意图保真验证

Evaluation dates: 2026-10-19–20, Asia/Shanghai. Status: candidate not accepted for stable upgrade; actual publication state is recorded in [metadata](../github-metadata.json).

**Current conclusion: the candidate does not meet the upgrade gate.** Original inherited-host comparisons were saturated, but the subsequent explicitly configured follow-up found regressions: Luna/medium went from 15/16 to 14/16, and Sol/medium from 16/16 to 13/16. Sol's candidate also had two critical cases. Meaningful improvement has not been demonstrated; the candidate is retained for review, not promoted to stable main. Each experiment and model is reported separately.

**当前结论：v2.5 候选版未达到升级标准。** 原宿主配置两组满分只说明这些题在该配置下没有区分度。按用户指定补测后，Luna/medium 从 15/16 降至 14/16（恢复1题、回退2题），Sol/medium 从 16/16 降至 13/16（恢复0题、回退3题，其中2题触发严重项）。保留全部失败记录，本版仅供候选审阅，不合入稳定 main，不替换实际启用的技能，也不宣称已提升精准度。

**Model coverage correction / 模型覆盖修正：** The primary and first supplemental experiments used fresh agents that inherited the host configuration, without an explicit model/effort override. The user reports selecting the host's strongest mode; exact backend build and sampling settings were not independently exposed. Those saturated results alone cannot establish behavior on other configurations. 两组满分不能用来判断其他模型是否受益；此次补测填补了两种明确请求配置的观察记录，未验证所有较弱模型，也未独立核实原宿主的精确后端身份。

A separately registered [model-stratified follow-up](v2.5.0/model-strata/README.md) is complete for `gpt-5.6-luna` / `medium` and `gpt-5.6-sol` / `medium`, as explicitly selected by the user. Both requested overrides were accepted. It reuses the unchanged 16-case supplement and frozen skill snapshots, with each model reported separately. This is not a new independent holdout, a model-capability ranking, a reasoning-effort experiment or a strong-optimizer-to-weak-executor handoff evaluation.

## Implementation and comparison

The baseline is v2.4.0 commit `93a193acb71636f3cbc929362c6ee1105f4a88ed`. The v2.5.0 candidate changes current-deliverable routing, consequential clarification, preservation of unaffected constraints across revisions, clause semantics and the UI entry prompt. These are implementation descriptions, not established performance gains. It adds no permanent user profile or mandatory visible intake form.

The candidate runtime was frozen before the implementation author inspected the independent primary task set. It remains byte-identical throughout the primary, supplemental and model-stratified comparisons. Snapshot hashes, actual execution limitations and condition identities are in the [run manifest](v2.5.0/RUN-MANIFEST.json).

## Primary paired results

| Stratum / category | v2.4.0 | v2.5.0 candidate | Recoveries | Regressions |
| --- | ---: | ---: | ---: | ---: |
| Clear requests | 6/6 | 6/6 | 0 | 0 |
| Reversible ambiguity | 6/6 | 6/6 | 0 | 0 |
| Consequential missing/conflicting input | 6/6 | 6/6 | 0 | 0 |
| Multi-turn revisions | 6/6 | 6/6 | 0 | 0 |
| **Core total** | **24/24** | **24/24** | **0** | **0** |
| Separate UI-entry probe | 4/4 | 4/4 | 0 | 0 |

Core paired outcomes: 24 stable passes, 0 stable failures, 0 recoveries, 0 regressions. UI paired outcomes: 4 stable passes and no other outcomes. Both versions had zero observed critical errors and no unknown paired judgments. The predeclared gate required at least four core recoveries, no regressions, no candidate critical cases and complete judgments. It is **inconclusive for practical improvement because no core gain was observed and baseline failures were below four**. UI fidelity was preserved on the four probes, with no measured improvement.

Two fresh independent AI reviewers assessed all 65 anonymous responses, including historical checks, without source skills or condition mappings. All 65 verdicts and critical-error flags agreed before unblinding. No adjudication was required. Both judged all responses proportionate, with no unnecessary clarification. These are AI judgments, not human expert or native-speaker review.

See the [evidence index](v2.5.0/README.md), [frozen protocol](v2.5.0/PROTOCOL.md), [aggregate results](v2.5.0/summary.json), original [review A](v2.5.0/reviewer-a.jsonl) and [review B](v2.5.0/reviewer-b.jsonl). The reporting script only aggregates supplied judgments; it does not automatically validate semantics.

## Separate longer-context supplement

After the primary ceiling result, an independent designer who did not read either implementation or prior tasks, answers or reviews authored 16 new cases. Fifteen have 6–10 historical messages; twelve are Chinese and four English. The same original frozen runtime snapshots were used. No instruction, task or scoring changes were made in response to observed answers. This is a separate follow-up, not an extension of the primary denominator.

| Supplemental category | v2.4.0 | v2.5.0 candidate | Recoveries | Regressions |
| --- | ---: | ---: | ---: | ---: |
| Current deliverable and elliptical references | 4/4 | 4/4 | 0 | 0 |
| Negation, conditions, exceptions and alternatives | 4/4 | 4/4 | 0 | 0 |
| Partial corrections and numeric dependencies | 4/4 | 4/4 | 0 | 0 |
| Facts, suggestions, acceptance and missing agreements | 4/4 | 4/4 | 0 | 0 |
| **Supplemental total** | **16/16** | **16/16** | **0** | **0** |

The supplemental paired outcomes were 16 stable passes, with no stable failures, recoveries, regressions, critical errors or unknown judgments. Its own predeclared four-recovery gate is also inconclusive for improvement because the baseline has no failures. Two new independent AI reviewers agreed on all 32 verdicts and critical-error flags before unblinding. Both judged all responses proportionate, with no unnecessary clarification.

The protocol originally described native sequential role injection. Before any supplemental response, the [run manifest](v2.5.0/supplemental/RUN-MANIFEST.json) recorded the actual shared host adaptation: unchanged role-labeled JSON histories instead. Live multi-turn behavior therefore remains unverified. There were zero infrastructure failures, reruns or recovery writes. Of 32 saved responses, 31 exactly matched the worker final text; one differed only by two blank lines. Both representations were retained and both blinded reviewers checked the actual final before completing their judgments; the verdict was unchanged. See the [fidelity audit](v2.5.0/supplemental/output-fidelity-audit.json).

See [supplemental evidence](v2.5.0/supplemental/README.md), [frozen protocol](v2.5.0/supplemental/PROTOCOL.md) and [summary](v2.5.0/supplemental/summary.json).

## Explicit model-stratified follow-up

| Requested configuration | v2.4.0 | v2.5.0 candidate | Recoveries | Regressions | Candidate critical cases |
| --- | ---: | ---: | ---: | ---: | ---: |
| gpt-5.6-luna / medium | 15/16 | 14/16 | 1 | 2 | 0 |
| gpt-5.6-sol / medium | 16/16 | 13/16 | 0 | 3 | 2 |

Both practical gates failed. Luna recovered H01 but regressed on H02 and H16; Sol regressed on H01, H14 and H16. Both have 13 stable passes, no stable failures and no unknown outcomes. Baselines had no critical cases. No pooled success rate or combined recovery gate is used.

The 64 fresh execution agents completed with no failed configurations, infrastructure failures, missing finals or reruns. Two independent AI reviewers, blind to model and version, initially agreed on 63/64 overall verdicts and critical flags. Both independently reconsidered the same anonymous disagreement against the frozen rubric and agreed on fail for Sol candidate H16; original judgments are preserved. A remaining criterion-attribution difference on Luna candidate H02 does not change its agreed noncritical failure. See [resolution and both reconciliations](v2.5.0/model-strata/review-resolution.json).

Observed failures include omitted time/location, confusion between the current rewrite-only task and the downstream output contract, a missing calendar-date clarification, and unsupported assumptions about plans or completed replies. These are failure observations, not proof that a specific added instruction caused each error. The candidate was not retuned after seeing them.

The collection audit retained 51 exact saved-body/final matches, 10 whitespace-only differences and 3 JSON-envelope finals. The three envelope values matched the saved bodies; actual final text was graded unchanged and all three passed their task-specific rubrics. Possible collection-harness interference remains a limitation, with no established cause. [Full evidence, per-category results and limitations](v2.5.0/model-strata/README.md).

## Candidate decision

The implementation and engineering checks are complete, but the requested meaningful precision improvement has **not** been established and the follow-up observed regressions. The delivery channel is a candidate branch for review and reproduction; consult [metadata](../github-metadata.json) for whether the public push has actually completed. Stable main and the active installed skill are not upgraded, and no tag or GitHub Release is created. These finite observations do not establish universal inferiority or equivalence. A revision informed by these failures must be a separately frozen candidate, retain this failed run, and use a fresh independent confirmation set with preregistered replication before claiming improvement.

The SKILL.md entrypoint increased from 13,532 to 15,684 characters (13,853 to 15,973 UTF-8 bytes). These are file-size counts, not tokens or measured cost. No efficiency gain is claimed.

## Historical response checks

The eight previously unrun cases and the v2.2 media-handoff issue were rerun into new records. Eight cases passed their applicable checks. The literal translation response passed, but the original no-implicit-trigger requirement is **unverified** because the harness explicitly loaded the skill. Its full verdict is unknown, so this is not a claim of nine fully verified historical passes. See [observations](v2.5.0/historical-results.jsonl) and [scope](v2.5.0/regression-scope.json).

Original historical evaluation files, the deliberately buggy fixtures and MIT LICENSE remain byte-identical to the baseline. Installation checks and historical language trials are not new intent-accuracy evidence.

## Engineering validation

- 41 automated tests passed: installation/distribution behavior and six aggregation tests.
- `python3 -B scripts/build_localized_docs.py --check`: 30 locales, 0 changed. These are 2 full primary document sets, 27 localized introductions/starters and 1 experimental bilingual Pāli starter, not 30 fully translated research/documentation sets.
- Skill structure validation passed; Python sources parsed against Python 3.9 grammar.
- Local 2.4.0 → 2.5.0 installation, status and uninstall passed in an isolated macOS/Python environment, preserving existing guidance. [Installation evidence](v2.5.0/installation-check.json). This did not change the real user installation.
- [Engineering check record](v2.5.0/engineering-checks.json) preserves the actual checks and their limits; structural correctness does not establish semantic improvement.

## Scope and limitations

The tasks are synthetic and mostly Chinese, with a small English subset. Each condition has one sample per case. The primary and first supplement inherited host configuration; the later follow-up explicitly requested Luna/medium and Sol/medium. Exact backend builds and sampling parameters were not exposed. The follow-up reused exposed tasks rather than a fresh holdout. No separate vendor API calls, exact token usage or controlled model-latency measurements were collected.

Histories were supplied as role-labeled packet data, not real earlier model turns or native message-role injection. This cannot establish full live multi-turn behavior or native implicit skill discovery. It also does not validate long-document retrieval, tool execution, external publication actions, all 30 documented locales or all named model families. Shared AI-review biases and sampling variability remain possible. No statistical-significance, token-saving, cost-reduction or universal precision claim is made.
