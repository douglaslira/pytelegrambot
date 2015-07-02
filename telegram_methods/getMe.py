__author__ = 'harsha'

import requests
import json
import telegram.User


def getMe(my_bot):
    bot_method = my_bot + "/getMe"
    response = requests.post(bot_method)
    print(response.text)
    user_data = json.loads(response.text)
    if user_data is not None:
        user_data = user_data['result']
        return telegram.User.User(user_data)
'''
## Testing
base_url = "https://api.telegram.org/bot"
auth_file_name = "./bots/doloresBot.auth"
auth_file = open(auth_file_name, 'r')
auth_token = auth_file.read()
auth_file.close()
auth_token = auth_token[:-1]
myBotUrl = base_url + auth_token
telUser = getMe(myBotUrl)
print(telUser)
'''

