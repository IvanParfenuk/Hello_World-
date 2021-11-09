from telebot import types
# main keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # creating a keyboard
eat_but = types.KeyboardButton('Пицца🍕')
eat_1but = types.KeyboardButton('Горячие закуски🧆')
eat_2but = types.KeyboardButton('Салаты🥗')
o_nas = types.KeyboardButton('💌 О нас')
markup.row(eat_but, eat_1but) #creating the first row of buttons
markup.row(eat_2but, o_nas) #creating a second row of buttons


# # keyboard for rewinding
eda_ = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="◀", callback_data="Вперед")
but_2 = types.InlineKeyboardButton(text="⬇", callback_data="Добавить в корзину")
but_3 = types.InlineKeyboardButton(text="▶", callback_data="Назад")
eda_.add(but_1, but_2, but_3) # adding buttons to the keyboard eda_


# pizza1 = types.InlineKeyboardMarkup()
# but_1 = types.InlineKeyboardButton(
#     text="Оформить заказ", url="https://t.me/por0vos1k")
# but_2 = types.InlineKeyboardButton(text="▶️", callback_data="Вперед1")
# pizza1.add(but_2)
# pizza1.add(but_1)