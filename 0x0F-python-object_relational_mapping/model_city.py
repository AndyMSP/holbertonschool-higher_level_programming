#!/usr/bin/python3
"""Module defines City class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


# Create City class
class City(Base):
    """Definition of City class"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
