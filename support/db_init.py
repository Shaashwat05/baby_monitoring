import sqlite3

def init(dest='data.db'):
    conn = sqlite3.connect(dest)
    try:
        conn.execute("CREATE TABLE pos(DTIME TEXT, BACK TEXT)")
        conn.execute("CREATE TABLE img(JPG TEXT)")
        conn.execute("INSERT INTO img VALUES(?)", ("abc",))
        conn.commit()
        pass
    finally:
        conn.close()
