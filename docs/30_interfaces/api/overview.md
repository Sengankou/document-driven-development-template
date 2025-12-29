# API概要

このドキュメントでは、API全体の方針と共通仕様を定義します。

## 基本情報

| 項目 | 内容 |
|------|------|
| ベースURL | `https://api.example.com/v1` |
| プロトコル | HTTPS |
| データ形式 | JSON |
| 文字エンコーディング | UTF-8 |

---

## バージョニング

### 方針
- URLパスにバージョンを含める（例: `/v1/users`）
- メジャーバージョンのみURLに反映
- 後方互換性のない変更時にバージョンアップ

### 現在のバージョン
- **v1**: 現行バージョン

---

## 認証・認可

### 認証方式
（例: JWT Bearer Token, OAuth 2.0, API Key など）

### 認証フロー
1. （認証の流れを記述）
2. ...

### 認証ヘッダー
```
Authorization: Bearer <token>
```

### トークン仕様
| 項目 | 内容 |
|------|------|
| 形式 | JWT |
| 有効期限 | （例: 1時間） |
| リフレッシュ | （方式を記述） |

---

## 共通リクエスト仕様

### 共通ヘッダー
| ヘッダー | 必須 | 説明 |
|---------|------|------|
| `Content-Type` | Yes | `application/json` |
| `Authorization` | 認証要 | Bearer トークン |
| `Accept-Language` | No | 言語指定（例: `ja`, `en`） |

### ページネーション
クエリパラメータでページネーションを制御:

| パラメータ | デフォルト | 説明 |
|-----------|-----------|------|
| `page` | 1 | ページ番号 |
| `per_page` | 20 | 1ページあたりの件数（最大100） |

---

## 共通レスポンス仕様

### 成功時
```json
{
  "data": { ... },
  "meta": {
    "page": 1,
    "per_page": 20,
    "total": 100
  }
}
```

### エラー時
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": [ ... ]
  }
}
```

### HTTPステータスコード
| コード | 意味 | 使用場面 |
|--------|------|---------|
| 200 | OK | 成功（GET, PUT, PATCH） |
| 201 | Created | リソース作成成功（POST） |
| 204 | No Content | 成功（DELETE） |
| 400 | Bad Request | リクエスト不正 |
| 401 | Unauthorized | 認証エラー |
| 403 | Forbidden | 認可エラー |
| 404 | Not Found | リソースなし |
| 422 | Unprocessable Entity | バリデーションエラー |
| 429 | Too Many Requests | レート制限超過 |
| 500 | Internal Server Error | サーバーエラー |

---

## エラーコード体系

| コード | 説明 |
|--------|------|
| `AUTH_INVALID_TOKEN` | トークンが無効 |
| `AUTH_EXPIRED_TOKEN` | トークンが期限切れ |
| `VALIDATION_ERROR` | バリデーションエラー |
| `RESOURCE_NOT_FOUND` | リソースが見つからない |
| `PERMISSION_DENIED` | 権限がない |
| ... | ... |

---

## レート制限

| 対象 | 制限 | ウィンドウ |
|------|------|----------|
| 認証済みユーザー | 1000 req | 1時間 |
| 未認証 | 100 req | 1時間 |

### レート制限ヘッダー
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640000000
```

---

## CORS

### 許可オリジン
- `https://example.com`
- `https://app.example.com`

### 許可メソッド
- GET, POST, PUT, PATCH, DELETE, OPTIONS

### 許可ヘッダー
- Content-Type, Authorization
