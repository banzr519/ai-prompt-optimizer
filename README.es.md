# AI Prompt Optimizer · Español

[English](README.md) · [简体中文](README.zh-CN.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)

**v2.5.0 · MIT · es**

**Convierte peticiones vagas en instrucciones claras y ejecutables para AI, conservando la intención original.**

Sirve para programación, diseño, escritura, investigación y solicitudes de imágenes o vídeo. Conserva cifras, restricciones y variables, y distingue hechos de supuestos. Solo ejecuta la tarea original cuando se solicita expresamente.

**Install with Codex / 使用 Codex 安装:** [English](docs/INSTALL.md) · [简体中文](docs/INSTALL.zh-CN.md) · [v2.5.0 candidate: regressions observed / 候选版：已观察到回退](evals/RESULTS-v2.5.0.md)

## Instalación

Descarga y descomprime el proyecto completo y llama a la carpeta ai-prompt-optimizer. Colócala en una sola de las rutas de habilidades indicadas abajo. SKILL.md debe estar directamente dentro. Después inicia una conversación nueva.

```text
~/.agents/skills/ai-prompt-optimizer/
<project>/.agents/skills/ai-prompt-optimizer/
%USERPROFILE%\.agents\skills\ai-prompt-optimizer\
```

## Tres modos

- Solo mejorar: crear una instrucción copiable sin ejecutar la tarea que contiene.
- Aclarar y ejecutar: resolver las dudas necesarias y realizar el trabajo autorizado.
- Revisar: señalar contradicciones o carencias importantes y proponer cambios mínimos.

## Ejemplo

```text
$ai-prompt-optimizer Mejora solo la instrucción, no ejecutes la tarea: Haz el informe más profesional, conserva todos los hechos y cifras y no añadas conclusiones sin respaldo en los documentos. Responde en español.
```

[Guía de uso](docs/USER_GUIDE.es.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)

## Alcance y validación

Esta introducción localizada fue redactada con AI y no cuenta con revisión profesional de un hablante nativo. El resultado depende del modelo y del cliente. Las 30 entradas de idioma no implican pruebas en todos los modelos. La documentación detallada de mantenimiento e investigación está principalmente en inglés y chino simplificado.

[MIT](LICENSE)
