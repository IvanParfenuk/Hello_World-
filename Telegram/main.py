import telebot
from telebot import types
TOKEN = '1958484914:AAElAx_Y-s766tWnOjDLf09-3DAbkqBOKBI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('👍 Пицца')
    item2 = types.KeyboardButton('🥗 Салаты')
    item3 = types.KeyboardButton('❌ Другое')





    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}', format(message.from_user), reply_markup = markup)

bot.polling(none_stop = True)







