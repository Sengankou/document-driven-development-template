# 15_tasks - 実装タスク

実装方法が確定したタスクチケットを管理します。
各タスクは Claude Code へのプロンプトとして直接利用できます。

## 特性

- **フェーズ別**: 各フェーズごとにサブディレクトリを作成
- **Claude Code連携**: `/subagent-fastapi docs/15_tasks/phase1/task01.md` のように使用
- **対象読者**: 開発者、Claude Code

## ディレクトリ構造

```
15_tasks/
├── README.md           # このファイル（タスク管理ダッシュボード）
├── _template.md        # タスクチケットテンプレート
├── ideas.md            # 検討中のアイデア（実装方法未定）
├── phase1/
│   ├── task01-xxx.md   # 個別タスクチケット
│   └── ...
└── phase2/
    └── ...
```

## タスクのライフサイクル

```
アイデア発生
    ↓
ideas.md に記録（検討中）
    ↓
要件整理 → 10_requirements/ に反映（必要に応じて）
    ↓
実装方法決定 → phaseN/taskNN-xxx.md にチケット化
    ↓
Claude Code で実行: /subagent-fastapi docs/15_tasks/phase1/task01.md
    ↓
完了 → ステータス更新 or 90_archive/ へ移動
```

## タスク一覧

### Phase 1

| ID | タイトル | 担当 | ステータス | 関連要件 |
|----|---------|------|----------|---------|
| TASK-001 | （タスク名） | fastapi-python-expert | 未着手 | US-001 |
| ... | ... | ... | ... | ... |

### Ideas（検討中）

[ideas.md](ideas.md) を参照

---

## ID体系

- **TASK-NNN**: 実装タスク（例: TASK-001）
- **IDEA-NNN**: 検討中アイデア（例: IDEA-001）

## ステータス定義

| ステータス | 定義 |
|-----------|------|
| 未着手 | 実装開始前 |
| 進行中 | 実装作業中 |
| レビュー中 | 実装完了、レビュー待ち |
| 完了 | 実装・テスト完了 |
| 保留 | 一時停止（理由を記載） |

## 担当エージェント

| エージェント | 対象技術 |
|-------------|---------|
| fastapi-python-expert | Python / FastAPI / バックエンド |
| react-vite-spa-typescript-expert | TypeScript / React / フロントエンド |
| hono-cloudflare-expert | Hono / Cloudflare Workers |

## 使用方法

### タスク実行

```bash
# FastAPI タスクの実行
/subagent-fastapi docs/15_tasks/phase1/task01-user-auth.md

# React タスクの実行
# （フロントエンド用スキルがあれば）
```

### 新規タスク作成

1. `_template.md` をコピー
2. `phaseN/taskNN-概要.md` にリネーム
3. 内容を記入
4. このREADMEの一覧表に追加
