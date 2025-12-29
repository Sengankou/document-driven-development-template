# デプロイメント

このドキュメントでは、デプロイ手順と環境構成を定義します。

## 環境一覧

| 環境 | 用途 | URL | 更新タイミング |
|------|------|-----|---------------|
| Development | 開発 | localhost | 随時 |
| Staging | 検証 | staging.example.com | PR マージ時 |
| Production | 本番 | example.com | リリース時 |

---

## 環境構成

### Development
- ローカル開発環境
- Docker Compose で依存サービスを起動

### Staging
- 本番と同等の構成
- テストデータを使用
- 自動デプロイ（main ブランチ）

### Production
- 高可用性構成
- 本番データ
- 手動承認後にデプロイ

---

## デプロイフロー

### 通常リリース
```
1. feature ブランチで開発
2. PR 作成 → レビュー → main にマージ
3. main → Staging に自動デプロイ
4. Staging で検証
5. リリース承認
6. main → Production にデプロイ
```

### ホットフィックス
```
1. main から hotfix ブランチを作成
2. 修正 → PR → マージ
3. 即座に Production にデプロイ
```

---

## CI/CD パイプライン

### CI（継続的インテグレーション）
```yaml
# PR 時に実行
- lint          # コード品質チェック
- type-check    # 型チェック
- test:unit     # ユニットテスト
- test:e2e      # E2Eテスト
- build         # ビルド確認
```

### CD（継続的デリバリー）
```yaml
# main マージ時
- build         # 本番ビルド
- deploy:staging # Staging デプロイ

# リリース時
- deploy:production # Production デプロイ
```

---

## デプロイ手順

### 事前準備
- [ ] 全テストがパス
- [ ] ビルドが成功
- [ ] 変更内容のレビュー完了
- [ ] リリースノート作成

### デプロイ実行
```bash
# 例: デプロイコマンド
npm run deploy:production
```

### デプロイ後確認
- [ ] ヘルスチェック OK
- [ ] 主要機能の動作確認
- [ ] エラーログの確認
- [ ] パフォーマンスメトリクスの確認

---

## ロールバック手順

### 自動ロールバック
- ヘルスチェック失敗時に自動ロールバック

### 手動ロールバック
```bash
# 例: ロールバックコマンド
npm run rollback:production
```

### ロールバック判断基準
- クリティカルなバグの発見
- パフォーマンスの著しい低下
- セキュリティ問題の発見

---

## 環境変数

### 管理方法
- 開発: `.env.local`
- Staging/Production: シークレット管理サービス

### 環境変数一覧
| 変数名 | 説明 | 必須 |
|--------|------|------|
| `DATABASE_URL` | DB接続文字列 | Yes |
| `API_SECRET` | APIシークレット | Yes |
| ... | ... | ... |

---

## インフラ構成図

```
[CDN] → [Load Balancer] → [App Server x N] → [Database]
                                          ↘ [Cache]
```

（実際の構成に合わせて更新）
