#!/usr/bin/python3
"""Practice sqlalchemy module"""

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from datetime import datetime

Base = declarative_base()

# connect_string = mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

engine = create_engine('mysql+mysqldb://root2:r@localhost/site', echo = True)

Session = sessionmaker()

class User(Base):
    """Class representing User table"""
    __tablename__ = 'User'
    id = Column(Integer(), primary_key = True)
    username = Column(String(25), nullable = False, unique = True)
    email = Column(String(80), unique = True, nullable = False)

    def __repr__(self):
        return(f"<User username={self.username} email={self.email}>")



# new_user = User(id = 1, username = 'Andy', email = 'Andrew@stoneengineering.net')
