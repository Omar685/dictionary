CREATE TABLE IF NOT EXISTS terms (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  word TEXT NOT NULL,
  definition TEXT NOT NULL
)
CREATE TABLE IF NOT EXISTS english (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  word TEXT NOT NULL,
  definition TEXT NOT NULL
)