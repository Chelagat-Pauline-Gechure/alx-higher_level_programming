#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name_of_state = sys.argv[4]
    sqlQuery = "SELECT name FROM cities WHERE state_id = \
    (SELECT id FROM states WHERE name LIKE BINARY %s) ORDER BY cities.id"

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=db_name,
        port=3306,
    )
    cursor = db.cursor()
    
    cursor.execute(sqlQuery, (name_of_state,))

    cities = cursor.fetchall()
    tuples = ()

    for city in cities:
        tuples += city
    print(*tuples, sep=", ")

    cursor.close()
    db.close()
