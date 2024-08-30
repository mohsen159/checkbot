import requests
from telegram import Bot

TELEGRAM_TOKEN = "7487022753:AAFPHijXrk4EqTmNJxhHTT6MllmTHog5Ue8"
CHAT_ID = "922909522"
WEBSITE_URL = "https://expressedzshop.peasy.top/body-scale-03-ar.html?fbclid=IwY2xjawE9_jpleHRuA2FlbQIxMAABHWYS7AjEfQZkjSrNw7JKMIUyH436kXYh2HpzhrkaE9jX5_WFUmQivSW_oA_aem_qRttjfua-CNfRG5NGm6Yag"

def check_website(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking website: {e}")
        return False

def send_telegram_message(token, chat_id, message):
    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message)

def main():
    website_status = check_website(WEBSITE_URL)
    status_message = "up" if website_status else "down"
    message = f"Alert: The website {WEBSITE_URL} is {status_message}!"
    send_telegram_message(TELEGRAM_TOKEN, CHAT_ID, message)

if __name__ == "__main__":
    print("Starting script...")
    main()
