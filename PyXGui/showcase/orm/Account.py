__author__ = 'Lex'


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime


Base = declarative_base()


class Account(Base):
    # __tablename__ = 'account'
    __tablename__ = 'tf_user'

    account_id = Column(Integer, primary_key=True)

    # id = Column('id', Integer, primary_key=True)
    # user_name = Column('user_name', String(16), unique=True, nullable=False)
    # password = Column('password', String(16), nullable=False)
    # email = Column('email', String(255), unique=True, nullable=False)
    # first_name = Column('first_name', String(255), default='')
    # last_name = Column('last_name', String(255), default='')
    # created = Column('created', DateTime, default=datetime.now)


# engine = create_engine('sqlite:///tutorial.db', echo=True)
engine = create_engine('postgresql://postgres:postgres@localhost/showcase', echo=False)

# TODO
meta = MetaData()
# Reflecting all tables at once
# meta.reflect(bind=engine)
# tables = meta.tables
# print(tables)
#
# users_table = meta.tables['tf_user']
users = Table('tf_user', meta, autoload=True, autoload_with=engine)
print(users)
print([c.name for c in users.columns])
# Session = sessionmaker(bind=engine)
# session = Session()
# query = session.query(Account)
# print(list(query))
# print(query.first().email)