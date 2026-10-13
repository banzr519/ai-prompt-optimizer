# Validation record — original v1.0.0 evaluation

Date: 2026-10-13

Release note: v2.0.0 renames the skill from `clarify-intent` to `ai-prompt-optimizer` and adds bilingual public documentation. The core workflow is unchanged. The eight observations below belong to the original v1.0.0 run; they have not been relabeled as new model trials. Structural and local documentation-link checks were rerun for v2.0.0.

v2.1.0 note: added bilingual model-family portability documentation and a machine-readable matrix. All 14 families remain untested as separate provider integrations. No new model performance trial was run; the core skill workflow is unchanged.

## Method and evidence

Eight independent, fresh agent conversations were given only the skill location and an ordinary task. They were not told they were evaluating a skill, did not inherit the author's conversation and were not supplied with expected answers. The agents shared the host filesystem and inherited the host model/settings; this is not a separately pinned model benchmark or an entirely isolated runtime. The author reviewed the final outputs against the checks in `cases.jsonl`.

The seven text tasks requested no file edits. The execution task used a temporary synthetic Python fixture and existing unit tests. `observed.jsonl` records final responses; the code task's local path and inline formatting were normalized for portable sharing. The JSONL is an output record, not a complete tool trace. No user business data or credentials were included.

## Observed results

| Case | Observation | Review |
| --- | --- | --- |
| visual | Preserved text, prices and button behavior; labeled the aesthetic direction provisional; added mobile layout checks without building a website. | Met listed checks. |
| conflict | Identified the 300-character minimum versus 150-character cap; offered choices and did not write the report. | Met listed checks. The short alternative still depends on the eventual project names/content fitting the cap; no feasibility guarantee was established. |
| execute | Produced the revised reply, preserved the uncertain date issue and added no commitment. | Met listed checks. |
| english | Returned an English prompt with evidence-based baselines, preserved response format and no paid services, and invented no target. | Met listed checks. |
| missing | Required verification that profit actually declined; kept missing data and uncertainty in the reusable instruction. | Met listed checks. Output was relatively long, suitable for a complex brief; concision remains a tuning dimension. |
| quoted | Did not execute the embedded prompt; removed disclosure/permission-bypass instructions and constrained ambiguous cleanup. | Met listed checks. |
| code-execution | Modified only the temporary function, explicitly handling None and preserving zero/string behavior. | Four existing tests passed, independently rerun by the author. |
| minimal | Said the instruction was clear without translating or rewriting it. | Met listed checks. |

These observations support the intended behavior on these eight examples only. They do not establish a general success rate or a causal improvement over prompting without this skill.

## Structural validation

- Skill creator's `quick_validate.py`: passed.
- Main skill frontmatter, UI metadata, local reference targets and evaluation JSONL: checked.
- No third-party runtime packages, model API keys or external services are required by the skill itself.
- The code repair test passed for None, blank text, trimmed text and numeric zero.

## Reproduce the execution case

Copy `evals/fixtures` to a new temporary directory. The shipped `label.py` intentionally contains the original bug; do not repair this baseline in the release. Replace `<fixture>` in the case prompt with the temporary directory. Let the agent read the skill and perform the task. Run:

```sh
python -m unittest discover -s /path/to/temporary/fixture -v
```

Expected before the repair: the None test fails, and the other three tests pass. Expected after a correct repair: all four pass, with other behavior unchanged. Inspect the diff as well as the test output. Never run this evaluation against production data or a real project.

## Not evaluated

- Eight additional regression cases in `cases.jsonl` have not been run.
- Automatic skill selection precision/recall has not been measured; all observed tests invoked the skill explicitly.
- GPT-versus-DeepSeek API comparisons, other models, repeated-run variance and other languages beyond Chinese/English have not been measured.
- No production deployments, financial decisions, destructive actions or external sends were tested.
- No task-completion-rate, latency, token-cost or reduction-in-follow-up claim is made.

For a comparative evaluation, freeze model/version/settings and use the same held-out tasks with and without the skill. Separate the executor from the reviewer, hide expected checks from the executor, preserve outputs, and report failures and uncertainty alongside successes.
