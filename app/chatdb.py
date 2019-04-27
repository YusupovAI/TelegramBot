import shelve
from config import shelve_name


def set_user_articles(chat_id, articles):
    with shelve.open(shelve_name) as storage:
        storage[str(chat_id)] = articles
        storage[str(chat_id) + '_cnt'] = 0


def del_user_articles(chat_id):
    with shelve.open(shelve_name) as storage:
        try:
            del storage[str(chat_id)]
            del storage[str(chat_id) + '_cnt']
        except Exception:
            return None


def get_article_for_user(chat_id):
    with shelve.open(shelve_name) as storage:
        try:
            answer = storage[str(chat_id)][storage[str(chat_id) + '_cnt']]
            storage[str(chat_id) + '_cnt'] += 1
            return answer
        except Exception:
            return None


def get_last_urls(chat_id):
    with shelve.open(shelve_name) as storage:
        try:
            article_no = storage[str(chat_id) + '_cnt'] - 1
            answer = storage[str(chat_id)][article_no]
            return answer['urls']
        except Exception:
            return None
