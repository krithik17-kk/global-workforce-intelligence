import sqlite3

conn = sqlite3.connect("hr_data.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(employees);")
columns = cursor.fetchall()

print("📌 Columns in 'employees' table:")
for col in columns:
    print(col[1])

conn.close()
