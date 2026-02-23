import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data
data = [
    ("Laptop", 5, 60000),
    ("Mouse", 20, 500),
    ("Keyboard", 15, 1200),
    ("Monitor", 7, 15000),
    ("Headphones", 10, 2000)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", data)

conn.commit()
conn.close()

print("Database created successfully!")