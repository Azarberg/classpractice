import telebot
from telebot import types
bot = telebot.TeleBot("5033565132:AAE0I6m_UNFOgMjuxwmX42epPxmcKLalzqY")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	image = open('/home/azamat/P/Telebot/images.jpeg', 'rb')
	bot.send_photo(message.chat.id, image)

	markup = types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = types.KeyboardButton('Ноутбуки')
	itembtn2 = types.KeyboardButton('Компьютер')

	markup.add(itembtn1, itembtn2)
	bot.send_message(message.chat.id,
					 "Выберите ноутбук или компьютер: ",
					 reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(message):

    if message.text == 'Ноутбуки':
        markup = types.InlineKeyboardMarkup(row_width=2)
        nout1 = telebot.types.InlineKeyboardButton("Macbook",  callback_data = 'mac')
        nout2 = telebot.types.InlineKeyboardButton("Dell inspiron", callback_data = 'dell')
        nout3 = telebot.types.InlineKeyboardButton("Lenovo", callback_data = 'lenovo')
        nout4 = telebot.types.InlineKeyboardButton("Acer", callback_data = 'acer')
        nout5 = telebot.types.InlineKeyboardButton("HP", callback_data = 'hp')
        markup.add(nout1, nout2, nout5, nout4, nout3)
        bot.send_message(message.chat.id,
                         "Выберите какой нутбук",
                         reply_markup=markup)
    elif message.text == 'Компьютер':
        markup = types.InlineKeyboardMarkup(row_width=2)
        comp1 = telebot.types.InlineKeyboardButton("Intel i-7200,16GB RAM,SSD 256gb", callback_data='Intel i-7')
        comp2 = telebot.types.InlineKeyboardButton("Intel i-5200, 8GB,512Gb,SSD 128Gb", callback_data='Intel i-5')
        comp3 = telebot.types.InlineKeyboardButton("AMD 9080, 32Gb,SSD 256", callback_data='AMD 9080')
        comp4 = telebot.types.InlineKeyboardButton("AMD 6080, 32Gb,HDD 1024", callback_data='AMD 6080')
        comp5 = telebot.types.InlineKeyboardButton("Intel i-3,integrate video,HDD 512Gb ", callback_data='Intel i-3')
        markup.add(comp1, comp2, comp3, comp4, comp5)
        bot.send_message(message.chat.id,
                     "Выберите какой компьютер",
                     reply_markup=markup)
    else:
        bot.send_message(message.chat.id,
                         "Обратитесь к консультанту")


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'mac':
            bot.send_message(call.message.chat.id, '1050$')
        if call.data == 'dell':
            bot.send_message(call.message.chat.id, '850$')
        if call.data == 'lenovo':
            bot.send_message(call.message.chat.id, '500$')
        if call.data == 'acer':
            bot.send_message(call.message.chat.id, '350$')
        if call.data == 'hp':
            bot.send_message(call.message.chat.id, '150$')
        if call.data == 'Intel i-7':
            bot.send_message(call.message.chat.id, '1100$')
        if call.data == 'Intel i-5':
            bot.send_message(call.message.chat.id, '822$')
        if call.data == 'AMD 9080':
            bot.send_message(call.message.chat.id, '940$')
        if call.data == 'AMD 6080':
            bot.send_message(call.message.chat.id, '760$')
        if call.data == 'Intel i-3':
            bot.send_message(call.message.chat.id, '200$')
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )
bot.polling(none_stop=True)



