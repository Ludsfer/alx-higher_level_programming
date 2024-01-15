#!/usr/bin/python3
""" MySQLdb script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa.
Usage:
    ./1-filter.py `user` `password` `database`
"""
import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    db = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    col_count = cur.execute("SELECT * FROM states ORDER BY id")
    table_rows = cur.fetchall()
    for row in table_rows:
        if row[1][0] == 'N':
            print(row)
