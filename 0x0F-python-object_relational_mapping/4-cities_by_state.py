#!/usr/bin/python3
"""script that lists all cities from
the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]

    db = MySQLdb.connect(host=HOST,
                         port=PORT,
                         user=USER,
                         passwd=PASS,
                         db=DB,
                         charset="utf8")

    cursor = db.cursor()
    query = " ".join(["SELECT c.id, c.name, st.name",
                      "FROM cities c, states st",
                      "WHERE c.state_id = st.id",
                      "ORDER BY c.id"])

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()

