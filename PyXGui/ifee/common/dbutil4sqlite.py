#!/bin/python
################################################################################
# author: Lex Li
# version: 1.0
################################################################################

import sqlite3


#DB_FILE_PATH = 'sqlite/ifee.db'
DB_FILE_PATH = './sqlite/ifee.db'
CONNECTION_POOL_SIZE = 10
CONNECTION_POOL = None


def get_connection():
    return sqlite3.connect(DB_FILE_PATH)

