__author__ = 'harsha'

import requests
import json
import telegram.Update
import telegram.Message

def get_update_obj_arry(response_json):
    updateObjs =[]
    for count in range(0, len(response_json)):
        # Create a Message Object
        messageString = response_json[count]['message']
        messageObj = telegram.Message.Message(messageString)
        updateObjs.append(telegram.Update.Update(response_json[count]['update_id'], messageObj))
    return updateObjs


def getUpdates(my_bot, offset, limit, timeout):
    bot_method = my_bot+"/getUpdates"
    params = {}

    if offset != None:
        params['offset'] = offset
    if limit != None:
        params['limit'] = limit
    if timeout != None:
        params['timeout'] = timeout

    response = requests.post(bot_method, params)
    response_data = json.loads(response.text)

    #Check result
    if(response_data['ok'] == False):
        print(response_data['description'])
        return
    else:
        response_data = response_data['result']
        return get_update_obj_arry(response_data)

'''
## Testing
base_url = "https://api.telegram.org/bot"
auth_file_name = "./bots/doloresBot.auth"
auth_file = open(auth_file_name, 'r')
auth_token = auth_file.read()
auth_file.close()
auth_token = auth_token[:-1]
myBotUrl = base_url+auth_token

telUser = getUpdates(myBotUrl, 315634024, None, None)
print(telUser)
'''
