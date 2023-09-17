#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    sqlQuery = "SELECT * FROM cities ORDER BY id ASC"

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
