from json import load

with open('config.json', 'r') as file:
    params = load(file)
    BOT_TOKEN = params['BOT_TOKEN']
    PARAMS = params['PARAMS']
    SEARCH_URL = params['SEARCH_URL']
    HOST = params['HOST']
    PORT = params['PORT']
    DB_NAME = params['DB_NAME']
