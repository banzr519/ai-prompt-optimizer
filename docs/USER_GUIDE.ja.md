# 利用ガイド · AI Prompt Optimizer

[日本語](../README.ja.md) · [English](USER_GUIDE.md) · [简体中文](USER_GUIDE.zh-CN.md) · [🌐 Languages / 语言](LANGUAGES.md)

**v2.5.0 · ja**

**Install with Codex / 使用 Codex 安装:** [English](INSTALL.md) · [简体中文](INSTALL.zh-CN.md) · [v2.5.0 candidate: regressions observed / 候选版：已观察到回退](../evals/RESULTS-v2.5.0.md)

## 必要な情報

目的、元の資料、変更禁止の内容、完了条件を伝えてください。添付資料がない場合は不足として明記し、空欄を推測で埋めません。

## 応用的な使い方

元のプロンプト、実際の回答、具体的な問題を渡して修正できます。変数付きテンプレート、JSON の出力条件、回答比較、会話の引き継ぎにも対応します。実測結果がなければ静的なレビューにとどめます。

## 言語と形式

説明、改善後の指示、最終成果物の言語を別々に指定できます。変数、コマンド、JSON キー、指定された引用文は変更しません。明示した言語は資料の言語より優先されます。

## 通常のチャットで使う

スキル非対応のチャットでは、SKILL.md の YAML ヘッダー以降の本文を貼り付け、元の依頼を別に入力してください。必要な参照資料だけを添付します。スキル名だけではファイルは読み込まれません。

## トラブル対処

スキルが見つからない場合はフォルダー構成、配置先、クライアントの対応を確認し、会話を開き直してください。更新前に独自の変更を保存してください。長すぎる回答には「1段落で」と指定できます。

## 範囲と検証

本ページは AI が作成したローカライズ版の入門資料で、母語話者による専門校閲は未実施です。結果はモデルとクライアントに依存します。30言語の入口は全モデルでの検証を意味しません。詳細な保守・調査資料は主に英語と簡体字中国語です。

## 詳細ドキュメント

- [English — full user guide](USER_GUIDE.md) · [简体中文 — 完整使用指南](USER_GUIDE.zh-CN.md)
- [English — models](MODEL_COMPATIBILITY.md) · [简体中文 — 模型说明](MODEL_COMPATIBILITY.zh-CN.md)
- [English — publishing](PUBLISHING.md) · [简体中文 — 发布指南](PUBLISHING.zh-CN.md)
- [English — research](RESEARCH.md) · [简体中文 — 研究记录](RESEARCH.zh-CN.md)
- [Language validation / 语言验证](../evals/RESULTS-v2.3.0.md)
