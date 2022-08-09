#!/usr/bin/python3
"""module defines Base class and state class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


# Create declarative_base class
Base = declarative_base()


# Create states class
class state(Base):
    """Definition of states class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
