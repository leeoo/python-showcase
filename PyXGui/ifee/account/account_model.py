__author__ = 'Lex'

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime


Base = declarative_base()


class Account(Base):
#     __table__ = account_table
    __tablename__ = 'account'

    # accountId = Column('account_id', Integer, primary_key=True)
    account_id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    salt = Column(String)
    password_hint = Column(String)
    gender = Column(String)
    age = Column(Integer)
    phone_number = Column(String)
    email = Column(String)
    description = Column(String)
    creator = Column(String)
    modifier = Column(String)
    creation_time = Column(DateTime)
    modification_time = Column(DateTime)
    account_enabled = Column(Boolean)
    account_locked = Column(Boolean)
    account_expired = Column(Boolean)
    credentials_expired = Column(Boolean)



# engine = create_engine('postgresql://postgres:postgres@localhost/ifee', echo=False)
#
# # meta = MetaData()
# #
# # meta.reflect(bind=engine)
# # tables = meta.tables
# # print([t for t in tables])
# #
# # account_table = meta.tables['account']
# #
# # print(account_table)
# # print([c.name for c in account_table.columns])
#
#
# Session = sessionmaker(bind=engine)
# session = Session()
# query = session.query(Account)
# print(list(query))
# print(query.first())
# print(query.first().username)
# print(query.first().password)
# print(query.first().credentials_expired)
#
# u = query.get(3)
#
# def getSession():
#     return session
#
#
# # TEST
# ses = getSession()
# query = ses.query(Account)
# print('query -> %s' % query)
# print(type(query))
# print(list(query)[1])
# print(query.all())
# print(len(query.all()))
#
#
#
# def toJson():
#     account = Account()
#     json = {'account_id': 1}

