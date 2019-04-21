import app
import config


def main():
    app.init_bot(config.bot_token)
    app.bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
