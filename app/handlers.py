from app import bot
import requests
import telebot
import config
from database import get_session
from database.worker import get_article, get_last_urls, add_user


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id,
                     'Hello! I am a bot for searching science articles. '
                     'Just use /search <query> command to begin')


def get_articles(response):
    l = []
    for publication in response.json()['data']:
        source = publication['_source']
        result = dict()
        result['authors'] = source['authors']
        result['date'] = source['datePublished']
        result['title'] = source['title']
        result['urls'] = source['urls']
        l.append(result)
    return l


def formulate_text(article):
    return '''Title: {title}
    
authors: {authors}

date: {date}'''.format(title=article.title,
                       authors=article.authors,
                       date=article.date)


def create_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    key_next = telebot.types.InlineKeyboardButton('Next',
                                                  callback_data='next')
    key_get = telebot.types.InlineKeyboardButton('Get sources',
                                                 callback_data='get')
    keyboard.add(key_get)
    keyboard.add(key_next)
    return keyboard


def next_article(chat_id):
    with get_session() as session:
        article = get_article(chat_id, session)
        if article is None:
            bot.send_message(chat_id, text='Sorry, variants ended')
        else:
            bot.send_message(chat_id, text=formulate_text(article),
                             reply_markup=create_keyboard())


@bot.message_handler(commands=['search'])
def handle_search(message):
    query = ' '.join(message.text.split()[1:])
    response = requests.get(config.search_url.format(query=query),
                            params=config.params)
    chat_id = message.chat.id
    if response.json()['data'] is None:
        bot.send_message(chat_id, 'Sorry, nothing found')
    else:
        with get_session() as session:
            add_user(chat_id, get_articles(response), session)
        next_article(chat_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'next':
        next_article(call.message.chat.id)
        bot.answer_callback_query(call.id)
    elif call.data == 'get':
        with get_session() as session:
            bot.send_message(call.message.chat.id,
                             get_last_urls(call.message.chat.id,
                                           session))
        bot.answer_callback_query(call.id)
