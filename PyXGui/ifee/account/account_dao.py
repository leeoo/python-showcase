#!/bin/python
# -*- coding: utf-8 -*-
################################################################################
# author: Lex Li
# version: 1.0
################################################################################


import logging
import common.dbutil4postgres as dbutil4postgres
from account.account import Account


################################
# 系统中已经有模块dashboardManager先初始化了一个全局的root级别的logging配置，此处可直接获取复用该配置的log对象!
log = logging.getLogger()
################################


class AccountDao:

    def __init__(self):
        pass

    def get_connection(self):
        try:
            conn = dbutil4postgres.get_connection('ifee', 'postgres', 'fuckgfw')
            return conn
        except Exception as e:
            raise e

    def list_all(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT account_id, username, gender, age, phone_number, email, description, creator, modifier, \
                to_char(creation_time, 'yyyy-MM-dd HH:mm:ss'), to_char(modification_time, 'yyyy-MM-dd HH:mm:ss'), account_enabled, account_locked, account_expired, credentials_expired \
            FROM account")
        row_set = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

        # Map sql row set to entities.
        # result = []
        # i = 0
        # for row in row_set:
        #     log.info('row->')
        #     log.info(row)
        #     account = Account()
        #     log.info('----> %s' % account.toString())
        #     account.accountId = row[0]
        #     account.username = row[1]
        #     log.info(account)
        #     result.append(account)
        #     # result[i] = account
        #     # i += 1

        return row_set

    def get_by_id(self, account_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM account WHERE account_id = (%s)", (account_id,))
        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return result

    def get_by_name(self, username):
        conn = None
        try:
            conn = self.get_connection()
        except Exception as e:
            raise e
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM account WHERE username = %s", (username,))
        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return result

    def delete_by_id(self, account_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM account WHERE account_id = %s", (account_id,))
            conn.commit()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def delete_by_name(self, username):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM account WHERE account_id = %s", (username,))
        conn.commit()
        cursor.close()
        conn.close()

    # def saveOrUpdate(self, account):
    #     conn = self.getConnection()
    #     cursor = conn.cursor()
    #     accountId = account.getAccountId()
    #     if accountId is None:
    #         log.info('Save an new account entity!')
    #         cursor.execute(
    #             "INSERT INTO account (username, password, salt, password_hint, gender, age, phone_number, email,"
    #             " description, creator, modifier, creation_time, modification_time, account_enabled, account_locked,"
    #             " account_expired, credentials_expired) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    #             (account.getUsername(), account.getPassword(), account.getSalt(), account.getPasswordHint(), account.getGender(),
    #             account.getAge(), account.getPhoneNo(), account.getEmail(), account.getDescription(), account.getCreator(),
    #             account.getModifier(), account.getCreateTime(), account.getUpdateTime(), account.getAccountEnabled(),
    #             account.getAccountLocked(), account.getAccountExpired(), account.getCredentialsExpired()))
    #     else:
    #         log.info('Update an persisted account entity!')
    #         cursor.execute("UPDATE account SET username=(%s), password=(%s), salt=(%s), password_hint=(%s), gender=(%s), age=(%s), phone_number=(%s), email,"
    #             " description=(%s), creator=(%s), modifier=(%s), creation_time=(%s), modification_time=(%s), account_enabled=(%s), account_locked,"
    #             " account_expired=(%s), credentials_expired WHERE account_id = (%s)",
    #             account.getAge(), account.getPhoneNo(), account.getEmail(), account.getDescription(), account.getCreator(),
    #             account.getModifier(), account.getCreateTime(), account.getUpdateTime(), account.getAccountEnabled(),
    #             account.getAccountLocked(), account.getAccountExpired(), account.getCredentialsExpired(), account.getAccountId())
    #     conn.commit()
    #     cursor.close()
    #     conn.close()

    def save_or_update(self, account):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            account_id = account.accountId
            if account_id is None:
                log.info('Saving a new account entity...')
                cursor.execute(
                    "INSERT INTO account (username, password, salt, password_hint, gender, age, phone_number, email,\
                     description, creator, modifier, creation_time, modification_time, account_enabled, account_locked,\
                     account_expired, credentials_expired) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                     current_timestamp, current_timestamp, %s, %s, %s, %s)",
                    (account.username, account.password, account.salt, account.passwordHint, account.gender,
                     account.age, account.phoneNo, account.email, account.description, account.creator,
                     account.modifier, account.accountEnabled,
                     account.accountLocked, account.accountExpired, account.credentialsExpired))
            else:
                log.info('Update an persisted account entity!')
                cursor.execute(
                        "UPDATE account \
                         SET password=(%s), salt=(%s), password_hint=(%s),gender=(%s), age=(%s), \
                             phone_number=(%s), email=(%s), description=(%s), modifier=(%s),\
                             modification_time=(current_timestamp), account_enabled=(%s), account_locked=(%s), \
                             account_expired=(%s), credentials_expired=(%s) \
                         WHERE account_id = (%s)",
                        (account.password, account.salt, account.passwordHint, account.gender,
                         account.age, account.phoneNo, account.email, account.description, account.modifier,
                         account.accountEnabled, account.accountLocked, account.accountExpired,
                         account.credentialsExpired, account.accountId))
            conn.commit()
            log.info('Save account entity successfully!')
        except Exception as e:
            # TODO
            log.error('Exception saving or updating account! Will rollback DB changes!', e)
            try:
                conn.rollback()
                log.info('Rollback DB changes successfully!')
            except Exception as e2:
                log.error('Rollback DB changes failed!', e2)
            raise Exception('Exception saving or updating account! DB changes rollbacked!')
        finally:
            cursor.close()
            conn.close()

    def list_4_account_manage_tab(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT account_id, username, gender, age, phone_number, email, description, creator, modifier,\
                            to_char(creation_time, 'yyyy-MM-dd HH:mm:ss') AS creation_time, \
                            to_char(modification_time, 'yyyy-MM-dd HH:mm:ss') AS modification_time, \
                            account_enabled, account_locked, account_expired, credentials_expired \
                        FROM account")
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return result

    def list_4_account_tab_by_username(self, username):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT account_id, username, gender, age, phone_number, email, description, creator, modifier,\
                            to_char(creation_time, 'yyyy-MM-dd') AS creation_time, \
                            to_char(modification_time, 'yyyy-MM-dd') AS modification_time, \
                            account_enabled, account_locked, account_expired, credentials_expired \
                        FROM account \
                        WHERE username LIKE %s ", ['%' + username + '%'])
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return result

    def list(self, search_dict):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT account_id, username, gender, age, phone_number, email, description, creator, modifier,\
                            to_char(creation_time, 'yyyy-MM-dd') AS creation_time, \
                            to_char(modification_time, 'yyyy-MM-dd') AS modification_time, \
                            account_enabled, account_locked, account_expired, credentials_expired \
                        FROM account \
                        WHERE \
                            account_id = %s \
                            AND username LIKE %s \
                            AND email LIKE %s \
                            AND phone_number LIKE %s \
                            AND creation_time <= %s",
                       (search_dict['accountId'],
                        '%' + search_dict['username'] + '%',
                        '%' + search_dict['email'] + '%',
                        '%' + search_dict['phoneNo'] + '%',
                        search_dict['registYear']
                        )
                    )
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return result

# conn = psycopg2.connect('dbname=ifee user=postgres password=postgres')
# Should be get from properties file.
# conn = psycopg2.connect(database='ifee', user='postgres', password='postgres')

# conn = DbUtil4Postgres.getConnection('ifee', 'postgres', 'postgres')
#
# cur = conn.cursor()
#
# cur.execute("SELECT * FROM account")

# cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer, data varchar);")

# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

# cur.execute("SELECT * FROM test;")


# account_dao = AccountDao()
# accountList = account_dao.list()
# log.info(accountList)
# log.info(len(accountList))
#
# account = account_dao.getById(-1)
# log.info(account)

