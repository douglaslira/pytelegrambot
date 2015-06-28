__author__ = 'harsha'

import requests
import json
import telegram.Update
import telegram.Message

def getUpdates(my_bot, offset, limit, timeout):
    bot_method = my_bot+"/sendMessage"
    params = {'offset': offset, 'limit': limit, 'timeout': timeout}
    response = requests.post(bot_method, params)

#def getUpdates(self, offset):

#def getUpdates(self, limit):

#def getUpdates(self, timeout):

def getUpdates(my_bot):
    bot_method = my_bot+"/getUpdates"
    response = requests.post(bot_method)
    response_data = json.loads(response.text)
    if response_data is not None:
        response_data = response_data['result']
        updateObjs =[]
        for count in range(0, len(response_data)):
            # Create a Message Object
            messageString = response_data[count]['message']
            #print(messageString) # Just to see chat id
            messageObj = telegram.Message.Message(messageString)
            updateObjs.append(telegram.Update.Update(response_data[count]['update_id'], messageObj))
        return updateObjs

'''
## Testing
base_url = "https://api.telegram.org/bot"
auth_token = "122152894:AAHV8afbjO_f4tPzmn-W8vLd7OWzWmxIbdw"
myBotUrl = base_url+auth_token

telUser = getUpdates(myBotUrl)
print(telUser)
'''
