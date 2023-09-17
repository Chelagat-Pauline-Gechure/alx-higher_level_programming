#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    sqlQuery = "SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON states.id = cities.state_id \
    WHERE states.name LIKE BINARY %s ORDER BY cities.id"

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=db_name,
        port=3306,
    )
    cursor = db.cursor()

    cursor.execute(sqlQuery)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
