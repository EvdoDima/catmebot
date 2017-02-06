import os
import random
import sys
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
cats = []
def loadcats():
    catsnames = os.listdir("cats")
    for cat in catsnames:
        # print(cat)
        cats.append(cat)



def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(str(chat_id)+ " : "+msg['text'])
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Cat me')]
    ])
    if msg['text'] == "/start":
        bot.sendMessage(chat_id, 'get the cats', reply_markup=keyboard)
    elif msg['text'] == "Cat me":
        loadcats()
        random.shuffle(cats)
        f = open("cats/"+cats[0], 'rb')
        bot.sendPhoto(chat_id,f)

    else:
        bot.sendMessage(chat_id, 'WTF', reply_markup=keyboard)


TOKEN = "310316284:AAHL5etFsIXbxnIVDkACj-OxijBTPJRqg5Q"

bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message})
print('Listening ...')

while 1:
    time.sleep(10)