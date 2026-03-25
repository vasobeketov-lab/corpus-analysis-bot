import telebot

# Initialize the bot with your token
TOKEN = '7655484821:AAH-V6qCSQsKi216uIEMe1hw08mhq4erIx0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to the Corpus Analysis Bot!')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling()
