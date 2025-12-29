# 10_requirements - 要求定義

ユーザー要求と機能/非機能要件を定義するドキュメント群です。

## 特性
- **フェーズ別**: 各フェーズごとにサブディレクトリを作成
- **対象読者**: プロダクトオーナー、開発チーム、ステークホルダー

## ディレクトリ構造

```
10_requirements/
├── README.md           # このファイル（ロードマップ）
├── backlog.md          # 将来フェーズの候補（未整理）
├── phase1/
│   ├── goals.md        # Phase 1 の目標・スコープ
│   ├── user_stories.md # Phase 1 のユーザーストーリー
│   ├── specifications.md # Phase 1 の要求仕様
│   └── acceptance.md   # Phase 1 の受け入れ基準
├── phase2/
│   └── ...
└── ...
```

## フェーズ別ドキュメント

### Phase 1
- [goals.md](phase1/goals.md) - フェーズ目標
- [user_stories.md](phase1/user_stories.md) - ユーザーストーリー
- [specifications.md](phase1/specifications.md) - 要求仕様
- [acceptance.md](phase1/acceptance.md) - 受け入れ基準

## ロードマップ

<!-- プロジェクト全体のフェーズ計画を記述 -->

| フェーズ | テーマ | 主要機能 | ステータス |
|---------|-------|---------|----------|
| Phase 1 | MVP | （主要機能を記述） | 計画中 |
| Phase 2 | 拡張 | （主要機能を記述） | 未着手 |
| ... | ... | ... | ... |

## ID体系

- **US-xxx**: ユーザーストーリー（例: US-001）
- **REQ-F-xxx**: 機能要件（例: REQ-F-001）
- **REQ-NF-xxx**: 非機能要件（例: REQ-NF-001）
- **AC-xxx**: 受け入れ基準（例: AC-001）

## トレーサビリティ

```
ユーザーストーリー (US-xxx)
    ↓
要求仕様 (REQ-xxx) ← 対応するUS-xxxを記載
    ↓
受け入れ基準 (AC-xxx) ← 対応するUS-xxx, REQ-xxxを記載
    ↓
テストケース (TC-xxx)
```
