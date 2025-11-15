from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# データベース初期化
def init_db():
    """データベースを初期化"""
    conn = sqlite3.connect('memos.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS memos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

@app.route('/')
def home():
    """ホームページ"""
    return render_template('index.html')

@app.route('/memos', methods=['POST'])
def create_memo():
    """メモを作成"""
    data = request.get_json()

    if not data or 'title' not in data or 'content' not in data:
        return jsonify({"error": "タイトルと内容が必要です"}), 400
    
    title = data['title']
    content = data['content']
    tags = data.get('tags', '')
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('memos.db')
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO memos (title, content, tags, created_at, updated_at) VALUES (?, ?, ?, ?, ?)',
        (title, content, tags, now, now)
    )

    memo_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return jsonify({
        "id": memo_id,
        "title": title,
        "content": content,
        "tags": tags,
        "created_at": now
    }), 201

@app.route('/memos', methods=['GET'])
def get_memos():
    """メモ一覧を取得（検索・フィルタリング対応）"""
    # クエリパラメータを取得
    search = request.args.get('search', '')
    tag = request.args.get('tag', '')

    conn = sqlite3.connect('memos.db')
    cursor = conn.cursor()

    query = 'SELECT id, title, content, tags, created_at, updated_at FROM memos WHERE 1=1'
    params = []

    # 検索条件を追加
    if search:
        query += ' AND (title LIKE ? OR content LIKE ?)'
        params.extend([f'%{search}%', f'%{search}%'])

    if tag:
        query += ' AND tags LIKE ?'
        params.append(f'%{tag}%')

    query += ' ORDER BY created_at DESC'

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    memos = []
    for row in rows:
        memos.append({
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "tags": row[3],
            "created_at": row[4],
            "updated_at": row[5]
        })

    return jsonify({"memos": memos, "count": len(memos)})

@app.route('/memos/<int:memo_id>', methods=['GET'])
def get_memo(memo_id):
    """個別メモを取得"""
    conn = sqlite3.connect('memos.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, title, content, tags, created_at, updated_at FROM memos WHERE id = ?', (memo_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "tags": row[3],
            "created_at": row[4],
            "updated_at": row[5]
        })
    else:
        return jsonify({"error": "メモが見つかりません"}), 404
    
@app.route('/memos/<int:memo_id>', methods=['PUT'])
def update_memo(memo_id):
    """メモを更新"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "更新データが必要です"}), 400
    
    title = data.get('title')
    content = data.get('content')
    tags = data.get('tags')
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('memos.db')
    cursor = conn.cursor()

    # 既存のメモを確認
    cursor.execute('SELECT * FROM memos WHERE id = ?', (memo_id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"error": "メモが見つかりません"}), 404
    
    # 更新
    if title:
        cursor.execute('UPDATE memos SET title = ?, updated_at = ? WHERE id = ?', (title, now, memo_id))
    if content:
        cursor.execute('UPDATE memos SET content = ?, updated_at = ? WHERE id = ?', (content, now, memo_id))
    if tags is not None:
        cursor.execute('UPDATE memos SET tags = ?, updated_at = ? WHERE id = ?', (tags, now, memo_id))

    conn.commit()
    conn.close()

    return jsonify({"message": "メモを更新しました", "id": memo_id})

@app.route('/memos/<int:memo_id>', methods=['DELETE'])
def delete_memo(memo_id):
    """メモを削除"""
    conn = sqlite3.connect('memos.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM memos WHERE id = ?', (memo_id,))

    if cursor.rowcount > 0:
        conn.commit()
        conn.close()
        return jsonify({"message": "メモを削除しました"})
    else:
        conn.close()
        return jsonify({"error": "メモが見つかりません"}), 404


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5004, debug=True)


