# Open-source research and v2.2.0 decisions

**English** | [简体中文](RESEARCH.zh-CN.md) · [Home](../README.md)

Reviewed on 2026-10-14. Scope: official repository READMEs, linked first-party documentation and the workflows they describe. The projects were not locally deployed, comprehensively code-audited or benchmark-reproduced. Selection emphasizes relevance, inspectable workflows and evaluation design, not star counts. This is not an exhaustive ranking.

## Decision

Keep AI Prompt Optimizer a lightweight skill inside an existing AI client. Extend the vague-request-to-clear-instruction flow with observed failure, targeted repair and evidence-based checking. A beginner can still use one sentence; advanced users can request templates, output contracts, handoffs and comparisons.

## Sources and adaptations

| Project and primary source | Observed design | Adaptation here | Outside this release |
| --- | --- | --- | --- |
| [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) | System/user prompt modes, variables/context testing, result comparison, iteration and image prompting | Variable fidelity, stable rules separated from inputs, feedback repair and image/video briefs | Web/desktop/extension UI, provider connections and persistent asset management |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo); [assertions](https://www.promptfoo.dev/docs/configuration/expected-outputs/) | Deterministic and model-graded checks of actual outputs | Separate static review from effectiveness; hard constraints first, with format and semantic checks identified | No CLI integration; a test plan is not a completed test |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy); [optimizers](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/learn/optimization/optimizers.md) | Optimize instructions/examples using a task program, metric and examples | Establish criteria first; separate development from final checks; use examples only when helpful | Automated search, weight optimization and expensive default runs |
| [microsoft/PromptWizard](https://github.com/microsoft/PromptWizard) | Feedback, critique and joint iteration over instructions and examples | Use original prompt, observed output and correction to make a targeted revision | Unbounded self-review, automatic example floods or forced chain-of-thought output |
| [gepa-ai/gepa](https://github.com/gepa-ai/gepa) | Evaluator feedback, candidate revision, train/validation data and call budgets | Preserve a baseline, tie repairs to evidence and bound comparison/stopping | No implementation of the GEPA algorithm; no inherited benchmark claims |
| [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | Reusable task patterns, standalone reuse and user customization | Load advanced workflows on demand and offer practical natural-language entry points | No bulk template import or universal rigid format |

The changes are independently authored interaction rules and documentation. No upstream source code or complete prompt was copied; no third-party runtime dependency was introduced. These references establish design provenance, not endorsement or certification.

## Implemented in v2.2.0

1. **Repair from observed failures.** Keep working instructions; distinguish demonstrated defects from hypotheses. Support changed-lines-only requests.
2. **Reusable variables.** Preserve identifiers and delimiters; describe required/optional inputs, missing behavior, and the meaning of false, zero and empty values.
3. **Output contracts.** Preserve JSON keys, enums, types and null rules. Separate plain chat from API roles without promising perfect format compliance.
4. **Evidence-based comparison.** Review prompt text statically; compare supplied actual outputs as observations; run bounded tests only when requested with an available authorized runner. An inconclusive answer is valid.
5. **Conversation handoff.** Carry current decisions, unsuperseded constraints and required attachments; exclude discarded options and invented completion.
6. **Image/video briefs.** Protect composition, dimensions, lettering, characters and reference roles. Disclose missing media; do not invent provider parameters or generate media in refinement mode.
7. **Adaptive length.** A paragraph for small tasks, structure for consequential complexity, and ordinary-language preferences for concise, detailed or result-only responses.

The invocation remains `$ai-prompt-optimizer`. Refine, Execute and Audit remain the three modes. Optional workflows load only when relevant.

## Priorities after this release

| Priority | Candidate | Entry condition and acceptance |
| --- | --- | --- |
| Next | Optional promptfoo evaluation example/connector | A real batch-testing need, pinned version, credentials and bounded calls; matched original/candidate inputs with actual exported results |
| Next | Community failure/regression set | Anonymized examples permitted for sharing; context, actual/expected behavior and a no-change counterexample |
| On demand | Saved/versioned prompt assets | Known host storage, privacy and sync requirements; no unsolicited edits to persistent user instructions |
| On demand | Client distribution/adapters | Install and verify in each target host/version; model portability is not proof of native loading |
| Outside core for now | Automated multi-model search or a complete app | Separate product scope with validated demand, cost controls and maintenance; retain standalone skill use |

## Acceptance principles

- Preserve constraints and facts; do not execute in refine-only mode; continue when execution is requested.
- Produce reusable, independently copyable outputs with proportionate explanation.
- Distinguish structure checks, agent trials, downstream effectiveness and provider API benchmarks.
- Stop at agreed checks/budget; never invent scores, improvement percentages or token savings.

See the [v2.2.0 validation record](../evals/RESULTS-v2.2.0.md) for actual trials and limitations. These are behavioral checks, not a randomized success rate or an old-versus-new effectiveness experiment.
