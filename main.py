import telebot
import config
from telebot import types

#TOKEN = "6198242396:AAFyJXZ43AmcjznCCx57hBSxzoC69heUc6c"
#telegram - "https://t.me/competitionAssistant_bot"

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}.\n Я - бот ассистент, созданный для улучшения работы <a href='http://айтикуб.рф/'>It-Куба.</a>"
                     .format(message.from_user, bot.get_me()), parse_mode='html')
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Список команд" , callback_data='list')
    item2 = types.InlineKeyboardButton('It-Куб Узнать больше', callback_data='itcube_menu')
    item3 = types.InlineKeyboardButton('Конкурс "Час земли"', url="http://ит-куб-пенза.ит-колледж.рф/час-земли/")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Что бы вы хотели сделать?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'list':
				bot.send_message(call.message.chat.id, 'lol')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'Бывает 😢')

	except Exception as e:
		print(repr(e))

bot.polling(none_stop=True)