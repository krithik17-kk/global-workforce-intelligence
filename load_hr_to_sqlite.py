import pandas as pd
import sqlite3
import os

# Mapping CSV filenames to country names
files = {
    "employees_india.csv": "India",
    "employees_us.csv": "US",
    "employees_uk.csv": "UK",
    "employees_germany.csv": "Germany"
}

# Connect to SQLite database (creates file if it doesn’t exist)
conn = sqlite3.connect("hr_data.db")
all_data = []

# Loop through each CSV and add a 'country' column
for file, country in files.items():
    file_path = os.path.join("data", "raw", file)  # Updated path
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df["country"] = country
        all_data.append(df)
        print(f"✅ Loaded {file}")
    else:
        print(f"❌ File not found: {file_path}")

# Combine all data and load into 'employees' table
if all_data:
    full_df = pd.concat(all_data)
    full_df.to_sql("employees", conn, if_exists="replace", index=False)
    print("🎯 All employee data loaded into SQLite as table 'employees'")
else:
    print("⚠️ No data loaded. Please check file paths.")

conn.close()
