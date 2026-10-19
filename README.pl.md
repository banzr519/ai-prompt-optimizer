# AI Prompt Optimizer · Polski

[English](README.md) · [简体中文](README.zh-CN.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)

**v2.5.0 · MIT · pl**

**Zamieniaj niejasne prośby w zrozumiałe instrukcje dla AI, zachowując pierwotny zamiar.**

Do programowania, projektowania, pisania, badań oraz poleceń dotyczących obrazów i filmów. Zachowuje liczby, ograniczenia i zmienne oraz oddziela fakty od założeń. Właściwe zadanie wykonuje tylko na wyraźną prośbę.

**Install with Codex / 使用 Codex 安装:** [English](docs/INSTALL.md) · [简体中文](docs/INSTALL.zh-CN.md) · [v2.5.0 candidate: regressions observed / 候选版：已观察到回退](evals/RESULTS-v2.5.0.md)

## Instalacja

Pobierz i rozpakuj cały projekt, nadaj folderowi nazwę ai-prompt-optimizer. Umieść go tylko w jednej z poniższych lokalizacji umiejętności. SKILL.md musi znajdować się bezpośrednio w folderze. Następnie rozpocznij nową rozmowę.

```text
~/.agents/skills/ai-prompt-optimizer/
<project>/.agents/skills/ai-prompt-optimizer/
%USERPROFILE%\.agents\skills\ai-prompt-optimizer\
```

## Trzy tryby

- Tylko ulepsz: przygotuj instrukcję do skopiowania, bez wykonywania opisanego zadania.
- Doprecyzuj i wykonaj: wyjaśnij niezbędne kwestie, a następnie wykonaj dozwoloną pracę.
- Sprawdź: wskaż istotne sprzeczności lub braki i zaproponuj minimalne poprawki.

## Przykład

```text
$ai-prompt-optimizer Ulepsz tylko instrukcję, nie wykonuj zadania: Napisz raport bardziej profesjonalnie, zachowaj wszystkie fakty i liczby, nie dodawaj wniosków bez potwierdzenia w materiałach. Odpowiedz po polsku.
```

[Instrukcja obsługi](docs/USER_GUIDE.pl.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)

## Zakres i weryfikacja

Ten zlokalizowany przewodnik wprowadzający opracowano z AI; nie przeszedł profesjonalnej korekty przez rodzimego użytkownika języka. Wyniki zależą od modelu i klienta. 30 wersji językowych nie oznacza testów wszystkich modeli. Szczegółowe dokumenty utrzymaniowe i badawcze są głównie po angielsku i w chińskim uproszczonym.

[MIT](LICENSE)
