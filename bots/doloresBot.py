__author__ = 'harsha'

import telegram_methods.getMe

base_url = "https://api.telegram.org/bot"
auth_token = "122152894:AAHV8afbjO_f4tPzmn-W8vLd7OWzWmxIbdw"

my_bot = base_url + auth_token

telegram_methods.getMe.getMe(my_bot)


