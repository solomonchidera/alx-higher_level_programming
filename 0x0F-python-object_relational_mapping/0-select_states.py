#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASSWORD = argv[2]
    DATABASE = argv[3]
    db = MySQLdb.connect(host=HOST,
                         port=PORT,
                         user=USER,
                         passwd=PASSWORD,
                         db=DATABASE,
                         charset="utf8")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
