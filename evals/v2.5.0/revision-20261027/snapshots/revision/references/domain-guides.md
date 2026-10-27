# Domain selection guide

Select the primary deliverable. Use only checks relevant to it; an entire row is not mandatory scope.

| Domain | Ground first | Translate vague quality into | Consequential missing information |
| --- | --- | --- | --- |
| Software feature | Existing behavior, files, project rules, desired user action | Required behavior, necessary states, compatibility, proportionate verification | Business rule, environment, irreversible migration |
| Bug repair | Observed vs expected behavior, reproduction, error evidence | Root cause, bounded fix, directly affected regressions | Missing failing artifact or ambiguous expected behavior |
| UI / visual design | Reference, content, existing system, surface | Hierarchy, spacing, typography, readability, relevant responsive/interaction states | Whether layout/content may change; required reference missing |
| Writing / editing | Audience, purpose, supplied facts, length/tone | Clear message, useful structure, factual fidelity, appropriate language | Recipient identity when sending; crucial missing facts |
| Analysis / research | Decision, sources, date window, metric definitions | Evidence, comparison basis, uncertainty, alternatives, implications | Missing dataset, incompatible measurement definitions |
| Product requirements | Journey, rules, scope, existing product | Input/output, state transitions, exceptions, observable acceptance | Commercial rules, permissions, authoritative version |
| Slides / documents | Content, hierarchy, intended use, editability | Faithful relationships, readable layout, correct export and content checks | Conflicting sources; whether text may change |
| Planning / learning | Goal, starting point, actual constraints | Ordered actions, milestones and learner-appropriate checks | Deadline/budget when essential; starting level if material |
| Operations / automation | Trigger, source, destination, authority | Conditions, exception handling, evidence of completion | Who/what to affect, permission, irreversible scope |
| Personal decision | Goals and supplied preferences | Options, relevant trade-offs, conditional recommendation | Preference that changes a costly decision |

## Capability-aware wording

- For a coding prompt without repository access, instruct the downstream agent to inspect files; do not claim repository facts.
- For analysis without data, specify needed evidence and mark conclusions pending. Do not create figures to fill a table.
- For a missing design reference, give a provisional direction or request the reference when fidelity is essential; do not claim visual matching.
- For authorized execution without a necessary tool, state the limitation and complete what is possible. Do not advertise capabilities this skill does not supply.
- For medical, legal or financial topics, preserve the question and require appropriate evidence and uncertainty. Do not invent individualized thresholds or convert exploration into an action recommendation without context.

## Minimal clarification examples

- “这份内容给管理层还是执行人员看？这决定我保留决策结论还是操作细节。” Ask only when context does not answer it and the output would materially differ.
- “你要求保持每句话原文，又改写语气。可以改措辞并保留事实，还是必须逐字保留？” Name the actual conflict.
- “我可以先完成候选清单，但删除前需要明确哪些数据算‘没用’。” Continue unblocked work; do not invent a deletion rule.
