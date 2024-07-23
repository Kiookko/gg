import telebot
import time
from threading import Thread

API_TOKEN = '7152378743:AAHX0lrzgcasCEIJP-fyqcoHQorDJ5SSfoM'
SPAM_TEXT = 'Это спам-сообщение'
SPAM_INTERVAL = 3  # Интервал между сообщениями в секундах

bot = telebot.TeleBot(API_TOKEN)

def spam(chat_id):
    while True:
        bot.send_message(chat_id, SPAM_TEXT)
        time.sleep(SPAM_INTERVAL)

@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    bot.reply_to(message, "Начинаю спамить!")
    Thread(target=spam, args=(chat_id,)).start()

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    chat_id = message.chat.id
    bot.reply_to(message, "Спам остановлен!")
    # Здесь можно добавить логику для остановки спама, если потребуется

# Запуск бота
bot.polling()
