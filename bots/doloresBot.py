__author__ = 'harsha'

import telegram_methods.getMe
import telegram_methods.getUpdates

base_url = "https://api.telegram.org/bot"
auth_token = "122152894:AAHV8afbjO_f4tPzmn-W8vLd7OWzWmxIbdw"

my_bot = base_url + auth_token

updates = telegram_methods.getUpdates.getUpdates(my_bot)

