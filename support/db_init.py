import sqlite3

def init(dest='support/data.db'):
    conn = sqlite3.connect(dest)
    try:
        conn.execute("CREATE TABLE pos(DTIME TEXT, BACK TEXT)")
        conn.execute("CREATE TABLE img(JPG BLOB)")
        conn.execute("INSERT INTO img VALUES(?)", (b"abc",))
        conn.commit()
    finally:
        conn.close()
init()