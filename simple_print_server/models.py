from sqlalchemy import Column, Integer, String
from simple_print_server.database import Base

import time

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

class PrintedFile(Base):
    __tablename__ = 'printedfiles'
    id = Column(Integer, primary_key=True)
    filename = Column(String(120), unique=False)
    uuid = Column(String(40), unique=True)
    time_printed = Column(String(40), unique=False) # Time string
#    user = None #TODO

    def __init__(self, filename=None, uuid=None):
        self.filename = filename
        self.uuid = uuid
        self.time_printed = time.strftime("%b %d %Y %H:%M:%S")

    def __repr__(self):
        return '<PrintedFile %r>' % (self.uuid)


