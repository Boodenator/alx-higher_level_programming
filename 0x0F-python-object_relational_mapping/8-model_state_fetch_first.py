#!/usr/bin/python3
"""Script uses alchemy to list object firts from database
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).first()
    if not states:
        print("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))
