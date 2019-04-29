from database import User, Article


def add_user(chat_id, articles, session):
    if session.query(User).exists().where(User.id == chat_id):
        session.query(Article).filter_by(Article.user_id == chat_id).delete()
        user = session.query(User).get(chat_id)
        user.article_no = -1
    else:
        user = User(chat_id)
        session.add(user)
    for i, article in enumerate(articles):
        insertion = Article(chat_id, i, article['title'],
                            ', '.join(article['authors']), article['date'],
                            '\n'.join(article['urls']))
        session.add(insertion)


def get_article(chat_id, session):
    user = session.query(User).get(chat_id)
    user.article_no += 1
    return session.query(Article).filter_by(
        Article.user_id == chat_id and Article.article_no == user.article_no)


def get_last_urls(chat_id, session):
    user = session.query(User).get(chat_id)
    return session.query(Article.urls).filter_by(
        Article.user_id == chat_id and Article.article_no == user.article_no)
