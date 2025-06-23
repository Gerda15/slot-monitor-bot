import requests
import time
from telegram import Bot

TOKEN = '8135556522:AAHQkBwTqoi63TpALncRGKzNp1auXYDXCWc'
CHAT_ID = 622506559
CHECK_INTERVAL = 60  # 1 хвилина

URL = 'https://icp.administracionelectronica.gob.es/icpplus/citar?p=46&locale=es'

def check_appointments():
    try:
        response = requests.get(URL, timeout=20)
        if response.status_code == 200:
            if "no hay citas disponibles" not in response.text.lower():
                return True
        return False
    except Exception as e:
        print(f"[!] Помилка: {e}")
        return False

def send_message(text):
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text)

if __name__ == "__main__":
    already_notified = False
    while True:
        if check_appointments():
            if not already_notified:
                send_message("📅 Увага! З'явилися вільні слоти на запис!")
                already_notified = True
        else:
            already_notified = False
        time.sleep(CHECK_INTERVAL)
