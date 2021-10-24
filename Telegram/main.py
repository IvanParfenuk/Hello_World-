import telebot
from telebot import types
from requests import get

bot =telebot.TeleBot('2098527930:AAGW6h800_oqeNCYbxX-axLsehlqzEtt-VA')


@bot.message_handler(commands=['start'])  # trigger for '/start' command
def begin(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # keyboard
    eat_but = types.KeyboardButton('Пицца🍕')
    eat_1but = types.KeyboardButton('Горячие закуски🧆')
    eat_2but = types.KeyboardButton('Салаты🥗')
    markup.add(eat_but, eat_1but, eat_2but)  # buttons import
    sti = 'Привет, что желаете заказать?'
    bot.send_message(message.chat.id, sti, reply_markup=markup)  # welcome message

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Пицца🍕':
        bot.send_photo(message.chat.id, get('https://discoveri.by/wp-content/uploads/2017/09/Pizza-Dobrynya.jpg').content)
        bot.send_message(message.chat.id, 'Добрыня:\n(тонкое тесто)пицца-соус, сыр Моцарелла, грудинка, креветки, шампиньоны, томаты, перец сладкий, специи 465 г')

        # markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # back_but = types.KeyboardButton('➖')
        # add = types.KeyboardButton('⬇')
        # forward = types.KeyboardButton('➕')
        # markup1.add(back_but, add, forward)
        # bot.send_message(message.chat.id, reply_markup=markup)
        # if message.text == '➕':
        #     bot.send_message(message.chat.id, get('https://discoveri.by/wp-content/uploads/2017/09/Pizza-Barskaya.jpg').content)
        #     bot.send_message(message.chat.id,'Барская:\n(тонкое тесто)пицца-соус, сыр Моцарелла, грудинка, колбаса сырокопченая, соус сметанно-чесночный, томаты, специи 485 г')

    elif message.text == 'Горячие закуски🧆':
        bot.send_photo(message.chat.id, get('https://discoveri.by/wp-content/uploads/2017/09/Chiken-Bastonni.jpg').content)
        bot.send_message(message.chat.id, 'Чикен Бастони:\nфиле птицы в панировке, соус Чили 150/30 г')
    else:
        bot.send_photo(message.chat.id, get('https://discoveri.by/wp-content/uploads/2017/09/Salat-Tsezar-s-krevetkami.jpg').content)
        bot.send_message(message.chat.id, 'Цезарь с креветками:\nкоролевские креветки, сыр Джюгас, томаты, салат Айсберг, чесночные гренки, зелень, соус Цезарь 230 г')







# if message.chat.id == 'Пицца🍕':
#     bot.send_photo(message.chat.id, photo=open('Telegram/Бронкс-семейная.png', 'rb'))



# @bot.message_handler(content_types=["photo"])
# def predlozh(message):
#     if message.chat.id == 'да':
#         # ph = open('Бронкс-семейная.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo=open('Бронкс-семейная.jpg', 'rb'))


# @bot.message_handler(content_types=["text1"])
# def predlozhenie1(message):
#     if message.chat.id.lower() == 'да':
#         nexts1 = 'Отлично, выберите то, что хотите заказать'
#         bot.send_message(message.chat.id, nexts1)
#     elif message.chat.id == 'Нет' or 'нет':
#         nexts2 = 'Понял, хорошего дня'
#         bot.send_message(message.chat.id, nexts2)



bot.polling(none_stop=True)























