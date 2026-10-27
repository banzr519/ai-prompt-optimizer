# R3 semantic repair confirmation

Registered 2026-10-27, Asia/Shanghai, before response collection. This is a new revision following the separately preserved [R2 run](../revision-20261026/README.md), not a rerun of selected poor answers.

## Frozen change and tasks

R3 adds explicit preservation of requested first/last placement and makes the distinction between an unresolved weekday/time option and its missing calendar date more direct. It retains the other R2 corrections. Runtime was frozen before the R3 author produced the fresh confirmation set and before the implementation author inspected it. [Hashes](runtime-manifest.json).

Use the same four exposed regression cases and original rubrics, H01/H02/H14/H16. Add eight newly authored synthetic confirmation tasks from a fresh author who has no access to runtime, previous tasks, outputs or conclusions. The author receives only broad categories: two multi-turn revisions, two reusable prompts, two material-information gaps, and two direct-response controls. Avoid previously used domains where practical. Record any pre-collection task/rubric corrections, retaining originals; never change them after collecting outputs.

## Fixed experiment

Use the same neutral batch wrapper and design as R2: stable v2.4 versus frozen R3, explicitly requested Luna/medium and Sol/medium, two repetitions for every condition. Eight fresh workers produce 96 case responses. Each worker handles 12 cases in a declared shuffled order; paired versions share an order, with a different order in repetition 2. Cases share context within a batch and are **not independent sessions**. Seed 20261027 fixes run/task order. Keep model identity/effort as requested/accepted, without inventing backend details.

Workers read only their assigned task packet, assigned SKILL.md and relevant linked runtime references. They receive no rubric or previous outcomes. No network or external effects. Exact response strings saved in JSON are the graded artifacts; final receipts contain output SHA256. Preserve all outputs, infrastructure failures and rejected configurations. No model fallback or answer reruns. This bounded revision will be reported even if it fails; no success claim follows merely from completing a run.

Two fresh independent AI reviewers grade randomized anonymous answers against frozen rubrics. No model/condition mappings, runtime or previous results. Preserve original judgments and resolve disagreements without revealing identities; unresolved substantive ambiguities remain unknown. Equivalent wording is accepted. Exact placeholders, scoped formatting and numeric constraints are checked; Chinese length uses NFC-normalized non-whitespace characters. A future artifact's length or JSON schema is not imposed on the present rewritten instruction.

## Decision rule and limits

Apply the same bounded repair gate separately to each model: R3 passes all four exposed regression tasks in both repetitions, has no rubric-listed critical errors, and has no paired regression or unknown on the eight new tasks in either repetition. Report both-pass, both-fail, recovery and regression counts per repetition/stratum. A baseline ceiling means no improvement can be inferred for that stratum. Never combine models to pass a gate.

Passing indicates a bounded repair observation, not stable-release qualification, statistical significance, a general improvement rate, all-model/all-language coverage or optimizer-to-executor transfer. Histories are data, not native prior turns. Batch-format and shared-context effects remain possible. No native implicit-discovery test, provider API benchmark, token/cost measurement or real external action is claimed. Keep R2 and original v2.5 evidence unchanged and do not replace the user's active v2.4 installation.
