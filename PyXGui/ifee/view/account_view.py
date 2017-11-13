__author__ = 'Lex'


class AccountView():
    def __init__(self):
        self.tableWiget

        head = ['#', 'User Name', 'password', 'Gender', 'Age', 'Phone Number',
                'Email', 'Description', 'Creator', 'Modifier', 'Creation Time', 'Modification Time',
                'Account Enabled', 'Account Locked', 'Account Expired', 'Credentials Expired']


class Account():
    def __init__(self):
        self.accountId = None
        self.username = None
        self.password = None
        self.salt = None
        self.passwordHint = None
        self.gender = None
        self.age = None
        self.phoneNumber = None
        self.email = None
        self.description = None
        self.creator = None
        self.modifier = None
        self.creation_time = None
        self.modification_time = None
        self.account_enabled = None
        self.account_locked = None
        self.account_expired = None
        self.credentials_expired = None


class AccountDao():
    def list(self):
        pass

    def get(self, accountId):
        pass

    def get(self, username):
        pass

    def delete(self, accountId):
        pass

    def delete(self, username):
        pass

    def saveOrUpdate(self, account):
        pass