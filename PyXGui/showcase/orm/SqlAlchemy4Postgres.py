__author__ = 'Lex'

from sqlalchemy.orm import mapper, session, sessionmaker
from datetime import datetime
from sqlalchemy import create_engine, Table, MetaData, Column, ForeignKey, Integer, String, Unicode, DateTime


engine = create_engine('postgresql://postgres:postgres@localhost/showcase', echo=True)
metadata = MetaData() # 跟踪表属性
user_table = Table(
    'tf_user', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_name', Unicode(16), unique=True, nullable=False),
    Column('password', Unicode(16), nullable=False),
    Column('email', Unicode(255), unique=True, nullable=False),
    Column('first_name', Unicode(255), default=''),
    Column('last_name', Unicode(255), default=''),
    Column('created', DateTime, default=datetime.now))

# metadata.create_all(engine)


class User(object):
    pass


mapper(User, user_table)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
# u = User()
# u.user_name = 'test'
# u.email = '测试用户@gmail.com'
# u.password = 'test'
# session.add(u)
#
# session.flush() # 保存数据
# session.commit()


query = session.query(User)
print(list(query))
print(query.get(1))  # 根据主键显示
print(query.filter_by(user_name='test').first())
u = query.filter_by(user_name='test').first()
u.password = 'newpass'
session.commit()
print(query.get(1).password)

for instance in session.query(User).order_by(User.id):
    print(instance.user_name, instance.email)

