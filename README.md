# Memo API

FlaskとSQLiteを使ったシンプルなメモ管理API

## 🌟 機能

- ✅ メモの作成
- ✅ メモ一覧取得
- ✅ 個別メモ取得
- ✅ メモ更新
- ✅ メモ削除
- ✅ タグ機能
- ✅ SQLiteデータベースで永続化

## 🛠 技術スタック

- **Python** 3.11
- **Flask** - Webフレームワーク
- **SQLite** - データベース

## 📦 インストール

### 1. リポジトリをクローン
```bash
git clone https://github.com/code-craftsman369/memo-api.git
cd memo-api
```

### 2. 依存パッケージをインストール
```bash
pip install flask
```

## 🚀 使い方

### サーバーを起動
```bash
python app.py
```

サーバーが `http://localhost:5004` で起動します。

## 📝 API エンドポイント

### 1. ホームページ
```bash
GET /
```

**レスポンス例**：
```json
{
  "message": "メモ管理APIへようこそ",
  "endpoints": {
    "memos": "GET /memos",
    "create": "POST /memos",
    "detail": "GET /memos/<id>",
    "update": "PUT /memos/<id>",
    "delete": "DELETE /memos/<id>"
  }
}
```

---

### 2. メモを作成
```bash
POST /memos
Content-Type: application/json

{
  "title": "メモのタイトル",
  "content": "メモの内容",
  "tags": "タグ1,タグ2"  // オプション
}
```

**レスポンス例**：
```json
{
  "id": 1,
  "title": "メモのタイトル",
  "content": "メモの内容",
  "tags": "タグ1,タグ2",
  "created_at": "2025-11-15 07:51:02"
}
```

**curlでの実行例**：
```bash
curl -X POST http://localhost:5004/memos \
  -H "Content-Type: application/json" \
  -d '{"title": "買い物リスト", "content": "牛乳、卵、パン", "tags": "買い物,日常"}'
```

---

### 3. メモ一覧を取得
```bash
GET /memos
```

**レスポンス例**：
```json
{
  "memos": [
    {
      "id": 1,
      "title": "メモのタイトル",
      "content": "メモの内容",
      "tags": "タグ1,タグ2",
      "created_at": "2025-11-15 07:51:02",
      "updated_at": "2025-11-15 07:51:02"
    }
  ],
  "count": 1
}
```

**curlでの実行例**：
```bash
curl http://localhost:5004/memos
```

---

### 4. 個別メモを取得
```bash
GET /memos/<id>
```

**レスポンス例**：
```json
{
  "id": 1,
  "title": "メモのタイトル",
  "content": "メモの内容",
  "tags": "タグ1,タグ2",
  "created_at": "2025-11-15 07:51:02",
  "updated_at": "2025-11-15 07:51:02"
}
```

**curlでの実行例**：
```bash
curl http://localhost:5004/memos/1
```

---

### 5. メモを更新
```bash
PUT /memos/<id>
Content-Type: application/json

{
  "title": "更新されたタイトル",  // オプション
  "content": "更新された内容",    // オプション
  "tags": "新しいタグ"           // オプション
}
```

**レスポンス例**：
```json
{
  "message": "メモを更新しました",
  "id": 1
}
```

**curlでの実行例**：
```bash
curl -X PUT http://localhost:5004/memos/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "更新されたメモ"}'
```

---

### 6. メモを削除
```bash
DELETE /memos/<id>
```

**レスポンス例**：
```json
{
  "message": "メモを削除しました"
}
```

**curlでの実行例**：
```bash
curl -X DELETE http://localhost:5004/memos/1
```

## 💡 使用例

### シナリオ：買い物メモを管理
```bash
# 1. メモを作成
curl -X POST http://localhost:5004/memos \
  -H "Content-Type: application/json" \
  -d '{"title": "買い物リスト", "content": "牛乳、卵、パン", "tags": "買い物"}'

# レスポンス: {"id": 1, ...}

# 2. メモ一覧を確認
curl http://localhost:5004/memos

# 3. メモを更新（チーズを追加）
curl -X PUT http://localhost:5004/memos/1 \
  -H "Content-Type: application/json" \
  -d '{"content": "牛乳、卵、パン、チーズ"}'

# 4. 買い物が終わったので削除
curl -X DELETE http://localhost:5004/memos/1
```

## 🗄️ データベース構造

### memos テーブル

| カラム | 型 | 説明 |
|--------|-----|------|
| id | INTEGER | 主キー（自動増分） |
| title | TEXT | メモのタイトル |
| content | TEXT | メモの内容 |
| tags | TEXT | タグ（カンマ区切り） |
| created_at | TEXT | 作成日時 |
| updated_at | TEXT | 更新日時 |

## 📁 ファイル構成
```
memo-api/
├── app.py                 # メインアプリケーション
├── memos.db              # SQLiteデータベース（自動生成）
├── .gitignore
└── README.md
```

## 🎓 学習内容

このプロジェクトを通じて学んだこと：

- FlaskでのCRUD API実装
- SQLiteデータベース操作（INSERT, SELECT, UPDATE, DELETE）
- REST APIの設計原則
- エラーハンドリング
- タプルの正しい使い方（カンマの重要性）
- データベーストランザクション
- レスポンスステータスコード（200, 201, 404, 400）

## 🔜 今後の改善予定（Day 22-23）

- [ ] 検索機能（タイトル・内容での検索）
- [ ] タグでのフィルタリング
- [ ] 日付範囲でのフィルタリング
- [ ] ページネーション
- [ ] ソート機能
- [ ] HTMLフロントエンド
- [ ] ユーザー認証
- [ ] 画像添付機能

## ⚠️ 注意事項

- このプロジェクトは学習目的です
- 本番環境で使用する場合は、以下の対策を追加してください：
  - ユーザー認証
  - 入力バリデーション強化
  - セキュリティヘッダー
  - HTTPS対応

## 📄 ライセンス

MIT License

## 👤 作成者

Tatsu - Python Developer
- GitHub: [@code-craftsman369](https://github.com/code-craftsman369)

## 🙏 謝辞

- [Flask](https://flask.palletsprojects.com/) - Webフレームワーク
- [SQLite](https://www.sqlite.org/) - データベース