#!/usr/bin/python3
"""Lists all values from table matching user input"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    MY_HOST = 'localhost'
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    match = sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

    # Create cursor
    cur = db.cursor()

    # print(query)
    cur.execute(
        "SELECT cities.name\
        FROM cities\
        INNER JOIN states\
        ON cities.state_id = states.id\
        WHERE BINARY states.name = %s\
        ORDER BY cities.id ASC;", (match,)
    )
    cities = cur.fetchall()
    cl = [item[0] for item in cities]
    print(*cl, sep=", ")

    # Close cursors and databases
    cur.close()
    db.close()
