#!/usr/bin/python3
"""Script adding State object “Louisiana” to hbtn_0e_6_usa database
"""
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    objects = session.query(State).filter(State.name.contains('%a'))
    for obj in objects:
        session.delete(obj)
    session.commit()
    session.close()
