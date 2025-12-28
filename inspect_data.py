import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Configuration
SERVICE_ACCOUNT_FILE = 'credentials.json'
SHEET_NAME = 'PedroDugadugaFamily'
WORKSHEET_INDEX = 0

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

try:
    print("Connecting...")
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME)
    worksheet = sheet.get_worksheet(WORKSHEET_INDEX)
    
    print("Fetching values...")
    data = worksheet.get_all_values()
    
    # helper to print clearly
    print("\n--- RAW DATA (First 15 Rows) ---")
    for i, row in enumerate(data[:15]):
        print(f"Row {i}: {row}")

    print("\n--- Possible Header candidates ---")
    print(f"Row 0: {data[0]}")
    
except Exception as e:
    print(e)
