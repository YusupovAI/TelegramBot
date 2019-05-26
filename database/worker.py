from database.models import User, Article
from sqlalchemy.sql import exists


def add_user(chat_id, articles, session):
    if session.query(exists().where(User.id == chat_id)).scalar():
        session.query(Article).filter_by(user_id=chat_id).delete()
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
    user = session.query(User).filter_by(id=chat_id).one()
    user.article_no += 1
    return session.query(Article).filter_by(user_id=chat_id,
                                            article_no=user.article_no).one()


def get_last_urls(chat_id, session):
    user = session.query(User).filter_by(id=chat_id).one()
    return session.query(Article.urls).filter_by(
        user_id=chat_id, article_no=user.article_no).scalar()
