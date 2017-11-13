#!/bin/python
# -*- coding: utf-8 -*-
################################################################################
# author: Lex Li
# version: 1.0
################################################################################


import logging
from account.account_dao import AccountDao
from common.ifee_exception import IfeeException
# from dao.RoleDao import RoleDao
# from dao.AuthorityDao import AuthorityDao
# from dao.ResourceDao import ResourceDao


log = logging.getLogger()


class AccountService():
    account_dao = AccountDao()
    # roleDao = RoleDao()
    # authorityDao = AuthorityDao()
    # resoureceDao = ResourceDao()

    def __init__(self):
        pass

    def list_all(self):
        all_accounts = None
        try:
            log.info('Listing all accounts...')
            all_accounts = self.account_dao.list_all()
        except Exception:
            log.error('Exception listing all accounts!')
        log.info('List all accounts successfully!')
        return all_accounts

    def list(self, search_dict):
        return self.account_dao.list(search_dict)

    def list_4_account_manage_tab(self):
        return self.account_dao.list_4_account_manage_tab()

    def list_4_account_tab_by_username(self, username):
        return self.account_dao.list_4_account_tab_by_username(username)

    def get_by_id(self, account_id):
        return self.account_dao.get_by_id(account_id)

    def get_by_name(self, username):
        return self.account_dao.get_by_id(username)

    def delete_by_id(self, account_id):
        log.info('Deleting account by id: %d' % account_id)
        try:
            self.account_dao.delete_by_id(account_id)
        except Exception as e:
            error_message = 'Failed to delete account by id: %d ' % account_id
            log.error(error_message, e)
            raise IfeeException(error_message)
        log.info('Delete account successfully!')

    def delete_by_name(self, username):
        self.account_dao.delete_by_name(username)