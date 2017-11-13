

from peewee import *


database = SqliteDatabase('wee.db')


class Artist(Model):
    name = CharField()

    class Meta:
        database = database


class Album(Model):
    artist = ForeignKeyField(Artist)
    title = CharField()
    release_date = DateTimeField()
    publisher = CharField()
    media_type = CharField()

    class Meta:
        database = database


if __name__ == '__main__':
    try:
        Artist.create_table()
    except OperationalError:
        print('Artist table already exists!')

    try:
        Album.create_table()
    except OperationalError:
        print('Album table already exists!')

