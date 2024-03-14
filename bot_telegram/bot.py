from telebot import TeleBot


BOT_TOKEN = "YOUR API KEY"
bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'Hello'])
def start_message(message):
    bot.reply_to(message, "Hello, how can I help you?")
    
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.infinity_polling()