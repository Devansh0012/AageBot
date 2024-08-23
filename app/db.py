import sqlite3

def init_db():
    conn = sqlite3.connect('user_links.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UserLink (
            id TEXT PRIMARY KEY,
            telegram_user_id INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
