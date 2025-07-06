import os
import requests

def send_slack_alert(message):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("⚠️ SLACK_WEBHOOK_URL not set, skipping Slack alert.")
        return
    payload = {"text": message}
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("✅ Slack alert sent successfully.")
        else:
            print(f"⚠️ Slack alert failed: {response.status_code} {response.text}")
    except Exception as e:
        print(f"⚠️ Slack alert exception: {e}")