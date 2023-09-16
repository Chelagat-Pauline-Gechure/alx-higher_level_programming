#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    statement: str = """
    SELECT *
    FROM states
    WHERE BINARY name LIKE 'N%'
    ORDER BY id
    """

    db = MySQLdb.connect(
        user=username,
        host="localhost",
        port=3306,
        password=password,
        database=db_name,
    )
    cursor = db.cursor()

    cursor.execute(statement)

    for row in cursor.fetchall():
        print(row)
