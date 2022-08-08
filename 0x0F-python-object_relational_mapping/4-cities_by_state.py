#!/usr/bin/python3
"""Lists all values from table matching user input"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    MY_HOST = 'localhost'
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

    # Create cursor
    cur = db.cursor()

    cur.execute(
        "SELECT cities.id, cities.name, states.name\
        FROM cities\
        LEFT JOIN states\
        ON cities.state_id = states.id\
        ORDER BY cities.id ASC;"
    )

    cities = cur.fetchall()
    for record in cities:
        print(record)

    # Close cursors and databases
    cur.close()
    db.close()
