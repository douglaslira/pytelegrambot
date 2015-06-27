__author__ = 'harsha'

import requests
import json
import telegram.Message

def send_message(my_bot, chat_id, message):
    bot_method = my_bot+"/sendMessage"
    params = {'text': message, 'chat_id': chat_id}
    response = requests.post(bot_method, params)
    return

## Testing
base_url = "https://api.telegram.org/bot"
auth_token = "122152894:AAHV8afbjO_f4tPzmn-W8vLd7OWzWmxIbdw"
myBotUrl = base_url+auth_token

telUser = getMe(myBotUrl)
print(telUser)
