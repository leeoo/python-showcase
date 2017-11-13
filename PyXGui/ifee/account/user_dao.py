#!/bin/python
################################################################################
# author: Lex Li
# version: 1.0
################################################################################

import time
import sqlite3
import common.dbutil4sqlite as dbutil4sqlite


class UserDao:
    def __init__(self):
        self.connection = dbutil4sqlite.get_connection()
        print('DB connection is %s' % type(self.connection))

    def get_user_by_id(self, userId):
        conn = dbutil4sqlite.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM user WHERE id = ?',
            str(userId)
        )
        result = cursor.fetchone()
        # conn.commit()
        cursor.close()
        conn.close()

        return result

    def get_user_by_username(self, username):
        conn = dbutil4sqlite.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM user WHERE username = ?',
            (username,)
        )
        result = cursor.fetchone()
        # conn.commit()
        cursor.close()
        conn.close()

        return result

    def delete_user_by_id(self):
        pass


def create_user_table():
    conn = dbutil4sqlite.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE user( \
            id INTEGER PRIMARY KEY AUTOINCREMENT, \
            username VARCHAR(50) NOT NULL UNIQUE, \
            password VARCHAR(255) NOT NULL, \
            mail_address VARCHAR(50), \
            gender VARCHAR(10), \
            age INTEGER, \
            description VARCHAR(255), \
            creator VARCHAR(50), \
            modifier VARCHAR(50), \
            modification_time TIMESTAMP, \
            modification_time TIMESTAMP \
        )')
    conn.commit()
    cursor.close()
    conn.close()


def drop_user_table():
    try:
        conn = dbutil4sqlite.get_connection()
        cursor = conn.cursor()
        cursor.execute('DROP TABLE user')
        conn.commit()
        cursor.close()
        conn.close()
    except sqlite3.OperationalError:
        print('Database ifee has no table named user.')


def init_user_table():
    conn = dbutil4sqlite.get_connection()
    cursor = conn.cursor()

    for i in range(100):
        username = 'user' + str(i)
        password = username
        mail_address = username + '@gmail.com'
        gender = 'male'
        if i % 2 == 0:
            gender = 'female'
        age = 20
        description = "I'm " + username + "."
        creator = 'apollo'
        create_time = time.time()
        modifier = 'Lex'
        updateTime = time.time()

        row = (username, password, mail_address, gender, age, description, creator, create_time, modifier, updateTime)

        cursor.execute('INSERT INTO user \
            (username, password, mail_address, gender, age, description, creator, modification_time, modifier, modification_time) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)

    conn.commit()
    cursor.close()
    conn.close()


# 如果需要单独执行本模块，需要使用 python -m dao.UserDao 来执行，否则会报 ImportError: No module named 'dao'！
# 单独执行某个包下的的某个模块的方法：
#   先CMD到模块所在包的顶层目录（如本模块所在包的顶层目录是 G:\workshop\Python\PyQt\ifee\dao ）python -m 包名.模块名
def main():
    drop_user_table()
    create_user_table()
    init_user_table()
    user_dao = UserDao()


if __name__ == '__main__':
    main()
