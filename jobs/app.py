import sqlite3
from flask import Flask, render_template, g

app=Flask(__name__)

PATH='db/jobs.sqlite'


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')


def open_connection():
    connection = getattr(g, '_connection', None)
    if connection is None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection
