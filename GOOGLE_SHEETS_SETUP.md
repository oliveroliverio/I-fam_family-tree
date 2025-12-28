# Google Sheets API Setup Guide

Follow these steps to obtain your `credentials.json` file for the Google Sheets EDA notebook.

## 1. Create a Project
1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  In the top-left, click the project dropdown (it might say "My First Project" or "Select a project").
3.  Click **"New Project"**.
4.  Name it something like `Family Tree EDA` and click **Create**.
5.  Wait for the notification that the project is created, then click **"Select Project"**.

## 2. Enable APIs
You need to enable both the Sheets API and Drive API.

1.  Open the **Navigation Menu** (three lines in top-left) > **APIs & Services** > **Enabled APIs & services**.
2.  Click **"+ ENABLE APIS AND SERVICES"** at the top.
3.  Search for **"Google Sheets API"**.
4.  Click on it and click **Enable**.
5.  Go back to the API Library (arrow back or search again).
6.  Search for **"Google Drive API"**.
7.  Click on it and click **Enable**.

## 3. Create a Service Account
1.  Go to **Navigation Menu** > **IAM & Admin** > **Service Accounts**.
2.  Click **"+ CREATE SERVICE ACCOUNT"** (near the top).
3.  **Step 1**: Enter a name (e.g., `sheets-editor`). Click **Create and Continue**.
4.  **Step 2**: Grant this service account access to project.
    *   Role: Select **Basic** > **Editor** (this is easiest for personal projects).
    *   Click **Continue**.
5.  **Step 3**: Optional, just click **Done**.

## 4. Create JSON Key
1.  You should now see your service account in the list (e.g., `sheets-editor@family-tree-eda...`).
2.  Click on the **Email address** link for that account.
3.  Go to the **"Keys"** tab (top menu bar of the details page).
4.  Click **"Add Key"** > **"Create new key"**.
5.  Select **JSON** and click **Create**.
6.  The file will automatically download to your computer.

## 5. Setup for Notebook
1.  **Rename**: Rename the downloaded file to `credentials.json`.
2.  **Move**: Move `credentials.json` to the root folder of this project: `/Users/mbp-14/Downloads/CLONED/I-fam_family-tree/`.
3.  **Share**: Open the `credentials.json` file (in a text editor) and find the `"client_email"` field. Copy that email address (e.g., `sheets-editor@...`).
4.  **Go to your Google Sheet** in your browser.
5.  Click **Share** (top right).
6.  Paste the service account email and ensure it has **Editor** access.
7.  Click **Send**.

Now you are ready to run the `google_sheets_eda.ipynb` notebook!
