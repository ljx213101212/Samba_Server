from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import config



Base = declarative_base()
#Base.metadata.create_all(bine=engine)

engine = create_engine(config.DATABASEURI)
metadata = MetaData(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()


# User class was only used for testing
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120))

    def __init__(self, id,name=None, email=None):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

studentModule = Table('student_module',
                      Base.metadata,
                      Column('dummy_id',Integer,primary_key=True),
                      Column('stud_dummy_id',Integer,ForeignKey('student.dummy_id')),
                      Column('module_dummy_id',Integer,ForeignKey('module.dummy_id'))
                      )


class Student(Base):
    __tablename__ = 'student'
    dummy_id = Column(Integer,primary_key=True)
    stud_id = Column(String(30),unique=True,nullable=False)
    username = Column(String(50))
    password = Column(String(50))

    moduled = relationship('Module',secondary=studentModule,
                            backref=backref('student', lazy='dynamic'))
    evented = relationship('Event',backref=backref('student'),lazy='dynamic')

    def __init__(self,stud_id,username=None,password=None):
        self.stud_id = stud_id
        self.username = username
        self.password = password

    def __repr__(self):
        return 'This Object Student Id is %r' %(self.stud_id)

class Module(Base):
    __tablename__ = 'module'
    dummy_id = Column(Integer,primary_key=True)
    module_id = Column(String(30),unique=True,nullable=False)
    module_name = Column(String(50))
    mod_details = Column(String(255))

    def __init__(self,module_id,module_name=None,mod_details = None):
        self.module_id = module_id
        self.module_name = module_name
        self.mod_details = mod_details

    def __repr__(self):
        return 'This Object Module Id is %r' %(self.module_id)




class Event(Base):
    __tablename__ = 'event'
    dummy_id = Column(Integer,primary_key=True)
    event_id = Column(String(30),primary_key=True)
    event_name = Column(String(50))
    event_details = Column(String(255))
    event_latitude = Column(String(255))
    event_longitude = Column(String(255))

    stud_id = Column(Integer,ForeignKey('student.dummy_id'))
    def __init__(self,event_id,event_name = None,event_details=None, event_latitude=None,event_longitude=None,
                 stud_id = None):
        self.event_id = event_id
        self.event_name = event_name
        self.event_details = event_details
        self.event_latitude = event_latitude
        self.event_longitude = event_longitude
        self.stud_id = stud_id


    def __repr__(self):
        return 'This Object event Id is %r' %(self.event_id)
