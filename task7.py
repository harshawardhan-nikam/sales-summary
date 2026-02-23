import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect database
conn = sqlite3.connect("sales_data.db")

# SQL query
query = """
SELECT 
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# Load data into pandas
df = pd.read_sql_query(query, conn)

# Print results
print("\nSales Summary:\n")
print(df)

# Plot bar chart
df.plot(kind='bar', x='product', y='revenue')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.savefig("sales_chart.png")
plt.show()

conn.close()