import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import os

# ---------------------- Setup -----------------------
# Path to your downloaded JSON key file
SERVICE_ACCOUNT_FILE = "credentials.json"  # Make sure this file is in the same folder or update path

# Name of the Google Sheet you created
GOOGLE_SHEET_NAME = "HR_Analytics"

# CSV files and sheet tab names
files = {
    "employees_india.csv": "HR_India",
    "employees_us.csv": "HR_US",
    "employees_uk.csv": "HR_UK",
    "employees_germany.csv": "HR_Germany"
}

# --------------------- Auth -------------------------
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
client = gspread.authorize(creds)

# Open your main Google Sheet
spreadsheet = client.open(GOOGLE_SHEET_NAME)

# ------------------ Upload Loop ---------------------
for file, sheet_name in files.items():
    print(f"Uploading {file} → {sheet_name}...")
    df = pd.read_csv(f"data/raw/{file}")

    try:
        # Create or open the worksheet
        try:
            worksheet = spreadsheet.worksheet(sheet_name)
            worksheet.clear()  # Clear existing content
        except gspread.exceptions.WorksheetNotFound:
            worksheet = spreadsheet.add_worksheet(title=sheet_name, rows="1000", cols="20")

        # Write DataFrame to worksheet
        set_with_dataframe(worksheet, df)
        print(f"✅ Uploaded to sheet: {sheet_name}")
    except Exception as e:
        print(f"❌ Failed for {sheet_name}: {e}")

print("🎉 All HR data uploaded to Google Sheets!")
