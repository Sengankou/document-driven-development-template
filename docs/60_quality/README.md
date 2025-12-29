# 60_quality - 品質保証

テスト戦略と品質要件を定義するドキュメント群です。

## 特性
- **ハイブリッド**:
  - テスト戦略・性能要件は**累積的**
  - テスト計画は**フェーズ別**
- **対象読者**: 開発チーム、QAチーム

## ディレクトリ構造

```
60_quality/
├── README.md              # このファイル
├── testing_strategy.md    # テスト戦略（累積的）
├── performance.md         # 性能要件（累積的）
└── test_plans/            # テスト計画（フェーズ別）
    ├── phase1/
    │   └── test_plan.md
    └── phase2/
        └── ...
```

## 累積的ドキュメント

| ファイル | 目的 | 更新タイミング |
|---------|------|---------------|
| [testing_strategy.md](testing_strategy.md) | テスト方針・カバレッジ目標・テスト種別 | テスト方針変更時 |
| [performance.md](performance.md) | 性能目標・計測方法・ベンチマーク | 性能要件変更時 |

## フェーズ別ドキュメント（テスト計画）

各フェーズのテスト計画を `test_plans/phaseN/` に配置:

- [test_plans/phase1/](test_plans/phase1/) - Phase 1 のテスト計画

### テスト計画の構成例

```
test_plans/phase1/
├── test_plan.md        # テスト計画概要
├── test_cases.md       # テストケース一覧
└── test_data.md        # テストデータ定義
```

## ID体系

- **TC-xxx**: テストケース（例: TC-001）
- **TS-xxx**: テストシナリオ（例: TS-001）

## トレーサビリティ

```
受け入れ基準 (AC-xxx)
    ↓
テストケース (TC-xxx) ← 対応するAC-xxx, REQ-xxxを記載
    ↓
テスト結果
```

## テストピラミッド

```
        /\
       /  \  E2E Tests (少数)
      /----\
     /      \ Integration Tests (中程度)
    /--------\
   /          \ Unit Tests (多数)
  /--------------\
```

`testing_strategy.md` で各層の方針を定義します。
