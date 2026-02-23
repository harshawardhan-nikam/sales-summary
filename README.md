# 📊 Sales Summary Using SQLite & Python

## 📌 Project Overview
This project demonstrates how to use SQL inside Python to extract and summarize sales data from a SQLite database. The analysis calculates total quantity sold and total revenue per product and visualizes the results using a bar chart.

---

## 🎯 Objective
- Connect to a SQLite database using Python
- Execute SQL queries to summarize sales data
- Display results using Python print statements
- Visualize revenue using a bar chart

---

## 🛠 Tools & Technologies
- Python
- SQLite (sqlite3)
- Pandas
- Matplotlib
- Visual Studio Code / Jupyter Notebook

---

## 📂 Database
A small SQLite database file:

contains one table:

### 🗄 Table: `sales`

| Column | Description |
|--------|------------|
| id | Unique record ID |
| product | Product name |
| quantity | Quantity sold |
| price | Price per unit |

---

## 🔍 SQL Query Used

sql
SELECT 
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;


📈 Visualization

A bar chart is generated showing:

Product vs Revenue

The chart is saved as:"C:\Users\Harshawardhan\OneDrive\Pictures\Screenshots\Screenshot 2026-02-23 210031.png"

👤 Author
Harsh Nikam
