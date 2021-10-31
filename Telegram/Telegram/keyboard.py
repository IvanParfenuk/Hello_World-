from telebot import types
# main keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # creating a keyboard
eat_but = types.KeyboardButton('Пицца🍕')
eat_1but = types.KeyboardButton('Горячие закуски🧆')
eat_2but = types.KeyboardButton('Салаты🥗')
o_nas = types.KeyboardButton('💌 О нас')
markup.add(eat_but, eat_1but, eat_2but, o_nas) # adding buttons to the keyboard markup

# keyboard for rewinding
eda_ = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="◀", callback_data="Вперед")
but_2 = types.InlineKeyboardButton(text="⬇", callback_data="Добавить в корзину")
but_3 = types.InlineKeyboardButton(text="▶", callback_data="Назад")
eda_.add(but_1, but_2, but_3) # adding buttons to the keyboard eda_
