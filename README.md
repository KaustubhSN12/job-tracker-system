<div align="center">

# 📬 Job Application Tracker
### Automated Gmail-based job tracking — straight to Excel

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Gmail API](https://img.shields.io/badge/Gmail%20API-enabled-EA4335?style=flat-square&logo=gmail&logoColor=white)](https://developers.google.com/gmail/api)
[![License](https://img.shields.io/badge/License-Open%20Source-brightgreen?style=flat-square)](#license)

> Stop manually tracking job applications. This tool reads your Gmail, detects application emails, and logs everything into a clean Excel sheet — automatically.

</div>

---

## 🚀 What It Does

| Feature | Description |
|--------|-------------|
| 📥 Auto-reads Gmail | Scans your Sent folder for job-related emails |
| 🏢 Extracts details | Company name, email ID, job role, and date |
| 📊 Logs to Excel | Saves everything in a structured `job_tracker.xlsx` |
| 👥 Multi-account | Supports multiple Gmail accounts simultaneously |
| 🔁 No duplicates | Smart deduplication on every run |
| 🔍 Keyword detection | Filters emails using customizable keywords |

---

## 🗂️ Project Structure

```
job-tracker/
├── tracker.py                  ← Main script
├── credentials_acc1.json       ← OAuth credentials (Account 1)
├── credentials_acc2.json       ← OAuth credentials (Account 2)
├── token_acc1.json             ← Auto-generated on first run
├── token_acc2.json             ← Auto-generated on first run
├── job_tracker.xlsx            ← Auto-generated output
└── README.md
```

---

## ⚙️ Setup Guide

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/job-tracker.git
cd job-tracker
```

---

### Step 2 — Install Dependencies

```bash
pip install pandas google-api-python-client google-auth-httplib2 google-auth-oauthlib openpyxl
```

---

### Step 3 — Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a **new project**
3. Enable the **Gmail API** (`APIs & Services → Library → Gmail API`)
4. Go to `APIs & Services → Credentials`
5. Click **Create Credentials → OAuth Client ID**
6. Select **Desktop App**
7. Download the credentials JSON file

---

### Step 4 — Configure OAuth Consent Screen

1. Go to `APIs & Services → OAuth Consent Screen`
2. Select **External**
3. Fill in basic app details
4. Add your Gmail address under **Test Users**
5. Keep status as **Testing**

> ⚠️ You must add your own email as a Test User, or you'll get a 403 error.

---

### Step 5 — Add Credentials to Project

Rename your downloaded files and place them in the project folder:

```
credentials_acc1.json   ← for your first Gmail account
credentials_acc2.json   ← for your second Gmail account (optional)
```

---

### Step 6 — Run the Script

```bash
python tracker.py
```

On **first run**, a browser window will open. Log in to your Gmail and click:
`Advanced → Go to App → Allow`

Repeat this for each account. Tokens are saved automatically for future runs.

---

### Step 7 — View Your Output

A file called `job_tracker.xlsx` is created in the project folder:

| Company | Email | Role | Date | Status |
|---------|-------|------|------|--------|
| Google | hr@google.com | Data Analyst | 2024-01-10 | Applied |
| Infosys | careers@infosys.com | Data Science Intern | 2024-01-12 | Applied |

---

## 🧠 How It Works

```
Gmail (Sent Folder)
        ↓
  Keyword Matching
        ↓
  Detail Extraction
  (Company / Role / Date / Email)
        ↓
  Duplicate Check
        ↓
  Excel Output (job_tracker.xlsx)
```

---

## 🔑 Supported Keywords

The script detects emails containing any of these keywords:

```python
["application", "applying", "resume", "cv", "internship", "data analyst", "data science"]
```

> 💡 You can edit this list directly in `tracker.py` to match your field.

---

## 🐛 Troubleshooting

### `access_denied` (Error 403)
- Go to OAuth Consent Screen → Add your email under **Test Users**
- Delete `token_acc1.json` and rerun the script

### Gmail API not enabled
- In Google Cloud Console: `APIs & Services → Library → search "Gmail API" → Enable`

### openpyxl version issue
```bash
pip install --upgrade openpyxl
```

### Encoded/garbled email subjects
- Already handled — the script decodes encoded email headers automatically.

---

## 🔮 Upcoming Features

- [ ] Detect interview invites and rejection emails
- [ ] Follow-up reminder system
- [ ] Power BI / Google Data Studio dashboard
- [ ] AI-powered company name extraction
- [ ] Real-time tracking with a scheduler (e.g., cron / APScheduler)

---

## 🛠️ Tech Stack

- **Python** — Core scripting
- **Gmail API** — Email access via OAuth 2.0
- **Pandas** — Data processing and deduplication
- **OpenPyXL** — Excel file generation

---

## 👤 Author

**Kaustubh Narayankar**  
Data Science & Analytics Enthusiast

---

## 📄 License

Open-source and free to use for personal and learning purposes.
