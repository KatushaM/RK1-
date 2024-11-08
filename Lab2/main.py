import telebot
from telebot import types
token = '7834644678:AAGKaMnH2b4ehG2d4MdKrL0QvmSoTn5a_Sw'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет!')
@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Ссылка на лк")
    item2 = types.KeyboardButton("Ссылка на лабы")
    item3 = types.KeyboardButton("Ссылка на студ почту")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id,text="Выберите, что вам надо", reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Ссылка на лк":
        bot.send_message(message.chat.id,"https://lks.bmstu.ru/schedule/")
    elif message.text=="Ссылка на лабы":
        bot.send_message(message.chat.id,"https://github.com/ugapanyuk/courses_content/wiki/COURSE_PCPL_MAIN")
    elif message.text=="Ссылка на студ почту":
        bot.send_message(message.chat.id,"https://student.bmstu.ru/?Skin=Samoware")
bot.infinity_polling(none_stop=True)

