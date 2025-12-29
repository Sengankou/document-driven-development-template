# 80_manuals - マニュアル

エンドユーザー・開発者向けのマニュアルです。

## 特性
- **累積的**: 機能追加に応じて継続的に更新
- **対象読者**: エンドユーザー、開発者、運用者

## ドキュメント一覧

| ファイル | 目的 | 対象読者 |
|---------|------|---------|
| [user_guide.md](user_guide.md) | システムの使い方ガイド | エンドユーザー |
| [reference.md](reference.md) | 機能・APIの詳細リファレンス | 開発者、パワーユーザー |

## 必要に応じて追加

プロジェクトの特性に応じて以下を追加:

- `admin_guide.md` - 管理者向けガイド
- `developer_guide.md` - 開発者向けガイド
- `api_reference.md` - API詳細リファレンス（OpenAPI等から生成）
- `troubleshooting.md` - トラブルシューティングガイド
- `faq.md` - よくある質問

## マニュアル作成の元資料

マニュアルは以下のドキュメントを元に作成:

```
ユースケース (40_behavior/use_cases/)
    ↓
ユーザーガイド (user_guide.md)

API仕様 (30_interfaces/api/)
    ↓
リファレンス (reference.md)

画面仕様 (30_interfaces/ui/)
    ↓
ユーザーガイド (user_guide.md)
```

## 作成タイミング

- **開発中**: ドラフトを作成・更新
- **リリース前**: 最終レビュー・承認
- **リリース後**: フィードバックに基づき改善

## 多言語対応

国際化が必要な場合:

```
80_manuals/
├── ja/
│   ├── user_guide.md
│   └── reference.md
└── en/
    ├── user_guide.md
    └── reference.md
```
