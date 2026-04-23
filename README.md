
---

# Job Application Tracker using Gmail API

An automated Python-based system that tracks job applications sent via Gmail and logs them into an Excel file. Supports multiple Gmail accounts and helps monitor application activity efficiently.

---

## Features

* Automatically reads sent emails from Gmail
* Detects job application emails using keywords
* Extracts:

  * Company name
  * Email ID
  * Job role
  * Date
* Supports multiple Gmail accounts
* Avoids duplicate entries
* Stores data in Excel for analysis
* Decodes encoded email subjects

---

## Tech Stack

* Python
* Gmail API
* Pandas
* OpenPyXL

---

## Project Structure

```bash
job-tracker/
│
├── tracker.py
├── credentials_acc1.json
├── credentials_acc2.json
├── token_acc1.json (auto-generated)
├── token_acc2.json (auto-generated)
├── job_tracker.xlsx (auto-generated)
└── README.md
```

---

## Step-by-Step Setup Guide

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/job-tracker.git
cd job-tracker
```

---

### Step 2: Install Dependencies

```bash
pip install pandas google-api-python-client google-auth-httplib2 google-auth-oauthlib openpyxl
```

---

### Step 3: Setup Google Cloud Project

1. Go to Google Cloud Console
2. Create a new project
3. Enable Gmail API
4. Go to “APIs & Services” → “Credentials”
5. Create OAuth Client ID
6. Select “Desktop App”
7. Download credentials file

---

### Step 4: Configure OAuth Consent Screen

1. Go to OAuth Consent Screen
2. Select “External”
3. Fill basic details
4. Add your Gmail under “Test Users”
5. Keep status as Testing

---

### Step 5: Add Credentials

Rename and place credentials in project folder:

```bash
credentials_acc1.json
credentials_acc2.json
```

---

### Step 6: Run the Script

```bash
python tracker.py
```

First run:

* Browser will open
* Login with Gmail account
* Click Advanced → Continue

Repeat for second account.

---

### Step 7: Output

After running, a file will be created:

```bash
job_tracker.xlsx
```

It contains:

| Company | Email | Role | Date | Status |
| ------- | ----- | ---- | ---- | ------ |

---

## How It Works

1. Connects to Gmail using Gmail API
2. Reads sent emails
3. Filters job-related emails using keywords
4. Extracts relevant details
5. Saves structured data into Excel
6. Prevents duplicate entries

---

## Supported Keywords

```python
application, applying, resume, cv, internship, data analyst, data science
```

You can customize these in the script.

---

## Common Errors & Fixes

### Error: access_denied (403)

* Add your email as Test User in OAuth Consent Screen
* Delete token.json and rerun

---

### Error: Gmail API not enabled

* Enable Gmail API in Google Cloud Console

---

### Error: openpyxl version issue

```bash
pip install --upgrade openpyxl
```

---

### Encoded Email Subjects

Handled using email header decoding in script.

---

## Future Improvements

* Detect interview and rejection emails
* Add follow-up reminders
* Build Power BI dashboard
* AI-based company extraction
* Real-time tracking using scheduler

---

## Use Case

This project helps job seekers:

* Track all applications automatically
* Avoid manual Excel updates
* Analyze job search performance
* Improve follow-up strategy

---

## Author

Kaustubh Narayankar
Data Science & Data Analytics Enthusiast

---

## License

This project is open-source and free to use for learning purposes.

---

If you want, I can next help you:

* write a strong GitHub description + tags
* create a LinkedIn post for this project
* prepare interview explanation for this project

Just tell me 👍
