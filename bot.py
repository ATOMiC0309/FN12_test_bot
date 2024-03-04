from telebot import TeleBot
from telebot.types import Message
BOT_TOKEN = '7052999075:AAE5goCPc759Y73GOk7eJIp8DyrJop8GpYs'
bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ['start'])
def start(message: Message):
    chat_id = message.chat.id
    chat_f_name = message.chat.first_name
    chat_l_name = message.chat.last_name
    full_name = message.from_user.full_name
    bot.send_message(chat_id, f"Assalomu alaykum, {full_name}")


@bot.message_handler(content_types=['text'])
def reaction_to_message(message: Message):
    chat_id = message.chat.id
    bot.copy_message(chat_id, chat_id, message.message_id)
    bot.reply_to(message, "Salom")

bot.polling(skip_pending=True)

