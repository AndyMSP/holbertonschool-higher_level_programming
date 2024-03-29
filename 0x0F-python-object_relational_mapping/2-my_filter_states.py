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

    # Perform queries
    query = "SELECT * FROM states WHERE name = '{}' \
        ORDER BY states.id ASC".format(match)
    # print(query)
    cur.execute(query)
    states = cur.fetchall()
    for record in states:
        if record[1] == match:
            print(record)

    # Close cursors and databases
    cur.close()
    db.close()
