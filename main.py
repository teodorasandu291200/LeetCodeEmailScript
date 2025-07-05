import requests
import smtplib
import json
from email.mime.text import MIMEText
import traceback

def load_config():
    with open("config.json") as f:
        return json.load(f)

def fetch_daily_problem():
    url = "https://leetcode.com/graphql"
    query = {
        "operationName": "questionOfToday",
        "query": """
            query questionOfToday {
              activeDailyCodingChallengeQuestion {
                date
                question {
                  title
                  titleSlug
                  difficulty
                  link: titleSlug
                }
              }
            }
        """,
        "variables": {}
    }

    response = requests.post(url, json=query)
    data = response.json()

    question = data['data']['activeDailyCodingChallengeQuestion']['question']
    date = data['data']['activeDailyCodingChallengeQuestion']['date']
    title = question['title']
    difficulty = question['difficulty']
    link = f"https://leetcode.com/problems/{question['titleSlug']}"

    return f"Date: {date}\nTitle: {title}\nDifficulty: {difficulty}\nLink: {link}"

def send_email(config, body):
    msg = MIMEText(body)
    msg['Subject'] = 'LeetCode Daily Problem'
    msg['From'] = config['email']
    msg['To'] = config['to_email']

    with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
        server.starttls()
        server.login('apikey', config['password'])
        server.sendmail(config['email'], config['to_email'], msg.as_string())
        print("Email sent!")

def main():
    config = load_config()
    body = fetch_daily_problem()
    send_email(config, body)
    print("✅ Email sent!")

def main_with_logging():
    try:
        main()
    except Exception:
        with open("error_log.txt", "a") as f:
            f.write(traceback.format_exc())
        print("Error occurred. Check error_log.txt")

if __name__ == "__main__":
    main_with_logging()
