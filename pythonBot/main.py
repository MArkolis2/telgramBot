import telebot
from telebot import types
import config
import feedparser
from requests import get

bot = telebot.TeleBot("5462898315:AAG-1n-ciAmHIzLPdL3_-W9YbPZKUqvTAQ4")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("вопросы и ответы")
    btn3 = types.KeyboardButton("приступить к работе")
    markup.add(btn1, btn2,btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я помогу тебе не пропускать новые выпуски подкастов ваших любимых дикторов".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Поздороваться"):
        bot.send_message(message.chat.id, text="привет я подкаст бот 🗣")

    #кнопки приступить к работе
    if (message.text == "приступить к работе"):
        bot.send_message(message.chat.id, text="хорошо,приступим к работе")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1a = types.KeyboardButton("что такое RSS ссылка")
        btn2b = types.KeyboardButton("где мне её взять ")
        backc = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1a, btn2b, backc)
        bot.send_message(message.chat.id, text="скопируй RSS-ссылку  и пришли её мне", reply_markup=markup)

    elif (message.text == "что такое RSS ссылка"):
        bot.send_message(message.chat.id,  "RSS ссылка нужна для того,чтобы я смог отправлять вам уведомления о новых видео")
    elif (message.text == "где мне её взять"):
        bot.send_photo(message.chat.id, open('photo/podcast_gaid.png', 'rb'))
        bot.send_message(message.chat.id,"RSS ссылку можно найти на странице подкаста")

    # вопросы и ответы
    elif (message.text == "вопросы и ответы"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("описание Podcastbot")
        btn2 = types.KeyboardButton("мои возможности")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2,  back)
        bot.send_message(message.chat.id, text="вопросы и ответы", reply_markup=markup)


    elif (message.text == "описание Podcastbot"):
        bot.send_message(message.chat.id, "Podcastbot  может быть полезен любителям подкастов, которые хотят\nбыть в курсе свежих выпусков без необходимости постоянного мониторинга сайтов или приложений для прослушивания подкастов.")


    elif message.text == "мои возможности":
        bot.send_message(message.chat.id, text="1.оповещать пользователя о новых выпусках подкаста")

    # кнопки для главного меню
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поздороваться")
        button2 = types.KeyboardButton("вопросы и ответы")
        button3 = types.KeyboardButton("приступить к работе")
        markup.add(button1, button2,  button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

bot.polling(none_stop=True)