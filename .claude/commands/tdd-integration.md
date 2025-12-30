---
name: tdd-integration
description: Enforce Test-Driven Development with strict Red-Green-Refactor cycle using integration tests. Auto-triggers when implementing new features or functionality. Trigger phrases include "implement", "add feature", "build", "create functionality", or any request to add new behavior. Does NOT trigger for bug fixes, documentation, or configuration changes.
---

# TDD 統合テスト

コードレビューフェーズを必須とする、厳格なテスト駆動開発を実施する。

## 必須ワークフロー

すべての新機能は、この厳格な3フェーズサイクルとコードレビューフェーズに従わなければならない。フェーズをスキップしてはならない。

### フェーズ1: RED - 失敗するテストを書く

🔴 REDフェーズ: tdd-test-writerに委譲中...

`tdd-test-writer` サブエージェントを以下の情報で呼び出す：
- ユーザーリクエストからの機能要件
- テストすべき期待される動作

サブエージェントが返すもの：
- テストファイルのパス
- テストが失敗したことを確認する出力
- テストが検証する内容のまとめ

**テストの失敗が確認されるまで、Greenフェーズに進んではならない。**

### フェーズ2: GREEN - テストを通す

🟢 GREENフェーズ: tdd-implementerに委譲中...

`tdd-implementer` サブエージェントを以下の情報で呼び出す：
- REDフェーズからのテストファイルパス
- 機能要件のコンテキスト

サブエージェントが返すもの：
- 変更されたファイル
- テストが通ったことを確認する出力
- 実装のまとめ

**テストが通るまで、Refactorフェーズに進んではならない。**

### フェーズ3: REFACTOR - 改善する

🔵 REFACTORフェーズ: tdd-refactorerに委譲中...

`tdd-refactorer` サブエージェントを以下の情報で呼び出す：
- テストファイルのパス
- GREENフェーズからの実装ファイル

サブエージェントが返すもの（いずれか）：
- 変更内容 + テスト成功出力、または
- 「リファクタリング不要」と理由

**レビューに進む前に完了させること。**

### フェーズ4: REVIEW - 品質ゲート
🔍 REVIEWフェーズ: code-reviewerに委譲中...

`code-reviewer` サブエージェントを以下の情報で呼び出す：
- 実装ファイル
- テストファイル
- ユーザーの元の要件

サブエージェントが返すもの：
- **ステータス: PASS** → サイクル完了
- **ステータス: FAIL** → 具体的なフィードバックと共にフェーズ3（Refactor）またはフェーズ2（Green）に戻る必要がある

**`code-reviewer`がPASSを返すまで、サイクルは完了しない。**

## 複数機能の場合

次の機能を開始する前に、各機能の完全なサイクルを完了させること：

- 機能1: 🔴 → 🟢 → 🔵 → 🔍 (PASS) ✓
- 機能2: 🔴 → 🟢 → 🔵 → 🔍 (FAIL) → 🔵 → 🔍 (PASS) ✓
- 機能3: 🔴 → 🟢 → 🔵 → 🔍 (PASS) ✓

## フェーズ違反

以下は禁止：
- テストより先に実装を書く
- Redの失敗を確認せずにGreenに進む
- Refactorの評価をスキップする
- 現在のサイクルを完了する前に新しい機能を開始する
- レビュアーからPASSを得る前に機能を完了としてマークする
- レビュアーからのアーキテクチャやスタイルに関する提案を無視する