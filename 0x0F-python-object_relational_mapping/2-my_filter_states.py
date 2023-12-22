#!/usr/bin/python3
"""script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                      .format(sys.argv[4]))
    db_rows = db_cursor.fetchall()
    for row in db_rows:
        print(row)
    db_cursor.close()
    db.close()
