# Independent intent-fidelity confirmation set

This directory contains eight fresh synthetic cases and separate requirement-based rubrics. The scope is prompt optimization, clarification, preservation of active instructions across revisions, and restraint on clear simple requests. No external knowledge, network, real-world execution, specialized domain expertise, or current factual lookup is needed.

The categories contain two cases each: Chinese multi-turn revisions; reusable-prompt or meta-level editing (including one English task); consequential missing information; and clear simple controls. The domains are deliberately varied. Logical relationships include upper bounds, expected versus maximum duration, alternative sufficient inputs, conditional fallbacks, partial updates, and the difference between absence of a requirement and prohibition.

Schema: messages is chronological prior conversation context only. current_request is the current user turn and is not duplicated inside messages. Empty messages arrays indicate self-contained current requests. An evaluation runner should concatenate messages with a final user message containing current_request.

The rubrics evaluate actual user requirements and permit equivalent wording. Instructions about a reusable prompt's future output are distinct from constraints on the present rewrite or audit. Where an unresolved choice prevents a final named assignment, a focused question or explicitly conditional work is accepted. Where the shared facts already support the requested notice, a truthful shared response is accepted without requiring a decision or a recap of all alternatives. Previously mentioned content is required only when it remains relevant to the requested artifact.

These are small synthetic confirmation cases, not a representative benchmark or a comprehensive safety, factuality, or performance evaluation. The simple controls check directness only. The missing-information cases cover different responses to uncertainty and do not imply that every ambiguity requires a question. Character-bound judgments should use a reasonable consistent counting convention rather than punctuation differences as a hidden scoring preference.

Authorship used only this task specification and the files created in this directory. No installed skill, project, prior test set, prior model output, other agent material, or network source was inspected. The tested runtime was reported as frozen before authorship; no runtime change or evaluation was performed here.
