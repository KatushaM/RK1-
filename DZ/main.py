import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import random

API_TOKEN = '7714543480:AAHU2y6IBKNN0YuDL1E4zb45DccdXOTJdW4'


engine = create_engine('sqlite:///dating_bot.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    liked_by = Column(String)
    disliked_by = Column(String)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

bot = telebot.TeleBot(API_TOKEN)



def get_user(telegram_id):
    try:
        return session.query(User).filter_by(telegram_id=str(telegram_id)).one()
    except NoResultFound:
        return None

@bot.message_handler(commands=['start'])
def start(message):
    user = get_user(message.from_user.id)
    if not user:
        bot.send_message(message.chat.id, "Привет! Давай создадим твой профиль. Как тебя зовут?")
        bot.register_next_step_handler(message, handle_first_name)
    else:
        main_menu(message)
        #bot.send_message(message.chat.id, f"Привет, {user.first_name}! Что хочешь сделать? Напиши любое сообщение")

def handle_first_name(message):
    first_name = message.text.strip()
    bot.send_message(message.chat.id, "Отлично! Теперь введи свою фамилию:")
    bot.register_next_step_handler(message, lambda msg: handle_last_name(msg, first_name))

def handle_last_name(message, first_name):
    last_name = message.text.strip()
    bot.send_message(message.chat.id, "И последний шаг - сколько тебе лет?")
    bot.register_next_step_handler(message, lambda msg: handle_age(msg, first_name, last_name))

def handle_age(message, first_name, last_name):
    try:
        age = int(message.text.strip())
        new_user = User(
            telegram_id=str(message.from_user.id),
            first_name=first_name,
            last_name=last_name,
            age=age
        )
        session.add(new_user)
        session.commit()
        bot.send_message(message.chat.id, "Профиль создан успешно!\n")
        bot.send_message(message.chat_id,
            f"Данные сохранены: Имя - {first_name}, Фамилия - {last_name}, Возраст - {age}"
        )
        
        browse_random_profile(message)
    except ValueError:
        bot.send_message(message.chat.id, "Возраст должен быть числом. Попробуй еще раз:")
        bot.register_next_step_handler(message, lambda msg: handle_age(msg, first_name, last_name))


@bot.message_handler(func=lambda m: True)
def main_menu(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 3
    keyboard.add(InlineKeyboardButton("Просмотреть анкеты", callback_data="browse_profiles"))
    keyboard.add(InlineKeyboardButton("Создать новый профиль", callback_data="new_profile"))
    keyboard.add(InlineKeyboardButton("Посмотреть профиль", callback_data="look_profile"))
    bot.send_message(message.chat.id, "Выбери действие:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "browse_profiles":
        browse_random_profile(call.message)
    elif call.data == "new_profile":
        edit_profile(call.message)
    elif call.data == "look_profile":
        bot.send_message(call.chat.id, f"{User.first_name} {User.last_name}, возраст: {User.age}" )

def browse_random_profile(message):
    users = session.query(User).all()
    if len(users) > 0:
        random_user = random.choice([u for u in users if str(u.telegram_id) != str(message.from_user.id)])
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Like", callback_data="like_"),
                   InlineKeyboardButton("Dislike", callback_data="dislike_"),
                   InlineKeyboardButton("Следующая анкета", callback_data="next_profile"))
        bot.send_message(message.chat.id, f"{random_user.first_name} {random_user.last_name}, возраст: {random_user.age}", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "К сожалению, пока нет доступных анкет для просмотра.")

@bot.callback_query_handler(func=lambda call: call.data == "next_profile")
def next_profile_callback(call):
    browse_random_profile(call.message)

@bot.callback_query_handler(func=lambda call: call.data.startswith("like_") or call.data.startswith("dislike_"))
def like_dislike_callback(call):
    action, target_id = call.data.split("_")
    target_user = get_user(target_id)
    current_user = get_user(call.from_user.id)
    if action == "like":
        if target_user is not None:
            target_user.liked_by += f"{current_user.telegram_id},"
            session.commit()
            bot.answer_callback_query(call.id, text="Понравилось!")

            
            browse_random_profile(call.message)
    elif action == "dislike":
        if target_user is not None:
            target_user.disliked_by += f"{current_user.telegram_id},"
            session.commit()
            bot.answer_callback_query(call.id, text="Не понравилось...")

           
            browse_random_profile(call.message)

def edit_profile(message):
    
    start(message)
    pass

if __name__ == '__main__':
    bot.polling(none_stop=True)
