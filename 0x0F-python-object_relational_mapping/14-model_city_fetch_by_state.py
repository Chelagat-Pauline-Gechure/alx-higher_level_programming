#!/usr/bin/python3
"""
Lists all states objects from the database htbn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
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

    """Getting cities in the states and commit the changes"""
    results = session.query(City, State).join(State)

    for city, state in results.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
