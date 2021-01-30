from datetime import datetime
import sqlite3

def init(dest='support/data.db'):
    conn = sqlite3.connect(dest)
    try:
        conn.execute("CREATE TABLE temp(DTIME TEXT, TEM TEXT)")
        conn.execute("CREATE TABLE pos(DTIME TEXT, BACK TEXT)")
        conn.execute("CREATE TABLE img(JPG BLOB)")
        conn.execute("INSERT INTO img VALUES(?)", (b"abc",))
        conn.commit()
    except:
        pass
    finally:
        conn.close()