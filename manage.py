import app
import config
import os

port = int(os.environ.get('PORT', '8443'))


def main():
    app.init_bot(config.bot_token)
    app.bot.set_webhook(
        "https://python-review-test-bot.herokuapp.com/" + config.bot_token)
    app.bot.idle()


if __name__ == '__main__':
    main()
