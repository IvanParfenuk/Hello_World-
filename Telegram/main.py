import telebot

bot =telebot.TeleBot('2098527930:AAGW6h800_oqeNCYbxX-axLsehlqzEtt-VA')

@bot.message_handler(commands=["start"])
def start(message):
    send_message = 'Привет'
    bot.send_message(message.chat.id, send_message)


bot.polling(none_stop=True)





# async def cmd_start(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup()
#     button_1 = types.KeyboardButton(text="С пюрешкой")
#     keyboard.add(button_1)
#     button_2 = "Без пюрешки"
#     keyboard.add(button_2)
#     await message.answer("Как подавать котлеты?", reply_markup=keyboard)





















