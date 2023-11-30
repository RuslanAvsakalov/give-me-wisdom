import telebot
TOKEN = '6957516672:AAHRM6iLoHUxlGA6Rz84bQm-3_ADKKRvx-M'

from telebot import types

bot=telebot.TeleBot(TOKEN)

@bot.message_handlater(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("❤️ Жопка карамельная")
	item1 = types.KeyboardButton("😁 А это я")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Hello friend, {0.first_name}!".format(message.from_user, bot.get
		parse_mode='html', reply_markup=markup)

	@bot.message_handler(content_types=['text'])
	def houhouhou(message):
		if message.chat.type == 'private':
			if message.text == "❤️ Жопка карамельная":
				bot.send_message(message.chat.id, 'https://vk.com/natali_avsakalova')
			elif message.text == "😁 А это я":
				bot.send_message(message.chat.id, 'https://vk.com/avsakalov_rs')
			else:
				bot.send_message(message.chat.id, 'Не знаю, что ответить')

				bot.polling(none_stop=True)
