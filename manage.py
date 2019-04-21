from config import bot_token
import os
from flask import Flask, request
import telebot

bot = telebot.TeleBot(bot_token)
server = Flask(__name__)


@server.route('/' + bot_token, methods=['POST'])
def get_message():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(
        url='https://python-review-test-bot.herokuapp.com')
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
