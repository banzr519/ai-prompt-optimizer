# 使用指南 · AI Prompt Optimizer

[繁體中文](../README.zh-Hant.md) · [English](USER_GUIDE.md) · [简体中文](USER_GUIDE.zh-CN.md) · [🌐 Languages / 语言](LANGUAGES.md)

**v2.4.0 · zh-Hant**

**Install with Codex / 使用 Codex 安装:** [English](INSTALL.md) · [简体中文](INSTALL.zh-CN.md)

## 提供資料

提供目標、原始資料、不可更動的內容，以及如何判斷完成。缺少附件時應明確註記，不要為了補齊格式而猜測。

## 進階用法

可提供原提示詞、實際回答與錯誤，要求針對性修訂；也可建立變數模板、檢查 JSON 格式、比較回答或整理對話交接。沒有實測結果時只能做靜態審閱。

## 語言與格式

可分別指定說明語言、優化後指令的語言和最終產出的語言。變數、命令、JSON 欄位與指定原文保持不變；繁體中文不自動等同特定地區用語。

## 一般聊天使用方式

不支援技能的聊天工具：貼上 SKILL.md 在 YAML 標頭之後的正文，再另行提供需求。只附必要參考資料。僅輸入技能名稱不會自動載入檔案。

## 疑難排解

找不到技能時檢查資料夾層級、安裝位置和客戶端支援，並重開對話。更新前保留自訂內容；不要直接覆蓋。輸出太長時可要求一段話。

## 範圍與驗證

本頁是 AI 撰寫的在地化入門文件，未經母語專業審校。效果取決於模型與客戶端；30 個語言入口不代表各模型均已實測。完整維護與研究文件主要提供英文及簡體中文。

## 完整文件

- [English — full user guide](USER_GUIDE.md) · [简体中文 — 完整使用指南](USER_GUIDE.zh-CN.md)
- [English — models](MODEL_COMPATIBILITY.md) · [简体中文 — 模型说明](MODEL_COMPATIBILITY.zh-CN.md)
- [English — publishing](PUBLISHING.md) · [简体中文 — 发布指南](PUBLISHING.zh-CN.md)
- [English — research](RESEARCH.md) · [简体中文 — 研究记录](RESEARCH.zh-CN.md)
- [Language validation / 语言验证](../evals/RESULTS-v2.3.0.md)
