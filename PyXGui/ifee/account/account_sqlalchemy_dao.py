__author__ = 'Lex'


# from ifee.model.Account import Account
from Account import Account
import CommonDao


class AccountDao:

    session = CommonDao.getSession()

    query = CommonDao.getQueryObj(Account)

    def list(self):
        return AccountDao.query.all()

print(AccountDao.session)
print(AccountDao.query)

accountDao = AccountDao()

accountList = accountDao.list()
print('len -> %s' % len(accountList))
