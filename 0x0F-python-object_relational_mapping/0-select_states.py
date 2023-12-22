#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states")
    db_rows = db_cursor.fetchall()
    for row in db_rows:
        print(row)
    db_cursor.close()
    db.close()
