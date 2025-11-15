# Memo API

FlaskとSQLiteを使った実用的なメモ管理アプリ

## 🌟 機能

- ✅ メモの作成・読取・更新・削除（CRUD）
- ✅ **タイトル・内容での検索機能**
- ✅ **タグでのフィルタリング**
- ✅ **美しいHTMLフロントエンド**
- ✅ タグ機能（カンマ区切り）
- ✅ 自動タイムスタンプ
- ✅ SQLiteデータベースで永続化

## 🛠 技術スタック

- **Python** 3.11
- **Flask** - Webフレームワーク
- **SQLite** - データベース
- **HTML/CSS/JavaScript** - フロントエンド

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

### ブラウザでアクセス
```
http://localhost:5004/
```

綺麗なWebインターフェースが表示されます！

## 🎨 Webインターフェース

### 特徴

- グラデーション背景
- リアルタイム検索
- タグフィルタリング
- レスポンシブデザイン

### 使い方

1. **検索窓**にキーワードを入力（タイトル・内容から検索）
2. **タグ入力窓**にタグを入力（タグで絞り込み）
3. **🔍 検索ボタン**をクリック
4. **📋 全て表示ボタン**で全メモを表示

## 📝 API エンドポイント

### 1. ホームページ（HTML）
```bash
GET /
```

Webインターフェースを表示

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

### 3. メモ一覧を取得（検索・フィルタリング対応）
```bash
GET /memos?search={keyword}&tag={tag}
```

**クエリパラメータ**：
- `search`: タイトルまたは内容で検索
- `tag`: タグで絞り込み

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
# 全メモを取得
curl http://localhost:5004/memos

# タイトル・内容で検索
curl "http://localhost:5004/memos?search=買い物"

# タグで絞り込み
curl "http://localhost:5004/memos?tag=仕事"

# 検索とタグを組み合わせ
curl "http://localhost:5004/memos?search=会議&tag=重要"
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

### シナリオ1：Webインターフェースで管理

1. ブラウザで `http://localhost:5004/` を開く
2. メモが一覧表示される
3. 検索窓に「買い物」と入力して検索
4. 買い物関連のメモだけが表示される

---

### シナリオ2：タグで整理
```bash
# 仕事メモを作成
curl -X POST http://localhost:5004/memos \
  -H "Content-Type: application/json" \
  -d '{"title": "会議メモ", "content": "プロジェクトの進捗", "tags": "仕事,重要"}'

# プライベートメモを作成
curl -X POST http://localhost:5004/memos \
  -H "Content-Type: application/json" \
  -d '{"title": "旅行プラン", "content": "京都旅行", "tags": "プライベート,旅行"}'

# 仕事のメモだけ表示
curl "http://localhost:5004/memos?tag=仕事"
```

---

### シナリオ3：検索機能
```bash
# 「会議」を含むメモを検索
curl "http://localhost:5004/memos?search=会議"

# 「重要」タグで絞り込み
curl "http://localhost:5004/memos?tag=重要"
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
├── templates/
│   └── index.html        # Webインターフェース
├── memos.db              # SQLiteデータベース（自動生成）
├── .gitignore
└── README.md
```

## 🎓 学習内容

このプロジェクトを通じて学んだこと：

- FlaskでのCRUD API実装
- SQLiteデータベース操作（INSERT, SELECT, UPDATE, DELETE）
- REST APIの設計原則
- **検索機能の実装（LIKE句）**
- **クエリパラメータの処理**
- **動的SQL構築**
- HTMLフロントエンドとAPIの連携
- JavaScriptでのfetch API使用
- レスポンシブデザイン
- エラーハンドリング
- タプルの正しい使い方

## ⚙️ 検索機能の仕組み

### タイトル・内容検索
```sql
SELECT * FROM memos 
WHERE title LIKE '%キーワード%' 
   OR content LIKE '%キーワード%'
```

### タグ検索
```sql
SELECT * FROM memos 
WHERE tags LIKE '%タグ%'
```

### 組み合わせ検索
```sql
SELECT * FROM memos 
WHERE (title LIKE '%キーワード%' OR content LIKE '%キーワード%')
  AND tags LIKE '%タグ%'
```

## 🔜 今後の改善予定

- [ ] 日付範囲でのフィルタリング
- [ ] ページネーション（大量のメモ対応）
- [ ] ソート機能（日付順、タイトル順）
- [ ] メモの編集機能（Webインターフェース）
- [ ] メモの削除機能（Webインターフェース）
- [ ] メモ作成機能（Webインターフェース）
- [ ] ユーザー認証
- [ ] 画像添付機能
- [ ] マークダウン対応
- [ ] エクスポート機能（CSV、JSON）

## ⚠️ 注意事項

- このプロジェクトは学習目的です
- 本番環境で使用する場合は、以下の対策を追加してください：
  - ユーザー認証
  - 入力バリデーション強化
  - XSS対策
  - SQLインジェクション対策（現在はプレースホルダーで対応済み）
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
