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
    my_bot = MyBot()
    habits = Habits.objects.all()
    for habit in habits:
        action = habit.action
        time = habit.time
        place = habit.place
        time_exec = habit.time_exec
        text = (f'Я должен {action} в {time} в {place} выполнять {time_exec}'
                f'секунд.')
        my_bot.send_message(text)
        time_sec = sum(x * int(t) for x, t in
                       zip([3600, 60, 1], time_exec.split(":")))

        time.sleep(time_sec)
        if habit.award is not None:
            text = f'Вознаграждение {habit.award}'
            my_bot.send_message(text)
