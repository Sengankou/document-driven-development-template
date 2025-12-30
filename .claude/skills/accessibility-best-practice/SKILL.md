---
name: accessibility-best-practices
description: アクセシビリティのベストプラクティス。WCAG 2.1、セマンティックHTML、キーボード操作、ARIA、コントラスト比、フォーカス管理等のレビュー時に参照。
allowed-tools: Read, Grep, Glob
---

# アクセシビリティ ベストプラクティス

## セマンティック HTML

### 原則
- 適切な HTML 要素を使用（div/span の乱用を避ける）
- 見出し階層（h1-h6）を正しく構造化
- ランドマーク要素（header, nav, main, footer）を活用

### アンチパターン

// ❌ div で見出しを模倣
<div style={{ fontSize: '32px', fontWeight: 'bold' }}>
  ページタイトル
</div>

// ✅ 適切な見出し要素
<h1>ページタイトル</h1>

// ❌ 見出し階層の飛ばし
<h1>タイトル</h1>
<h3>サブセクション</h3>  {/* h2 が飛ばされている */}

// ✅ 正しい見出し階層
<h1>タイトル</h1>
<h2>セクション</h2>
<h3>サブセクション</h3>


## インタラクティブ要素

### 原則
- クリック可能な要素は `<button>` または `<a>` を使用
- `<div onClick>` や `<span onClick>` は避ける
- キーボード操作（Enter, Space）に対応

### アンチパターン

// ❌ div をボタンとして使用
<div onClick={handleClick} style={{ cursor: 'pointer' }}>
  クリック
</div>

// ❌ role="button" だけでは不十分
<div role="button" onClick={handleClick}>
  クリック
</div>

// ✅ 適切な button 要素
<button type="button" onClick={handleClick}>
  クリック
</button>

// ✅ やむを得ず div を使う場合の完全な実装
<div
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault()
      handleClick()
    }
  }}
>
  クリック
</div>


## 画像の代替テキスト

### 原則
- すべての `<img>` に `alt` 属性を設定
- 装飾画像は `alt=""` で空に
- 意味のある画像は内容を説明する alt を設定

### アンチパターン

// ❌ alt 属性なし
<img src="/logo.png" />

// ❌ 無意味な alt
<img src="/logo.png" alt="image" />
<img src="/logo.png" alt="logo.png" />

// ✅ 意味のある alt
<img src="/logo.png" alt="会社ロゴ" />

// ✅ 装飾画像は空の alt
<img src="/decoration.png" alt="" />

// ✅ Next.js Image コンポーネント
<Image src="/logo.png" alt="会社ロゴ" width={100} height={50} />


## フォームのラベル

### 原則
- すべての入力要素に関連付けられた `<label>` を設定
- `id` と `for`（htmlFor）で関連付け
- または `<label>` で入力要素を囲む

### アンチパターン

// ❌ ラベルなし
<input type="text" placeholder="名前を入力" />

// ❌ placeholder はラベルの代替にならない
<input type="email" placeholder="メールアドレス" />

// ✅ label との関連付け
<label htmlFor="name">名前</label>
<input id="name" type="text" />

// ✅ label で囲む
<label>
  名前
  <input type="text" />
</label>

// ✅ 視覚的に非表示だがスクリーンリーダーに読み上げ
<label htmlFor="search" className="sr-only">検索</label>
<input id="search" type="search" placeholder="検索..." />


## コントラスト比

### 原則
- テキストと背景のコントラスト比は WCAG 基準を満たす
  - 通常テキスト: 4.5:1 以上
  - 大きいテキスト（18px bold / 24px）: 3:1 以上
- 色だけで情報を伝えない

### アンチパターン
// ❌ コントラスト比が低い
<p style={{ color: '#aaa', backgroundColor: '#eee' }}>
  このテキストは読みにくい
</p>

// ❌ 色だけでステータスを表現
{items.map(item => (
  <span style={{ color: item.active ? 'green' : 'red' }}>
    {item.name}
  </span>
))}

// ✅ 十分なコントラスト
<p style={{ color: '#333', backgroundColor: '#fff' }}>
  このテキストは読みやすい
</p>

// ✅ 色以外でも情報を伝達
{items.map(item => (
  <span style={{ color: item.active ? 'green' : 'red' }}>
    {item.name} {item.active ? '(有効)' : '(無効)'}
  </span>
))}


## フォーカス管理

### 原則
- フォーカスインジケータを削除しない
- カスタムフォーカススタイルを設定する場合は視認性を確保
- フォーカス順序（tabIndex）を適切に管理

### アンチパターン

/* ❌ フォーカスインジケータの削除 */
a:focus,
button:focus {
  outline: none;
}

/* ✅ カスタムフォーカススタイル */
a:focus,
button:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

/* ✅ focus-visible を活用 */
button:focus-visible {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}


### tabIndex の適切な使用
// ❌ 不適切な tabIndex
<div tabIndex={5}>...</div>  // 正の値は避ける

// ✅ tabIndex の適切な使用
<div tabIndex={0}>...</div>   // フォーカス可能にする
<div tabIndex={-1}>...</div>  // プログラムでのみフォーカス可能


## ARIA の正しい使用

### 原則
- ネイティブ HTML 要素を優先（ARIA は最後の手段）
- 第一ルール: 「ARIA を使わない方法があれば使わない」
- ARIA を使う場合は正しいロール・ステート・プロパティを設定

### アンチパターン

// ❌ 不要な ARIA
<button role="button">クリック</button>  // button には不要

// ❌ 誤った ARIA 使用
<div role="button">クリック</div>  // キーボード対応なし

// ✅ ネイティブ要素で十分
<button>クリック</button>

// ✅ 必要な場合の正しい ARIA
<div
  role="alert"
  aria-live="polite"
>
  エラーが発生しました
</div>

## lang 属性

### 原則
- `<html>` に `lang` 属性を設定
- 部分的に異なる言語がある場合は該当要素に `lang` を設定

### アンチパターン

// ❌ lang 属性なし
<html>
  <body>...</body>
</html>

// ✅ lang 属性あり
<html lang="ja">
  <body>...</body>
</html>

// ✅ 部分的な言語指定
<html lang="ja">
  <body>
    <p>日本語のテキスト</p>
    <p lang="en">English text</p>
  </body>
</html>

## レビューチェックリスト

- [ ] 適切な HTML 要素を使用しているか？（div/span の乱用なし）
- [ ] 見出し階層（h1-h6）は正しいか？
- [ ] クリック可能要素は `<button>` または `<a>` か？
- [ ] キーボード操作に対応しているか？
- [ ] すべての画像に適切な `alt` があるか？
- [ ] フォーム要素に `<label>` が関連付けられているか？
- [ ] コントラスト比は WCAG 基準を満たしているか？
- [ ] 色以外でも情報を伝達しているか？
- [ ] フォーカスインジケータが視認可能か？
- [ ] `<html lang="...">` が設定されているか？
