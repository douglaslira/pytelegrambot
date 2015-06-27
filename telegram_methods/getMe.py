__author__ = 'harsha'

import requests
import json
import telegram.User


def getMe(my_bot):
    bot_method = my_bot+"/getMe"
    response = requests.post(bot_method)
    print(response.text)
    user_data = json.loads(response.text)
    if user_data is not None:
        user_data = user_data['result']

        if 'last_name' in user_data.keys():
            last_name = user_data['last_name']
        else:
            last_name = ''

        if 'username' in user_data.keys():
            username = user_data['username']
        else:
            username = ''

        return telegram.User.User(user_data['id'], user_data['first_name'], last_name, username)


## Testing
base_url = "https://api.telegram.org/bot"
auth_token = "122152894:AAHV8afbjO_f4tPzmn-W8vLd7OWzWmxIbdw"
myBotUrl = base_url+auth_token

telUser = getMe(myBotUrl)
print(telUser)
