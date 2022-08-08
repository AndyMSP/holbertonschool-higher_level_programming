#!/usr/bin/python3
"""Lists all states in a database"""

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

    # Perform queries
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    states = cur.fetchall()
    for record in states:
        print(record)

    # Close cursors and databases
    cur.close()
    db.close()

