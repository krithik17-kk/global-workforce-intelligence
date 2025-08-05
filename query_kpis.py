import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("hr_data.db")

# ----------- 1. Attrition Rate by Country -----------
query1 = """
SELECT 
    country,
    ROUND(100.0 * SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS attrition_rate_pct
FROM employees
GROUP BY country
ORDER BY attrition_rate_pct DESC;
"""
df1 = pd.read_sql_query(query1, conn)
print("📉 Attrition Rate by Country")
print(df1)
print("\n" + "-"*60 + "\n")

# ----------- 2. Average Absenteeism by Dept & Country -----------
query2 = """
SELECT 
    dept,
    country,
    ROUND(AVG(absenteeism_days), 1) AS avg_absenteeism_days
FROM employees
GROUP BY dept, country
ORDER BY avg_absenteeism_days DESC;
"""
df2 = pd.read_sql_query(query2, conn)
print("🕒 Average Absenteeism by Dept & Country")
print(df2)
print("\n" + "-"*60 + "\n")

# ----------- 3. Engagement Score by Country -----------
query3 = """
SELECT 
    country,
    ROUND(AVG(engagement), 2) AS avg_engagement
FROM employees
GROUP BY country
ORDER BY avg_engagement DESC;
"""
df3 = pd.read_sql_query(query3, conn)
print("🔥 Avg Engagement Score by Country")
print(df3)
print("\n" + "-"*60 + "\n")

# ----------- 4. Performance Score Distribution -----------
query4 = """
SELECT 
    perf_score,
    COUNT(*) AS num_employees
FROM employees
GROUP BY perf_score
ORDER BY perf_score DESC;
"""
df4 = pd.read_sql_query(query4, conn)
print("⭐ Performance Score Distribution")
print(df4)
print("\n" + "-"*60 + "\n")

# ----------- 5. Average Salary by Department -----------
query5 = """
SELECT 
    dept,
    ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY dept
ORDER BY avg_salary DESC;
"""
df5 = pd.read_sql_query(query5, conn)
print("💰 Average Salary by Department")
print(df5)

# Close DB connection
conn.close()
