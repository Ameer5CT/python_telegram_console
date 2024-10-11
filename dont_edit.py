from telebot import TeleBot
import threading
import time

bot = None
chat_id = 0
text_input = ""


def start_bot(token):
    global bot
    bot = TeleBot(token, skip_pending=True)
    bot.message_handler(commands=['start'])(start_message)
    bot.message_handler(content_types=['text'])(text_message)
    def run_bot():
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()


def start_message(msg):
    global chat_id
    if chat_id == 0:
        chat_id = msg.chat.id
        bot.send_message(chat_id, "Your code started\n🔽🔽🔽🔽🔽")


def text_message(msg):
    global chat_id
    if chat_id == 0:
        chat_id = msg.chat.id
        bot.send_message(chat_id, "Your code started\n🔽🔽🔽🔽🔽")
    elif msg.chat.id == chat_id:
        global text_input
        text_input = msg.text


def wait_start():
    while chat_id == 0:
        time.sleep(1)


def wait_input():
    while text_input == "":
        time.sleep(1)


def tprint(text):
    wait_start()
    if text:
        bot.send_message(chat_id, text)
    else:
        bot.send_message(chat_id, "Empty output.")


def tinput(text):
    wait_start()
    if text:
        bot.send_message(chat_id, text)
    else:
        bot.send_message(chat_id, "Empty input:")
    wait_input()
    global text_input
    temp_text = text_input
    text_input = ""
    return temp_text
