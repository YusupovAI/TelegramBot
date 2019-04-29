from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from sqlalchemy import Column, Integer, String, ForeignKey

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    article_no = Column(Integer)

    def __init__(self, chat_id):
        self.id = chat_id
        self.article_no = -1


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


@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()
