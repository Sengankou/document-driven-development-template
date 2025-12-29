# Document Map

このドキュメントは、コーディングツール（Claude Code / Codex / Gemini CLI等）がプロジェクトのドキュメントを効率的に参照するためのインデックスです。

> **現在のフェーズ**: [CURRENT_PHASE.md](CURRENT_PHASE.md) を参照

---

## ドキュメント構造

```
docs/
├── CURRENT_PHASE.md          # 現在のフェーズ情報（最初に読む）
├── README.md                 # このファイル（ドキュメントマップ）
│
├── 00_project/               # プロジェクト定義（累積的）
├── 10_requirements/          # 要求定義（フェーズ別）
├── 20_architecture/          # アーキテクチャ（累積的）
├── 30_interfaces/            # インターフェース定義（累積的）
├── 40_behavior/              # 振る舞い・ロジック（ハイブリッド）
├── 50_cross_cutting/         # 横断的関心事（累積的）
├── 60_quality/               # 品質保証（ハイブリッド）
├── 70_operations/            # 運用（累積的）
├── 80_manuals/               # マニュアル（累積的）
└── 90_archive/               # 完了フェーズのアーカイブ
```

---

## 目的別ドキュメントガイド

### プロジェクトについて理解したいとき

| ドキュメント | 目的 | パス |
|------------|------|------|
| プロジェクト憲章 | 目的・スコープ・成功基準を知る | [charter.md](00_project/charter.md) |
| 組織体制 | 役割・責任・意思決定者を知る | [organization.md](00_project/organization.md) |
| 用語集 | プロジェクト固有の用語を確認 | [glossary.md](00_project/glossary.md) |
| リスク管理 | 既知のリスクと対策を確認 | [risks.md](00_project/risks.md) |

### 機能要件を知りたいとき

| ドキュメント | 目的 | パス |
|------------|------|------|
| 要件ロードマップ | 全体計画・フェーズ構成を把握 | [10_requirements/README.md](10_requirements/README.md) |
| ユーザーストーリー | ユーザー視点の要求を理解 | [phase1/user_stories.md](10_requirements/phase1/user_stories.md) |
| 要求仕様 | 機能・非機能要件の詳細 | [phase1/specifications.md](10_requirements/phase1/specifications.md) |

### システム構成を知りたいとき

| ドキュメント | 目的 | パス |
|------------|------|------|
| アーキテクチャ概要 | システム全体構成・技術スタック | [overview.md](20_architecture/overview.md) |
| データモデル | ER図・テーブル定義・型定義 | [data_model.md](20_architecture/data_model.md) |
| ADR | アーキテクチャ上の重要な決定事項 | [decisions.md](20_architecture/decisions.md) |
| 技術スタック | 使用技術の一覧と選定理由 | [tech_stack.md](20_architecture/tech_stack.md) |

### API/UIの仕様を知りたいとき

| ドキュメント | 目的 | パス |
|------------|------|------|
| API概要 | 認証・共通仕様・レート制限 | [api/overview.md](30_interfaces/api/overview.md) |
| APIエンドポイント | 各エンドポイントの詳細仕様 | [api/endpoints.md](30_interfaces/api/endpoints.md) |
| デザインシステム | UIガイドライン・コンポーネント | [ui/design_system.md](30_interfaces/ui/design_system.md) |
| 画面仕様 | 各画面の詳細仕様 | [ui/screens.md](30_interfaces/ui/screens.md) |
| 画面遷移 | 画面間の遷移フロー | [ui/navigation.md](30_interfaces/ui/navigation.md) |

### 実装の詳細を知りたいとき

| ドキュメント | 目的 | パス |
|------------|------|------|
| ビジネスロジック | ドメインルール・計算ロジック | [business_logic.md](40_behavior/business_logic.md) |
| 永続化処理 | DB操作・キャッシュ戦略 | [persistence.md](40_behavior/persistence.md) |
| 状態管理 | アプリケーション状態の管理方法 | [state_management.md](40_behavior/state_management.md) |
| ユースケース | 具体的な実装フロー | [use_cases/](40_behavior/use_cases/) |

### 横断的な仕様を知りたいとき

| ドキュメント | 目的 | パス |
|------------|------|------|
| セキュリティ | 認証・認可・データ保護 | [security.md](50_cross_cutting/security.md) |
| エラー処理 | エラーハンドリング方針 | [error_handling.md](50_cross_cutting/error_handling.md) |
| ログ戦略 | ログ出力・監視方針 | [logging.md](50_cross_cutting/logging.md) |
| 国際化 | 多言語対応・ローカライズ | [i18n.md](50_cross_cutting/i18n.md) |
| 外部連携 | 外部サービスとの連携仕様 | [external_integrations.md](50_cross_cutting/external_integrations.md) |
| ネットワーク | 通信・プロトコル仕様 | [network.md](50_cross_cutting/network.md) |

### 品質・テストについて知りたいとき

| ドキュメント | 目的 | パス |
|------------|------|------|
| テスト戦略 | テスト方針・カバレッジ目標 | [testing_strategy.md](60_quality/testing_strategy.md) |
| 性能要件 | パフォーマンス目標・計測方法 | [performance.md](60_quality/performance.md) |
| テスト計画 | フェーズ別のテスト計画 | [test_plans/](60_quality/test_plans/) |

### 運用について知りたいとき

| ドキュメント | 目的 | パス |
|------------|------|------|
| デプロイメント | デプロイ手順・環境構成 | [deployment.md](70_operations/deployment.md) |
| バックアップ・リカバリ | データ保全・復旧手順 | [backup_recovery.md](70_operations/backup_recovery.md) |
| 保守運用 | 運用ポリシー・監視体制 | [maintenance.md](70_operations/maintenance.md) |

### マニュアルを参照したいとき

| ドキュメント | 目的 | パス |
|------------|------|------|
| ユーザーガイド | エンドユーザー向け操作説明 | [user_guide.md](80_manuals/user_guide.md) |
| リファレンス | 機能・APIの詳細リファレンス | [reference.md](80_manuals/reference.md) |

---

## ドキュメント更新ルール

### 累積的ドキュメント（1つにまとめる）
- `00_project/`, `20_architecture/`, `30_interfaces/`, `50_cross_cutting/`, `70_operations/`, `80_manuals/`
- フェーズを超えて参照される「真実の源泉」
- 変更時は履歴を記録し、最新状態を維持

### フェーズ別ドキュメント
- `10_requirements/phaseN/`, `40_behavior/use_cases/phaseN/`, `60_quality/test_plans/phaseN/`
- 各フェーズの目標と成果を明確に記録
- 完了後は `90_archive/` にサマリを記録

### ID体系

| プレフィックス | 用途 | 例 |
|--------------|------|-----|
| PRJ | プロジェクト関連 | PRJ-001 |
| US | ユーザーストーリー | US-001 |
| REQ | 要求仕様（機能/非機能） | REQ-F-001, REQ-NF-001 |
| ADR | アーキテクチャ決定 | ADR-001 |
| API | APIエンドポイント | API-001 |
| SCR | 画面 | SCR-001 |
| UC | ユースケース | UC-001 |
| TC | テストケース | TC-001 |
| EXT | 外部連携 | EXT-001 |
