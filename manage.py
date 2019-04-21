from config import bot_token
import os
from flask import Flask, request
import telebot
from app import bot, init_bot

port = int(os.environ.get('PORT', '8443'))
init_bot(bot_token)
server = Flask(__name__)


@server.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your_heroku_project.com/' + bot_token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
