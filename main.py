import telebot

bot = telebot.Telebot("7884887946:AAG8-4A98vjnmgUukqVZ9LhwjBga4s1v5C8")

@bot.message_handlers(commands=['start'])
def start(message):
    bot.send_