# Model-stratified follow-up / 按模型分层的补测

Registered on 2026-10-20 before any response in this batch. This is a follow-up to a user-identified coverage gap, not a replacement for the earlier saturated experiments.

## Question and scope

Does the unchanged v2.5 candidate recover intent-fidelity failures relative to v2.4 within either of two explicitly requested configurations: `gpt-5.6-luna` with `medium`, and `gpt-5.6-sol` with `medium`?

The earlier runs used inherited host settings without a model override. They are descriptive regression evidence in that host configuration, not evidence about lower-capability models. The user's report that their host was set to its strongest mode is not independent verification of the backend model build. The two new model names are identifiers offered by the current subagent interface; this protocol does not assert a measured capability ranking or treat `medium` as equal compute across models.

This batch evaluates a model directly using the assigned skill to respond to a task. It does **not** evaluate a stronger optimizer producing a prompt for a separate weaker execution model. There is no no-skill control, so it cannot establish the absolute benefit of using a skill versus not using one.

## Frozen material and sampling

- Reuse all 16 tasks and rubrics from [the longer-context supplement](../supplemental/PROTOCOL.md), without selection or modification. Runtime snapshots and hashes are identical to that completed supplement.
- This is exposed, reused material, not a new independent holdout. No runtime tuning occurred after either previous experiment. It supports a same-task comparison across the requested configurations; it cannot be advertised as newly independent confirmation.
- Each model has 16 cases × 2 versions × 1 response = 32 responses; total 64. Each response uses a fresh `fork_turns=none` agent with explicitly selected model and `medium` reasoning effort. No session is reused across cases or conditions.
- Keep the original neutral execution wrapper unchanged. Histories are role-labeled task data rather than native chat turns, as in the prior runs. Executors may read only their assigned input, assigned skill and relevant linked runtime references. They receive no rubric, other answer, version mapping, prior result or review feedback.
- Freeze the complete run order before execution, using the seed in `RUN-MANIFEST.json`. Sort cases by SHA256(seed + `|case|` + case ID). Reverse model order on odd final hex digits of SHA256(seed + `|model|` + ID); reverse version order similarly with `|condition|MODEL|ID`. Preserve that start order even with concurrent jobs.
- Record requested configuration, successful spawn/finish receipts, exact saved response and its final-message fidelity audit. A requested model accepted by the host is not proof of an undisclosed backend build. Do not infer model identity from an agent's self-description.
- Preserve infrastructure failures and missing responses; do not replace them or rerun low-quality answers. Stop and report if a requested configuration is rejected. Never silently fall back to the inherited host.

## Review and interpretation

Use two fresh independent AI reviewers with inherited host settings. Hide both model and version labels, randomize the 64 output IDs with seed 20261023, and score each answer against its original supplemental rubric and counting rules. Preserve original judgments; resolve disagreements while labels remain hidden. Stronger judges do not substitute for weaker execution models, and AI judgments are not professional human review.

Apply the supplemental practical gate **separately to each model**: at least 4 recoveries, zero regressions, zero candidate critical errors, zero unknown/missing outcomes. Never sum recoveries across models to pass a gate or pool their denominators. Report stable pass/fail, recoveries, regressions, critical errors and all four categories for each configuration. Insufficient baseline failures imply insufficient headroom, not proof of no effect.

One response per condition is a bounded diagnostic experiment. Even a passed practical gate supports only a result on this selected set and configuration, not statistical significance, a stable improvement rate, general superiority or support for other model families. Any broader reliability claim requires a separately preregistered replication with repeated samples and an independently authored holdout. Do not selectively repeat only favorable cases.

Model choice and reasoning effort are separate factors. Comparing the earlier inherited host with these two configurations changes multiple factors, so differences across those groups cannot isolate a reasoning-effort effect. This batch makes no latency, cost, token-efficiency, native implicit invocation, multilingual or vendor-API claims.

## 中文说明

用户指出原宿主配置可能掩盖弱模型错误，因此本次固定技能与16道原题，分别在 Luna/medium、Sol/medium 中比较两版本，共64次独立响应。记录实际请求配置及工具接收情况，不把不可见的后端版本写成已核实事实。

原题已公开给维护者，不再称为新盲测集；执行器仍看不到评分规则或其他答案，评审同时看不到模型与版本。旧结果保留且不合并。每个模型分别判断恢复、回归和严重错误；不能把两个模型的提升相加，也不能把一次小样本结果称为统计显著或保证。模型差异和推理档位差异必须分别研究。
