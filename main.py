import telebot
import requests
import bs4

from telebot import types

bot = telebot.TeleBot('5112099975:AAF4_2svFifCIPpPMCi0OOm_dqli-gCe1wo')  # Создаем экземпляр бота @Ivanov_Ivan_1MD19_bot

@bot.message_handler (commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Book")
    markup.add(btn1)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text =="Book":
        bot.send_message(message.chat.id, get_book())

def get_book():
    source_url = 'https://readly.ru/books/i_am_lucky/?show=1'
    page = requests.get(source_url)
    soup = bs4.BeautifulSoup(page.text, "html.parser")

    for b in soup.select("h3 > a"):
        book = ("https://readly.ru" + str(b.get('href')))
    return book
# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)
