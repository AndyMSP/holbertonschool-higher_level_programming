#!/usr/bin/python3

from os import stat_result
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey

Base = declarative_base()
engine = create_engine('mysql+mysqldb://root2:r@localhost/practice3', echo = True)
Session = sessionmaker()


class State(Base):
    """Definition of state class"""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False, unique=True)
    cities = relationship('City', back_populates='state', cascade='all, delete')

    def __repr__(self):
        return(f"<State: {self.id} {self.name}>")
    
class City(Base):
    __tablename__ ='cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'))
    state = relationship('State', back_populates='cities')

    def __repr__(self):
        return(f"<City: {self.id} {self.name}>")

Base.metadata.create_all(engine)

session = Session(bind=engine)