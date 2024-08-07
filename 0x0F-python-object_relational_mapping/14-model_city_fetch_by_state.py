#!/usr/bin/python3
"""Listing every object from the database
"""
import sys
from mode_city import City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).join(City, State.id == City.state_id).\
        order_by(City.id)
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
