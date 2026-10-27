# Independent longer-context supplement

**Result: 16/16 for both versions; no observed improvement or regression.** The predeclared four-recovery gate is inconclusive because the baseline had no failures. These results are separate from the [primary comparison](../README.md), with no pooled success rate. The runtime remained unchanged.

中文：补充集两版均为 16/16，没有观察到提升或退步。旧版没有失败案例，无法提供达到预设恢复门槛的证据。本组结果独立报告，不能替换首轮结果或拼成总体成功率。候选版继续保持未发布状态。

An independent designer authored 16 synthetic tasks without reading either skill, prior tasks, outputs or reviews. Fifteen cases contain 6–10 historical messages; twelve are Chinese and four English. The four categories cover current deliverables/references, logical scope, numeric corrections, and the distinction between facts, proposals and accepted decisions. Two new independent AI reviewers agreed on all 32 verdicts and critical-error flags before unblinding; no adjudication was needed. No critical errors, unknown judgments or unnecessary clarification were observed. These are bounded AI-reviewed observations, not human validation or statistical certification.

- [Inputs](inputs.jsonl), [rubrics](rubrics.jsonl), [counts](category_counts.json), [protocol](PROTOCOL.md) and [freeze manifest](FREEZE_MANIFEST.json): frozen before execution.
- [Run manifest](RUN-MANIFEST.json): identical runtime snapshots, original SHA-based ordering, review randomization and the pre-execution adaptation from native role injection to role-labeled packet histories. Real live multi-turn interaction remains untested.
- [Execution summary](execution-summary.json), [receipts](execution-receipts.jsonl) and [wrapper](execution-wrapper.txt): 32 new workers, maximum concurrency two, no failures, reruns or recovered writes. Private filesystem paths and worker identities are omitted from public receipt copies; original logs are retained locally.
- [Anonymous review input](blind-answers.jsonl), [review instructions](reviewer-instructions.md), original [review A](reviewer-a.jsonl), [review B](reviewer-b.jsonl) and [resolution](review-resolution.json): labels remained hidden until agreement was checked.
- [Output fidelity audit](output-fidelity-audit.json): one saved answer differs from its actual final only by two blank lines. Original representations were preserved; both blinded reviewers checked the actual final, with no verdict change. Normalized results use the actual final.
- [Answer mapping](answer-map.jsonl), [case strata](cases.jsonl), [normalized results](paired-results.jsonl), [summary](summary.json) and [diagnostics](review-diagnostics.json): no recovery, regression or critical failure was hidden by aggregation. Verbosity is reported separately and contributes nothing to the gate.

Reproduce aggregation from the repository root:

```bash
python3 -B scripts/summarize_intent_eval.py \
  --cases evals/v2.5.0/supplemental/cases.jsonl \
  --results evals/v2.5.0/supplemental/paired-results.jsonl
```

Execution took place on October 19, 2026; review completed on October 20, Asia/Shanghai. Exact model build and sampling controls were not exposed. The same host configuration was inherited, with one response per case/condition. This does not verify vendor APIs, all documented languages, native skill discovery, tool workflows, token savings, model latency or cost. The design's date context and frozen hashes are unchanged.
