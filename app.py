from flask import Flask, request, Response, render_template
from flask_cors import CORS
import sqlite3

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

if __name__=="__main__":
    app.run(debug=True)