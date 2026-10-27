# Model-stratified intent fidelity results / 按模型分层的意图保真结果

Completed on 2026-10-20, Asia/Shanghai. **The unchanged v2.5.0 candidate fails the predeclared practical gate in both requested configurations.** Earlier inherited-host ceiling results remain intact; they did not establish behavior on these configurations.

本次按用户指定使用 Luna 与 Sol、均为 medium。候选版在两种配置中均出现回退，不能据此发布为“精准度明显提升”的稳定升级。模型名称是实际请求且被宿主接受的配置；精确后端构建不可见，也不据名称推定能力排名。

## Separate paired results

| Requested configuration | v2.4 baseline | v2.5 candidate | Recoveries | Regressions | Candidate critical cases | Unknown |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-5.6-luna / medium | 15/16 | 14/16 | 1 | 2 | 0 | 0 |
| gpt-5.6-sol / medium | 16/16 | 13/16 | 0 | 3 | 2 | 0 |

Luna: 13 stable passes, H01 recovered, H02/H16 regressed, no stable failures. Sol: 13 stable passes, H01/H14/H16 regressed, no recoveries or stable failures. Both baselines had zero critical cases. Do not pool these denominators or use one configuration's recovery to offset another's regressions.

| Category | Luna baseline → candidate | Luna recoveries / regressions | Sol baseline → candidate | Sol recoveries / regressions |
| --- | ---: | ---: | ---: | ---: |
| Current deliverable and elliptical references | 3/4 → 3/4 | 1 / 1 | 4/4 → 3/4 | 0 / 1 |
| Negation, conditions, exceptions and alternatives | 4/4 → 4/4 | 0 / 0 | 4/4 → 4/4 | 0 / 0 |
| Partial corrections and numeric dependencies | 4/4 → 4/4 | 0 / 0 | 4/4 → 4/4 | 0 / 0 |
| Facts, suggestions, acceptance and missing agreements | 4/4 → 3/4 | 0 / 1 | 4/4 → 2/4 | 0 / 2 |

The gate required ≥4 recoveries, zero regressions, zero candidate critical cases and no unknown outcomes within each configuration. Both fail because regressions occurred; Sol additionally has critical errors. Limited baseline headroom also prevents establishing four recoveries. This is a bounded observation, not proof that the candidate is universally worse.

## What failed

| Case | Observed defect | Configuration and condition |
| --- | --- | --- |
| H01 | A confirmation omitted the required event time and location. | Luna baseline; Sol candidate |
| H02 | The reusable prompt began by requesting a group recap, but ended by requesting only a task instruction. It mixed this turn's rewrite-only boundary into the downstream task. | Luna candidate |
| H14 | An onboarding skeleton asserted an unprovided first-week plan instead of leaving that content unknown. | Sol candidate; critical |
| H16 | Asked the user to select a time option but did not also request the missing calendar date. | Luna candidate |
| H16 | Asked which option was chosen “after the last two replies,” presupposing that outstanding replies had arrived. | Sol candidate; critical after blind reconciliation |

中文：问题集中在保留活动时间地点、区分本轮改写任务与下游提示词、补齐真正缺失的信息，以及避免把未知进展写成既成事实。可能的修订方向是收紧这些边界；本次没有证明任何具体规则是错误的因果来源，也未据答案修改被冻结的候选。

## Execution and review integrity

All 64 fresh execution agents completed: 16 cases ×2 versions ×2 configurations, one response per condition. Requested overrides were accepted; there were no infrastructure failures, missing finals, rejected configurations or reruns. Histories were role-labeled task packets, not native conversation turns. The [protocol](PROTOCOL.md) and [run manifest](RUN-MANIFEST.json) were registered before execution; the skill snapshots, wrapper, 16 tasks and rubrics remained unchanged.

Two fresh independent AI reviewers used inherited host settings and did not see model/version labels. Original verdict and critical-flag agreement was **63/64**. They separately reconsidered answer-049 while still blind and agreed on fail with a critical error; A revised pass, B retained fail. After this resolution, all 64 aggregate verdicts and critical flags agree. For answer-018 both agree on a noncritical failure but still differ on which additional preservation criterion fails. Original reviews and both reconciliation records are retained; this is not a claim of identical criterion-level scoring or professional human review. Both reviewers marked all responses proportionate, with no unnecessary clarification; that does not compensate for missing necessary clarification or failed deliverables.

The collection audit found 51 exact matches between saved body and actual final, 10 whitespace-only differences and 3 JSON-envelope finals. Those three envelope values exactly match the saved bodies; the actual finals, including envelopes, were graded unchanged and all three passed their task-specific rubrics. They were Luna baseline H05/H15 and candidate H08. Possible collection-harness interference is a limitation, not an established cause. No output was silently unwrapped, substituted or rerun.

## Evidence and reproduction

- Frozen [protocol](PROTOCOL.md), [manifest](RUN-MANIFEST.json), [wrapper](execution-wrapper.txt) and unchanged [original task/rubric files](../supplemental/README.md).
- [Execution receipts](execution-receipts.jsonl), [execution summary](execution-summary.json) and [saved-body/final audit](output-fidelity-audit.json).
- [Anonymous actual answers](blind-answers.jsonl), [review instructions](reviewer-instructions.md), original [review A](reviewer-a.jsonl) and [review B](reviewer-b.jsonl).
- Separate [reconciliation A](reconciliation-a.json), [reconciliation B](reconciliation-b.json), [resolution](review-resolution.json), [diagnostics](review-diagnostics.json) and post-review [answer mapping](answer-map.jsonl).
- Luna [paired judgments](gpt-5.6-luna/paired-results.jsonl) and [summary](gpt-5.6-luna/summary.json); Sol [paired judgments](gpt-5.6-sol/paired-results.jsonl) and [summary](gpt-5.6-sol/summary.json).
- [Summary index](summary.json) and [case categories](cases.jsonl); there is deliberately no pooled accuracy or combined gate.

From the repository root, aggregate the supplied judgments separately:

```sh
python3 -B scripts/summarize_intent_eval.py --cases evals/v2.5.0/model-strata/cases.jsonl --results evals/v2.5.0/model-strata/gpt-5.6-luna/paired-results.jsonl
python3 -B scripts/summarize_intent_eval.py --cases evals/v2.5.0/model-strata/cases.jsonl --results evals/v2.5.0/model-strata/gpt-5.6-sol/paired-results.jsonl
```

The script aggregates supplied semantic judgments; it does not independently grade answers or rerun models.

## Limits and acceptance decision

These are 16 reused synthetic tasks, one response per condition, not a new independent holdout. The test covers direct skill use, not a stronger optimizer handing prompts to a weaker executor, a no-skill control, native UI/discovery, live multi-turn interaction, all documented languages or separate provider APIs. Requested model and effort are recorded separately; `medium` does not establish equal compute. Exact backend build, sampling parameters, token usage, latency and cost are not exposed or measured here.

The candidate is retained for public review and reproduction, not accepted as a stable upgrade. Check [publication metadata](../../../github-metadata.json) for actual publication state. Stable main and the active user skill were not replaced. Any rule revision after inspecting these failures is a new candidate: keep this failed run, use these tasks only as development/regression material, and register a fresh independent holdout and replication before another improvement claim.
