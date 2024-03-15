import requests
from celery import shared_task

from config.settings import TG_URL, TG_BOT_TOKEN, TG_CHAT_ID
from habits.models import Habits


class MyBot:
    URL = TG_URL
    TOKEN = TG_BOT_TOKEN

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': TG_CHAT_ID,
                'text': text
            }
        )

@shared_task
def habits_bot():
    habits = Habits.objects.all()
    for habit in habits:
        pass
