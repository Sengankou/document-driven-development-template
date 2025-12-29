# Current Phase: Phase 1

> このファイルは、コーディングツールが最初に参照すべきエントリーポイントです。
> 現在のフェーズで何を実装すべきか、何を参照すべきかを示します。

---

## フェーズ概要

| 項目 | 内容 |
|------|------|
| フェーズ名 | Phase 1: 初期リリース |
| 期間 | YYYY-MM-DD 〜 YYYY-MM-DD |
| テーマ | （例: MVP機能の実装） |
| ステータス | 計画中 / 進行中 / 完了 |

## フェーズ目標

<!-- このフェーズで達成すべきゴールを記述 -->

1. （目標1）
2. （目標2）
3. （目標3）

## 実装対象

### ユーザーストーリー
- [user_stories.md](10_requirements/phase1/user_stories.md)

### 要求仕様
- [specifications.md](10_requirements/phase1/specifications.md)

### ユースケース
- [use_cases/phase1/](40_behavior/use_cases/phase1/)

### テスト計画
- [test_plans/phase1/](60_quality/test_plans/phase1/)

---

## 参照すべき設計ドキュメント

### 必須参照
| ドキュメント | 参照理由 | リンク |
|------------|---------|--------|
| アーキテクチャ概要 | システム全体構成の把握 | [overview.md](20_architecture/overview.md) |
| データモデル | テーブル・型定義 | [data_model.md](20_architecture/data_model.md) |
| API仕様 | エンドポイント実装時 | [endpoints.md](30_interfaces/api/endpoints.md) |
| 画面仕様 | UI実装時 | [screens.md](30_interfaces/ui/screens.md) |

### 横断的関心事（必要に応じて参照）
| ドキュメント | 参照タイミング | リンク |
|------------|---------------|--------|
| セキュリティ | 認証・認可実装時 | [security.md](50_cross_cutting/security.md) |
| エラー処理 | エラーハンドリング実装時 | [error_handling.md](50_cross_cutting/error_handling.md) |
| ログ戦略 | ログ出力実装時 | [logging.md](50_cross_cutting/logging.md) |

---

## 前フェーズからの変更点

<!-- Phase 2以降で記入 -->
（Phase 1のため該当なし）

---

## 進捗・メモ

<!-- フェーズ進行中に更新 -->

### 完了した項目
- [ ] （完了した項目をチェック）

### 課題・ブロッカー
- （発生した課題を記録）

### 決定事項
- （フェーズ中に決定した事項を記録）

---

## 次フェーズへの引き継ぎ事項

<!-- フェーズ完了時に記入 -->

- （次フェーズで対応すべき事項）
- （残タスク・技術的負債）
