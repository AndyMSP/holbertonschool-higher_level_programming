#!/usr/bin/python3

from sqlalchemy import create_engine, Integer, Column, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('mysql+mysqldb://root2:r@localhost/practice2', echo=True)

Base = declarative_base()

"""
class User:
    id: int pk
    username: str
    email: str


class Post:
    id: int pk
    title: str
    contents: str
    user_id: int foreignkey
"""

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(40), nullable=False)
    email = Column(String(40), nullable=True)
    posts = relationship('Post', backref='author')

    def __repr__(self):
        return f"<user {self.username}>"


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer(), primary_key=True)
    title = Column(String(45), nullable=False)
    content = Column(String(255), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id'))

    def __repr__(self):
        return f"<user {self.title}>"


Base.metadata.create_all(engine)
session = sessionmaker()(bind=engine)
