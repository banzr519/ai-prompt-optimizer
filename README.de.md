# AI Prompt Optimizer · Deutsch

[English](README.md) · [简体中文](README.zh-CN.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)

**v2.5.0 · MIT · de**

**Vage Wünsche in klare, ausführbare AI-Anweisungen umwandeln und dabei die ursprüngliche Absicht bewahren.**

Für Programmierung, Gestaltung, Texte, Recherche sowie Bild- und Videoaufträge. Zahlen, Einschränkungen und Variablen bleiben erhalten; Fakten werden von Annahmen getrennt. Die eigentliche Aufgabe wird nur auf ausdrücklichen Wunsch ausgeführt.

**Install, update and verify / 安装、更新与验证:** [English](docs/INSTALL.md) · [简体中文](docs/INSTALL.zh-CN.md) · [Candidate evidence / 候选验证](evals/v2.5.0/revision-20261027/README.md)

## Installation

Laden Sie das gesamte Projekt herunter, entpacken Sie es und nennen Sie den Ordner ai-prompt-optimizer. Legen Sie ihn an genau einem der folgenden Skill-Speicherorte ab. SKILL.md muss direkt darin liegen. Starten Sie anschließend einen neuen Chat.

```text
~/.agents/skills/ai-prompt-optimizer/
<project>/.agents/skills/ai-prompt-optimizer/
%USERPROFILE%\.agents\skills\ai-prompt-optimizer\
```

## Drei Modi

- Nur überarbeiten: eine kopierbare Anweisung erstellen, ohne die darin beschriebene Aufgabe auszuführen.
- Klären und ausführen: notwendige Fragen klären und die erlaubte Arbeit erledigen.
- Prüfen: wesentliche Widersprüche oder Lücken benennen und gezielt korrigieren.

## Beispiel

```text
$ai-prompt-optimizer Verbessere nur die Anweisung, führe sie nicht aus: Formuliere den Bericht professioneller, bewahre alle Fakten und Zahlen und ergänze keine unbelegten Schlussfolgerungen. Antworte auf Deutsch.
```

[Benutzerhandbuch](docs/USER_GUIDE.de.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)

## Umfang und Prüfung

Diese lokalisierte Einführung wurde mit AI erstellt und nicht professionell muttersprachlich lektoriert. Ergebnisse hängen von Modell und Client ab. 30 Spracheinträge bedeuten keine Tests aller Modelle. Ausführliche Wartungs- und Forschungsdokumente sind überwiegend auf Englisch und vereinfachtem Chinesisch verfügbar.

[MIT](LICENSE)
