import traceback
import gspread
from google.oauth2.service_account import Credentials

# Configuration
SERVICE_ACCOUNT_FILE = './credentials.json'
SHEET_NAME = 'PedroDugadugaFamily'
WORKSHEET_INDEX = 0

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

print("Starting debug script...")
try:
    print(f"Loading credentials from {SERVICE_ACCOUNT_FILE}...")
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    print("Authorizing client...")
    client = gspread.authorize(creds)
    
    print("Listing all available spreadsheets...")
    files = client.openall()
    print(f"Found {len(files)} spreadsheets:")
    for f in files:
        print(f" - '{f.title}' (ID: {f.id})")

    print(f"Attempting to open specific sheet: '{SHEET_NAME}'...")
    sheet = client.open(SHEET_NAME)
    
    print("Selecting worksheet...")
    worksheet = sheet.get_worksheet(WORKSHEET_INDEX)
    
    print(f"Successfully connected to: {sheet.title}")
    
    data = worksheet.get_all_records()
    print(f"Retrieved {len(data)} records.")

except Exception:
    print("\n!!! EXCEPTION OCCURRED !!!\n")
    traceback.print_exc()
