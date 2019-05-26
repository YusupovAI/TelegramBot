from json import load

BOT_TOKEN = None
SEARCH_URL = None
PARAMS = None
PORT = None
HOST = None
DB_NAME = None


def init_config():
    global BOT_TOKEN
    global SEARCH_URL
    global PARAMS
    global PORT
    global HOST
    global DB_NAME
    with open('config.json', 'r') as file:
        params = load(file)
        BOT_TOKEN = params['BOT_TOKEN']
        SEARCH_URL = params['SEARCH_URL']
        HOST = params['HOST']
        PORT = params['PORT']
        DB_NAME = params['DB_NAME']
