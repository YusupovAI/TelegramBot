import telebot
from config import bot_token

bot = telebot.TeleBot(bot_token, threaded=True)

from app import handlers
