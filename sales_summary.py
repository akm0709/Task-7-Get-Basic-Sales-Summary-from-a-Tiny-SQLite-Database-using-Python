import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the database
conn = sqlite3.connect('sales_data.db')

# Step 2: Run SQL query
query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)
conn.close()

# Step 3: Print and plot results
print("Sales Summary:\n", df)

# Bar chart
df.plot(kind='bar', x='product', y='revenue', title='Revenue by Product', legend=False, color='skyblue')
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()