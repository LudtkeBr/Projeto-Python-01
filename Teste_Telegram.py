import telebot
import time

bot_token = ''

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])

def send_welcome(message):
    bot.reply_to(message, 'Olá, este é um teste de resposta.')

bot.polling()