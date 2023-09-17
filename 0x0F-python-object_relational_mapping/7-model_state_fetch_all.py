#!/sur/bin/python3
"""
Lists all states objects from the database htbn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name), pool_pre_ping=True)

    """Bind the engine to the Base"""
    Base.metadata.create_all(engine)

    """Create a session to interact with the database"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query & list all State objects sorted by id"""
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}:{}".format(state.id, state.name))

    """Close session"""
    session.close()