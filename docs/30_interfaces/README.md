# 30_interfaces - インターフェース定義

システムの外部・内部インターフェースを定義するドキュメント群です。

## 特性
- **累積的**: 全エンドポイント・画面を1箇所で管理
- **対象読者**: フロントエンド開発者、バックエンド開発者、APIコンシューマー

## ディレクトリ構造

```
30_interfaces/
├── README.md       # このファイル
├── api/
│   ├── overview.md    # API全体方針・認証・共通仕様
│   └── endpoints.md   # エンドポイント定義
└── ui/
    ├── design_system.md  # デザインシステム・UIガイドライン
    ├── screens.md        # 画面仕様
    ├── navigation.md     # 画面遷移
    ├── wireframes.md     # ワイヤーフレーム
    └── components.md     # 共通コンポーネント
```

## API ドキュメント

| ファイル | 目的 |
|---------|------|
| [api/overview.md](api/overview.md) | ベースURL、認証方式、共通レスポンス形式、レート制限 |
| [api/endpoints.md](api/endpoints.md) | 各エンドポイントの詳細仕様 |

### API ID体系
- **API-xxx**: エンドポイント（例: API-001）

## UI ドキュメント

| ファイル | 目的 |
|---------|------|
| [ui/design_system.md](ui/design_system.md) | カラー、タイポグラフィ、スペーシング等のガイドライン |
| [ui/screens.md](ui/screens.md) | 各画面の詳細仕様（表示項目、入力項目、バリデーション） |
| [ui/navigation.md](ui/navigation.md) | 画面遷移図・遷移条件 |
| [ui/wireframes.md](ui/wireframes.md) | ワイヤーフレーム・モックアップ |
| [ui/components.md](ui/components.md) | 共通UIコンポーネント仕様 |

### 画面 ID体系
- **SCR-xxx**: 画面（例: SCR-001）
- **CMP-xxx**: 共通コンポーネント（例: CMP-001）

## 作成順序

1. **api/overview.md** - API全体方針を先に決定
2. **ui/design_system.md** - UI全体方針を先に決定
3. **api/endpoints.md** と **ui/screens.md** - 並行して作成
4. 残りのドキュメント - 必要に応じて作成

## フェーズ管理

累積的ドキュメントですが、フェーズごとの追加を明示するため:

```markdown
## API-020: POST /payments
<!-- [Phase 2] で追加 -->
...
```

のようにコメントでフェーズを記録し、リリース後に削除します。
