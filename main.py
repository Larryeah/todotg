import telebot
from telebot import types
from funcs import *

bot = telebot.TeleBot("7884887946:AAG8-4A98vjnmgUukqVZ9LhwjBga4s1v5C8")


dict = {
    "1": "Помыть посуду",
    "2": "Выбросить мусор"
}

# Отслеживание команд
# Приветственное сообщение
@bot.message_handler(commands=['start'])
def start(message):
    mess = f"""<b>Привет, {message.from_user.first_name}.</b>
Этот телеграмм бот создан для отслеживания дел на день.
Для создания задач воспользуйтесь командами ниже ⬇️
"""
    # bot.send_message(message.chat.id, mess, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    todolist = types.KeyboardButton("1. Показать список на день")
    add = types.KeyboardButton("2. Добавить задачу")
    delete = types.KeyboardButton("3. Удалить задачу")
    deleteAll = types.KeyboardButton("4. Удалить все задачи")
    markup.add(todolist, add, delete, deleteAll)
    bot.send_message(message.chat.id,mess, reply_markup=markup, parse_mode='html')

@bot.message_handler(content_types=['text'])
def tasks(message):
    if message.text == "1. Показать список на день":
        if dict == {}:
            bot.send_message(message.chat.id, f"Список задач пуст!", parse_mode="html")
        else:
            bot.send_message(message.chat.id, f"<b>Ваш список задач:</b>\n\n {print_dict(dict,message)}", parse_mode="html")
    if message.text == "2. Добавить задачу":
        bot.send_message(message.chat.id, f"<b>Введите текст задачи</b>", parse_mode="html")
        bot.register_next_step_handler(message, add_task)
    if message.text == "3. Удалить задачу":
        bot.send_message(message.chat.id, f"Напишите номер задачи", parse_mode="html")
        bot.register_next_step_handler(message, delete_task)
    if message.text == "4. Удалить все задачи":
        dict.clear()
        bot.send_message(message.chat.id, f"Все задачи удалены!", parse_mode="html")


bot.message_handler()



bot.polling(non_stop=True) #запускаем бота