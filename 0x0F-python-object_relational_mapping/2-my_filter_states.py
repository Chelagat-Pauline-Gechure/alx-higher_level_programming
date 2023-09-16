#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where name matches an argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    name_of_state: str = sys.argv[4]
    host: str = "localhost"
    port: int = 3306
    sql_query = "SELECT * FROM states WHERE name LIKE BINARY\
    '{}' ORDER BY id ASC".format(name_of_state)

    db = MySQLdb.connect(
        user=username,
        host=host,
        port=port,
        password=password,
        database=db_name,
    )
    cursor = db.cursor()

    cursor.execute(sql_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)