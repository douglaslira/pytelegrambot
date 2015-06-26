__author__ = 'harsha'

import requests
import json

base_url = "https://api.telegram.org/bot"
auth_token = "122152894:AAHV8afbjO_f4tPzmn-W8vLd7OWzWmxIbdw"

#testing_json = "{\"ok\":true,\"result\":[{\"update_id\":315634024,\"message\":{\"message_id\":29,\"from\":{\"id\":58905931,\"first_name\":\"Sruthi\",\"last_name\":\"K\"},\"chat\":{\"id\":-10841416,\"title\":\"FoV Labs\"},\"date\":1435314327,\"text\":\"\ud83c\udfad\"}},{\"update_id\":315634025,\"message\":{\"message_id\":30,\"from\":{\"id\":58905931,\"first_name\":\"Sruthi\",\"last_name\":\"K\"},\"chat\":{\"id\":-10841416,\"title\":\"FoV Labs\"},\"date\":1435314341,\"sticker\":{\"width\":448,\"height\":512,\"thumb\":{\"file_id\":\"AAQFABOQyrEyAAQIMgtH7_G8U-d_AAIC\",\"file_size\":2564,\"width\":79,\"height\":90},\"file_id\":\"BQADBQADJQADyIsGAAGdzbYn4WkdaAI\",\"file_size\":46298}}},{\"update_id\":315634026,\"message\":{\"message_id\":31,\"from\":{\"id\":58905931,\"first_name\":\"Sruthi\",\"last_name\":\"K\"},\"chat\":{\"id\":-10841416,\"title\":\"FoV Labs\"},\"date\":1435314354,\"sticker\":{\"width\":336,\"height\":512,\"thumb\":{\"file_id\":\"AAQFABMs5rEyAARBrYEofz_QmNB_AAIC\",\"file_size\":2054,\"width\":59,\"height\":90},\"file_id\":\"BQADBQADFQADyIsGAAEO_vKI0MR5bAI\",\"file_size\":29354}}},{\"update_id\":315634027,\"message\":{\"message_id\":32,\"from\":{\"id\":58905931,\"first_name\":\"Sruthi\",\"last_name\":\"K\"},\"chat\":{\"id\":-10841416,\"title\":\"FoV Labs\"},\"date\":1435314361,\"sticker\":{\"width\":302,\"height\":512,\"thumb\":{\"file_id\":\"AAQFABNdz7EyAASqXwRjP4GAynt_AAIC\",\"file_size\":2046,\"width\":53,\"height\":90},\"file_id\":\"BQADBQADIwADyIsGAAEsv26c3x-AkQI\",\"file_size\":31286}}},{\"update_id\":315634028,\"message\":{\"message_id\":33,\"from\":{\"id\":22899305,\"first_name\":\"Bharath\",\"last_name\":\"Palavalli\"},\"chat\":{\"id\":-10841416,\"title\":\"FoV Labs\"},\"date\":1435314370,\"text\":\"group muted again \ud83d\ude10\"}},{\"update_id\":315634029,\"message\":{\"message_id\":35,\"from\":{\"id\":56912673,\"first_name\":\"Harsha\",\"last_name\":\"K\",\"username\":\"disturbedspace\"},\"chat\":{\"id\":56912673,\"first_name\":\"Harsha\",\"last_name\":\"K\",\"username\":\"disturbedspace\"},\"date\":1435314646,\"text\":\"\/start\"}},{\"update_id\":315634030,\"message\":{\"message_id\":36,\"from\":{\"id\":64514616,\"first_name\":\"Murali\"},\"chat\":{\"id\":-10841416,\"title\":\"FoV Labs\"},\"date\":1435315146,\"text\":\":-\/\"}},{\"update_id\":315634031,\"message\":{\"message_id\":40,\"from\":{\"id\":56912673,\"first_name\":\"Harsha\",\"last_name\":\"K\",\"username\":\"disturbedspace\"},\"chat\":{\"id\":-10841416,\"title\":\"FoV Labs\"},\"date\":1435319455,\"text\":\"\/kshiraja\"}},{\"update_id\":315634032,\"message\":{\"message_id\":41,\"from\":{\"id\":56912673,\"first_name\":\"Harsha\",\"last_name\":\"K\",\"username\":\"disturbedspace\"},\"chat\":{\"id\":56912673,\"first_name\":\"Harsha\",\"last_name\":\"K\",\"username\":\"disturbedspace\"},\"date\":1435320449,\"text\":\"\/kshiraja\"}}]}"

myBotUrl = base_url+auth_token

chat_id = "-10841416"



getMeMethod = "getMe"
url = base_url + auth_token + "/" + getMeMethod

# About Me method
def getMe(mybot):
    botMethod = mybot+"/getMe"
    return botMethod

# Get Updates from Bot
def getUpdates(mybot):
    botMethod = mybot+"/getUpdates"
    return botMethod

# Get Updates from Bot
def getSingleUpdate(mybot):
    botMethod = mybot+"/getUpdates"
    return botMethod


def sendMessage(mybot, msg_text):
    botMethod = mybot+"/sendMessage"
    params = {'text':msg_text, 'chat_id':chat_id}
    requests.post(botMethod,params)
    return


while True:
    params = {'limit': 100}
    print("polling")
    responseObj = requests.post(getSingleUpdate(myBotUrl), params)

    data = json.loads(responseObj.text)
    for count in range(0,len(data['result'])):
        if('text' in data['result'][count]['message']):
            message_text = data['result'][count]['message']['text']
            print(message_text)
            if(message_text == '/kshiraja'):
                print("/kshiraja recognised, responding..")
                sendMessage(myBotUrl, "Hello Dead End!")
