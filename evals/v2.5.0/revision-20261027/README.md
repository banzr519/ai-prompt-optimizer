# R3 semantic repair check / R3 语义修订验证

Run date: **2026-10-27, Asia/Shanghai**. This revision follows the separately retained [R2 run](../revision-20261026/README.md). Stable `main` and the user's active installation remain v2.4.0. Publication is recorded separately in [repository metadata](../../../github-metadata.json).

R3 retains the R2 rule changes for active-context preservation, unknown facts and present-versus-future output contracts. It additionally preserves required first/last placement and distinguishes an undecided weekday/time option from a missing calendar date. The runtime was frozen before fresh task authorship and response collection; see the [protocol](PROTOCOL.md), [runtime hashes](runtime-manifest.json) and [preflight note](preflight-note.md). The four exposed cases H01/H02/H14/H16 keep their original requirements. Eight new synthetic cases were authored independently without access to the skill, previous cases or results; see [design notes](confirmation-design.md).

## Experiment

- Stable v2.4 versus R3; requested and accepted `gpt-5.6-luna` / `medium` and `gpt-5.6-sol` / `medium`.
- Two complete batch repetitions per model and version: **8 worker sessions, 96 case responses**. Each session handles 12 cases, so these are not 96 independent sessions. Case order is matched within a version pair and changed for the next repetition.
- Role-labeled histories are supplied as task data, not native prior conversation turns. Saved response strings are the artifacts being graded. No downstream optimizer-to-executor experiment is claimed.
- No reruns, model fallback, rejected configuration or missing response. All eight final receipt hashes match the saved outputs. Requested settings do not establish an independently verified backend model build.
- Two fresh AI reviewers receive anonymous answers and the frozen rubrics, without model/version mappings, runtime or previous results. This is AI semantic review, not human expert grading.

## Results

**R3 does not meet the bounded repair gate on Luna/medium. Sol/medium meets it in this run. This remains a review candidate, not an accepted stable upgrade.**

**中文结论：仍未全部通过。** Sol 两轮都通过 4 个旧失败题；Luna 两轮分别为 3/4、2/4，最终日期澄清仍有遗漏，第二轮另有语气要求遗漏。两种模型的 R3 在新题上两轮均为 8/8；不能用这些结果抵消旧题回退，也不能合并模型后宣布通过。

| Requested model | Repetition | Exposed 4: stable → R3 | Recovery / regression | Fresh 8: stable → R3 | Recovery / regression |
| --- | --- | --- | --- | --- | --- |
| Luna / medium | 1 | 3/4 → 3/4 | 0 / 0 | 7/8 → 8/8 | 1 / 0 |
| Luna / medium | 2 | 3/4 → 2/4 | 0 / 1 | 7/8 → 8/8 | 1 / 0 |
| Sol / medium | 1 | 3/4 → 4/4 | 1 / 0 | 8/8 → 8/8 | 0 / 0 |
| Sol / medium | 2 | 4/4 → 4/4 | 0 / 0 | 8/8 → 8/8 | 0 / 0 |

Both independent reviewers agreed on all **96/96** aggregate verdicts and critical-error flags initially: 88 pass, 8 fail, 0 unknown across both versions. No reconciliation or grading-driven response rerun was needed. There were no rubric-listed critical errors in R3, which does not make the remaining unmet requirements acceptable. Raw judgments and failures remain in [review A](reviewer-a.jsonl), [review B](reviewer-b.jsonl), [resolved records](reconciled-results.jsonl) and [summary](summary.json).

Luna R3 failed H16 in both repetitions: it reported that the poll was unresolved but did not ask for the confirmed option and calendar date needed for the final invitation. In repetition 2, H02 additionally omitted the active natural/not-too-formal tone requirement from the reusable prompt. This is a paired regression because that repetition's stable answer passed H02. The two fresh-case recoveries were N03's future word-count unit and specified fallback text. Sol's single old-case recovery was H16 in repetition 1; its other old-case repetition and both fresh-case repetitions were already at the baseline ceiling.

R2 had already failed the Luna gate (H16 and final-position preservation), while meeting Sol's bounded gate. R3's new set and outcomes must not be treated as a directly comparable percentage trend against R2. Both runs and the original failed candidate remain available. Additional instructions did not establish a dependable repair for Luna; these observations do not isolate the cause among instruction design, model variability and the batch-input format. Stop this registered run here rather than selecting or retrying poor answers until the scores pass.

## Installation and documentation

The [isolated installation check](installation-check.json) exercised stable installation, offline update to R3, preserved mode/user guidance, backups, refusal to overwrite local changes, status and uninstall. The real personal v2.4 installation was unchanged. New-chat discovery and invocation, Windows PowerShell execution, native plugin onboarding and online downloading were not tested in this smoke check.

The final automated suite passed **41/41** tests; localized generation is synchronized across 30 entries. Skill structure, JSON/JSONL, relative links and anchors, bilingual navigation, Python 3.9 grammar, frozen hashes and public-file checks passed. All 86 pre-existing evaluation/LICENSE files remain byte-identical to the starting commit, including the deliberately incorrect fixture. Intermediate documentation checks caught ungenerated pages and the not-yet-written report link; these were completed before the final passing suite. See [deterministic checks](verification.json).

## Limits

The four known failures informed development and remain exposed regression material. The eight fresh tasks are a small synthetic set, not a representative benchmark. Full scores on a fresh-task stratum provide no measured improvement there. Batch context, model variability and reviewer judgment remain limitations. Do not infer general accuracy gains, statistical significance, cost savings, all-language/all-model coverage or stable-release acceptance. The original failed candidate and R2 evidence are retained unchanged; no tag or GitHub Release is created by this check.

## Evidence

- [Task and run manifest](run-manifest.json), [tasks](cases.jsonl), [frozen rubrics](rubrics.jsonl).
- [Execution receipts](execution-receipts.json), individual JSON outputs in `outputs/`, and task packets in `packets/`.
- [Anonymous answers](blind-answers.jsonl), [answer mappings](answer-map.jsonl), [review instructions](reviewer-instructions.md).
