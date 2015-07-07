# Readme
-------------

This is a python frontend module to use the newly released Telegram bot API. 
This project is intended to do various tasks from our group accounts using Telegram Bots. 
Currently a simple bot, __doloresBot__ is implemented to test some of the API. The bot is able to read messages, 
interpret them into message objects. Currently, the only action implemented is a text reply with a generic message 
using the telegram bot API and is able to tweet messages to from Telegram.
 
# Install
_________

1. Run __pip3 install__ to install the project. 
2. Add the auth code for the bot in the __<bot-name>.auth__ file.
3. Run individual bot __python <bot-name>__
OR. add an entry to __runBots.sh__ to run all of them as __nohup__ process.
 
Currently there is a sample bot called __doloresBot.py__ is created. This bot responds to some generic messages, 
and is able to tweet a message to twitter.

## Dependency
1. Requests python module
2. Json python module
3. Tweeepy python module


# Wish-list for Bots
-------------------
1. Post a telegram message to Twitter account (done)
2. Post a telegram message to Facebook account
3. A events reminder Bot to remind about events from the group calendar

## Bots for fun
----------------
1. Plant watering bot
2. Code repo status bot
3. Read weather data from a seeduino sensor array.
