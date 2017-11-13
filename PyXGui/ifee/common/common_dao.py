__author__ = 'Lex'

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime


# Base = declarative_base()

engine = create_engine('postgresql://postgres:postgres@localhost/ifee', echo=False)

# meta = MetaData()
#
# meta.reflect(bind=engine)
# tables = meta.tables
# print([t for t in tables])
#
# account_table = meta.tables['account']
#
# print(account_table)
# print([c.name for c in account_table.columns])

Session = sessionmaker(bind=engine)
__session = Session()


def getSession():
    return __session

def getQueryObj(clazz):
    queryObj = __session.query(clazz)
    return queryObj

