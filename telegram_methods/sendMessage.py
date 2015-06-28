__author__ = 'harsha'

import requests
import json
import telegram.Message
import telegram.User

def send_message(my_bot, chat_id, message):
    bot_method = my_bot+"/sendMessage"
    params = {'text': message, 'chat_id': chat_id}
    response = requests.post(bot_method, params)
    responseData = json.loads(response.text)
    recvMessage = telegram.Message.Message(responseData['result'])
    if recvMessage.text == message:
        return True
    return False

'''
## Testing
base_url = "https://api.telegram.org/bot"
auth_token = "122152894:AAHV8afbjO_f4tPzmn-W8vLd7OWzWmxIbdw"
myBotUrl = base_url + auth_token

if send_message(myBotUrl, -28546005, "Hello, World!") == True:
    print("Message Sent")
else:
    print("Message Failed")
'''
