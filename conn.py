import sqlite3

conn = sqlite3.connect("dictionary.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS english (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  word TEXT NOT NULL,
  definition TEXT NOT NULL
)
""")

conn.commit()
conn.close()