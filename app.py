from datetime import date, datetime, timedelta
from flask import Flask, request, Response, render_template
from flask_cors import CORS
import sqlite3
from support.db_init import init
import json

init()
app = Flask(__name__)

def getim():
    while True:
        conn=sqlite3.connect("support/data.db")
        a = conn.execute("SELECT * FROM img").fetchall()[0][0]
        conn.close()
        yield(a)

@app.route('/vfeed')
def videof():
    return Response(getim(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def landing():
    return render_template("index.html")

@app.route('/articles')
def article():
    return render_template("articles.html")

@app.route('/statistics')
def stats():
    return render_template("stats.html")

@app.route('/danger', methods=['POST'])
def dange():
    conn=sqlite3.connect("support/data.db")
    a = conn.execute("SELECT * FROM pos ORDER BY DTIME DESC").fetchall()[0][1]
    conn.close()
    if a=="True":
        return "0"
    return "1"

@app.route('/pie', methods=['POST', 'GET'])
def pies():
    conn = sqlite3.connect("support/data.db")
    a=conn.execute("SELECT COUNT(*) FROM pos WHERE BACK=? AND DTIME LIKE ? ORDER BY DTIME", ("False", str(datetime.now())[:10]+"%")).fetchall()[0][0]
    t=conn.execute("SELECT COUNT(*) FROM pos WHERE DTIME LIKE ? ORDER BY DTIME", (str(datetime.now())[:10]+"%",)).fetchall()[0][0]
    conn.close()
    return "%.2f"%(a*100/t)

@app.route('/lnf', methods=['POST', 'GET'])
def lnfs():
    d=date.today()
    td=timedelta(days=1)
    al=list()
    tl=list()
    dl=list()
    conn=sqlite3.connect("support/data.db")
    tot=conn.execute("SELECT COUNT(*) FROM pos").fetchall()[0][0]
    while True:
        al.append(conn.execute("SELECT COUNT(*) FROM pos WHERE BACK=? AND DTIME LIKE ? ORDER BY DTIME", ("False", str(d)+"%")).fetchall()[0][0])
        tl.append(conn.execute("SELECT COUNT(*) FROM pos WHERE DTIME LIKE ? ORDER BY DTIME", (str(d)+"%",)).fetchall()[0][0])
        dl.append(str(d))
        d=d-td
        if sum(tl)>=tot:
            break
    conn.close()
    return json.dumps({'val': [i*100/j for i,j in zip(al, tl)], 'dates': dl})

@app.route('/ltemp', methods=['POST', 'GET'])
def ltemps():
    te=list()
    ti=list()
    conn=sqlite3.connect('support/data.db')
    l=conn.execute("SELECT * FROM temp ORDER BY DTIME").fetchall()
    conn.close()
    return json.dumps({
        'x': [i for i, _ in l],
        'y': [i for _, i in l]
    })
@app.route('/gtemp', methods=['POST', 'GET'])
def gtemps():
    conn=sqlite3.connect('support/data.db')
    a=conn.execute("SELECT TEM FROM temp ORDER BY DTIME DESC").fetchall()[0][0]
    return str(a)

if __name__=="__main__":
    app.run(debug=True)