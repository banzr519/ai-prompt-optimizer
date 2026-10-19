# AI Prompt Optimizer · 日本語

[English](README.md) · [简体中文](README.zh-CN.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)

**v2.5.0 · MIT · ja**

**意図を保ったまま、曖昧な依頼を明確で実行可能な AI 指示に整えます。**

開発、デザイン、文章作成、調査、画像・動画の指示に利用できます。数値、制約、変数を保持し、事実と仮定を区別します。元の作業は明示的に依頼された場合だけ実行します。

**Install with Codex / 使用 Codex 安装:** [English](docs/INSTALL.md) · [简体中文](docs/INSTALL.zh-CN.md) · [v2.5.0 candidate: regressions observed / 候选版：已观察到回退](evals/RESULTS-v2.5.0.md)

## インストール

プロジェクト全体をダウンロードして展開し、フォルダー名を ai-prompt-optimizer に変更します。下記のいずれか1つのスキル用フォルダーに配置し、SKILL.md が直下にあることを確認して新しい会話を開始します。

```text
~/.agents/skills/ai-prompt-optimizer/
<project>/.agents/skills/ai-prompt-optimizer/
%USERPROFILE%\.agents\skills\ai-prompt-optimizer\
```

## 3つの使い方

- 最適化のみ：コピーして使える指示を作り、その中の作業は実行しません。
- 整理して実行：必要な点だけ確認し、許可された作業を進めます。
- レビュー：重要な矛盾や不足を指摘し、必要最小限の修正を示します。

## 例

```text
$ai-prompt-optimizer 指示だけを改善し、作業は実行しないでください：報告書をより専門的な文章にしてください。事実と数値をすべて保持し、資料に裏付けのない結論を追加しないでください。日本語で出力してください。
```

[利用ガイド](docs/USER_GUIDE.ja.md) · [🌐 Languages / 语言](docs/LANGUAGES.md)

## 範囲と検証

本ページは AI が作成したローカライズ版の入門資料で、母語話者による専門校閲は未実施です。結果はモデルとクライアントに依存します。30言語の入口は全モデルでの検証を意味しません。詳細な保守・調査資料は主に英語と簡体字中国語です。

[MIT](LICENSE)
