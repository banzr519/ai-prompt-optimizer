# Preregistered paired evaluation protocol

Status: proposed evaluation protocol and practical acceptance criterion, prepared independently of either skill implementation. This is our proposed criterion, not a user-specified requirement and not statistical certification. No model experiment has been run by the dataset designer. All tasks and conversations are synthetic.

## Files and access separation

- `inputs.jsonl`: 24 core cases. Fields: `id`, `category`, `messages`, `current_request`.
- `rubrics.jsonl`: the corresponding independent evaluator records. Fields: `id`, `category`, `rubric`.
- `ui_inputs.jsonl`: 4 additional direct-deliverable UI-entry probes.
- `ui_rubrics.jsonl`: evaluator records for the UI probes.
- `category_counts.json`: aggregate counts for the core set only.
- `FREEZE_MANIFEST.json`: exact SHA-256 hashes of the frozen inputs, rubrics, counts and protocol.

Join inputs and rubrics only by `id` for evaluation. Executors receive only their assigned input case, the assigned frozen skill snapshot and any normal runtime dependencies needed to load that skill. They must not receive rubrics, other cases, implementation proposals, prior observed outputs or the other condition's answer. Dataset construction scripts are evaluator-side material because they contain rubrics; do not expose them to executors.

The core `messages` array contains historical turns, excluding `current_request`. Replay it in order, then append `current_request` as the final user turn exactly once. Historical assistant messages are synthetic context, not experimental outputs or evidence of earlier model behavior. Empty `messages` is valid. User text must be unchanged across paired conditions.

## Independence and freezing

The dataset designer did not inspect either version's SKILL.md, runtime references, previous experimental responses, implementation proposals or candidate files. The 24 core cases were completed before any candidate contents were available to the designer. The additional UI probes are a separate stratum requested before execution; they do not replace or modify the core cases.

Freeze and hash both complete skill snapshots, the task input files, evaluator rubrics, protocol, common wrapper and execution settings before the first scored run. The implementation author should freeze the candidate before opening task contents or rubrics. Record the snapshot paths and actual hashes in the run manifest. A candidate change after viewing results creates a new candidate; this holdout is then exposed, and a newly authored independent holdout is required for a new confirmation claim.

Do not tune the skill, task text, rubric, scoring policy, outcome gate or task selection to observed answers. A substantive data defect discovered during review requires documenting the defect before condition labels are revealed, excluding the paired case from both conditions, and treating the current preregistered gate as inconclusive rather than quietly changing its denominator. Correct cosmetic typos only with an audit record; never rewrite task difficulty after execution.

## Two distinct invocation strata

### Core skill: 24 pairs

Invoke the assigned frozen skill explicitly using the same neutral harness entry instruction for both versions. Do not use either version's UI `default_prompt` here. The entry instruction must request use of the assigned skill for the conversation, without telling the model whether to refine, answer directly, ask questions, or choose defaults. Those choices must follow the synthetic conversation itself.

Use one fresh executor per condition per case. The executor may load its own snapshot and its prescribed runtime references but may not access task-external websites, APIs, user files or another experiment's state. The final deliverable is plain text. A reference absent from the supplied conversation is deliberately unavailable; appropriate uncertainty handling is a valid complete response to that case.

### UI-entry probe: 4 additional pairs

For each assigned snapshot, extract the actual `agents/openai.yaml` `default_prompt`, preserving it exactly, and provide that entry text followed by the identical assigned UI user task. Record the exact extracted text and source hash. Do not substitute a paraphrase, a manually repaired entry prompt, or the other version's entry prompt. All other executor settings and permissible runtime loading must match the core protocol.

These probes measure final-deliverable fidelity through the UI entry path, not whether a response uses preferred words. Keep their results, denominators and comparison tables separate from the 24 core cases. A 4-case UI improvement cannot inflate a core skill improvement claim, and a core improvement cannot be used to claim the UI entry improved. Missing or unparseable default_prompt is a reported UI setup defect; do not invent a fallback prompt.

## Paired execution controls

- Run v2.4 and v2.5 on the same actual host, model configuration, tool permissions, sampling settings where controllable, context limits and reasoning configuration. Record settings actually exposed by the host; mark undisclosed settings as unavailable.
- Use independent fresh sessions with no prior task outputs, conversational memory, cross-case cache content or reviewer feedback deliberately injected. Do not reuse an ongoing executor between conditions.
- Precompute and save a reproducible random run order, balancing which condition runs first across cases and categories. Use an identical task and historical conversation within each pair. Record the randomization seed, exact request, output and actual execution receipt where available.
- One scored response per condition per case is the primary run: 48 core outputs plus 8 UI outputs. Do not silently rerun a poor answer or select the best of multiple attempts. Log infrastructure failures separately; a transparent paired retry with unchanged settings is permissible only for a verified transport/infrastructure failure, not an undesirable answer.
- A one-shot clarifying response may be correct on a materially missing case. Do not fabricate follow-up user answers for one condition. No extra-turn rescues are part of this primary protocol.
- If repeated runs are desired, predeclare the number and seed/order policy before observing answers, run all cases in both conditions equally, and report every repetition separately plus the predeclared aggregate. Repetition is not a license to select favorable outputs.
- Record model IDs, versions, token counts and latency only when actually returned or reliably measured. Do not infer a model identity from marketing labels or invent token counts from character counts. If same-host equivalence cannot be verified, report the limitation and do not describe the comparison as controlled.

## Blinded review

Keep the version-to-run mapping in an executor-only manifest. Export final answers to reviewers under randomly assigned anonymous output IDs, without snapshot paths, version labels, model receipts or timestamps that reveal assignment. Randomize left/right position within each pair; do not always make one letter the baseline. Do not rewrite substantive output text to conceal a self-revealed version; instead flag possible unblinding.

Reviewers receive task context, the relevant frozen rubric and anonymous final outputs. Prefer two independent reviewers. Each should initially score each answer on its own before viewing the pair together, then reconcile disagreements while still blinded. Preserve both original judgments and adjudicated results. If only one reviewer is available, report that limitation and independently audit all claimed recoveries, new failures and critical errors before revealing labels.

Score observed deliverables and preserved meaning, not internal reasoning, preferred terminology, resemblance to the candidate's instruction language or personal style taste. `acceptable_variants` explicitly prevent a single exemplar wording from becoming the answer key. Reviewers must identify the exact missing/violated requirement and point to the output evidence for every failure. Rubrics are not instructions to executors.

## Case scoring and error taxonomy

For every output record:

1. `pass`: all material `must_preserve` and `must_deliver` requirements met, with no listed critical violation. An acceptable variant satisfies the equivalent requirement. Cosmetic wording differences do not fail a case.
2. `critical_error`: yes/no plus the exact applicable rubric item and output evidence. Count both the number of affected cases and distinct error types. Unsupported factual invention, reversing a prohibition, performing explicitly forbidden execution, or pretending an unseen reference was available are examples where a case rubric marks them critical. Other omissions or format/length violations are not automatically critical.
3. `noncritical_failures`: each unmet deliverable, format, length or fidelity requirement not classified as critical. Treat absence of a requested real deliverable as a task failure even if the response is articulate.
4. `verbosity`: separately label proportionate, somewhat excessive, or materially distracting. Do not add verbosity to the pass count or critical-error total. Necessary disclosure of a conflict or a targeted clarification is not needless verbosity. If length/format is itself an explicit task constraint, score that observable violation separately from the general verbosity label.
5. `unnecessary_clarification`: note whether the answer withheld a useful reversible deliverable for an immaterial question. Do not penalize targeted clarification where the rubric identifies materially missing information. No universal rule that asking fewer questions is better.

For explicit Chinese length limits, count non-whitespace visible characters; punctuation, each digit and each Latin character count as one. For English word limits, use whitespace-delimited words after trimming. Historical constraints count only when still active; latest explicit changes supersede incompatible earlier requirements. Do not count scaffolding outside a quoted target as part of the target's length unless the task asks for only that deliverable. When the task requires only the deliverable, extra commentary is a format failure.

## Proposed practical improvement gate

This is a conservative project acceptance criterion proposed before the first run. It is not a user-specified target and not statistical certification. Only core-case recoveries can establish the required gain; UI cases supply a separate entry-path safeguard and must be reported separately.

Calculate paired outcomes after blinded adjudication:

- recovery: baseline fails, candidate passes;
- new failure/regression: baseline passes, candidate fails;
- stable pass and stable fail;
- critical failure: a case with at least one rubric-listed critical error.

The candidate meets the proposed practical acceptance gate only if all conditions hold:

1. At least four paired recoveries among the 24 core cases.
2. Zero pass-to-fail regressions among either the 24 core cases or the 4 UI-entry probes.
3. Zero candidate critical-failure cases across both strata.
4. No unknown judgments or missing paired outcomes. All outputs must be scored with adjudicated evidence; unverifiable infrastructure failures or unresolved judgments make acceptance inconclusive.

This deliberately conservative gate requires meaningful task recoveries and guards against displaced failure. An already-existing critical error still blocks acceptance if it remains in the candidate. Passing the gate does not certify the skill as universally safe or error-free. Report all observed baseline and candidate critical errors even when the gate is not met.

If baseline has fewer than four failing core cases, the dataset has too little headroom to satisfy this preregistered practical gate. Report the result as inconclusive for practical improvement, even if the candidate is perfect. Do not relax the gate after seeing a strong baseline. Stable high quality or observed regressions can still be reported descriptively. A separately authored frozen follow-up holdout is needed to test additional improvement.

No significance claim is justified by this gate. Report all four category pass counts, the paired contingency table, critical-error evidence and verbosity separately. State that the 24 deliberately selected small tasks are not a random sample of all user requests and do not measure long documents, browsing, coding tools or real external actions.

## Separate UI-entry reporting

Report the four UI pairs in their own table. For the UI path itself to be called improved on this probe, require zero new failures, zero candidate critical cases and at least one paired recovery. If both versions pass all four, report fidelity preserved with no measured improvement; do not claim improvement from a prompt text diff alone. If the baseline already passes all four, improvement is inconclusive for this probe. UI recoveries never count toward the four required core recoveries. A UI regression or candidate critical error blocks the joint project acceptance gate even when the core cases improve.

## Interpretation cautions

- The core dataset is majority Chinese with one English case in each six-case category. The UI probe is three Chinese cases and one English case. Do not infer broad multilingual robustness from these counts.
- Missing-reference cases intentionally test honest handling of unavailable context. They do not authorize accessing user files or constructing invented context.
- This is primarily a final-deliverable and faithful-intent evaluation. It cannot establish hidden reasoning quality, reliability across all sampling runs, production latency or token savings.
- Qualitative gains in calmness, concision or preferred wording may be reported separately but cannot rescue a failed task or meet the core gate.
- A two-condition evaluation with one sample per case is sensitive to sampling variability. Do not present the exact observed recovery rate as a guaranteed future improvement rate.
