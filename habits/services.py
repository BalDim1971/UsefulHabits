import requests

from config.settings import TG_URL, TG_BOT_TOKEN, TG_CHAT_ID


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
