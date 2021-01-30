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

if __name__=="__main__":
    app.run(debug=True)