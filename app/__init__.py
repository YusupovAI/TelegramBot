import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN, threaded=True)

from app import handlers
