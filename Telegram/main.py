import telebot
import config

bot = telebot.Telegram(config.Token)

@bot.message_handler(content_types=['text'])
def mas(message):
    if message.chat.type == 'private':
        if message.text == 'Скандинаская':
bot.send_message(message.chat.id,'Хороший выбор, оплатите заказ')
elif message.text == 'Мафия-семейная':

markup = types.InlineKeyboardMarkup(row_width=2)
item1 = types.InlineKeyboardButton("")
item2 = types.InlineKeyboardButton("Не очень")

markup.add(item1, item2)

bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
else:
bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
bot.polling()