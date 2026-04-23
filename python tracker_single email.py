import os
import base64
import pandas as pd
from email import message_from_bytes
from email.utils import parsedate_to_datetime

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


# ---------------- AUTH ----------------
def authenticate():
    creds = None
    if os.path.exists('YOUR_token.json'):
        creds = Credentials.from_authorized_user_file('YOUR_token.json', SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'YOUR_credentials_FILE.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open('YOUR_token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


# ---------------- FETCH EMAILS ----------------
def get_sent_emails(service):
    results = service.users().messages().list(
        userId='me',
        labelIds=['SENT'],
        maxResults=100   # increased
    ).execute()

    return results.get('messages', [])


# ---------------- EXTRACT EMAIL ----------------
def extract_email_data(service, msg_id):
    msg = service.users().messages().get(
        userId='me',
        id=msg_id,
        format='raw'
    ).execute()

    raw_msg = base64.urlsafe_b64decode(msg['raw'])
    mime_msg = message_from_bytes(raw_msg)

    subject = mime_msg['subject']
    to = mime_msg['to']
    date = mime_msg['date']

    return subject, to, date


# ---------------- FILTER ----------------
def is_job_application(subject):
    keywords = [
        'application',
        'applying',
        'resume',
        'cv',
        'internship',
        'data analyst',
        'data science'
    ]
    return any(word in subject.lower() for word in keywords)


# ---------------- CLEAN ROLE ----------------
def clean_role(subject):
    if subject:
        return subject.replace("Application for", "").strip()
    return ""


# ---------------- EXTRACT COMPANY ----------------
def extract_company(email):
    try:
        return email.split('@')[-1].split('.')[0]
    except:
        return email


# ---------------- MAIN ----------------
def main():
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)

    messages = get_sent_emails(service)

    data = []

    for msg in messages:
        subject, to, date = extract_email_data(service, msg['id'])

        # DEBUG PRINT (optional)
        print(subject, "|", to)

        if subject and is_job_application(subject):
            try:
                formatted_date = parsedate_to_datetime(date).strftime("%Y-%m-%d")
            except:
                formatted_date = date

            data.append({
                "Company": extract_company(to),
                "Email": to,
                "Role": clean_role(subject),
                "Date": formatted_date,
                "Status": "Applied"
            })

    df = pd.DataFrame(data)

    file = "job_tracker.xlsx"

    if os.path.exists(file):
        existing = pd.read_excel(file)
        df = pd.concat([existing, df]).drop_duplicates(
            subset=["Company", "Role"]
        )

    df.to_excel(file, index=False)

    print("\nTracker updated successfully!")


if __name__ == "__main__":
    main()