import requests
from telegram import Bot
from telegram.ext import ApplicationBuilder, ContextTypes
import asyncio

# Telegram bot token and chat ID
TELEGRAM_TOKEN = "7487022753:AAFPHijXrk4EqTmNJxhHTT6MllmTHog5Ue8"
CHAT_ID = "922909522"

# Website URL to check
WEBSITE_URL = "https://expressedzshop.peasy.top/body-scale-03-ar.html?fbclid=IwY2xjawE9_jpleHRuA2FlbQIxMAABHWYS7AjEfQZkjSrNw7JKMIUyH436kXYh2HpzhrkaE9jX5_WFUmQivSW_oA_aem_qRttjfua-CNfRG5NGm6Yag"
def check_website(url):
    try:
        response = requests.get(url)
        print(f"Website response code: {response.status_code}")
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking website: {e}")
        return False

async def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(f"Message sent to Telegram: {message}")
    except requests.RequestException as e:
        print(f"Failed to send message to Telegram: {e}")

async def main():
    while True:
        print("Starting website status check...")
        website_status = check_website(WEBSITE_URL)  # No 'await' here
        if not website_status:  # Send message only if the site is down
            message = f"Alert: The website {WEBSITE_URL} is down!"
            print(f"Sending message: {message}")
            await send_telegram_message(TELEGRAM_TOKEN, CHAT_ID, message)
        else:
            print(f"The website {WEBSITE_URL} is up.")
        
        await asyncio.sleep(900)  # Wait for 2 minutes before checking again

if __name__ == "__main__":
    asyncio.run(main())
