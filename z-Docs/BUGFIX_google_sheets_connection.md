# Bugfix: Google Sheets Connection & Header Errors

**Date:** 2025-12-28
**Issue:** `gspread.exceptions.SpreadsheetNotFound: <Response [200]>` and `gspread.exceptions.GSpreadException: the header row in the worksheet contains duplicates`.

## Problem Description
1.  **Connection Error**: The initial script failed to connect to the Google Sheet, returning a generic `<Response [200]>` error. This was misleading (200 usually means OK), but in `gspread` it often indicates a permisson or "not found" issue where the API returns a success page (HTML) instead of JSON data.
2.  **Header Error**: After fixing the connection, the script crashed because `get_all_records()` strictly requires unique, non-empty headers, which the target sheet lacked.

## Diagnosis Steps
1.  Verified `credentials.json` existed.
2.  Created a debug script `debug_sheets.py` to isolate the connection logic and print full tracebacks.
3.  Used `client.openall()` to list all sheets visible to the service account.
    *   **Result**: Found `PedroDugadugaFamily` instead of the expected `Family Tree`.
4.  Updated script to use the correct name, then encountered the duplicate header error.

## Solution

### 1. Fix Sheet Name
Updated `SHEET_NAME` variable to match the actual file name found in the service account's drive.

### 2. Robust Data Loading
Switched from `get_all_records()` (strict) to `get_all_values()` (raw data), cleaning it manually in Python.

**Code Snippet (Before):**
```python
# Fails on duplicate/empty headers
data = worksheet.get_all_records()
df = pd.DataFrame(data)
```

**Code Snippet (After):**
```python
# Robust to messy headers
data = worksheet.get_all_values()
headers = data.pop(0)  # Use first row as headers
df = pd.DataFrame(data, columns=headers)
```

## Terminal Commands Used
```bash
# Debugging
uv run debug_sheets.py
```
