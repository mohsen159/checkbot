import requests
from telegram import Bot

# Telegram bot token and chat ID
TELEGRAM_TOKEN = "7487022753:AAFPHijXrk4EqTmNJxhHTT6MllmTHog5Ue8"
CHAT_ID = "922909522"  # Replace with your actual chat ID

# Website URL to check
WEBSITE_URL = "https://expressedzshop.peasy.top/body-scale-03-ar.html?fbclid=IwY2xjawE9_jpleHRuA2FlbQIxMAABHWYS7AjEfQZkjSrNw7JKMIUyH436kXYh2HpzhrkaE9jX5_WFUmQivSW_oA_aem_qRttjfua-CNfRG5NGm6Yag"  # Replace with the URL you want to monitor

def check_website(url):
    """Check if the website is reachable."""
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False

def send_telegram_message(token, chat_id, message):
    """Send a message to a Telegram chat."""
    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message)

def main():
    if not check_website(WEBSITE_URL):
        message = f"Alert: The website {WEBSITE_URL} is down!"
        send_telegram_message(TELEGRAM_TOKEN, CHAT_ID, message)

if __name__ == "__main__":
    main()
