import requests
from secr import telegram_token, telegram_channel
from fastapi import APIRouter

router = APIRouter()


# Sending messages to telegram channel
@router.post('/tg/send_message', tags=['telegram'])
def send_telegram_message(msg: str = 'Test from service'):
    token = telegram_token
    chat_id = telegram_channel
    # url = f"https://api.telegram.org/bot{token}/getUpdates"
    # resp = requests.get(url).json()
    resp = requests.get(f"https://api.telegram.org/bot{token}/sendMessage", params=dict(
                        text=msg, chat_id=chat_id))
    return resp.json()
