#!/bin/python
################################################################################
# author: Lex Li
# version: 1.0
################################################################################

import logging

'''
TODO
1) Need to add support for pg8000.
2) Support SQLAlchemy & Peewee?
'''

log = logging.getLogger()
# May need to enhance the following import logic...
try:
    import psycopg2 as db_driver
    log.info('Get DB connection via psycopg2 successfully!')
except ImportError as ie:
    log.warning('Failed to get DB connection via psycopg2! Try using pg8000!')
    import pg8000 as db_driver
    log.info('Get DB connection via pg8000 successfully!')


def get_connection(db_name, username, password):
    try:
        connection = db_driver.connect(database=db_name, user=username, password=password)
        log.info('Get DB connection successfully.')
    except Exception as e:
        msg = 'Exception getting DB connection!'
        log.error(msg, e)
        raise RuntimeError(msg, e)
    return connection


def query():
    pass


def save_or_update():
    pass


def delete():
    pass
