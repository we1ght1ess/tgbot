import telebot

TOKEN = '6169338679:AAGOyjud6ZV3VU-2_tRmhyNC2wabez_OUVU'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который выводид необходимые данные из Excel файла")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
