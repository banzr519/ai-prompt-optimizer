# Language and locale guidance

Read only when language handling matters. Keep the core instruction in SKILL.md authoritative; localized user documentation does not create alternative behavior rules.

## Resolve the language

1. Follow explicit language assignments for each output: e.g. Chinese explanation and an English reusable prompt.
2. Otherwise follow the user's current request and established conversation preference, not the language of a quoted task, attachment, source code or README.
3. If a short mixed-language request is ambiguous, use the established preference or a reversible default. Ask only when a wrong choice would materially change the result.

Input language, explanation language, optimized-prompt language and the downstream deliverable's language can differ. Preserve their distinctions inside a portable prompt. Asking for an English optimized prompt does not cancel a requirement that the downstream email be in Spanish.

## Preserve locale without inventing one

- Chinese: maintain Simplified or Traditional as requested. Traditional does not by itself mandate a Taiwan, Hong Kong or other regional vocabulary. Ask about regional terminology only when consequential.
- Portuguese: distinguish pt-BR and pt-PT. Generic Portuguese is not automatically Brazilian; follow existing wording or an explicit preference. Other variants remain usable according to model capability.
- Ukrainian/Russian and Malay/Indonesian are distinct languages; never substitute one for the other.
- Filenames, identifiers and supplied placeholders remain byte-for-byte unchanged. Preserve Greek spelling such as Ελληνικά; do not mix a Latin `n` into the language label.
- Pāli (`pi`) is distinct from Balinese (`ban`) and Bengali (`bn`). Documentation uses a small experimental Latin-script Pāli/English entry. Do not silently normalize other Pāli scripts, transliteration systems or diacritics. Avoid inventing a canonical technical term; mark a gloss or retain the original technical term.
- Arabic, Persian and Hebrew use right-to-left prose. Keep code/paths in fenced code or inline code with their actual character order. Do not insert invisible direction controls into executable text. Document layout is a rendering concern and does not authorize changing the content.

## Semantics before typography

Preserve constraints, negation, named entities, numeric magnitude, units, currencies, dates and intentional tone. A decimal comma is not a thousands separator by default. Do not convert a date such as 03/04/2026 to a guessed calendar date when locale is unknown. Ask or preserve the source representation if the ambiguity matters.

Respect exact output keys/enums even when prose is localized. Translate free-text values only when requested or clearly appropriate. Keep exact slogans and quoted strings if the user asked to preserve them. Do not localize `true`, `false`, `null`, API fields, commands or the `$ai-prompt-optimizer` identifier.

When a length limit matters, preserve its stated unit. Chinese characters, Thai text segmentation, words, Unicode code points and model tokens are different measures. Do not invent a conversion ratio. Use a relevant counter only when tools and the agreed counting rule exist; otherwise describe the verification limitation.

## Coverage and honesty

The project has 30 documentation entries, including regional/script variants. This is a discoverability catalog, not a restriction: other languages may be used if the host model can handle them. No catalog entry implies provider integration, equal language quality or professional translation review.

Most added documents are AI-authored localized introductions and getting-started guides. Pāli is explicitly an experimental bilingual starter. Detailed research, publishing and historical evaluations remain in English/Chinese where not separately translated; label fallback links. Disclose a specific language uncertainty when present, not a repetitive disclaimer on every ordinary answer.
