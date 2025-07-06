# bot/alerts/telegram.py

import requests
import os

# Securely fetch from environment, fallback to hardcoded for dev
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "7359752723:AAFcF8B233U66aMacYw-Gqs6t48nItE4SdA")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "-4868580944")

def send_telegram_message(message: str):
    """Send a plain text message to your Telegram group."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Telegram alert sent successfully.")
        else:
            print(f"⚠️ Telegram alert failed. Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"⚠️ Telegram alert exception: {e}")