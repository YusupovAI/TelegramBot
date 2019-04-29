from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    article_no = Column(Integer)

    def __init__(self, chat_id):
        self.id = chat_id
        self.article_no = -1


class Article(Base):
    __tablename__ = 'articles'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    article_no = Column(Integer, primary_key=True)
    title = Column(String)
    authors = Column(String)
    date = Column(String)
    urls = Column(String)

    def __init__(self, chat_id, article_no, title, authors, date, urls):
        self.user_id = chat_id
        self.article_no = article_no
        self.title = title
        self.authors = authors
        self.date = date
        self.urls = urls
