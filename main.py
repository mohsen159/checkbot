import requests
from telegram import Bot
from telegram.ext import ApplicationBuilder, ContextTypes
import asyncio

# Telegram bot token and chat ID
TELEGRAM_TOKEN = "7487022753:AAFPHijXrk4EqTmNJxhHTT6MllmTHog5Ue8"
CHAT_ID = "922909522"

# Website URL to check
WEBSITE_URL = "https://expressedzshop.peasy.top/body-scale-03-ar.html?fbclid=IwY2xjawE9_jpleHRuA2FlbQIxMAABHWYS7AjEfQZkjSrNw7JKMIUyH436kXYh2HpzhrkaE9jX5_WFUmQivSW_oA_aem_qRttjfua-CNfRG5NGm6Yag"
async def send_telegram_message(token, chat_id, message):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=message)

def check_website(url):
    try:
        response = requests.get(url, timeout=10)
        print(f"Website response code: {response.status_code}")  # Debug information
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking website: {e}")
        return False

async def main():
    while True:
        print("starting ")
        website_status = check_website(WEBSITE_URL)
        status_message = "up" if website_status else "down"
        message = f"Alert: The website {WEBSITE_URL} is {status_message}!"
        print(f"Sending message: {message}")  # Debug information
        await send_telegram_message(TELEGRAM_TOKEN, CHAT_ID, message)
        await asyncio.sleep(120)  # Wait for 2 minutes before checking again

if __name__ == "__main__":
    asyncio.run(main())  

