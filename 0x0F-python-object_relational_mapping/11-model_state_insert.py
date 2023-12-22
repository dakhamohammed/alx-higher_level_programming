#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    add_state = State(name='Louisiana')
    session.add(add_state)
    new_state = session.query(State).filter_by(name='Louisiana').first()
    print(new_state.id)
    session.commit()
