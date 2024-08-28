from celery import shared_task
from django.utils.timezone import localtime

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_habit_reminder():
    time_now = localtime()
    formatted_time = time_now.strftime("%H:%M")
    print(f"Текущее время {formatted_time}")
    habits = Habit.objects.filter(time_habit=formatted_time)
    print(f"Найдено привычек: {habits.count()}")
    for habit in habits:
        if habit.user_habit.tg_chat_id:
            send_telegram_message(habit)
        else:
            print(f"{habit.user_habit} не имеет привязки к telegram")
