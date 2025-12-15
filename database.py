import sqlite3

conn = sqlite3.connect("sentiment.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    sentiment TEXT
)
""")

conn.commit()
conn.close()
