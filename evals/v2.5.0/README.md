# v2.5.0 evaluation evidence

The primary comparison used 24 core pairs, 4 separate UI-entry pairs and 9 historical response checks. Both versions passed all 24 core cases and all 4 UI cases. There were no paired recoveries or regressions and no observed critical errors. The predeclared practical improvement gate is **inconclusive because no core gain was observed**; a perfect baseline leaves no headroom on this set. This does not establish a general accuracy rate or a meaningful version improvement.

中文：首轮核心任务两版均为 24/24，默认入口两版均为 4/4，没有观察到恢复、退步或关键错误。由于旧版已全部通过，本组题不能满足预设的“至少四个核心任务恢复”门槛，**未能证明版本提升**。不得将该结论改写成普遍的 100% 准确率。

## Evidence map

- [Protocol](PROTOCOL.md), [frozen dataset manifest](FREEZE_MANIFEST.json) and [run manifest](RUN-MANIFEST.json): predeclared rules, hashes and actual scope.
- [Core inputs](inputs.jsonl), [core rubrics](rubrics.jsonl), [UI inputs](ui_inputs.jsonl) and [UI rubrics](ui_rubrics.jsonl): frozen independent synthetic tasks.
- [Anonymous review input](blind-answers.jsonl), [review instructions](reviewer-instructions.md), [reviewer A](reviewer-a.jsonl), [reviewer B](reviewer-b.jsonl) and [resolution](review-resolution.json): both original independent AI reviews. All 65 verdicts and critical-error flags agreed; no adjudication was required. These were host agents, not human expert reviewers.
- [Review diagnostics](review-diagnostics.json): verbosity and unnecessary clarification are reported separately. Both reviewers judged all primary responses proportionate, with no unnecessary clarification; these labels do not contribute to the improvement gate.
- [Answer mapping](answer-map.jsonl): condition identities revealed only after independent review and agreement checking.
- [Paired results](paired-results.jsonl), [case strata](cases.jsonl) and [summary](summary.json): normalized observations and deterministic aggregation. The script aggregates supplied judgments; it does not judge semantics.
- [Execution wrapper](execution-wrapper.txt), [receipts](execution-receipts.jsonl) and [queue summary](execution-summary.json): 64 fresh executors, one per queued response, no reruns or recovered writes. One earlier historical check used a separate fresh executor and is explicitly outside those queue receipts.
- [Historical cases](historical-cases.jsonl), [new observations](historical-results.jsonl) and [scope](regression-scope.json): eight complete passes and one partial verification. The literal translation response passed, but native implicit invocation remains unverified. Original historical records remain unchanged.
- [Isolated installation check](installation-check.json): local 2.4.0-to-2.5.0 upgrade, status and uninstall; user guidance preserved. This is not model-accuracy evidence or a change to the real user installation.
- [Engineering check record](engineering-checks.json) and [final public-file checks](final-checks.json): actual automated, format, localization, preservation and file-inventory checks, with counts and scope.

Reproduce the aggregation from the repository root, choosing a new output file if saving:

```bash
python3 -B scripts/summarize_intent_eval.py \
  --cases evals/v2.5.0/cases.jsonl \
  --results evals/v2.5.0/paired-results.jsonl
```

The tasks are synthetic, mostly Chinese with a small English subset. Each condition has one sample per task. The exact model build and sampling parameters were not exposed. Histories were replayed as role-labeled packet data; native discovery, live multi-turn interaction, external tool actions, all 30 documented locales and independent vendor APIs were not tested. No token, latency, cost or statistical-significance claim is made.

A separately frozen [longer-context supplement](supplemental/README.md) is complete: both versions passed 16/16, with no observed recovery or regression. It used the unchanged runtime snapshots and has its own inconclusive improvement gate. It does not replace or inflate the primary result.

The primary and first supplemental experiments inherited the current host configuration. They do not establish behavior on other model configurations. The completed [model-stratified follow-up](model-strata/README.md) found Luna/medium 15/16 →14/16 (1 recovery,2 regressions) and Sol/medium 16/16 →13/16 (0 recoveries,3 regressions,2 candidate critical cases). Both practical gates failed. Its requested model and reasoning settings are explicit, while the backend build remains undisclosed. The candidate is not accepted as a stable upgrade; these results stay separate from the earlier ceiling observations.
