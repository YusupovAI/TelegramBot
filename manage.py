import os
from app import bot
from flask import Flask, request
from config import init_config
import telebot
from database import init_db

if __name__ == "__main__":
    init_config()
    from config import BOT_TOKEN, HOST, PORT

    server = Flask(__name__)


    @server.route('/' + BOT_TOKEN, methods=['POST'])
    def get_message():
        bot.process_new_updates(
            [telebot.types.Update.de_json(
                request.stream.read().decode("utf-8"))])
        return "!", 200


    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(
            url='https://python-review-test-bot.herokuapp.com/' + BOT_TOKEN)
        return "!", 200


    init_db()
    server.run(host=HOST, port=int(os.environ.get('PORT', PORT)))
