from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey, Table 
from sqlalchemy.orm import  relationship
from main import db

from datetime import datetime 

class users(db.Model):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(String(64))
    display_name = Column(String(64))
    insert_time = Column(DateTime(), default=datetime.now)

    def __init__(self , userid, display_name):
        self.userid = userid
        self.display_name = display_name

    def new_user(self):
        user = db.session.query(users.userid==self.userid).first()
        if not user:
            db.session.add(users(self.userid, self.display_name))
            db.session.commit()
            print("Done!")
        else:
            print ("{} has already existed.".format(self.userid))

    def __repr__(self):
        return '%r' % (self.userid)

steps_tasks_table = Table('steps_tasks', db.Model.metadata,
    Column('steps_id', ForeignKey('steps.uid')),
    Column('tasks_id', ForeignKey('tasks.uid'))
)

class Steps(db.Model):
    __tablename__='steps'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    time_1 = Column(String(12), nullable=False)
    time_2 = Column(String(12), nullable=False)
    is_finished = Column(Boolean, default=False)
    insert_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)
    _tasks_items = relationship(
        'Tasks',
        secondary=steps_tasks_table,
        backref='steps'
    )

class Tasks(db.Model):
    __tablename__='tasks'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    cat_id = Column(Integer, ForeignKey('categorys.uid'))
    category_relationship = relationship('Categorys', backref='tasks')
    name = Column(String(20), nullable=False, unique=True)
    desc = Column(String(150), nullable=False)
    pic = Column(String(50), nullable=False)
    is_finished = Column(Boolean, default=False)
    insert_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)
    _steps_items = relationship(
        'Steps',
        secondary=steps_tasks_table,
        backref='tasks'
    )


    def __init__(self, uid, name, desc, pic, is_finished):
        self.uid = uid
        self.name = name
        self.desc = desc
        self.pic = pic
        self.is_finished = is_finished


class Categorys(db.Model):
    __tablename__='categorys'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    tasks_relationship = relationship('Tasks', backref='categorys')
    insert_time = Column(DateTime, nullable=False, default=datetime.now)
    is_closed = Column(Integer)
    closed_time = Column(DateTime)

    def __init__(self, uid=None, name=None, is_closed=None, closed_time=None):
        self.uid = uid
        self.name = name 
        self.is_closed = is_closed 
        self.closed_time = closed_time 

    def __repr__(self):
        return self.uid

    def select (self):
        cat = Categorys.query.filter(Categorys.name==self.name).first()
        return cat.uid


class Main_tasks(db.Model):
    __tablename__='main_tasks'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    tasks_uid = Column(Integer, ForeignKey('tasks.uid'))
    tasks_relationship = relationship('Tasks', backref='main_tasks')

db.create_all()
