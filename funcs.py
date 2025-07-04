

def print_dict(dict, message=None):
    result = "\n".join(f"{k}. {v}" for k, v in dict.items())
    return result

def add_task(message):
    dict[f"{len(dict) + 1}"] = f"{message.text}"
    bot.send_message(message.chat.id, f"<b>Задача успешно добавлена.</b>\nВаш список:\n{print_dict(dict)}", parse_mode="html")

def delete_task(message):
    del dict[message.text]
    bot.send_message(message.chat.id, f"<b>Задача успешно удалена.</b>\n\nВаш список:{print_dict(dict)}",parse_mode="html")