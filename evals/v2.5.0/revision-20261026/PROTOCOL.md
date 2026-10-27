# v2.5 revision r2: bounded semantic repair check

Registered 2026-10-27 (Asia/Shanghai) before collecting responses. The directory retains the 20261026 planning label. This is a new diagnostic run, separate from every earlier v2.5 experiment. The original failed candidate and its observations remain unchanged.

## Question and frozen runtime

Compare stable v2.4 (`93a193acb71636f3cbc929362c6ee1105f4a88ed`) with revision r2 of the v2.5 candidate. R2 changes four paragraphs: preservation of still-relevant details through edits; keeping unknown substance blank; complete questions without unsupported past-event assumptions; and separating present rewriting directions from the future executor's output contract. It does not change the UI entry, installer or model settings.

Runtime files were frozen and hashed before the implementation author inspected the new confirmation tasks. See `runtime-manifest.json`. Both snapshots contain SKILL.md, agents/openai.yaml and their runtime references. No runtime changes are allowed after viewing responses. Any further repair needs a separately frozen revision and separately reported run.

## Tasks and sampling

- Four exposed regression tasks, H01/H02/H14/H16, with their original task and rubric, selected because either model had a failure. Selection makes these diagnostic repairs, not representative benchmarks.
- Eight newly authored synthetic confirmation tasks, N01–N08, by an independent author with no access to runtime, previous tasks or outcomes. The author was given broad task categories and fidelity principles, not particular failures or desired answers. Two cases are simple direct-response controls. Task/rubric defects discovered before collection must be recorded, not silently edited after outcomes.
- Two requested configurations, `gpt-5.6-luna` / `medium` and `gpt-5.6-sol` / `medium`, continuing the user's explicit model selection. Accepted request parameters do not independently identify hidden backend builds or equalize computation.
- Two conditions × two models × two complete batch repetitions = eight fresh worker agents. Each worker receives all 12 cases, its assigned runtime, no scoring rubric, and no other outputs. Total: 96 case responses. These are **eight independent worker sessions, not 96 independent single-case sessions**. Cases share batch context, so carryover and JSON evidence formatting can affect behavior.
- Each batch uses its own predeclared shuffled case order (seed 20261026 and run ID). Paired conditions within a model/repetition share the same order. The second repetition changes the order. Both conditions use the same neutral wrapper and permitted reference access. Each case's conversation is role-labeled data, not native prior turns. Models return only a response for the current request; no network or external effects.
- Workers save a JSON array of case IDs and response strings. These stored strings are the evaluated artifacts, not claimed to be independently emitted native chat finals. Final receipts identify the file and SHA256. Retain empty/failed outputs, tool rejection and infrastructure problems. Never substitute a different model or retry an answer because it scored poorly. An unavailable requested model is a concrete gap.

## Review

Two fresh independent AI reviewers receive shuffled anonymous answers, original tasks/rubrics and this protocol's semantic evaluation rules. They must not read runtime, model/condition mapping, other reviews or previous outcomes. Verify explicit constraints with local calculations when needed. Exact variables and field names remain exact; equivalent natural phrasing is accepted. Do not transfer a future artifact's length/format limit to the present rewritten instruction. Only rubric-listed critical errors count as critical. Missing information can justify a concise question; do not demand invented facts.

Preserve both original judgments. Resolve disagreements against the frozen rubric while condition identities are hidden; unresolved cases remain unknown. Report all failures with their concrete requirement and response evidence. Style preferences are not failures. Historical H14 allows generic welcoming language without factual commitments; H01 requires the relevant time/location in the final message; H16 requires both a selected option and its calendar date without assuming pending replies arrived.

## Interpretation, separately for each model

Report each repetition and each task stratum separately. Count stable passes/failures, recoveries, regressions, critical cases and unknowns. Do not pool model denominators to claim a benefit.

The bounded repair check passes only if the revision passes all four selected regression tasks in both repetitions, introduces no critical errors, and has no paired regression or unknown on the eight new tasks in either repetition. If baseline and revision both pass a task, it establishes preserved observed behavior, not a gain. Meaningful improvement requires actual paired recoveries on new tasks; this small batch design cannot establish statistical significance or general reliability even if that occurs.

Passing this check is not authorization to replace stable main or the user's active v2.4 installation. It is not a claim about all 14 model families, 30 locales, independent provider APIs, implicit skill discovery, live sequential dialogue, token/cost savings, or a separate optimizer-to-executor handoff. Those require their own controlled checks. Installation and documentation engineering checks are reported independently.
