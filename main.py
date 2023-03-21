import telebot
import config
from telebot import types
import random

# telegram - "https://t.me/competitionAssistant_bot"
# username - @competitionAssistant_bot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('❕ Меню ❕', callback_data='menustart')
    markup.add(item1)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Меню")
    item2 = types.KeyboardButton("Список команд")
    markup1.add(item1, item2)
    bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup1)
    bot.send_message(message.chat.id,"Я - бот ассистент, созданный для улучшения работы <a href='http://айтикуб.рф/'>It-Куба</a>.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['menustart'])
def menustart(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("📜 Список команд 📜", callback_data='list_of_commands')
    item2 = types.InlineKeyboardButton('It-Куб Новости', url='http://айтикуб.рф/news091121')
    item4 = types.InlineKeyboardButton('It-Куб Узнать больше', callback_data='itcube')
    item3 = types.InlineKeyboardButton('It-Куб в вашем городе', callback_data='yourcity')
    item5 = types.InlineKeyboardButton('Информация о боте', callback_data='author')
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, '<b>Главное меню</b>'
                                      '\n● Список команд - выводит на экран все доступные команды.'
                                      '\n● It-куб Новости - показывает последние новости It-Куб.'
                                      '\n● It-Куб в вашем городе - помогает найти центр It-Куб в вашем городе.'
                                      '\n● It-Куб Узнать больше - выводит подробную информацию о It-Куб.'
                                      '\n● Информация о боте - выводит информацию о боте.', reply_markup=markup, parse_mode='html')
@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("📜 Список команд 📜", callback_data='list_of_commands')
    item2 = types.InlineKeyboardButton('It-Куб Новости', url='http://айтикуб.рф/news091121')
    item4 = types.InlineKeyboardButton('It-Куб Узнать больше', callback_data='itcube')
    item3 = types.InlineKeyboardButton('It-Куб в вашем городе', callback_data='yourcity')
    item5 = types.InlineKeyboardButton('Информация о боте', callback_data='author')
    markup.add(item1, item2, item3, item4, item5)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='<b>Главное меню</b>'
                                      '\n● Список команд - выводит на экран все доступные команды.'
                                      '\n● It-куб Новости - показывает последние новости It-Куб.'
                                      '\n● It-Куб в вашем городе - помогает найти центр It-Куб в вашем городе.'
                                      '\n● It-Куб Узнать больше - выводит подробную информацию о It-Куб.'
                                      '\n● Информация о боте - выводит информацию о боте.', reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['author'])
def author(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('⛔ Назад ⛔', callback_data='menu')
    markup.add(item1)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='<b>Информация о боте</b>'
                                      '\nБота создал - Боркин Евгений для конкурса <a href="http://ит-куб-пенза.ит-колледж.рф/час-земли/">"Час земли" от It-Куб Пенза</a>.'
                                      '\n'
                                      '\n<a href="https://github.com/Bebrak/telegram_competition_bot.git">github - https://github.com/Bebrak/telegram_competition_bot.git</a>'
                                      '\n'
                                      '\n<a href="https://drive.google.com/drive/folders/10cYyyyx1-z_qwfn7DQlWZX8wzuQZS_PO?usp=sharing">Гугл диск - https://drive.google.com/drive/folders/10cYyyyx1-z_qwfn7DQlWZX8wzuQZS_PO?usp=sharing</a>'
                                      '\n',reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['itcube'])
def itcube(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("It-Куб Сайт", url='http://айтикуб.рф/')
    item2 = types.InlineKeyboardButton("It-Куб ВКонтакте", url='https://vk.com/itcube_official')
    item3 = types.InlineKeyboardButton('Конкурс "Час земли"', url="http://ит-куб-пенза.ит-колледж.рф/час-земли/")
    item4 = types.InlineKeyboardButton('⛔ Назад ⛔', callback_data='menu')
    markup.add(item1, item2, item3, item4)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='<b>It-Куб</b>'
                                      '\nЭто центр образования детей по программам, направленным на ускоренное освоение актуальных и востребованных знаний, навыков и компетенций в сфере информационных технологий.'
                                      '\nПроект формирует современную образовательную экосистему, объединяющую компании-лидеров ИТ-рынка, опытных наставников и начинающих разработчиков от 7 до 18 лет.'
                                      '\nНа данный момент в программе доступно множество направлений, таких как "Мобильная разработка" и "Программирование роботов".'
                                      '\nЭту и другую информацию вы найдете на официальном сайте It-Куб и в группе ВК.',reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['yourcity'])
def yourcity(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Москва", url='https://vk.com/itcube_official?yandex-source=desktop-maps')
    item2 = types.InlineKeyboardButton("Санкт-Петербург", url='https://vk.com/it_cube_spb')
    item3 = types.InlineKeyboardButton("Новосибирск", url='https://vk.com/public199226159')
    item4 = types.InlineKeyboardButton("Екатеринбург", url='https://vk.com/cube_ekb')
    item5 = types.InlineKeyboardButton("Казань", url='https://vk.com/itcube.kazan')
    item6 = types.InlineKeyboardButton("Нижний Новгород", url='https://vk.com/itcube52')
    item7 = types.InlineKeyboardButton('📜 Список всех центров 📜', url="https://drive.google.com/file/d/1PmQfOHDmavSnG1hj7aIh7Kk1YO_9QU90/view")
    item8 = types.InlineKeyboardButton('🔎 Найти центр в моем городе 🔎', url='https://yandex.ru/maps/?ll=41.441065%2C55.162816&z=5')
    item9 = types.InlineKeyboardButton('⛔ Назад ⛔', callback_data='menu')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='<b>Ваш город</b>'
                                      '\nСейчас в Российской Федерации находится более 150 центров It-Куб.'
                                      '\nПоэтому ниже перечислены лишь некоторые города.', reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['list_of_commands'])
def list_of_commands(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('⛔ Назад ⛔', callback_data='menu')
    markup.add(item1)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='<b>Список команд</b>'
                                      '\n● /menustart - перейти в меню.'
                                      '\n● /start - перейти на приветственный экран.'
                                      '\n● /yourcity - искать центр It-Куб в вашем городе.'
                                      '\n● /itcube - узнать больше о It-Куб.'
                                      '\n● /author - узнать больше о боте.', reply_markup=markup, parse_mode='html')
@bot.message_handler(commands=['list_of_commandsstart'])
def list_of_commandsstart(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('⛔ Назад ⛔', callback_data='menu')
    markup.add(item1)
    bot.send_message(message.chat.id,'<b>Список команд</b>'
                                      '\n● /menustart - перейти в меню.'
                                      '\n● /start - перейти на приветственный экран.'
                                      '\n● /yourcity - искать центр It-Куб в вашем городе.'
                                      '\n● /itcube - узнать больше о It-Куб.'
                                      '\n● /author - узнать больше о боте.', reply_markup=markup, parse_mode='html')
@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.chat.type == 'private':
        if message.text == 'Меню':
            menustart(message)
        elif message.text == 'Список команд':
            list_of_commandsstart(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'list_of_commands':
                list_of_commands(call.message)
            if call.data == 'list_of_commandsstart':
                list_of_commandsstart(call.message)
            elif call.data == 'menu':
                menu(call.message)
            elif call.data == 'itcube':
                itcube(call.message)
            elif call.data == 'author':
                author(call.message)
            elif call.data == 'yourcity':
                yourcity(call.message)
            elif call.data == 'menustart':
                menustart(call.message)

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
