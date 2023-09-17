#!/usr/bin/python3
"""
Lists all states objects from the database htbn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """SQLAlchemy database engine created with pooling & pre-ping"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name
        ),
        pool_pre_ping=True,
    )

    """Create a session factory to interact with the DB in an ORM context"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Adding city with a relationship to a state and commit the changes"""
    addState = State(name'California')
    addCity = City(name='San Francisco', state=addState)
    session.add_all([addState, addCity])
    
    session.commit()
    session.close()
