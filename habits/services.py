import requests
from rest_framework import status

from config import settings


def send_telegram_message(habit):
    message = f"Я буду {habit.action_habit} в {habit.time_habit} в {habit.place_habit}."
    chat_id = habit.user_habit.tg_chat_id
    params = {"text": message, "chat_id": chat_id}
    response = requests.get(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
        params=params,
    )
    if response.status_code != status.HTTP_200_OK:
        print(f"Ошибка при отправке сообщения в Telegram: {response.text}")
