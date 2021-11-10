import telebot
from Telegram import keyboard

bot = telebot.TeleBot('2098527930:AAGW6h800_oqeNCYbxX-axLsehlqzEtt-VA')

# Пропишем описание для каждой пиццы
text_about_dobrynya = "Добрыня:\nпицца-соус, сыр Моцарелла, грудинка, креветки, шампиньоны, томаты, перец сладкий, специи 465 г"
text_about_man = "Мужская(острая):\nпицца-соус, сыр Моцарелла, колбаса сырокопченая, ветчина, филе птицы, свинина отварная, маслины, масло оливковое, кайенский перец, специи 430 г"
text_about_mushrooms = 'Грибная:\nпицца-соус, сыр Моцарелла, шампиньоны, соевый соус, лук-порей, специи 455 г'

# Создадим словарь
dict_pizzas = {'Добрыня': (open('Pizza-Dobrynya.jpg', 'rb'), text_about_dobrynya),
               'Мужская': (open('Pizza-Muzhskaya-ostraya-300x300.jpg', 'rb'), text_about_man),
               'Грибная': (open('Pizza-Gribnaya.jpg', 'rb'), text_about_mushrooms)}

# Приветствие на команду старт
@bot.message_handler(commands=['start'])
def begin(message):
    sti = 'Привет, что желаете заказать?'
    bot.send_message(message.chat.id, sti, reply_markup=keyboard.markup) # welcome message

# Ответ на команды типа: текст
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '💌 О нас':
        doc = open('fortg.txt', 'rb')
        bot.send_document(message.chat.id, doc, reply_markup=keyboard.markup)
    if message.text == 'Пицца🍕':
        bot.send_photo(message.chat.id, photo=dict_pizzas['Добрыня'][0], caption=dict_pizzas['Добрыня'][1], reply_markup=keyboard.markup2) # Обращаюсь в словарь к ключу "Добрыня", затем через индекс обращаюсь к нужному значению
    if message.text == '▶':
        bot.send_photo(message.chat.id, photo=dict_pizzas['Мужская'][0], caption=dict_pizzas['Мужская'][1], reply_markup=keyboard.markup2) # Обращаюсь в словарь к ключу "Мужская", затем через индекс обращаюсь к нужному значению
    elif message.text == '◀':
        bot.send_photo(message.chat.id, photo=dict_pizzas['Грибная'][0], caption=dict_pizzas['Грибная'][1], reply_markup=keyboard.markup2) # Обращаюсь в словарь к ключу "Грибная", затем через индекс обращаюсь к нужному значению
    elif message.text == 'Назад в меню':
        transition_text = 'Пожалуйста, вы в главном меню😋'
        bot.send_message(message.chat.id, transition_text, reply_markup=keyboard.markup)




#     elif message.text == 'Горячие закуски🧆':
#         description = 'Чикен Бастони:\nфиле птицы в панировке, соус Чили 150/30 г'
#         bot.send_photo(message.chat.id, photo=open('Chiken-Bastonni.jpg', 'rb'), caption=description, reply_markup=keyboard.markup2)
#
#     elif message.text == 'Салаты🥗':
#         description = 'Цезарь с креветками:\nкоролевские креветки, сыр Джюгас, томаты, салат Айсберг, чесночные гренки, зелень, соус Цезарь 230 г'
#         bot.send_photo(message.chat.id, photo=open('Salat-Tsezar-s-krevetkami.jpg', 'rb'), caption=description, reply_markup=keyboard.markup2)
#
bot.polling(none_stop=True)




















