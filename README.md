# Document-Driven Development Template

コーディングツール（Claude Code / Codex / Gemini CLI など）を活用した開発において、十分なコンテキスト情報を提供するためのドキュメントテンプレートです。

## 背景・目的

PoCを超えた規模のプロジェクトでは、コーディングツールが十分にコンテキストを把握しきれず、不適切なコードを生成するケースが多発します。

**このテンプレートの目的:**
- 構造化されたドキュメントにより、コーディングツールが必要な情報を効率的に参照できる
- プロジェクトの全体像から詳細仕様まで、階層的に情報を整理
- フェーズ管理と累積的なドキュメント管理を両立

## クイックスタート

1. このリポジトリをテンプレートとして使用
2. [docs/CURRENT_PHASE.md](docs/CURRENT_PHASE.md) を確認し、現在のフェーズを設定
3. [docs/README.md](docs/README.md) でドキュメント構造を把握
4. プロジェクトに必要なドキュメントを選択・記述

## Claude Code中心のAIコーディング戦略
1. 並列開発：git worktreeで「モジュールごとに別窓」を作る

    基本は1モジュール1 Claude Codeで実装することで、それぞれのconflictは最小限に抑えられる

2. Markdownによるタスクチケット管理

    Claude Codeに投げる指示をMarkdownで書き、そのファイルをそのまま渡す

    "スラッシュコマンド＋Markdownファイルパス指定"で、実装↔レビューを強制ループ

    常に並列稼働させるために「次にやるタスク」をストックしておく

3. ★（考え中）：：：tddとexpertの統合ができるか？expertにtddの各フェーズのSKILLを参照させるようにするか...？

## ドキュメント構造

```
docs/
├── CURRENT_PHASE.md          # 現在のフェーズ情報（エントリーポイント）
├── README.md                 # ドキュメントマップ
│
├── 00_project/               # プロジェクト定義（累積的）
│   ├── charter.md            # プロジェクト憲章
│   ├── organization.md       # 組織体制
│   ├── glossary.md           # 用語集
│   └── risks.md              # リスク管理
│
├── 10_requirements/          # 要求定義（フェーズ別）
│   ├── README.md             # ロードマップ
│   ├── backlog.md            # 将来の候補
│   └── phase1/               # Phase 1
│       ├── goals.md          # 目標
│       ├── user_stories.md   # ユーザーストーリー
│       ├── specifications.md # 要求仕様
│       └── acceptance.md     # 受け入れ基準
│
├── 20_architecture/          # アーキテクチャ（累積的）
│   ├── overview.md           # システム概要
│   ├── decisions.md          # ADR
│   ├── tech_stack.md         # 技術スタック
│   └── data_model.md         # データモデル
│
├── 30_interfaces/            # インターフェース（累積的）
│   ├── api/
│   │   ├── overview.md       # API概要
│   │   └── endpoints.md      # エンドポイント定義
│   └── ui/
│       ├── design_system.md  # デザインシステム
│       ├── screens.md        # 画面仕様
│       ├── navigation.md     # 画面遷移
│       ├── wireframes.md     # ワイヤーフレーム
│       └── components.md     # 共通コンポーネント
│
├── 40_behavior/              # 振る舞い（ハイブリッド）
│   ├── business_logic.md     # ビジネスロジック
│   ├── state_management.md   # 状態管理
│   ├── persistence.md        # 永続化
│   └── use_cases/            # ユースケース（フェーズ別）
│       └── phase1/
│
├── 50_cross_cutting/         # 横断的関心事（累積的）
│   ├── security.md           # セキュリティ
│   ├── error_handling.md     # エラー処理
│   ├── logging.md            # ログ戦略
│   ├── i18n.md               # 国際化
│   ├── external_integrations.md # 外部連携
│   └── network.md            # ネットワーク
│
├── 60_quality/               # 品質保証（ハイブリッド）
│   ├── testing_strategy.md   # テスト戦略
│   ├── performance.md        # 性能要件
│   └── test_plans/           # テスト計画（フェーズ別）
│       └── phase1/
│
├── 70_operations/            # 運用（累積的）
│   ├── deployment.md         # デプロイメント
│   ├── backup_recovery.md    # バックアップ・リカバリ
│   └── maintenance.md        # 保守運用
│
├── 80_manuals/               # マニュアル（累積的）
│   ├── user_guide.md         # ユーザーガイド
│   └── reference.md          # リファレンス
│
└── 90_archive/               # アーカイブ
    └── phase1/               # 完了フェーズの記録
```

## ドキュメントの種類

### 累積的ドキュメント
フェーズを超えて継続的に更新される「真実の源泉」
- プロジェクト定義、アーキテクチャ、インターフェース、横断的関心事、運用、マニュアル

### フェーズ別ドキュメント
各フェーズの目標と成果を記録
- 要求定義（ユーザーストーリー、仕様）、ユースケース、テスト計画

## コーディングツールでの活用

コーディングツールは以下の順序でドキュメントを参照することを想定:

1. **[docs/CURRENT_PHASE.md](docs/CURRENT_PHASE.md)** - 現在のフェーズと参照すべきドキュメントを確認
2. **[docs/README.md](docs/README.md)** - 必要なドキュメントを目的別に検索
3. **各ドキュメント** - 詳細情報を取得

## ドキュメント間の関係性と作成順序

各ドキュメントは独立しているわけではなく、相互に関連し合っています。

### 作成順序の概要

1. **プロジェクト初期化**: プロジェクト憲章、組織体制、用語集（初版）、リスク管理（初版）
2. **要求分析**: ユーザーストーリー、要求仕様書
3. **アーキテクチャ設計**: アーキテクチャ概要、ADR、技術スタック
4. **データ設計**: データモデル
5. **詳細設計**: API仕様、画面仕様、ユースケース
6. **実装・テスト**: テスト計画、テスト実施
7. **リリース準備**: マニュアル

### トレーサビリティ（追跡可能性）

```
プロジェクト憲章（目的・スコープ）
    ↓
ユーザーストーリー（US-001...）
    ↓
要求仕様書（REQ-F-001, REQ-NF-001...）
    ↓
設計仕様書群
    ├─ アーキテクチャ（ADR-001...）
    ├─ データモデル
    ├─ API仕様（API-001...）
    ├─ 画面仕様（SCR-001...）
    └─ ユースケース（UC-001...）
    ↓
テスト仕様（TC-001...）
    ↓
マニュアル
```

## プロジェクト規模別の推奨

### 個人開発
**必須:**
- プロジェクト憲章（簡易版）
- アーキテクチャ概要
- データモデル

**推奨:**
- ユーザーストーリー
- API/画面仕様

### 小規模チーム（2-5人）
**必須:**
- 00_project 全体
- 10_requirements 全体
- 20_architecture 全体
- 30_interfaces 全体
- 60_quality（テスト戦略）

**推奨:**
- 40_behavior
- 50_cross_cutting（必要なもの）

### 中規模以上（6人+）
**すべてのドキュメントを作成することを推奨**

## 重要な原則

1. **ドキュメントは手段であり目的ではない** - プロジェクトの実態に合わせて柔軟に運用
2. **段階的な詳細化** - すべてを一度に完璧に作ろうとせず、段階的に詳細化
3. **トレーサビリティの確保** - ドキュメント間のIDによる紐付けを徹底
4. **継続的な更新** - 特に用語集、リスク管理表は常に最新の状態を保つ
5. **LLMの活用** - ドキュメント作成・整合性チェックにLLMを活用
6. **実装との整合性** - ドキュメントと実装が乖離しないよう常にチェック

## 参考

- [ソフトウェアプロジェクトドキュメント 上流工程ガイド](https://github.com/osawa-naotaka/vanishtodo/blob/main/doc/software_project_documents.md)
- https://zenn.dev/mkj/articles/868e0723efa060


## ライセンス

MIT License
