"""
@author: Lex
@version: 1.3, 2014/7/12
"""


class Book:
    def __init__(self):
        self.bookId = None
        self.bookChineseName = None
        self.bookEnglishName = None
        self.authorChineseName = None
        self.authorEnglishName = None
        self.bookType = None
        self.bookClass = None
        self.description = None
        self.readingStatus = None
        self.creator = None
        self.modifier = None
        self.createTime = None
        self.updateTime = None

    def toString(self):
        result = 'bookId: %s, bookChineseName: %s, bookEnglishName: %s, authorChineseName: %s, authorEnglishName: %s,' \
                 ' bookType: %s, bookClass: %s, description: %s, readingStatus: %s, creator: %s, modifier: %s, ' \
                 ' createTime: %s, updateTime: %s'\
            % (str(self.bookId), self.bookChineseName, self.bookEnglishName, self.authorChineseName,
               self.authorEnglishName, self.bookType, self.bookClass,
               self.description, self.readingStatus, self.creator, self.modifier, self.createTime, self.updateTime)
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
book = Book()
print(book.toString())
print(book.toJson())
