# createdb.py
import sqlite3

DB_PATH = "portfolio.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Drop table if exists (for re-runs)
cursor.execute("DROP TABLE IF EXISTS clients;")

cursor.execute("""
CREATE TABLE clients (
    id INTEGER PRIMARY KEY,
    name TEXT,
    portfolio_value INTEGER,
    investments INTEGER,
    risk_profile TEXT
)
""")

sample_data = [
    (1, 'Alice', 600000, 250000, 'High'),
    (2, 'Bob', 450000, 150000, 'Medium'),
    (3, 'Charlie', 750000, 300000, 'High'),
    (4, 'Diana', 500000, 200000, 'Low'),
    (5, 'Eve', 300000, 100000, 'Low')
]

cursor.executemany("INSERT INTO clients VALUES (?, ?, ?, ?, ?)", sample_data)
conn.commit()
conn.close()
print("✅ portfolio.db created and populated successfully!")
