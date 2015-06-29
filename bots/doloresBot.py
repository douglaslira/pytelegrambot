__author__ = 'harsha'

import telegram_methods.getMe
import telegram_methods.getUpdates
import telegram_methods.sendMessage
import telegram.Update
import telegram.Message
import telegram.User
import telegram.GroupChat

base_url = "https://api.telegram.org/bot"
auth_file_name = "doloresBot.auth"
auth_file = open(auth_file_name, 'r')
auth_token = auth_file.read()
auth_file.close()

bot_generic_message = "Hello, I am Dead End Dolores. I like turning left at dead ends and Harry Potter."
my_bot = base_url + auth_token

# On first run last update was 0
last_update_id = 0

while True:
    updates = telegram_methods.getUpdates.getUpdates(my_bot, last_update_id, None, None)
    print(len(updates),"Last ID:" + str(last_update_id))
    for count in range(0, len(updates)):
        updateObj = updates[0]
        messageObj = updateObj.get_message()
        # Debugging start
        print(messageObj.get_text())
        print(messageObj)
        # Debugging end
        if messageObj.get_text() == "/dalores":
            chatObj = messageObj.get_chat()
            if type(chatObj) == telegram.GroupChat.GroupChat:
                chat_id = chatObj.get_user_id()
                telegram_methods.sendMessage.send_message(my_bot, chat_id, bot_generic_message)
            else:
                chat_id = chatObj.get_id()
                telegram_methods.sendMessage.send_message(my_bot, chat_id, bot_generic_message)
        last_update_id = updateObj.get_update_id() + 1
