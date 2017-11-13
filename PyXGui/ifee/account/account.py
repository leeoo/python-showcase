"""
@author: Lex
@version: 1.3, 2014/7/12
"""


class Account:
    def __init__(self):
        self.accountId = None
        self.username = None
        self.password = None
        self.salt = None
        self.passwordHint = None
        self.gender = None
        self.age = None
        self.phoneNo = None
        self.email = None
        self.description = None
        self.creator = None
        self.modifier = None
        self.createTime = None
        self.updateTime = None
        self.accountEnabled = None
        self.accountLocked = None
        self.accountExpired = None
        self.credentialsExpired = None

    def toString(self):
        result = 'accountId: %s, username: %s, password: %s, salt: %s, passwordHint: %s, gender: %s, age: %s, ' \
            'phoneNo: %s, email: %s, description: %s, creator: %s, modifier: %s, createTime: %s, ' \
            'updateTime: %s, accountEnabled: %s, accountLocked: %s, accountExpired: %s, credentialsExpired: %s'\
            % (str(self.accountId), self.username, self.password, self.salt, self.passwordHint, self.gender, self.age,
               self.phoneNo, self.email, self.description, self.creator, self.modifier, self.createTime,
               self.updateTime, self.accountEnabled, self.accountLocked, self.accountExpired, self.credentialsExpired)
        return result

    def toJson(self):
        result = '{%s}' % self.toString()
        text = self.toString()
        fieldPairs = []
        for field in text.split(','):
            for pair in field.split(':'):
                if pair[1].strip() == 'None':
                    pair[1] = ''
        return result
# Test
account = Account()
print(account.toString())
print(account.toJson())
