import telebot
from Telegram import keyboard

bot =telebot.TeleBot('2098527930:AAGW6h800_oqeNCYbxX-axLsehlqzEtt-VA')

@bot.message_handler(commands=['start'])
def begin(message):
    sti = 'Привет, что желаете заказать?'
    bot.send_message(message.chat.id, sti, reply_markup=keyboard.markup)  # welcome message

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '💌 О нас':
        doc = open('fortg.txt', 'rb')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'Пицца🍕':
        description = 'Добрыня:\n(тонкое тесто)пицца-соус, сыр Моцарелла, грудинка, креветки, шампиньоны, томаты, перец сладкий, специи 465 г'
        bot.send_photo(message.chat.id, photo=open('Pizza-Dobrynya.jpg', 'rb'), caption=description, reply_markup=keyboard.eda_)

    elif message.text == 'Горячие закуски🧆':
        description = 'Чикен Бастони:\nфиле птицы в панировке, соус Чили 150/30 г'
        bot.send_photo(message.chat.id, photo=open('Chiken-Bastonni.jpg', 'rb'), caption=description, reply_markup=keyboard.eda_)

    else:
        description = 'Цезарь с креветками:\nкоролевские креветки, сыр Джюгас, томаты, салат Айсберг, чесночные гренки, зелень, соус Цезарь 230 г'
        bot.send_photo(message.chat.id, photo=open('Salat-Tsezar-s-krevetkami.jpg', 'rb'), caption=description, reply_markup=keyboard.eda_)

bot.polling(none_stop=True)























