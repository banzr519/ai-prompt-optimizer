# R2 semantic repair observations / R2 语义修订观察

Actual collection and review: **2026-10-27, Asia/Shanghai**. The directory retains its 20261026 planning label. This is a separate local experiment, not a replacement for the [original failed v2.5 record](../../RESULTS-v2.5.0.md), and is not a published stable release.

R2 modified four paragraphs: preserve necessary details across edits, keep unknown substance blank, ask complete questions without assuming pending events occurred, and keep current rewriting directions separate from downstream output contracts. Snapshots were frozen before inspecting the new tasks. [Runtime hashes](runtime-manifest.json) · [Protocol](PROTOCOL.md) · [Run manifest](run-manifest.json).

## Results / 结果

| Requested configuration | Repetition | Exposed regression tasks, stable → R2 | New tasks, stable → R2 | Recoveries / regressions (old; new) |
| --- | --- | --- | --- | --- |
| Luna / medium | 1 | 3/4 → 3/4 | 7/8 → 8/8 | 1/1; 1/0 |
| Luna / medium | 2 | 3/4 → 3/4 | 8/8 → 8/8 | 0/0; 0/0 |
| Sol / medium | 1 | 3/4 → 4/4 | 8/8 → 8/8 | 1/0; 0/0 |
| Sol / medium | 2 | 2/4 → 4/4 | 8/8 → 8/8 | 2/0; 0/0 |

**R2 did not pass the complete bounded repair check.** Sol passed its model-specific check; Luna did not. Luna R2 omitted the necessary calendar-date question in H16 repetition 2 and placed an optional mentor field after the email that had to be last in H14 repetition 1. All R2 responses had zero rubric-listed critical errors, but the remaining failures prevent promotion. The two critical baseline observations were in Sol repetition 2. [Machine-readable results](summary.json) · [All reconciled answers](reconciled-results.jsonl).

**R2 未完全通过修订检查。** Sol 在两轮旧失败题中均为 4/4；Luna 仍有一次日期信息缺口，并新增一次末尾字段位置问题。新题没有观察到修订版回退，但不能据此忽略旧题未解决的问题。后续修改必须另行冻结、另用新确认题，保留本轮结果。

## Evidence and limits / 证据与边界

- Four exposed tasks (H01/H02/H14/H16) were selected because previous failures occurred; they are diagnostic, not representative samples. Eight new synthetic tasks were independently authored without access to runtime or previous tasks/results. [Original author rubric](confirmation-rubrics-as-authored.jsonl) and [pre-collection adjustment](preflight-note.md) preserve the N06 clarification that a truthful shared reply may be complete without choosing an unresolved remedy.
- Eight fresh worker sessions produced 96 case responses: two models × two conditions × two batch repetitions × 12 tasks. Cases shared a batch context, so this is **not 96 independent single-case sessions**. Requested model/effort overrides were accepted; exact backend builds were not exposed. [Receipts](execution-receipts.json) and `outputs/` preserve all batches; there were no reruns or missing outputs, and all eight file hashes matched final receipts.
- Two independent AI reviewers initially agreed on 92/96 verdicts and critical-error flags. Four disagreements concerned implicit tone use or conditional playback allocation. They independently reconsidered while identities remained hidden and agreed on pass. Original judgments remain in [A](reviewer-a.jsonl) and [B](reviewer-b.jsonl), with [disagreements](review-disagreements.json) and [reconciliation A](reconciliation-a.json) / [B](reconciliation-b.json). These are AI judgments, not professional human review.
- Histories were supplied as role-labeled data. Graded artifacts are response strings in a batch JSON file, not native sequential chat finals. Results do not establish implicit discovery, live multi-turn execution, optimizer-to-executor handoff, multilingual coverage, provider API compatibility, resource savings or statistical significance. Models and strata are reported separately; denominators differ from the original v2.5 experiment.

The runtime was not retuned after viewing these responses. Any later revision remains separate from this frozen R2 evidence.
