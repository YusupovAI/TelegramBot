from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from config import DB_NAME

engine = create_engine('sqlite:///' + DB_NAME, echo=True, )
Base = declarative_base()
Session = sessionmaker(bind=engine)


def init_db():
    from database.models import Article, User
    Base.metadata.create_all(engine)


@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
