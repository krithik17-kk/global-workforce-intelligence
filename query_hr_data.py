import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("hr_data.db")

# Example 1: Total Employees by Country
query1 = """
SELECT country, COUNT(*) AS total_employees
FROM employees
GROUP BY country
ORDER BY total_employees DESC;
"""

df1 = pd.read_sql_query(query1, conn)
print("👥 Total Employees by Country")
print(df1)
print("\n" + "-"*50 + "\n")

# Example 2: Average Salary by Department & Country
query2 = """
SELECT dept, country, ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY dept, country
ORDER BY avg_salary DESC;
"""

df2 = pd.read_sql_query(query2, conn)
print("💰 Avg Salary by Department & Country")
print(df2)

# Close connection
conn.close()

