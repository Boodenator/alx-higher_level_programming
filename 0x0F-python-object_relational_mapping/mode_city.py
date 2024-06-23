#!/usr/bin/python3
"""Defines a class of a State along with an instance
Base = declarative_base() """

from sqlalchmey import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """ Inheriting city class from Base declarative_base()
    linking the MySQL table states
    Attr:
        id, name
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)
