# 50_cross_cutting - 横断的関心事

機能を横断する共通の関心事を定義するドキュメント群です。

## 特性
- **累積的**: 全フェーズで一貫性を保つため1箇所で管理
- **対象読者**: 開発チーム全員

## ドキュメント一覧

| ファイル | 目的 | 参照タイミング |
|---------|------|---------------|
| [security.md](security.md) | 認証・認可・データ保護 | 認証機能実装時、セキュリティレビュー時 |
| [error_handling.md](error_handling.md) | エラー分類・ハンドリング方針 | 例外処理実装時 |
| [logging.md](logging.md) | ログレベル・出力形式・監視 | ログ出力実装時 |
| [i18n.md](i18n.md) | 多言語対応・ローカライズ | 国際化対応時 |
| [external_integrations.md](external_integrations.md) | 外部サービス連携仕様 | 外部API連携実装時 |
| [network.md](network.md) | 通信仕様・プロトコル | ネットワーク通信実装時 |

## 必要に応じて追加

プロジェクトの特性に応じて以下を追加:

- `caching.md` - キャッシュ戦略
- `monitoring.md` - 監視・アラート設計
- `feature_flags.md` - フィーチャーフラグ管理
- `rate_limiting.md` - レート制限
- `audit.md` - 監査ログ

## 参照ガイド

### セキュリティ関連の実装時
1. [security.md](security.md) で認証・認可方式を確認
2. [error_handling.md](error_handling.md) でセキュリティエラーの扱いを確認
3. [logging.md](logging.md) でセキュリティログの出力方針を確認

### 外部連携の実装時
1. [external_integrations.md](external_integrations.md) で連携先の仕様を確認
2. [error_handling.md](error_handling.md) で外部エラーの扱いを確認
3. [network.md](network.md) で通信仕様を確認

## ID体系

- **SEC-xxx**: セキュリティ要件（例: SEC-001）
- **EXT-xxx**: 外部連携（例: EXT-001）
