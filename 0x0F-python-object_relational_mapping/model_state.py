#!/usr/bin/python3
"""Define a State class and create a connection to the database.
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an instance of declarative base
Base = declarative_base()

# Define the State class
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    # Create a connection to the MySQL server
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name), pool_pre_ping=True)

    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Perform any additional database operations as needed

    # Close the session
    session.close()
