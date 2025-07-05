# LeetCode Daily Email Script

This Python script fetches the daily LeetCode coding challenge and emails it to your personal email using SMTP.

---

## Features

- Fetches daily problem via LeetCode’s GraphQL API  
- Sends email with problem details  
- Configurable via `config.json`  
- Supports running locally and scheduling daily via Windows Task Scheduler  

---

## Setup Instructions


# 1. Clone the Repository

```bash

git clone git@github.com:teodorasandu291200/LeetCodeEmailScript.git
cd LeetCodeEmailScript
```

# 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate     # Windows
source venv/bin/activate    # macOS/Linux
```

# 3. Install dependencies

```bash
pip install -r requirements.txt
```

# 4. Setup SendGrid free(tier) account
SendGrid is a popular free-tier SMTP service. Here's how to set it up:
```bash
1️⃣ Sign up for a free SendGrid account.
2️⃣ Go to Sender Authentication.
3️⃣ Choose Single Sender Verification.
4️⃣ Add your email address (e.g. yourname@gmail.com).
5️⃣ Verify it by clicking the link in the email they send you.
6️⃣ Go to Settings > API Keys.
7️⃣ Create an API key (e.g. "LeetCodeEmailScript").
```

# 5. Create config.json in root folder:
```bash
{
  "smtp_server": "smtp.sendgrid.net",
  "smtp_port": 587,
  "email": "your_verified_sender_email@example.com",
  "password": "your_smtp_password_or_api_key",
  "to_email": "your_personal_email@example.com"
}
```

# 6. Create .bat for task scheduler automation

```bash
a. Create run_script.bat in root folder
b. Paste this content into it:
@echo off
REM Change this to your project folder path
cd /d C:\Users\YOUR_USERNAME\Path\To\LeetCodeEmailScript

REM Activate your virtual environment
call venv\Scripts\activate.bat

REM Run the script
python main.py
```

# 7. Create .bat for task scheduler automation
```bash
Open Task Scheduler (press Win + R, type taskschd.msc, hit Enter).
Click Create Basic Task… on the right.
Name it (e.g. LeetCode Daily Email), click Next.
Choose Daily. Set the time you want it to run.
Action: choose Start a program.
Browse and select your run_script.bat file.
Click Finish.
```