import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("hr_data.db")

# Load data from the 'employees' table
df = pd.read_sql_query("SELECT * FROM employees", conn)

# Export to CSV
df.to_csv("employees.csv", index=False)

print("✅ Exported employees table to employees.csv")

# Close the connection
conn.close()

