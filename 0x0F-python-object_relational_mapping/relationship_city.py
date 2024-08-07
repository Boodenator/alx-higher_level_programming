#!/usr/bin/python3
"""Defines the class of a State and an instance
Base = declarative_base() """


from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """Inheritition of city class from Base declarative_base()
    linking the MySQL table states
    Attr:
        id, name
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
