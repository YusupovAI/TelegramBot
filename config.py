from json import load

BOT_TOKEN = '873276013:AAFoxZ7sdhU-mSpsB-Hjsz1XkNGUetuhWho'
API_KEY = 'hDmv4CkWbO8TtXUrGaQBPfn2jqcAydMN'
SEARCH_URL = 'https://core.ac.uk:443/api-v2/search/{query}'
PARAMS = {
    'apiKey': API_KEY, 'page': 1, 'pageSize': 100
}
PORT = 5000
HOST = '0.0.0.0'
DB_NAME = 'users.db'


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