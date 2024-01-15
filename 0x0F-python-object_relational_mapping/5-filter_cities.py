#!/usr/bin/python3
"""MySQLdb script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa.
Usage:
    ./1-filter.py `user` `password` `database` `state name searched`
"""
import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    db = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    col_count = cur.execute(f"SELECT DISTINCT(cities.name), cities.id\
                            FROM `cities` INNER JOIN `states` ON\
                            cities.state_id = (SELECT states.id FROM states\
                            WHERE states.name = '{args[4].split(';')[0]}')\
                            ORDER BY cities.id ASC")
    table_rows = cur.fetchall()
    temp_list = [name[0] for name in table_rows]
    print(", ".join(temp_list))
    cur.close()
    db.close()
