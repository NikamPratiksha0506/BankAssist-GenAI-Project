import sqlite3
from datetime import datetime, timedelta
import random

# Connect to SQLite database (creates portfolio.db if it doesn't exist)
conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

# Create clients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    risk_profile TEXT,
    portfolio_value REAL
)
""")

# Create investments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS investments (
    investment_id INTEGER PRIMARY KEY,
    client_id INTEGER,
    fund_name TEXT,
    amount_invested REAL,
    date TEXT,
    FOREIGN KEY(client_id) REFERENCES clients(client_id)
)
""")

# Insert 30 sample clients
risk_profiles = ["Low", "Medium", "High"]
for i in range(1, 31):
    cursor.execute("""
    INSERT INTO clients (name, age, risk_profile, portfolio_value)
    VALUES (?, ?, ?, ?)
    """, (
        f"Client_{i}",
        random.randint(25, 65),
        random.choice(risk_profiles),
        random.randint(100000, 1000000)
    ))

# Insert 1-5 investments per client
fund_names = ["Equity Fund", "Bond Fund", "Mutual Fund", "ETF"]
for i in range(1, 31):
    for j in range(random.randint(1, 5)):
        cursor.execute("""
        INSERT INTO investments (client_id, fund_name, amount_invested, date)
        VALUES (?, ?, ?, ?)
        """, (
            i,
            random.choice(fund_names),
            random.randint(50000, 300000),
            (datetime.today() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
        ))

conn.commit()
conn.close()

print("✅ portfolio.db created and populated successfully!")
