__author__ = 'harsha'

import telegram_methods.getMe
import telegram_methods.getUpdates
import telegram_methods.sendMessage
import telegram.Update
import telegram.Message
import telegram.User
import telegram.GroupChat
import bot_utilities.tgtwitter
import re

base_url = "https://api.telegram.org/bot"
auth_file_name = "../bots/doloresBot.auth"
auth_file = open(auth_file_name, 'r')
auth_token = auth_file.readline()
consumer_key = auth_file.readline()
consumer_secret = auth_file.readline()
access_token = auth_file.readline()
access_token_secret = auth_file.readline()
auth_file.close()

# Remove the newline at end of file.
auth_token = auth_token[:-1]
consumer_key = consumer_key[:-1]
print(consumer_key)
consumer_secret = consumer_secret[:-1]
print(consumer_secret)
access_token = access_token[:-1]
print(access_token)
access_token_secret = access_token_secret[:-1]
print(access_token_secret )


bot_generic_message = "Hello, I am Dead End Dolores. I like turning left at dead ends and Harry Potter."
my_bot = base_url + auth_token

# On first run last update was 0
last_update_id = 0
first_run = True

while True:
    updates = telegram_methods.getUpdates.getUpdates(my_bot, last_update_id, None, None)
    print(len(updates), "Last ID:" + str(last_update_id))

    updateObj = None
    messageObj = None

    if len(updates) > 0:
        updateObj = updates[0]
        messageObj = updateObj.get_message()

    # Ignore all old messages.
    if first_run:
        print(updates)
        if len(updates) > 0:
            last_update_id = updateObj.get_update_id() + 1
        else:
            last_update_id += 1
        first_run = False

    elif len(updates) == 0:
        continue

    else:
        for count in range(0, len(updates)):
            updateObj = updates[0]
            messageObj = updateObj.get_message()
            # Debugging start
            #print(messageObj.get_text())
            print(messageObj)
            # Debugging end
            if messageObj.get_text() == "/dolores":
                chatObj = messageObj.get_chat()
                if type(chatObj) == telegram.GroupChat.GroupChat:
                    chat_id = chatObj.get_user_id()
                    telegram_methods.sendMessage.send_message(my_bot, chat_id, bot_generic_message)
                else:
                    chat_id = chatObj.get_id()
                    telegram_methods.sendMessage.send_message(my_bot, chat_id, bot_generic_message)

            if "/tweet" in messageObj.get_text() and last_update_id > 0:
                chatObj = messageObj.get_chat()
                tweet_message = re.sub('\/tweet', '', messageObj.get_text())
                tweet_message = tweet_message[:140]
                if tweet_message == "":
                    print("Empty Message")
                    continue
                print(tweet_message)
                if type(chatObj) == telegram.GroupChat.GroupChat:
                    status = bot_utilities.tgtwitter.tweet(consumer_key, consumer_secret, access_token, access_token_secret, tweet_message)
                    chat_id = chatObj.get_user_id()
                    telegram_methods.sendMessage.send_message(my_bot, chat_id, "Tweeted")# + status)
                else:
                    status = bot_utilities.tgtwitter.tweet(consumer_key, consumer_secret, access_token, access_token_secret, tweet_message)
                    chat_id = chatObj.get_id()
                    telegram_methods.sendMessage.send_message(my_bot, chat_id, "Tweeted")# + status)

        last_update_id = updateObj.get_update_id() + 1

