#!/usr/bin/python3
"""
Lists all states objects from the database htbn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine, select
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    new_state_name = "Louisiana"

    """SQLAlchemy database engine created with pooling & pre-ping"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name
        ),
        pool_pre_ping=True,
    )
    """Establish connection to the database"""
    with engine.connect() as connection:
        query = select(State).where(State.name == new_state_name)
        existing_state = connection.execute(query).fetchone()

        """Iterate over results & display them"""
        if existing_state:
            print(existing_state.id)
        else:
            new_state = State(name=new_statae_name)
            connection.add(new_state)
            connection.flush """Flush to generate the id"""
            print(new_state.id)

    engine.dispose()
