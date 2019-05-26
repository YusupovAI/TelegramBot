from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    article_no = Column(Integer)

    def __init__(self, chat_id):
        self.id = chat_id
        self.article_no = -1

    def __repr__(self):
        return 'id = {id}, article_no = {no}'.format(id=self.id,
                                                     no=self.article_no)


class Article(Base):
    __tablename__ = 'articles'

    user_id = Column(String, ForeignKey('users.id'), primary_key=True)
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

    def __repr__(self):
        return 'id = {id}, article = {no}'.format(id=self.user_id,
                                                  no=self.article_no)
