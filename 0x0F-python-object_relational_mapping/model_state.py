#!/usr/bin/python3
"""Defines a class of a State with an instance
Base = declarative_base() """


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """Inheritition of state class from Base declarative_base()
    linking the MySQL table states
    Attr:
        id, name
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
