import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot("")

def print_dict(dict, message=None):
    result = "\n".join(f"{k}. {v}" for k, v in dict.items())
    return result

def add_task(message):
    dict[f"{len(dict) + 1}"] = f"{message.text}"
    bot.send_message(message.chat.id, f"<b>Задача успешно добавлена.</b>\n\nВаш список:\n{print_dict(dict)}", parse_mode="html")

def delete_task(message):
    global dict
    del dict[message.text]
    dict = {i: val for i, val in enumerate(dict.values(), start=1)}
    bot.send_message(message.chat.id, f"<b>Задача успешно удалена.</b>\n\nВаш список:\n{print_dict(dict)}",parse_mode="html")

dict = {
}

# Отслеживание команд
# Приветственное сообщение
@bot.message_handler(commands=['start'])
def start(message):
    #Создаем БД на SQlite3
    # conn = sqlite3.connect('baza.sql')
    # cur = conn.cursor()
    # cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50)')
    # conn.commit()
    # cur.close()
    # conn.close()
    #
    # bot.send_message()

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
    elif message.text == "2. Добавить задачу":
        bot.send_message(message.chat.id, f"<b>Введите текст задачи</b>", parse_mode="html")
        bot.register_next_step_handler(message, add_task)
    elif message.text == "3. Удалить задачу":
        bot.send_message(message.chat.id, f"Напишите номер задачи", parse_mode="html")
        bot.register_next_step_handler(message, delete_task)
    elif message.text == "4. Удалить все задачи":
        dict.clear()
        bot.send_message(message.chat.id, f"Все задачи удалены!", parse_mode="html")
    else:  bot.send_message(message.chat.id, f"Чтобы воспользоваться ботом, используй команды снизу (Специальной клавиатурой)", parse_mode="html")

bot.message_handler()



bot.polling(non_stop=True) #запускаем бота